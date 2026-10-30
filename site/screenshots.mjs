// Screenshots of every page language at 1280 and 375 px, light and dark, plus overflow check.
// Usage: python -m http.server 8767 --directory docs, then node site/screenshots.mjs http://localhost:8767/ <out-dir>
// Needs global playwright-core and an installed Chrome (as docs/assets/hero/render.mjs).
import { execSync } from "node:child_process";
import { createRequire } from "node:module";
import { mkdirSync } from "node:fs";
import { join } from "node:path";

const { chromium } = await import("playwright-core").catch(() =>
  createRequire(join(execSync("npm root -g", { encoding: "utf8" }).trim(), "_"))("playwright-core"));
const [base, out] = process.argv.slice(2);
mkdirSync(out, { recursive: true });
const browser = await chromium.launch({ channel: "chrome" });
const problems = [];
for (const lang of ["de", "en", "tr", "fr", "ar", "fa"]) {
  for (const width of [1280, 1024, 375]) {
    for (const scheme of ["light", "dark"]) {
      const page = await browser.newPage({ viewport: { width, height: 900 }, colorScheme: scheme, reducedMotion: "reduce" });
      await page.goto(base + (lang === "de" ? "" : lang + "/"));
      await page.evaluate(() => document.fonts.ready);
      const bad = await page.evaluate(() => {
        const vw = document.documentElement.clientWidth, hits = [];
        if (document.documentElement.scrollWidth > vw) hits.push(`page scrollWidth ${document.documentElement.scrollWidth} > ${vw}`);
        for (const el of document.querySelectorAll("body *")) {
          if (el.closest("nav, .flow, math, dialog, .skip, [hidden]")) continue;
          const r = el.getBoundingClientRect();
          if (r.width && (r.right > vw + 1 || r.left < -1)) hits.push(`${el.tagName.toLowerCase()}.${el.className} ${Math.round(r.left)}..${Math.round(r.right)}`);
          if (el.scrollWidth > el.clientWidth + 1 && getComputedStyle(el).overflowX === "hidden") hits.push(`clipped ${el.tagName.toLowerCase()}.${el.className}`);
        }
        return hits.slice(0, 5);
      });
      if (bad.length) problems.push(`${lang} ${width} ${scheme}: ${bad.join("; ")}`);
      if (width !== 1024) await page.screenshot({ path: join(out, `${lang}-${width}-${scheme}.png`), fullPage: true });
      if (width === 375 && scheme === "light") {
        await page.click(".top .lang-btn");
        await page.screenshot({ path: join(out, `${lang}-375-dialog.png`) });
      }
      await page.close();
    }
  }
}
await browser.close();
console.log(problems.length ? problems.join("\n") : "no overflow");
