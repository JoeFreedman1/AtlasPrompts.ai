# LAUNCH.md: set up the company, then launch

Well Listed trades through its own **private limited company**, so your name and home address stay off the website, receipts and emails (see ASSUMPTIONS.md point 12). A new company has to be approved by Companies House before it can open a bank account and appear in the legal notice, so the launch happens in **two sessions**, each under 2 hours:

- **Session 1, tomorrow (98 minutes):** apply for the company, then build all the accounts that do not need it yet (email, logo, social accounts, email tool).
- **Session 2, launch day (71 minutes):** once Companies House has sent the company number and a business bank account is open: shop, website, first posts. Companies House often approves online applications within about a day, but allow a few working days (check the current timings on gov.uk).

Do the steps in order. Each step says how long it should take. Everything else (writing, designing, planning) is already done. Tick them off in the dashboard as you go. Launch day is day 1: the £12 launch price runs for days 1 to 14 and ends at 11:59pm on day 14.

**Where the files are:** everything lives in the GitHub repo. File paths below start inside the `launch-kit` folder (so `product/dist/Well-Listed-Kit.zip` means `launch-kit/product/dist/Well-Listed-Kit.zip`). Until the pull request is merged, the files are on the **working branch** named in `STATE.md` (at the time of writing `claude/keen-thompson-uxkjgk`), not on main. The simplest fix: before you start, tell Claude "merge the Well Listed pull request into main". Otherwise, on GitHub, switch the branch menu (top left of the file list, usually showing "main") to the working branch before downloading anything.
- **To download one file** (like the zip in step 13): open the file on GitHub and press the download button ("Download raw file").
- **To download a folder** (like the website in step 15): on the repo's front page, press the green **Code** button, then **Download ZIP**. Unzip it on your computer and open the folder you need. Always download a fresh copy after Claude has changed something.
- **The dashboard:** download `launch-kit/dashboard.html` the same way and open it in your phone's browser. Ticks are saved in that browser only and may reset when you open a newer copy, so treat this file as the master list. Download a fresh copy each time Claude rebuilds it.

**Before you start:** use a browser profile or phone that is **not** logged in to your personal Google, Instagram or TikTok accounts, so nothing links the brand to you by accident. On a computer, create a new browser profile called "Well Listed" (Chrome: profile icon, Add). On a phone, log out of personal accounts in each app first, or use the app's "add account" option carefully and double-check which account you are posting from every time.

**Security:** use a password manager (e.g. the free one built into your browser or phone) and a unique password for every account below. Turn on two-step verification wherever offered. **Never write passwords in this repo or in chats with Claude.**

---

## Session 1: tomorrow (98 minutes)

### Part 1: Name, email and company (50 minutes)

1. **Check the name is free (5 min).** Three checks: (a) the Companies House company name availability checker (search "Companies House company name availability" on Google) for "Well Listed Ltd" or "Well Listed UK Ltd"; (b) the UK IPO trade mark search (search "UK IPO trade mark search") in classes 9, 35 and 41; (c) the handle `welllisted.uk` / `welllisteduk` / `well.listed.uk` on TikTok, Instagram, YouTube and Pinterest. If something very similar exists in the same field, pick an alternative from `01-brief/BRIEF.md` and tell Claude to rename everything (it can do it in one go).
2. **Create the brand email (5 min).** Make a new free Gmail or Outlook address using the brand name, not yours (birthday and phone number are only for account recovery and are not shown publicly). This email is used for every account below.
3. **Choose a registered office and service address (10 min).** A company's registered office address is public, and so is each director's correspondence ("service") address. To keep your home off the public register, sign up for a registered office and director service address service from a UK provider (search "registered office address service UK"; many company formation agents offer both for a yearly fee, check what is included). Your home (usual residential) address is still given to Companies House but is not shown publicly. Note the new address: it also goes in the website footer and the email footer.
4. **Verify your identity for Companies House (10 min).** Companies House now asks company directors to verify their identity, usually online with GOV.UK One Login and a photo ID. Do this first if the application asks for it (check the current process on gov.uk, search "Companies House verify identity").
5. **Register the company online (20 min).** On gov.uk, search "set up a limited company" and use the Companies House online service. Typical choices: company name as checked in step 1; private company limited by shares; you as the only director and shareholder (one share of £1 is common); model articles of association; the registered office from step 3 as the company's address and your service address; a nature of business (SIC) code that fits selling digital downloads online (gov.uk lists the codes; ask an accountant if unsure). Pay the fee shown on the site (see MONEY.md). Tell Claude "the company application is in" so it can update STATE.md. **This is general information, not legal advice.**

