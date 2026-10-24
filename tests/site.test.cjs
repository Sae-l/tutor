const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { runInNewContext } = require('node:vm');
const { join } = require('node:path');

function fixture(clipboard) {
  const element = (extra = {}) => ({
    hidden: true, events: {},
    addEventListener(name, handler) { this.events[name] = handler; },
    ...extra,
  });
  const inputs = ['erklaer', 'tipp', 'check'].map(value => element({ value }));
  const answers = inputs.map(input => element({ id: `preview-${input.value}` }));
  const controls = element({ querySelectorAll: () => inputs });
  const button = element({ textContent: 'Kopieren', dataset: { copy: 'hilfe' } });
  const status = element();
  const link = element();
  const summary = { focus() { this.focused = true; } };
  const menu = element({ open: true, querySelectorAll: () => [link], querySelector: () => summary });
  const selectors = { '.preview-controls': controls, '#copy-status': status, '.mobile-nav': menu };
  const timers = [];
  runInNewContext(readFileSync(join(__dirname, '../docs/site.js'), 'utf8'), {
    document: {
      querySelector: selector => selectors[selector],
      querySelectorAll: selector => selector === '.preview-answer' ? answers : [button],
    },
    navigator: { clipboard }, setTimeout: handler => timers.push(handler),
  });
  return { inputs, answers, controls, button, status, menu, link, summary, timers };
}

test('each mode shows exactly its own answer', () => {
  const f = fixture();
  assert.equal(f.controls.hidden, false);
  for (const input of f.inputs) {
    input.events.change();
    assert.deepEqual(f.answers.filter(a => !a.hidden).map(a => a.id), [`preview-${input.value}`]);
  }
});

test('copy success and unavailable clipboard both leave a usable button', async () => {
  let copied;
  const success = fixture({ writeText: async text => { copied = text; } });
  const failure = fixture();
  for (const f of [success, failure]) {
    assert.equal(f.button.hidden, false);
    await f.button.events.click();
    assert.ok(f.status.textContent);
    assert.equal(f.button.textContent, f === success ? 'Kopiert' : 'Bitte Text markieren');
    f.timers[0]();
    assert.equal(f.button.textContent, 'Kopieren');
  }
  assert.equal(copied, 'hilfe');
});

test('mobile links close menu; Escape returns focus without intercepting other keys', () => {
  const f = fixture();
  f.menu.events.keydown({ key: 'Tab' });
  assert.equal(f.menu.open, true);
  f.link.events.click();
  assert.equal(f.menu.open, false);
  f.menu.open = true;
  f.menu.events.keydown({ key: 'Escape' });
  assert.equal(f.menu.open, false);
  assert.equal(f.summary.focused, true);
});
