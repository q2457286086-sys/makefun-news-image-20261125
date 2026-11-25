// Entry point for the news-image-20261125 make.fun submission.
//
// Copies the composed front page (entry.png, next to this file) to the
// output location the scoring harness expects: $MAKEFUN_OUTPUT_DIR when
// set, otherwise /output/entry.png. The copy is byte-for-byte identical,
// so repeated runs produce identical output.
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");

if (!existsSync(source)) {
  console.error(`entry.png not found at ${source}`);
  process.exit(1);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const target = join(outDir, "entry.png");
mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
console.log(`copied entry.png -> ${target}`);
