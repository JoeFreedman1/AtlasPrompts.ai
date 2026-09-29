# 09 Rule checker

Run these just before you post. They take a minute and catch the things that get listings removed, accounts warned or items returned: a flaw that went missing between your notes and the description, a title that is too long, a "genuine" you cannot prove, an "eco-friendly" you cannot back up.

**Important: this is not legal advice.** These prompts are a practical checklist. An AI tool can spot likely problems, but it can also miss things or be wrong about a rule. Platform rules change often. For anything important, check the current rule in the platform's help pages, and for legal questions see gov.uk, Citizens Advice or a qualified adviser.

## How to use this module

1. Write your listing (modules 02 to 04).
2. Run **C1** against your Listing Brief. This is the accuracy check and it matters on every platform.
3. Run the platform check for where you are posting (**C2 to C7**).
4. If your listing mentions brands, authenticity, health, the environment or returns, run **C8 to C11** as needed.

The platform facts built into these prompts were checked in September 2026. Where a prompt says "at the time of writing", that is your cue to check the platform's help pages. Even better: copy the relevant rule text from the help pages and paste it into the prompt where it says **[PASTE CURRENT RULE TEXT]**. The AI will then check against today's rule rather than our summary.

## What the AI is told to do in every check

- Compare the listing with your Listing Brief and flag anything added, changed or missing.
- Flag, not fix silently. You see every issue and decide.
- Rate each issue: **Must fix** (likely to break a rule or mislead a buyer), **Should fix** (weak or risky) or **Fine**.
- Write [CHECK: ...] where it cannot tell.
- Use UK English and plain words.

---

### C1 Accuracy check: listing against brief
**Use it when:** every time, on every platform, before you post.
**Paste this:**
```text
Check my listing for accuracy against my Listing Brief. You are a careful proofreader, not a copywriter. Do not rewrite the listing unless I ask.

My Listing Brief (the facts):
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, description, item specifics or tags, condition, price and postage):
[PASTE YOUR LISTING HERE]

Check and report, as a short list:
1. Added facts: anything in the listing that is NOT in the brief (for example a material, a size, a year, "original box", "never worn"). These are invented until I confirm them.
2. Changed facts: anything that differs from the brief (size, colour, measurements, condition, what is included, price, postage).
3. Missing flaws: every flaw in the brief must appear in the listing, worded no more mildly than in the brief. List any that are missing or softened.
4. Missing essentials: anything a buyer would need that is in the brief but not the listing (measurements, what is included, postage).
5. Misleading wording: anything that could give a false impression, even if technically true (for example "like new" for an item with wear in the brief).
6. UK English: any American spellings or sizes (for example "color", "pants" for trousers, US sizes without the UK size).

Label each point Must fix, Should fix or Fine. Finish with a one-line verdict: "Ready to post" or "Fix first".

Rules: UK English. Only compare what I have pasted. If you are unsure, write [CHECK: ...]. Do not add new selling points.
```
**What good output looks like:**
> **Item:** grey Next wool-blend jumper, size 12, small bobbling under arms.
>
> 1. **Must fix:** listing says "100% wool". The brief says "wool blend". [CHECK: care label]
> 2. **Fine:** size, colour and price match.
> 3. **Must fix:** the bobbling under the arms is missing from the description.
> 4. **Should fix:** the brief has pit to pit 50 cm and length 62 cm, the listing has no measurements.
> 5. **Must fix:** "excellent condition" does not fit an item with bobbling. Suggest "good used condition" to match the brief.
> 6. **Fine:** UK spellings throughout.
>
> **Verdict: Fix first.**

**Check before you post:**
- Every Must fix is fixed, not just noted.
- Any "added fact" you keep is one you have checked on the item itself.

---

