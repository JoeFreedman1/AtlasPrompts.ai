# Module 09: Rule checker

Run these just before you post. They take a minute and catch what gets listings removed or items returned: a flaw that went missing between your notes and the description, a title that is too long, a "genuine" you cannot prove, an "eco-friendly" you cannot back up.

**This is not legal advice.** An AI tool can spot likely problems but can also miss things or be wrong about a rule. For anything important, check the current rule in the platform's help pages, and for legal questions see gov.uk, Citizens Advice or a qualified adviser.

## How to use this module

1. Run **C1** on every listing. It checks the listing against your brief.
2. Run the check for where you are posting: **C2** eBay UK, **C3** Vinted, **C4** Depop, **C5** Etsy, **C6** Amazon UK, **C7** TikTok Shop UK.
3. If the listing mentions health, the environment, quality, brands, authenticity or returns, add **C8**, **C9** or **C11**. For keyword stuffing, use **K7** (Module 04).

The platform points built into C2 to C7 are our summary, checked in September 2026. Even better: copy the rule text from the platform's help pages and paste it where the prompt says. The AI will then check against today's rule.

Every check labels each issue **Must fix**, **Should fix** or **Fine**, flags rather than silently fixes, and ends with a verdict: "Ready to post" or "Fix first".

---

### C1 Accuracy check: listing against brief
**Use it when:** Every time, on every platform, before you post.
**Paste this:**
```text
Check my listing for accuracy against my Listing Brief. You are a careful proofreader, not a copywriter. Do not rewrite unless I ask.

Report, as a short list:
1. Added facts: anything in the listing NOT in the brief (a material, size, year, "original box", "never worn").
2. Changed facts: anything that differs from the brief (size, colour, measurements, condition, what is included, price, postage).
3. Missing or softened flaws: every flaw in the brief must appear, worded no more mildly.
4. Missing essentials that are in the brief but not the listing (measurements, what is included, postage).
5. Misleading wording, even if technically true ("like new" for an item with wear).
6. American spellings or US sizes.

Label each point Must fix, Should fix or Fine, then a verdict: "Ready to post" or "Fix first". UK English. If unsure, write [CHECK: ...].

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, description, specifics or tags, condition, price, postage):
[PASTE YOUR LISTING HERE]
```
**What good output looks like:**

For the Next jumper:

> 1. **Must fix:** listing says "100% wool". The brief says 60% acrylic, 40% wool.
> 2. **Must fix:** the bobbling under the arms is missing from the description.
> 3. **Should fix:** the brief has pit to pit 51 cm and length 63 cm; the listing has no measurements.
> 4. **Must fix:** "excellent condition" does not fit an item with bobbling. The brief says Good.
>
> **Verdict: Fix first.**

**Check before you post:**
- Every Must fix is fixed, not just noted.

### C2 eBay UK pre-post check
**Use it when:** You are about to post on eBay UK.
**Paste this:**
```text
Check my eBay UK listing before I post. Report problems, do not rewrite.

I sell as a: [PRIVATE SELLER / BUSINESS SELLER]
Rule text copied from eBay's help pages today (optional): [PASTE OR "NONE"]

Check (our September 2026 summary; pasted rule text wins if different):
- Title 80 characters or fewer including spaces. Show the count.
- Title is plain words: no shouting capitals, "L@@K", hype, unrelated brands or keyword lists.
- No "style", "like", "inspired by" or "dupe" next to a brand that did not make the item. Nothing suggesting a replica.
- Item specifics match the brief and are not stuffed.
- Condition matches the brief; every flaw is described.
- Photos described are of the actual item, with no added text, borders or watermarks.
- No contact details or requests to deal outside eBay.
- If I am a business seller: no wording that implies buyers have no rights.

Output: numbered issues labelled Must fix, Should fix or Fine, the title count, then a verdict. UK English. If a rule may have changed, write [CHECK: eBay help pages]. Not legal advice.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, specifics, condition, description, photos in a line each, price, postage, returns):
[PASTE YOUR LISTING HERE]
```
**What good output looks like:**

