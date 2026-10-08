#!/usr/bin/env node
/**
 * LeerMees — export van de volledige rekenbank (G3–G8) naar JSON + CSV + README + zip.
 *
 * Draaien (opnieuw draaien mag altijd; de exportmap wordt telkens opnieuw opgebouwd):
 *   node /workspace/tools/export_bank.js                 # alles, incl. G7 Claude-pilotbestanden
 *   node /workspace/tools/export_bank.js --zonder-pilots # zonder *-claude-pilot.md
 *
 * Alleen-lezen t.o.v. bron: de bank-md, de prototype-code en data.json worden niet aangeraakt.
 * Parsing hergebruikt letterlijk de functies uit leermees-prototype-v1/scripts/build-bank.js
 * (geladen in een vm-sandbox zónder main() te draaien) en de bank-adapter uit mc-shuffle.js.
 * Daarbovenop leest dit script de velden die build-bank laat vallen (Getallenruimte, Context,
 * Visual, Subfocus, UI, Invoer …) en controleert het dat beide parsers dezelfde waarden geven.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { execFileSync } = require('child_process');

// ---------------------------------------------------------------- paden
const WS = '/workspace';
const PROTO = path.join(WS, 'leermees-prototype-v1');
const BUILD_BANK = path.join(PROTO, 'scripts', 'build-bank.js');
const PROTO_DATA = path.join(PROTO, 'bank', 'data.json');
const PROTO_HOLD = path.join(PROTO, 'bank', 'hold.json');
const VISUALS_DIR = path.join(PROTO, 'visuals');
const LEERLIJN = path.join(WS, 'leerlijn');
const SPEC_V3 = path.join(LEERLIJN, 'BORD_STRUCTUUR_V3_SPEC.md');
const GROUPS = [3, 4, 5, 6, 7, 8];
const EXPORTS = path.join(WS, 'exports');
const OUT_NAME = 'leermees-vragenbank-export';
const OUT = path.join(EXPORTS, OUT_NAME);

const ARGS = new Set(process.argv.slice(2));
const INCLUDE_PILOTS = !ARGS.has('--zonder-pilots');

const EXPECTED = { 3: 284, 4: 368, 5: 320, 6: 352, 7: 376, 8: 296 }; // richtgetal uit de opdracht

const DOMAINS = {
  GET: 'Getallen',
  VERH: 'Verhoudingen',
  MEET: 'Meten',
  MKU: 'Meetkunde',
  VBN: 'Verbanden',
  DENK: 'Denken & handelen',
};
const DOMAIN_ORDER = ['GET', 'VERH', 'MEET', 'MKU', 'VBN', 'DENK'];
const PHASE_ORDER = { start: 0, midden: 1, eind: 2 };
const LEVEL_CHILD = { basis: 'Opwarmen', toepassen: 'Oefenen', kritisch: 'Uitdaging' };

function bankDir(g) { return path.join(WS, `rekenen-groep${g}`, 'bank'); }
function rel(p) { return path.relative(WS, p); }
function read(p) { return fs.readFileSync(p, 'utf8'); }

// ---------------------------------------------------------------- hergebruik build-bank.js
function loadBuildBank() {
  const src = read(BUILD_BANK);
  const body = src.replace(/^#!.*\n/, '');
  const noMain = body.replace(/\nmain\(\);\s*$/, '\n');
  if (noMain === body) throw new Error('build-bank.js: slot-aanroep main(); niet gevonden — parser niet veilig te laden');
  const sandbox = {
    require, console, process: { env: {} }, __dirname: path.dirname(BUILD_BANK), __filename: BUILD_BANK,
    module: { exports: {} }, exports: {},
  };
  vm.createContext(sandbox);
  vm.runInContext(
    noMain +
      '\n;this.__api = {};' +
      ['parseMeta', 'parseG3', 'parseG7', 'parseFile', 'fieldMapKey', 'normalizeStatus', 'isApprovedFile', 'listMdOptional',
        'scrapeBoardTitles', 'hasG3Sections', 'parseAcceptSteps', 'DIVISION_INPUT_IDS', 'APPROVED_ONLY_DIRS',
        'G3_DIR', 'G4_DIR', 'G5_DIR', 'G6_DIR', 'G7_DIR', 'G8_DIR', 'BOARD_PATHS']
        .map((n) => `\ntry { this.__api.${n} = ${n}; } catch (e) {}`).join(''),
    sandbox,
    { filename: BUILD_BANK }
  );
  const api = sandbox.__api;
  for (const n of ['parseMeta', 'parseG3', 'parseFile', 'normalizeStatus', 'isApprovedFile', 'listMdOptional', 'scrapeBoardTitles', 'hasG3Sections', 'APPROVED_ONLY_DIRS', 'BOARD_PATHS']) {
    if (api[n] === undefined) throw new Error('build-bank.js: ' + n + ' niet gevonden — parser gewijzigd?');
  }
  if (!api.DIVISION_INPUT_IDS) api.DIVISION_INPUT_IDS = []; // sinds 2026-09-30: alleen de item-vlag Invoer telt
  return api;
}

const BB = loadBuildBank();
const MC = require(path.join(PROTO, 'mc-shuffle.js'));
const VIS = require(path.join(PROTO, 'visuals.js'));

// ---------------------------------------------------------------- anomalieën
const anomalies = [];
function anomaly(ernst, soort, id, bericht) { anomalies.push({ ernst, soort, id, bericht }); }

// ---------------------------------------------------------------- volledige item-parser
const SECTION_RE = /^##\s+(\d{3})\s*·\s*([^\n·]+?)\s*·\s*([^\n]+)\s*$/gm; // zelfde regex als build-bank parseG3

const LABEL_KEYS = {
  'opgave': 'opgave',
  'antwoord': 'antwoord',
  'opties': 'opties',
  'hint': 'hint',
  'sterkere hint': 'sterkereHint',
  'fout-hints': 'foutHints',
  'fout hints': 'foutHints',
  'ouderzin': 'ouderzin',
  'getallenruimte': 'getallenruimte',
  'context': 'context',
  'visual': 'visual',
  'husselen': 'husselen',
  'rekenmachine': 'rekenmachine',
  'invoer': 'invoer',
  'subfocus': 'subfocus',
  'ui': 'ui',
};

function parseItemsFull(text) {
  const items = [];
  const matches = [...text.matchAll(SECTION_RE)];
  for (let i = 0; i < matches.length; i++) {
    const m = matches[i];
    const start = m.index + m[0].length;
    const end = i + 1 < matches.length ? matches[i + 1].index : text.length;
    const body = text.slice(start, end);
    const headParts = m[3].trim().split(/\s*·\s*/);
    const item = { nr: m[1], niveau: m[2].trim(), typeRaw: m[3].trim(), type: headParts[0], kopExtra: headParts.slice(1), velden: {}, labels: [], losseRegels: [] };

    const lines = body.split(/\r?\n/);
    let cur = null;
    let buf = [];
    const flush = () => {
      if (!cur) return;
      const val = buf.join('\n').trim();
      if (Object.prototype.hasOwnProperty.call(item.velden, cur)) item.dubbeleVelden = (item.dubbeleVelden || []).concat(cur);
      item.velden[cur] = val;
      cur = null;
      buf = [];
    };
    for (const line of lines) {
      const fm = line.match(/^- \*\*([^*]+):\*\*\s*(.*)$/);
      if (fm) {
        flush();
        cur = fm[1].trim();
        item.labels.push(cur);
        buf = [fm[2] || ''];
        continue;
      }
      if (line.startsWith('##')) { flush(); break; }
      if (cur && (/^\s{2,}/.test(line) || line.trim() === '')) { buf.push(line.replace(/^\s{2}/, '')); continue; }
      if (cur && line.trim() && !line.startsWith('- **')) { buf.push(line); continue; }
      if (line.trim()) item.losseRegels.push(line);
    }
    flush();
    items.push(item);
  }
  return items;
}