### C2 eBay UK pre-post check
**Use it when:** you are about to post on eBay UK.
**Paste this:**
```text
Check my eBay UK listing before I post. Report problems, do not rewrite unless I ask.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, item specifics, condition, description, photos described in a line each, price, postage, returns):
[PASTE YOUR LISTING HERE]

I sell as a: [PRIVATE SELLER / BUSINESS SELLER]

Current rule text I copied from eBay's help pages today (optional but best):
[PASTE CURRENT RULE TEXT OR "NONE"]

Check against these points (our summary at the time of writing, September 2026; where my pasted rule text differs, follow the pasted text):
- Title is 80 characters or fewer, including spaces. Count it and show the count.
- Title is plain words that describe the item: no ALL CAPS shouting, no "L@@K", no hype, no unrelated brand names, no keyword lists.
- No brand comparisons or lookalike wording ("style", "like", "inspired by", "dupe") next to a brand the item is not made by. eBay's rules say "dupe" with a brand name is not allowed and comparisons with other products are not allowed.
- Nothing suggests counterfeit, replica or fake items.
- Item specifics match the brief and are not stuffed with extra keywords.
- Condition chosen matches the brief, and the description describes every flaw.
- Photos: of the actual item, no stock photos for used items, no added text, borders or watermarks.
- No request to pay, message or buy outside eBay, and no contact details (email, phone, social handles, websites).
- Returns wording: if I am a business seller, it must not say or imply buyers have no rights (for example "no returns, no refunds under any circumstances").

Output: a numbered list of issues labelled Must fix, Should fix or Fine, then the title character count, then a one-line verdict.

Rules: UK English. Only judge what I pasted. If a rule is unclear or may have changed, write [CHECK: eBay help pages] rather than stating it as fact. This is a checklist, not legal advice.
```
**What good output looks like:**
> **Item:** Clarks black leather Chelsea boots, UK 6.
>
> 1. **Must fix:** title is 86 characters. Suggested cut: remove "Womens Ladies" duplication. New count 74.
> 2. **Must fix:** description says "Dr Martens style". These are Clarks, so remove the other brand name.
> 3. **Should fix:** item specific "Colour" says "Black Brown Tan". The brief says black only.
> 4. **Fine:** heel scuff described and photographed.
> 5. **Fine:** no contact details or off-eBay wording.
>
> **Title count:** 86 (limit 80). **Verdict: Fix first.**

**Check before you post:**
- Title count is 80 or fewer after your edits.
- No other brand's name appears anywhere unless it is genuinely relevant and allowed (check the current rule).

---

### C3 Vinted pre-post check
**Use it when:** you are about to post on Vinted.
**Paste this:**
```text
Check my Vinted listing before I post. Report problems, do not rewrite unless I ask.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, description, category, brand, size, condition, colour, material, photos described in a line each, price):
[PASTE YOUR LISTING HERE]

Am I selling my own second-hand things, or trading as a business? [OWN THINGS / BUSINESS]

Current rule text I copied from Vinted's help pages or catalogue rules today (optional but best):
[PASTE CURRENT RULE TEXT OR "NONE"]

Check against these points (our summary at the time of writing, September 2026; where my pasted rule text differs, follow the pasted text):
- The brand field and title show the real brand. No other brand names used to attract searches.
- Nothing suggests replica, fake or counterfeit items.
- Condition chosen matches the brief, and every flaw is described.
- Photos: my own photos of this item in its current condition, whole item in the first photo, labels shown for branded items, every defect shown, no stock, watermarked or found-online images, no collages.
- Size is given in UK sizing (or clearly labelled if it is a European or US size), with measurements where useful.
- No request to pay or message outside Vinted, and no contact details.
- If I said BUSINESS: remind me that Vinted says traders should use Vinted Pro, and that Pro sellers must accept returns within 14 days of receipt. Tell me to check the current Vinted Pro terms.

Output: numbered issues labelled Must fix, Should fix or Fine, then a one-line verdict.

Rules: UK English. Only judge what I pasted. If unsure about a rule, write [CHECK: Vinted help pages]. This is a checklist, not legal advice.
```
**What good output looks like:**
> **Item:** cream Zara linen shirt, size S, faint mark on left cuff.
>
> 1. **Must fix:** photo list has no photo of the cuff mark. Add one.
> 2. **Should fix:** condition is "Very good" but there is a mark. "Good" matches the brief better.
> 3. **Should fix:** size says "S" only. Add chest and length measurements from the brief.
> 4. **Fine:** brand field is Zara, no other brands mentioned.
>
> **Verdict: Fix first.**

**Check before you post:**
- The flaw photo is in the set.
- If you buy items to resell, you have read Vinted's current guidance on Vinted Pro.

