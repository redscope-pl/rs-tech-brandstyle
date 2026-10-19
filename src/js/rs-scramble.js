/* rs-scramble: the title effect of the nexus drafts. Letters of an element with
   data-rs-scramble settle out of noise. The real words stay for screen readers
   (a hidden copy); nothing moves for visitors who ask for less motion; only
   elements holding plain text are touched. A plain script, no dependencies. */
(function (root) {
  "use strict";
  var CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";

  // The text at a step (0..1) of settling: settled letters come from the left.
  function frame(original, progress, random) {
    var settled = Math.floor(original.length * progress);
    return original.split("").map(function (ch, i) {
      if (i < settled || ch === " ") return ch;
      return CHARS[Math.floor(random() * CHARS.length)];
    }).join("");
  }

  function scramble(el) {
    var original = el.textContent;
    if (!original.trim() || el.children.length) return;
    var doc = el.ownerDocument;
    var real = doc.createElement("span");
    real.className = "rs-sr";
    real.textContent = original;
    var shown = doc.createElement("span");
    shown.setAttribute("aria-hidden", "true");
    el.textContent = "";
    el.appendChild(real);
    el.appendChild(shown);
    var steps = Math.min(30, original.length * 3), step = 0;
    var timer = setInterval(function () {
      step += 1;
      shown.textContent = frame(original, step / steps, Math.random);
      if (step >= steps) {
        clearInterval(timer);
        el.textContent = original;
      }
    }, 30);
  }

  function init(doc) {
    doc = doc || document;
    var view = doc.defaultView;
    if (view && view.matchMedia && view.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    Array.prototype.forEach.call(doc.querySelectorAll("[data-rs-scramble]"), scramble);
  }

  var api = { frame: frame, scramble: scramble, init: init };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else {
    root.rsScramble = api;
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { init(); });
    else init();
  }
})(this);
