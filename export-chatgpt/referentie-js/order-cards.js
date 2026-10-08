/**
 * LeerMees — ordening-items als losse kaartjes (leerdoel.html; ook in node voor tests).
 *
 * extractOrderCards(item) → { ok, lead, cards[], tail, sep } of { ok:false, reason }.
 * - Kandidaat: format "ordenen", of opgave met "op volgorde" / "zet … van … naar …".
 * - Lijst = na de laatste ": " (dubbele punt + spatie; "8:50" telt dus niet); staat er daarna
 *   eerst nog een vraag of haakje ("…? (dichtst → verst) A · B"), dan begint de lijst daarna.
 *   Of: lijst op de volgende regel(s), als opsommingsregels ("· x", "- x") of één regel met " · ".
 * - Scheidingsteken: " · ", anders " en " / ", " (zoals "3 × 8 en 5 × 5 en 2 × 10").
 * - Controle tegen het antwoord (dat blijft ongewijzigd): het antwoord "x → y → z" moet
 *   evenveel delen hebben als er kaartjes zijn, en elk kaartje moet bij precies één deel
 *   passen (zelfde tekst, begin van de tekst, of dezelfde getallen). Anders: tekst-fallback.
 * - Kaartjes blijven in de volgorde van de opgave (niet gesorteerd, niet geschud).
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.LeerMeesOrderCards = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  var CANDIDATE_RE = /op volgorde|\bzet\b[^.?:]{0,60}\bvan\b[^.?:]{1,40}\bnaar\b|\bvan (?:klein|groot|kort|lang|licht|zwaar|vroeg|laat|weinig|veel)\w* naar\b/i;

  function isCandidate(item) {
    if (!item) return false;
    if (/^ordenen$/i.test(String(item.format || "").trim())) return true;
    return CANDIDATE_RE.test(String(item.prompt || ""));
  }

  function norm(s) {
    return String(s || "")
      .toLowerCase()
      .replace(/\([^)]*\)/g, " ")
      .replace(/[“”„"']/g, "")
      .replace(/\s+/g, " ")
      .replace(/[.,;:!?]+$/, "")
      .trim();
  }

  function numbers(s) {
    var t = String(s || ""), prev;
    do { prev = t; t = t.replace(/(\d)\.(\d{3})(?!\d)/g, "$1$2"); } while (t !== prev); // 1.005.000 → 1005000
    return (t.replace(/(\d),(\d)/g, "$1.$2").match(/\d+(?:\.\d+)?/g) || []).map(Number);
  }

  function tokens(s) { return norm(s).split(/[\s—–-]+/).filter(Boolean); }

  function numsSubset(a, b) {
    var pool = b.slice();
    return a.every(function (x) { var i = pool.indexOf(x); if (i < 0) return false; pool.splice(i, 1); return true; });
  }

  function matches(card, part) {
    var c = norm(card), p = norm(part);
    if (!c || !p) return false;
    // zelfde tekst, of de een is het begin van de ander (op woordgrens)
    if (c === p || c.indexOf(p + " ") === 0 || p.indexOf(c + " ") === 0) return true;
    // antwoord noemt alleen het label: "C → A → …" bij kaartjes "lint C", "beker R — …"
    if (/^[a-z]$|^[a-z]\d?$/.test(p) && tokens(card).indexOf(p) >= 0) return true;
    // dezelfde getallen (kaartje ⊆ antwoorddeel, incl. getallen tussen haakjes)
    var cn = numbers(card);
    if (cn.length && numsSubset(cn, numbers(part))) return true;
    return false;
  }

  /** Kaartjes ↔ antwoorddelen één-op-één koppelen (kleine n → backtracking). */
  function matchAll(cards, parts) {
    var used = parts.map(function () { return false; });
    function go(i) {
      if (i === cards.length) return true;
      for (var j = 0; j < parts.length; j++) {
        if (!used[j] && matches(cards[i], parts[j])) { used[j] = true; if (go(i + 1)) return true; used[j] = false; }
      }
      return false;
    }
    return go(0);
  }

  function fail(reason) { return { ok: false, reason: reason }; }

  var BULLET_RE = /^\s*[·•\-]\s+/;
  // Verhouding/schaal "1 : 100" (cijfer, spatie, dubbele punt, spatie, cijfer) is geen lijst-dubbelepunt.
  var RATIO_RE = /\d\s:\s\d/g;

  /** Positie van de laatste ": " die een lijst inleidt (dus niet die in "schaal 1 : 100"); -1 als er geen is. */
  function listColon(line) {
    var at = -1, re = /:\s/g, m;
    while ((m = re.exec(line))) {
      var i = m.index;
      if (i >= 2 && /\d\s/.test(line.slice(i - 2, i)) && /\d/.test(line.charAt(i + 2))) continue;
      at = i;
    }
    return at;
  }

  /** Kaartjes uit één lijst-tekst; lead-in-vraag/haakje vóór het eerste kaartje gaat naar `pre`. */
  function splitList(list) {
    var sep, first, pre = "";
    if (list.indexOf(" · ") >= 0) sep = "·";
    else if (/\sen\s/.test(list) || /,\s/.test(list)) sep = "en";
    else return null;
    var sepRe = sep === "·" ? /\s+·\s+/ : /\s+en\s+|,\s+/;
    // alleen in het stuk vóór het eerste scheidingsteken zoeken naar "? " of ") "
    first = list.split(sepRe)[0];
    var cut = Math.max(first.lastIndexOf("? "), first.lastIndexOf(") "));
    if (cut >= 0 && first.slice(cut + 2).trim()) { pre = list.slice(0, cut + 1); list = list.slice(cut + 2); }
    return { sep: sep, pre: pre, cards: list.split(sepRe) };
  }

  function extractOrderCards(item) {
    if (!isCandidate(item)) return fail("geen ordening-item");
    var prompt = String(item.prompt || "");
    if (/```/.test(prompt)) return fail("opgave bevat een tekening/codeblok");
    var lines = prompt.split("\n");
    var lead, sp, restLines, tail = "";
    var colon = listColon(lines[0]);
    if (colon >= 0 && lines[0].slice(colon + 2).trim()) {
      // A. lijst op dezelfde regel na ": "
      lead = lines[0].slice(0, colon + 1);
      sp = splitList(lines[0].slice(colon + 2));
      if (!sp) return fail("geen scheidingsteken (· / en / ,) in de lijst");
      restLines = lines.slice(1);
    } else if (lines.length > 1) {
      // B. lijst op de volgende regel(s): opsommingsregels "· x" / "- x", of één regel met " · "
      lead = lines[0];
      var i = 1, bullets = [];
      while (i < lines.length && BULLET_RE.test(lines[i])) { bullets.push(lines[i].replace(BULLET_RE, "").trim()); i++; }
      if (bullets.length === 1 && bullets[0].indexOf(" · ") >= 0) sp = { sep: "·", pre: "", cards: bullets[0].split(/\s+·\s+/) };
      else if (bullets.length >= 2) sp = { sep: "regels", pre: "", cards: bullets };
      else if (lines[1].indexOf(" · ") >= 0) { sp = { sep: "·", pre: "", cards: lines[1].split(/\s+·\s+/) }; i = 2; }
      else return fail("geen lijst gevonden");
      restLines = lines.slice(i);
    } else return fail("geen ': ' voor de lijst");
    if (sp.pre) lead += " " + sp.pre;
    var cards = sp.cards;
    // staartzin na het laatste kaartje ("… · 2 m. Zet ze …")
    var last = cards[cards.length - 1];
    var tm = last.match(/^(.*?[^\d\s])([.?!])\s+(\S.*)$/);
    if (tm) { cards[cards.length - 1] = tm[1]; tail = tm[2] === "." ? tm[3] : tm[2] + " " + tm[3]; }
    cards = cards.map(function (c) { return c.replace(/\s*\.$/, "").trim(); });
    tail = [tail].concat(restLines).join("\n").trim();
    if (cards.length < 2 || cards.length > 8) return fail("aantal kaartjes " + cards.length);
    if (cards.some(function (c) { return !c || c.length > 70 || /[:?]\s/.test(c.replace(RATIO_RE, "")); })) return fail("kaartje te lang of bevat zin");
    var ans = String(item.answer || "");
    // meerstaps-item ("1) 37 → 70 → 73 · 2) 37 · 3) nee"): alleen stap 1 is de ordening
    if (/^\s*1\)\s*/.test(ans)) ans = ans.replace(/^\s*1\)\s*/, "").split(/\s+·\s+(?=\d\)\s)/)[0];
    var parts = ans.split(/\s*→\s*/).map(function (p) { return p.trim(); }).filter(Boolean);
    if (parts.length < 2) return fail("antwoord is geen '→'-reeks");
    if (parts.length !== cards.length) return fail("aantal kaartjes (" + cards.length + ") ≠ delen in antwoord (" + parts.length + ")");
    if (!matchAll(cards, parts)) return fail("kaartjes passen niet één-op-één bij het antwoord");
    return { ok: true, lead: lead.trim(), cards: cards, tail: tail, sep: sp.sep };
  }

  /** Opgave-HTML met kaartjes, of null (→ pagina toont gewone tekst). */
  function promptHtmlWithCards(item, esc) {
    var r = extractOrderCards(item);
    if (!r.ok) return null;
    return (
      '<span class="order-lead">' + esc(r.lead) + "</span>" +
      '<span class="order-cards" role="list" aria-label="Kaartjes om te ordenen">' +
      r.cards.map(function (c) { return '<span class="order-card" role="listitem">' + esc(c) + "</span>"; }).join("") +
      "</span>" +
      (r.tail ? '<span class="order-tail">' + esc(r.tail) + "</span>" : "")
    );
  }

  return { isCandidate: isCandidate, extractOrderCards: extractOrderCards, promptHtmlWithCards: promptHtmlWithCards, _matches: matches };
});
