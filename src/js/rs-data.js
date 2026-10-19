/* rs-data: reads public JSON (e.g. what gitrecon gathers into redscope-pl/.github)
   into accessible lists and tiles. A plain script, no dependencies; works as
   <script src> or inlined. Markup:

     <ul class="rs-feed" data-rs-src="https://…/events.json"
         data-rs-title="repo.name" data-rs-url="html_url" data-rs-date="created_at"
         data-rs-kind="type" data-rs-limit="10">
       <li>…what shows when there is no script or no data…</li>
     </ul>

   data-rs-from: dotted path to the array inside the JSON (default: the JSON
   itself). data-rs-view="tiles": data-rs-value as the big number, data-rs-title
   as its label. Text goes in as text, never as HTML; links only http(s). */
(function (root) {
  "use strict";

  function pick(obj, path) {
    if (!path) return undefined;
    return path.split(".").reduce(function (o, k) { return o == null ? undefined : o[k]; }, obj);
  }

  function records(json, from) {
    var list = from ? pick(json, from) : json;
    return Array.isArray(list) ? list : [];
  }

  function safeUrl(value, base) {
    if (typeof value !== "string" || !value) return null;
    try {
      var url = new URL(value, base);
      return url.protocol === "https:" || url.protocol === "http:" ? url.href : null;
    } catch (e) {
      return null;
    }
  }

  function text(value) {
    return value == null ? "" : String(value);
  }

  // One record as the plain fields a list item needs.
  function entry(rec, fields, base) {
    var date = pick(rec, fields.date);
    var parsed = date ? new Date(date) : null;
    return {
      title: text(pick(rec, fields.title)),
      url: safeUrl(pick(rec, fields.url), base),
      kind: text(pick(rec, fields.kind)),
      note: text(pick(rec, fields.note)),
      value: text(pick(rec, fields.value)),
      date: parsed && !isNaN(parsed) ? parsed : null,
    };
  }

  function fieldsOf(el) {
    var d = el.dataset;
    return { title: d.rsTitle, url: d.rsUrl, date: d.rsDate, kind: d.rsKind, note: d.rsNote, value: d.rsValue };
  }

  function add(parent, tag, cls, content) {
    var node = parent.ownerDocument.createElement(tag);
    if (cls) node.className = cls;
    if (content != null) node.textContent = content;
    parent.appendChild(node);
    return node;
  }

  function render(el, json) {
    var fields = fieldsOf(el);
    var limit = parseInt(el.dataset.rsLimit || "20", 10);
    var base = el.ownerDocument.location ? el.ownerDocument.location.href : undefined;
    var list = records(json, el.dataset.rsFrom).slice(0, limit).map(function (r) { return entry(r, fields, base); });
    var tiles = el.dataset.rsView === "tiles";
    el.textContent = "";
    list.forEach(function (e) {
      if (tiles) {
        var tile = add(el, "div", "rs-tile");
        add(tile, "b", null, e.value);
        add(tile, "span", null, e.title);
        return;
      }
      var li = add(el, "li");
      if (e.kind) add(li, "span", "rs-kind", e.kind);
      if (e.url) add(li, "a", null, e.title || e.url).href = e.url;
      else add(li, "span", null, e.title);
      if (e.date) {
        var time = add(li, "time", null, e.date.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" }));
        time.dateTime = e.date.toISOString();
      }
      if (e.note) add(li, "span", "rs-note", e.note);
    });
    if (!list.length) add(el, tiles ? "p" : "li", "rs-note", "Nothing here yet.");
  }

  function fail(el) {
    var note = el.ownerDocument.createElement("p");
    note.className = "rs-data-error";
    note.setAttribute("role", "status");
    note.textContent = "Could not load the data; what is shown may be old.";
    el.parentNode.insertBefore(note, el.nextSibling);
  }

  function load(el) {
    el.setAttribute("aria-busy", "true");
    return fetch(el.dataset.rsSrc, { headers: { Accept: "application/json" } })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (json) { render(el, json); })
      .catch(function () { fail(el); })
      .then(function () { el.removeAttribute("aria-busy"); });
  }

  function init(doc) {
    Array.prototype.forEach.call((doc || document).querySelectorAll("[data-rs-src]"), load);
  }

  var api = { pick: pick, records: records, safeUrl: safeUrl, entry: entry, render: render, load: load, init: init };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else {
    root.rsData = api;
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { init(); });
    else init();
  }
})(this);
