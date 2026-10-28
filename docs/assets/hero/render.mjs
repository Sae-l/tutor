// Erzeugt docs/assets/hero-light.gif, hero-dark.gif und das Vorschaubild hero-light.png (og:image) aus hero.html.
// Braucht playwright-core (nicht Teil des Repos), Chromium und ffmpeg:
//   CHROME=/pfad/chrome FFMPEG=/pfad/ffmpeg node docs/assets/hero/render.mjs
// Die ffmpeg-Version aus ms-playwright reicht nicht (kein PNG-Eingang). FRAMES setzt optional den Ordner für Zwischenbilder.
import { chromium } from "playwright-core";
import { execFileSync } from "node:child_process";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const fps = 15, width = 960;
const browser = await chromium.launch({ executablePath: process.env.CHROME });
const page = await browser.newPage({ viewport: { width: 1200, height: 600 } });

for (const theme of ["light", "dark"]) {
  const frames = mkdtempSync(join(process.env.FRAMES ?? tmpdir(), `hero-${theme}-`));
  await page.goto(`${pathToFileURL(join(here, "hero.html"))}?render&theme=${theme}`);
  await page.evaluate(() => document.fonts.ready);
  if (theme === "light") {
    await page.evaluate(() => window.render(3.5)); // erklär-Szene vollständig sichtbar
    await page.screenshot({ path: join(here, "..", "hero-light.png") });
  }
  const loop = await page.evaluate(() => window.LOOP);
  for (let i = 0; i < loop * fps; i++) {
    await page.evaluate(t => window.render(t), i / fps);
    await page.screenshot({ path: join(frames, `${String(i).padStart(4, "0")}.png`) });
  }
  const out = join(here, "..", `hero-${theme}.gif`);
  execFileSync(process.env.FFMPEG ?? "ffmpeg", ["-y", "-loglevel", "error", "-framerate", String(fps), "-i", join(frames, "%04d.png"),
    "-vf", `scale=${width}:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=none:diff_mode=rectangle`,
    "-loop", "0", out]);
  rmSync(frames, { recursive: true });
  console.log(out);
}
await browser.close();