For Clarks black leather Chelsea boots, UK 6:

> 1. **Must fix:** title is 86 characters. Remove the "Womens Ladies" repeat: 74.
> 2. **Must fix:** description says "Dr Martens style". These are Clarks: remove the other brand.
> 3. **Should fix:** item specific Colour says "Black Brown Tan". The brief says black.
>
> **Title:** 86 (limit 80). **Verdict: Fix first.**

**Check before you post:**
- The title count is 80 or fewer after your edits, in eBay's own box.

### C3 Vinted pre-post check
**Use it when:** You are about to post on Vinted.
**Paste this:**
```text
Check my Vinted listing before I post. Report problems, do not rewrite.

Am I selling my own things, or trading as a business? [OWN THINGS / BUSINESS]
Rule text copied from Vinted's help pages or Catalogue Rules today (optional): [PASTE OR "NONE"]

Check (our September 2026 summary; pasted rule text wins if different):
- Brand field and title show the real brand only. Nothing suggesting a replica.
- Condition matches the brief; every flaw is described.
- Photos: my own, current condition, whole item first, labels for branded items, every defect shown. No stock, watermarked or found-online images, no collages.
- Size in UK sizing (or clearly labelled), with measurements where useful.
- No contact details or requests to pay or message outside Vinted.
- If BUSINESS: remind me that Vinted says traders should use Vinted Pro, whose sellers must accept returns within 14 days of receipt, and to check the current Pro terms.

Output: numbered issues labelled Must fix, Should fix or Fine, then a verdict. UK English. If unsure, write [CHECK: Vinted help pages]. Not legal advice.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, description, category, brand, size, condition, colour, material, photos in a line each, price):
[PASTE YOUR LISTING HERE]
```
**What good output looks like:**

For a cream Zara linen shirt, size S, faint mark on the left cuff:

> 1. **Must fix:** no photo of the cuff mark. Add one.
> 2. **Should fix:** condition "Very good", but there is a mark. "Good" fits the brief better.
> 3. **Should fix:** size says "S" only. Add chest and length measurements.
>
> **Verdict: Fix first.**

**Check before you post:**
- If you buy items to resell, read Vinted's current guidance on Vinted Pro.

### C4 Depop pre-post check
**Use it when:** You are about to post on Depop.
**Paste this:**
```text
Check my Depop listing before I post. Report problems, do not rewrite.

Rule text copied from Depop's help pages today (optional): [PASTE OR "NONE"]

Check (our September 2026 summary; pasted rule text wins if different):
- The first line clearly says what the item is. Depop advises short, clear descriptions with measurements and signs of wear.
- No more than 5 hashtags, each relevant to this item. Flag unrelated brands or trend words.
- No other brand names, "dupe", "replica" or "inspired by [BRAND]".
- Every flaw in the brief is described in plain words.
- Photos of the actual item, within the app's current limit (8 when we checked).
- Size in UK sizing or clearly labelled, with measurements.
- No contact details, social handles or requests to pay outside Depop.

Output: numbered issues labelled Must fix, Should fix or Fine, the hashtag count, then a verdict. UK English. If unsure, write [CHECK: Depop help pages]. Not legal advice.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (description with hashtags, category, brand, size, condition, photos in a line each, price):
[PASTE YOUR LISTING HERE]
```
**What good output looks like:**

For Levi's 501 jeans, W30 L32, light fading on the knees:

> 1. **Must fix:** 8 hashtags, limit 5. Keep #levis #501 #straightleg #bluejeans #denim.
> 2. **Must fix:** #wranglerstyle names another brand. Remove.
> 3. **Should fix:** the fading is only called "character". Say "light fading on both knees".
>
> **Hashtags:** 8 (limit 5). **Verdict: Fix first.**

**Check before you post:**
- Wear is described in plain words, not dressed up.

