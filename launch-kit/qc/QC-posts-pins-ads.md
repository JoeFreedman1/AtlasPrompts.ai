# QC: short-form posts, Pinterest pins and paid ads

Reviewed 29 September 2026 against QUALITY-CHECKLIST.md, 01-brief/WRITING-RULES.md, BRAND-GUIDE.md, marketing/POST-PLAN.md, marketing/POST-FORMAT.md and research/platform-rules-uk.md.

Files: `marketing/b-short-form-posts/posts-P01-P20.md`, `posts-P21-P40.md`, `posts-P41-P60.md`, `marketing/c-pinterest/pins.md`, `marketing/f-paid-ads/ads.md`, `marketing/f-paid-ads/test-plan.md`.

Result after fixes: `check_content.py` reports 0 problems (16 warnings, all deliberate: Americanisms shown as words to avoid in P18, P38 and P41 and in ads A05, A06 and A13). `build_dashboard.py` reports posts: 60, pins: 30. All POST-FORMAT headings and pin field labels unchanged.

Overall: the batch was already well above average (honest, faceless, careful with platform facts). The real problems were repetition across the 60 (the same grey Next jumper, the same boots and pricing numbers, the same casserole, the same "small mark on left cuff", the same "Here is..." hook shape), two scheduled posts quoting the launch price after it ends, a few character counts that did not add up, policy wording that went further than our fact sheet, and "tested" as an unsupported claim in ads.

## Issues found and fixes made