---

### C4 Depop pre-post check
**Use it when:** you are about to post on Depop.
**Paste this:**
```text
Check my Depop listing before I post. Report problems, do not rewrite unless I ask.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (description including any hashtags, category, brand, size, condition, colour, photos described in a line each, price, postage):
[PASTE YOUR LISTING HERE]

Current rule text I copied from Depop's help pages today (optional but best):
[PASTE CURRENT RULE TEXT OR "NONE"]

Check against these points (our summary at the time of writing, September 2026; where my pasted rule text differs, follow the pasted text):
- The first line clearly says what the item is. Depop advises short, clear descriptions with measurements and signs of wear.
- Hashtags: no more than 5, and each one relevant to this item (its brand, style or type). Flag unrelated brands or trend words used only to get views.
- No other brand names used to attract searches, no "dupe", "replica", "inspired by [BRAND]" or similar.
- Every flaw in the brief is described and photographed.
- Photos: of the actual item, up to the app's current limit (8 at the time of writing).
- Size in UK sizing or clearly labelled, with measurements.
- No request to pay or message outside Depop, and no contact details or social handles.

Output: numbered issues labelled Must fix, Should fix or Fine, a count of hashtags, then a one-line verdict.

Rules: UK English. Only judge what I pasted. If unsure about a rule, write [CHECK: Depop help pages]. This is a checklist, not legal advice.
```
**What good output looks like:**
> **Item:** Levi's 501 jeans, W30 L32, mid blue, light fading on knees.
>
> 1. **Must fix:** 8 hashtags. Limit is 5. Suggested keep: #levis #501 #vintagedenim #straightleg #bluejeans.
> 2. **Must fix:** hashtag #wranglerstyle mentions another brand. Remove.
> 3. **Should fix:** fading on knees is in the brief but only mentioned as "character". Say "light fading on both knees".
> 4. **Fine:** waist and leg given in the brief and listing.
>
> **Hashtags:** 8 (limit 5). **Verdict: Fix first.**

**Check before you post:**
- 5 hashtags or fewer, all relevant.
- Wear is described in plain words, not dressed up.

---

### C5 Etsy pre-post check
**Use it when:** you are about to post a handmade, vintage or craft supply listing on Etsy.
**Paste this:**
```text
Check my Etsy listing before I post. Report problems, do not rewrite unless I ask.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, the 13 tags, description, category, what type of item it is: handmade, vintage or craft supply, materials, photos described in a line each, price, postage, returns):
[PASTE YOUR LISTING HERE]

Did I use AI in making the item or its design? [NO / YES, HOW]
Did I use AI to create or heavily edit the photos? [NO / YES, HOW]

Current rule text I copied from Etsy's help pages or policies today (optional but best):
[PASTE CURRENT RULE TEXT OR "NONE"]

Check against these points (our summary at the time of writing, September 2026; where my pasted rule text differs, follow the pasted text):
- Title is 140 characters or fewer. Count it. It reads as a clear description, not a list of repeated keywords.
- 13 tags or fewer, each 20 characters or fewer. Count each. Flag repeated tags or tags that do not describe this item.
- The item type (handmade, vintage, craft supply) fits the brief. Vintage on Etsy has an age requirement, so flag it as [CHECK: Etsy's current vintage rule] if the brief does not give an age.
- If AI was used for the item or design, remind me that Etsy's rules expect this to be disclosed, and to check the current Creativity Standards for how.
- Photos show what the buyer will actually receive. If photos are mockups or AI-assisted, flag that the listing must not mislead and to check Etsy's current rules.
- No other brand names, characters or logos I do not have the right to use (for example a football club crest or a cartoon character on a handmade item).
- Materials and any eco or health claims are backed by the brief.
- Returns wording does not remove UK buyers' legal rights (see C11).

Output: numbered issues labelled Must fix, Should fix or Fine, the title character count, tag count and any tag over 20 characters, then a one-line verdict.

Rules: UK English. Only judge what I pasted. If unsure about a rule, write [CHECK: Etsy help pages]. This is a checklist, not legal advice.
```
**What good output looks like:**
> **Item:** handmade blue ceramic mug, speckled glaze, 350 ml.
>
> 1. **Must fix:** description says "eco-friendly glaze". The brief gives no evidence. Remove, or state the specific fact (for example the glaze name) if you have it.
> 2. **Should fix:** tags "mug", "mugs" and "blue mug" overlap. Replace two with different searches a buyer might use, such as "speckled mug" and "stoneware cup". [CHECK: is it stoneware? The brief says ceramic.]
> 3. **Should fix:** tag "handmade ceramic coffee mug" is 27 characters. Limit is 20.
> 4. **Fine:** title 94 characters and reads clearly.
>
> **Title:** 94 of 140. **Tags:** 13, one over 20 characters. **Verdict: Fix first.**

