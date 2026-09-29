# Module 09: Rule checker

Run these just before you post. They catch what gets listings removed or items returned: a flaw lost between your notes and the description, a title that is too long, a "genuine" you cannot prove, an "eco-friendly" you cannot back up.

**This is not legal advice.** An AI tool can miss things or be wrong about a rule. For anything important, check the current rule in the platform's help pages, and for legal questions see gov.uk, Citizens Advice or a qualified adviser.

**How to use it:** run **C01** on every listing. Then the check for where you are posting: **C02** eBay UK, **C03** Vinted, **C04** Depop, **C05** Etsy, **C06** Amazon UK, **C07** TikTok Shop UK. Add **C08**, **C09** or **C10** if the listing mentions health, the environment, brands, authenticity or returns. Makers selling their own products: **C11** for safety text and label details. For keyword stuffing, use **K07** (Module 04).

The platform points in C02 to C07 are our summary, checked in September 2026. Better still, paste the rule text from the platform's help pages where the prompt says, so the AI checks against today's rule.

---

### C01 Accuracy check: listing against brief
**Use it when:** Every time, on every platform, before you post.
**Paste this:**
```text
Check my listing for accuracy against my Listing Brief. You are a careful proofreader, not a copywriter. Do not rewrite unless I ask.

Report, as a short list:
1. Added facts: anything in the listing NOT in the brief (a material, size, year, "original box", "never worn").
2. Changed facts: anything that differs from the brief.
3. Missing or softened flaws: every flaw in the brief must appear, worded no more mildly.
4. Missing essentials that are in the brief (measurements, what is included, postage).
5. Misleading wording, even if technically true ("like new" for an item with wear).
6. American spellings or US sizes.

Label each point Must fix, Should fix or Fine, then a verdict: "Ready to post" or "Fix first". UK English. If unsure, write [CHECK: ...].

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, description, specifics or tags, condition, price, postage):
[PASTE YOUR LISTING HERE]
```
**What good output looks like** for the Next jumper:

> 1. **Must fix:** listing says "100% wool". The brief says 60% acrylic, 40% wool.
> 2. **Must fix:** the bobbling under the arms is missing from the description.
> 3. **Should fix:** the brief has measurements; the listing has none.
>
> **Verdict: Fix first.**

**Check before you post:**
- Every Must fix is fixed, not just noted.

### C02 eBay UK pre-post check
**Use it when:** You are about to post on eBay UK.
**Paste this:**
```text
Check my eBay UK listing before I post. Report problems, do not rewrite.

I sell as a: [PRIVATE SELLER / BUSINESS SELLER]
eBay rule text I copied today (optional): [PASTE OR "NONE"]

Check (pasted rule text wins if different):
- Title 80 characters or fewer including spaces. Show the count.
- Plain words: no shouting capitals, "L@@K", hype or keyword lists.
- No other brand's name, and no "style", "inspired by" or "dupe" next to one. Nothing suggesting a replica.
- Specifics and condition match the brief; every flaw is described.
- Photos of the actual item, no added text, borders or watermarks.
- No contact details or dealing outside eBay.
- Business seller: nothing implying buyers have no rights.

Label issues Must fix, Should fix or Fine, then a verdict. UK English. If a rule may have changed, write [CHECK: eBay help pages].

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, specifics, condition, description, photos in a line each, price, postage, returns):
[PASTE YOUR LISTING HERE]
```
**What good output looks like** for Clarks black leather Chelsea boots, UK 6:

> 1. **Must fix:** title is 86 characters. Remove the "Womens Ladies" repeat: 74.
> 2. **Must fix:** "Dr Martens style" in the description. These are Clarks: remove it.

**Check before you post:**
- The title count is 80 or fewer in eBay's own box.

### C03 Vinted pre-post check
**Use it when:** You are about to post on Vinted.
**Paste this:**
```text
Check my Vinted listing before I post. Report problems, do not rewrite.

Selling my own things, or trading as a business? [OWN THINGS / BUSINESS]
Vinted rule text I copied today (optional): [PASTE OR "NONE"]

Check (pasted rule text wins if different):
- Brand field and title show the real brand only. Nothing suggesting a replica.
- Condition matches the brief; every flaw is described.
- Photos: my own, current condition, whole item first, labels on branded items, every defect. No stock, found-online or watermarked images, no collages.
- UK size (or clearly labelled), with measurements where useful.
- No contact details or paying or messaging outside Vinted.
- If BUSINESS: remind me Vinted says traders should use Vinted Pro, whose sellers must accept returns within 14 days of receipt.

Label issues Must fix, Should fix or Fine, then a verdict. UK English. If unsure, write [CHECK: Vinted help pages].

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, description, fields, photos in a line each, price):
[PASTE YOUR LISTING HERE]
```
**What good output looks like** for a cream Zara linen shirt, size S, faint mark on the left cuff:

