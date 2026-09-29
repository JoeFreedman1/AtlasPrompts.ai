# Module 10: Batch workflow

Listing ten items one at a time, starting a new chat for each, is slow. This module sets up one chat session that knows your shop, feeds it a stack of items, and gets back tidy listings you can copy straight in or paste into a spreadsheet for a bulk upload or cross-listing tool.

The order we suggest:

1. **W1** Write your shop style instruction once and save it in your phone's notes.
2. **W3** Turn rough notes for the whole pile into Listing Briefs in one go.
3. **W2** Start a batch session with your style instruction, then feed it up to 10 briefs.
4. **W4** Get the batch back as a table or CSV. **W5** Check the whole batch.
5. **W6 to W8** Plan the week, cross-list, and refresh quiet listings.

Free AI chats can lose track in very long sessions. If answers start drifting (American spelling, invented details, forgotten rules), start a fresh chat and paste your style instruction again. Batches of 5 to 10 items work best.

---

### W1 Build your reusable "shop style" instruction
**Use it when:** You are fed up of re-explaining your shop to the AI. Do this once, save the result, and paste it at the start of every session.
**Paste this:**
```text
Write me a short, reusable "shop style instruction" to paste at the start of any AI chat before I list items. UK English, no more than 12 numbered lines, starting "You are my listing assistant for a UK shop."

My answers:
- Platforms: [E.G. VINTED AND EBAY UK]
- What I mostly sell: [E.G. WOMEN'S CLOTHING, SIZES 8 TO 18]
- Private seller or business: [PRIVATE / BUSINESS]
- Tone: [E.G. FRIENDLY AND PLAIN, NO EMOJI]
- Condition words I use: [E.G. NEW WITH TAGS / VERY GOOD / GOOD / SATISFACTORY]
- How I measure: [E.G. PIT TO PIT AND LENGTH IN CM, LAID FLAT]
- Postage line: [E.G. "POSTED WITHIN 2 WORKING DAYS"; ADD SMOKE-FREE OR PET-FREE ONLY IF TRUE]
- Words I never want: [E.G. "STUNNING", "RARE" UNLESS IT IS]

It must include these fixed rules: UK English, UK sizes and £. Only facts from each Listing Brief; never invent brand, size, material, measurements, age, condition or contents. Missing facts become [CHECK: what is missing]. eBay UK titles 80 characters or fewer. State flaws clearly. No hype, keyword stuffing, misleading or health claims, fake urgency, other platform names, or payment outside the platform.
```
**What good output looks like:**

For a private seller on Vinted and eBay UK:

> You are my listing assistant for a UK shop.
> 1. I am a private seller on Vinted and eBay UK, mainly women's clothing, UK sizes 8 to 18.
> 2. Use UK English, UK sizes and £. Only use facts from the Listing Brief I give you; write [CHECK: what is missing] for gaps.
> 3. eBay UK titles: 80 characters or fewer. Vinted titles: short and plain.
> ...

**Check before you post:**
- Only include "smoke-free" or "pet-free" if it is true for every item.
- Business sellers: any returns wording must respect buyers' legal rights (Module 07).

### W2 Start a batch session (list up to 10 items in one chat)
**Use it when:** You have a pile of items photographed and noted, and want to list them in one sitting.
**Paste this:**
```text
[PASTE YOUR SHOP STYLE INSTRUCTION FROM W1]

We are going to list [NUMBER, UP TO 10] items in this chat. Platform for this batch: [EBAY UK / VINTED / DEPOP / ETSY].

How this works:
- I will paste one Listing Brief at a time, each starting "ITEM [NUMBER]".
- For each, reply with: Title, Description, Condition line, [ITEM SPECIFICS FOR EBAY / TAGS FOR ETSY / HASHTAGS FOR DEPOP / FIELDS FOR VINTED], and a list of [CHECK: ...] items.
- Same layout every time so I can copy quickly on my phone.
- Never carry facts from one item to another.
- No price unless the brief includes one.
- When I type "DONE", stop and wait.

Reply "Ready for ITEM 1" and nothing else.
```
Then paste each brief starting with ITEM 1, ITEM 2 and so on.

**What good output looks like:**

For ITEM 3 on eBay UK: "Joules women's quilted gilet, navy, size 12, zip front, 2 zip pockets, light pilling on inside collar, pre-owned, good":