### C5 Etsy pre-post check
**Use it when:** You are about to post a handmade, vintage or craft supply listing on Etsy.
**Paste this:**
```text
Check my Etsy listing before I post. Report problems, do not rewrite.

Did I use AI in making the item, its design or the photos? [NO / YES, HOW]
Rule text copied from Etsy's help pages today (optional): [PASTE OR "NONE"]

Check (our September 2026 summary; pasted rule text wins if different):
- Title 140 characters or fewer, reads as a clear description. Show the count.
- 13 tags or fewer, each 20 characters or fewer. Count each. Flag repeats and tags that do not describe the item.
- The item type (handmade, vintage, craft supply) fits the brief. Vintage needs an age: flag [CHECK: Etsy's vintage rule] if the brief gives none.
- If AI was used, remind me Etsy expects it to be disclosed, and to check the current Creativity Standards.
- Photos show what the buyer will receive; mockups or AI-assisted images must not mislead.
- No brands, characters or logos I have no right to use (e.g. a football crest on a handmade item).
- Materials, eco and health claims are backed by the brief. Returns wording does not remove UK buyers' rights (see C11).

Output: numbered issues labelled Must fix, Should fix or Fine, the title count, tag count and any tag over 20, then a verdict. UK English. If unsure, write [CHECK: Etsy help pages]. Not legal advice.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, 13 tags, description, item type, materials, photos in a line each, price, postage, returns):
[PASTE YOUR LISTING HERE]
```
**What good output looks like:**

For a handmade speckled blue ceramic mug, 350 ml:

> 1. **Must fix:** "eco-friendly glaze" has no evidence in the brief. Remove, or state the specific fact.
> 2. **Should fix:** tag "handmade ceramic coffee mug" is 27 characters. Limit 20.
> 3. **Fine:** title 94 characters, reads clearly.
>
> **Tags:** 13, one over 20. **Verdict: Fix first.**

**Check before you post:**
- Any AI use is disclosed the way Etsy currently requires.

### C6 Amazon UK pre-post check
**Use it when:** You are about to publish or update an Amazon UK product listing. Skip this if you only sell second-hand.
**Paste this:**
```text
Check my Amazon UK product listing before I publish. Report problems, do not rewrite.

Media product (books, music, video)? [YES / NO]
Rule text copied from Seller Central today (optional): [PASTE OR "NONE"]

Check (our September 2026 summary; pasted rule text wins if different):
- Title 75 characters or fewer including spaces for non-media categories (from 27 July 2026). Show the count. Media: [CHECK: current limit].
- Item Highlights 125 characters or fewer.
- Title: no ! $ ? _ { } ^ ¬ ¦ unless in the brand name, and no word more than twice (small words excepted).
- No promotional phrases (best seller, free delivery, sale, guaranteed), emoji, or refund and guarantee claims.
- Nothing claimed that is not in the brief (materials, sizes, compatibility, certifications).
- Backend search terms: no title words, no competitor brands, no irrelevant words. [CHECK: current byte limit.]
- Main image as described: plain white background, product only, no text or extra items.
- Any health, safety or eco claim is flagged for C8.

Output: numbered issues labelled Must fix, Should fix or Fine, the title count, the repeated-word check, then a verdict. UK English. If unsure, write [CHECK: Seller Central help]. Not legal advice.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, Item Highlights, bullets, description, search terms, images in a line each):
[PASTE YOUR LISTING HERE]
```
**What good output looks like:**

For an own-brand "Oakden Home" bamboo chopping board set of 3:

> 1. **Must fix:** title is 118 characters, limit 75. Suggested: "Oakden Home Bamboo Chopping Board Set of 3, Small Medium Large" (62).
> 2. **Must fix:** "board" appears three times. Maximum twice.
> 3. **Must fix:** bullet 2 says "antibacterial" with no evidence in the brief. Remove (see C8).
>
> **Verdict: Fix first.**

**Check before you post:**
- The title is within the current limit shown in Seller Central.

