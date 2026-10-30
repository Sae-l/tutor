"""PROTOTYPE builder for Sae-l/tutor #98: injects three language-button variants into docs/index.html."""
import sys, pathlib

src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
html = src.read_text(encoding="utf-8")

LANGS = [("de", "Deutsch", "ltr"), ("ar", "العربية", "rtl"), ("tr", "Türkçe", "ltr"),
         ("fr", "Français", "ltr"), ("en", "English", "ltr"), ("fa", "فارسی", "rtl")]

def items(cls):
    return "".join(
        f'<a class="{cls}" href="#" data-goto="{c}" hreflang="{c}" lang="{c}"'
        f'{" aria-current=\"page\"" if c == "de" else ""}>'
        f'<span>{n}</span> <small>[{c}]</small></a>' for c, n, _ in LANGS)

GLOBE = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true" style="stroke:currentColor" '
         'stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/></svg>')

CSS = """
/* ===== PROTOTYPE #98 Sprachknopf (wegwerfen) ===== */
.top nav { margin-inline-start: auto; }
.lang { position: relative; margin-inline-start: 1.25rem; font-family: var(--sans); }
.lang [data-v] { display: none; }
html[data-variant="A"] .lang [data-v="A"], html[data-variant="B"] .lang [data-v="B"], html[data-variant="C"] .lang [data-v="C"] { display: contents; }
.lang-btn {
  min-height: 44px; padding: 0 .9rem; border-radius: 999px; border: 1px solid var(--hairline);
  background: var(--sheet); color: var(--ink); font: 600 .9375rem var(--sans); cursor: pointer;
  display: inline-flex; align-items: center; gap: .45rem; transition: border-color .2s, background .2s;
}
.lang-btn:hover { border-color: var(--pencil); }
.lang-btn[aria-expanded="true"] { background: var(--wash); border-color: var(--accent); }
.lang-btn .code { font: 500 .8125rem var(--mono); letter-spacing: .02em; }
.lang-btn .caret { width: .5rem; height: .5rem; border-inline-end: 1.5px solid currentColor; border-bottom: 1.5px solid currentColor;
  transform: translateY(-2px) rotate(45deg); transition: transform .2s var(--ease); }
.lang-btn[aria-expanded="true"] .caret { transform: translateY(1px) rotate(-135deg); }
.lang-item {
  min-height: 44px; padding: 0 1rem; border-radius: 999px; border: 1px solid var(--hairline);
  background: var(--sheet); color: var(--ink); font: 500 .9375rem var(--sans); text-decoration: none;
  display: inline-flex; align-items: center; justify-content: space-between; gap: .75rem; transition: background .2s, border-color .2s;
}
.lang-item:hover { color: var(--ink); border-color: var(--pencil); }
.lang-item small { font: 400 .75rem var(--mono); color: var(--pencil); }
.lang-item[aria-current="page"] { background: var(--wash); border-color: var(--accent); }
.lang-item[aria-current="page"] small { color: var(--accent); }
.lang-item[lang="ar"], .lang-item[lang="fa"] { font-family: "Noto Naskh Arabic", var(--sans); }

/* A: Ausklappliste unter dem Knopf */
.pop { position: absolute; inset-inline-end: 0; top: calc(100% + .5rem); z-index: 30; display: grid; gap: .4rem;
  min-width: 13rem; padding: .6rem; background: var(--sheet); border: 1px solid var(--hairline); border-radius: 1rem; box-shadow: var(--shadow); }
.pop[hidden] { display: none; }

/* B: Chipzeile unter der Kopfzeile, ganze Breite */
.strip { position: absolute; inset-inline: 0; top: 100%; z-index: 9; background: color-mix(in srgb, var(--paper) 94%, transparent);
  backdrop-filter: blur(10px); border-bottom: 1px solid var(--hairline); }
.strip[hidden] { display: none; }
.strip .row { max-width: 1200px; margin: 0 auto; padding: .75rem var(--gutter); display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; }
.strip .row b { font: 500 .8125rem var(--mono); color: var(--pencil); margin-inline-end: .5rem; }

/* C: Dialog mit Raster, auf dem Handy als Blatt von unten */
dialog.sheet { border: 1px solid var(--hairline); border-radius: 1.25rem; background: var(--sheet); color: var(--ink);
  padding: 1.5rem; width: min(30rem, calc(100vw - 2rem)); box-shadow: var(--shadow); }
dialog.sheet::backdrop { background: rgba(22,20,18,.35); backdrop-filter: blur(2px); }
dialog.sheet h2 { font: 700 1.25rem var(--sans); margin-bottom: 1rem; }
dialog.sheet .grid { display: grid; grid-template-columns: 1fr 1fr; gap: .5rem; }
dialog.sheet .lang-item { border-radius: .75rem; min-height: 56px; }
dialog.sheet .close { position: absolute; inset-inline-end: 1rem; top: 1rem; }

@media (max-width: 767px) {
  .top { align-items: center; }
  .top nav { order: 2; margin-inline-start: 0; }
  .lang { order: 1; margin-inline-start: auto; }
  .pop { min-width: min(15rem, calc(100vw - 2rem)); }
  dialog.sheet { margin: auto auto 0; width: 100vw; max-width: 100vw; border-radius: 1.25rem 1.25rem 0 0; padding-bottom: 2rem; }
}

/* RTL-Vorschau: Mathe und Code bleiben LTR */
html[dir="rtl"] math, html[dir="rtl"] code, html[dir="rtl"] pre { direction: ltr; unicode-bidi: isolate; }
html[dir="rtl"] body { font-family: "Noto Naskh Arabic", var(--serif); }

/* Umschalter des Prototyps, gehört nicht zum Design */
.proto-bar { position: fixed; left: 50%; bottom: 1rem; transform: translateX(-50%); z-index: 99; direction: ltr;
  display: flex; align-items: center; gap: .5rem; padding: .4rem; border-radius: 999px; background: #111; color: #fff;
  font: 600 .8125rem system-ui, sans-serif; box-shadow: 0 6px 24px rgba(0,0,0,.35); }
.proto-bar button { all: unset; cursor: pointer; padding: .4rem .75rem; border-radius: 999px; background: #333; }
.proto-bar button:hover { background: #555; }
.proto-bar span { padding: 0 .5rem; white-space: nowrap; }
"""