> - **Title:** Joules Womens Navy Quilted Gilet Size 12 Full Zip Two Zip Pockets (65)
> - **Description:** Navy quilted gilet from Joules, women's size 12. Full zip front and two zip pockets. Pre-owned, good: light pilling on the inside collar (see photos). Measurements: pit to pit [CHECK: cm], length [CHECK: cm].
> - **Item specifics:** Brand: Joules. Size: 12. Colour: Blue [CHECK: eBay's colour list may use Blue for navy]. Type: Gilet. Department: Women. Outer shell material: [CHECK].

**Check before you post:**
- Scan each item for facts that leaked from an earlier item.

### W3 Turn messy notes for 10 items into Listing Briefs in one go
**Use it when:** You have quick notes for a stack of items and want proper briefs before you start W2.
**Paste this:**
```text
Turn my rough notes for [NUMBER] items into Listing Briefs. UK English.

Headings for each: Item number | What it is | Brand | Size | Measurements | Colour | Material | Condition and flaws | Included | Platform | Postage | Price floor

Rules:
- Only what is in my notes. Do not guess brand, size, material, age or value.
- Empty headings get [CHECK: ...] with what to find (e.g. [CHECK: care label for material]).
- Every flaw mentioned goes in "Condition and flaws".
- One short block per item. At the end, one combined "to find" list grouped by item, so I can check everything in one trip to the pile.

My notes:
[PASTE YOUR NOTES HERE]
```
**Check before you post:**
- Check the brand label on every item. Never list an item as a brand you cannot confirm.

### W4 Batch output as a table or CSV for bulk upload tools
**Use it when:** You have finished a batch and want it in a spreadsheet, or a CSV to import into a bulk listing or cross-listing tool.
**Paste this:**
```text
Put all the items we have written in this chat into one table.

Columns, in this order: [PASTE YOUR TOOL'S COLUMN HEADERS, OR USE: SKU, Title, Description, Condition, Brand, Size, Colour, Material, Category, Price, Quantity, Postage]

Rules:
- One row per item. Use the facts already agreed in this chat. Do not add or change anything.
- Missing facts: [CHECK]. Do not guess.
- For CSV: one code block, comma-separated, every cell in double quotes, line breaks inside cells replaced with a space, any double quote inside a cell doubled.
- Price column: numbers only, e.g. 12.50.
- Afterwards, list any rows that still contain [CHECK].

Output format: [TABLE / CSV]
```
**What good output looks like:**

```text
"SKU","Title","Description","Condition","Brand","Size","Colour","Material","Category","Price","Quantity","Postage"
"WL-014","Joules Womens Navy Quilted Gilet Size 12 Full Zip Two Zip Pockets","Navy quilted gilet from Joules, women's size 12. Full zip front and two zip pockets. Light pilling on the inside collar (see photos).","Pre-owned, good","Joules","12","Blue","[CHECK]","Coats and jackets","18.00","1","Royal Mail 2nd Class"
```

Rows with [CHECK]: WL-014 (Material).

**Check before you post:**
- Use your bulk tool's own template headers, open the CSV in a spreadsheet app before uploading, and test one or two rows first.

### W5 Batch accuracy check before you post
**Use it when:** You have a batch of listings ready and want a second pair of eyes to spot invented details, missing flaws and rule problems.
**Paste this:**
```text
Act as a careful UK listings checker. For each item, compare the listing with its brief and report:
1. Any detail NOT in the brief (possible invention).
2. Any flaw in the brief that is missing or softened.
3. Title length problems (eBay UK over 80 characters; other platforms [CHECK: current limit]).
4. Hype, keyword stuffing, misleading or health claims, fake urgency or other platform names.
5. American spellings or US sizes.

One short row per item: Item number | Problems found | Suggested fix. If fine, write "No problems found". Do not rewrite whole listings. UK English.

BRIEFS:
[PASTE BRIEFS]

LISTINGS:
[PASTE LISTINGS]
```
**What good output looks like:**

> | Item | Problems found | Suggested fix |
> |---|---|---|
> | 1 | Listing says "100% wool", brief says 60% acrylic, 40% wool | Use the brief's composition |
> | 2 | Scuffed toes in the brief, not in the listing | Add "Scuffs on the toes (see photos)" |
> | 3 | Title is 86 characters | Remove "Great" and "Look" |
> | 4 | No problems found | None |

**Check before you post:**
- The checker can miss things. Always read the flaws yourself, and go back to the item, not the AI, for the truth.

### W6 Weekly listing routine planner
**Use it when:** You want a realistic weekly plan that fits your evenings and weekends, so listing does not pile up.
**Paste this:**
```text
Help me plan a weekly listing routine. UK English. Realistic, not motivational.

- Time I have: [E.G. MONDAY AND WEDNESDAY EVENINGS 1 HOUR, SATURDAY MORNING 2 HOURS]
- Items I want to list each week: [NUMBER]
- Platforms: [LIST]
- What slows me down most: [E.G. PHOTOS, MEASURING, WRITING, POSTING]
- Drop-off options near me: [E.G. LOCKER, 24 HOURS]

Give me:
1. A day-by-day table: Day, Time, Task, Roughly how many items, Prompts to use (by ID, e.g. W2, W5, R prompts, M prompts).
2. Batch similar tasks: all photos in one go, all measuring in one go, all writing in one AI session.
3. A 10-minute daily check for messages and dispatch.
4. A weekly 20-minute review: what sold, what has had no interest, what to refresh or reprice.

Simple enough to follow on a phone. Do not promise any sales results.
```
**Check before you post:**
- The dispatch times in your listings match the plan you can actually keep. The stock tracker template makes the weekly review quick.

### W7 Repurpose one listing across platforms
**Use it when:** You have a good listing for one platform and want versions for others without starting again.
**Paste this:**
```text
[PASTE YOUR SHOP STYLE INSTRUCTION FROM W1, IF YOU HAVE ONE]

Here is the listing I wrote for [PLATFORM]:
[PASTE THE LISTING]

Rewrite it for: [TARGET PLATFORMS, E.G. VINTED, DEPOP]

Give each platform what it needs:
- eBay UK: title of 80 characters or fewer, description, item specifics.
- Vinted: short plain title, description with measurements and condition, field values.
- Depop: description starting with the key details, up to 5 relevant hashtags.
- Etsy (handmade, vintage of 20 years or more, or craft supplies only): readable title under 140 characters, description, 13 tags of 20 characters or fewer.

Rules:
- Same facts on every platform, from the brief only. Change format and tone, not facts.
- Missing facts become [CHECK: ...].
- No other platform named inside a listing. No hype, stuffing or misleading claims.
- Tell me if the item does not suit a platform instead of forcing it.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
For Amazon UK or TikTok Shop UK, use A5 or A6 in Module 00 with the same facts.

**What good output looks like:**

For a Levi's denim jacket, size M, mid-wash, small fade at the left cuff, care label dated 1996, first written for eBay UK:

> **Depop.** Vintage 1996 Levi's denim jacket, size M, mid-wash. Small fade at the left cuff (see photos). Pit to pit 56 cm, length 62 cm. #vintagelevis #denimjacket #90svintage #levisjacket #midwash

**Check before you post:**
- Cross-listing one item? Remove it everywhere else as soon as it sells, or you may sell it twice.

### W8 Refresh a batch of quiet listings
**Use it when:** Some listings have had little interest for a couple of weeks and you want to improve them honestly, without stuffing or fake price tricks.
**Paste this:**
```text
Below are [NUMBER] listings that have had little interest. For each I have added the Listing Brief, current title and description, days listed, and any views, likes or watchers.

[FOR EACH ITEM PASTE: BRIEF / TITLE / DESCRIPTION / DAYS LISTED / VIEWS, LIKES OR WATCHERS]

For each item suggest:
1. A clearer title using words buyers search, most important first, within the platform's limit.
2. The top 1 or 2 description fixes (missing measurements, unclear condition, missing brand or size).
3. Photo fixes (daylight, plain background, label or flaw close-up).
4. Whether a price check is worth doing, and what sold listings I should search for (describe the search, do not invent prices).

UK English. Only facts from the brief; [CHECK: ...] for gaps. No stuffing, no "rare" or "vintage" unless the brief supports it, no fake discounts. Do not promise it will sell.
```
**Check before you post:**
- A price drop must be real. Never raise a price just to "drop" it later, and check the platform's rules on relisting duplicates.

---

## Save these for every session

Keep these in one phone note: your shop style instruction (W1), the empty Listing Brief (templates/listing-brief-template.txt) and your bulk tool's column headers (for W4).