### C7 TikTok Shop UK pre-post check
**Use it when:** You are about to publish a product on TikTok Shop UK, or post a video that shows it. Skip this if you only sell second-hand on the resale apps.
**Paste this:**
```text
Check my TikTok Shop UK listing (and video script, if included) before I publish. Report problems, do not rewrite.

Rule text copied from TikTok Shop Seller Center today (optional): [PASTE OR "NONE"]

Check (our September 2026 summary; pasted rule text wins if different):
- Title at least 15 characters, accurate and concise. No promotions, seller name, web address, platform names, symbols or special characters.
- No claim anywhere (title, description, images, video) that it cures, treats, prevents or relieves any disease or condition.
- No weight loss claims without diet and exercise, and no before and after weight images.
- Images: square, main image shows the front of the product, colour, no text or watermarks other than product branding.
- Realistic AI images or video are labelled and do not change how the product looks.
- Nothing claimed that is not in the brief. No fake urgency or invented reviews.
- The product itself is allowed: [CHECK: current prohibited and restricted products lists].

Output: numbered issues labelled Must fix, Should fix or Fine, the title count, then a verdict. UK English. If unsure, write [CHECK: Seller Center]. Not legal advice.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My title, description, images in a line each, and any video script or captions:
[PASTE YOUR LISTING HERE]
```
**What good output looks like:**

For an own-brand lavender and shea hand balm, 50 ml:

> 1. **Must fix:** "soothes eczema" is a claim to treat a condition. Remove.
> 2. **Must fix:** caption "helps you sleep" is a health claim. Remove.
> 3. **Should fix:** title "Hand Balm!! 20% OFF" has symbols and a promotion. Suggested: "Lavender and Shea Butter Hand Balm 50 ml" (40).
>
> **Verdict: Fix first.**

**Check before you post:**
- Cosmetics have their own UK safety rules. [CHECK: gov.uk guidance on selling cosmetics.]

### C8 Risky claims scan
**Use it when:** Your listing claims anything about health, safety, the environment, quality, origin or popularity, on any platform.
**Paste this:**
```text
Scan my listing for risky claims. For each: quote it, name the type, rate it Must fix or Should fix, and suggest a safer, accurate alternative using only facts from my brief.

Platform: [PLATFORM]
Evidence I actually hold (certificate, test report, care label, receipt): [LIST OR "NONE"]

Types to look for:
1. Health: cures, treats, heals, relieves, soothes, detox, weight loss, hypoallergenic, antibacterial, "safe for babies".
2. Environmental: eco-friendly, sustainable, biodegradable, plastic-free, carbon neutral, natural, non-toxic. UK green claims should be truthful, clear, specific and backed by evidence.
3. Authenticity and origin: genuine, authentic, original, handmade (if not by me), vintage (without an age), "made in [COUNTRY]", designer.
4. Quality and safety: waterproof, unbreakable, tested, certified, CE or UKCA marked, BPA-free, fire resistant.
5. Popularity and urgency: best seller, most popular, "only 1 left" (if untrue), selling fast.
6. Condition: like new, perfect, flawless, mint (if the brief lists wear).

If my evidence supports a claim, say it can stay, worded specifically ("100% cotton, per care label" rather than "natural"). UK English. Do not invent evidence or approve a claim because it is common. Not legal advice.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing:
[PASTE YOUR LISTING HERE]
```
**What good output looks like:**

For second-hand Joules wellies, UK 5, small scuff on the left toe:

> | Claim | Type | Rating | Safer wording |
> |---|---|---|---|
> | "100% waterproof" | Quality | Must fix | "No leaks when I tested them in water" (only if you did), or remove |
> | "Eco-friendly natural rubber" | Environmental | Must fix | "Rubber" (per the brief) |
> | "Like new" | Condition | Must fix | "Good used condition, small scuff on left toe" |

**Check before you post:**
- Every claim left in is one you could prove if asked.

