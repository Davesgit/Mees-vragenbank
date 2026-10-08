/**
 * LeerMees — visuals voor bank-items (leerdoel.html; ook bruikbaar in node voor checks).
 *
 * Turven: bosjes van 5 (4 staande streepjes + 1 schuine streep erdoorheen), daarna losse
 * streepjes. Een turf wordt getekend zoals de ASCII hem opbouwt: "||||/" of "|||||" = bosje,
 * "|" = los streepje. "| | | | | |" (zes losse) blijft dus zes losse streepjes.
 *
 * VISUAL_OVERRIDES koppelt een item-ID aan turf-marks (zolang data.json geen visual-ID draagt):
 *   marks: [{ id, field: "prompt"|"answer"|"hint"|"strongerHint"|"errorHints", find, ascii, count, label? }]
 *     find  = exact stuk tekst (precies één keer in het veld) waarin `ascii` staat
 *     ascii = het deel dat door de SVG vervangen wordt; count = aantal streepjes
 *   check: hoe het antwoord bij de turven past (zie scripts/check-visuals.js):
 *     total · row{label} · table{labels} (MC-optie) · steps{n:{row}|{tableRow}|{row,equalsTable,yes,no}}
 *     · pairs (antwoord "turf → N") · claims[] (zin → klopt / klopt niet)
 * Harde regel: visual = ASCII in de opgave = antwoord. De SVG tekent precies `count` streepjes.
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.LeerMeesVisuals = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  function P(find, ascii, count, label, id) { return { field: "prompt", find: find, ascii: ascii, count: count, label: label || null, id: id || null }; }
  function A(find, ascii, count, id) { return { field: "answer", find: find, ascii: ascii, count: count, id: id || null }; }
  // Hint-velden (hint / strongerHint / errorHints). Controle via `= N` in find, `sameAs` (id van een
  // opgave-turf; bij `group` telt de som van de groep) of `unit` (los symbool "|" = 1 streepje).
  function H(field, find, ascii, count, extra) {
    var m = { field: field, find: find, ascii: ascii, count: count };
    for (var k in extra || {}) m[k] = extra[k];
    return m;
  }

  var VISUAL_OVERRIDES = {
    "G6-VBN-V01-005": { type: "turf", size: "m",
      marks: [P("Ze turft: ||||/ ||||/ |||", "||||/ ||||/ |||", 13)],
      check: { type: "total" } },

    "G4-VBN-E02-001": { type: "turf",
      marks: [P("(elke | = 1 stem)", "|", 1, "legenda"), P("rood   | | | |", "| | | |", 4, "rood"), P("blauw  | | |", "| | |", 3, "blauw"),
        H("strongerHint", "vier | -streepjes", "|", 1, { unit: true })],
      check: { type: "row", label: "rood" } },
    "G4-VBN-E02-003": { type: "turf",
      marks: [P("dwars; ||||| = 5", "|||||", 5, "legenda"), P("hond  |||||  | |", "|||||  | |", 7, "hond")],
      check: { type: "row", label: "hond" } },
    "G4-VBN-E02-004": { type: "turf",
      marks: [P("appel  |||||", "|||||", 5, "appel"), P("peer   | | |", "| | |", 3, "peer"), P("banaan |||||  |", "|||||  |", 6, "banaan"),
        H("hint", "||||| = 5", "|||||", 5)],
      check: { type: "table", labels: ["appel", "peer", "banaan"] } },
    "G4-VBN-E02-006": { type: "turf",
      marks: [P("- |||||  | |  →", "|||||  | |", 7, null, "t7"), P("- | | |  →", "| | |", 3, null, "t3"), P("- |||||  |||||  →", "|||||  |||||", 10),
        A("||||| | | → 7", "||||| | |", 7), A("· | | | → 3", "| | |", 3), A("||||| ||||| → 10", "||||| |||||", 10),
        H("hint", "Bundeltje ||||| = 5", "|||||", 5),
        H("errorHints", "|||||+", "|||||", 5, { sameAs: "t7", group: "f7" }), H("errorHints", "+| | →", "| |", 2, { sameAs: "t7", group: "f7" }),
        H("errorHints", "· ||| → 5", "|||", 3, { sameAs: "t3" })],
      check: { type: "pairs" } },
    "G4-VBN-E02-007": { type: "turf",
      marks: [P("“||||| betekent", "|||||", 5, null, "z1"), P("Turf | | | | | | (zes", "| | | | | |", 6, null, "z3a"), P("als |||||  | .", "|||||  |", 6, null, "z3b"),
        A("“||||| = 5”", "|||||", 5), A("= ||||| |”", "||||| |", 6),
        H("errorHints", "||||| = 5 →", "|||||", 5)],
      check: { type: "claims", claims: [
        { segment: 0, mark: "z1", value: 5, text: "betekent 5 stemmen" },
        { segment: 2, same: ["z3a", "z3b"], text: "zes losse = ||||| |" }] } },
    "G4-VBN-E02-008": { type: "turf",
      marks: [P("bal    |||||  | |", "|||||  | |", 7, "bal"), P("pop    | | | |", "| | | |", 4, "pop"), P("auto   |||||", "|||||", 5, "auto", "auto"),
        H("errorHints", "Auto is ||||| = 5", "|||||", 5, { sameAs: "auto" })],
      check: { type: "steps", steps: { 1: { row: "bal" }, 2: { row: "pop" }, 3: { row: "auto" } } } },
    "G5-VBN-V01-002": { type: "turf",
      marks: [P("voetbal  | | | |", "| | | |", 4, "voetbal"), P("tennis   | | |", "| | |", 3, "tennis"),
        H("strongerHint", "drie | -streepjes", "|", 1, { unit: true })],
      check: { type: "row", label: "tennis" } },
    "G5-VBN-V01-005": { type: "turf",
      marks: [P("(||||| = 5)", "|||||", 5, "legenda"), P("rood   |||||  | |", "|||||  | |", 7, "rood"), P("blauw  |||||", "|||||", 5, "blauw"), P("groen  | | |", "| | |", 3, "groen"),
        H("hint", "||||| = 5", "|||||", 5)],
      check: { type: "table", labels: ["rood", "blauw", "groen"] } },
    "G5-VBN-V01-008": { type: "turf",
      marks: [P("rood | | | |", "| | | |", 4, "rood"), P("blauw ||||| |", "||||| |", 6, "blauw", "blauw"),
        H("errorHints", "||||| | = 6", "||||| |", 6, { sameAs: "blauw" })],
      check: { type: "steps", steps: { 1: { tableRow: "blauw" }, 2: { row: "rood" }, 3: { row: "blauw", equalsTable: "blauw", yes: "ja", no: "nee" } } } },

    // ---- Grafieken (spec Didactiek 2026-09-30). Geen waardelabels, geen letters; waarden = opgave.
    "G8-VBN-V01-004": { type: "graph", alt: "Lijngrafiek: lengte van een zonnebloem per week",
      graph: { kind: "line", x: { title: "weken", min: 0, max: 6, step: 1 }, y: { title: "lengte (cm)", min: 0, max: 100, step: 10 },
        series: [{ name: "zonnebloem", color: "#1e3a5f", marker: "circle", data: [{ x: 2, y: 30, find: "(2, 30)" }, { x: 4, y: 70, find: "(4, 70)" }] }] },
      check: { type: "mcPoint", x: 4, series: 0, unit: "cm", onGrid: [30, 70] } },
    "G8-VBN-V01-007": { type: "graph", alt: "Staafdiagram: aantal kinderen op De Linde en De Eik; de y-as begint bij 180",
      graph: { kind: "bar", x: { categories: ["De Linde", "De Eik"] }, y: { title: "kinderen", min: 180, max: 220, step: 10 },
        series: [{ name: "kinderen", color: "#1e3a5f", data: [{ x: "De Linde", y: 210, find: "De Linde 210" }, { x: "De Eik", y: 190, find: "De Eik 190" }] }] },
      check: { type: "barRatio", a: "De Linde", b: "De Eik", ratio: 3, find: "3 keer zo hoog", axisStartFind: "bij 180" } },
    "G8-VBN-E01-008": { type: "graph", alt: "Lijngrafiek: bezoekers van De Golf en Het Bad in juni, juli en augustus",
      graph: { kind: "line", legend: true, x: { categories: ["juni", "juli", "augustus"] }, y: { title: "bezoekers", min: 0, max: 1600, step: 200 },
        series: [
          { name: "De Golf", color: "#2563a8", marker: "circle", data: [{ x: "juni", y: 800, find: "Juni → blauw 800" }, { x: "juli", y: 1200, find: "juli → blauw 1200" }, { x: "augustus", y: 1000, find: "augustus → blauw 1000" }] },
          { name: "Het Bad", color: "#c0392b", marker: "square", dash: true, data: [{ x: "juni", y: 600, find: "rood 600" }, { x: "juli", y: 1000, find: "rood 1000" }, { x: "augustus", y: 1500, find: "rood 1500" }] }] },
      check: { type: "steps", steps: { 1: { series: 0, x: "juli" }, 2: { higher: 1, than: 0 } }, totals: [3000, 3100], halfway: [1500] } },
    "G8-VBN-E04-008": { type: "graph", alt: "Staafdiagram: uitgeleende boeken in 2023, 2024 en 2025; de y-as begint bij 3800",
      graph: { kind: "bar", x: { categories: ["2023", "2024", "2025"] }, y: { title: "boeken", min: 3800, max: 4600, step: 200 },
        series: [{ name: "boeken", color: "#1e3a5f", data: [{ x: "2023", y: 4000, find: "2023 → 4000" }, { x: "2024", y: 4200, find: "2024 → 4200" }, { x: "2025", y: 4400, find: "2025 → 4400" }] }] },
      check: { type: "steps", steps: { 1: { diff: ["2025", "2023"] }, 2: { ratioAbove: ["2025", "2023"] } }, axisStartFind: "bij 3800" } },

    // ---- Patronen: alleen de gegeven stappen; nooit de stap die gevraagd wordt.
    "G8-VBN-E03-003": { type: "pattern", alt: "Huisjes van lucifers: 1, 2 en 3 huisjes naast elkaar",
      pattern: { kind: "matchHouses", steps: [1, 2, 3] },
      check: { counts: [{ step: 1, find: "1 huisje kost 5 lucifers" }, { step: 2, find: "kosten 9 lucifers" }, { step: 3, find: "3 huisjes kosten 13" }], asked: [5] } },
    "G8-VBN-E03-008": { type: "pattern", alt: "Rijen witte tegels met een rand van grijze tegels: 1, 2 en 3 witte tegels",
      pattern: { kind: "tileBorder", steps: [1, 2, 3] },
      check: { counts: [{ step: 1, find: "Bij 1 witte tegel horen 8 grijze" }, { step: 2, find: "Bij 2 witte tegels horen 10 grijze" }, { step: 3, find: "Bij 3 witte tegels horen 12 grijze" }], asked: [4, 10, 20] } },

    // ---- Bouwplaten als optie-plaatjes: elk plaatje hoort bij zijn optietekst en schudt mee.
    "G8-MKU-E02-005": { type: "optionNets", solid: "kubus",
      options: {
        A: { text: "6 vierkanten op één rij.", cells: [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]] },
        B: { text: "4 vierkanten op een rij, met boven het eerste én boven het tweede vierkant nog één vierkant.", cells: [[1, 0], [1, 1], [1, 2], [1, 3], [0, 0], [0, 1]] },
        C: { text: "6 vierkanten in twee rijen van 3, precies onder elkaar.", cells: [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]] },
        D: { text: "4 vierkanten op een rij, met boven en onder het tweede vierkant nog één vierkant.", cells: [[1, 0], [1, 1], [1, 2], [1, 3], [0, 1], [2, 1]] }
      } }
  };

  /**
   * ASCII-turf → { total, bundles, loose }. Tokens gescheiden door spaties:
   *   "||||/" of "|||||" = bosje van 5 · "|", "||", "|||", "||||" = losse streepjes.
   * Ongeldig token → null.
   */
  function parseTallyAscii(str) {
    var tokens = String(str || "").trim().split(/\s+/).filter(Boolean);
    if (!tokens.length) return null;
    var total = 0, bundles = 0, loose = 0;
    for (var i = 0; i < tokens.length; i++) {
      var t = tokens[i];
      if (/^\|{4}\/$/.test(t) || /^\|{5}$/.test(t)) { total += 5; bundles += 1; }
      else if (/^\|{1,4}$/.test(t)) { total += t.length; loose += t.length; }
      else return null;
    }
    return { total: total, bundles: bundles, loose: loose };
  }

  function tallyWords(bundles, loose) {
    var parts = [];
    if (bundles) parts.push(bundles + (bundles === 1 ? " bosje" : " bosjes") + " van 5");
    if (loose) parts.push(loose + (loose === 1 ? " los streepje" : " losse streepjes"));
    return "Turfjes: " + (parts.join(" en ") || "geen streepjes");
  }

  /** SVG met `bundles` bosjes van 5 en daarna `loose` losse streepjes (= bundles*5 + loose lijnen). */
  function tallySvgParts(bundles, loose, opts) {
    var o = opts || {};
    var h = o.height || 34, gap = o.gap || Math.round(h * 0.27), groupGap = o.groupGap || Math.round(h * 0.53), pad = Math.max(3, Math.round(h * 0.17));
    var stroke = o.color || "#1e3a5f", sw = o.strokeWidth || (h < 30 ? 2.5 : 3);
    var top = pad, bottom = pad + h, x = pad + 4, lines = [];
    function vline(px) { lines.push('<line class="turf-stroke" x1="' + px + '" y1="' + top + '" x2="' + px + '" y2="' + bottom + '"/>'); }
    for (var b = 0; b < bundles; b++) {
      var x0 = x;
      for (var k = 0; k < 4; k++) { vline(x); x += gap; }
      var x3 = x - gap, d = Math.round(h * 0.15);
      lines.push('<line class="turf-slash" x1="' + (x0 - d) + '" y1="' + (bottom - d) + '" x2="' + (x3 + d) + '" y2="' + (top + d) + '"/>');
      x = x3 + groupGap;
    }
    for (var r = 0; r < loose; r++) { vline(x); x += gap; }
    var width = Math.max(x - gap + pad + 4, 2 * pad);
    return (
      '<svg class="viz-turf" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="' + tallyWords(bundles, loose) + '"' +
      ' width="' + width + '" height="' + (h + 2 * pad) + '" viewBox="0 0 ' + width + " " + (h + 2 * pad) + '">' +
      '<g stroke="' + stroke + '" stroke-width="' + sw + '" stroke-linecap="round">' + lines.join("") + "</g></svg>"
    );
  }

  /** Standaard-opbouw: ⌊n/5⌋ bosjes + rest. */
  function tallySvg(count, opts) {
    var n = Math.max(0, Math.floor(Number(count) || 0));
    return tallySvgParts(Math.floor(n / 5), n % 5, opts);
  }

  /** SVG voor een mark: opbouw zoals in de ASCII. */
  function markSvg(mark, size) {
    var p = parseTallyAscii(mark.ascii);
    var opts = { height: size === "m" ? 34 : 22 };
    return p ? tallySvgParts(p.bundles, p.loose, opts) : "";
  }

  // ---------------------------------------------------------------- grafieken
  function escXml(t) { return String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  function fmtNum(n) { return String(n); }
  function range(min, max, step) { var out = []; for (var v = min; v <= max + 1e-9; v += step) out.push(Math.round(v * 1e6) / 1e6); return out; }

  /**
   * Lijn- of staafgrafiek. Tekst in de SVG: alleen as-titels (g-axis-title), schaalgetallen (g-tick),
   * categorieën (g-cat) en legenda (g-legend). Nooit waardelabels bij punten of staven.
   */
  function graphSvg(g, alt) {
    var W = 460, H = 300, L = 64, R = 18, T = 20, B = 58;
    var legendW = g.legend ? 150 : 0;
    var pw = W - L - R, ph = H - T - B;
    var y = g.y, yv = function (v) { return T + ph - (v - y.min) / (y.max - y.min) * ph; };
    var cats = g.x.categories, xv;
    if (cats) {
      var slot = pw / cats.length;
      xv = function (x) { return L + slot * (cats.indexOf(x) + 0.5); };
    } else xv = function (x) { return L + (x - g.x.min) / (g.x.max - g.x.min) * pw; };
    var o = [];
    o.push('<rect x="' + L + '" y="' + T + '" width="' + pw + '" height="' + ph + '" fill="#fff"/>');
    range(y.min, y.max, y.step).forEach(function (v) {
      var py = yv(v).toFixed(1);
      o.push('<line class="g-grid" x1="' + L + '" y1="' + py + '" x2="' + (L + pw) + '" y2="' + py + '" stroke="#d5dde6" stroke-width="1"/>');
      o.push('<line class="g-tickmark" x1="' + (L - 5) + '" y1="' + py + '" x2="' + L + '" y2="' + py + '" stroke="#1e3a5f" stroke-width="1.5"/>');
      o.push('<text class="g-tick g-ytick" data-v="' + v + '" x="' + (L - 9) + '" y="' + (+py + 4) + '" text-anchor="end" font-size="' + (v === y.min ? 13 : 12) + '"' + (v === y.min ? ' font-weight="700"' : "") + ">" + fmtNum(v) + "</text>");
    });
    if (cats) {
      cats.forEach(function (c) { o.push('<text class="g-cat" x="' + xv(c).toFixed(1) + '" y="' + (T + ph + 20) + '" text-anchor="middle" font-size="13">' + escXml(c) + "</text>"); });
    } else {
      range(g.x.min, g.x.max, g.x.step).forEach(function (v) {
        var px = xv(v).toFixed(1);
        o.push('<line class="g-grid g-xgrid" x1="' + px + '" y1="' + T + '" x2="' + px + '" y2="' + (T + ph) + '" stroke="#eef2f6" stroke-width="1"/>');
        o.push('<line class="g-tickmark" x1="' + px + '" y1="' + (T + ph) + '" x2="' + px + '" y2="' + (T + ph + 5) + '" stroke="#1e3a5f" stroke-width="1.5"/>');
        o.push('<text class="g-tick g-xtick" data-v="' + v + '" x="' + px + '" y="' + (T + ph + 19) + '" text-anchor="middle" font-size="12">' + fmtNum(v) + "</text>");
      });
    }
    // assen
    o.push('<line class="g-axis" x1="' + L + '" y1="' + T + '" x2="' + L + '" y2="' + (T + ph) + '" stroke="#1e3a5f" stroke-width="2"/>');
    o.push('<line class="g-axis" x1="' + L + '" y1="' + (T + ph) + '" x2="' + (L + pw) + '" y2="' + (T + ph) + '" stroke="#1e3a5f" stroke-width="2"/>');
    if (y.title) o.push('<text class="g-axis-title" x="16" y="' + (T + ph / 2) + '" text-anchor="middle" font-size="13" transform="rotate(-90 16 ' + (T + ph / 2) + ')">' + escXml(y.title) + "</text>");
    if (g.x.title) o.push('<text class="g-axis-title" x="' + (L + pw / 2) + '" y="' + (H - 12) + '" text-anchor="middle" font-size="13">' + escXml(g.x.title) + "</text>");
    // data
    g.series.forEach(function (s, si) {
      if (g.kind === "bar") {
        var bw = Math.min(70, pw / cats.length * 0.5);
        s.data.forEach(function (d) {
          var top = yv(d.y), base = yv(y.min);
          o.push('<rect class="g-bar" data-series="' + si + '" data-x="' + escXml(d.x) + '" data-y="' + d.y + '" x="' + (xv(d.x) - bw / 2).toFixed(1) + '" y="' + top.toFixed(1) + '" width="' + bw.toFixed(1) + '" height="' + (base - top).toFixed(1) + '" fill="' + s.color + '"/>');
        });
      } else {
        var pts = s.data.map(function (d) { return xv(d.x).toFixed(1) + "," + yv(d.y).toFixed(1); }).join(" ");
        o.push('<polyline class="g-line" data-series="' + si + '" points="' + pts + '" fill="none" stroke="' + s.color + '" stroke-width="3"' + (s.dash ? ' stroke-dasharray="9 6"' : "") + "/>");
        s.data.forEach(function (d) { o.push(markerSvg(s, si, xv(d.x), yv(d.y), d)); });
      }
    });
    if (g.legend) {
      var lx = W + 8, ly = T + 10;
      g.series.forEach(function (s, si) {
        var yy = ly + si * 28;
        o.push('<line class="g-legend-line" x1="' + lx + '" y1="' + yy + '" x2="' + (lx + 36) + '" y2="' + yy + '" stroke="' + s.color + '" stroke-width="3"' + (s.dash ? ' stroke-dasharray="9 6"' : "") + "/>");
        o.push(markerSvg(s, si, lx + 18, yy, null));
        o.push('<text class="g-legend" x="' + (lx + 44) + '" y="' + (yy + 4) + '" font-size="13">' + escXml(s.name) + "</text>");
      });
    }
    var TW = W + legendW;
    return '<svg class="viz-graph" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="' + escXml(alt || "Grafiek") + '" width="' + TW + '" height="' + H + '" viewBox="0 0 ' + TW + " " + H + '" font-family="inherit" fill="#1e3a5f">' + o.join("") + "</svg>";
  }

  function markerSvg(s, si, x, y, d) {
    var attrs = d ? ' class="g-point" data-series="' + si + '" data-x="' + escXml(d.x) + '" data-y="' + d.y + '"' : ' class="g-legend-marker"';
    if (s.marker === "square") return '<rect' + attrs + ' x="' + (x - 6).toFixed(1) + '" y="' + (y - 6).toFixed(1) + '" width="12" height="12" fill="' + s.color + '" stroke="#fff" stroke-width="1.5"/>';
    return '<circle' + attrs + ' cx="' + x.toFixed(1) + '" cy="' + y.toFixed(1) + '" r="6" fill="' + s.color + '" stroke="#fff" stroke-width="1.5"/>';
  }

  // ---------------------------------------------------------------- patronen
  /** n huisjes naast elkaar die een muur delen: vloer + 2 muren + 2 dakstukken, dan per huisje +4 = 4n + 1 lucifers. */
  // Lucifers: elk stokje 12% korter aan beide kanten (gaatje bij elke hoek), precies 1 kop per stokje,
  // koppen als laatste getekend en nooit binnen 2 × r van elkaar (spec Didactiek 2026-09-30).
  // Dakstokjes zijn korter en staan schuin in de nok: daar 15%, zodat de nok-kop het andere dakstokje niet raakt.
  var MATCH_HEAD_R = 3.6, MATCH_GAP = 0.12, MATCH_GAP_ROOF = 0.15;
  function matchHousesSvg(n, x0, y0, u) {
    var lines = [], heads = [], hw = u, roof = u * 0.6;
    // (xa,ya) → (xb,yb); de kop komt op het (ingekorte) b-uiteinde
    function match(xa, ya, xb, yb, g) {
      var dx = xb - xa, dy = yb - ya;
      g = g || MATCH_GAP;
      var x1 = xa + dx * g, y1 = ya + dy * g, x2 = xb - dx * g, y2 = yb - dy * g;
      lines.push('<line class="match" x1="' + x1.toFixed(1) + '" y1="' + y1.toFixed(1) + '" x2="' + x2.toFixed(1) + '" y2="' + y2.toFixed(1) + '" stroke="#b7803e" stroke-width="4" stroke-linecap="round"/>');
      heads.push('<circle class="match-head" cx="' + x2.toFixed(1) + '" cy="' + y2.toFixed(1) + '" r="' + MATCH_HEAD_R + '" fill="#b3261e"/>');
    }
    var base = y0 + roof + hw;
    for (var i = 0; i < n; i++) {
      var xl = x0 + i * hw, xr = xl + hw, xm = xl + hw / 2, sh = base - hw, top = base - hw - roof;
      if (i === 0) match(xl, base, xl, sh); // linker muur, kop boven
      match(xr, base, xr, sh);              // rechter muur (gedeeld met het volgende huisje), kop boven
      match(xl, base, xr, base);            // vloer, kop rechts
      match(xl, sh, xm, top, MATCH_GAP_ROOF); // dak links, kop bij de nok
      match(xm, top, xr, sh, MATCH_GAP_ROOF); // dak rechts, kop bij de schouder
    }
    return lines.join("") + heads.join("");
  }


  /** k witte tegels op een rij met een rand grijze tegels: (k+2) × 3, grijs = 2k + 6. Grijs heeft ook arcering. */
  function tileBorderSvg(k, x0, y0, t) {
    var o = [];
    for (var r = 0; r < 3; r++) for (var c = 0; c < k + 2; c++) {
      var white = r === 1 && c >= 1 && c <= k;
      o.push('<rect class="' + (white ? "tile-white" : "tile-grey") + '" x="' + (x0 + c * t) + '" y="' + (y0 + r * t) + '" width="' + t + '" height="' + t + '" fill="' + (white ? "#ffffff" : "url(#lm-grey-hatch)") + '" stroke="#1e3a5f" stroke-width="1.5"/>');
    }
    return o.join("");
  }

  function patternSvg(p, alt) {
    var parts = [], x = 12, H, captions = [];
    if (p.kind === "matchHouses") {
      var u = 40; H = u * 1.6 + 48;
      p.steps.forEach(function (n) {
        parts.push('<g class="pattern-step" data-step="' + n + '">' + matchHousesSvg(n, x, 12, u) + "</g>");
        captions.push({ x: x + n * u / 2, text: n + (n === 1 ? " huisje" : " huisjes") });
        x += n * u + 46;
      });
    } else if (p.kind === "tileBorder") {
      var t = 26; H = 3 * t + 48;
      p.steps.forEach(function (k) {
        parts.push('<g class="pattern-step" data-step="' + k + '">' + tileBorderSvg(k, x, 12, t) + "</g>");
        captions.push({ x: x + (k + 2) * t / 2, text: k + (k === 1 ? " witte tegel" : " witte tegels") });
        x += (k + 2) * t + 34;
      });
    } else return "";
    var W = x - 20;
    var defs = '<defs><pattern id="lm-grey-hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#b9c3cd"/><line x1="0" y1="0" x2="0" y2="8" stroke="#7d8a97" stroke-width="2"/></pattern></defs>';
    var cap = captions.map(function (c) { return '<text class="pattern-caption" x="' + c.x.toFixed(1) + '" y="' + (H - 10) + '" text-anchor="middle" font-size="13">' + escXml(c.text) + "</text>"; }).join("");
    return '<svg class="viz-pattern" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="' + escXml(alt || "Patroon") + '" width="' + W + '" height="' + H + '" viewBox="0 0 ' + W + " " + H + '" fill="#1e3a5f" font-family="inherit">' + defs + parts.join("") + cap + "</svg>";
  }

  // ---------------------------------------------------------------- bouwplaten
  function netSvg(cells, alt) {
    var s = 30, pad = 4;
    var maxR = Math.max.apply(null, cells.map(function (c) { return c[0]; })), maxC = Math.max.apply(null, cells.map(function (c) { return c[1]; }));
    var W = (maxC + 1) * s + 2 * pad, H = (maxR + 1) * s + 2 * pad;
    var rects = cells.map(function (c) { return '<rect class="net-face" x="' + (pad + c[1] * s) + '" y="' + (pad + c[0] * s) + '" width="' + s + '" height="' + s + '" fill="#e8f1f8" stroke="#1e3a5f" stroke-width="2"/>'; }).join("");
    return '<svg class="viz-net" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="' + escXml(alt || "Bouwplaat") + '" width="' + W + '" height="' + H + '" viewBox="0 0 ' + W + " " + H + '">' + rects + "</svg>";
  }

  /** Rol een kubus over de bouwplaat: vouwbaar tot kubus ⇔ 6 aaneengesloten vierkanten die 6 verschillende vlakken raken. */
  function foldsToCube(cells) {
    if (!cells || cells.length !== 6) return false;
    var key = function (r, c) { return r + "," + c; }, set = {};
    cells.forEach(function (c) { set[key(c[0], c[1])] = true; });
    if (Object.keys(set).length !== 6) return false;
    var neg = function (v) { return [-v[0], -v[1], -v[2]]; }, vk = function (v) { return v.join(","); };
    var seen = {}, faces = {}, queue = [];
    var start = cells[0];
    seen[key(start[0], start[1])] = { down: [0, 0, -1], north: [0, 1, 0], east: [1, 0, 0] };
    queue.push(start);
    while (queue.length) {
      var cur = queue.shift(), st = seen[key(cur[0], cur[1])];
      faces[vk(st.down)] = true;
      var moves = [
        [0, 1, function (s) { return { down: s.east, north: s.north, east: neg(s.down) }; }],
        [0, -1, function (s) { return { down: neg(s.east), north: s.north, east: s.down }; }],
        [-1, 0, function (s) { return { down: s.north, north: neg(s.down), east: s.east }; }],
        [1, 0, function (s) { return { down: neg(s.north), north: s.down, east: s.east }; }]
      ];
      moves.forEach(function (m) {
        var nr = cur[0] + m[0], nc = cur[1] + m[1], k = key(nr, nc);
        if (set[k] && !seen[k]) { seen[k] = m[2](st); queue.push([nr, nc]); }
      });
    }
    return Object.keys(seen).length === 6 && Object.keys(faces).length === 6;
  }

  /** SVG voor optie `letter` van item `key`, alleen als de optietekst exact overeenkomt (tekst = alt-tekst). */
  function optionVisualSvg(key, letter, text) {
    var v = overrideFor(key);
    if (!v || v.type !== "optionNets" || !v.options[letter]) return null;
    var o = v.options[letter];
    if (text != null && String(text).trim() !== o.text) return null;
    return netSvg(o.cells, o.text);
  }

  /** Figuur (grafiek/patroon) bij de opgave, of null. */
  function figureSvg(key) {
    var v = overrideFor(key);
    if (!v) return null;
    if (v.type === "graph") return graphSvg(v.graph, v.alt);
    if (v.type === "pattern") return patternSvg(v.pattern, v.alt);
    return null;
  }

  /** Opgave-HTML met figuur: vóór de eerste genummerde vervolgvraag ("\n1. "), anders erachter. */
  function promptHtmlWithFigure(key, prompt, esc) {
    var svg = figureSvg(key);
    if (!svg) return null;
    var s = String(prompt || ""), m = s.match(/\n\s*1\.\s/), cut = m ? m.index : s.length;
    var fig = '<span class="viz-figure">' + svg + "</span>";
    return esc(s.slice(0, cut)) + fig + esc(s.slice(cut).replace(/^\n/, ""));
  }

  function overrideFor(key) {
    return Object.prototype.hasOwnProperty.call(VISUAL_OVERRIDES, key) ? VISUAL_OVERRIDES[key] : null;
  }

  /**
   * Veld-HTML met turf-SVG's op de plek van de ASCII. `esc` = HTML-escape van de pagina.
   * Geen marks voor dit veld, of een `find` niet (precies één keer) gevonden → null
   * (pagina toont dan gewoon de tekst; check-visuals.js vangt dat af).
   */
  function fieldHtmlWithVisual(key, field, text, esc) {
    var v = overrideFor(key);
    if (!v || v.type !== "turf") return null;
    var marks = (v.marks || []).filter(function (m) { return m.field === field; });
    if (!marks.length) return null;
    var s = String(text || "");
    var spots = [];
    for (var i = 0; i < marks.length; i++) {
      var m = marks[i], at = s.indexOf(m.find);
      if (at < 0 || s.indexOf(m.find, at + 1) >= 0) return null;
      var off = m.find.indexOf(m.ascii);
      if (off < 0) return null;
      spots.push({ start: at + off, end: at + off + m.ascii.length, mark: m });
    }
    spots.sort(function (a, b) { return a.start - b.start; });
    for (var j = 1; j < spots.length; j++) if (spots[j].start < spots[j - 1].end) return null;
    var html = "", pos = 0;
    spots.forEach(function (sp) {
      html += esc(s.slice(pos, sp.start)) + '<span class="viz-inline">' + markSvg(sp.mark, v.size) + "</span>";
      pos = sp.end;
    });
    return html + esc(s.slice(pos));
  }

  function promptHtmlWithVisual(key, prompt, esc) { return fieldHtmlWithVisual(key, "prompt", prompt, esc); }
  function answerHtmlWithVisual(key, answer, esc) { return fieldHtmlWithVisual(key, "answer", answer, esc); }

  return {
    VISUAL_OVERRIDES: VISUAL_OVERRIDES,
    parseTallyAscii: parseTallyAscii,
    tallySvg: tallySvg,
    tallySvgParts: tallySvgParts,
    tallyWords: tallyWords,
    markSvg: markSvg,
    overrideFor: overrideFor,
    fieldHtmlWithVisual: fieldHtmlWithVisual,
    promptHtmlWithVisual: promptHtmlWithVisual,
    answerHtmlWithVisual: answerHtmlWithVisual,
    graphSvg: graphSvg,
    patternSvg: patternSvg,
    netSvg: netSvg,
    foldsToCube: foldsToCube,
    optionVisualSvg: optionVisualSvg,
    figureSvg: figureSvg,
    promptHtmlWithFigure: promptHtmlWithFigure
  };
});