**Check before you post:**
- Tag lengths are 20 characters or fewer.
- Any AI use is disclosed in the way Etsy currently requires.

---

### C6 Amazon UK pre-post check
**Use it when:** you are about to publish or update a product listing on Amazon UK.
**Paste this:**
```text
Check my Amazon UK product listing before I publish. Report problems, do not rewrite unless I ask.

My Listing Brief (product facts):
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, Item Highlights if used, bullet points, description, backend search terms, main image described in a line, other images):
[PASTE YOUR LISTING HERE]

Is this a media product (books, music, video)? [YES / NO]

Current rule text I copied from Seller Central today (optional but best):
[PASTE CURRENT RULE TEXT OR "NONE"]

Check against these points (our summary at the time of writing, September 2026; where my pasted rule text differs, follow the pasted text):
- Title length: from 27 July 2026, Amazon announced titles of 75 characters or fewer including spaces for all categories except media. Count it and show the count. (Media titles have a longer limit, [CHECK: current limit].)
- Item Highlights (if used): 125 characters or fewer.
- Title: no special characters such as ! $ ? _ { } ^ ¬ ¦ unless part of the brand name. The same word no more than twice (little words like "and", "for", "the" do not count).
- Title and bullets: no promotional phrases ("best seller", "free delivery", "sale", "guaranteed", "top quality"), no emojis, no refund or guarantee claims.
- Nothing claimed that is not in the brief (materials, sizes, compatibility, certifications).
- Backend search terms: do not repeat title words, no competitor brand names, not stuffed with irrelevant words. [CHECK: current byte limit in Seller Central.]
- Main image: my description suggests a plain white background, product only, no text, logos or extra items not included.
- Any health, safety or eco claim is flagged for C8.

Output: numbered issues labelled Must fix, Should fix or Fine, the title character count, repeated-word check, then a one-line verdict.

Rules: UK English. Only judge what I pasted. If unsure about a rule, write [CHECK: Seller Central help]. This is a checklist, not legal advice.
```
**What good output looks like:**
> **Item:** bamboo cutting board set of 3, own brand "Oakden Home".
>
> 1. **Must fix:** title is 118 characters. Limit is 75. Suggested: "Oakden Home Bamboo Chopping Board Set of 3, Small Medium Large" (62).
> 2. **Must fix:** "board" appears three times in the title. Maximum twice.
> 3. **Must fix:** bullet 2 says "antibacterial". The brief gives no test evidence. Remove (see C8).
> 4. **Must fix:** bullet 5 says "Best seller, free UK delivery". Promotional phrases are not allowed.
> 5. **Fine:** main image described as white background, boards only.
>
> **Title:** 118 of 75. **Verdict: Fix first.**

**Check before you post:**
- The title is at or under the current limit in Seller Central.
- No claim appears that you cannot evidence.

---