> 1. **Must fix:** no photo of the cuff mark. Add one.
> 2. **Should fix:** condition "Very good", but there is a mark. "Good" fits the brief better.

**Check before you post:**
- If you buy items to resell, read Vinted's current guidance on Vinted Pro.

### C04 Depop pre-post check
**Use it when:** You are about to post on Depop.
**Paste this:**
```text
Check my Depop listing before I post. Report problems, do not rewrite.

Depop rule text I copied today (optional): [PASTE OR "NONE"]

Check (pasted rule text wins if different):
- The first line says clearly what the item is. Short, clear description with measurements and signs of wear.
- 5 hashtags or fewer, each relevant. Show the count. Flag unrelated brands or trend words.
- No other brand names, "dupe", "replica" or "inspired by [BRAND]".
- Every flaw in the brief described in plain words.
- Photos of the actual item, within the app's limit (8 when we checked).
- UK size or clearly labelled, with measurements.
- No contact details, social handles or paying outside Depop.

Label issues Must fix, Should fix or Fine, then a verdict. UK English. If unsure, write [CHECK: Depop help pages].

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (description with hashtags, fields, photos in a line each, price):
[PASTE YOUR LISTING HERE]
```
**What good output looks like** for Levi's 501 jeans, W30 L32, light fading on the knees:

> 1. **Must fix:** 8 hashtags (limit 5), and #wranglerstyle names another brand.
> 2. **Should fix:** the fading is only called "character". Say "light fading on both knees".

**Check before you post:**
- Wear is described in plain words, not dressed up.

### C05 Etsy pre-post check
**Use it when:** You are about to post a handmade, vintage or craft supply listing on Etsy.
**Paste this:**
```text
Check my Etsy listing before I post. Report problems, do not rewrite.

Who made it and how: [E.G. "I THROW AND GLAZE EACH ONE"]
Did I use AI in making the item, its design or the photos? [NO / YES, HOW]
Etsy rule text I copied today (optional): [PASTE OR "NONE"]

Check (pasted rule text wins if different):
- Title 140 characters or fewer, readable. Show the count.
- Up to 13 tags, each 20 characters or fewer. Count each. Flag repeats and tags that do not fit.
- Item type fits the brief. Vintage with no age: [CHECK: Etsy's vintage rule].
- AI used in the item, design or photos: the description says so (Creativity Standards).
- Hand words (handmade, hand-poured) match who made it.
- Photos show what the buyer receives; mockups must not mislead.
- No brands, characters or crests I have no right to use.
- Materials, eco and health claims backed by the brief. Returns wording keeps UK buyers' rights (see C10).

Label issues Must fix, Should fix or Fine, then a verdict. UK English. If unsure, write [CHECK: Etsy help pages].

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, tags, description, item type, photos in a line each, returns):
[PASTE YOUR LISTING HERE]
```
**What good output looks like** for a handmade speckled blue ceramic mug:

> 1. **Must fix:** "eco-friendly glaze" has no evidence in the brief. Remove, or state the specific fact.
> 2. **Should fix:** tag "handmade ceramic coffee mug" is 27 characters. Limit 20.

**Check before you post:**
- Any AI use is disclosed the way Etsy currently requires.
- Safety text on the listing matches your label (C11).
- Used AI only to help write the listing text? We found no Etsy rule on that, but check the current Creativity Standards.

### C06 Amazon UK pre-post check
**Use it when:** You are about to publish or update an Amazon UK product listing. Skip this if you only sell second-hand.
**Paste this:**
```text
Check my Amazon UK product listing before I publish. Report problems, do not rewrite.

Media product (books, music, video)? [YES / NO]
Seller Central rule text I copied today (optional): [PASTE OR "NONE"]

Check (pasted rule text wins if different):
- Title 75 characters or fewer including spaces for non-media (from 27 July 2026). Show the count. Media: [CHECK: current limit].
- Item Highlights 125 characters or fewer.
- Title: no ! $ ? _ { } ^ ¬ ¦ unless in the brand, no word more than twice (small words excepted).
- No promotional phrases, emoji, or refund and guarantee claims.
- Nothing claimed that is not in the brief (materials, sizes, compatibility, certifications).
- Search terms: no title words, competitor brands or irrelevant words. [CHECK: byte limit.]
- Main image: plain white background, product only.
- Flag any health, safety or eco claim for C08.

Label issues Must fix, Should fix or Fine, then a verdict. UK English. If unsure, write [CHECK: Seller Central help].

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, Item Highlights, bullets, description, search terms, images in a line each):
[PASTE YOUR LISTING HERE]
```
**What good output looks like** for an own-brand "Oakden Home" bamboo chopping board set of 3:

