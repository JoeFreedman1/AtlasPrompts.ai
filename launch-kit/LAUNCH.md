# LAUNCH.md: what you do tomorrow (about 1 hour 55 minutes, under 2 hours)

Do these in order. Each step says how long it should take. Everything else (writing, designing, planning) is already done. Tick them off in `dashboard.html` as you go.

**Before you start:** use a browser profile or phone that is **not** logged in to your personal Google, Instagram or TikTok accounts, so nothing links the brand to you by accident. On a computer, create a new browser profile called "Well Listed" (Chrome: profile icon, Add). On a phone, log out of personal accounts in each app first, or use the app's "add account" option carefully and double-check which account you are posting from every time.

**Security:** use a password manager (e.g. the free one built into your browser or phone) and a unique password for every account below. Turn on two-step verification wherever offered. **Never write passwords in this repo or in chats with Claude.**

---

### Part 1: Brand identity (22 minutes)

1. **Check the name is free (5 min).** Search "Well Listed" on the UK IPO trade mark search (search "UK IPO trade mark search" on Google) in classes 9, 35 and 41, and search the handle `welllisted.uk` / `wellisteduk` / `well.listed.uk` on TikTok, Instagram, YouTube and Pinterest. If something very similar exists in the same field, pick an alternative from `01-brief/BRIEF.md` and tell Claude to rename everything (it can do it in one go).
2. **Create the brand email (5 min).** Make a new free Gmail or Outlook address such as `hello.welllisted@gmail.com` (use the brand name, not yours; birthday and phone number are only for account recovery and are not shown publicly). This email is used for every account below.
3. **Decide the legal identity (5 min).** Read point 12 of `ASSUMPTIONS.md`. Either (a) sole trader: your legal name goes only in the legal notice at the bottom of the sales page, or (b) limited company: set it up this week and launch with it (adds cost, see MONEY.md). Write your choice in STATE.md (Claude can do this for you). **If unsure, choose (a) for launch and switch later.**
4. **Make the logo files (7 min).** In Canva (free, sign up with the brand email): create a 1080 x 1080 design, cream background `#FAF6EF`, the letters "WL" in Archivo or Montserrat ExtraBold, colour `#1F2A44`, and a green tick `#1E7F55`. Download as PNG. This is your profile picture everywhere. Details: `01-brief/BRAND-GUIDE.md`.

### Part 2: Social accounts (26 minutes)

For each: sign up with the brand email, use the brand logo, and paste the bio below. Switch to a **business or creator account** (free) so you get analytics.

**Bio (use on all):** `Faster, honest listings for UK sellers. AI prompts for eBay, Vinted, Depop, Etsy and more. Free cheat sheet below.`

5. **TikTok (7 min).** Sign up, set name "Well Listed", handle as close to `welllisted.uk` as possible. Settings: switch to a Business account (category: Education or Business services). Add the bio. The website link field may only appear later; add it when it does. Until then, put "Link in Instagram bio" in the bio.
6. **Instagram (6 min).** Sign up with the brand email (not "continue with Facebook" from your personal Facebook). Switch to a Professional account, Business. Add the bio and the sales page link (you get it in step 12, so come back to add it).
7. **YouTube (6 min).** Using the brand Gmail, create a YouTube **channel** named "Well Listed" (choose "use a custom name", which creates a brand account separate from your personal name). Add the logo and bio.
8. **Pinterest (7 min).** Create a **business** account with the brand email. Create 4 boards: "eBay Selling Tips UK", "Vinted Selling Tips", "Listing Templates and Prompts", "Reseller Organisation". Claim your website once it is live (step 12, optional today).

### Part 3: Shop, website and email (48 minutes)

9. **Gumroad product (13 min).** Sign up at Gumroad with the brand email. Create a product:
   - Name: **The Well Listed Kit**. Price: **£12** (set currency to GBP in settings first).
   - Upload the file `product/dist/Well-Listed-Kit.zip` (download it from GitHub: open the file, tap "Download raw").
   - Description, summary and tags: copy from `marketing/i-marketplace-listings/listings.md` (Gumroad section).
   - Cover image: use the Canva cover described in the same file (5 minutes to make).
   - Turn on "Allow customers to pay what they want"? **No.** Keep it simple.
   - Refund policy: set to match the sales page guarantee (30 days, no questions).
   - Connect your bank account for payouts (Gumroad asks for this; this is the only place payment details go).
   - Copy the product link (it looks like `https://yourname.gumroad.com/l/...`).
10. **Email tool (15 min).** Sign up to MailerLite free with the brand email. It will ask for a physical address for the footer of emails (the law requires one): use your business address, or a PO box or registered office service if you prefer not to use home (see ASSUMPTIONS.md point 12).
    - Create a group called "Cheat sheet".
    - Create an embedded form with just an email field (and optional first name). Copy its embed code.
    - Create an automation: trigger "joins group Cheat sheet". Add the 7 welcome emails from `marketing/e-email/welcome-sequence.md` with the delays written there. Put the cheat sheet download link in email 1 (step 12 gives you the link).
    - Turn on double opt-in (recommended, keeps the list clean).
11. **Put the links into the sales page (5 min).** Open `sales-site/README.md` and follow "Fill in the placeholders": paste the Gumroad link, the MailerLite form code and your legal name or company in the footer. Claude can do this for you if you paste the Gumroad link and form code into a message (never passwords).
12. **Go live on Netlify (10 min).** Sign up to Netlify with the brand email. Choose "Deploy manually" and drag the folder `sales-site/netlify-site/` onto the page (download it from GitHub first as a zip, and unzip it). Netlify gives you a web address like `well-listed.netlify.app` (change the site name in Site settings). Test on your phone: open the page, press the buy button (it should open Gumroad), and sign up with a spare email to check the cheat sheet arrives.
13. **Add the link everywhere (5 min).** Put the Netlify address in the Instagram, TikTok (when available), YouTube and Pinterest bios.

### Part 4: First posts (18 minutes)

14. **Make and post Day 1 Slot A (8 min).** Open `dashboard.html`, find Day 1, and follow the 10-minute method in `marketing/j-tools/free-tools-and-10-minute-workflow.md`. Post to TikTok, Instagram Reels and YouTube Shorts.
15. **Schedule Day 1 Slot B and the first pin (5 min).** Slot B for 19:30, PIN01 for 12:00 (or now, if it is already past 12:00).
16. **Tell Claude you have launched (5 min).** Start a session and say: "We launched today. Launch date is [today's date]. Gumroad link is [link]. Netlify address is [address]." It will update STATE.md so the daily operator knows day 1. Then add the first metrics row tomorrow morning.

### This week (not today)
- Do the ICO data protection fee self-assessment (5 min, search "ICO fee self assessment").
- Buy a domain if you want one (about £10) and connect it in Netlify.
- If you chose a limited company, set it up and update the legal notice.
- Register for Self Assessment with HMRC if you expect trading income over £1,000 this tax year.

**Total: 114 minutes (1 hour 54 minutes).** If a step runs over, skip step 8 (Pinterest) and do it tomorrow.