### C7 TikTok Shop UK pre-post check
**Use it when:** you are about to publish a product on TikTok Shop UK, or post a video that shows it.
**Paste this:**
```text
Check my TikTok Shop UK product listing (and video script, if I include it) before I publish. Report problems, do not rewrite unless I ask.

My Listing Brief (product facts):
[PASTE YOUR LISTING BRIEF HERE]

My product title, description, images described in a line each, and video script or captions (if any):
[PASTE YOUR LISTING HERE]

Current rule text I copied from TikTok Shop Seller University today (optional but best):
[PASTE CURRENT RULE TEXT OR "NONE"]

Check against these points (our summary at the time of writing, September 2026; where my pasted rule text differs, follow the pasted text):
- Title: at least 15 characters, accurate and concise (product type, material, key features, quantity, size). No promotions ("x% off"), no seller name or URL, no mention of TikTok or other platforms, no symbols or special characters.
- No claims anywhere (title, description, images or video) that the product cures, treats, prevents or relieves any disease or condition.
- No weight loss claims without diet and exercise, no before and after weight images, no "easy", "guaranteed" or "permanent" weight loss.
- Images: square, the main image shows the front of the product, colour only, no text or watermarks other than product branding.
- AI content: realistic AI images or video are labelled, and AI does not make the product look different from reality (texture, features, size).
- Nothing claimed that is not in the brief. No fake urgency ("only 2 left" when untrue), no invented reviews or customer numbers.
- The product itself is allowed. [CHECK: TikTok Shop UK's current prohibited and restricted products list.]

Output: numbered issues labelled Must fix, Should fix or Fine, the title character count, then a one-line verdict.

Rules: UK English. Only judge what I pasted. If unsure about a rule, write [CHECK: TikTok Shop Seller University]. This is a checklist, not legal advice.
```
**What good output looks like:**
> **Item:** lavender and shea hand balm, 50 ml, own brand.
>
> 1. **Must fix:** description says "soothes eczema". That is a claim to treat a condition. Remove.
> 2. **Must fix:** video caption says "helps you sleep". Remove, as it is a health claim the brief cannot support.
> 3. **Should fix:** title "Hand Balm!! 20% OFF" includes symbols and a promotion. Suggested: "Lavender and Shea Butter Hand Balm 50 ml" (40).
> 4. **Fine:** images described as square, product front, no added text.
>
> **Verdict: Fix first.**

**Check before you post:**
- No health or medical wording anywhere, including in the video voiceover.
- Cosmetics have their own UK safety rules. [CHECK: gov.uk guidance on selling cosmetics before listing.]

---

### C8 Risky claims scan
**Use it when:** your listing includes any claim about health, safety, the environment, quality, origin or popularity, on any platform.
**Paste this:**
```text
Scan my listing for risky claims. List them, explain the risk in one line each, and suggest a safer, accurate alternative that uses only facts from my brief.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing:
[PASTE YOUR LISTING HERE]

Platform: [PLATFORM]
Evidence I actually hold (for example a certificate, a test report, a care label, a receipt): [LIST OR "NONE"]

Look for these types of claim:
1. Health and medical: cures, treats, prevents, heals, relieves, soothes a condition, boosts immunity, detox, weight loss, "hypoallergenic", "antibacterial", "safe for babies".
2. Environmental: eco-friendly, sustainable, green, biodegradable, compostable, plastic-free, carbon neutral, "natural", "non-toxic". In the UK, environmental claims should be truthful, clear, specific and backed by evidence. Vague terms like "eco-friendly" are risky on their own.
3. Authenticity and origin: genuine, authentic, 100% real, original, handmade (if not made by the seller), vintage (without an age), "made in [COUNTRY]", "designer".
4. Quality and safety: waterproof, unbreakable, "tested", "certified", "CE marked", "UKCA", "BPA-free", "fire resistant".
5. Popularity and urgency: best seller, most popular, "everyone loves it", "only 1 left" (if untrue), "selling fast", "price going up".
6. Condition: "like new", "perfect", "flawless", "as new", "mint" (if the brief lists any wear).

For each claim found: quote it, name the type, rate it Must fix or Should fix, and suggest a replacement. If I have listed evidence that supports a claim, say it can stay, but tell me to keep the evidence and word it specifically (for example "Cotton, 100%, per care label" rather than "natural").

Rules: UK English. Do not invent evidence. Do not suggest a claim is fine just because it is common. This is a checklist, not legal advice.
```
**What good output looks like:**
> **Item:** second-hand Joules wellies, UK 5, small scuff on toe.
>
> | Claim | Type | Rating | Safer wording |
> |---|---|---|---|
> | "100% waterproof" | Quality | Must fix | "No leaks when I tested them in water" (only if you did), or remove |
> | "Eco-friendly natural rubber" | Environmental | Must fix | "Rubber" (per the brief), no eco claim |
> | "Genuine Joules" | Authenticity | Should fix | "Joules" with a photo of the brand label and inside stamp |
> | "Like new" | Condition | Must fix | "Good used condition, small scuff on left toe" |