BTN = lambda ctl, extra="": (f'<button class="lang-btn" type="button" aria-expanded="false" aria-controls="{ctl}"{extra} '
                             f'aria-label="Sprache der Seite: Deutsch">{GLOBE}<span class="code">DE</span><span class="caret"></span></button>')

MARKUP = f"""
    <div class="lang">
      <div data-v="A">{BTN("lang-pop")}
        <div class="pop" id="lang-pop" hidden>{items("lang-item")}</div></div>
      <div data-v="B">{BTN("lang-strip")}</div>
      <div data-v="C">{BTN("lang-dialog")}</div>
    </div>"""

STRIP = f"""<div class="strip" id="lang-strip" hidden><div class="row"><b>Seitensprache</b>{items("lang-item")}</div></div>"""
DIALOG = f"""
<dialog class="sheet" id="lang-dialog" aria-labelledby="lang-dialog-h">
  <h2 id="lang-dialog-h">Seitensprache</h2>
  <button class="lang-btn close" type="button" aria-label="Schließen">✕</button>
  <div class="grid">{items("lang-item")}</div>
</dialog>"""

JS = """
<script>
/* PROTOTYPE #98: Varianten-Umschalter und simulierte Sprachwahl (Links zeigen noch ins Leere) */
(() => {
  const V = { A: 'Ausklappliste', B: 'Chipzeile', C: 'Dialog / Blatt' }, keys = Object.keys(V);
  const NAMES = { de: 'Deutsch', ar: 'العربية', tr: 'Türkçe', fr: 'Français', en: 'English', fa: 'فارسی' };
  const q = new URLSearchParams(location.search);
  const root = document.documentElement;
  const set = (k, val) => { q.set(k, val); history.replaceState(null, '', '?' + q + location.hash); };
  let v = keys.includes(q.get('variant')) ? q.get('variant') : 'A';
  const lang = l => {
    root.lang = l; root.dir = (l === 'ar' || l === 'fa') ? 'rtl' : 'ltr'; set('lang', l);
    document.querySelectorAll('.lang-btn:not(.close)').forEach(b => {
      b.querySelector('.code').textContent = l.toUpperCase();
      b.setAttribute('aria-label', 'Sprache der Seite: ' + NAMES[l]);
    });
    document.querySelectorAll('[data-goto]').forEach(a => a.dataset.goto === l ? a.setAttribute('aria-current', 'page') : a.removeAttribute('aria-current'));
    label();
  };
  const closeAll = () => {
    document.querySelectorAll('#lang-pop, #lang-strip').forEach(e => e.hidden = true);
    document.querySelectorAll('.lang-btn').forEach(b => b.setAttribute('aria-expanded', 'false'));
    const d = document.getElementById('lang-dialog'); if (d.open) d.close();
  };
  document.querySelectorAll('.lang-btn:not(.close)').forEach(b => b.addEventListener('click', e => {
    e.stopPropagation();
    const t = document.getElementById(b.getAttribute('aria-controls')), open = b.getAttribute('aria-expanded') !== 'true';
    closeAll();
    if (!open) return;
    b.setAttribute('aria-expanded', 'true');
    if (t.tagName === 'DIALOG') t.showModal(); else { t.hidden = false; t.querySelector('a').focus(); }
  }));
  document.querySelector('.sheet .close').addEventListener('click', closeAll);
  document.getElementById('lang-dialog').addEventListener('close', () => document.querySelectorAll('.lang-btn').forEach(b => b.setAttribute('aria-expanded', 'false')));
  document.getElementById('lang-dialog').addEventListener('click', e => { if (e.target.tagName === 'DIALOG') closeAll(); });
  document.addEventListener('click', e => { if (!e.target.closest('.pop, .strip')) closeAll(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeAll(); });
  // real page: href = '/tutor/<lang>/' + location.hash; here we only simulate
  document.querySelectorAll('[data-goto]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); lang(a.dataset.goto); closeAll(); }));

  const bar = document.createElement('div'); bar.className = 'proto-bar';
  bar.innerHTML = '<button data-d="-1">←</button><span></span><button data-d="1">→</button>';
  document.body.append(bar);
  const label = () => bar.querySelector('span').textContent = `Prototyp ${v} (${V[v]}) · ${root.lang} · ${root.dir}`;
  const show = nv => { v = nv; root.dataset.variant = v; set('variant', v); closeAll(); label(); };
  bar.addEventListener('click', e => { const d = +e.target.dataset.d; if (d) show(keys[(keys.indexOf(v) + d + keys.length) % keys.length]); });
  document.addEventListener('keydown', e => {
    if (e.target.closest('input, textarea, [contenteditable]')) return;
    if (e.key === 'ArrowRight') show(keys[(keys.indexOf(v) + 1) % keys.length]);
    if (e.key === 'ArrowLeft') show(keys[(keys.indexOf(v) + keys.length - 1) % keys.length]);
  });
  show(v); lang(NAMES[q.get('lang')] ? q.get('lang') : 'de');
})();
</script>
"""

def once(hay, needle, repl):
    assert hay.count(needle) == 1, needle
    return hay.replace(needle, repl)

html = once(html, "</style>", CSS + "</style>")
html = once(html, "<title>", "<title>PROTOTYP #98 · ")
html = once(html, '<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"')
html = once(html, "    </nav>\n  </header>", "    </nav>" + MARKUP + "\n  </header>")
html = once(html, '<div class="progress" aria-hidden="true"></div>', STRIP + '\n<div class="progress" aria-hidden="true"></div>')
html = once(html, "</body>", DIALOG + JS + "</body>")
out.write_text(html, encoding="utf-8", newline="\n")
print("wrote", out)