### C9 Brands, authenticity and trademark wording
**Use it when:** Your item is branded, looks like a brand, or you are tempted to write "genuine", "authentic", "style", "inspired by" or "dupe".
**Paste this:**
```text
Check the brand and authenticity wording in my listing.

Platform: [PLATFORM]

1. List every brand, designer, character, team or trademark name in the listing.
2. For each, say whether the brief shows the item is made or officially licensed by that brand. If not: Must fix.
3. Flag "style", "inspired by", "look-alike", "dupe", "replica", "1:1" or "same as [BRAND]". Selling counterfeits is illegal and banned on every major platform, and using another brand's name to attract searches is against most platforms' rules. Suggest describing the item by its own features instead.
4. For "genuine" or "authentic": if the brief gives proof (receipt, authenticity card, bought from the brand), suggest stating the proof plainly. If not, suggest removing the word and relying on clear photos of labels.
5. Handmade items using a character, crest or logo: flag that I may need the rights holder's permission [CHECK: the platform's intellectual property rules].

UK English. Never help a replica appear genuine. If the brief suggests the item may be fake, tell me plainly not to list it as that brand. Not legal advice.

My Listing Brief (including how I know the brand):
[PASTE YOUR LISTING BRIEF HERE]

My listing:
[PASTE YOUR LISTING HERE]
```
**What good output looks like:**

For an unbranded tan faux leather tote bag:

> 1. **Brands found:** "Michael Kors style" in the title, #mulberry in the tags.
> 2. **Must fix:** the brief says unbranded. Neither brand made this bag.
> 3. **Replace with its own features:** "Tan faux leather tote bag, zip top, two handles, 38 cm wide".

**Check before you post:**
- Authenticity is shown with photos and plain facts, not adjectives.

### C11 UK consumer law wording check
**Use it when:** Your listing or shop has returns, refunds or guarantee wording, or you are not sure whether you are a private seller or a business.
**Paste this:**
```text
Check the returns, refunds and guarantee wording below against UK consumer law basics. A practical check, not legal advice.

I sell as a: [PRIVATE SELLER CLEARING MY OWN THINGS / I BUY TO RESELL / I MAKE ITEMS TO SELL / NOT SURE]
Platform: [PLATFORM]
My wording:
[PASTE WORDING]

1. Status: if I buy to resell or make items to sell, explain I am likely to be a trader under consumer law, even on a personal account. If NOT SURE, list the kind of factors looked at (buying to resell, how often, profit motive) and tell me to check gov.uk. Do not decide for me.
2. If I am a trader, flag wording that limits buyers' rights ("no refunds", "sold as seen", "buyer pays return costs even if faulty"). Explain that buyers from traders generally have: goods of satisfactory quality, fit for purpose and as described; a short-term right to reject faulty goods, generally within 30 days; and for most online orders a 14-day right to cancel, with exceptions (e.g. personalised items).
3. If I am a private seller: the item must still be as described, "no returns" covers change of mind only, and platform protection can still apply.
4. Flag vague guarantees ("guaranteed quality") and suggest a clear version or removal.
5. Suggest fair, clear replacement wording for my status.

UK English. Never suggest wording that denies legal rights. Tell me to check gov.uk, Citizens Advice and the platform's help pages.
```
**What good output looks like:**

For a seller who buys clothes at car boots to resell on eBay, with "Sold as seen. No returns, no refunds.":

> 1. **Status:** buying to resell suggests you are likely a trader. Check gov.uk guidance on selling online.
> 2. **Must fix:** "Sold as seen. No returns, no refunds" tries to remove rights a trader cannot remove.
> 5. **Suggested:** "Returns accepted within 14 days of delivery. Please message me through eBay to start a return. This does not affect your statutory rights."
>
> Not legal advice. Check gov.uk, Citizens Advice and eBay's current help pages.

**Check before you post:**
- Your returns settings in the app match your wording.

---

## Two more UK rules worth knowing

The private seller and trader table is in Module 07. Two extras:

- **Environmental claims:** the Competition and Markets Authority's Green Claims Code says claims should be truthful and accurate, clear and unambiguous, not leave out important information, make fair comparisons, consider the full life cycle, and be substantiated. If you cannot back a green claim, leave it out.
- **Fake or incentivised reviews** are against platform rules and, for businesses, banned under the Digital Markets, Competition and Consumers Act 2024.

**Tax is separate:** platforms report some sellers' sales to HMRC. That report is not the same as being a trader under consumer law, and it does not by itself mean you owe tax. Check gov.uk if you are unsure.
