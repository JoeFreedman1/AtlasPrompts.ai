# STATE.md: where Well Listed is right now

Updated by every session. Newest log entries at the top of the log. The dashboard and the daily operator read the "Key facts" table, so keep its labels exactly as they are and put values in the second column.

## Key facts

| Fact | Value |
|---|---|
| Launch date | 2026-09-30 |
| Current price | £12 launch price (days 1 to 14), £19 from 14 October 2026 |
| Launch price end date | 2026-10-13 (£12 ends at 11:59pm that night) |
| Gumroad link | https://welllisted.gumroad.com/l/well-listed-kit (live) |
| Sales page address | https://well-listed.netlify.app (Netlify connected to the repo; deploys from `main` when the site folder changes) |
| Sales page version live | A |
| Email tool | None. No sign-up form: the cheat sheet is a direct download and the site collects no personal data |
| Legal identity | Sole trader trading as Well Listed. No name or address anywhere in the site or repo; all sales through Gumroad as merchant of record; contact hello.welllisted@gmail.com |
| Ad budget cap | £0. Ads are for later, only once money kept from sales covers the £70 test budget (then Meta first) |
| Working branch | main (the launch kit was merged into main on 30 September 2026) |

## Current numbers (fill in from launch-kit/metrics/)

| Number | Yesterday | Last 7 days | Total to date |
|---|---|---|---|
| Sales | | | |
| Money kept after fees (£) | | | |
| Checkout page views | | | |
| Checkout conversion | | | |
| Email subscribers (total) | | | |
| Bio link clicks | | | |
| Short-form video views (all platforms) | | | |
| Pinterest impressions | | | |
| Ad spend (£) | | | |
| Ad cost per sale (£) | | | |

## What is done
- Business chosen and brand created (Well Listed). See `launch-kit/01-brief/`.
- Research folder, product, sales pages, lead magnet, full marketing machine, money plan, routines, operator, dashboard, growth plan: all built overnight as files. See the "What has been built" table in CLAUDE.md.
- Gumroad product is live. The site is built and ready; Netlify deploys it once the owner connects the repo (YOUR-TURN.md step 3).

## What is next
1. Owner works through `YOUR-TURN.md` (about 55 minutes, £0): connect Netlify to the repo, set up socials, post the first 3 posts.
2. Owner sends Claude the handles; the session records them here and rebuilds the dashboard.
3. From the next morning: "Run OPERATOR.md" daily.

## Decisions waiting for the owner
- Facts were checked online on 30 September 2026 (see `launch-kit/research/STILL-TO-VERIFY.md`). Only minor items remain unverified (some marketplace limits, KDP royalty in pounds, community rules, which must be read in each app). Do the free ICO self-assessment in the first two weeks: the business looks exempt.

## Log
- 2026-09-30: Launch day. Gumroad live at https://welllisted.gumroad.com/l/well-listed-kit; every buy button points there. Owner's name and address removed from the whole plan (no [LEGAL NAME] or [ADDRESS] placeholders). Email sign-up form removed: cheat sheet is a direct download and the site collects no personal data. Privacy and terms rewritten (Gumroad as merchant of record). Site rebuilt for https://well-listed.netlify.app; `netlify.toml` added (publishes `launch-kit/sales-site/netlify-site`, no build command, deploys only when that folder changes).
- 2026-09-30: Ready-to-post images made for all 60 posts and 30 pins (`launch-kit/marketing/ready-to-post/`, plus `first-14-days.zip`), proofread at source. Blog guides linked from the sales pages. Sign-up switched to Netlify Forms (free, no MailerLite needed). Launch dates now worked out automatically on deploy day. Facts verified online (MailerLite free plan is now 250 subscribers). Only the Gumroad link, legal name and address are left in the site. Everything merged into main. Owner's checklist: `YOUR-TURN.md`.
- 2026-09-30: Owner chose option (a): welcome emails stay off; the MailerLite form shows the cheat sheet link on screen. Added `launch-kit/LAUNCH-COPY-PASTE.md` with every launch-day value in its own copy box.
- 2026-09-29: Owner decisions: sole trader (limited company removed everywhere), £0 budget (company, registered office and paid ads removed from the launch plan; ads files kept and marked "later, only once sales cover it"). LAUNCH.md is now one 87-minute session with a handover to Claude for the Netlify deploy. Legal name and address only on terms and privacy. Logo and Gumroad cover generated in `launch-kit/sales-site/brand-assets/`.
- 2026-09-29: Owner verified Gumroad fees, VAT handling and the $100 payout minimum (MONEY.md now shows sales needed before the first payout). Brand will trade through a new limited company: LAUNCH.md is now two sessions (98 and 71 minutes). All tax rules removed from content; posts P28 and P31 replaced with non-tax posts. Remaining unverified facts listed in `launch-kit/research/STILL-TO-VERIFY.md`.
- 2026-09-29: Final pass. Product critiqued twice (now 90 prompts, 141-page PDF, two-digit prompt IDs), all files synced to the final product, every file checked (0 problems in check_content.py, no dashes), site, kit and dashboard rebuilt. Ready for the owner's LAUNCH.md.
- 2026-09-29: Quality check of blog, community, affiliate, tools and operating docs (see `launch-kit/qc/QC-blog-community-docs.md`). Launch steps now total 119 minutes; day 15 price switch steps added to ROUTINE.md and OPERATOR.md; ads confirmed as Meta first from day 15.
- 2026-09-29: Overnight build session. Everything in launch-kit/ created. Pull request opened for review, not merged.