> 1. **Must fix:** title is 118 characters and "board" appears three times. Suggested: "Oakden Home Bamboo Chopping Board Set of 3, Small Medium Large" (62).
> 2. **Must fix:** "antibacterial" has no evidence in the brief. Remove.

**Check before you post:**
- The title is within the current limit shown in Seller Central.

### C07 TikTok Shop UK pre-post check
**Use it when:** You are about to publish a product on TikTok Shop UK, or a video that shows it. Skip this if you only sell second-hand on the resale apps.
**Paste this:**
```text
Check my TikTok Shop UK listing (and video script, if included) before I publish. Report problems, do not rewrite.

Seller Center rule text I copied today (optional): [PASTE OR "NONE"]

Check (pasted rule text wins if different):
- Title at least 15 characters, accurate. No promotions, seller name, web address, platform names or symbols.
- No claim anywhere that it cures, treats, prevents or relieves any condition. No weight loss claims or before and after images.
- Images: square, front of product first, colour, no text or watermarks beyond product branding.
- Realistic AI images or video labelled, and not changing how the product looks.
- Nothing claimed that is not in the brief. No fake urgency or invented reviews.
- The product is allowed: [CHECK: prohibited and restricted products lists].

Label issues Must fix, Should fix or Fine, then a verdict. UK English. If unsure, write [CHECK: Seller Center].

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My title, description, images in a line each, and any video script:
[PASTE YOUR LISTING HERE]
```
**What good output looks like** for an own-brand lavender and shea hand balm, 50 ml:

> 1. **Must fix:** "soothes eczema" and "helps you sleep" are health claims. Remove.
> 2. **Should fix:** "Hand Balm!! 20% OFF" has symbols and a promotion. Suggested: "Lavender and Shea Butter Hand Balm 50 ml" (40).

**Check before you post:**
- Cosmetics have their own UK safety rules. [CHECK: gov.uk guidance on selling cosmetics.]

### C08 Risky claims scan
**Use it when:** Your listing claims anything about health, safety, the environment, quality, origin or popularity, on any platform.
**Paste this:**
```text
Scan my listing for risky claims. For each: quote it, name the type, rate it Must fix or Should fix, and suggest an accurate alternative from my brief.

Platform: [PLATFORM]
Evidence I hold (certificate, test report, care label, receipt): [LIST OR "NONE"]

Types:
1. Health: cures, heals, relieves, soothes, detox, hypoallergenic, antibacterial, "safe for babies".
2. Environmental: eco-friendly, sustainable, biodegradable, plastic-free, natural, non-toxic. UK green claims must be clear, specific and backed by evidence.
3. Authenticity and origin: genuine, authentic, handmade (if not by me), vintage (no age), "made in [COUNTRY]", designer.
4. Quality and safety: waterproof, unbreakable, tested, certified, CE or UKCA, BPA-free.
5. Popularity and urgency: best seller, "only 1 left" (if untrue), selling fast.
6. Condition: like new, perfect, flawless, mint (if the brief lists wear).

If my evidence supports a claim, it can stay, worded specifically ("100% cotton, per care label", not "natural"). UK English. Do not invent evidence or approve a claim because it is common. Not legal advice.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing:
[PASTE YOUR LISTING HERE]
```
**What good output looks like** for second-hand Joules wellies, UK 5, small scuff on the left toe:

> | Claim | Type | Rating | Safer wording |
> |---|---|---|---|
> | "100% waterproof" | Quality | Must fix | "No leaks when I tested them in water" (only if you did), or remove |
> | "Like new" | Condition | Must fix | "Good used condition, small scuff on left toe" |

**Check before you post:**
- Every claim left in is one you could prove if asked.

### C09 Brands, authenticity and trademark wording
**Use it when:** Your item is branded, looks like a brand, or you are tempted to write "genuine", "authentic", "style", "inspired by" or "dupe".
**Paste this:**
```text
Check the brand and authenticity wording in my [PLATFORM] listing.

1. List every brand, designer, character, team or trademark name in it.
2. For each, say whether the brief shows the item is made or licensed by that brand. If not: Must fix.
3. Flag "style", "inspired by", "dupe", "replica", "1:1" or "same as [BRAND]". Counterfeits are illegal and banned on every major platform, and using another brand's name for searches is against most platforms' rules. Suggest describing the item by its own features.
4. "Genuine" or "authentic": if the brief gives proof (receipt, bought from the brand), state the proof plainly. If not, remove the word and rely on clear photos of labels.
5. Handmade items with a character, crest or logo: I may need the rights holder's permission [CHECK: the platform's intellectual property rules].

UK English. Never help a replica appear genuine. If the brief suggests it may be fake, tell me plainly not to list it as that brand. Not legal advice.

My Listing Brief (including how I know the brand):
[PASTE YOUR LISTING BRIEF HERE]

My listing:
[PASTE YOUR LISTING HERE]
```
**Check before you post:**
- Authenticity is shown with photos and plain facts, not adjectives.