### Part 2: Brand and accounts (48 minutes)

6. **Make the logo files (7 min).** In Canva (free, sign up with the brand email): create a 1080 x 1080 design, cream background `#FAF6EF`, the letters "WL" in Archivo or Montserrat ExtraBold, colour `#1F2A44`, and a green tick `#1E7F55`. Download as PNG. This is your profile picture everywhere. Details: `01-brief/BRAND-GUIDE.md`.

For each social account: sign up with the brand email, use the brand logo, and paste the bio below. Switch to a **business or creator account** (free) so you get analytics.

**Bio (use on all):** `Faster, honest listings for UK sellers. AI prompts for eBay, Vinted, Depop, Etsy and more. Free cheat sheet below.`

7. **TikTok (7 min).** Sign up, set name "Well Listed", handle as close to `welllisted.uk` as possible. Settings: switch to a Business account (category: Education or Business services). Add the bio. The website link field may only appear later; add it when it does. Until then, put "Link in Instagram bio" in the bio.
8. **Instagram (6 min).** Sign up with the brand email (not "continue with Facebook" from your personal Facebook). Switch to a Professional account, Business. Add the bio. The sales page link comes in session 2.
9. **YouTube (6 min).** Using the brand Gmail, create a YouTube **channel** named "Well Listed" (choose "use a custom name", which creates a brand account separate from your personal name). Add the logo and bio.
10. **Pinterest (7 min).** Create a **business** account with the brand email. Create 4 boards: "eBay Selling Tips UK", "Vinted Selling Tips", "Listing Templates and Prompts", "Reseller Organisation".
11. **Email tool (15 min).** Sign up to MailerLite free with the brand email. For the footer address the law requires in marketing emails, use the registered office address from step 3, never your home.
    - Create a group called "Cheat sheet".
    - Create an embedded form with just an email field (and optional first name). Copy its embed code and keep it for session 2.
    - Create an automation: trigger "joins group Cheat sheet". Add the 7 welcome emails from `marketing/e-email/welcome-sequence.md` with the delays written there. Leave the cheat sheet link in email 1 as `[CHEAT_SHEET_LINK]` for now: you fill it in at step 17. Do not switch the automation on yet.
    - Turn on double opt-in (recommended, keeps the list clean).

## Session 2: launch day, once the company number has arrived (71 minutes)

### Part 3: Bank, shop and website (51 minutes)

12. **Open a business bank account for the company (15 min).** Use a UK bank or app that offers business accounts for limited companies (several are free or low cost; compare fees). You need the company number from the Companies House email. Gumroad payouts must go to the company's account, not your personal one.
13. **Gumroad product (13 min).** Sign up at Gumroad with the brand email. Pick the username `welllisted` (or close to it), never your own name: it appears in the product link. In Settings, set the profile name to "Well Listed" and give the company's details where Gumroad asks for business or payout information. Create a product:
   - Name: **The Well Listed Kit**. Price: **£12** (set currency to GBP in settings first).
   - Upload the file `product/dist/Well-Listed-Kit.zip` (download it from GitHub: open the file, tap "Download raw").
   - Description, summary and tags: copy from `marketing/i-marketplace-listings/listings.md` (Gumroad section).
   - Cover image: use the Canva cover described in the same file (5 minutes to make).
   - Turn on "Allow customers to pay what they want"? **No.** Keep it simple.
   - Refund policy: set to match the sales page guarantee (30 days, no questions).
   - Make sure the description includes "Instant download. By buying you agree to immediate access." (it is in the copy in `listings.md`; the terms page relies on it).
   - Connect the company bank account from step 12 for payouts (this is the only place payment details go). Gumroad only pays out once your balance reaches $100 (see MONEY.md for roughly how many sales that is).
   - Copy the product link (it looks like `https://welllisted.gumroad.com/l/...`).
