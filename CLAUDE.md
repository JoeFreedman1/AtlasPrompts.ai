# CLAUDE.md: read this first

This repo runs a faceless UK side business called **Well Listed**. Any new session can take over from here. The owner is **not a developer**: explain everything in plain English, UK English, prices in £, and **never use em dashes or en dashes** in anything you write.

If the owner types **"Run OPERATOR.md"**, follow `OPERATOR.md` step by step.

## The business in one paragraph
Well Listed sells **The Well Listed Kit**, a £19 digital download (launch price £12 for the first 14 days) of tested AI prompts, fill-in templates and checklists that help UK sellers write accurate listings, price items and answer buyers on eBay, Vinted, Depop, Etsy, Amazon and TikTok Shop, using free AI chat tools. It is sold through Gumroad, marketed with faceless short-form content (TikTok, Instagram, YouTube Shorts), Pinterest, a blog, and an email list fed by a free lead magnet ("The UK Listing Cheat Sheet").

**Who it is for:** UK side-business resellers (Vinted, eBay, Depop), small makers and brand owners (Etsy, Amazon, TikTok Shop), and declutterers turning pro. Time-poor, on mobile, price-sensitive, sceptical of hype and of "AI nonsense" listings.

**The pitch:** "Paste in your item's details and get a UK-ready listing, a price check and polite buyer replies, using the free AI tools you already have."

**The positioning:** "The marketplaces give you an AI button. We give you control of what it says." Our difference is the Listing Brief method: the AI only uses the seller's facts and flags gaps with [CHECK: ...] instead of inventing details.

## The faceless rule (absolute)
- The business is completely separate from the owner. **Never use the owner's name, face, voice, handwriting, home, or personal accounts** anywhere: content, pages, emails, commits to content files, metadata.
- All content works without a person on camera: text-on-screen slideshows, carousels, screen recordings (with account names blurred), licence-free stock footage without "us", simple graphics, AI text-to-speech voiceover (never a voice clone), Pinterest, blog posts and email.
- The brand speaks as "we". No founder story. Sign-off: "The Well Listed team".
- The only place a legal name may appear is the legally required notice on the sales page footer and privacy page (see `launch-kit/ASSUMPTIONS.md` point 12). The automatic checker flags possible owner identifiers without storing them.

## Brand guide (short version; full version in `launch-kit/01-brief/BRAND-GUIDE.md`)
- **Voice:** plain, practical, seller to seller, dry British warmth, honest. No hype. Banned words include hustle, grind, passive income, guru, secret, game-changer, unlock, skyrocket, insane.
- **Colours:** Ink `#1F2A44`, Cream `#FAF6EF`, Kraft `#C9A27E`, Sold Green `#1E7F55`, Label Yellow `#F2C84B`, Returns Red `#C4453B` (sparingly).
- **Fonts:** Archivo 700/800 (headings, slide text), Inter (body), JetBrains Mono (prompts). Fallback: Montserrat ExtraBold, Open Sans.
- **Visual signature:** the parcel label card (cream card, kraft border, dashed cut line); before (grey, red strike) and after (ink, green tick) comparisons; screen recordings with yellow highlight boxes; max 12 words per slide.

