# Module 04: Keywords, tags and item specifics

Buyers do not only search. They tap filters: size, brand, colour, condition. If your fields are empty, you are missing from those results however good your title is.

This module covers eBay item specifics, Etsy's 13 tags, Depop's hashtags, Vinted's fields and Amazon's backend search terms. Module 12 has each platform's current limits and sources. Every prompt stays honest: only the item's own brand, no stuffing, no invented details.

## What counts as keyword stuffing

Stuffing is packing a listing with words that do not honestly describe the item, or repeating words to game search. It can breach platform rules (eBay, for example, has a search and browse manipulation policy) and it looks spammy to buyers.

| Stuffing (avoid) | Honest (fine) |
|---|---|
| "Not Zara, similar to Mango, like H&M" | The item's own brand only |
| "Dress dress midi dress summer dress" | "Midi dress" once, with real details |
| "Nike" on unbranded trainers | "White lace up trainers" |
| "Y2K 90s 80s vintage retro" on a 2022 top | "Y2K style" only if it honestly has that look |
| A hidden list of words at the end of a description | A short, useful description |

**Simple test:** if a buyer searched that word, found your item and was annoyed, it should not be there.

## UK words: say it the way UK buyers type it

Generic AI tools default to American words. Use the UK word in the title. Where both are searched, the other word can go once in tags, specifics or backend fields.

| US word | UK word |
|---|---|
| Sweater | Jumper |
| Pants | Trousers |
| Sneakers | Trainers |
| Purse | Handbag (a UK "purse" is a small wallet) |
| Vest | Waistcoat (a UK "vest" is an underwear top) |
| Zipper, cleats, stroller | Zip, football boots, pushchair |
| Diaper bag, comforter, flashlight | Changing bag, duvet, torch |

---

## The K prompts

### K1 eBay UK item specifics
**Use it when:** You are listing on eBay UK and want every relevant item specific filled in accurately.
**Paste this:**
```text
I am listing on eBay UK in the category [CATEGORY]. Below are the item specifics fields eBay shows me, and my Listing Brief. Fill in each field using ONLY facts from the brief.

Rules:
- UK English and UK sizes.
- If the brief does not give the answer, write [CHECK: ...] and say where to find it (care label, base, settings menu).
- Never guess brand, material, model, year or country of manufacture.
- Use the simple words buyers filter by ("Grey", not "dove grey heather").
- Keep each value short (under 65 characters; I will check the form).
- No other brand names, hype or keywords that do not describe the item.
- Output a two-column table: Item specific | Value.

eBay's item specific fields for my category:
[PASTE THE FIELD NAMES FROM THE EBAY FORM]

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like,** for the Next jumper:

> | Item specific | Value |
> |---|---|
> | Brand / Size / Colour | Next / 12 / Grey |
> | Neckline / Material | Crew Neck / Acrylic, Wool |
> | Country of manufacture | [CHECK: on the care label, or leave blank] |

**Check before you post:**
- Copy the field names straight from the eBay form, so the AI works with the fields your category really has.
- Leave a field blank rather than guess. A wrong specific can lead to a "not as described" case.

### K2 Etsy 13 tags
**Use it when:** You are listing on Etsy and want 13 honest, varied tags within the 20-character limit.
**Paste this:**
```text
Write 13 Etsy tags for the item in my Listing Brief below.

- Each tag 20 characters or fewer including spaces. Show the count for each.
- Multi-word phrases a UK buyer would type ("silver stacking ring", not just "ring").
- Cover different angles: what it is, material, style, colour, occasion or recipient (only if the brief supports it), personalisation if offered.
- Vary the wording. UK spellings (personalised, jewellery); a US spelling in one tag at most.

Rules:
- Use ONLY facts from my brief. No material, style or use the item does not have.
- No other brands, characters or celebrity names. No health or wellbeing words. No hype.
- "Vintage" only if the brief supports it and it meets Etsy's current rule.
- Output a numbered list, then all 13 on one comma-separated line.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like,** for a handmade hammered sterling silver stacking ring:

> silver stacking ring (20), hammered silver ring (20), sterling silver band (20), thin silver ring (16), minimalist ring (15), handmade silver ring (20), textured ring (13), dainty silver ring (18), everyday ring (13), 925 silver ring (15), simple stacking band (20), hand forged ring (16), womens silver ring (18)

**Check before you post:**
- "Hand forged" only if you forge it by hand. Every tag must be true.
- Fill in Etsy's attributes (colour, material, occasion) as well.

### K3 Depop hashtags
**Use it when:** You are listing on Depop and want up to 5 relevant hashtags.
**Paste this:**
```text
Suggest 5 Depop hashtags for the item in my Listing Brief below, plus 3 spares, each with a one-line reason.

Rules:
- Depop allows up to 5 and asks for relevant words, brands and tags only. I will check the current limit in the app.
- Each hashtag honestly describes the item: type, its own brand, colour, material, fit or a style it really has.
- Style or era tags (y2k, 90s, grunge, cottagecore) only if the brief supports them. If unsure, leave them out and tell me.
- No other brands, trend tags that do not fit, or price tags.
- Lower case, no spaces, UK spelling (e.g. #jumper).

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like,** for the brown suede Topshop jacket, 90s style:

> #suedejacket (what it is), #topshop (its own brand), #brownsuede (colour and material), #90sstyle (style, era not claimed), #croppedjacket (the fit). Spares: #buttonfront, #womensjacket, #suede

**Check before you post:**
- Swap hashtags rather than going over the limit.

### K4 Vinted fields and search words
**Use it when:** You are listing on Vinted and want every field filled in and the right search words in your title and description.
**Paste this:**
```text
I am listing on Vinted in the UK. Vinted uses structured fields, not free tags.

