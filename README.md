[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/q2457286086-sys/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/q2457286086-sys/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

# The Daily Globe — 25 November 2026

A 1024×1024 newspaper front page summing up 25 November 2026's world news
in one image — an entry for the make.fun `news-image-20261125` bounty
("Sum up 25 November's world news in one image", $100 shared by the top 50).

## Stories covered

All headlines were checked against reports dated 25 November 2026:

- **Lead:** Nvidia's reinstated CEO Jensen Huang holds his first all-hands,
  apologises, says he made "some terrible mistakes" and is in therapy, as the
  comeback rally fades. The board reinstated him on Monday, 11 days after he
  resigned amid a 'spy' controversy, after President Trump intervened directly;
  shares soared 31% on Monday, regaining roughly $900 billion in market value.
  Huang testifies before Congress in early December.
- The CIA and the Office of the Director of National Intelligence suffer a
  cybersecurity breach of some unclassified information.
- NATO responds to reports Russia may launch a nuclear-armed satellite.
- Ukraine sea-drone fallout: a senior Libyan official wants Zelensky on a
  terrorism watchlist; Ukraine says its sea drones sank a Russian warship off
  Benghazi.
- China announces a shock corruption probe into a Politburo member; a US jury
  finds Huawei guilty of conspiracy to steal trade secrets and bank fraud.
- Hamas security chief killed in an Israeli air strike on Gaza City; deadly
  floods swamp tens of thousands in Gaza.
- Saudi Arabia condemns a 'terrorist attack' after the Riyadh PIF skyscraper
  was hit twice in a week.
- Trump awards Rudy Giuliani the Medal of Freedom and outlines a Cuba plan.
- Over 400,000 workers strike across Germany.
- Storms and a radar issue at Chicago O'Hare threaten messy Thanksgiving travel.
- Senegal gets the AFCON title back after a CAS ruling.
- UK police arrest two men after a break-in at Prince William's Norfolk home.

## Files

- `hero.png` — photorealistic image of Nvidia headquarters, Santa Clara, at dusk.
- `build_frontpage.py` — composes `entry.png` from `hero.png` with PIL
  (masthead, lead story, secondary stories, IN BRIEF band, footer).
- `entry.png` — the 1024×1024 submission image (≤ 1 MiB).
- `main.ts` — copies `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output/entry.png`).

## Run

```bash
python3 build_frontpage.py   # rebuild entry.png from hero.png
node main.ts                 # copy entry.png to the output directory
```