**Check before you post:**
- Every claim left in is one you could prove if asked.
- Vague green words are replaced with specific facts or removed.

---

### C9 Brands, authenticity and trademark wording
**Use it when:** your item is branded, looks similar to a brand, or you are tempted to write "genuine", "authentic", "style", "inspired by" or "dupe".
**Paste this:**
```text
Check the brand and authenticity wording in my listing.

My Listing Brief (including how I know the brand, for example label, receipt, serial number, where I bought it):
[PASTE YOUR LISTING BRIEF HERE]

My listing:
[PASTE YOUR LISTING HERE]

Platform: [PLATFORM]

Do the following:
1. List every brand, designer, character, team or trademark name in the listing.
2. For each, say whether the brief shows the item is actually made by or officially licensed by that brand. If not, flag it Must fix.
3. Flag any "style", "inspired by", "look-alike", "dupe", "replica", "copy", "1:1", "mirror quality" or "same as [BRAND]" wording. Explain that selling counterfeit or replica items is not allowed on any major platform and is illegal, and that using another brand's name to attract searches is against most platforms' rules even for a non-branded item. Suggest describing the item by its own features instead (for example "black quilted crossbody bag with chain strap").
4. For "genuine" or "authentic": if the brief gives proof (receipt, authenticity card, serial number, bought from the brand), suggest stating the proof plainly instead ("bought from [SHOP] in [YEAR], receipt included"). If the brief gives no proof, suggest removing the word and relying on clear photos of labels and marks.
5. If the item is handmade and uses a character, team crest or logo, flag that I may need permission from the rights holder. [CHECK: the platform's intellectual property rules.]

Rules: UK English. Never help word a listing so that a replica or counterfeit item appears genuine. If the brief suggests the item may be fake, tell me plainly not to list it as that brand. This is a checklist, not legal advice.
```
**What good output looks like:**
> **Item:** unbranded tan leather-look tote bag.
>
> 1. **Brands found:** "Michael Kors style" in the title, #mulberry in the tags.
> 2. **Must fix:** the brief says unbranded. Neither brand made this bag.
> 3. **Must fix:** "style" next to a brand name, and another brand in the tags. Replace with the bag's own features: "Tan faux leather tote bag, zip top, two handles, 38 cm wide".
> 4. **Fine:** no "genuine" claims.

**Check before you post:**
- No brand name appears that did not make the item.
- Authenticity is shown with photos and plain facts, not adjectives.

---

### C10 Keyword stuffing check
**Use it when:** your title, tags or description feel crammed, or you have pasted in a list of search words.
**Paste this:**
```text
Check my listing for keyword stuffing and fix it with me.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My listing (title, tags, hashtags, item specifics or search terms, description):
[PASTE YOUR LISTING HERE]

Platform: [PLATFORM]

Flag any of these, quoting the words:
1. Words repeated in the title more than needed.
2. Brand names, character names or product types that do not describe this item.
3. Lists of search words at the end of the description ("keywords: dress gown frock party wedding summer...").
4. Tags or hashtags that describe other items, trends or sizes this item is not.
5. Misspellings added on purpose to catch searches.
6. Size, colour or condition words that contradict the brief (for example "S M L" for a single size).

Then suggest a cleaner version of the title and tags that uses only accurate words from the brief, within the platform's limits.
Platform limits I have checked today (optional): [PASTE OR "NONE"]

Rules: UK English. Only use facts from the brief. If you do not know the platform's current limit, write [CHECK: current limit]. Accurate words buyers actually search for are fine; the aim is relevance, not fewer words.
```
**What good output looks like:**
> **Item:** Boden navy spotty midi dress, size 12, eBay UK.
>
> 1. **Repeated:** "dress" appears three times in the title.
> 2. **Unrelated:** "Hobbs Whistles" in the title. Neither brand made it.
> 3. **Size list:** "10 12 14". The brief says size 12 only.
> 4. **Keyword block** at the end of the description: remove.
>
> **Cleaner title:** "Boden Navy Spot Midi Dress Size 12 Short Sleeve Cotton Jersey" [CHECK: is it cotton jersey? The brief says cotton only.] (61 characters)