### C10 UK consumer law wording check
**Use it when:** Your listing or shop has returns, refunds or guarantee wording, or you are not sure whether you are a private seller or a business.
**Paste this:**
```text
Check my returns, refunds and guarantee wording against UK consumer law basics. A practical check, not legal advice.

I sell as a: [PRIVATE SELLER CLEARING MY OWN THINGS / I BUY TO RESELL / I MAKE ITEMS TO SELL / NOT SURE]
Platform: [PLATFORM]
My wording:
[PASTE WORDING]

1. Status: buying to resell or making to sell means I am likely a trader, even on a personal account. If NOT SURE, list the factors looked at (buying to resell, how often, profit motive) and tell me to check gov.uk. Do not decide for me.
2. Trader: flag wording that limits buyers' rights ("no refunds", "sold as seen", "buyer pays return costs even if faulty"). Buyers from traders generally have goods of satisfactory quality, fit for purpose and as described; a short-term right to reject faulty goods, generally within 30 days; and for most online orders a 14-day right to cancel, with exceptions such as personalised items.
3. Private seller: the item must still be as described, "no returns" covers change of mind only, and platform protection can still apply.
4. Flag vague guarantees ("guaranteed quality").
5. Suggest fair, clear replacement wording for my status.

UK English. Never suggest wording that denies legal rights. Tell me to check gov.uk, Citizens Advice and the platform's help pages.
```
**What good output looks like** for a seller who buys at car boots to resell on eBay, with "Sold as seen. No returns, no refunds.":

> 1. **Status:** buying to resell suggests you are likely a trader.
> 2. **Must fix:** this tries to remove rights a trader cannot remove.
> 5. **Suggested:** "Returns accepted within 14 days of delivery. Please message me through eBay to start a return. This does not affect your statutory rights."

**Check before you post:**
- Your returns settings in the app match your wording.

### C11 Product safety and label details (makers)
**Use it when:** You make and sell your own products (candles, ceramics, jewellery, textiles, toys, cosmetics) and want the safety text and label details gathered before you list.
**Paste this:**
```text
I make and sell [PRODUCT] in the UK on [PLATFORM(S)]. Help me gather its safety and label details. A practical checklist, not legal advice.

Materials and components: [LIST]
Who it is for: [ADULTS / COULD APPEAL TO CHILDREN / MADE FOR CHILDREN]
Warnings and instructions from my suppliers (paste exactly): [TEXT OR "NONE"]
What my label or packaging says now: [TEXT OR "NO LABEL"]
My business name and address on the product or packaging? [YES / NO]
Product or batch reference: [REFERENCE OR "NONE"]
Post to Northern Ireland or the EU? [YES / NO]

Give me:
1. A "Safety information" block for my listing, using ONLY the supplier and label text above, word for word. Gaps become [CHECK: ...].
2. A label checklist: what my label already has, and what is missing, as questions.
3. Up to 6 questions to check on GOV.UK for this product type. If I post to Northern Ireland or the EU, include whether the EU General Product Safety Regulation (GPSR) applies to me.

Rules: UK English. State no law, standard or certification as fact. Never write "safe", "non-toxic", "child-safe", CE or UKCA unless my supplier text says so. If it could appeal to children but is not made for them, flag it.
```
**What good output looks like** for a soy wax candle with the fragrance supplier's warning text pasted and no label yet:

> 1. **Safety information:** "Never leave a burning candle unattended. Burn out of reach of children and pets." (from your supplier's text, unchanged) [CHECK: the allergen statement your fragrance supplier gives for this fragrance]
> 2. **Label:** no business name or address yet. No batch reference [CHECK: would one help you trace a batch?]
> 3. **To check on GOV.UK:** what labelling applies to scented candles? Does your supplier's safety data sheet say what must go on the label?

**Check before you post:**
- Keep supplier documents and your label wording on file for each product and batch.
- Rules differ by product and change. If unsure, check GOV.UK or ask your local Trading Standards service.

---

## Two more UK rules worth knowing

The private seller and trader table is in Module 07.

- **Green claims:** the Competition and Markets Authority's Green Claims Code says claims should be truthful and accurate, clear and unambiguous, not leave out important information, make fair comparisons, consider the full life cycle, and be substantiated.
- **Fake or incentivised reviews** are against platform rules and, for businesses, banned under the Digital Markets, Competition and Consumers Act 2024.

**Tax is separate:** platforms report some sellers' sales to HMRC. That is not the same as being a trader under consumer law, and it does not by itself mean you owe tax. Check gov.uk if unsure.
