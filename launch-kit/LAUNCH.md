# LAUNCH.md: launch day in one session (80 minutes)

Well Listed trades as a **sole trader** under the brand name Well Listed. Your legal name and address appear **only** on the terms and privacy pages, which you fill in yourself (step 4). They never appear in the brand, bios, posts, emails, product or sales page. **Budget: £0.** Everything below uses free plans only: Gumroad, Netlify (including its free forms), free social accounts and free content tools. No ads.

**Every value you type today** (email options, Gumroad text, handles, bios, captions and download links) is in `LAUNCH-COPY-PASTE.md`, each in its own copy box. Keep it open alongside this checklist.

Do the steps in order. Each step says how long it should take. Everything else (writing, designing, planning) is already done. Tick them off in the dashboard as you go. Launch day is day 1: the £12 launch price runs for days 1 to 14 and ends at 11:59pm on day 14.

**Where the files are:** everything lives in the GitHub repo. File paths below start inside the `launch-kit` folder (so `product/dist/Well-Listed-Kit.zip` means `launch-kit/product/dist/Well-Listed-Kit.zip`). Until the pull request is merged, the files are on the **working branch** named in `STATE.md` (at the time of writing `claude/keen-thompson-uxkjgk`), not on main. The simplest fix: before you start, tell Claude "merge the Well Listed pull request into main". Otherwise, on GitHub, switch the branch menu (top left of the file list, usually showing "main") to the working branch before downloading anything.
- **To download one file** (like the zip in step 3): open the file on GitHub and press the download button ("Download raw file").
- **To download a whole folder:** on the repo's front page, press the green **Code** button, then **Download ZIP**. Unzip it on your computer and open the folder you need. Always download a fresh copy after Claude has changed something.
- **The dashboard:** download `launch-kit/dashboard.html` the same way and open it in your phone's browser. Ticks are saved in that browser only and may reset when you open a newer copy, so treat this file as the master list. Download a fresh copy each time Claude rebuilds it.

**Before you start:** use a browser profile or phone that is **not** logged in to your personal Google, Instagram or TikTok accounts, so nothing links the brand to you by accident. On a computer, create a new browser profile called "Well Listed" (Chrome: profile icon, Add). On a phone, log out of personal accounts in each app first, or use the app's "add account" option carefully and double-check which account you are posting from every time.

**Security:** use a password manager (e.g. the free one built into your browser or phone) and a unique password for every account below. Turn on two-step verification wherever offered. **Never write passwords in this repo or in chats with Claude.**

---

### Part 1: Name, email and shop (29 minutes)

1. **Check the name and handles are free (5 min).** Search "Well Listed" on the UK IPO trade mark search (search "UK IPO trade mark search") in classes 9, 35 and 41, and check the handle `welllisted.uk` / `welllisteduk` / `well.listed.uk` on TikTok, Instagram, YouTube and Pinterest. If something very similar exists in the same field, pick an alternative from `01-brief/BRIEF.md` and tell Claude to rename everything (it can do it in one go).
2. **Create the brand email (5 min).** Make a new free Gmail or Outlook address using the brand name, not yours (birthday and phone number are only for account recovery and are not shown publicly). This email is used for every account below.
3. **Gumroad product with the zip uploaded (12 min).** Sign up free at Gumroad with the brand email. Pick the username `welllisted` (or close to it), never your own name: it appears in the product link. In Settings, set the profile name to "Well Listed" and the currency to GBP. Gumroad asks for your own details and bank account for payouts: these stay private inside Gumroad and are not shown to buyers. Create a product:
   - Name: **The Well Listed Kit**. Price: **£12**.
   - Upload `product/dist/Well-Listed-Kit.zip` (download it from GitHub: open the file, press "Download raw file").
   - Cover image: upload `sales-site/brand-assets/gumroad-cover-1280x720.png` (already made for you).
   - Description, summary and tags: copy from `marketing/i-marketplace-listings/listings.md` (Gumroad section). It includes the line "Instant download. By buying you agree to immediate access.", which the terms page relies on.
   - Refund policy: 30 days, no questions (matches the sales page).
   - Publish the product and copy its link (it looks like `https://welllisted.gumroad.com/l/...`).
