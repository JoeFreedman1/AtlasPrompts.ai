# Assumptions and decisions made overnight

I worked without asking questions, so here is every judgement call I made. Change any of them and tell the next session (it reads this file).

## The business
1. **The "business models in the repo" are the Atlas Prompts products** (LaunchPad, Creator's Toolkit, Scale-Up Blueprint, general prompt packs, the blog, paid updates). I also scored a niche version of the same prompt-blueprint format aimed at UK marketplace sellers, because it matches your expertise. It won. See `01-brief/BUSINESS-MODELS-SCORED.md`.
2. **New brand:** "Well Listed". The existing Atlas Prompts website in `public/` is untouched and is not linked from anything new. I assumed Atlas Prompts may be connected to you, so the new brand shares nothing with it (no name, colours, fonts or links).
3. **The product is digital only** (PDF, HTML, text and CSV files). No stock, no shipping, no food or FMCG.
4. **Target market is the UK.** Prices are in pounds, spelling is UK English, and platform rules quoted are the UK versions.

## Platforms and tools
5. **Checkout: Gumroad.** It costs nothing up front. **Checked by the owner:** Gumroad charges 10% plus $0.50 per direct sale, plus card processing of about 2.9% plus $0.30; it is the merchant of record and handles UK and EU VAT, so the business does not need to register for VAT for Gumroad sales; and it pays out only once the balance reaches $100 (see `MONEY.md` for roughly how many sales that takes). Payhip and Lemon Squeezy are noted as alternatives in `research/tools-and-fees.md` and `marketing/i-marketplace-listings/listings.md`.
6. **Website hosting: Netlify free plan**, drag-and-drop deploy of the `sales-site/netlify-site/` folder. Values (Gumroad link, dates, and the owner's legal name and address for the terms and privacy pages) go in `sales-site/placeholders.json`, then `python3 launch-kit/tools/build_site.py` rebuilds the folder.
7. **Email:** there is no email sign-up. The site collects no personal data and the free cheat sheet is a direct download (owner's decision, 30 September 2026). Welcome emails are off. MailerLite's free plan was cut on 1 July 2026 to 250 subscribers and 2,500 emails a month, with 3 automations and 3 forms, and it requires a postal address in every email footer; Kit's free plan (up to 10,000 subscribers) is the alternative if emails are ever switched on. I did not create any account.
8. **AI tools the buyer uses: free tiers** of ChatGPT, Claude, Gemini or Microsoft Copilot. The kit works with any of them.
9. **Internet research:** web search was available but limited (the search budget ran out, and most official pages could not be opened directly). The research folder cites sources and labels every fact VERIFIED, SECONDARY or NOT VERIFIED. A fact-check session on 30 September 2026 verified most of the open items from official page text (list in `research/STILL-TO-VERIFY.md`). Platform rules change often, so the product tells buyers to check the platform's help page too.

## Pricing
10. **Launch price £12, full price £19.** The launch price runs for days 1 to 14 (day 1 is launch day) and ends at 11:59pm on day 14; £19 from day 15. Reasoning is in `MONEY.md`. Generic prompt packs sell for a few pounds on Etsy, so we compete on being UK-specific, accurate and tidy, not on the number of prompts.

## Faceless and legal identity (please read)
11. **Faceless means:** no name, face, voice, handwriting, home or personal account appears in any content, and the brand has its own email and social accounts.
12. **No personal details anywhere (owner's decision, 30 September 2026).** The owner trades as a sole trader under the brand name Well Listed. Their name and address appear nowhere in the site or the repo. All sales are made through Gumroad as merchant of record, and the terms say so; the contact is `hello.welllisted@gmail.com`. The site collects no personal data (no forms, accounts, analytics or tracking cookies), and the privacy page says so and points to Gumroad's own privacy policy for purchases. **Known risk:** UK rules for websites that sell (the Electronic Commerce Regulations 2002) generally expect the trader's name and geographic address to be easy to find. Because Gumroad is the seller of record, this may be covered by Gumroad's details, but that is not certain. If it ever matters, the low-cost fix is a business address service, which is outside the £0 budget. **This is general information, not legal advice.**
13. **Tax is not described anywhere in this kit or its content.** Gumroad handles VAT on its sales (point 5). For everything else about tax, follow gov.uk (search "selling online tax" or "working for yourself") or ask an accountant. Posts and product text point people to gov.uk and never state tax rules or thresholds.
14. **ICO data protection fee:** the ICO says processing personal data only for advertising and marketing your own goods, and for accounts and records, does not need the fee (verified 30 September 2026: https://ico.org.uk/for-organisations/data-protection-fee/data-protection-fee/exemptions/). Well Listed looks exempt, but do the ICO's free online self-assessment in the first two weeks (about 5 minutes) to confirm. This is in `LAUNCH.md`.

## Content
15. **No testimonials, reviews, sales figures or income claims exist anywhere.** Where a sales page would normally show reviews, it says so honestly and uses an explanation of what is inside instead. Add real reviews only once real buyers give permission.
16. **All example listings in the product and marketing are invented items** written by me (for example "a grey Next wool-blend jumper, size 12"). Brand names of items (Next, Levi's, LEGO) appear only as example items, which is normal descriptive use.
17. **Accounts named in `research/faceless-accounts.md`** are real public accounts found by search, used only as examples to learn from. Follower counts are not quoted because they change and could not all be verified.
18. **The AI voiceover** should be a text-to-speech voice, never a clone of anyone's voice.
19. **No dashes rule:** no em dashes or en dashes are used anywhere (checked with an automatic search in Phase 8).

## Systems
20. **Metrics** live in `launch-kit/metrics/` as CSV files you fill in by hand (or paste from exports). The dashboard reads the latest one when a future session rebuilds it, because a static page on your phone cannot read files from the repo by itself.
21. **The folder layout** follows your brief: everything in `launch-kit/`, with `CLAUDE.md`, `STATE.md` and `OPERATOR.md` at the repo root.
22. **Budget is £0 (owner's decision).** Only free plans: Gumroad, Netlify (300 free credits a month, hard limit, so it can never be charged), MailerLite free (only if emails are switched on), free social accounts and free content tools. No domain, no paid tools, no company costs.
23. **Paid ads are for later, only once sales cover it.** The ads files (`marketing/f-paid-ads/`) are kept but marked "later": the £5 a day test only starts once money kept from sales covers the test budget (about £70), and then on Meta first, because TikTok Ads Manager's minimum budgets are more than $50 a day per campaign and $20 a day per ad group (verified 30 September 2026), well above £5 a day.
