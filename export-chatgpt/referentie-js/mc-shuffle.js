/**
 * LeerMees — meerkeuze-opties schudden (kind-oefenscherm).
 *
 * Identiteit = de oorspronkelijke optie-sleutel uit de bank (o.key, bv. "A").
 * Goed/fout en fout-hints blijven aan die sleutel hangen; alleen de volgorde
 * op het scherm en de getoonde letters (A, B, C, D) veranderen.
 *
 * Vaste opties (regel):
 *  1. Meta-opties blijven op hun plek: "even groot/evenveel/gelijk", "allebei",
 *     "beide(n)", "geen van beide(n)", "alle(maal/drie …)", "weet ik niet",
 *     "dat kun je niet zeggen/vergelijken", "onmogelijk te zeggen".
 *     (Alleen als de optie daarmee begint; "Ja, want … allebei …" schudt gewoon.)
 *  2. Hele set in bankvolgorde als:
 *     a. alle opties getallen zijn (zelfde eenheid) in oplopende of aflopende volgorde, of
 *     b. een optie een letterlabel noemt (A–F als los woord: "plaatje A", "Doos B",
 *        "A B C") — anders staat letter A naast "plaatje C".
 *     c. (tekening-regel) het item een tekening/visual heeft (Visual: ja, een ```-blok of
 *        "(Visual: …)" in de opgave) EN de opties of de opgave naar letterlabels in die
 *        tekening verwijzen ("bouwplaat A", "strook B", "figuur C", "tekening A", "vorm A",
 *        "plaatje 2", een kale "A" als optie, "A–D", "A, B of C", of regels in de tekening
 *        die met A/B/C/D beginnen), of
 *     d. de opgave vraagt "welke strook/bouwplaat/figuur/…" met letters ("(A–D)", "A, B of C").
 *  0. Vlag gaat vóór alles: item.shuffle === false (bank-md "- **Husselen:** nee") → bankvolgorde.
 *  3. Minder dan 2 schudbare opties → niets schudden.
 * Schudden = Fisher–Yates op de schudbare opties; komt de volgorde exact
 * gelijk uit aan de bankvolgorde, dan opnieuw (zodat A niet 'toevallig' A blijft).
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.LeerMeesMC = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  var LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H"];

  var META_RE = new RegExp(
    "^\\s*(?:" +
      [
        "(?:ze zijn |ze krijgen |ze eten allemaal |het is |zijn )?even(?:\\s)?(?:groot|veel|sterk|steil|warm|koud|lang|zwaar|duur|ver|dichtbij|oud|hoog|breed)\\b",
        "evenveel\\b",
        "alle drie evenveel",
        "(?:blijft |is )?gelijk\\b",
        "allebei\\b",
        "beide[n]?[.!]?\\s*$",
        "geen van (?:beide[n]?|allen|alle|deze|bovenstaande)\\b",
        "alle(?:maal| antwoorden| opties| drie| vier)\\b",
        "weet ik niet",
        "geen idee",
        "(?:dat |je )?(?:kun|kan) je (?:het )?niet (?:zeggen|weten|vergelijken|met elkaar vergelijken)\\b",
        "je kunt het niet (?:zeggen|weten|vergelijken)\\b",
        "(?:dat is )?(?:niet te zeggen|onmogelijk te zeggen)\\b"
      ].join("|") +
      ")",
    "i"
  );

  var LABEL_RE = /(^|[^A-Za-zÀ-ÿ°])[A-F](?=$|[^A-Za-zÀ-ÿ'’])/; // '°C' is een eenheid, geen label

  // --- tekening-regel ---------------------------------------------------------
  var DRAW_WORDS = [
    "bouwplaat", "bouwplaten", "strook", "stroken", "figuur", "figuren", "tekening", "tekeningen",
    "plaatje", "plaatjes", "vorm", "vormen", "afbeelding", "plaat", "staaf", "staven", "balk",
    "blok", "toren", "bouwwerk", "kaart", "kaartje", "patroon", "net", "klok", "weegschaal",
    "beker", "doos", "zak", "pijl", "route", "rooster", "vak", "rij", "kolom", "lijn", "punt",
    "driehoek", "vierkant", "rechthoek", "cirkel", "grafiek", "diagram", "tegel", "bak", "fles"
  ].map(function (w) { return "[" + w[0].toUpperCase() + w[0] + "]" + w.slice(1); }).join("|");
  // "strook B", "figuur C", "plaatje 2"
  var DRAW_LABEL_RE = new RegExp("(?:^|[^A-Za-zÀ-ÿ])(?:" + DRAW_WORDS + ")\\s+(?:[A-F]|[1-9])(?![A-Za-zÀ-ÿ0-9])");
  var BARE_LABEL_RE = /^\s*[A-F]\s*[.)]?\s*$/;                                      // optie is alleen "A"
  var LETTER_RANGE_RE = /(?:^|[^A-Za-zÀ-ÿ])[A-F]\s*(?:–|—|-|t\/m|tot en met)\s*[A-F](?![A-Za-zÀ-ÿ])/;
  var LETTER_LIST_RE = /(?:^|[^A-Za-zÀ-ÿ])[A-F](?:\s*[,/]\s*[A-F])*\s*(?:,|\/|\bof\b|\ben\b)\s*[A-F](?![A-Za-zÀ-ÿ])/;
  var WELKE_RE = new RegExp("\\b[Ww]elke\\s+(?:" + DRAW_WORDS + ")\\b");

  function hasDrawing(ctx) {
    if (!ctx) return false;
    if (ctx.visual === true || /^\s*ja\b/i.test(String(ctx.visual || ""))) return true;
    var p = String(ctx.prompt || "");
    return /```/.test(p) || /\bVisual\s*:/i.test(p);
  }

  /** Letterlabels in de tekening zelf: ≥2 regels in een ```-blok die met een eigen letter beginnen. */
  function drawingRowLabels(prompt) {
    var seen = {};
    String(prompt || "").replace(/```[\s\S]*?```/g, function (block) {
      block.split("\n").forEach(function (line) {
        var m = line.match(/^\s*([A-F])(?:\s{2,}|\s*[):.]\s|\s*$)/);
        if (m) seen[m[1]] = true;
      });
      return block;
    });
    return Object.keys(seen).length >= 2;
  }

  function promptRefersToLabels(prompt) {
    var p = String(prompt || "");
    var text = p.replace(/```[\s\S]*?```/g, " ");
    return DRAW_LABEL_RE.test(text) || LETTER_RANGE_RE.test(text) || LETTER_LIST_RE.test(text) || drawingRowLabels(p);
  }

  function optionsReferToLabels(options) {
    return (options || []).some(function (o) {
      var t = String(o.text || "");
      return DRAW_LABEL_RE.test(t) || BARE_LABEL_RE.test(t);
    });
  }

  /** @returns reden-string als de set vast moet blijven door de tekening-regel, anders null */
  function drawingRule(options, ctx) {
    var prompt = String((ctx && ctx.prompt) || "");
    var text = prompt.replace(/```[\s\S]*?```/g, " ");
    if (WELKE_RE.test(text) && (LETTER_RANGE_RE.test(text) || LETTER_LIST_RE.test(text))) return "welke-vraag met letters";
    if (hasDrawing(ctx) && (optionsReferToLabels(options) || promptRefersToLabels(prompt))) return "tekening + letterlabels";
    return null;
  }

  function isMetaOption(text) {
    return META_RE.test(String(text || ""));
  }

  function hasLetterLabel(text) {
    return LABEL_RE.test(String(text || ""));
  }

  /** "€1.285", "46.389", "3,5 m", "25%", "−2 °C", "3/4", "schaal 1 : 100", "1 op de 5" → {value, unit} of null */
  function parseNumber(text) {
    var t = String(text || "").trim().replace(/\u00a0/g, " ");
    // Verhoudingsnotatie van de bank: "schaal 1 : 100" / "1 : 100" en "1 op de 5".
    // Alleen gelijksoortige reeksen tellen als geordend (andere unit dan gewone getallen/%).
    // ' : ' is in G4–G8 ook het deelteken ("12 : 4"). Alleen "schaal a : b" en "1 : n" zijn verhoudingen;
    // een andere "a : b" is een deelsom en geen los getal (dus nooit een geordende reeks die vast moet staan).
    var r = t.match(/^(schaal\s+)?(\d+)\s:\s(\d{1,3}(?:\.\d{3})+|\d+)\.?$/i);
    if (r && (r[1] || r[2] === "1")) return { value: parseFloat(r[3].replace(/\./g, "")) / parseFloat(r[2]), unit: r[1] ? "schaal" : "1:n" };
    if (r) return null;
    r = t.match(/^(\d+)\s+op\s+de\s+(\d{1,3}(?:\.\d{3})+|\d+)\.?$/i);
    if (r) return { value: parseFloat(r[1]) / parseFloat(r[2].replace(/\./g, "")), unit: "op de" };
    var m = t.match(/^(€\s?)?([−-]?)(\d{1,3}(?:[.\s]\d{3})+|\d+)(?:,(\d+))?(?:\s*\/\s*(\d+))?\s*(%|°C|[a-zA-Zµ²³]{1,4})?\.?$/);
    if (!m) return null;
    var whole = m[3].replace(/[.\s]/g, "");
    var v = parseFloat(whole + (m[4] ? "." + m[4] : ""));
    if (m[5]) v = v / parseFloat(m[5]);
    if (m[2]) v = -v;
    return { value: v, unit: (m[1] ? "€" : "") + (m[6] || "") + (m[5] ? "/" : "") };
  }

  function isOrderedNumberSet(options) {
    if (!options || options.length < 3) return false;
    var nums = options.map(function (o) { return parseNumber(o.text); });
    if (nums.some(function (n) { return !n; })) return false;
    var unit = nums[0].unit;
    if (nums.some(function (n) { return n.unit !== unit; })) return false;
    var asc = true, desc = true;
    for (var i = 1; i < nums.length; i++) {
      if (!(nums[i].value > nums[i - 1].value)) asc = false;
      if (!(nums[i].value < nums[i - 1].value)) desc = false;
    }
    return asc || desc;
  }

  function fisherYates(arr, rng) {
    var r = rng || Math.random;
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(r() * (i + 1));
      var tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
    }
    return arr;
  }

  /**
   * @param options [{key, text}] in bankvolgorde
   * @param rng optioneel (0..1), standaard Math.random
   * @param ctx optioneel {shuffle, prompt, visual} van het item (vlag + tekening-regel)
   * @returns {order: number[] (indices in bankvolgorde), reason: string, fixed: boolean[]}
   */
  function planOrder(options, rng, ctx) {
    var n = (options || []).length;
    var identity = [];
    for (var i = 0; i < n; i++) identity.push(i);
    var allFixed = function (reason) { return { order: identity, reason: reason, fixed: identity.map(function () { return true; }) }; };
    if (ctx && (ctx.shuffle === false || /^\s*nee\b/i.test(String(ctx.shuffle)))) return allFixed("vlag Husselen: nee");
    if (n < 2) return allFixed("te weinig opties");
    if (options.some(function (o) { return hasLetterLabel(o.text); })) return allFixed("letterlabels");
    var dr = drawingRule(options, ctx);
    if (dr) return allFixed(dr);
    if (isOrderedNumberSet(options)) {
      return { order: identity, reason: "geordende getallen", fixed: identity.map(function () { return true; }) };
    }
    var fixed = options.map(function (o) { return isMetaOption(o.text); });
    var movable = identity.filter(function (i) { return !fixed[i]; });
    if (movable.length < 2) return { order: identity, reason: "te weinig schudbare opties", fixed: fixed };
    var shuffled;
    var guard = 0;
    do {
      shuffled = fisherYates(movable.slice(), rng);
      guard++;
      // Bij ≥3 schudbare opties: nooit exact de bankvolgorde tonen. Bij 2: eerlijke 50/50
      // (anders zou de ruil altijd plaatsvinden en staat het goede antwoord weer vast).
    } while (movable.length >= 3 && guard < 50 && shuffled.every(function (v, k) { return v === movable[k]; }));
    var order = identity.slice();
    movable.forEach(function (slot, k) { order[slot] = shuffled[k]; });
    return { order: order, reason: fixed.some(Boolean) ? "geschud, meta-optie vast" : "geschud", fixed: fixed };
  }

  function letters(n) {
    return LETTERS.slice(0, n);
  }

  // ---- Bank-adapter (bank/data.json-item → {options, correctKey, errorHints}) ----
  function optionsFromBank(raw) {
    var s = String(raw || "").trim();
    if (!s) return [];
    // formaten: "A) x · B) y", "- A) x\n- B) y", "A) x\nB) y" en code-blokken "A)```…```\nB)```…```"
    var parts = s.replace(/^- (?=[A-F]\))/gm, "").split(/\s*·\s*(?=[A-F]\)\s)|\n+(?=[A-F]\))/);
    return parts.map(function (p) {
      var m = p.match(/^([A-F])\)\s*([\s\S]*)$/);
      return m ? { key: m[1], text: m[2].trim() } : null;
    }).filter(Boolean);
  }

  function errorHintsFromBank(raw) {
    var map = {};
    // ook gecombineerde sleutels: "C of D → …", "C/D → …", "C en D → …"
    var KEYS = "[A-F](?:\\s*(?:,|/|of|en)\\s*[A-F])*";
    String(raw || "").split(new RegExp("\\s·\\s(?=" + KEYS + "\\s*→)")).forEach(function (p) {
      var m = p.match(new RegExp("^\\s*(" + KEYS + ")\\s*→\\s*([\\s\\S]*)$"));
      if (!m) return;
      m[1].match(/[A-F]/g).forEach(function (k) { map[k] = m[2].trim(); });
    });
    return map;
  }

  /**
   * @param key     optioneel item-ID ("G8-MKU-E02-005") voor optie-plaatjes
   * @param visuals optioneel LeerMeesVisuals: optie krijgt `visual` (SVG) als er een plaatje bij die optietekst hoort.
   *                Het plaatje hoort bij de optie zelf en schudt dus mee.
   */
  function fromBank(item, key, visuals) {
    var ans = String(item.answer || "").trim().match(/^([A-F])\b/);
    var options = optionsFromBank(item.options);
    if (key && visuals && typeof visuals.optionVisualSvg === "function") {
      options.forEach(function (o) { var svg = visuals.optionVisualSvg(key, o.key, o.text); if (svg) o.visual = svg; });
    }
    return {
      options: options,
      correctKey: ans ? ans[1] : null,
      errorHints: errorHintsFromBank(item.errorHints),
      ctx: { shuffle: item.shuffle, prompt: item.prompt, visual: item.visual }
    };
  }

  /** Volgorde-plan voor een bank-item (data.json-item of parseMdItem-resultaat). */
  function planForBankItem(item, rng) {
    var b = fromBank(item);
    return planOrder(b.options, rng, b.ctx);
  }

  /**
   * Eén item-blok uit een bank-md ("## 004 · toepassen · meerkeuze" + "- **Veld:** waarde")
   * → bank-achtig item. "- **Husselen:** nee" → shuffle:false; "- **Visual:** ja" → visual:true.
   */
  function parseMdItem(block) {
    var MAP = { "opgave": "prompt", "antwoord": "answer", "opties": "options", "fout-hints": "errorHints",
      "fout hints": "errorHints", "hint": "hint", "sterkere hint": "strongerHint", "ouderzin": "parentLine",
      "visual": "visual", "husselen": "shuffle" };
    var item = {}, cur = null, buf = [];
    var head = String(block || "").match(/^##\s+(\d{3})\s*·\s*([^\n·]+?)\s*·\s*([^\n]+?)\s*$/m);
    if (head) { item.n = head[1]; item.level = head[2].trim(); item.format = head[3].trim(); }
    function flush() { if (cur) item[cur] = buf.join("\n").trim(); cur = null; buf = []; }
    String(block || "").split(/\r?\n/).forEach(function (line) {
      var fm = line.match(/^- \*\*([^*]+):\*\*\s*(.*)$/);
      if (fm) { flush(); var k = MAP[fm[1].toLowerCase().replace(/\s+/g, " ").trim()]; if (k) { cur = k; buf = [fm[2] || ""]; } return; }
      if (/^##/.test(line)) { flush(); return; }
      if (cur) buf.push(line.replace(/^\s{2}/, ""));
    });
    flush();
    if ("shuffle" in item) { if (/^nee\b/i.test(item.shuffle)) item.shuffle = false; else delete item.shuffle; }
    if ("visual" in item) item.visual = /^ja\b/i.test(item.visual);
    return item;
  }

  return {
    planOrder: planOrder,
    fisherYates: fisherYates,
    letters: letters,
    isMetaOption: isMetaOption,
    hasLetterLabel: hasLetterLabel,
    isOrderedNumberSet: isOrderedNumberSet,
    parseNumber: parseNumber,
    fromBank: fromBank,
    planForBankItem: planForBankItem,
    parseMdItem: parseMdItem,
    drawingRule: drawingRule,
    hasDrawing: hasDrawing,
    optionsFromBank: optionsFromBank,
    errorHintsFromBank: errorHintsFromBank
  };
});