1. From my brief, give the value for each field: Category (the most specific path, e.g. Women > Clothing > Jumpers and sweaters > Jumpers), Brand, Size, Condition, Colour (a second colour only if clearly true), Material.
2. List 5 to 8 search words UK buyers would type for this item. Say which are already in my title or description, and where the missing ones could go naturally, once each.
3. Flag any word in my title or description that is not in the brief, or is another brand.

Rules: UK English and UK sizes. Use ONLY facts in my brief; missing facts become [CHECK: ...]. No repeated words or keyword lists. Category paths change, so tell me to pick the closest match I can see.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My current title and description (if written):
[PASTE HERE]
```
**What good output looks like,** for black Levi's 501 jeans, W30 L32:

> - **Fields:** Category: Jeans > Straight fit [CHECK: men's or women's, from the label]. Brand: Levi's. Size: W30 L32. Condition: Good. Colour: Black. Material: Cotton.
> - **Search words:** levis 501, black jeans, straight leg jeans (all in title). Faded black jeans: could go in the description as "faded to a washed charcoal".

**Check before you post:**
- Select the brand from Vinted's list where it exists, so brand filters find you.

### K5 Amazon UK backend search terms
**Use it when:** You are a brand owner or seller filling in the backend search terms field on Amazon UK. Skip this if you only sell second-hand.
**Paste this:**
```text
Write backend search terms for my Amazon UK product listing.

Rules:
- The field is commonly quoted as 250 bytes (not characters; accented letters use more). Stay under 240 bytes and show the count. I will check Seller Central.
- Words separated by spaces. No commas or punctuation. Lower case.
- No word already in my title, Item Highlights or bullets (below), and no repeats within the field.
- Include synonyms, UK and US variants (e.g. jumper sweater), common misspellings, and uses only if my brief supports them.
- No other brand names, ASINs, temporary words (new, sale), subjective words (best) or offensive terms.
- Use ONLY facts from my brief. No materials, uses or features the product does not have.

My title, Item Highlights and bullets:
[PASTE THEM HERE]

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like,** for the "Hartwell Home" linen napkins:

> serviettes dinner fabric reusable washable dining kitchen flax natural textured square hemmed table setting (106 bytes)
>
> Left out: "napkins", "linen", "sage" and "green" (in the title) and "tablecloth" (a different product).

**Check before you post:**
- Remove any term that would disappoint a buyer who searched it.

### K6 Buyer search phrase finder (from what you see)
**Use it when:** You want to know how buyers search for your item, using the suggestions the platform's own search bar shows you.
**Paste this:**
```text
I am selling [ITEM] on [PLATFORM] in the UK. Below are the suggestions the platform's search bar showed me, and titles of a few sold listings I looked up myself.

Using ONLY these and my Listing Brief:
1. Group the phrases: what it is, brand and model, size, colour and material, style, condition.
2. Say which phrases honestly describe MY item. Ignore the rest.
3. Say where each fitting phrase should go: title, fields, tags or hashtags, or description.
4. Point out any US words and give the UK version.

UK English. Do not invent search data or say how popular a phrase is. No other brands.

Search bar suggestions I saw:
[PASTE SUGGESTIONS]

Sold listing titles I looked up:
[PASTE TITLES]

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**Check before you post:**
- Copy suggestions and titles by hand. Do not use automated tools to collect data from platforms.

### K7 Keyword stuffing checker
**Use it when:** You want a quick check that your title, tags, hashtags or search terms are honest and will not look like spam, on any platform.
**Paste this:**
```text
Check my [PLATFORM] UK listing for keyword stuffing and misleading search words.

Look for:
1. Any brand, character or product name that is not the item's own (including "style", "like", "similar to", "not X", "dupe").
2. Words repeated more than needed, in the title or across title and backend fields.
3. Style, era or trend words the brief does not support (vintage, y2k, 90s, designer, luxury).
4. Condition or authenticity words the brief does not support (new, unworn, genuine, rare).
5. Tags, hashtags or specifics that describe other items, sizes or trends.
6. Keyword lists or deliberate misspellings hidden in the description.

For each problem: quote it, give the risk in one line, and an honest replacement from my brief (or "remove"). Then give a verdict: "Ready to post" or "Fix first". Accurate words buyers really search are fine: the aim is relevance, not fewer words.

UK English. Do not invent facts.

My listing (title, description, tags or hashtags, specifics):
[PASTE YOUR LISTING HERE]

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like,** for a Vinted listing of an unbranded floral midi dress, size 12:

> | Problem | Risk | Replacement |
> |---|---|---|
> | "Zara style" in title | Another brand's name to attract searches | Remove |
> | "vintage" | No era in the brief | Remove |
> | "dress" 4 times in the title | Stuffing | "Floral midi dress, size 12, button front" |
>
> **Verdict:** Fix first.

**Check before you post:**
- Remove another brand's name even if other sellers use it. It can breach platform and trademark rules.

