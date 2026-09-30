# STATE.md: where Well Listed is right now

Updated by every session. Newest log entries at the top of the log. The dashboard and the daily operator read the "Key facts" table, so keep its labels exactly as they are and put values in the second column.

## Key facts

| Fact | Value |
|---|---|
| Launch date | _not set_ |
| Current price | £12 launch price (planned), £19 from day 15 |
| Launch price end date | _not set (day 14 = launch date + 13 days; £12 ends 11:59pm that night)_ |
| Gumroad link | _not set_ |
| Sales page address | _not set_ |
| Sales page version live | _not set (A or B)_ |
| Email tool | None at launch. Sign-ups use Netlify Forms (free); welcome emails OFF (owner chose option a); the cheat sheet opens after sign-up |
| Legal identity | Sole trader trading as Well Listed. Legal name and address only on the terms and privacy pages (placeholders the owner fills in) |
| Ad budget cap | £0. Ads are for later, only once money kept from sales covers the £70 test budget (then Meta first) |
| Working branch | main (the launch kit was merged into main on 30 September 2026) |

## Current numbers (fill in from launch-kit/metrics/)

| Number | Yesterday | Last 7 days | Total to date |
|---|---|---|---|
| Sales | | | |
| Money kept after fees (£) | | | |
| Checkout page views | | | |
| Checkout conversion | | | |
| Email sign-ups | | | |
| Email subscribers (total) | | | |
| Bio link clicks | | | |
| Short-form video views (all platforms) | | | |
| Pinterest impressions | | | |
| Ad spend (£) | | | |
| Ad cost per sale (£) | | | |

## What is done
- Business chosen and brand created (Well Listed). See `launch-kit/01-brief/`.
- Research folder, product, sales pages, lead magnet, full marketing machine, money plan, routines, operator, dashboard, growth plan: all built overnight as files. See the "What has been built" table in CLAUDE.md.
- Nothing is live yet. No accounts exist.

## What is next
1. Owner works through `YOUR-TURN.md` (the short version of `launch-kit/LAUNCH.md`, 80 minutes, £0). Step 7 hands over to Claude to deploy the site to Netlify.
2. Owner tells a session the launch date, Gumroad link and sales page address; the session fills in the Key facts table above and rebuilds the dashboard.
3. From the next morning: "Run OPERATOR.md" daily.

## Decisions waiting for the owner
- Merge the pull request into main before launch, so every new session sees these files (say "merge the Well Listed pull request"). Until then, sessions must work from the working branch above.
- Check the facts still marked "NOT VERIFIED" (full list: `launch-kit/research/STILL-TO-VERIFY.md`) that matter most before launch: the MailerLite free plan limit, the ICO fee exemption, and the consumer law points in `launch-kit/research/platform-rules-uk.md`. (Gumroad fees, VAT handling and the $100 payout minimum are now verified by the owner. Tax rules were removed from all content.)

## Log
- 2026-09-30: Owner chose option (a): welcome emails stay off; the MailerLite form shows the cheat sheet link on screen. Added `launch-kit/LAUNCH-COPY-PASTE.md` with every launch-day value in its own copy box.
- 2026-09-29: Owner decisions: sole trader (limited company removed everywhere), £0 budget (company, registered office and paid ads removed from the launch plan; ads files kept and marked "later, only once sales cover it"). LAUNCH.md is now one 87-minute session with a handover to Claude for the Netlify deploy. Legal name and address only on terms and privacy. Logo and Gumroad cover generated in `launch-kit/sales-site/brand-assets/`.
- 2026-09-29: Owner verified Gumroad fees, VAT handling and the $100 payout minimum (MONEY.md now shows sales needed before the first payout). Brand will trade through a new limited company: LAUNCH.md is now two sessions (98 and 71 minutes). All tax rules removed from content; posts P28 and P31 replaced with non-tax posts. Remaining unverified facts listed in `launch-kit/research/STILL-TO-VERIFY.md`.
- 2026-09-29: Final pass. Product critiqued twice (now 90 prompts, 141-page PDF, two-digit prompt IDs), all files synced to the final product, every file checked (0 problems in check_content.py, no dashes), site, kit and dashboard rebuilt. Ready for the owner's LAUNCH.md.
- 2026-09-29: Quality check of blog, community, affiliate, tools and operating docs (see `launch-kit/qc/QC-blog-community-docs.md`). Launch steps now total 119 minutes; day 15 price switch steps added to ROUTINE.md and OPERATOR.md; ads confirmed as Meta first from day 15.
- 2026-09-29: Overnight build session. Everything in launch-kit/ created. Pull request opened for review, not merged.