14. **Put the links into the sales page (5 min).** Start a Claude session and paste: the Gumroad link, the brand email, the company's legal details for the footer (company name, "registered in England and Wales" or wherever it is registered, the company number and the registered office address), the launch end date and the MailerLite form embed code. The launch end date is day 14, which is launch day plus 13 days: launch on Monday 5 October 2026 and the end date is Sunday 18 October 2026. Say "fill in the sales site placeholders, rebuild and push". Claude puts the values in `sales-site/placeholders.json`, runs `python3 launch-kit/tools/build_site.py` (which rebuilds the `sales-site/netlify-site/` folder) and pushes the change to GitHub. Never paste passwords. (Details: `sales-site/README.md`.)
15. **Go live on Netlify (12 min).** On a computer (drag and drop does not work on a phone), download a fresh ZIP from GitHub (see "Where the files are" above), unzip it and find `launch-kit/sales-site/netlify-site`. Sign up to Netlify with the brand email. Choose "Add new site", then "Deploy manually", and drag the whole `netlify-site` folder onto the page. Netlify gives you a web address like `random-name-123.netlify.app`: change it to something like `well-listed` in Site configuration, "Change site name". Tell Claude the address and say "put this in site_url, rebuild and push" (this fills in the cheat sheet link and share previews). Download a fresh ZIP again and, in Netlify, open Deploys and drag the new `netlify-site` folder onto the drag and drop box.
16. **Claim the website on Pinterest (6 min).** In Pinterest's business settings, claim the Netlify address, and add it to the Instagram, TikTok (when available), YouTube and Pinterest bios.

### Part 4: Switch on and first posts (20 minutes)

17. **Switch on the emails and test (5 min).** In MailerLite, open welcome email 1 and put in the cheat sheet link: your Netlify address followed by `/free/uk-listing-cheat-sheet.pdf`. Switch the automation on. On your phone: open the site, press the buy button (it should open Gumroad at £12), and sign up with a spare email address to check welcome email 1 arrives with a working cheat sheet link.
18. **Make and post Day 1 Slot A (7 min).** Open the dashboard, find Day 1, and follow the 10-minute method in `marketing/j-tools/free-tools-and-10-minute-workflow.md`. Keep this first one simple (text over a screen recording is fine). Post to TikTok, Instagram Reels and YouTube Shorts.
19. **Make and schedule Day 1 Slot B and the first pin (5 min).** Slot B for 19:30, PIN01 for 12:00 (or now, if it is already past 12:00).
20. **Tell Claude you have launched (3 min).** Start a session and say: "We launched today. Launch date is [today's date]. Gumroad link is [link]. Netlify address is [address]. Company name and number are [details]." It will fill in the Key facts in STATE.md and rebuild the dashboard, so the daily operator knows today is day 1. From tomorrow morning, follow `ROUTINE.md`: add yesterday's numbers, then type "Run OPERATOR.md".

### In the first two weeks (not on launch day)
- Before day 3: do the one-time 30-minute template setup in section 2 of `marketing/j-tools/free-tools-and-10-minute-workflow.md`, so every post after that takes 10 minutes.
- Do the ICO data protection fee self-assessment for the company (5 min, search "ICO fee self assessment").
- Read gov.uk's guidance on running a limited company (search "running a limited company" on gov.uk). It explains the company's filing and tax duties and deadlines. We do not state those rules here: follow gov.uk, or ask an accountant.
- Buy a domain if you want one (about £10) and connect it in Netlify.
- Check the facts STATE.md lists under "Decisions waiting for the owner" (the MailerLite free limit and the others listed there).

**Total: 169 minutes over two sessions (Session 1: 98 minutes, Session 2: 71 minutes).** Both sessions are under 2 hours. If session 1 runs over, move Pinterest (step 10) to session 2.

**No ads yet.** Paid ads are optional and start on day 15 at the earliest, on Meta first (see `marketing/f-paid-ads/test-plan.md`).
