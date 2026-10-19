// Unit tests of the pack's scripts (node --test); the DOM parts are seen in docs/preview.html.
const test = require("node:test");
const assert = require("node:assert");
const data = require("../../src/js/rs-data.js");
const scramble = require("../../src/js/rs-scramble.js");

test("pick follows dotted paths and survives missing ones", () => {
  assert.strictEqual(data.pick({ repo: { name: "a/b" } }, "repo.name"), "a/b");
  assert.strictEqual(data.pick({ repo: null }, "repo.name"), undefined);
  assert.strictEqual(data.pick({}, undefined), undefined);
});

test("records takes the array, from a path or the root", () => {
  assert.deepStrictEqual(data.records([1, 2]), [1, 2]);
  assert.deepStrictEqual(data.records({ items: [3] }, "items"), [3]);
  assert.deepStrictEqual(data.records({ items: "no" }, "items"), []);
});

test("safeUrl lets through only http(s)", () => {
  assert.strictEqual(data.safeUrl("https://github.com/x"), "https://github.com/x");
  assert.strictEqual(data.safeUrl("/rel", "https://redscope.pl/a/"), "https://redscope.pl/rel");
  assert.strictEqual(data.safeUrl("javascript:alert(1)"), null);
  assert.strictEqual(data.safeUrl("data:text/html,x"), null);
  assert.strictEqual(data.safeUrl(42), null);
});

test("entry maps a GitHub event", () => {
  const e = data.entry(
    { type: "PushEvent", repo: { name: "redscope-pl/x" }, created_at: "2026-10-19T10:00:00Z" },
    { title: "repo.name", kind: "type", date: "created_at", url: "nope" },
  );
  assert.strictEqual(e.title, "redscope-pl/x");
  assert.strictEqual(e.kind, "PushEvent");
  assert.strictEqual(e.url, null);
  assert.strictEqual(e.date.toISOString(), "2026-10-19T10:00:00.000Z");
});

test("scramble frames settle from the left and keep spaces", () => {
  const zero = () => 0;
  assert.strictEqual(scramble.frame("AB CD", 0, zero), "AA AA");
  assert.strictEqual(scramble.frame("AB CD", 0.4, zero), "AB AA");
  assert.strictEqual(scramble.frame("AB CD", 1, zero), "AB CD");
});
