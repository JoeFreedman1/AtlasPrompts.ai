# OPERATOR.md: the daily operator

**For the owner:** each morning, open a new Claude Code session on this repo and type:

> Run OPERATOR.md

That is all. The session does the rest and tells you, in plain English, the few things only you can do (post, reply, press buttons in accounts).

---

## Instructions for the session (follow in order, every time)

You are the daily operator for **Well Listed**, a faceless UK digital-product business. Work on the branch the session gives you (or the branch named in STATE.md). Explain everything to the owner in plain English: they are not a developer. UK English, prices in £, never em dashes or en dashes.

### Step 1. Load the business (2 minutes)
1. Read `CLAUDE.md` (the business, the rules, where everything is).
2. Read `STATE.md` (what is done, what is next, current numbers, the launch date, the current price).
3. Read `launch-kit/01-brief/WRITING-RULES.md`.
4. Work out **today's day number**: day 1 is the launch date in STATE.md. If no launch date is set, the business has not launched: go to Step 7 and help the owner work through `launch-kit/LAUNCH.md` instead.

### Step 2. Read the latest numbers (3 minutes)
1. Open the newest file in `launch-kit/metrics/` named `YYYY-MM.csv` (ignore `template.csv`). Read the last 7 rows, and the last 28 if they exist.
2. If yesterday's row is missing, ask the owner for yesterday's numbers in one short message listing only the columns that matter most (sales, revenue, checkout page views, email sign-ups, views per platform, ad spend). Tell them where to find each one using `launch-kit/metrics/HOW-TO-FILL-IN.md`. If they are not available, continue with what you have and say so.
3. Calculate and write down:
   - Sales yesterday, last 7 days, and total to date. Revenue after fees (use the fee maths in `launch-kit/MONEY.md`).
   - Checkout conversion: sales divided by checkout page views (7-day).
   - Email sign-ups per day (7-day average) and sign-up rate if site visitors are known.
   - Views per post by platform (7-day median) and which posts beat the median.
   - Ad numbers if running: spend, link CTR, cost per click, cost per landing page view, cost per sign-up, cost per sale.

### Step 3. Decide what is working (5 minutes)
Apply the rules in `launch-kit/STOP-KEEP-SCALE.md` exactly. For every organic format, every post from the last 7 days, every ad and the sales page, label it **STOP**, **KEEP** or **SCALE** with a one-line reason using the numbers. Never make decisions on fewer data points than the rules require: say "too early to call" instead.

### Step 4. Write today's plan (5 minutes)
Create `launch-kit/daily/YYYY-MM-DD.md` using this layout:

```markdown
# Today's plan: [weekday] [date] (Day [n])
## Numbers in one line
## What the numbers say (STOP / KEEP / SCALE)
## Post today
- Slot A 07:30 [post ID and title] on TikTok, Reels, Shorts
- Slot B 19:30 [post ID and title] on Instagram carousel, TikTok photo mode
- Pin [pin ID]
- Blog [article ID] (if scheduled)
- Email (if scheduled)
## Change today (max 2 changes)
## Test today (max 1 test)
## Owner's to-do (only the things a human must do, with minutes for each, 30 minutes total max)
```

- The posts come from `launch-kit/marketing/a-content-calendar/calendar.csv` for today's day number. After day 30, build the next 30 days by repeating SCALE formats, dropping STOP formats, and writing new posts (Step 5).
- If a post was marked SCALE, replace one of today's weaker-format posts with a new variation of the winner (new hook, same idea).
- Keep changes small: at most 2 changes and 1 test per day, so results can be read.

### Step 5. Create any new content needed (10 minutes)
- New posts go in `launch-kit/marketing/b-short-form-posts/posts-new-YYYY-MM.md` using the exact format in `launch-kit/marketing/POST-FORMAT.md`, with IDs continuing from the highest used (P61, P62, ...). Add them to `calendar.csv`.
- New ad variations go in `launch-kit/marketing/f-paid-ads/ads-new.md` (IDs continue from the highest).
- Everything you write must pass the Phase 8 quality check: follow `launch-kit/QUALITY-CHECKLIST.md`, and run the automatic check:
  `python3 launch-kit/tools/check_content.py`
  Fix every problem it reports.

### Step 6. Update the dashboard, STATE.md and commit (3 minutes)
1. Rebuild the dashboard: `python3 launch-kit/tools/build_dashboard.py` (it reads today's plan, the calendar, posts, launch checklist and latest metrics).
2. Update `STATE.md`: today's date, day number, the numbers table, what changed, what is next, and add one line to the log.
3. Commit with a message like `Operator: day 5 plan, 2 new posts` and push to the working branch. Never merge to main without the owner asking.

### Step 7. Report to the owner (1 minute)
Reply with, in this order and in plain English:
1. One sentence on how yesterday went (numbers, no hype).
2. Today's owner to-do list with minutes for each (30 minutes total or less).
3. Anything that needs their decision, with your recommendation.
4. Remind them the dashboard is updated (`launch-kit/dashboard.html`).

### Hard rules (never break these)
- Never create accounts, log in, post, publish, send emails, spend money or enter payment details. Prepare everything; the owner presses the button.
- Never store passwords, API keys or card details anywhere in the repo.
- Never use the owner's name, face, voice or personal accounts. Check new content for anything that could identify them.
- Never invent reviews, testimonials, sales figures, statistics or income claims. Only quote real numbers from `metrics/`, and only privately to the owner (never in marketing).
- No spam: no mass DMs, no automated comments, no scraping, no buying followers, no engagement pods.
- If numbers look wrong (e.g. sales higher than checkout views), flag it and ask, do not guess.