## All the rules (from the owner's original brief; never break them)
1. Do not create accounts, enter payment details, publish, post, send emails or spend money. Prepare everything; the owner does the human steps.
2. Never store passwords, API keys or card details anywhere in the repo or in chat.
3. Never invent reviews, testimonials, sales figures, statistics, follower counts or income claims. No misleading claims of any kind.
4. Stay within UK law and platform rules: no retail arbitrage dropshipping, no fake reviews, no misleading income claims, no scraping, no spam, no mass messaging, no bought followers or engagement pods. Affiliates and creators must disclose (#ad).
5. No food or FMCG products.
6. UK English, prices in £, no em dashes or en dashes (use commas, colons, full stops or brackets; write ranges as "5 to 10").
7. Everything customer-facing passes the quality check: `launch-kit/QUALITY-CHECKLIST.md` plus `python3 launch-kit/tools/check_content.py` with zero problems.
8. Work on a branch, commit after each meaningful step, open pull requests, and never merge unless the owner asks.
9. Where tasks are independent (posts, articles, emails, ads), subagents may work in parallel, and every subagent's output goes through the quality check.
10. Facts that change (fees, character limits, rules) must come from `launch-kit/research/platform-rules-uk.md` or `tools-and-fees.md`, and be phrased with "check the current rule" where not verified. Web research was limited overnight (search budget ran out, many sites blocked); many facts there are marked NOT VERIFIED.

## What has been built (all in `launch-kit/` unless stated)
| What | Where |
|---|---|
| Assumptions and decisions made overnight | `ASSUMPTIONS.md` |
| Business models scored, brief, brand guide, writing rules | `01-brief/` |
| Research: competitors, buyer language, keywords and hashtags, where buyers hang out, faceless accounts, UK platform rules, tools and fees | `research/` |
| The product: markdown source modules 00 to 12, templates, build script, critique log | `product/source/`, `product/templates/`, `product/build.py`, `product/CRITIQUE.md` |
| The product as sold (PDF, prompt library, prompt text file, zip for Gumroad) | `product/dist/` (rebuild with `python3 launch-kit/product/build.py`) |
| Sales pages A and B, privacy and terms, lead magnet, deploy guide | `sales-site/` (`sales-site/README.md` explains placeholders) |
| Ready-to-deploy Netlify folder (built from the above plus the blog) | `sales-site/netlify-site/` (rebuild with `python3 launch-kit/tools/build_site.py`) |
| 30-day content calendar | `marketing/a-content-calendar/calendar.csv` |
| 60 faceless short-form posts (P01 to P60) and their plan and format | `marketing/b-short-form-posts/`, `marketing/POST-PLAN.md`, `marketing/POST-FORMAT.md` |
| 30 Pinterest pins | `marketing/c-pinterest/pins.md` |
| 10 SEO blog articles (B01 to B10) | `marketing/d-blog/` |
| 7 welcome emails and 3 launch emails | `marketing/e-email/` |
| 20 ads, £5 a day test plan | `marketing/f-paid-ads/` |
| Affiliate and creator programme | `marketing/g-affiliates/` |
| Community plan with 10 helpful posts | `marketing/h-community/` |
| Marketplace listings (Gumroad, Payhip, Amazon KDP; why not Etsy or TikTok Shop) | `marketing/i-marketplace-listings/` |
| Free tools and the 10-minute post method | `marketing/j-tools/` |
| Money: prices, fees, profit per sale, break-even, scenarios, daily numbers | `MONEY.md` |
| Stop, keep, scale rules | `STOP-KEEP-SCALE.md` |
| Daily 30-minute routine, weekly review, first 14 days of posts | `ROUTINE.md` |
| Owner's launch checklist (under 2 hours) | `LAUNCH.md` |
| Growth plan (next products, prices, affiliates, ads) | `GROWTH.md` |
| Quality checklist | `QUALITY-CHECKLIST.md` |
| Mission control page for the owner's phone | `dashboard.html` (rebuild with `python3 launch-kit/tools/build_dashboard.py`) |
| Daily metrics template and guide | `metrics/template.csv`, `metrics/HOW-TO-FILL-IN.md` (real data goes in `metrics/YYYY-MM.csv`) |
| Daily plans written by the operator | `daily/YYYY-MM-DD.md` |
| Tools (no internet or installs needed): markdown converter, content checker, dashboard and site builders | `tools/` |
| Running log, key facts, current numbers | `STATE.md` (repo root) |
| Daily operator instructions | `OPERATOR.md` (repo root) |

The older **Atlas Prompts** website in `public/` and `css/` is unrelated to Well Listed. Leave it alone and never link the two.

## What is live
Nothing yet, as of the overnight build. `STATE.md` holds the truth: launch date, links, price, and what is live. Always read it before acting.

## How to do common jobs
- **Rebuild everything after edits:** `python3 launch-kit/product/build.py && python3 launch-kit/tools/build_site.py && python3 launch-kit/tools/build_dashboard.py && python3 launch-kit/tools/check_content.py`
- **Add new posts:** follow `marketing/POST-FORMAT.md` exactly (the dashboard parses it), continue IDs from the highest, add rows to `calendar.csv`.
- **Rename the brand** (if the trade mark check fails): replace "Well Listed" and handles across `launch-kit/`, update the brand guide, rebuild, run the checker.
- **Weekly review:** see `ROUTINE.md`.
