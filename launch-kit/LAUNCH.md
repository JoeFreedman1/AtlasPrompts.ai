# LAUNCH.md: what you do on launch day (about 1 hour 59 minutes, under 2 hours)

Do these in order. Each step says how long it should take. Everything else (writing, designing, planning) is already done. Tick them off in the dashboard as you go. Launch day is day 1: the £12 launch price runs for days 1 to 14 and ends at 11:59pm on day 14.

**Where the files are:** everything lives in the GitHub repo. File paths below start inside the `launch-kit` folder (so `product/dist/Well-Listed-Kit.zip` means `launch-kit/product/dist/Well-Listed-Kit.zip`). Until the pull request is merged, the files are on the **working branch** named in `STATE.md` (at the time of writing `claude/keen-thompson-uxkjgk`), not on main. The simplest fix: before you start, tell Claude "merge the Well Listed pull request into main". Otherwise, on GitHub, switch the branch menu (top left of the file list, usually showing "main") to the working branch before downloading anything.
- **To download one file** (like the zip in step 9): open the file on GitHub and press the download button ("Download raw file").
- **To download a folder** (like the website in step 12): on the repo's front page, press the green **Code** button, then **Download ZIP**. Unzip it on your computer and open the folder you need. Always download a fresh copy after Claude has changed something.
- **The dashboard:** download `launch-kit/dashboard.html` the same way and open it in your phone's browser. Your ticks are saved in that browser on that device. Download a fresh copy each time Claude rebuilds it.

**Before you start:** use a browser profile or phone that is **not** logged in to your personal Google, Instagram or TikTok accounts, so nothing links the brand to you by accident. On a computer, create a new browser profile called "Well Listed" (Chrome: profile icon, Add). On a phone, log out of personal accounts in each app first, or use the app's "add account" option carefully and double-check which account you are posting from every time.

**Security:** use a password manager (e.g. the free one built into your browser or phone) and a unique password for every account below. Turn on two-step verification wherever offered. **Never write passwords in this repo or in chats with Claude.**

---

### Part 1: Brand identity (22 minutes)

1. **Check the name is free (5 min).** Search "Well Listed" on the UK IPO trade mark search (search "UK IPO trade mark search" on Google) in classes 9, 35 and 41, and search the handle `welllisted.uk` / `welllisteduk` / `well.listed.uk` on TikTok, Instagram, YouTube and Pinterest. If something very similar exists in the same field, pick an alternative from `01-brief/BRIEF.md` and tell Claude to rename everything (it can do it in one go).
2. **Create the brand email (5 min).** Make a new free Gmail or Outlook address such as `hello.welllisted@gmail.com` (use the brand name, not yours; birthday and phone number are only for account recovery and are not shown publicly). This email is used for every account below.
3. **Decide the legal identity (5 min).** Read point 12 of `ASSUMPTIONS.md`. Either (a) sole trader: your legal name goes only in the legal notice at the bottom of the sales page and in the privacy notice, or (b) limited company: the company name goes there instead, but it has to exist first, so launch once it is set up (adds cost, see MONEY.md). Tell Claude your choice and it will write it in STATE.md. **If unsure, choose (a) for launch and switch later.**
4. **Make the logo files (7 min).** In Canva (free, sign up with the brand email): create a 1080 x 1080 design, cream background `#FAF6EF`, the letters "WL" in Archivo or Montserrat ExtraBold, colour `#1F2A44`, and a green tick `#1E7F55`. Download as PNG. This is your profile picture everywhere. Details: `01-brief/BRAND-GUIDE.md`.

### Part 2: Social accounts (26 minutes)

For each: sign up with the brand email, use the brand logo, and paste the bio below. Switch to a **business or creator account** (free) so you get analytics.

**Bio (use on all):** `Faster, honest listings for UK sellers. AI prompts for eBay, Vinted, Depop, Etsy and more. Free cheat sheet below.`

5. **TikTok (7 min).** Sign up, set name "Well Listed", handle as close to `welllisted.uk` as possible. Settings: switch to a Business account (category: Education or Business services). Add the bio. The website link field may only appear later; add it when it does. Until then, put "Link in Instagram bio" in the bio.
6. **Instagram (6 min).** Sign up with the brand email (not "continue with Facebook" from your personal Facebook). Switch to a Professional account, Business. Add the bio. The sales page link comes in step 12; you add it in step 13.
7. **YouTube (6 min).** Using the brand Gmail, create a YouTube **channel** named "Well Listed" (choose "use a custom name", which creates a brand account separate from your personal name). Add the logo and bio.
8. **Pinterest (7 min).** Create a **business** account with the brand email. Create 4 boards: "eBay Selling Tips UK", "Vinted Selling Tips", "Listing Templates and Prompts", "Reseller Organisation". Claim your website once it is live (step 12, optional today).

### Part 3: Shop, website and email (51 minutes)

