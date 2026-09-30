# QC: sales pages, legal pages, cheat sheet, emails and marketplace listings

Reviewed 29 September 2026 against QUALITY-CHECKLIST.md, WRITING-RULES.md, BRAND-GUIDE.md and research/platform-rules-uk.md. Kit contents checked against product/source/ and product/templates/.

**Prompt recount:** the product was being revised during this review. The first count gave 94. A later recount after the product QC edits gave **92** (V4 TikTok Shop title removed as a duplicate of T6; C10 keyword stuffing check removed as a duplicate of K7). Every page now says 92: A 6, B 7, T 8, D 10, K 8, PH 8, R 8, M 12, V 7, C 10, W 8. Recount before launch with `grep -cE '^### [A-Z]{1,2}[0-9]+ ' launch-kit/product/source/*.md`. If the number changes again, update every file in the table below that mentions a count.

**Automatic check:** `check_content.py` gives 0 problems. The 11 warnings are all deliberate: the `theme-color` meta tag, and "sweater" and "color" used as examples of words to avoid.

**Build:** netlify-site/ has been rebuilt from the edited sources.

## Issues found and fixes made

| File | Problem | Fix made |
|---|---|---|
| version-a.html, version-b.html, cheat sheet, both email files, listings.md | Prompt count out of date. Pages said 94, emails and listings said 88, and the product now has 92 | All set to 92. Module 08 now 7 prompts and module 09 now 10, in the version A table and the version B cards |
| version-a.html, version-b.html, listings.md | Module 08 said it includes "TikTok Shop UK titles" and module 09 said it includes "keyword stuffing". Neither is true after the product edits | Module 08 now lists descriptions, claims check, run-sheet and "one listing into a week of videos" (A notes titles are in module 02). Keyword stuffing removed from 09 (still in module 04) |
| version-a.html, version-b.html, cheat sheet, welcome W2, listings.md | Said "6 category versions" of the brief, but the product now has one master brief plus category "extras" blocks. The cheat sheet also said "a brief for every category" | Now "master brief plus extra lines for 6 categories". The overclaim is gone |
| version-a.html, version-b.html, cheat sheet | Said "20 ready buyer replies". message-snippets.txt has 22 | Changed to 22 everywhere, and the emails and listings now give the same number |
| welcome W6, launch L1, listings.md (Gumroad and Payhip) | "88 tested prompts" and "tested AI prompts". There is no record of testing to back this up (CAP Code: need evidence before you publish) | "tested" removed everywhere |
| version-a.html, version-b.html | FAQ "Do I get updates? Yes..." read as a promise of ongoing updates | Now: free through the Gumroad library if we update, but "We cannot promise future updates, so please buy it for what is in it today." terms.html section 10 and listings.md say the same |
| version-a.html, version-b.html | Price box said "Instant download" but gave no immediate-access or cancellation wording (Consumer Contracts Regs 2013, digital content) | Added a line in the price box: buying asks for immediate access, which ends the 14-day cancellation right once the download starts, and the 30-day refund still applies |
| version-b.html | Price box left out the refund, so it did not match version A | Added "30-day no-questions refund" to the micro line |
| version-a.html, version-b.html | Hero said "Launch price (full price £19)" with no end date, and the price box gave the date but no time. The emails say 11:59pm UK time | Hero now "Launch price until [LAUNCH END DATE], then £19". Price box now "ends at 11:59pm UK time on [LAUNCH END DATE]". It is still a real date, with no countdown |
| version-a.html | Problem-section quotes in first person ("I never had...") looked like real customer quotes or testimonials | Added a label: "Typical complaints, reworded by us. These are not reviews or quotes from real people." |
| version-b.html | FAQ "that is where most people will use it": a claim we have no evidence for | Now "Yes, it is built for phones." |
| version-a.html, version-b.html, privacy.html, terms.html | Mobile: footer links are inline text, well under a 44px tap target | `footer p a` now inline-block with 10px vertical padding and min-height 44px |
| version-a.html, version-b.html | Mobile: the sticky bar button could squash or wrap on narrow phones | `.sticky .btn` set to `flex:0 0 auto; white-space:nowrap` |
| privacy.html | Mobile: the 3-column legal table could overflow at 320px | Table wrapped in `.table-scroll` (overflow-x:auto) |
| terms.html, privacy.html | Section 1 printed the name twice ("[LEGAL NAME], [LEGAL NAME AND ADDRESS]") | Now "run by [LEGAL NAME AND ADDRESS]" |
| terms.html | Section 3: "£12 for the first 14 days after launch" had no fixed date | Now "£12 until 11:59pm UK time on [LAUNCH END DATE]", plus "you pay the price shown at checkout" |
| terms.html | Section 4: consent was only implied ("By buying, you ask us..."). The law needs an express request and an acknowledgement, confirmed in writing | Reworded: the product page states it before payment, completing the purchase gives the request and acknowledgement, and the Gumroad receipt confirms it. Says the 30-day refund applies even after download. A hidden comment tells the owner to put the wording on Gumroad and to recheck that Gumroad is merchant of record (NOT VERIFIED) |
| terms.html | Section 9: the liability cap at the price paid did not carve out the CRA 2015 right to a remedy when digital content damages a device | Carve-out added |
| privacy.html | UK GDPR gaps: no cookies section, no statement on automated decisions, nothing on whether giving data is required, no record of consent, no reminder about the ICO fee | Added section 4 "Cookies" (no own cookies, Gumroad's own at checkout, consent before any non-essential cookie), the consent record, "you do not have to give us your email", "no automated decisions", and a template comment on the ICO fee and MailerLite embed cookies. Sections renumbered 1 to 8 |
| privacy.html | Gumroad's role was unclear | States that Gumroad, as merchant of record, is responsible for the payment data it collects |
| welcome-sequence.md | Setup notes gave a real-looking address "hello.welllisted@gmail.com" (misspelt, and could be registered by someone else) | Replaced with [BRAND_EMAIL], with a note to use a domain address if possible and never a personal one |
| welcome W1 preview | "the one reply that fixes most AI listings": an unbacked "most" claim | "two lines to paste when the AI makes things up" |
| welcome W3 | "Most 'not as described' disputes come from...": an invented statistic | "A 'not as described' dispute often starts with..." |
| welcome W4 | "Most platforms' terms forbid [scraping]": not verified | "Platform terms often do not allow them (check the current rules)" |
| welcome W5 | "Most people who send low offers..." | "Plenty of people..." |
| welcome W6, W7 | W6 left out the refund. W7's refund route did not match the sales pages | W6 adds the 30-day refund and 22 replies. W7 adds "within 30 days of buying" and [BRAND_EMAIL] |
| launch-emails.md | Deadline handling said "change it before bed" if the owner would be asleep. That ends the price before the 11:59pm promised everywhere, so the deadline would be untrue | Now: change it after 11:59pm, never before (next morning is fine). If it changes early by mistake, change it back and refund the difference |
| launch-emails.md | L3 subject "ends tonight at midnight" did not match the 11:59pm in the body | "ends tonight at 11:59pm" |
| launch-emails.md | L2 alternative subject "One listing, five platforms" did not match the prompt, which covers three apps | "One listing, three apps" |
| launch-emails.md | L1 "listing 10 items in one sitting" | "up to 10 items in one chat", which matches W2 in the kit |
| launch-emails.md | L1 and L3 refund lines gave no way to ask for a refund | Added "reply to your Gumroad receipt or email [BRAND_EMAIL]", "within 30 days of buying" |
| launch-emails.md | "7:30pm, when most sellers are sorting listings": a claim we have no evidence for | Now shown as a guess to test |
| launch-emails.md | L1 goes out on day 7, which spends half the launch window before the warmest audience hears about it | Added a note recommending day 1 or 2 (the body works on any day). The schedule is left for the owner to decide |
| launch-emails.md | L1 "saves an evening of packing" overstated | "one listing and one parcel instead of five" |
| listings.md | Facts line said "modules 01 to 10" and left out the A prompts in module 00 | Now modules 00 to 10, IDs A to W, with the recount command, 6 examples, 22 replies and 9 shot-list categories |
| listings.md | Two different price-change times: "morning of day 15" here, "11:59pm day 14" in the emails | Both now say: after 11:59pm UK time on [LAUNCH END DATE], never before. The launch line uses [LAUNCH END DATE] in place of a free-text date |
| listings.md | The Gumroad checklist assumed Gumroad supplies its own digital-content consent wording (not verified) | Added a "DELIVERY AND REFUND" paragraph with the immediate-access acknowledgement to the Gumroad and Payhip descriptions, plus a confirmation line in the receipt note. The checklist now says not to rely on a Gumroad tick box |
| listings.md | No updates line, and the refund line did not say how to ask | "UPDATES" paragraph added (not guaranteed). Refund now names [BRAND_EMAIL] or the receipt |
| listings.md | Receipt tip "save the prompt library to your home screen": you cannot reliably do this with a local HTML file on a phone | Now "keep it in a favourite folder in Files or Downloads" |
| listings.md | Receipt said "We read everything": a promise a small faceless operation may not keep | Removed |
| listings.md | "5-minute starter prompt" did not match the product's name for it | Now "the all-in-one prompt for your platform (Module 00, Quick start)" |
| cheat sheet | "£12 at launch, then £19": the PDF lives on after launch and would go out of date | "Full price £19 (£12 launch price for the first 14 days after launch only; the sales page always shows the current price)" |
| sales-site/README.md | Placeholder table and count note were out of date | [LAUNCH END DATE] now also listed for the hero and terms. Count note updated to 92 with the new per-module figures |

## Checked and fine (no change needed)

- **Two versions are genuinely different.** A is about accuracy ("AI listings that stick to your facts and sound like a normal person", Clarks boots eBay example, problem then example then inside). B is about time ("Clear the listing pile and the buyer messages without losing your evening", notes-app raincoat on Vinted with an "is this still available?" reply, how-it-works first, lead magnet before the price).
- **Example title lengths are correct:** the Clarks title is 72 characters as stated, and the cheat sheet F2 example is 67.
- **No income claims, fake reviews, invented sales numbers or implied affiliation.** "No reviews yet" is stated openly, and disclaimers are in every footer, the FAQ, the listings and the emails.
- **The guarantee is the same everywhere:** 30 days from purchase, full refund through Gumroad, no questions, on top of legal rights.
- **Platform facts on the pages match the research sheet** (eBay 80 characters secondary, Amazon 75 from 27 July 2026, Depop 5 hashtags and 8 photos, Vinted 20 photos), with "check the current rule" lines.
- **Placeholders are unchanged:** [GUMROAD_PRODUCT_LINK], [BRAND_EMAIL], [LEGAL NAME AND ADDRESS], [LEGAL NAME], [DATE], [EMAIL_FORM_ACTION_URL], [LAUNCH END DATE], [SALES_PAGE_URL], [CHEAT_SHEET_LINK], [CURRENT_PRICE], [FOOTER_ADDRESS].
- **No em or en dashes** (and no the em dash HTML code or the en dash HTML code) in any reviewed file. The HTML tags balance in all four pages.
- **Etsy and TikTok Shop are correctly not used as sales channels** (the Etsy AI prompt-bundle rule, and TikTok Shop UK not supporting digital downloads).

## Still for the owner (cannot be fixed in copy)

1. **[LEGAL NAME AND ADDRESS] is legally needed and can identify the owner.** Use a registered office or PO box service, and think about a limited company (ASSUMPTIONS.md point 12).
2. **Put the immediate-access wording in the live Gumroad description and receipt,** then check the real checkout on a phone.
3. **Check Gumroad's merchant of record status and its refund tools before launch** (NOT VERIFIED).
4. **Check the ICO data protection fee,** and whether the MailerLite embed sets cookies.
5. **Recount the prompts right before launch,** because the product was still being edited during this review.
