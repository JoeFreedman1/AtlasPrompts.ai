# Module 04: Keywords, tags and item specifics

Buyers do not only type into a search bar. They tap filters: size, brand, colour, condition. If your listing's fields are empty, you are missing from those filtered results however good your title is.

This module covers the "behind the scenes" parts of a listing:

- **eBay item specifics:** the structured fields (brand, size, colour, style, and so on).
- **Etsy tags:** 13 short phrases that help your listing match searches.
- **Depop hashtags:** up to 5 relevant words at the end of your description.
- **Vinted fields and search words:** Vinted relies on its own fields rather than free tags.
- **Amazon UK backend search terms:** hidden keywords that buyers never see.

Every prompt uses your Listing Brief from Module 01, and every prompt tells the AI to stay honest: no brand names that are not the item's, no keyword stuffing, no invented details.

---

## Fields and limits at a glance

These are the facts at the time of writing (September 2026). Platforms change them, so **check the current rule in the platform's help pages**. Module 12 has the sources.

| Platform | Where keywords live | Limit or rule |
|---|---|---|
| eBay UK | Title, item specifics, category | Fill in every item specific that applies. Values are commonly quoted as limited to 65 characters each (check the form) |
| Etsy | Title, 13 tags, attributes, category | 13 tags, up to 20 characters each (spaces count) |
| Depop | Description, hashtags, category and attribute fields | Up to 5 hashtags. Depop says to use only relevant words, brands and tags |
| Vinted | Title, description, and the structured fields: category, brand, size, condition, colour, material | No free tag field. Fill in every field that applies |
| Amazon UK | Title, Item Highlights, bullets, backend search terms | Backend search terms commonly quoted as 250 bytes (bytes, not characters). If over, the whole field may be ignored. Do not repeat title words or use other brands |

---

## What counts as keyword stuffing

Keyword stuffing is packing a listing with search words that do not honestly describe the item, or repeating words to game search. It can breach platform rules (eBay, for example, has a search and browse manipulation policy) and it makes listings look spammy to real buyers.