// Kop-meta vóór het eerste item: "Sleutel: waarde" (+ eventuele vervolgregels)
function parseHeaderMeta(text) {
  const firstItem = text.search(/^##\s+\d{3}\s*·/m);
  const head = firstItem >= 0 ? text.slice(0, firstItem) : text;
  const meta = {};
  let key = null;
  for (const line of head.split(/\r?\n/)) {
    if (/^#\s/.test(line)) continue;
    const km = line.match(/^([A-Z][A-Za-z0-9 -]{0,30}):\s*(.*)$/);
    if (km) { key = km[1].trim(); meta[key] = km[2].trim(); continue; }
    if (key && line.trim() && !/^#/.test(line)) meta[key] += '\n' + line.trim();
    else if (!line.trim()) key = null;
  }
  const h1 = text.match(/^#\s+(.+)$/m);
  return { meta, h1: h1 ? h1[1].trim() : '' };
}

// ---------------------------------------------------------------- veld-structuur
function balancedGroups(s, opener) {
  // alle "(opener …)"-groepen met gebalanceerde haakjes → [{inhoud, start, end}]
  const out = [];
  const re = new RegExp('\\(' + opener, 'gi');
  let m;
  while ((m = re.exec(s))) {
    let depth = 0;
    for (let i = m.index; i < s.length; i++) {
      if (s[i] === '(') depth++;
      else if (s[i] === ')') { depth--; if (depth === 0) { out.push({ inhoud: s.slice(m.index + m[0].length, i).trim(), start: m.index, end: i + 1 }); break; } }
    }
  }
  return out;
}

function parseAcceptList(inhoud) {
  let lijst = inhoud;
  let toelichting = null;
  const dash = lijst.search(/\s—\s/);
  if (dash >= 0) { toelichting = lijst.slice(dash + 3).trim(); lijst = lijst.slice(0, dash); }
  const sep = /\s·\s/.test(lijst) ? /\s·\s/ : /\s\/\s/;
  const waarden = lijst.split(sep).map((x) => x.trim()).filter(Boolean);
  return { waarden, toelichting };
}

function parseAnswerChunk(txt) {
  const d = {};
  const acc = balancedGroups(txt, 'accept:');
  if (acc.length) {
    const all = [];
    const toel = [];
    for (const g of acc) { const a = parseAcceptList(g.inhoud); all.push(...a.waarden); if (a.toelichting) toel.push(a.toelichting); }
    d.accept = all;
    if (toel.length) d.acceptToelichting = toel.join(' · ');
  }
  const rub = balancedGroups(txt, 'rubric:');
  if (rub.length) d.rubric = rub.map((g) => g.inhoud).join(' · ');
  return d;
}

function splitSteps(answer) {
  if (!/^1\)\s/.test(answer)) return null;
  const parts = answer.split(/\s·\s(?=\d\)\s)/);
  const steps = [];
  for (let i = 0; i < parts.length; i++) {
    const m = parts[i].match(/^(\d)\)\s*([\s\S]*)$/);
    if (!m || Number(m[1]) !== i + 1) return null;
    steps.push({ stap: i + 1, antwoord: m[2].trim() });
  }
  return steps.length >= 2 ? steps : null;
}

function splitPromptSteps(prompt) {
  const lines = prompt.split('\n');
  const intro = [];
  const steps = [];
  for (const line of lines) {
    const m = line.match(/^\s*(\d)\.\s+(.*)$/);
    if (m && Number(m[1]) === steps.length + 1) { steps.push({ stap: steps.length + 1, tekst: m[2] }); continue; }
    if (steps.length) steps[steps.length - 1].tekst += '\n' + line;
    else intro.push(line);
  }
  if (steps.length < 2) return null;
  steps.forEach((s) => { s.tekst = s.tekst.trim(); });
  return { inleiding: intro.join('\n').trim() || null, stappen: steps };
}

const SENTENCE_START = /^[“"'‘(]?[A-ZÀ-Ý][a-zà-ÿ]/;
function parseFoutHints(raw, isMC) {
  if (!raw) return [];
  // ' · ' scheidt fout-hints, maar staat soms ook in een sleutel ('14 · 14 → …' bij twee vakjes)
  // of in een uitleg. Stuk zonder '→': kort en zonder spatie → hoort bij de volgende sleutel; anders bij de vorige uitleg.
  const segs = [];
  let pending = null;
  for (const s of raw.split(/\s·\s/)) {
    if (/→/.test(s)) { segs.push(pending !== null ? pending + ' · ' + s : s); pending = null; continue; }
    const t = s.trim();
    if (!segs.length || (!/\s/.test(t) && t.length <= 12)) pending = pending !== null ? pending + ' · ' + s : s;
    else segs[segs.length - 1] += ' · ' + s;
  }
  if (pending !== null) { if (segs.length) segs[segs.length - 1] += ' · ' + pending; else segs.push(pending); }
  return segs.map((seg) => {
    const arrows = [...seg.matchAll(/\s*→\s*/g)];
    if (!arrows.length) return { stap: null, fout: null, uitleg: seg.trim(), zekerheid: 'geen sleutel' };
    let cut = null;
    if (isMC && /^\s*[A-H](?:\s*(?:,|\/|of|en)\s*[A-H])*\s*→/.test(seg)) cut = arrows[0];
    if (!cut) cut = arrows.find((a) => SENTENCE_START.test(seg.slice(a.index + a[0].length))) || arrows[arrows.length - 1];
    let sleutel = seg.slice(0, cut.index).trim();
    const uitleg = seg.slice(cut.index + cut[0].length).trim();
    let stap = null;
    const sm = sleutel.match(/^Stap\s*(\d+)\s*→\s*([\s\S]*)$/i);
    if (sm) { stap = Number(sm[1]); sleutel = sm[2].trim(); }
    return { stap, fout: sleutel, uitleg };
  });
}

// ---------------------------------------------------------------- leerlijn-bronnen (titels, fase, nieuw2026)
function stripMd(s) { return String(s || '').replace(/\*\*/g, '').replace(/`/g, '').trim(); }
function normHeader(h) {
  const x = stripMd(h).toLowerCase();
  if (x === 'id') return 'id';
  if (x === 'fase') return 'fase';
  if (x === 'label') return 'label';
  if (x === 'bron') return 'bron';
  if (x.startsWith('korte naam')) return 'korteNaam';
  if (x === 'oude titel') return 'oudeTitel';
  if (x === 'titel' || x === 'nieuwe titel' || x === 'vriendelijke bordtitel' || x === 'bordtitel') return 'titel';
  if (x === 'voorbeeld') return 'voorbeeld';
  if (x === 'nieuw2026') return 'nieuw2026';
  if (x.startsWith('reden') || x === 'toelichting') return 'toelichting';
  return null;
}
function parseGoalTables(file) {
  const rows = {};
  if (!fs.existsSync(file)) return rows;
  const lines = read(file).split(/\r?\n/);
  let headers = null;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (!/^\|/.test(line)) { headers = null; continue; }
    const cells = line.replace(/^\|/, '').replace(/\|\s*$/, '').split('|').map((c) => c.trim());
    if (/^[-:\s|]+$/.test(line)) continue;
    if (!headers) { headers = cells.map(normHeader); continue; }
    const id = stripMd(cells[0]);
    if (!/^G\d-[A-Z]+-[A-Z]?\d{2}$/.test(id)) continue;
    const row = rows[id] || {};
    headers.forEach((h, k) => {
      if (!h || h === 'id') return;
      const v = stripMd(cells[k] || '');
      if (v && row[h] === undefined) row[h] = v;
    });
    rows[id] = row;
  }
  return rows;
}

function leerlijnSources(g) {
  const dir = path.join(LEERLIJN, `rekenen-groep${g}`);
  const L7 = path.join(LEERLIJN, 'rekenen-groep7');
  // prioriteit: eerste bron die een veld heeft wint
  const list = [];
  if (g === 3) {
    list.push(path.join(dir, 'BORDTITELS_V2.md'), path.join(L7, 'SPINE_G3_v1.md'), SPEC_V3);
  } else if (g === 7) {
    list.push(SPEC_V3, path.join(LEERLIJN, 'rekenen-groep3', 'BORDTITELS_V2.md'));
  } else {
    list.push(path.join(dir, `BORDTITELS_G${g}.md`), path.join(dir, `SPINE_G${g}_v1.md`));
  }
  return list.filter((f) => fs.existsSync(f));
}

function leerlijnInfo(g) {
  const merged = {};
  const used = leerlijnSources(g);
  for (const f of used) {
    const rows = parseGoalTables(f);
    for (const [id, row] of Object.entries(rows)) {
      if (!id.startsWith(`G${g}-`)) continue;
      const t = merged[id] || { _bronnen: [] };
      for (const [k, v] of Object.entries(row)) if (t[k] === undefined) t[k] = v;
      t._bronnen.push(rel(f));
      merged[id] = t;
    }
  }
  return { info: merged, bronnen: used.map(rel) };
}

function faseFrom(val, id) {
  const s = String(val || '').toLowerCase();
  if (/midden\s*→\s*eind/.test(s)) return 'eind';
  const m = s.match(/\b(start|midden|eind)\b/);
  if (m) return m[1];
  const p = id.match(/-([KVME])\d{2}$/);
  if (p) return { K: 'start', V: 'start', M: 'midden', E: 'eind' }[p[1]];
  return null;
}

// G3-visuals (statische SVG's per doel) uit VISUALS_G3.md
function goalVisualAssets() {
  const map = {};
  const f = path.join(VISUALS_DIR, 'VISUALS_G3.md');
  if (!fs.existsSync(f)) return map;
  for (const line of read(f).split(/\r?\n/)) {
    if (!/^\|\s*G\d-/.test(line)) continue;
    const cells = line.split('|').map((c) => c.trim());
    const idCell = cells[1];
    const svgs = [...line.matchAll(/`([^`]+\.svg)`/g)].map((m) => m[1]);
    const reuse = [...line.matchAll(/`(\/manipulatieven\/[^`]+\.html)`/g)].map((m) => m[1]);
    const base = idCell.match(/^(G\d-[A-Z]+-)([A-Z]\d{2})((?:\/[A-Z]\d{2})*)$/);
    const ids = base ? [base[1] + base[2], ...base[3].split('/').filter(Boolean).map((x) => base[1] + x)] : [idCell];
    for (const id of ids) map[id] = { svg: svgs, hergebruik: reuse, behoefte: cells[2] || '' };
  }
  return map;
}

// ---------------------------------------------------------------- tijd
function localIso(d) {
  const pad = (n) => String(n).padStart(2, '0');
  const off = -d.getTimezoneOffset();
  const sign = off >= 0 ? '+' : '-';
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}T${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}` +
    `${sign}${pad(Math.floor(Math.abs(off) / 60))}:${pad(Math.abs(off) % 60)}`;
}

// ---------------------------------------------------------------- bord-simulatie (welk bestand staat op het bord?)
function boardPublication(boardTitles) {
  const published = {};
  const skipped = [];
  for (const dir of [BB.G3_DIR, BB.G4_DIR, BB.G5_DIR, BB.G6_DIR, BB.G7_DIR, BB.G8_DIR]) {
    for (const file of BB.listMdOptional(dir)) {
      if (BB.APPROVED_ONLY_DIRS.has(dir) && !BB.isApprovedFile(file)) { skipped.push(file); continue; }
      const entry = BB.parseFile(file, boardTitles);
      if (!entry) continue;
      published[entry.id] = file; // laatste wint, net als data[entry.id] = entry in build-bank
    }
  }
  let held = {};
  if (fs.existsSync(PROTO_HOLD)) held = (JSON.parse(read(PROTO_HOLD)) || {}).hold || {};
  return { published, skipped, held };
}

function sourceType(base) {
  if (/-claude-pilot$/.test(base)) return 'claude-pilot';
  if (/-claude$/.test(base)) return 'claude-live';
  if (/-claude-bijvul\d+$/.test(base)) return 'claude-bijvul-verwijzing';
  return 'canoniek';
}

const BOARD_FIELD_MAP = [
  ['prompt', 'Opgave'], ['answer', 'Antwoord'], ['hint', 'Hint'], ['strongerHint', 'Sterkere hint'],
  ['parentLine', 'Ouderzin'], ['errorHints', 'Fout-hints'],
];

function velden(it, label) {
  // case-ongevoelig opzoeken
  const k = Object.keys(it.velden).find((x) => x.toLowerCase().replace(/\s+/g, ' ') === label.toLowerCase());
  return k === undefined ? undefined : it.velden[k];
}

let svgCount = 0;
function writeSvg(dir, name, svg) {
  fs.mkdirSync(dir, { recursive: true });
  const content = /^<\?xml|^<svg[^>]*xmlns=/.test(svg) ? svg : svg.replace(/^<svg\b(?![^>]*xmlns=)/, '<svg xmlns="http://www.w3.org/2000/svg"');
  fs.writeFileSync(path.join(dir, name), content + '\n', 'utf8');
  svgCount++;
  return 'assets/svg-items/' + name;
}

function buildVisual(itemId, visualRaw, prompt, options) {
  const v = { nodig: null, toelichting: null, asciiSchets: /```/.test(prompt || ''), jsRender: null, svgBestanden: [] };
  if (visualRaw !== undefined) {
    v.nodig = /^ja\b/i.test(visualRaw) ? true : /^nee\b/i.test(visualRaw) ? false : null;
    const t = visualRaw.replace(/^(ja|nee)\b\s*/i, '').trim();
    v.toelichting = t ? t.replace(/^\((.*)\)$/s, '$1') : null;
    if (v.nodig === null) v.waardeRaw = visualRaw;
  }
  const ov = VIS.overrideFor(itemId);
  if (ov) {
    v.jsRender = JSON.parse(JSON.stringify(ov));
    const dir = path.join(OUT, 'assets', 'svg-items');
    try {
      if (ov.type === 'graph' || ov.type === 'pattern') {
        const svg = VIS.figureSvg(itemId);
        if (svg) v.svgBestanden.push(writeSvg(dir, `${itemId}.svg`, svg));
      } else if (ov.type === 'optionNets') {
        for (const o of options || []) {
          const svg = VIS.optionVisualSvg(itemId, o.key, o.text);
          if (svg) v.svgBestanden.push(writeSvg(dir, `${itemId}-optie-${o.key}.svg`, svg));
        }
      } else if (ov.type === 'turf') {
        (ov.marks || []).forEach((mk, k) => {
          const svg = VIS.markSvg(mk, ov.size);
          if (svg) v.svgBestanden.push(writeSvg(dir, `${itemId}-turf-${mk.field}-${k + 1}.svg`, svg));
        });
      }
    } catch (e) {
      anomaly('let op', 'visual-render', itemId, 'SVG renderen mislukt: ' + e.message);
    }
    if (!v.svgBestanden.length) anomaly('let op', 'visual-render', itemId, 'visuals.js heeft een override maar gaf geen SVG');
  }
  return v;
}

function buildItem(ctx, it, boardItem) {
  const { goalId, fileBase, bronType, relFile, opBord } = ctx;
  const itemId = `${fileBase}-${it.nr}`;
  const V = (l) => velden(it, l);
  const opgave = V('Opgave');
  const antwoord = V('Antwoord');
  const optiesRaw = V('Opties');
  const opties = optiesRaw ? MC.optionsFromBank(optiesRaw).map((o) => ({ letter: o.key, tekst: o.text })) : null;
  const isMC = it.type === 'meerkeuze' || (opties && opties.length >= 2);
  const husselRaw = V('Husselen');
  const rekenRaw = V('Rekenmachine');
  const invoerRaw = V('Invoer');

  // --- kernvelden aanwezig?
  for (const lab of ['Opgave', 'Antwoord', 'Hint', 'Sterkere hint', 'Fout-hints', 'Ouderzin']) {
    const val = V(lab);
    if (val === undefined || val === '') {
      const hard = lab === 'Antwoord' || lab === 'Opgave';
      anomaly(hard ? 'fout' : 'let op', 'veld-ontbreekt', itemId, `veld '${lab}' ontbreekt of is leeg`);
    }
  }
  if (it.dubbeleVelden) anomaly('let op', 'veld-dubbel', itemId, `veld(en) dubbel: ${it.dubbeleVelden.join(', ')} (laatste waarde gebruikt, zoals build-bank)`);
  if (it.losseRegels.length) anomaly('let op', 'losse-regels', itemId, `${it.losseRegels.length} regel(s) buiten een veld: ${JSON.stringify(it.losseRegels.slice(0, 2))}`);
  if (optiesRaw && (!opties || opties.length < 2)) anomaly('fout', 'opties-parse', itemId, 'Opties-veld kon niet in A)/B)/… gesplitst worden');
  const bekend = new Set(Object.keys(LABEL_KEYS));
  const onbekend = it.labels.filter((l) => !bekend.has(l.toLowerCase().replace(/\s+/g, ' ')));
  if (onbekend.length) anomaly('let op', 'onbekend-veld', itemId, `onbekend(e) veld(en): ${onbekend.join(', ')} (bewaard onder extraVelden)`);

  // --- pariteit met de bord-parser (build-bank parseG3)
  if (boardItem) {
    for (const [bk, lab] of BOARD_FIELD_MAP) {
      const mine = V(lab) === undefined ? '' : V(lab);
      if ((boardItem[bk] || '') !== mine) anomaly('fout', 'parser-verschil', itemId, `veld '${lab}' wijkt af van build-bank`);
    }
    if ((boardItem.options || null) !== (optiesRaw || null)) anomaly('fout', 'parser-verschil', itemId, "veld 'Opties' wijkt af van build-bank");
    if ((boardItem.shuffle === false) !== (husselRaw !== undefined && /^nee\b/i.test(husselRaw))) anomaly('fout', 'parser-verschil', itemId, "vlag 'Husselen' wijkt af van build-bank");
    if ((boardItem.calculator === true) !== (rekenRaw !== undefined && /^ja\b/i.test(rekenRaw))) anomaly('fout', 'parser-verschil', itemId, "vlag 'Rekenmachine' wijkt af van build-bank");
    const invoerFlag = invoerRaw !== undefined && /÷/.test(invoerRaw) && /:/.test(invoerRaw) && /\//.test(invoerRaw);
    if ((boardItem.divisionInput === true) !== invoerFlag) anomaly('fout', 'parser-verschil', itemId, "vlag 'Invoer' wijkt af van build-bank");
    if (boardItem.level !== it.niveau || boardItem.format !== it.typeRaw) anomaly('fout', 'parser-verschil', itemId, 'kop (niveau/type) wijkt af van build-bank');
  } else {
    anomaly('fout', 'parser-verschil', itemId, 'build-bank vond dit item niet');
  }
  if (husselRaw !== undefined && !/^nee$/i.test(husselRaw.trim())) anomaly('let op', 'vlag-waarde', itemId, `Husselen heeft waarde '${husselRaw}' (alleen 'nee' is geldig)`);
  if (rekenRaw !== undefined && !/^ja$/i.test(rekenRaw.trim())) anomaly('let op', 'vlag-waarde', itemId, `Rekenmachine heeft waarde '${rekenRaw}' (alleen 'ja' is geldig)`);

  // --- antwoord-detail
  const detail = {};
  if (antwoord) {
    const steps = splitSteps(antwoord);
    if (steps) detail.stappen = steps.map((s) => Object.assign({ stap: s.stap, antwoord: s.antwoord }, parseAnswerChunk(s.antwoord)));
    else Object.assign(detail, parseAnswerChunk(antwoord));
    if (isMC && !steps) {
      const km = antwoord.match(/^([A-H])\b/);
      if (km) {
        detail.juisteOptie = km[1];
        const o = (opties || []).find((x) => x.letter === km[1]);
        if (o) detail.juisteOptieTekst = o.tekst;
        else if (opties) anomaly('fout', 'mc-sleutel', itemId, `juiste optie ${km[1]} staat niet in Opties`);
        else anomaly('let op', 'mc-opties-in-opgave', itemId, `meerkeuze zonder Opties-veld; de keuzes staan in de Opgave (sleutel ${km[1]})`);
      } else if (it.type === 'meerkeuze') {
        anomaly('let op', 'mc-sleutel', itemId, `meerkeuze-antwoord begint niet met een optieletter: '${antwoord.slice(0, 60)}'`);
      }
    }
    if (!steps && it.type === 'verslepen' && !/^\s*\(/.test(antwoord)) {
      const parts = antwoord.split(/\s·\s/);
      if (parts.length >= 2 && parts.every((p) => (p.match(/\s→\s/g) || []).length === 1)) {
        detail.koppelingen = parts.map((p) => { const [a, b] = p.split(/\s→\s/); return { van: a.trim(), naar: b.trim() }; });
      }
    }
    if (!steps && it.type === 'ordenen' && /\s→\s/.test(antwoord) && !/\s·\s/.test(antwoord)) {
      detail.volgorde = antwoord.split(/\s→\s/).map((x) => x.trim());
    }
  }

  // --- fout-hints
  const fhRaw = V('Fout-hints');
  const foutHints = parseFoutHints(fhRaw, isMC);
  if (isMC && opties && fhRaw) {
    const letters = new Set(opties.map((o) => o.letter));
    for (const f of foutHints) {
      if (f.stap === null && f.fout && /^[A-H]$/.test(f.fout) && !letters.has(f.fout)) anomaly('let op', 'fout-hint-sleutel', itemId, `fout-hint voor optie ${f.fout} die niet bestaat`);
      if (f.stap === null && f.fout === detail.juisteOptie) anomaly('let op', 'fout-hint-sleutel', itemId, `fout-hint staat op de goede optie ${f.fout}`);
    }
  }
  for (const f of foutHints) if (f.zekerheid) anomaly('let op', 'fout-hint-parse', itemId, `fout-hint zonder '→'-sleutel: '${f.uitleg.slice(0, 60)}'`);

  // --- husselen (bankvlag + wat de app doet volgens mc-shuffle.js planOrder)
  let husselPlan = null;
  if (isMC) {
    const plan = MC.planOrder((opties || []).map((o) => ({ key: o.letter, text: o.tekst })), () => 0.42, {
      shuffle: husselRaw !== undefined && /^nee\b/i.test(husselRaw) ? false : undefined,
      prompt: opgave || '',
      visual: V('Visual') !== undefined && /^ja\b/i.test(V('Visual')),
    });
    husselPlan = {
      appHusselt: /^geschud/.test(plan.reason),
      reden: plan.reason,
      vasteOpties: (opties || []).filter((o, k) => plan.fixed[k]).map((o) => o.letter),
    };
  }

  const deelsom = (invoerRaw !== undefined && /÷/.test(invoerRaw) && /:/.test(invoerRaw) && /\//.test(invoerRaw)) || BB.DIVISION_INPUT_IDS.includes(itemId);
  if (BB.DIVISION_INPUT_IDS.includes(itemId) && invoerRaw === undefined) anomaly('let op', 'invoer', itemId, 'staat op DIVISION_INPUT_IDS in build-bank maar heeft geen Invoer-regel');

  if (deelsom && antwoord && typeof BB.parseAcceptSteps === 'function') {
    const acc = BB.parseAcceptSteps(antwoord);
    if (Object.keys(acc).length) detail.acceptPerStap = acc; // zelfde als data.json acceptSteps
  }
  if (deelsom && antwoord && !/\d\s*:\s*\d/.test(antwoord)) anomaly('let op', 'invoer', itemId, "Invoer-vlag maar het antwoord heeft geen deelsom met ':'");

  const extra = {};
  for (const l of onbekend) extra[l] = it.velden[l];
  const promptSteps = it.type === 'multi' && opgave ? splitPromptSteps(opgave) : null;

  const item = {
    id: itemId,
    nr: it.nr,
    doelId: goalId,
    niveau: it.niveau,
    niveauKind: LEVEL_CHILD[it.niveau] || null,
    type: it.type,
    opgave: opgave === undefined ? null : opgave,
    opgaveStappen: promptSteps,
    opties,
    optiesTekst: optiesRaw === undefined ? null : optiesRaw,
    antwoord: antwoord === undefined ? null : antwoord,
    antwoordDetail: Object.keys(detail).length ? detail : null,
    hint: V('Hint') === undefined ? null : V('Hint'),
    sterkereHint: V('Sterkere hint') === undefined ? null : V('Sterkere hint'),
    foutHints,
    foutHintsTekst: fhRaw === undefined ? null : fhRaw,
    ouderzin: V('Ouderzin') === undefined ? null : V('Ouderzin'),
    getallenruimte: V('Getallenruimte') === undefined ? null : V('Getallenruimte'),
    context: V('Context') === undefined ? null : V('Context'),
    visual: buildVisual(itemId, V('Visual'), opgave, (opties || []).map((o) => ({ key: o.letter, text: o.tekst }))),
    husselen: isMC ? !(husselRaw !== undefined && /^nee\b/i.test(husselRaw)) : null,
    husselPlan,
    rekenmachine: rekenRaw !== undefined && /^ja\b/i.test(rekenRaw),
    deelsomInvoer: deelsom,
    subfocus: V('Subfocus') === undefined ? null : V('Subfocus'),
    ui: V('UI') === undefined ? null : V('UI'),
    bronVariant: null,
    kopExtra: null,
    extraVelden: Object.keys(extra).length ? extra : null,
    bron: { bestand: relFile, type: bronType },
    opBord: opBord,
  };
  const bronPart = it.kopExtra.find((x) => /^bron:/i.test(x));
  if (bronPart) item.bronVariant = bronPart.replace(/^bron:\s*/i, '');
  const rest = it.kopExtra.filter((x) => !/^bron:/i.test(x));
  if (rest.length) item.kopExtra = rest;
  if (bronType === 'claude-pilot' && /÷/.test(JSON.stringify([opgave, antwoord, item.hint, item.sterkereHint, fhRaw, item.ouderzin, optiesRaw]))) {
    anomaly('let op', 'pilot-deelteken', itemId, "bevat '÷' (pilotbestand valt buiten de deelteken-fix van 2026-09-30; niet live)");
  }
  return item;
}

// ---------------------------------------------------------------- hoofdprogramma
function countHeadersDirect(g, withPilots) {
  const dir = bankDir(g);
  let n = 0;
  for (const f of fs.readdirSync(dir).sort()) {
    if (!new RegExp(`^G${g}-.*\\.md$`).test(f)) continue;
    if (!withPilots && /-claude-pilot\.md$/.test(f)) continue;
    n += (read(path.join(dir, f)).match(/^##\s+\d{3}\s*·/gm) || []).length;
  }
  return n;
}

function normPrompt(s) { return String(s || '').replace(/(\d)\.(\d{3})/g, '$1$2').replace(/\s+/g, ' ').trim(); }

function main() {
  const now = new Date();
  const stamp = localIso(now);
  const today = stamp.slice(0, 10);

  fs.rmSync(OUT, { recursive: true, force: true });
  fs.mkdirSync(path.join(OUT, 'assets'), { recursive: true });

  const boardTitles = BB.scrapeBoardTitles(read(BB.BOARD_PATHS[0]));
  const pub = boardPublication(boardTitles);
  for (const f of pub.skipped) anomaly('let op', 'niet-op-bord', path.basename(f, '.md'), 'build-bank publiceert dit bestand niet (geen Didactiek-af + taal: ok)');
  const heldIds = Object.keys(pub.held);
  const goalAssets = goalVisualAssets();
  const protoData = fs.existsSync(PROTO_DATA) ? JSON.parse(read(PROTO_DATA)) : {};

  const groups = [];
  const allItems = [];
  const seenIds = new Map();

  for (const g of GROUPS) {
    const dir = bankDir(g);
    const { info: ll, bronnen: llBronnen } = leerlijnInfo(g);
    const files = fs.readdirSync(dir).filter((f) => new RegExp(`^G${g}-.*\\.md$`).test(f)).sort();
    const goals = {};
    const variants = {};
    const skippedFiles = [];

    for (const f of files) {
      const file = path.join(dir, f);
      const base = path.basename(f, '.md');
      const bronType = sourceType(base);
      if (bronType === 'claude-pilot' && !INCLUDE_PILOTS) { skippedFiles.push({ bestand: rel(file), reden: '--zonder-pilots' }); continue; }
      const text = read(file);
      if (text.includes('\uFFFD')) anomaly('fout', 'utf8', base, 'bronbestand bevat U+FFFD (kapotte tekens)');
      const full = parseItemsFull(text);
      const boardEntry = BB.parseFile(file, boardTitles);
      const { meta, h1 } = parseHeaderMeta(text);
      const bbMeta = BB.parseMeta(text);
      const goalId = bbMeta.id || base;
      if (!full.length) {
        skippedFiles.push({ bestand: rel(file), reden: bronType === 'claude-bijvul-verwijzing' ? 'verwijzing, items staan al in het pilotbestand' : 'geen items (overzicht/stub)' });
        continue;
      }
      if (!BB.hasG3Sections(text)) anomaly('fout', 'formaat', base, 'bestand gebruikt geen "## NNN · niveau · type"-koppen');
      if (bronType === 'canoniek' && goalId !== base) anomaly('let op', 'id', base, `Leerdoel-ID ${goalId} ≠ bestandsnaam`);
      if (!goalId.startsWith(`G${g}-`)) anomaly('fout', 'id', base, `Leerdoel-ID ${goalId} hoort niet bij groep ${g}`);

      const opBord = bronType === 'canoniek' && pub.published[goalId] === file && !heldIds.includes(goalId);
      const ctx = { goalId, fileBase: base, bronType, relFile: rel(file), opBord };
      const boardItems = boardEntry ? boardEntry.items : [];
      if (boardItems.length !== full.length) anomaly('fout', 'parser-verschil', base, `build-bank telt ${boardItems.length} items, export ${full.length}`);
      const items = full.map((it, k) => buildItem(ctx, it, boardItems[k] && boardItems[k].n === it.nr ? boardItems[k] : boardItems.find((b) => b.n === it.nr)));
      // nummering
      items.forEach((it, k) => { if (Number(it.nr) !== k + 1) anomaly('let op', 'nummering', it.id, `volgnummer ${it.nr} op positie ${k + 1}`); });
      for (const it of items) {
        if (seenIds.has(it.id)) anomaly('fout', 'dubbel-id', it.id, `item-ID komt dubbel voor (${seenIds.get(it.id)} en ${rel(file)})`);
        seenIds.set(it.id, rel(file));
      }

      const statusTekst = meta.Status || '';
      const fileInfo = {
        bestand: rel(file), type: bronType, h1, status: BB.normalizeStatus(statusTekst), statusTekst,
        taalOk: /taal:\s*ok\b/i.test(statusTekst), meta, boardEntry, items,
      };
      if (bronType === 'canoniek') {
        if (goals[goalId]) anomaly('fout', 'dubbel-doel', goalId, `twee canonieke bestanden voor ${goalId}`);
        goals[goalId] = fileInfo;
      } else {
        (variants[goalId] = variants[goalId] || []).push(fileInfo);
      }
    }

    // doelen samenstellen (bank ∪ leerlijn)
    const ids = new Set([...Object.keys(goals), ...Object.keys(variants), ...Object.keys(ll)]);
    const goalObjs = [];
    for (const id of ids) {
      const fi = goals[id];
      const L = ll[id] || {};
      const dm = id.match(/^G\d-([A-Z]+)-/);
      const dom = dm ? dm[1] : '?';
      if (!DOMAINS[dom]) anomaly('let op', 'domein', id, `onbekend domein ${dom}`);
      const meta = fi ? fi.meta : {};
      const be = fi ? fi.boardEntry : null;
      let bordtitel = null;
      let bordtitelBron = null;
      if (be) {
        bordtitel = be.title;
        bordtitelBron = be.titleFromBord ? 'bank (Bordtitel:)' : boardTitles[id] ? 'bordpagina (leerlijn-bord.html)' : 'bank (kop #)';
      } else if (L.titel) { bordtitel = L.titel; bordtitelBron = 'leerlijn (' + (L._bronnen || [])[0] + ')'; }
      if (be && L.titel && L.titel !== bordtitel) anomaly('info', 'titel-verschil', id, `bordtitel '${bordtitel}' ≠ leerlijn '${L.titel}'`);
      const fase = faseFrom(L.fase, id);
      if (!L.fase) anomaly('info', 'fase-afgeleid', id, `fase '${fase}' afgeleid uit ID-prefix (niet in leerlijn-tabel)`);
      let nieuw2026 = null;
      if (L.nieuw2026) nieuw2026 = /^ja/i.test(L.nieuw2026) ? true : /^nee/i.test(L.nieuw2026) ? false : null;
      else if (g >= 4 && g !== 7) nieuw2026 = false; // BORDTITELS G4–G6/G8: "alle IDs nee"
      const h1Summary = fi ? (BB.parseMeta(read(path.join(WS, fi.bestand))).summary || null) : null;
      const labelTxt = meta.Label || L.label || null;
      const items = fi ? fi.items : [];
      const lv = { basis: 0, toepassen: 0, kritisch: 0 };
      for (const it of items) if (lv[it.niveau] !== undefined) lv[it.niveau]++;
      const knownMeta = new Set(['Status', 'Bordtitel', 'Bordvoorbeeld', 'Leerdoel-ID', 'Groep', 'Label', 'Notitie']);
      const extraMeta = {};
      for (const [k, v] of Object.entries(meta)) if (!knownMeta.has(k)) extraMeta[k] = v;
      const ga = goalAssets[id];
      const goal = {
        id,
        domein: dom,
        bordtitel,
        bordtitelBron,
        korteNaam: L.korteNaam || L.oudeTitel || null,
        beschrijving: h1Summary,
        voorbeeld: meta.Bordvoorbeeld || L.voorbeeld || null,
        fase,
        nieuw2026,
        label: labelTxt,
        status: fi ? fi.status : null,
        statusTekst: fi ? fi.statusTekst : null,
        taalOk: fi ? fi.taalOk : null,
        notitie: meta.Notitie || null,
        meta: Object.keys(extraMeta).length ? extraMeta : null,
        bronBestand: fi ? fi.bestand : null,
        inBank: !!fi,
        opBord: fi ? items.length > 0 && items[0].opBord : false,
        aantalItems: items.length,
        niveaus: lv,
        visualAssets: ga ? { svg: ga.svg.map((s) => 'assets/svg-doelen/' + s), hergebruikPrototype: ga.hergebruik, behoefte: ga.behoefte } : null,
        items,
        claudeVarianten: (variants[id] || []).map((v) => ({
          bestand: v.bestand, type: v.type, status: v.status, statusTekst: v.statusTekst, taalOk: v.taalOk,
          kop: v.h1, bron: v.meta.Bron || null, opBord: false, aantalItems: v.items.length, items: v.items,
        })),
      };
      if (!fi) anomaly('let op', 'doel-zonder-bank', id, 'staat in de leerlijn maar heeft geen bankbestand (0 items)');
      if (fi && fi.status !== 'Didactiek-af') anomaly('info', 'status', id, `status '${fi.statusTekst}'`);
      if (fi && fi.status === 'Didactiek-af' && !fi.taalOk) anomaly('info', 'status', id, `Didactiek-af zonder 'taal: ok' (${fi.statusTekst})`);
      if (fi && !goal.opBord) anomaly('info', 'niet-op-bord', id, heldIds.includes(id) ? 'vastgehouden in hold.json' : 'build-bank zet dit doel (nog) niet op het bord');
      if (heldIds.includes(id)) goal.vastgehouden = pub.held[id];
      if (goal.visualAssets) for (const s of goal.visualAssets.svg) if (!fs.existsSync(path.join(VISUALS_DIR, path.basename(s)))) anomaly('let op', 'asset', id, `asset ${s} niet gevonden`);

      // Claude-live vs pilot: dubbele inhoud?
      const vs = variants[id] || [];
      const live = vs.filter((v) => v.type === 'claude-live');
      const pil = vs.filter((v) => v.type === 'claude-pilot');
      for (const a of live) for (const b of pil) {
        const same = a.items.filter((x, k) => b.items[k] && normPrompt(x.opgave) === normPrompt(b.items[k].opgave)).length;
        if (same) anomaly('info', 'claude-dubbel', id, `${path.basename(a.bestand)} = ${path.basename(b.bestand)} items 001–${String(a.items.length).padStart(3, '0')} (${same}/${a.items.length} opgaven gelijk, op notatie 1.000/1000 na); beide geëxporteerd`);
      }
      goalObjs.push(goal);
    }

    // structuur groep → domein → doel
    goalObjs.sort((a, b) => (DOMAIN_ORDER.indexOf(a.domein) - DOMAIN_ORDER.indexOf(b.domein)) ||
      ((PHASE_ORDER[a.fase] ?? 9) - (PHASE_ORDER[b.fase] ?? 9)) || a.id.localeCompare(b.id, 'nl', { numeric: true }));
    const domeinen = [];
    for (const code of DOMAIN_ORDER) {
      const gs = goalObjs.filter((x) => x.domein === code);
      if (!gs.length) continue;
      domeinen.push({ code, naam: g === 7 && code === 'MEET' ? 'Meten & meetkunde' : DOMAINS[code], aantalDoelen: gs.length, aantalItems: gs.reduce((n, x) => n + x.aantalItems + x.claudeVarianten.reduce((m, v) => m + v.aantalItems, 0), 0), doelen: gs });
    }
    const other = goalObjs.filter((x) => !DOMAIN_ORDER.includes(x.domein));
    if (other.length) domeinen.push({ code: '?', naam: 'Onbekend', aantalDoelen: other.length, doelen: other });

    const perBron = {};
    let total = 0;
    const groupItems = [];
    for (const goal of goalObjs) {
      const sets = [{ items: goal.items }, ...goal.claudeVarianten];
      for (const s of sets) for (const it of s.items) {
        perBron[it.bron.type] = (perBron[it.bron.type] || 0) + 1; total++;
        groupItems.push({ goal, it });
      }
    }
    const direct = countHeadersDirect(g, INCLUDE_PILOTS);
    if (direct !== total) anomaly('fout', 'telling', `G${g}`, `export ${total} items, directe telling in de bank ${direct}`);
    const goalsWithItems = goalObjs.filter((x) => x.inBank).length;
    groups.push({
      groep: g,
      telling: {
        doelen: goalObjs.length, doelenMetBank: goalsWithItems, items: total, itemsDirectGeteld: direct,
        itemsCanoniek: perBron.canoniek || 0, itemsPerBron: perBron,
        itemsOpBord: groupItems.filter((x) => x.it.opBord).length,
      },
      bronnen: { bank: rel(dir), leerlijn: llBronnen, voortgang: rel(path.join(WS, `rekenen-groep${g}`, 'VOORTGANG.md')), overgeslagen: skippedFiles },
      domeinen,
    });
    allItems.push(...groupItems.map((x) => Object.assign({ groep: g }, x)));

    // vergelijking met prototype data.json (info)
    let diffGoals = 0;
    for (const goal of goalObjs) {
      if (!goal.opBord) continue;
      const pd = protoData[goal.id];
      if (!pd) { diffGoals++; continue; }
      const same = pd.items.length === goal.items.length && pd.items.every((pi, k) => pi.prompt === goal.items[k].opgave && pi.answer === goal.items[k].antwoord &&
        pi.hint === goal.items[k].hint && pi.strongerHint === goal.items[k].sterkereHint && (pi.errorHints || '') === (goal.items[k].foutHintsTekst || '') && (pi.options || null) === (goal.items[k].optiesTekst || null));
      if (!same) diffGoals++;
    }
    if (diffGoals) anomaly('info', 'prototype-data-json', `G${g}`, `${diffGoals} doel(en) wijken af van leermees-prototype-v1/bank/data.json (die is ouder dan de bank; bron = bank-md)`);
  }

  return { stamp, today, groups, allItems, pub };
}

// ---------------------------------------------------------------- schrijven
function csvCell(v) {
  if (v === null || v === undefined) return '';
  const s = typeof v === 'boolean' ? (v ? 'ja' : 'nee') : String(v);
  return /[",\n\r]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
}

function writeJson(file, obj) {
  const s = JSON.stringify(obj, null, 2) + '\n';
  fs.writeFileSync(file, s, 'utf8');
  JSON.parse(read(file)); // valideren
}

function copyAssets() {
  const dst = path.join(OUT, 'assets', 'svg-doelen');
  fs.mkdirSync(dst, { recursive: true });
  const copied = [];
  for (const f of fs.readdirSync(VISUALS_DIR).sort()) {
    if (!f.endsWith('.svg')) continue;
    fs.copyFileSync(path.join(VISUALS_DIR, f), path.join(dst, f));
    copied.push('assets/svg-doelen/' + f);
  }
  const js = path.join(OUT, 'referentie-js');
  fs.mkdirSync(js, { recursive: true });
  for (const f of ['visuals.js', 'mc-shuffle.js', 'order-cards.js']) fs.copyFileSync(path.join(PROTO, f), path.join(js, f));
  return copied;
}

function run() {
  const { stamp, today, groups, allItems, pub } = main();
  const assetsDoel = copyAssets();

  for (const grp of groups) {
    writeJson(path.join(OUT, `vragenbank_g${grp.groep}.json`), Object.assign({
      schema: 'leermees-vragenbank-export/v1', gegenereerdOp: stamp, pilotsMeegenomen: INCLUDE_PILOTS,
    }, grp));
  }
  const telling = {};
  let totaal = 0;
  for (const grp of groups) { telling['G' + grp.groep] = grp.telling; totaal += grp.telling.items; }
  writeJson(path.join(OUT, 'vragenbank_alles.json'), {
    schema: 'leermees-vragenbank-export/v1', gegenereerdOp: stamp, pilotsMeegenomen: INCLUDE_PILOTS,
    totaalItems: totaal, telling, groepen: groups,
  });

  // CSV (één rij per item, hoofdvelden)
  const cols = ['groep', 'domein', 'doel_id', 'bordtitel', 'fase', 'nieuw2026', 'doel_status', 'item_id', 'nr', 'niveau', 'type',
    'opgave', 'opties', 'antwoord', 'juiste_optie', 'accept', 'hints', 'fout_hints', 'ouderzin', 'getallenruimte', 'context',
    'visual', 'husselen', 'rekenmachine', 'deelsom_invoer', 'bron_type', 'op_bord', 'bron_bestand'];
  const rows = [cols.join(',')];
  for (const { groep, goal, it } of allItems) {
    const d = it.antwoordDetail || {};
    const acc = d.accept || (d.stappen ? d.stappen.flatMap((s) => (s.accept || []).map((a) => `${s.stap}) ${a}`)) : []);
    rows.push([
      groep, goal.domein, goal.id, goal.bordtitel, goal.fase, goal.nieuw2026, goal.status, it.id, it.nr, it.niveau, it.type,
      it.opgave, it.opties ? it.opties.map((o) => `${o.letter}) ${o.tekst}`).join(' | ') : '', it.antwoord, d.juisteOptie || '',
      acc.join(' | '), [it.hint, it.sterkereHint].filter(Boolean).join(' | '),
      it.foutHints.map((f) => (f.stap ? `Stap ${f.stap} → ` : '') + (f.fout ? f.fout + ' → ' : '') + f.uitleg).join(' | '),
      it.ouderzin, it.getallenruimte, it.context,
      it.visual.nodig === null ? '' : it.visual.nodig, it.husselen === null ? '' : it.husselen, it.rekenmachine, it.deelsomInvoer,
      it.bron.type, it.opBord, it.bron.bestand,
    ].map(csvCell).join(','));
  }
  fs.writeFileSync(path.join(OUT, 'vragenbank_alles.csv'), rows.join('\n') + '\n', 'utf8');

  // validatie
  const fouten = anomalies.filter((a) => a.ernst === 'fout');
  const utf8Check = ['×', ':', '→', '€', 'ë', '□'].every((ch) => read(path.join(OUT, 'vragenbank_alles.json')).includes(ch));
  const noMissingAnswer = allItems.filter(({ it }) => !it.antwoord).map(({ it }) => it.id);
  const validatie = {
    gegenereerdOp: stamp,
    ok: fouten.length === 0 && noMissingAnswer.length === 0 && utf8Check,
    telling: groups.map((g) => ({ groep: g.groep, doelen: g.telling.doelen, doelenMetBank: g.telling.doelenMetBank, items: g.telling.items,
      directGeteld: g.telling.itemsDirectGeteld, richtgetal: EXPECTED[g.groep], perBron: g.telling.itemsPerBron, opBord: g.telling.itemsOpBord })),
    itemsZonderAntwoord: noMissingAnswer,
    parserFouten: fouten.length,
    utf8TekensAanwezig: utf8Check,
    svgGerenderd: svgCount,
    anomalieenPerErnst: anomalies.reduce((m, a) => { m[a.ernst] = (m[a.ernst] || 0) + 1; return m; }, {}),
    anomalieen: anomalies,
  };
  writeJson(path.join(OUT, 'validatie.json'), validatie);

  fs.writeFileSync(path.join(OUT, 'README.md'), readme({ stamp, groups, totaal, validatie, assetsDoel }), 'utf8');

  // zip
  const zip = path.join(EXPORTS, `${OUT_NAME}_${today}.zip`);
  fs.rmSync(zip, { force: true });
  execFileSync('python3', ['-m', 'zipfile', '-c', zip, OUT_NAME], { cwd: EXPORTS });

  // samenvatting
  console.log(`export → ${OUT}`);
  console.log(`zip    → ${zip}`);
  for (const g of validatie.telling) {
    console.log(`  G${g.groep}: ${g.items} items (direct geteld ${g.directGeteld}, richtgetal ${g.richtgetal}) · ${g.doelen} doelen · ${JSON.stringify(g.perBron)} · op bord ${g.opBord}`);
  }
  console.log(`  totaal ${totaal} items · svg ${svgCount} · anomalieën ${JSON.stringify(validatie.anomalieenPerErnst)}`);
  for (const a of fouten) console.log(`  FOUT ${a.soort} ${a.id}: ${a.bericht}`);
  console.log(validatie.ok ? 'VALIDATIE OK' : 'VALIDATIE MISLUKT');
  if (!validatie.ok) process.exitCode = 1;
}

// ---------------------------------------------------------------- README (Nederlands)
function readme({ stamp, groups, totaal, validatie, assetsDoel }) {
  const B = '`';
  const rowsTelling = groups.map((g) => {
    const t = g.telling;
    const pb = t.itemsPerBron;
    return `| G${g.groep} | ${t.doelen} | ${t.items} | ${pb.canoniek || 0} | ${pb['claude-live'] || 0} | ${pb['claude-pilot'] || 0} | ${t.itemsOpBord} |`;
  }).join('\n');
  const per = validatie.anomalieenPerErnst;
  return `# LeerMees vragenbank — export rekenen groep 3 t/m 8

Gegenereerd: ${stamp} (Europe/Amsterdam) · ${totaal} items · schema ${B}leermees-vragenbank-export/v1${B}

Dit is een **letterlijke export** van de LeerMees-rekenbank (${B}/workspace/rekenen-groepN/bank/GN-*.md${B}). Alle kindteksten zijn Nederlands en staan er precies zoals in de bank; er is niets herschreven. Opnieuw maken (overschrijft deze map en de zip van vandaag):

\`\`\`
node /workspace/tools/export_bank.js                  # alles, incl. G7 Claude-pilotbestanden
node /workspace/tools/export_bank.js --zonder-pilots  # zonder *-claude-pilot.md
\`\`\`

## Bestanden

| Bestand | Inhoud |
|---|---|
| ${B}vragenbank_g3.json${B} … ${B}vragenbank_g8.json${B} | één groep: groep → domeinen → doelen → items |
| ${B}vragenbank_alles.json${B} | alle groepen samen (${B}groepen[]${B}), met tellingen |
| ${B}vragenbank_alles.csv${B} | platte lijst, één rij per item, hoofdvelden; meerdere hints/opties gescheiden door ${B} \\| ${B} |
| ${B}validatie.json${B} | tellingen, controles en de lijst met aandachtspunten (anomalieën) |
| ${B}assets/svg-doelen/${B} | statische SVG-plaatjes per doel (G3-starters uit het prototype) |
| ${B}assets/svg-items/${B} | SVG's die het prototype per item met JavaScript tekent, hier vooraf gerenderd |
| ${B}referentie-js/${B} | referentiecode uit het prototype: ${B}visuals.js${B} (tekeningen), ${B}mc-shuffle.js${B} (husselen), ${B}order-cards.js${B} (ordenen-kaartjes) |

Alle bestanden zijn UTF-8 (zonder BOM). Tekens als × : → € □ ë staan er letterlijk in.

## Tellingen

| Groep | Doelen | Items | Canoniek | Claude-live | Claude-pilot | Op het bord |
|---|---|---|---|---|---|---|
${rowsTelling}

"Op het bord" = items die ${B}build-bank.js${B} nu op het leerlijnbord zet. Elke itemtelling is gecontroleerd tegen een directe telling van de ${B}## NNN ·${B}-koppen in de bankbestanden.

## Opbouw van de JSON

\`\`\`
groep            3..8
telling          aantallen
domeinen[]       code (GET, VERH, MEET, MKU, VBN, DENK), naam
  doelen[]       één leerdoel (tegel op het bord)
    items[]            de oefeningen van dit doel (canonieke bank)
    claudeVarianten[]  alleen G7: parallelle Claude-sets, elk met eigen items[]
\`\`\`

Domeinen: GET Getallen · VERH Verhoudingen · MEET Meten (G7: Meten & meetkunde) · MKU Meetkunde · VBN Verbanden · DENK Denken & handelen (alleen G7). Doelen staan per domein op fase (start → midden → eind) en daarna op ID.

### Velden van een doel

| Veld | Betekenis |
|---|---|
| ${B}id${B} | doel-ID, bv. ${B}G5-GET-M03${B} (G = groep, domein, K/V = start, M = midden, E = eind, nummer). G7 gebruikt ${B}G7-GET-01${B} |
| ${B}domein${B} | domeincode |
| ${B}bordtitel${B} | titel zoals het bord hem toont (bank ${B}Bordtitel:${B}, anders de bordpagina); ${B}bordtitelBron${B} zegt waar hij vandaan komt |
| ${B}korteNaam${B} | vakinhoudelijke korte naam uit de spine/leerlijn |
| ${B}beschrijving${B} | omschrijving uit de kop van het bankbestand |
| ${B}voorbeeld${B} | voorbeeldvraag voor het bord (bank ${B}Bordvoorbeeld:${B} of BORDTITELS) |
| ${B}fase${B} | ${B}start${B} (instroom/onderhoud), ${B}midden${B} (opbouw) of ${B}eind${B} (beheersen) |
| ${B}nieuw2026${B} | ${B}true${B} = badge "nieuw 2026" (G3-VERH-E01, G3-VBN-E03, G7-DENK-01…05); ${B}false${B} = geen badge |
| ${B}label${B} | spinelabel: KLEUTER, VORIG, G5-nieuw, G5-verdieping … |
| ${B}status${B} / ${B}statusTekst${B} / ${B}taalOk${B} | ${B}Didactiek-af${B} of ${B}concept${B}, de volledige statusregel, en of er "taal: ok" in staat |
| ${B}notitie${B} | didactische notitie voor makers (geen kindtekst) |
| ${B}meta${B} | overige kopregels (Bron, Prereq, Doel, KD-ref, Visual-needed, Bron-slug …) |
| ${B}bronBestand${B} | het bankbestand |
| ${B}inBank${B} / ${B}opBord${B} | heeft een bankbestand / staat nu op het bord |
| ${B}aantalItems${B} / ${B}niveaus${B} | aantal items en verdeling basis/toepassen/kritisch |
| ${B}visualAssets${B} | statische plaatjes voor dit doel (zie Visuals) of ${B}null${B} |

### Velden van een item

| Veld | Banklabel | Betekenis |
|---|---|---|
| ${B}id${B} | kop | item-ID = bestandsnaam + nummer, bv. ${B}G3-GET-M01-004${B}; zelfde ID als op het bord. Claude-sets: ${B}G7-GET-01-claude-003${B}, ${B}G7-GET-01-claude-pilot-003${B} |
| ${B}nr${B}, ${B}doelId${B} | kop | volgnummer (${B}"001"${B}) en doel |
| ${B}niveau${B} / ${B}niveauKind${B} | kop | ${B}basis${B} / ${B}toepassen${B} / ${B}kritisch${B}; kindlabel Opwarmen / Oefenen / Uitdaging |
| ${B}type${B} | kop | itemtype, zie hieronder |
| ${B}opgave${B} | Opgave | de vraag (kindtekst). ${B}□${B} = invulvakje; een blok tussen \`\`\` is een ASCII-schets van de tekening |
| ${B}opgaveStappen${B} | Opgave | alleen ${B}multi${B}: ${B}{inleiding, stappen:[{stap, tekst}]}${B} |
| ${B}opties${B} / ${B}optiesTekst${B} | Opties | meerkeuze: ${B}[{letter, tekst}]${B} in bankvolgorde, en de ruwe tekst |
| ${B}antwoord${B} | Antwoord | het goede antwoord, letterlijk. Dit veld is leidend |
| ${B}antwoordDetail${B} | Antwoord | automatisch afgeleid: ${B}juisteOptie${B}/${B}juisteOptieTekst${B} (meerkeuze), ${B}accept${B} (ook goed te rekenen invoer), ${B}acceptToelichting${B} (feedbackzinnen bij een variant), ${B}rubric${B} (nakijkregel voor uitleg), ${B}stappen${B} (multi: per stap), ${B}koppelingen${B} (verslepen: van → naar), ${B}volgorde${B} (ordenen), ${B}acceptPerStap${B} (deelsom-items, zoals ${B}acceptSteps${B} in data.json) |
| ${B}hint${B} | Hint | hint 1 (kindtekst, verklapt het antwoord niet) |
| ${B}sterkereHint${B} | Sterkere hint | hint 2, sterker |
| ${B}foutHints${B} / ${B}foutHintsTekst${B} | Fout-hints | per fout antwoord de denkfout-uitleg: ${B}[{stap, fout, uitleg}]${B}. ${B}fout${B} = de sleutel (optieletter, fout getal, of bij verslepen/ordenen de foute koppeling); ${B}uitleg${B} = kindtekst. Plus de ruwe tekst |
| ${B}ouderzin${B} | Ouderzin | één zin voor de ouder: wat oefent het kind |
| ${B}getallenruimte${B} | Getallenruimte | getalbereik (bv. ${B}0–100${B}) |
| ${B}context${B} | Context | hoeveel verhaal/context: ${B}laag${B} of ${B}midden${B} |
| ${B}visual${B} | Visual | ${B}{nodig, toelichting, asciiSchets, jsRender, svgBestanden}${B}; ${B}nodig: null${B} = geen Visual-regel |
| ${B}husselen${B} | Husselen | meerkeuze: ${B}false${B} bij ${B}Husselen: nee${B}, anders ${B}true${B}; ${B}null${B} bij andere types |
| ${B}husselPlan${B} | – | wat ${B}mc-shuffle.js${B} doet: ${B}appHusselt${B}, ${B}reden${B}, ${B}vasteOpties${B} |
| ${B}rekenmachine${B} | Rekenmachine | ${B}true${B} = eenvoudige rekenmachine tonen (alleen bij ${B}Rekenmachine: ja${B}) |
| ${B}deelsomInvoer${B} | Invoer | ${B}true${B} = kind typt een deelsom; ÷, : en / gelden als hetzelfde deelteken |
| ${B}subfocus${B}, ${B}ui${B} | Subfocus, UI | zeldzame extra's (subthema; UI-aanwijzing) |
| ${B}bronVariant${B} | kop | alleen Claude-sets: oorspronkelijke variant-slug (${B}bron: …${B} in de kop) |
| ${B}extraVelden${B} | – | onbekende labels (nu leeg) |
| ${B}bron${B} | – | ${B}{bestand, type}${B}; type = ${B}canoniek${B}, ${B}claude-live${B} of ${B}claude-pilot${B} |
| ${B}opBord${B} | – | ${B}true${B} als dit item nu op het bord staat |

### Itemtypes (${B}type${B})

| Type | Wat het kind doet |
|---|---|
| ${B}kale${B} | kale som: korte vraag, typt een getal of woord |
| ${B}invullen${B} | vult het vakje □ in een zin of som in (soms meer vakjes: per vakje nakijken) |
| ${B}meerkeuze${B} | kiest één van (meestal) 4 opties; opties worden gehusseld, behalve bij Husselen: nee |
| ${B}verslepen${B} | sleept kaartjes naar vakjes/labels (koppelen). Antwoord ${B}X → Y · …${B}; afleider-kaartjes mogen overblijven |
| ${B}ordenen${B} | zet kaartjes op volgorde. Antwoord ${B}a → b → c${B} |
| ${B}multi${B} | meerstaps (kritisch): 2–3 stappen, per stap nakijken; vaak stap 3 = ja/nee + korte uitleg (rubric) |
| ${B}schattend${B} | schatten: kiest/typt een schatting ("ongeveer 400") |
| ${B}verhaal${B} | alleen in G7-Claude-pilot: verhaaltjessom, typt het antwoord |

### Schrijfwijze in de tekstvelden

- In ${B}antwoord${B} en ${B}foutHintsTekst${B} is ${B} · ${B} de scheider tussen delen (structuur voor de app). In kindtekst staat tussen sommen het woord "en".
- In fout-hints is het stuk vóór ${B}→${B} de sleutel (metadata, mag een optieletter zijn); ná de laatste ${B}→${B} staat de kindtekst. Kindteksten noemen nooit een optieletter, want de opties worden gehusseld.
- ${B}(accept: …)${B} = ook goed te rekenen invoer; ${B}(rubric: …)${B} = nakijkregel voor een uitleg; "canoniek" + "correctiezin" = goed rekenen maar netjes verbeteren.
- ${B}antwoordDetail${B} en ${B}foutHints${B} zijn automatisch afgeleid. Bij twijfel gelden ${B}antwoord${B} en ${B}foutHintsTekst${B}.

## Bron van de items (G7 Claude-bestanden)

- **canoniek**: de gewone bank; staat in ${B}items[]${B}. Gebruik dit voor de website.
- **claude-live** (${B}G7-GET-01-claude.md${B}, ${B}G7-GET-03-claude.md${B}): parallelle Claude-set, in VOORTGANG G7 "live Claude-bestand" genoemd en meegenomen in de fixes van 30-09. Staat níét op het bord (build-bank toont voor hetzelfde doel de canonieke set). In ${B}claudeVarianten[]${B}.
- **claude-pilot** (${B}*-claude-pilot.md${B}): parallelle concept-track ("geen merge zonder Overzicht"); niet op het bord en **niet** meegenomen in de deelteken-fix van 30-09 (sommige bevatten nog ÷). G7-VBN-01/02-pilot zijn concept. In ${B}claudeVarianten[]${B}; weglaten kan met ${B}--zonder-pilots${B}.
- De eerste 8 items van ${B}GET-01/03-claude-pilot${B} zijn (bijna) dezelfde als ${B}GET-01/03-claude${B}.
- Niet geëxporteerd: ${B}G7-VBN.md${B} (overzicht, geen items), ${B}*-claude-bijvulN.md${B} (verwijzingen; items staan al in de pilot), ${B}*.bak-*${B}, ${B}drafts/${B} en ${B}_backup_compact/${B}.

## Visuals

- ${B}Visual: ja${B} = er hoort een tekening bij, en die is een productie-eis vóór live. Het ASCII-blok in de opgave is de schets en de terugval, niet het eindplaatje. Er staan geen antwoorden en geen letters A–D in een plaatje (de opties worden gehusseld).
- ${B}visual.jsRender${B}: bij ${Object.keys(VIS.VISUAL_OVERRIDES).length} items tekent het prototype het plaatje met ${B}referentie-js/visuals.js${B} (turven, grafieken, patronen, bouwplaten). De data staat in ${B}jsRender${B}; de SVG's staan kant-en-klaar in ${B}assets/svg-items/${B} (${B}visual.svgBestanden${B}). Bij turven vervangt de SVG het stuk ASCII uit ${B}jsRender.marks[].ascii${B} in het genoemde veld.
- ${B}assets/svg-doelen/${B} (${assetsDoel.length} bestanden): G3-starterplaatjes per doel; het doel verwijst ernaar via ${B}visualAssets${B}. ${B}hergebruikPrototype${B} verwijst naar een interactieve pagina in het prototype (niet gekopieerd).
- Alle andere items met ${B}Visual: ja${B} hebben nog geen plaatje: de website moet dat tekenen of maken op basis van de opgave en de ${B}toelichting${B}.

## Productieregels

Nagelopen in ${B}rekenen-groepN/VOORTGANG.md${B} (✓ = staat daar; ⚠ = staat daar niet, bron erbij).

1. **Husselen** ✓ (G6, Productie-eisen en Optieletters): de app husselt meerkeuze-opties, behalve bij ${B}Husselen: nee${B} (${B}husselen: false${B}; 14 items: opties hangen aan labels in de tekening). Goed/fout en fout-hints hangen aan de oorspronkelijke letter. Aanvulling uit ${B}mc-shuffle.js${B} (niet in VOORTGANG): ook opties als "even groot"/"allebei", oplopende getallenrijen en opties met letterlabels blijven staan; zie ${B}husselPlan${B}.
2. **Rekenmachine** ✓ (G8, Productie-eisen): een eenvoudige rekenmachine (4 bewerkingen en komma, rekent van links naar rechts, geen haakjes of geheugen), alleen bij ${B}Rekenmachine: ja${B} (G8-GET-E05-001, G8-GET-E05-008, G8-GET-V02-008, G8-VERH-E05-008). Bij een multi-item geldt hij voor alle stappen. De opgave zegt dan ook "Je mag de rekenmachine gebruiken". Open besluit Dave: in de app bouwen of een echte rekenmachine toestaan.
3. **Dubbele punt, verhouding, schaal** ✓ (G8 Deelteken G4–G8 en Keuzes; G7-bankregels): ${B}:${B} betekent "gedeeld door", met een spatie aan beide kanten (${B}12 : 4 = 3${B}); nooit ÷ in kindtekst. Een verhouding staat in woorden ("op elke 2 jongens 3 meisjes"); "1 op de 4" is een deel van een groep. Schaal staat altijd als ${B}schaal 1 : n${B}, met de uitleg "1 cm op de kaart is n cm in het echt"; in een schaalitem is ${B}:${B} nooit een deelteken ("gedeeld door" voluit). Blijven staan: kloktijden (${B}23:40${B}) en labels als "Stap 1:". G3 schrijft geen deelsommen. Typt het kind zelf een deelsom (${B}deelsomInvoer: true${B}), dan gelden ÷, : en / als goed.
4. **Mees-hintflow** ⚠ (niet in VOORTGANG; opgegeven door Dave, past bij "hint-first" en de Hint-knop in ${B}leermees-prototype-v1/PROTOTYPE_STATUS.md${B}). Na een fout antwoord: ${B}hint${B} → opnieuw proberen → ${B}sterkereHint${B} → opnieuw proberen → de denkfout-uitleg (${B}foutHints${B}-regel waarvan ${B}fout${B} past bij het gegeven antwoord; zonder passende sleutel een algemene zin) met het goede ${B}antwoord${B} → door naar de volgende vraag. Daarnaast is er altijd een vrijwillige Hint-knop (toont eerst ${B}hint${B}, daarna ${B}sterkereHint${B}, nooit het antwoord). De bank heeft geen apart veld "denkfout-uitleg": dat zijn de fout-hints.
5. **Lettertype** ✓ (G8, Productie-eisen, Lettertype symmetrie): een schreefloos lettertype waarin S en Z echt puntsymmetrisch zijn en H, T, O en V echt lijnsymmetrisch (G8-MKU-V01-007/008, G8-MKU-E03-005/007). Ook (G6): letter A schreefloos, kleine l niet gelijk aan 1 ("1,5 l").
6. **Tekendoelen** ⚠ (niet in VOORTGANG; wel in de bank-notities van G6-VBN-E03 "'Tekenen' is in de app vertaald naar kiezen en slepen van lijnvormen (productie: eventueel later een tekenvak)" en G6-MKU-E02 "'ontwerpen' vertaald naar kiezen, aanvullen en slepen"): symmetrie, vlakvulling en een lijngrafiek tekenen zijn voorlopig kiezen of slepen; later is een tekenvak nodig.

Overige regels uit VOORTGANG:

7. **Plaatjes** (G4, G6, G8): ${B}Visual: ja${B} = productie-eis vóór live; geen antwoordlabels en geen letters A–D in beeld; kleuren ook met patroon of letter (kleurenblind). Blocker: G8-MKU-E02-005 niet live zonder de vier bouwplaten.
8. **Invoer tolerant** (G6, G8): grote getallen met punt, spatie of zonder scheiding (46.000 · 46000 · 46 000); temperatuur met − of -; kloktijd 9.00 · 9 · 09.00 · 9 uur; woordantwoorden volgens ${B}accept${B}; getalwoorden spelling-tolerant.
9. **Nakijken** (G6, G8): multi per stap; ja/nee automatisch, de uitleg via de ${B}rubric${B} (kernwoorden), nooit blokkeren op de uitleg alleen; meerdere vakjes per vakje nakijken met een fout-hint per vakje; accept-varianten met een feedbackzin goed rekenen; doorwerkfout bij G8-GET-V02-008 stap 2.
10. **Verslepen** (G6): afleider-kaartjes mogen overblijven; fout-hints alleen op bestaande kaartjes, anders een algemene hint; veel kaartjes op mobiel in 2 rijen van 4 zonder scrollen.
11. **Typografie en notatie** (G6, G8): gemengde getallen getypografeerd of met vaste spatie (nooit afbreken tussen 1 en 1/3); breukkaartjes met echte breukstreep; verhoudingstabel als echte tabel; hele getallen van 4 cijfers zonder punt, vanaf 10.000 met punt; Nederlandse komma.
12. **Live en volgorde**: build-bank zet G6 en G8 alleen op het bord met ${B}Didactiek-af${B} + ${B}taal: ok${B}; G6-GET-M05/M06 vóór of samen met G6-GET-E04/E06; G8-MEET-V01 vóór G8-MEET-E01. G3-K-doelen zijn instroom-diagnostiek: 4 items (2 basis, 1 toepassen, 1 kritisch), geen mastery.

## Controle (deze run)

- Items per groep = directe telling van de koppen in de bank: ${validatie.telling.every((t) => t.items === t.directGeteld) ? 'ja, overal gelijk' : 'NEE, zie validatie.json'}.
- Items zonder antwoord: ${validatie.itemsZonderAntwoord.length}. Parserfouten: ${validatie.parserFouten}. Elk veld is ook vergeleken met de parser van het bord (${B}build-bank.js${B}): ${validatie.parserFouten === 0 ? 'geen verschillen' : 'zie validatie.json'}.
- Aandachtspunten: ${Object.entries(per).map(([k, v]) => `${v} × ${k}`).join(' · ') || 'geen'}. De volledige lijst staat in ${B}validatie.json${B} (${B}anomalieen${B}); er is geen item weggelaten.
`;
}

run();
