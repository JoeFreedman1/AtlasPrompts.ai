# Assumptions and decisions made overnight

I worked without asking questions, so here is every judgement call I made. Change any of them and tell the next session (it reads this file).

## The business
1. **The "business models in the repo" are the Atlas Prompts products** (LaunchPad, Creator's Toolkit, Scale-Up Blueprint, general prompt packs, the blog, paid updates). I also scored a niche version of the same prompt-blueprint format aimed at UK marketplace sellers, because it matches your expertise. It won. See `01-brief/BUSINESS-MODELS-SCORED.md`.
2. **New brand:** "Well Listed". The existing Atlas Prompts website in `public/` is untouched and is not linked from anything new. I assumed Atlas Prompts may be connected to you, so the new brand shares nothing with it (no name, colours, fonts or links).
3. **The product is digital only** (PDF, HTML, text and CSV files). No stock, no shipping, no food or FMCG.
4. **Target market is the UK.** Prices are in pounds, spelling is UK English, and platform rules quoted are the UK versions.

## Platforms and tools
5. **Checkout: Gumroad.** It costs nothing up front. **Checked by the owner:** Gumroad charges 10% plus $0.50 per direct sale, plus card processing of about 2.9% plus $0.30; it is the merchant of record and handles UK and EU VAT, so the business does not need to register for VAT for Gumroad sales; and it pays out only once the balance reaches $100 (see `MONEY.md` for roughly how many sales that takes). Payhip and Lemon Squeezy are noted as alternatives in `research/tools-and-fees.md` and `marketing/i-marketplace-listings/listings.md`.
6. **Website hosting: Netlify free plan**, drag-and-drop deploy of the `sales-site/netlify-site/` folder. Values (Gumroad link, dates, legal notice) go in `sales-site/placeholders.json`, then `python3 launch-kit/tools/build_site.py` rebuilds the folder.
7. **Email: MailerLite free plan** (or any free tool with a sign-up form). I did not create any account.
8. **AI tools the buyer uses: free tiers** of ChatGPT, Claude, Gemini or Microsoft Copilot. The kit works with any of them.
9. **Internet research:** web search was available but limited (the search budget ran out, and most official pages could not be opened directly). The research folder cites sources and labels every fact VERIFIED, SECONDARY or NOT VERIFIED; many are NOT VERIFIED. Platform rules change often, so the product tells buyers to check the platform's help page too.

## Pricing
10. **Launch price £12, full price £19.** The launch price runs for days 1 to 14 (day 1 is launch day) and ends at 11:59pm on day 14; £19 from day 15. Reasoning is in `MONEY.md`. Generic prompt packs sell for a few pounds on Etsy, so we compete on being UK-specific, accurate and tidy, not on the number of prompts.

## Faceless and legal identity (please read)
11. **Faceless means:** no name, face, voice, handwriting, home or personal account appears in any content, and the brand has its own email and social accounts.
12. **The brand trades through a new private limited company (owner's decision).** A website that sells or collects emails must say who runs it, so the legal notice and privacy notice name the **company** (company name, where it is registered, company number and registered office address), not a person. A registered office and director service address service keeps your home address off the public register and off the site. Your name will still appear on the public Companies House register as a director, but nowhere on the brand's site, emails or content. The company must exist before the Gumroad payouts, business bank account and legal notice can be finished, so `LAUNCH.md` is split into two sessions: set-up tomorrow, launch once the company number arrives. The Companies House fee is reported as £100 (check the current fee on gov.uk). The sales pages keep the placeholder `[LEGAL NAME AND ADDRESS]` for the company details. **This is general information, not legal advice.**
13. **Tax is not described anywhere in this kit or its content.** Gumroad handles VAT on its sales (point 5). For everything else about the company's tax and filing duties, follow gov.uk (search "running a limited company") or ask an accountant. Posts and product text point people to gov.uk and never state tax rules or thresholds.
14. **ICO data protection fee:** businesses that only process personal data for their own marketing, accounts and records are often exempt (not verified: check). The company should do the ICO's online self-assessment in the first two weeks (about 5 minutes). This is in `LAUNCH.md`.

## Content
15. **No testimonials, reviews, sales figures or income claims exist anywhere.** Where a sales page would normally show reviews, it says so honestly and uses an explanation of what is inside instead. Add real reviews only once real buyers give permission.
16. **All example listings in the product and marketing are invented items** written by me (for example "a grey Next wool-blend jumper, size 12"). Brand names of items (Next, Levi's, LEGO) appear only as example items, which is normal descriptive use.
17. **Accounts named in `research/faceless-accounts.md`** are real public accounts found by search, used only as examples to learn from. Follower counts are not quoted because they change and could not all be verified.
18. **The AI voiceover** should be a text-to-speech voice, never a clone of anyone's voice.
19. **No dashes rule:** no em dashes or en dashes are used anywhere (checked with an automatic search in Phase 8).

## Systems
20. **Metrics** live in `launch-kit/metrics/` as CSV files you fill in by hand (or paste from exports). The dashboard reads the latest one when a future session rebuilds it, because a static page on your phone cannot read files from the repo by itself.
21. **The folder layout** follows your brief: everything in `launch-kit/`, with `CLAUDE.md`, `STATE.md` and `OPERATOR.md` at the repo root.
22. **Paid ads start on Meta, not TikTok.** TikTok Ads Manager's minimum daily budget has historically been well above £5 a day (not verified for the UK), so the optional £5 a day test starts on Meta from day 15. See `marketing/f-paid-ads/test-plan.md`.
23. **Ad budget before day 15 is £0.** No ads run at the £12 launch price.