| Stuffing (avoid) | Honest (fine) |
|---|---|
| "Not Zara, similar to Mango, like H&M" | The item's own brand only |
| "Dress dress midi dress summer dress" | "Midi dress" once, with other real details |
| Tagging "Nike" on unbranded trainers | "White trainers", "lace up trainers" |
| "Y2K 90s 80s vintage retro" on a 2022 top | "Y2K style" only if it honestly has that look |
| Hashtags for trends that do not fit (#cottagecore on a hoodie) | Hashtags that describe the item |
| Hidden lists of unrelated words at the end of a description | A short, useful description |

**Simple test:** if a buyer searched that word, found your item and was annoyed, it should not be there.

---

## UK search words: say it the way UK buyers type it

Generic AI tools often default to American words. UK buyers mostly search in UK English. Where a word is used in both countries, it can be worth including both in tags or specifics (not repeated in the title).

| US word | UK word buyers search |
|---|---|
| Sweater | Jumper |
| Pants | Trousers |
| Sneakers | Trainers |
| Purse | Handbag (a "purse" in the UK is a small wallet) |
| Vest | Waistcoat (a "vest" in the UK is an underwear top) |
| Suspenders | Braces |
| Zipper | Zip |
| Cleats | Football boots |
| Diaper bag | Changing bag |
| Stroller | Pushchair or pram |
| Comforter | Duvet |
| Flashlight | Torch |
| Faucet | Tap |
| Cell phone | Mobile phone |

---

## The K prompts

### K1 eBay UK item specifics
**Use it when:** you are listing on eBay UK and want every relevant item specific filled in accurately.
**Paste this:**
```text
I am listing on eBay UK in the category [CATEGORY, E.G. WOMEN'S JUMPERS AND CARDIGANS]. Below are the item specifics fields eBay shows me for this category, and my Listing Brief.

Fill in each item specific using ONLY facts from my Listing Brief.

Rules:
1. UK English and UK sizes.
2. If the brief does not give the answer, write [CHECK: ...] and tell me how to find it (e.g. "on the care label", "on the base", "in the settings menu").
3. Never guess brand, material, model, year or country of manufacture.
4. Use the simple, standard wording buyers filter by (e.g. "Grey", not "dove grey heather"; "Crew Neck", not "rounded neckline").
5. Keep each value short (under 65 characters, and I will check the form's limit).
6. Do not put other brand names, hype words or keywords that do not describe the item into any field.
7. Output as a two-column table: Item specific | Value.
8. After the table, list up to 3 extra item specifics that buyers in this category often filter by, if eBay allows custom ones, using only facts from the brief.

eBay's item specific fields for my category:
[PASTE THE FIELD NAMES FROM THE EBAY LISTING FORM]

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like:**

For a grey Next wool-blend jumper, size 12:

> | Item specific | Value |
> |---|---|
> | Brand | Next |
> | Size | 12 |
> | Size type | Regular |
> | Colour | Grey |
> | Type | Jumper |
> | Neckline | Crew Neck |
> | Sleeve length | Long Sleeve |
> | Material | Polyester, Acrylic, Wool Blend |
> | Pattern | Solid |
> | Style | [CHECK: e.g. Pullover, from the brief] |
> | Occasion | [CHECK: leave blank if unsure] |
> | Country of manufacture | [CHECK: on the care label, or leave blank] |
>
> **Extra ones buyers filter by:** Fit: Regular [CHECK], Features: Ribbed cuffs.

**Check before you post:**
- Copy the field names straight from the eBay form, so the AI works with the fields your category really has.
- Leave a field blank rather than guess. A wrong specific can lead to a "not as described" case.
- Brand must be the item's real brand. "Unbranded" is fine.

### K2 Etsy 13 tags
**Use it when:** you are listing on Etsy and want 13 honest, varied tags within the 20-character limit.
**Paste this:**
```text
Write 13 Etsy tags for the item in my Listing Brief below.

How to build them:
- Each tag up to 20 characters including spaces. Show the character count for each.
- Use multi-word phrases a UK buyer would actually type (e.g. "silver stacking ring" not just "ring").
- Cover different angles: what it is, material, style, colour, occasion or recipient (only if the brief supports it), and personalisation if offered.
- Do not repeat the exact title phrase in every tag. Vary the wording.
- Include UK spellings (personalised, jewellery, colour). If a US spelling is commonly searched too, you may use it in one tag at most.

Rules:
1. Use ONLY facts from my brief. Do not tag a material, style or use the item does not have.
2. No other brand names, trademarked characters or celebrity names.
3. No health or wellbeing words (healing, calming, anxiety).
4. "Vintage" only if the brief supports it and meets Etsy's current vintage rules.
5. No hype words (best, perfect, amazing).
6. Output as a numbered list. Then show the 13 tags as one comma-separated line so I can paste them quickly.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like:**

For a handmade hammered sterling silver stacking ring:

> 1. silver stacking ring (20)
> 2. hammered silver ring (20)
> 3. sterling silver band (20)
> 4. thin silver ring (16)
> 5. minimalist ring (15)
> 6. handmade silver ring (20)
> 7. textured ring (13)
> 8. dainty silver ring (18)
> 9. everyday ring (13)
> 10. 925 silver ring (15)
> 11. simple stacking band (20)
> 12. hand forged ring (16)
> 13. womens silver ring (18)
>
> silver stacking ring, hammered silver ring, sterling silver band, thin silver ring, minimalist ring, handmade silver ring, textured ring, dainty silver ring, everyday ring, 925 silver ring, simple stacking band, hand forged ring, womens silver ring

**Check before you post:**
- Count tags that look close to 20 characters. Etsy will not accept a longer one.
- "Hand forged" only if you forge it by hand. Every tag must be true.
- Fill in Etsy's attributes (colour, material, occasion) as well. They also help your item show up.

### K3 Depop hashtags
**Use it when:** you are listing on Depop and want 5 relevant hashtags.
**Paste this:**
```text
Suggest 5 Depop hashtags for the item in my Listing Brief below, plus 3 spares.

Rules:
1. Depop allows up to 5 hashtags and asks for relevant words, brands and tags only. I will check the current limit in the app.
2. Each hashtag must honestly describe the item: its type, brand (only its own brand), colour, material, fit or a style the item really has.
3. Style or era tags (y2k, 90s, grunge, cottagecore, gorpcore) only if the item honestly fits them and my brief supports it. If you are not sure, leave them out and tell me.
4. No other brand names, no trend tags that do not fit, no hashtags about price or "fast selling".
5. Lower case, no spaces, UK spelling where it matters (e.g. #jumper).
6. For each, give a one-line reason so I can decide.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like:**

For a brown suede Topshop jacket, size 10, 90s style:

> 1. #suedejacket (what it is)
> 2. #topshop (the item's own brand)
> 3. #brownsuede (colour and material)
> 4. #90sstyle (honest style word, era not claimed)
> 5. #croppedjacket (the fit)
>
> Spares: #buttonfront, #womensjacket, #suede

**Check before you post:**
- Swap hashtags rather than add more than the limit.
- Brand hashtags must be the item's own brand, shown on the label in your photos.
- Fill in Depop's category, brand, size, colour and condition fields as well.

### K4 Vinted fields and search words
**Use it when:** you are listing on Vinted and want every field filled in and the right search words in your title and description.
**Paste this:**
```text
I am listing on Vinted in the UK. Vinted uses structured fields rather than free tags, so help me get the fields and wording right.

Step 1. From my Listing Brief, give me the value for each Vinted field: Category (suggest the most specific path, e.g. Women > Clothing > Jumpers and sweaters > Jumpers), Brand, Size, Condition, Colour (main colour, and a second colour only if clearly true), Material.
Step 2. List 5 to 8 search words or short phrases UK buyers would type for this item. Tell me which already appear in my title or description, and suggest where the missing ones could go naturally (once each).
Step 3. Flag any word in my current title or description that is not supported by the brief, or that is another brand.

Rules:
1. UK English and UK sizes.
2. Use ONLY facts in my brief. Write [CHECK: ...] if something is missing.
3. Do not suggest repeating words or adding lists of keywords to the description.
4. Category paths change in the app. Tell me to pick the closest match I can see.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My current title and description (if written):
[PASTE HERE]
```
**What good output looks like:**

For black Levi's 501 jeans, W30 L32:

> **Fields:** Category: Men > Clothing > Jeans > Straight fit jeans [CHECK: men's or women's, from the label]. Brand: Levi's. Size: W30 L32. Condition: Good. Colour: Black. Material: Cotton.
>
> **Search words:** levis 501 (in title), black jeans (in title), straight leg jeans (in title), button fly jeans (in description), w30 jeans (add "W30" to title, already there), faded black jeans (could go in the description: "faded to a washed charcoal").
>
> **Flags:** none.

**Check before you post:**
- Choose Vinted's category from the options you actually see. They do change.
- Match the condition field to your description (see Module 03's grading table).
- Brand must be selected from Vinted's list where it exists, so buyers who filter by brand find you.

### K5 Amazon UK backend search terms
**Use it when:** you are a brand or seller filling in the backend "search terms" field on Amazon UK.
**Paste this:**
```text
Write backend search terms for my Amazon UK product listing.

Rules:
1. The field is commonly quoted as 250 bytes (not characters). For plain letters and spaces, 1 character is 1 byte, but accented letters and some symbols use more. Stay under 240 bytes to be safe and show the count. I will check the current limit in Seller Central.
2. Separate words with spaces. No commas, no punctuation.
3. Do not repeat any word already in my title, Item Highlights or bullets (listed below).
4. Do not repeat words within the field. No plurals of words already used unless they are genuinely different searches.
5. Include: synonyms, UK and US variants (e.g. jumper sweater), common misspellings buyers really make, and uses or occasions only if my brief supports them.
6. Do NOT include: other brand names, ASINs, temporary words (new, sale, on offer), subjective words (best, amazing), or offensive terms.
7. Use ONLY facts from my Listing Brief. No uses or features the product does not have.
8. Lower case.

My title, Item Highlights and bullets:
[PASTE THEM HERE]

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like:**

For "Hartwell Home" linen napkins, set of 4, sage green:

> serviettes dinner fabric reusable washable dining kitchen flax natural textured square hemmed wedding christmas table setting
>
> (125 bytes)
>
> Not included: "napkins", "linen", "sage" and "green" (already in the title), and "tablecloth" (a different product).
>
> Note: "wedding" and "christmas" are uses. Keep them only if your product is suitable and your brief supports it.

**Check before you post:**
- Use a byte counter (search "byte counter" for a free one) if your terms include accented letters or symbols.
- Remove any term that would disappoint a buyer who searched it.
- Never add other brands, even as "compatible with" terms, unless your category rules and the facts allow it.

### K6 Buyer search phrase finder (from what you see)
**Use it when:** you want to know how buyers actually search for your item, using the suggestions the platform's own search bar shows you.
**Paste this:**
```text
I am selling [ITEM] on [PLATFORM] in the UK. I typed the start of a search into the platform's search bar and copied the suggestions it showed me. I also noted the titles of a few sold listings for similar items that I looked up myself.

Using ONLY the suggestions and titles below:
1. Group the search phrases into: what it is, brand and model, size, colour and material, style, condition.
2. Tell me which phrases honestly describe MY item (using my Listing Brief). Ignore any that do not fit.
3. Suggest where each fitting phrase should go: title, item specifics or fields, tags or hashtags, or description.
4. Point out any US spellings or words, and give the UK version.

Rules: UK English. Do not invent search data or say how popular a phrase is. Do not suggest words that are not true of my item. No other brands.

Search bar suggestions I saw:
[PASTE SUGGESTIONS]

Sold listing titles I looked up:
[PASTE TITLES]

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like:**

For a Nintendo Switch Lite on eBay UK:

> | Phrase | Fits my item? | Where it goes |
> |---|---|---|
> | nintendo switch lite grey | Yes | Title |
> | switch lite console | Yes | Title |
> | switch lite with case | No, no case included | Leave out |
> | switch lite boxed | Partly, box included but no inserts | Item specifics and description: "Boxed, no inserts" |
> | switch lite turquoise | No, mine is grey | Leave out |

**Check before you post:**
- Only copy suggestions and titles by hand from what you see. Do not use automated tools to collect data from platforms.
- Suggestions change over time. Repeat this for items you sell often.
- A search phrase only belongs in your listing if it is true of your item.

### K7 Keyword stuffing checker
**Use it when:** you want a quick check that your title, tags or hashtags are honest and will not look like spam.
**Paste this:**
```text
Check my [PLATFORM] UK listing for keyword stuffing and misleading search words.

Check:
1. Any brand, character or product name that is not the item's own (including "style", "like", "similar to", "not X", "dupe").
2. Words repeated more than needed in the title, or repeated across title and backend fields where the platform advises against it.
3. Style, era or trend words not supported by my Listing Brief (vintage, y2k, 90s, designer, luxury).
4. Condition or authenticity words not supported by the brief (new, unworn, genuine, authentic, rare, limited).
5. Tags, hashtags or item specifics that do not describe the item.
6. Hidden lists of words in the description.

For each problem: quote it, say why it is a risk in one line, and give an honest replacement using only facts from my brief (or say "remove").
Then give a short verdict: "Ready to post" or "Fix first".

UK English. Do not invent facts.

My listing (title, description, tags or hashtags, item specifics):
[PASTE LISTING]

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like:**

For a Vinted listing of an unbranded floral dress:

> | Problem | Why it is a risk | Replacement |
> |---|---|---|
> | "Zara style" in title | Another brand's name to attract searches. Misleading and can break platform rules | Remove |
> | "vintage" in description | Brief gives no era | Remove, or "floral midi dress" |
> | "#reformation" hashtag (in a cross-post to Depop) | Another brand | #floralmididress |
> | "dress" appears 4 times in the title | Stuffing, wastes space | "Floral midi dress, size 12, button front" |
>
> **Verdict:** Fix first.

**Check before you post:**
- Using another brand's name to attract buyers can breach platform rules and trademark rules. Remove it even if other sellers do it.
- Run this check on older listings too. They may have been written before you started using briefs.
- Honest listings with fewer words are better than long ones with wrong words.

### K8 UK and US search word pairs for my category
**Use it when:** you sell a category where UK and US words differ and want a reference list for your tags, specifics and backend fields.
**Paste this:**
```text
I sell second-hand [CATEGORY] in the UK on [PLATFORM(S)]. Make me a reference table of search words for this category.

Columns: UK word | US or other word buyers might also use | Notes (where UK and US meanings differ, and could confuse a buyer).

Rules:
1. Up to 20 rows, most useful first.
2. Flag any word that means something different in the UK (e.g. vest, pants, purse, jumper dress) so I do not mislead a UK buyer.
3. Suggest where each word should go: title (UK word only), tags, hashtags or backend fields (either), or nowhere.
4. UK English. Do not include brand names.
5. Do not claim how popular any word is. I will check the platform's own search suggestions.
```
**What good output looks like:**

For baby and toddler gear:

> | UK word | Also used | Notes | Where |
> |---|---|---|---|
> | Pushchair | Stroller | Common in UK searches too | Title: pushchair. Tags or specifics: stroller |
> | Pram | Baby carriage | "Pram" in the UK often means a lie-flat carrycot style | Only if it is a pram |
> | Changing bag | Diaper bag | "Diaper" is not a UK word | Title: changing bag |
> | Dummy | Pacifier | | Tags |
> | Nappy | Diaper | | Title: nappy |
> | Babygrow | Onesie, sleepsuit | Onesie in the UK can also mean an adult lounge suit | Title: babygrow or sleepsuit |

**Check before you post:**
- UK words go in the title. Alternatives go in fields or tags where the platform allows, once each.
- Never use a word that would make a UK buyer expect something different.
- Save the table in your notes app and reuse it for every listing in that category.

---

## Keywords checklist

- [ ] Every field, specific or attribute that applies is filled in
- [ ] Every word, tag and hashtag describes the item honestly
- [ ] Only the item's own brand, anywhere in the listing
- [ ] No repeated words to pad the title
- [ ] UK words in the title, alternatives only where they fit
- [ ] Within each platform's current limits (tags, hashtags, bytes)
- [ ] Nothing collected by scraping or automated tools

Next: Module 05 for photos, then Module 06 to price the item from sold listings you look up yourself.
