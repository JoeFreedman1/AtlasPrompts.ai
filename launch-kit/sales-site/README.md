# Sales site: how to put it live

Everything here is plain HTML. You fill in a few blanks, drag a folder onto Netlify, and the site is live.

**The easy way (recommended):** paste your Gumroad link, brand email, legal name and address, launch end date and MailerLite form code into a message to Claude and say "fill in the sales site placeholders". Claude writes them into `placeholders.json`, runs `python3 launch-kit/tools/build_site.py`, and the finished folder appears in `netlify-site/`. Never paste passwords.

**Doing it yourself:** edit the values in `placeholders.json` (the name on the left is the placeholder, type your value between the quotes on the right), then ask any Claude session to run the build. Do not edit files inside `netlify-site/` directly: the build replaces that folder each time.

## What is in this folder

| File | What it is |
|---|---|
| `version-a.html` | Sales page, angle A: "accuracy and control". Headline: *AI listings that stick to your facts and sound like a normal person.* |
| `version-b.html` | Sales page, angle B: "time back". Headline: *Clear the listing pile and the buyer messages without losing your evening.* |
| `privacy.html` | Privacy notice (UK GDPR). A template: check it before publishing. |
| `terms.html` | Terms of sale and licence. A template: check it before publishing. |
| `lead-magnet/uk-listing-cheat-sheet.md` | The free "UK Listing Cheat Sheet" source. The build turns it into `netlify-site/free/uk-listing-cheat-sheet.pdf` automatically. |
| `placeholders.json` | The values that replace the [PLACEHOLDERS]. `live_version` chooses A or B for the home page. `site_url` is your Netlify address once you have it |
| `netlify-site/` | Built by the script: the folder you drag onto Netlify. Holds `index.html` (the live version), `b/` (the other version, hidden from Google, for testing), `privacy.html`, `terms.html`, `blog/` (all 10 articles), `free/` (the cheat sheet PDF), `og-image.png` (share preview image) and `robots.txt`. |

**Which file is the home page?** Netlify shows whichever file is called `index.html`. The `netlify-site/index.html` file starts as a copy of `version-a.html`. We suggest launching with version A, because the "AI makes things up" complaint was the strongest thing sellers said in our research.

## Step 1: fill in the placeholders

Put each value into `placeholders.json` (or give them to Claude), then rebuild. The build prints any placeholder still empty. The two HTML comments (the MailerLite embed and the analytics snippet) are pasted into `version-a.html` and `version-b.html` by Claude, because they are code rather than a single value.

| Placeholder | Where it appears | What to put in | Where the value comes from |
|---|---|---|---|
| `[GUMROAD_PRODUCT_LINK]` | Sales page: 3 buy buttons (hero, price box, sticky phone bar) | Your full Gumroad product link, e.g. `https://yourname.gumroad.com/l/wellisted` | Gumroad: open the product, press "Share" or copy the address from the product page (LAUNCH.md step 9) |
| `[LAUNCH END DATE]` | Sales page: hero line under the buy button and price box; terms section 3 | The date the £12 price ends, written out, e.g. `Sunday 18 October 2026` | Day 14 of the launch, which is launch day plus 13 days (launch Monday 5 October 2026, end date Sunday 18 October 2026). The price ends at 11:59pm that night; switch Gumroad to £19 after that and update the page (see "After launch" below) |
| `[BRAND_EMAIL]` | Sales page (guarantee, FAQ, footer), privacy, terms | The brand's own email address, never your personal one | The brand email you created in LAUNCH.md part 1 |
| `[LEGAL NAME]` | Terms and privacy pages only | Your full legal name (you trade as a sole trader under the brand Well Listed) | You fill this in yourself. It must never appear anywhere else: the build warns if it does |
| `[ADDRESS]` | Terms and privacy pages only | Your postal address | You fill this in yourself. Keep the GitHub repository private, because this file holds it |
| `[DATE]` | Top of privacy and terms ("Last updated") | Today's date, e.g. `29 September 2026` | The day you publish |
| `[EMAIL_FORM_ACTION_URL]` | Sales page: the simple sign-up form in the "free cheat sheet" section | Only needed if you use the simple fallback form. Most people will not: see the next row | MailerLite: form settings, "HTML code" option, the address after `action="` |
| `<!-- EMAIL FORM EMBED CODE: paste MailerLite form here -->` | Sales page: "free cheat sheet" section | Paste MailerLite's embed code directly under this line, then delete the whole `<form class="signup" ...> ... </form>` block below it so there are not two forms | MailerLite: Forms, Embedded forms, your form, "Embed", copy the HTML code (LAUNCH.md step 10) |
| `<!-- ANALYTICS SNIPPET -->` | Sales page, privacy and terms: in the `<head>` near the top | Optional. Paste an analytics code snippet here if you add one later. Netlify's built-in analytics needs no code | Your analytics tool. If it sets cookies, you also need a cookie banner and a line in the privacy notice |
| `[ANALYTICS PROVIDER, ...]` | Privacy notice, section 3 | Name the analytics tool and what it records, or delete this bullet if you do not use one | As above |
| `/og-image.png` | Sales page: the preview image used when someone shares the link | Nothing to do: the build makes it automatically | |
| `[SALES_PAGE_URL]` and `[CHEAT_SHEET_LINK]` | Cheat sheet last page, welcome email 1 | Filled automatically from `site_url` (the cheat sheet link becomes `your-site/free/uk-listing-cheat-sheet.pdf`) | Put your Netlify address in `site_url` after step 3, rebuild and redeploy |

