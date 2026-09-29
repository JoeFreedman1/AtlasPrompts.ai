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
| Email tool | MailerLite (planned) |
| Legal identity | _not decided (sole trader or limited company, see launch-kit/ASSUMPTIONS.md point 12)_ |
| Ad budget cap | £0 until day 15, then £5 a day, £70 per fortnight, Meta first |
| Working branch | claude/keen-thompson-uxkjgk |

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
1. Owner works through `launch-kit/LAUNCH.md` (under 2 hours).
2. Owner tells a session the launch date, Gumroad link and sales page address; the session fills in the Key facts table above and rebuilds the dashboard.
3. From the next morning: "Run OPERATOR.md" daily.

## Decisions waiting for the owner
- Merge the pull request into main before launch, so every new session sees these files (say "merge the Well Listed pull request"). Until then, sessions must work from the working branch above.
- Legal identity: sole trader or limited company (see ASSUMPTIONS.md point 12). Default if not decided: sole trader for launch.
- Check the facts marked "NOT VERIFIED" in `launch-kit/research/platform-rules-uk.md` and `launch-kit/research/tools-and-fees.md` that matter most before launch: Gumroad fees and VAT handling (the money maths in `launch-kit/MONEY.md` assumes 10% + $0.50 plus card processing, VAT added on top), the MailerLite free plan limit, and the HMRC rules used in posts P28 and P31.

## Log
- 2026-09-29: Final pass. Product critiqued twice (now 90 prompts, 141-page PDF, two-digit prompt IDs), all files synced to the final product, every file checked (0 problems in check_content.py, no dashes), site, kit and dashboard rebuilt. Ready for the owner's LAUNCH.md.
- 2026-09-29: Quality check of blog, community, affiliate, tools and operating docs (see `launch-kit/qc/QC-blog-community-docs.md`). Launch steps now total 119 minutes; day 15 price switch steps added to ROUTINE.md and OPERATOR.md; ads confirmed as Meta first from day 15.
- 2026-09-29: Overnight build session. Everything in launch-kit/ created. Pull request opened for review, not merged.
