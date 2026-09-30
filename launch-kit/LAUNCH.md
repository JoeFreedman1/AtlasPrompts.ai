# LAUNCH.md: launch day in one session (67 minutes)

Well Listed trades under the brand name Well Listed, and **your name and address appear nowhere in the site or the repo**. Every sale is made through Gumroad as merchant of record, and the site collects no personal data: there is no sign-up form, and the free cheat sheet is a direct download. **Budget: £0.** Free plans only: Gumroad, Netlify, free social accounts and free content tools. No ads.

**Every value you type today** is in `LAUNCH-COPY-PASTE.md`, each in its own copy box.

Launch day is **30 September 2026** (day 1). The £12 launch price ends at 11:59pm on **Tuesday 13 October 2026** (day 14); from 14 October it is £19.

**Where the files are:** everything lives in the GitHub repo. File paths below start inside the `launch-kit` folder (so `product/dist/Well-Listed-Kit.zip` means `launch-kit/product/dist/Well-Listed-Kit.zip`). Everything is on the `main` branch.
- **To download one file** (like the zip in step 3): open the file on GitHub and press the download button ("Download raw file").
- **To download a whole folder:** on the repo's front page, press the green **Code** button, then **Download ZIP**. Unzip it on your computer and open the folder you need. Always download a fresh copy after Claude has changed something.
- **The dashboard:** download `launch-kit/dashboard.html` the same way and open it in your phone's browser. Ticks are saved in that browser only and may reset when you open a newer copy, so treat this file as the master list. Download a fresh copy each time Claude rebuilds it.

**Before you start:** use a browser profile or phone that is **not** logged in to your personal Google, Instagram or TikTok accounts, so nothing links the brand to you by accident. On a computer, create a new browser profile called "Well Listed" (Chrome: profile icon, Add). On a phone, log out of personal accounts in each app first, or use the app's "add account" option carefully and double-check which account you are posting from every time.

**Security:** use a password manager (e.g. the free one built into your browser or phone) and a unique password for every account below. Turn on two-step verification wherever offered. **Never write passwords in this repo or in chats with Claude.**

---

### Part 1: Name, email and shop (22 minutes)

1. **Check the name and handles are free (5 min).** Search "Well Listed" on the UK IPO trade mark search (search "UK IPO trade mark search") in classes 9, 35 and 41, and check the handle `welllisted.uk` / `welllisteduk` / `well.listed.uk` on TikTok, Instagram, YouTube and Pinterest.
2. **Create the brand email (5 min).** `hello.welllisted@gmail.com` (the site already shows this address). Use the brand name, not yours.
3. **Gumroad product (12 min).** Done: the kit is live at `https://welllisted.gumroad.com/l/well-listed-kit` at £12. Check the description, cover and refund policy match `marketing/i-marketplace-listings/listings.md`, and set a reminder to change the price to £19 after 11:59pm on 13 October 2026.

### Part 2: Website (6 minutes)

4. **Connect the repo in Netlify (6 min).** Sign up free at Netlify with the brand email. Add new site, Import an existing project, GitHub, pick this repository and the `main` branch. Netlify reads `netlify.toml` (no build command; publishes `launch-kit/sales-site/netlify-site`). Set the site name to `well-listed` (Site configuration, Change site name). Then check on your phone: `https://well-listed.netlify.app` opens, every buy button goes to Gumroad at £12, and the cheat sheet downloads. From now on Netlify redeploys by itself whenever the site folder changes on `main`.

### Part 3: Social accounts (22 minutes)

For each: sign up with the brand email, use `sales-site/brand-assets/logo-1080.png` as the profile picture (already made for you), and paste the bio below. Switch to a free **business or creator account** so you get analytics.

**Bio (use on all):** `Faster, honest listings for UK sellers. AI prompts for eBay, Vinted, Depop, Etsy and more. Free cheat sheet below.` Add the website address `https://well-listed.netlify.app` as the link.

5. **TikTok (6 min).** Sign up, set name "Well Listed", handle as close to `welllisted.uk` as possible. Switch to a Business account (category: Education or Business services). Add the bio. The website link field may only appear later; until then, put "Link in Instagram bio" in the bio.
6. **Instagram (5 min).** Sign up with the brand email (not "continue with Facebook" from your personal Facebook). Switch to a Professional account, Business. Add the bio and the website link.
7. **YouTube (5 min).** Using the brand Gmail, create a YouTube **channel** named "Well Listed" (choose "use a custom name", which creates a brand account separate from your personal name). Add the logo, bio and link.
8. **Pinterest (6 min).** Create a free **business** account with the brand email. Create 4 boards: "eBay Selling Tips UK", "Vinted Selling Tips", "Listing Templates and Prompts", "Reseller Organisation". Add the website link.

### Part 4: First 3 posts (17 minutes)

9. **Post 1: Day 1 Slot A video (7 min).** Open the dashboard, find Day 1, and follow the 10-minute method in `marketing/j-tools/free-tools-and-10-minute-workflow.md` using free CapCut or Canva. Keep this first one simple (text over a screen recording is fine). Post to TikTok, Instagram Reels and YouTube Shorts.
10. **Post 2: Day 1 Slot B carousel (6 min).** Make it in free Canva from the slide text in the dashboard and schedule it for 19:30 on Instagram (and TikTok photo mode).
11. **Post 3: the first pin, PIN01 (4 min).** Make the pin in free Canva from its design brief in the dashboard and publish or schedule it in Pinterest.

From tomorrow morning, follow `ROUTINE.md`: add yesterday's numbers, then type "Run OPERATOR.md".

### In the first two weeks (free, not on launch day)
- Before day 3: do the one-time 30-minute template setup in section 2 of `marketing/j-tools/free-tools-and-10-minute-workflow.md`, so every post after that takes 10 minutes.
- Do the free ICO data protection fee self-assessment (5 min, search "ICO fee self assessment"), to check whether a fee applies.
- There is no email list at launch. If you ever want one, it needs a sign-up form, a rewritten privacy page and a postal address in every email footer (MailerLite's rule): ask Claude first.
- For tax questions, read gov.uk (search "selling online tax") or ask an accountant. We do not state tax rules here.

**Total: 67 minutes in one session.** If a step runs over, move Pinterest (step 8) and the pin (step 11) to tomorrow.

**No ads.** Paid ads are for later, only once money kept from sales covers the test budget (see `marketing/f-paid-ads/test-plan.md`).