**Check you got them all:** the build lists every site placeholder still unfilled. Square brackets inside example prompts (like `[CHECK: ...]` or `[PASTE YOUR NOTES]`) are meant to be there.

**Before you publish privacy.html and terms.html:** read them through. They are plain-English templates, not legal advice. Make sure the 30-day refund in the terms matches the refund policy you set in Gumroad, and that the list of providers (Gumroad, MailerLite, Netlify, Google Fonts) matches what you actually use. The HTML comment at the top of each file says the same thing; it is invisible to visitors.

**Gumroad checkout wording:** the terms say buyers agree to get the download straight away. Check your Gumroad checkout or product page says this too (for example in the product description: "Instant download. By buying you agree to immediate access."). The 30-day refund covers them anyway.

## Step 2: test it on your phone before it goes live

1. Email the `netlify-site/index.html` file to yourself, or put it in Google Drive or iCloud, and open it on your phone. It will look right, apart from the fonts, which may take a second to load.
2. Check: the headline is readable without zooming, nothing runs off the side of the screen, the green buy button at the bottom of the screen appears as you scroll and hides when you reach the price box.
3. Tap a buy button. It should open your Gumroad product. If it opens a page that says `[GUMROAD_PRODUCT_LINK]`, that placeholder has not been replaced.
4. Tap each FAQ question: the answer should open underneath.
5. After going live (step 3), repeat on the real web address, and sign up for the cheat sheet with a spare email address to check the welcome email arrives.

## Step 3: deploy on Netlify by drag and drop

1. Go to https://app.netlify.com and sign up with the brand email.
2. Choose "Add new site" (or "Add new project"), then "Deploy manually".
3. On your computer, find the `netlify-site` folder (if the repo is on GitHub, download it as a ZIP first and unzip it).
4. Drag the whole `netlify-site` **folder** onto the box on the Netlify page. Drag the folder, not the individual files.
5. After a few seconds Netlify gives you an address like `random-name-123.netlify.app`. Go to Site configuration, "Change site name" to pick something like `well-listed`.
6. To update the site later, open the site in Netlify, go to Deploys, and drag the updated folder onto the "drag and drop" box at the bottom. It replaces the old version.

The privacy and terms links in the footer (`/privacy.html`, `/terms.html`) only work once the site is on Netlify, because they point to the site's own address. They will not open when you view the file from your phone's downloads.

## Step 4: turn the cheat sheet into a PDF

Done for you: the build makes `netlify-site/free/uk-listing-cheat-sheet.pdf`. Once the site is live, its link is `your-site-address/free/uk-listing-cheat-sheet.pdf`. Put that link in welcome email 1 (in place of `[CHEAT_SHEET_LINK]`).

## Swapping between version A and version B

The two versions have different headlines, different examples and a different section order, so you can test which angle works better.

1. Change `live_version` in `placeholders.json` to `"B"` (or ask Claude to).
2. Rebuild, then drag the new `netlify-site` folder onto Netlify again (step 3, point 6).

To go back, set it to `"A"`. Whichever version is not live is still reachable at `your-site/b/` (or `/a/`) for checking, and is hidden from Google.

**How to test fairly:** run one version for a full week, then the other for a full week, and compare Gumroad's "views to sales" figure and the number of cheat sheet sign-ups (log both in `metrics/`). Change only the page, not your posting, during the test. Small numbers swing a lot, so do not decide on a handful of sales.

## After launch

- **After 11:59pm on the launch end date (or first thing the next morning, day 15):** change the Gumroad price to £19. Ask Claude to switch both sales pages to £19 (hero button, price box, buy button, sticky bar; remove the launch price note), rebuild and redeploy. Do not extend or restart the launch price: that would make the "ends on" date untrue.
- **When you get real reviews:** only add them with the buyer's permission, word for word, and replace the "New for 2026: no reviews yet" line. Never write or edit a review yourself.
- **If the kit changes** (for example the number of prompts), update the "What is inside" section and the price box so every number on the page stays true. The prompt counts on the page were taken from the kit source files on 29 September 2026 (after the second product critique round): A 6, B 7, T 8, D 10, K 7, PH 7, R 8, M 12, V 6, C 11, W 8 (90 in total, in modules 00 to 10; modules 11 and 12 are examples and the cheatsheet). Recount with: `grep -cE "^### [A-Z]{1,2}[0-9]+ " launch-kit/product/source/*.md`