**Check before you post:**
- Every word in the title is true for this item.
- No keyword block left in the description.

---

### C11 UK consumer law wording check
**Use it when:** your listing or shop has returns, refunds or guarantee wording, or you are not sure whether you are selling as a private seller or a business.
**Paste this:**
```text
Check the returns, refunds and guarantee wording in my listing or shop policy against UK consumer law basics. This is a practical check, not legal advice.

I sell as a: [PRIVATE SELLER CLEARING MY OWN THINGS / I BUY TO RESELL / I MAKE ITEMS TO SELL / NOT SURE]
Platform: [PLATFORM]
My returns, refunds or guarantee wording:
[PASTE WORDING]
My listing (for context):
[PASTE YOUR LISTING HERE]

Do the following:
1. Seller status: if I said "I buy to resell" or "I make items to sell", explain that I am likely to be treated as a trader under consumer law, even on a personal account, and should check gov.uk guidance. If "NOT SURE", list the kind of factors HMRC and consumer law look at (such as buying to resell, regularity, profit motive) and tell me to check gov.uk. Do not decide for me.
2. If I am a trader, flag any wording that tries to remove or limit buyers' legal rights, such as "no refunds", "no returns under any circumstances", "sold as seen" or "buyer pays all return costs even if faulty". Explain in plain words that UK buyers from traders generally have:
   - a right to goods that are of satisfactory quality, fit for purpose and as described;
   - a short-term right to reject faulty goods, generally within 30 days;
   - for most online orders, a right to cancel within 14 days of delivery, with some exceptions (for example personalised or made-to-order items).
3. If I am a private seller, explain that the item must still be as described, that a "no returns" policy covers change of mind only, and that platform buyer protection can still apply if the item is not as described, faulty or damaged.
4. Flag any guarantee or warranty I offer that is vague ("guaranteed quality"), and suggest a clear version or removing it.
5. Suggest fair, clear replacement wording for my status.

Rules: UK English. Never suggest wording that denies legal rights. Mark this clearly as not legal advice, and tell me to check gov.uk, Citizens Advice and the platform's current help pages.
```
**What good output looks like:**
> **Seller:** buys clothes at car boots to resell on eBay. Wording: "Sold as seen. No returns, no refunds."
>
> 1. **Status:** buying to resell suggests you are likely a trader in law. Check gov.uk guidance on selling online.
> 2. **Must fix:** "Sold as seen. No returns, no refunds" tries to remove rights that traders cannot remove. Buyers generally keep the right to cancel most online orders within 14 days and to reject faulty goods.
> 3. (Not applicable.)
> 4. (No guarantee offered.)
> 5. **Suggested wording:** "Returns accepted within 14 days of delivery. Please message me through eBay to start a return. This does not affect your statutory rights."
>
> Not legal advice. Check gov.uk, Citizens Advice and eBay's current help pages.

**Check before you post:**
- Your returns settings in the app match the wording in your listing.
- If you are a trader, your policy does not remove any legal right.

---

## UK consumer law basics (quick reference)

Plain summary for everyday selling. Not legal advice. Check gov.uk and Citizens Advice for the current position.

| Topic | Private seller | Trader |
|---|---|---|
| Item must match the description | Yes | Yes |
| Satisfactory quality and fit for purpose | Not in the same way, so describe faults honestly | Yes (Consumer Rights Act 2015) |
| Faulty item rejected for a refund | Only if not as described | Generally within 30 days |
| Change-of-mind cancellation online | No legal right | Generally 14 days from the day after delivery, some exceptions |
| Misleading claims | Can lead to platform action and "not as described" claims | Also against UK consumer protection law |
| Fake or incentivised reviews | Against platform rules | Against platform rules, and banned under the Digital Markets, Competition and Consumers Act 2024 |

**Environmental claims:** the Competition and Markets Authority's Green Claims Code says claims should be truthful and accurate, clear and unambiguous, not leave out important information, make fair comparisons, consider the full life cycle, and be substantiated. If you cannot back a green claim with evidence, leave it out.

**Tax is separate:** platforms now report some sellers' sales to HMRC. That report is not the same as being a trader under consumer law, and it does not by itself mean you owe tax. Check gov.uk if you are unsure.
