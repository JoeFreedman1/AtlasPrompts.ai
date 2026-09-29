# Sales site: how to put it live

Everything here is plain HTML. There is nothing to install or build. You fill in a few blanks, drag a folder onto Netlify, and the site is live.

## What is in this folder

| File | What it is |
|---|---|
| `version-a.html` | Sales page, angle A: "accuracy and control". Headline: *AI listings that stick to your facts and sound like a normal person.* |
| `version-b.html` | Sales page, angle B: "time back". Headline: *Clear the listing pile and the buyer messages without losing your evening.* |
| `privacy.html` | Privacy notice (UK GDPR). A template: check it before publishing. |
| `terms.html` | Terms of sale and licence. A template: check it before publishing. |
| `lead-magnet/uk-listing-cheat-sheet.md` | The free "UK Listing Cheat Sheet" that people get for signing up. Turn it into a PDF (see step 4) and put the PDF link in your first welcome email. It is not part of the website. |
| `netlify-site/` | The folder you drag onto Netlify. It holds `index.html` (a copy of version A), `privacy.html` and `terms.html`. |

**Which file is the home page?** Netlify shows whichever file is called `index.html`. The `netlify-site/index.html` file starts as a copy of `version-a.html`. We suggest launching with version A, because the "AI makes things up" complaint was the strongest thing sellers said in our research.

## Step 1: fill in the placeholders

Open each file in `netlify-site/` in a plain text editor (Notepad on Windows, TextEdit on a Mac set to plain text, or edit directly on GitHub with the pencil icon). Use Find and Replace (Ctrl+H on Windows, Cmd+Option+F on a Mac) for each placeholder below. Type the placeholder exactly, including the square brackets.

| Placeholder | Where it appears | What to put in | Where the value comes from |
|---|---|---|---|
| `[GUMROAD_PRODUCT_LINK]` | Sales page: 3 buy buttons (hero, price box, sticky phone bar) | Your full Gumroad product link, e.g. `https://yourname.gumroad.com/l/wellisted` | Gumroad: open the product, press "Share" or copy the address from the product page (LAUNCH.md step 9) |
| `[LAUNCH END DATE]` | Sales page: price box | The date the £12 price ends, written out, e.g. `Sunday 18 October 2026` | 14 days after the day you go live. On that date, change the price in Gumroad to £19 and update the page (see "After launch" below) |
| `[BRAND_EMAIL]` | Sales page (guarantee, FAQ, footer), privacy, terms | The brand's own email address, never your personal one | The brand email you created in LAUNCH.md part 1 |
| `[LEGAL NAME AND ADDRESS]` | Footer of every page, privacy and terms section 1 | Sole trader: your legal name and a business address. Company: the company name, company number and registered office address | See ASSUMPTIONS.md point 12. A registered office or PO box service keeps your home address off the site |
| `[LEGAL NAME]` | Privacy and terms, section 1 | The same legal name or company name as above, without the address | As above |
| `[DATE]` | Top of privacy and terms ("Last updated") | Today's date, e.g. `29 September 2026` | The day you publish |
| `[EMAIL_FORM_ACTION_URL]` | Sales page: the simple sign-up form in the "free cheat sheet" section | Only needed if you use the simple fallback form. Most people will not: see the next row | MailerLite: form settings, "HTML code" option, the address after `action="` |
| `<!-- EMAIL FORM EMBED CODE: paste MailerLite form here -->` | Sales page: "free cheat sheet" section | Paste MailerLite's embed code directly under this line, then delete the whole `<form class="signup" ...> ... </form>` block below it so there are not two forms | MailerLite: Forms, Embedded forms, your form, "Embed", copy the HTML code (LAUNCH.md step 10) |
| `<!-- ANALYTICS SNIPPET -->` | Sales page, privacy and terms: in the `<head>` near the top | Optional. Paste an analytics code snippet here if you add one later. Netlify's built-in analytics needs no code | Your analytics tool. If it sets cookies, you also need a cookie banner and a line in the privacy notice |
| `[ANALYTICS PROVIDER, ...]` | Privacy notice, section 3 | Name the analytics tool and what it records, or delete this bullet if you do not use one | As above |
| `/og-image.png` | Sales page: the preview image used when someone shares the link | Not a placeholder to type over: add an image file called `og-image.png` (1200 x 630 pixels) into `netlify-site/` next to `index.html` | Make it in Canva: cream background, "Well Listed" logo, the headline, parcel-label style |
| `[SALES_PAGE_URL]` | Lead magnet cheat sheet, last page | The live site address, e.g. `https://well-listed.netlify.app` | Netlify, after step 3 |

**Check you got them all:** use Find to search each file for `[` . The only square brackets left on the sales page should be the `[CHECK: ...]` examples and the `[BUYER]` example in the FAQ, which are meant to be there.

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

The cheat sheet is written in Markdown (plain text with simple formatting). Easiest route: open https://github.com on the repo, open `lead-magnet/uk-listing-cheat-sheet.md` (GitHub shows it formatted), and use your browser's Print, "Save as PDF". Or paste it into Google Docs or Canva and export as PDF. It prints at around 3 to 4 pages. Upload the PDF to MailerLite (Files) or Google Drive (set to "anyone with the link can view") and put that link in welcome email 1.

## Swapping between version A and version B

The two versions have different headlines, different examples and a different section order, so you can test which angle works better.

1. Make sure the placeholders are also filled in on the other version (open `version-b.html` and do the same Find and Replace as in step 1).
2. Copy `version-b.html` into the `netlify-site` folder and rename it to `index.html`, replacing the old one.
3. Drag the `netlify-site` folder onto Netlify again (step 3, point 6).

To go back, do the same with `version-a.html`.

**How to test fairly:** run one version for a full week, then the other for a full week, and compare Gumroad's "views to sales" figure and the number of cheat sheet sign-ups (log both in `metrics/`). Change only the page, not your posting, during the test. Small numbers swing a lot, so do not decide on a handful of sales.

## After launch

- **On the launch end date:** change the Gumroad price to £19. On the sales page, change "£12" to "£19" in the hero button, price box, buy button and sticky bar, remove the "Full price £19" line and the launch price note, and redeploy. Do not extend or restart the launch price: that would make the "ends on" date untrue.
- **When you get real reviews:** only add them with the buyer's permission, word for word, and replace the "New for 2026: no reviews yet" line. Never write or edit a review yourself.
- **If the kit changes** (for example the number of prompts), update the "What is inside" section and the price box so every number on the page stays true. The prompt counts on the page were taken from the kit source files on 29 September 2026: B 7, T 8, D 10, K 8, PH 8, R 8, M 12, V 8, C 11, W 8 (88 in total), plus the starter prompt in "Start here".