9. **Gumroad product (13 min).** Sign up at Gumroad with the brand email. Pick the username `welllisted` (or close to it), never your own name: it appears in the product link. In Settings, set the profile name to "Well Listed". Create a product:
   - Name: **The Well Listed Kit**. Price: **£12** (set currency to GBP in settings first).
   - Upload the file `product/dist/Well-Listed-Kit.zip` (download it from GitHub: open the file, tap "Download raw").
   - Description, summary and tags: copy from `marketing/i-marketplace-listings/listings.md` (Gumroad section).
   - Cover image: use the Canva cover described in the same file (5 minutes to make).
   - Turn on "Allow customers to pay what they want"? **No.** Keep it simple.
   - Refund policy: set to match the sales page guarantee (30 days, no questions).
   - Make sure the description includes "Instant download. By buying you agree to immediate access." (it is in the copy in `listings.md`; the terms page relies on it).
   - Connect your bank account for payouts (Gumroad asks for this; this is the only place payment details go).
   - Copy the product link (it looks like `https://welllisted.gumroad.com/l/...`).
10. **Email tool (15 min).** Sign up to MailerLite free with the brand email. It will ask for a physical address for the footer of emails (the law requires one): use your business address, or a PO box or registered office service if you prefer not to use home (see ASSUMPTIONS.md point 12).
    - Create a group called "Cheat sheet".
    - Create an embedded form with just an email field (and optional first name). Copy its embed code.
    - Create an automation: trigger "joins group Cheat sheet". Add the 7 welcome emails from `marketing/e-email/welcome-sequence.md` with the delays written there. Leave the cheat sheet link in email 1 as `[CHEAT_SHEET_LINK]` for now: you fill it in at step 13.
    - Turn on double opt-in (recommended, keeps the list clean).
11. **Put the links into the sales page (5 min).** Start a Claude session and paste: the Gumroad link, the brand email, your legal name and address (or company details), the launch end date and the MailerLite form embed code. The launch end date is day 14, which is launch day plus 13 days: launch on Monday 5 October 2026 and the end date is Sunday 18 October 2026. Say "fill in the sales site placeholders, rebuild and push". Claude puts the values in `sales-site/placeholders.json`, runs `python3 launch-kit/tools/build_site.py` (which rebuilds the `sales-site/netlify-site/` folder) and pushes the change to GitHub. Never paste passwords. (Details: `sales-site/README.md`.)
12. **Go live on Netlify (12 min).** On a computer (drag and drop does not work on a phone), download a fresh ZIP from GitHub (see "Where the files are" above), unzip it and find `launch-kit/sales-site/netlify-site`. Sign up to Netlify with the brand email. Choose "Add new site", then "Deploy manually", and drag the whole `netlify-site` folder onto the page. Netlify gives you a web address like `random-name-123.netlify.app`: change it to something like `well-listed` in Site configuration, "Change site name". Tell Claude the address and say "put this in site_url, rebuild and push" (this fills in the cheat sheet link and share previews). Download a fresh ZIP again and, in Netlify, open Deploys and drag the new `netlify-site` folder onto the drag and drop box.
13. **Add the link everywhere and test (6 min).** In MailerLite, open welcome email 1 and put in the cheat sheet link: your Netlify address followed by `/free/uk-listing-cheat-sheet.pdf`. Put the Netlify address in the Instagram, TikTok (when available), YouTube and Pinterest bios. Then test on your phone: open the site, press the buy button (it should open Gumroad at £12), and sign up with a spare email address to check welcome email 1 arrives with a working cheat sheet link.

### Part 4: First posts (20 minutes)

14. **Make and post Day 1 Slot A (10 min).** Open the dashboard, find Day 1, and follow the 10-minute method in `marketing/j-tools/free-tools-and-10-minute-workflow.md`. The reusable templates are not set up yet, so keep this first one simple (text over a screen recording is fine). Post to TikTok, Instagram Reels and YouTube Shorts.
15. **Make and schedule Day 1 Slot B and the first pin (7 min).** Slot B for 19:30, PIN01 for 12:00 (or now, if it is already past 12:00).
16. **Tell Claude you have launched (3 min).** Start a session and say: "We launched today. Launch date is [today's date]. Gumroad link is [link]. Netlify address is [address]." It will fill in the Key facts in STATE.md (launch date, launch price end date, links) and rebuild the dashboard, so the daily operator knows today is day 1. From tomorrow morning, follow `ROUTINE.md`: add yesterday's numbers, then type "Run OPERATOR.md".

### This week (not today)
- Before day 3: do the one-time 30-minute template setup in section 2 of `marketing/j-tools/free-tools-and-10-minute-workflow.md`, so every post after that takes 10 minutes.
- Check the facts STATE.md lists under "Decisions waiting for the owner" (Gumroad fees and VAT, the MailerLite free limit).
- Do the ICO data protection fee self-assessment (5 min, search "ICO fee self assessment").
- Buy a domain if you want one (about £10) and connect it in Netlify.
- If you chose a limited company, set it up and update the legal notice.
- Register for Self Assessment with HMRC if you expect trading income over £1,000 this tax year.

**Total: 119 minutes (1 hour 59 minutes).** If a step runs over, skip step 8 (Pinterest) and the first pin, and do them tomorrow.

**No ads yet.** Paid ads are optional and start on day 15 at the earliest, on Meta first (see `marketing/f-paid-ads/test-plan.md`).