| File / ID | Problem | Fix made |
|---|---|---|
| P12 (day 23), P16 (day 15) | "£12 at launch" in posts the calendar schedules after the 14-day launch window. That is an inaccurate price, and reads as fake urgency. | Price lines replaced with "Link in bio". Added a production note to the P01 to P20 and P41 to P60 headers: "£12 at launch" only in posts published inside the window. |
| P53 (day 7) | Launch price correct on day 7, but the product tour is the post most likely to be reposted or boosted later. | Visuals now say to change the price line to £19 if published or reposted after the window. |
| P05 vs P24 | Near duplicates: same Clarks Chelsea boots UK 6, same £20 to £32 comps, same median £25, list £28, floor £18, same closing line "You find the prices. AI does the maths." | P24 rewritten: Hunter wellies, new figures (£18 to £30, list £27, floor £20), and a new teaching point (drop poor matches: compare condition, not just the name). New hook. |
| P05, P24, P49 | Three pricing hooks with the same shape ("Stop asking AI what it is worth", "'What's this worth?' is the worst question"). | P24 hook now "Guessed £45. The last five matching pairs sold for £18 to £30." P49 hook now "Sealed, opened or loose. Mix them up and your LEGO price is wrong before you start." |
| P06 vs P30 | Same item and numbers: £65 listing, £56 counter, cast iron casserole b-roll in both. | P30 changed to an example Dualit toaster (list £45, floor £32, accept £40+, counter £38). |
| P18, P29, P58 | Three posts making the same point with the same example (grey Next jumper, invented "merino", Americanisms). | P29 rewritten around a cordless drill where AI invents a second battery (a real not-as-described risk). P58 rewritten around AI knowing out-of-date rules (Amazon UK 75-character title from 27 July 2026), miscounting, softening flaws and privacy of pasted buyer details. P18 keeps the Americanism example. |
| P02 | Also used "merino". Hook blamed the viewer ("You are briefing it badly"). | Hook now "'Blue jumper, good condition.' That is all the AI got. So it invented cashmere." Invented fabric changed to cashmere throughout. |
| Grey Next jumper (P18, P25, P29, P35, P36, P52, P55, P58, P60) | Same example item in 9 posts. | Kept only in P18 (Kit module example). P25 chinos, P29 drill, P35 corduroy skirt, P36 rain jacket, P52 and P60 wellies, P55 camera, P58 no item. |
| "Small mark on left cuff, about 5 mm" (P07, P35, P41, P42, P57, PIN06, A11) | Same flaw example reused 7 times. | Varied: hem pulled thread (P41, PIN06, A11), faded shoulder patch (P42), faded pocket edge (P35), pulled threads on the back (P57). P07 keeps the original. |
| P20 vs P32 | Same hook shape (a row of vibe hashtags) and same lesson (no false "vintage"). | P32 rewritten: "Depop gives you 5 hashtags. #fyp should not be one of them." Cherry red Dr. Martens example, focused on vibe words vs search words. P20 keeps brand-spam lesson. |
| P09 vs P52 | Same hook: "Ten items. One chat." | P52 hook now "One spreadsheet column shows which of ten listings still need a measurement." |
| P19 vs P44 | Same bundle (three children's tops, £19) and word-for-word identical reply. | P44 now three paperback picture books, £10, different reply wording and a postage-focused hook. |
| P10 vs P35 vs P57 | The "size 12 in 1985" idea repeated three times, including a copied caption line. | P35 new hook on fabric composition ("'Cotton' is not a fabric description. '98% cotton, 2% elastane' is.") and new caption. P57 lesson 3 changed to "say what is not included". |
| P10 | "Size 12 in 2024" dated (it is 2026). | Now "Size 12 today". |
| P04, P16, P48 | Three candle holder examples (P48 is the planned one). | P04 now a block printed linen tea towel with a full new counted tag set. P16 now a macrame plant hanger (before 131 characters, after 85, counted). |
| P04 | Hook "Most shops waste half of them" is an invented statistic. | Hook now "13 Etsy tags. Write 'tea towel' three ways and two of them are wasted." |
| P11 | Claimed the bad title was 138 characters but showed only 89 characters plus "...". On-screen said "breaks 4 rules" but "best" is not a rule. | Full bad title written out (counted: 138). "Breaks 4 rules" changed to "has 4 problems". |
| P27 | Contradiction: hook said "Not Zara" but the after title said the dress was Zara. | Dress is now Warehouse; after title recounted (79 of 80). |
| P48 | "No duplicates" claim, but tags included candle holder, cream candle holder, stoneware tealight and ceramic tealight. | Two overlapping tags replaced (neutral decor, stoneware). Hook no longer "Here is a full set". |
| P47 | Called the jacket "vintage" and used #90sstyle with nothing in the brief to support an era, contradicting our own P20/P32 advice. | Brief now includes "care label dated 1996"; hashtag #90sdenim; caption explains why "vintage" is earned; visuals warn to drop it if the real brief has no evidence. |
| P28 | Accuracy wording: said the 14-day right "doesn't apply to you"; did not say the 14 days run from delivery. | Now "applies when a business sells online. It does not apply to a private sale"; trader slide says "14 days from delivery". Disclaimer reads "general information, not legal or tax advice". Fact note to recheck gov.uk kept. |
| P31 | "Earn less than about £1,700" (the test is money received, not profit); "Reach either and your details can be reported" was vague; caption said "You will not be reported", which is stronger than the rule; trading allowance did not say it is counted before costs; quoted a gov.uk page title we have not verified. | Reworded to "receive less than about £1,700 (2,000 euros) in total"; "Make 30 sales, or go over that amount, and your details will usually be reported"; "A platform does not have to report you if"; allowance "counted on money in before costs, tax year 6 April to 5 April"; "thresholds can change"; unverified page title removed. Disclaimer "general information, not legal or tax advice" on slide and caption. Fact note to recheck gov.uk kept. |
| P22 | "Business sellers ... you have to offer returns" is an oversimplification and the post had no legal disclaimer. | Now "online buyers usually get 14 days to cancel, plus rights if an item is faulty", with "general information, not legal advice" in VO, on-screen text and caption. |
| P12, P51 | Said TikTok Shop UK's policies require claims to be "genuine, accurate and verifiable": that wording is not in our fact sheet. P51 said "no platform names in your copy" (verified only for titles). | Reworded to what is verified: health and medical claims are banned, listings must be accurate, titles must not mention TikTok or other platforms. |
| P59 | "Realistic AI images need labelling" stated as settled fact (SECONDARY in fact sheet); bamboo drawer organiser reused from P11 and P12. | Attributed to "TikTok Shop UK's AI content policy"; example changed to an invented stoneware mug set. |
| P06 | "Fake pressure ... breaks most platforms' rules": unverified claim. | Now "Fake pressure is a bad look, and buyers can usually tell." |
| P24 | "Most platforms' terms forbid [scraping tools] anyway": unverified. | Removed. |
| P26 | Visual example (Denby jug) duplicated P40's worked example. | P26 visual now a Pyrex mixing bowl. |
| Hooks starting "Here is / Here's" (P19, P35, P40, P42, P44, P47, P48, P53, P55, P59) and "Your listing is not ready..." (P41) | Same opener shape across the set, several generic. | All rewritten to lead with a specific detail, e.g. P41 "'[CHECK: size]' went live in the listing. Seven checks so yours never does.", P42 "'Good used condition' could mean worn once or worn to bits.", P55 "eBay counts the spaces. 'Nikon D3200 18-55mm' is 19 characters, not 17.", P59 "'50% OFF' in a TikTok Shop UK title breaks the title rules. So does your shop name." |
| P45 vs P39 | Two late-night time-stamp hooks ("It's 10pm", "POV: it is 11pm"). | P45 hook now "Fourth message. All capitals. And your draft reply is not one you want on record." |
| P55 | Reused "Nice jumper" from P13 and "like Zara" from P41/P43. | Rewritten around a camera title (counted: before 79, after 75), with other-brand spam ("like canon sony") and an untested claim ("works perfect") struck out. |
| P41, P43, P55 | "Like Zara" used as the other-brand example three times. | P41 now "Joules coat, like Barbour"; P55 "like Canon". |
| Caption closers (P03, P07, P10, P30, P41, P42, P44, P57) | "Save this for your next listing" and "grab the free cheat sheet from the link in bio" repeated almost word for word. | Closers varied to fit each post. |
| P16, P49 | Captions over the 150-word limit after edits. | Trimmed to 146 and 144 words. |
| PIN06 | Reused "small pale mark on left cuff". | Now "Pulled thread on the hem, about 2 cm, see photo 6". |
| PIN18 | Title "Best Reply" is an unsupported superlative. | "A Better Reply". |
| PIN25 | "mailing" is not the Americanism AI actually produces; out of step with P38 and A05 ("shipping"). | Changed to "shipping". |
| PIN23 | "7 checks" list differed from P41's "7 checks", both pointing to the same cheat sheet. | Aligned PIN23's description with P41's seven checks. |
| PIN12, PIN14, PIN27 | Five pin descriptions opened "A simple...". | Three rewritten with different openers. |
| PIN10 | Invented AI line had no "Example" label. | Label added. |
| PIN17 | "stop eating your evenings" echoed PIN24. | Reworded to "the same questions take seconds to answer". |
| A07 | Inaccurate: "the AI can't see the stain" (many AI tools can read photos). | Now "Myth: the AI knows about the stain on the cuff." Primary text "Only if you tell it"; card adds "Even from a photo, small marks get missed." |
| A12, A16, A20 | "Tested prompts" is an objective claim that needs evidence before the ad runs (CAP Code). | Replaced with "prompts with worked examples". New rule and checklist line: no "tested" or "proven" without evidence on file. |
| A20 | "Says nothing it can't see" was confusing and not accurate. | "Says nothing you didn't tell it." |
| A09 | Reply "£22, which includes room for postage" was unclear; "all within the rules" vague. | Reply now "The lowest I can do is £22. Happy to answer any questions about the fit." Ad text "Polite, short, kept on the platform." |
| ads.md rules | No rule on income-opportunity framing or implied TikTok partnership; Spark Ads could boost organic posts with an expired launch price. | Added rules 10a (no money-making or "side income" framing, Meta and TikTok both restrict it) and 10b (TikTok is not a partner), and a Spark Ads note. |
| test-plan.md | Policy checks were only by reference. No note on special ad category, income-style targeting, or boosting expired-price posts. | Added a short policy list (Meta personal attributes, money-making framing, before and after, TikTok exaggerated claims, Meta special ad category "none"), a targeting note and two "common mistakes". |

## Checked and left as they are

- Faceless: every post works as text on screen, screen recording, hands-only stock or AI voiceover. Screen-recording blur instructions are present throughout. No real listings, real messages or real accounts are shown; mock-ups are built in Canva.
- No marketplace logos anywhere; "not affiliated" line on every Meta ad and the ad end card; P53 caption carries it too.
- Kit mentions: 15 of 60 posts (1 in 4), all soft.
- Meta personal attributes: no ad text addresses the viewer's circumstances. Before and after in ads is text only, labelled "Example item", with no outcome.
- Platform facts on P01, P08, P13, P21, P23, P26, P40, P46, P54 and P59 match research/platform-rules-uk.md and carry a "check the current rule" line.
- 30-day refund in ads matches sales-site/terms.html and both sales page versions.
- Pin links all point to blog pages that exist in sales-site/netlify-site/blog/ or to the `#free-cheat-sheet` anchor.

## For the owner (outside these files)

1. The product itself says "88 tested prompts" (product/dist/Well-Listed-Kit.html) while sales page version B says "94 prompts in 13 modules". Settle one number, and only keep "tested" if there is a written record of testing.
2. Before scheduling P28 and P31, open the gov.uk pages listed in their fact notes: all UK law points are NOT VERIFIED in the fact sheet.
3. If the launch date moves, recheck which Kit posts fall inside the 14-day window (calendar.csv) before any of them say "£12".
