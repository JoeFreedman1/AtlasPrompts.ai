# Assumptions and decisions made overnight

I worked without asking questions, so here is every judgement call I made. Change any of them and tell the next session (it reads this file).

## The business
1. **The "business models in the repo" are the Atlas Prompts products** (LaunchPad, Creator's Toolkit, Scale-Up Blueprint, general prompt packs, the blog, paid updates). I also scored a niche version of the same prompt-blueprint format aimed at UK marketplace sellers, because it matches your expertise. It won. See `01-brief/BUSINESS-MODELS-SCORED.md`.
2. **New brand:** "Well Listed". The existing Atlas Prompts website in `public/` is untouched and is not linked from anything new. I assumed Atlas Prompts may be connected to you, so the new brand shares nothing with it (no name, colours, fonts or links).
3. **The product is digital only** (PDF, HTML, text and CSV files). No stock, no shipping, no food or FMCG.
4. **Target market is the UK.** Prices are in pounds, spelling is UK English, and platform rules quoted are the UK versions.

## Platforms and tools
5. **Checkout: Gumroad.** It costs nothing up front, and since January 2025 Gumroad acts as "merchant of record", meaning it calculates and pays VAT and sales taxes on each sale for you. That removes the biggest tax headache for digital downloads sold abroad. Fees are higher than some rivals (10% plus 50 US cents per sale, plus card processing). Payhip and Lemon Squeezy are noted as alternatives in `MONEY.md`.
6. **Website hosting: Netlify free plan**, drag-and-drop deploy of a single HTML file.
7. **Email: MailerLite free plan** (or any free tool with a sign-up form). I did not create any account.
8. **AI tools the buyer uses: free tiers** of ChatGPT, Claude, Gemini or Microsoft Copilot. The kit works with any of them.
9. **Internet research:** web search was available, so the research folder cites sources. Some sites could not be fetched directly; where a fact could not be confirmed it is marked "check before relying on this". Platform rules change often, so the product tells buyers to check the platform's help page too.

## Pricing
10. **Launch price £12, full price £19.** Reasoning is in `MONEY.md`. Generic prompt packs sell for a few pounds on Etsy, so we compete on being UK-specific, tested and tidy, not on the number of prompts.

## Faceless and legal identity (please read)
11. **Faceless means:** no name, face, voice, handwriting, home or personal account appears in any content, and the brand has its own email and social accounts.
12. **UK law still needs a trader identity somewhere.** A website that sells or collects emails must say who runs it (Electronic Commerce Regulations 2002, UK GDPR privacy notices). If you trade as a **sole trader**, your legal name must appear in the small-print legal notice and privacy policy. If that is not acceptable, set up a **private limited company** (£50 at Companies House online at the time of writing; check the current fee) and use a registered office address service so your home address is not shown. Directors' names are still on the public Companies House register, but are not on the brand's site or content. The sales pages have a placeholder `[LEGAL NAME AND ADDRESS]` in the footer for whichever you choose. **This is general information, not legal advice.**
13. **Because Gumroad is the merchant of record**, Gumroad handles the sale itself and VAT on it. You still need to register with HMRC for Self Assessment if your trading income goes over the £1,000 trading allowance in a tax year.
14. **ICO data protection fee:** businesses that only process personal data for their own marketing, accounts and records are often exempt. Use the ICO's online self-assessment during launch week (it takes about 5 minutes). This is in `LAUNCH.md`.

## Content
15. **No testimonials, reviews, sales figures or income claims exist anywhere.** Where a sales page would normally show reviews, it says so honestly and uses an explanation of what is inside instead. Add real reviews only once real buyers give permission.
16. **All example listings in the product and marketing are invented items** written by me (for example "a grey Next wool-blend jumper, size 12"). Brand names of items (Next, Levi's, LEGO) appear only as example items, which is normal descriptive use.
17. **Accounts named in `research/faceless-accounts.md`** are real public accounts found by search, used only as examples to learn from. Follower counts are not quoted because they change and could not all be verified.
18. **The AI voiceover** should be a text-to-speech voice, never a clone of anyone's voice.
19. **No dashes rule:** no em dashes or en dashes are used anywhere (checked with an automatic search in Phase 8).

## Systems
20. **Metrics** live in `launch-kit/metrics/` as CSV files you fill in by hand (or paste from exports). The dashboard reads the latest one when a future session rebuilds it, because a static page on your phone cannot read files from the repo by itself.
21. **The folder layout** follows your brief: everything in `launch-kit/`, with `CLAUDE.md`, `STATE.md` and `OPERATOR.md` at the repo root.