4. **Fill in the terms page placeholders yourself (4 min).** On GitHub (make sure the repository is **private**: Settings, General, the "Danger zone" shows the visibility), open `launch-kit/sales-site/placeholders.json` and press the pencil icon. Type your full legal name between the quotes after `LEGAL NAME`, and your postal address after `ADDRESS`. Commit the change. These two values are used only on the terms and privacy pages; the build warns if they ever appear anywhere else. (The brand email, website address and launch dates are already filled in or worked out automatically.)
5. **Put the Gumroad link into the sales page (3 min).** In the same file, paste the Gumroad link from step 3 between the quotes after `GUMROAD_PRODUCT_LINK` and commit.

### Part 2: Website (12 minutes)

6. **Check the free sign-up form needs nothing from you (2 min).** The cheat sheet form uses Netlify's own free form handling, so there is no MailerLite set-up today: sign-ups appear in your Netlify account under "Forms", and the cheat sheet opens straight after signing up. Welcome emails stay off (your decision). Skip MailerLite until you decide to send emails.
7. **HANDOVER TO CLAUDE: deploy the site to Netlify (10 min).** Sign up free at Netlify with the brand email. Then open Claude (claude.ai), make sure the Netlify connector is connected (Settings, Connectors, Netlify), and in a session on this repo say the message in `LAUNCH-COPY-PASTE.md` (step 7). Claude sets today as the launch date, rebuilds the site from `placeholders.json`, deploys it to your Netlify account, records everything in STATE.md and gives you the live address. Check it on your phone: the page loads, the buy button opens Gumroad at £12, and signing up with a spare email opens the cheat sheet. In Netlify, open Forms and switch on form detection if it asks. Never paste passwords.

### Part 3: Social accounts (22 minutes)

For each: sign up with the brand email, use `sales-site/brand-assets/logo-1080.png` as the profile picture (already made for you), and paste the bio below. Switch to a free **business or creator account** so you get analytics.

**Bio (use on all):** `Faster, honest listings for UK sellers. AI prompts for eBay, Vinted, Depop, Etsy and more. Free cheat sheet below.` Add the live website address from step 7 as the link.

8. **TikTok (6 min).** Sign up, set name "Well Listed", handle as close to `welllisted.uk` as possible. Switch to a Business account (category: Education or Business services). Add the bio. The website link field may only appear later; until then, put "Link in Instagram bio" in the bio.
9. **Instagram (5 min).** Sign up with the brand email (not "continue with Facebook" from your personal Facebook). Switch to a Professional account, Business. Add the bio and the website link.
10. **YouTube (5 min).** Using the brand Gmail, create a YouTube **channel** named "Well Listed" (choose "use a custom name", which creates a brand account separate from your personal name). Add the logo, bio and link.
11. **Pinterest (6 min).** Create a free **business** account with the brand email. Create 4 boards: "eBay Selling Tips UK", "Vinted Selling Tips", "Listing Templates and Prompts", "Reseller Organisation". Add the website link.

### Part 4: First 3 posts (17 minutes)

12. **Post 1: Day 1 Slot A video (7 min).** Open the dashboard, find Day 1, and follow the 10-minute method in `marketing/j-tools/free-tools-and-10-minute-workflow.md` using free CapCut or Canva. Keep this first one simple (text over a screen recording is fine). Post to TikTok, Instagram Reels and YouTube Shorts.
13. **Post 2: Day 1 Slot B carousel (6 min).** Make it in free Canva from the slide text in the dashboard and schedule it for 19:30 on Instagram (and TikTok photo mode).
14. **Post 3: the first pin, PIN01 (4 min).** Make the pin in free Canva from its design brief in the dashboard and publish or schedule it in Pinterest.

From tomorrow morning, follow `ROUTINE.md`: add yesterday's numbers, then type "Run OPERATOR.md".

### In the first two weeks (free, not on launch day)
- Before day 3: do the one-time 30-minute template setup in section 2 of `marketing/j-tools/free-tools-and-10-minute-workflow.md`, so every post after that takes 10 minutes.
- Do the free ICO data protection fee self-assessment (5 min, search "ICO fee self assessment"), to check whether a fee applies.
- Welcome emails stay off (option a). If you ever change your mind, set up MailerLite free and load the 7 emails in `marketing/e-email/welcome-sequence.md` (Claude can move the form over).
- For tax questions, read gov.uk (search "selling online tax") or ask an accountant. We do not state tax rules here.

**Total: 80 minutes in one session.** If a step runs over, move Pinterest (step 11) and the pin (step 14) to tomorrow.

**No ads.** Paid ads are for later, only once money kept from sales covers the test budget (see `marketing/f-paid-ads/test-plan.md`).
