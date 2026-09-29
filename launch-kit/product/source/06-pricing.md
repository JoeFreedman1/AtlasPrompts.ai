# 06 Pricing

Pricing is where most sellers guess. These prompts replace the guess with a quick, written reason you can stand behind.

We are honest about what they do: they help you set a sensible price from real evidence and do the sums properly. They cannot promise a sale, a profit or a particular price. Buyers decide that.

## The rule: you find the sold prices, the AI does the maths

AI chat tools do not know what your item sold for last week. If you ask "what is this worth?" with nothing else, you get a confident guess. Do not use it.

Instead:

1. **Look up sold listings yourself** on the platform you are selling on. On eBay, search for your item and turn on the "Sold items" filter. On other apps, look for items marked as sold, and remember that an asking price is not a sold price.
2. **Copy the details** of 5 to 10 comparable items into your notes app: title, sold price, postage, condition, and the date if you can see it. Matching items are better than lots of items.
3. **Paste them into the prompt** along with your Listing Brief.

Please do not use scraping tools, bots or browser add-ons that harvest listings automatically. Most platforms' terms forbid it, and you do not need it. Ten minutes of looking gives you better comps anyway, because you can see which items actually match yours.

## What makes a good comp

| Good comp | Weak comp |
|---|---|
| Same brand, model or style | "Similar" items from a different brand |
| Same or similar size | Different size (especially children's clothes and shoes) |
| Similar condition | New with tags against your well-worn item |
| Sold in the last few months | Sold two years ago |
| Sold price with postage noted | Asking price on an unsold listing |

---

### R1 Tidy my sold comps
**Use it when:** you have copied a messy pile of sold listings into your notes and want them in a clean table before pricing.
**Paste this:**
```text
I have copied some sold listings I found myself. Put them into a clean table so I can compare them with my item.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

Sold listings I copied (paste exactly as copied, messy is fine):
[PASTE YOUR SOLD LISTINGS HERE]

Make a table with these columns: Title (shortened), Sold price £, Postage £ (or "free" or [CHECK]), Total paid £, Condition, Size or model, Date sold (or [CHECK]), Match to my item (Good, Partial, Poor) and a one-line reason.

Rules:
- UK English, prices in pounds.
- Only use numbers that appear in what I pasted. Never invent a price, date or condition. If a detail is missing, write [CHECK].
- If something looks like an asking price rather than a sold price, flag it with [CHECK: sold or asking?].
- Put Good matches first.
- Below the table, list any comps I should drop and why, in one line each.
```
**What good output looks like:**
> **Item:** grey Next wool-blend jumper, size 12, small bobbling under arms.
>
> | Title | Sold £ | Postage £ | Total £ | Condition | Size | Date | Match |
> |---|---|---|---|---|---|---|---|
> | Next grey wool blend jumper | 12.00 | 2.99 | 14.99 | Good | 12 | 3 weeks ago | Good: same style and size |
> | Next grey crew neck knit | 10.50 | free | 10.50 | Good | 14 | [CHECK] | Partial: one size up |
> | Next wool mix jumper grey NWT | 22.00 | 3.20 | 25.20 | New with tags | 12 | 1 month ago | Poor: new, yours is worn |
>
> **Drop:** the NWT one. New with tags is not comparable with a worn jumper with bobbling.

*(Example figures only, invented for illustration.)*

**Check before you post:**
- Every price in the table is one you actually saw.
- You have at least three Good matches before moving on to R2.

---

### R2 Price from my sold comps
**Use it when:** you have your tidied comps and want a list price, a realistic range and a floor.
**Paste this:**
```text
Suggest a price for my item using only the sold listings I have found.

My Listing Brief (includes my price floor, the lowest I will accept):
[PASTE YOUR LISTING BRIEF HERE]

Platform: [PLATFORM]
Do buyers pay postage on top, or is it included in my price? [ON TOP / INCLUDED]
My sold comps (ideally the table from R1):
[PASTE COMPS HERE]

Give me:
1. The sold price range from the Good matches only (lowest to highest), and the middle (median) value.
2. How my item compares: better, same or worse condition than the Good matches, based only on my brief.
3. A suggested list price, a likely accepted price, and my floor from the brief. If my floor is above what the comps support, say so plainly.
4. Two or three lines of reasoning I could save in my notes.

Rules:
- UK English, pounds, show your working in simple sums.
- Use only the numbers I pasted. Do not use outside knowledge of prices.
- If I have fewer than three Good matches, say the evidence is thin and tell me what to search for.
- Do not promise the item will sell, or at what price. Say "based on these comps" not "this will sell for".
- Write ranges as "£10 to £14", never with a dash.
```
**What good output looks like:**
> **Item:** Clarks black leather Chelsea boots, UK 6, light toe creasing, small heel scuff. Floor £18.
>
> 1. **Good matches sold for** £20 to £32. Median £25.
> 2. **Your condition:** similar to most Good matches. The heel scuff puts you slightly below the two best ones.
> 3. **List at £28, expect offers around £22 to £25, floor £18.** Your floor sits comfortably below the range.
> 4. **Reasoning:** five Good matches, median £25. Listing a little above median leaves room for offers. Scuff disclosed, so no surprises for the buyer.
>
> Based on these comps only. Buyers set the final price.

**Check before you post:**
- The range comes only from your pasted comps.
- Your floor still covers fees and postage (use R7 to check).

---

### R3 Adjust for condition and extras
**Use it when:** your item is not quite like the comps (better or worse condition, missing box, extra accessories) and you want a fair adjustment.
**Paste this:**
```text
My item is different from the comps I found. Help me adjust the price fairly.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My closest sold comps:
[PASTE COMPS HERE]

How my item differs from these comps (in my own words):
[E.G. "NO ORIGINAL BOX, BUT COMES WITH A SPARE CHARGER" / "MINE HAS A SMALL CHIP, THEIRS DID NOT"]

Do the following:
1. List each difference and whether it pushes the price up, down or makes no clear difference, with a one-line reason a buyer would recognise.
2. If the comps themselves show the effect (for example boxed sold higher than unboxed), use those numbers and show the sum. If they do not, say "the comps do not show this" and give a cautious suggestion, clearly labelled as a judgement, not evidence.
3. Give an adjusted list price and floor.

Rules: UK English, pounds. Only use numbers I have pasted. Never guess a "collector's value". Do not tell me to describe the item as better than my brief says.
```
**What good output looks like:**
> **Item:** Nintendo Switch Lite, turquoise, working, light scratches on screen, no box, includes case.
>
> 1. **No box:** down. In your comps, boxed ones sold at £95 and £100, unboxed at £82 and £85. Roughly £12 to £15 less.
> 2. **Light screen scratches:** down. Your comps do not show this clearly. Judgement: buyers are cautious with screens, so price towards the lower end of unboxed.
> 3. **Includes case:** small plus, but the comps do not show a clear difference.
>
> **Adjusted list price £85, floor £75.**

*(Example figures only, invented for illustration.)*

**Check before you post:**
- Differences are in your description too (no box, scratches, extras).
- Judgement calls are labelled as judgement in your own notes.

---

### R4 Bundle pricing
**Use it when:** you want to sell several items together, or a buyer asks for a bundle price.
**Paste this:**
```text
Help me price a bundle.

Items in the bundle (one short Listing Brief or line each, with my individual list price and floor):
[PASTE ITEMS HERE]

Platform: [PLATFORM]
Postage for the bundle as one parcel: £[AMOUNT OR "NOT SURE"]
Postage if sent separately (total): £[AMOUNT OR "NOT SURE"]
Does the platform have its own bundle discount tool I have switched on? [YES, WITH % / NO / NOT SURE]

Give me:
1. The total of individual list prices and the total of floors.
2. The postage saving from sending one parcel (if I gave both figures).
3. A suggested bundle price and the lowest bundle price I should accept, keeping every item at or above its floor in total.
4. A one-line reason I can send the buyer, based on the postage saving and my time, without pressure.

Rules: UK English, pounds, show the sums. Use only my numbers. If postage is missing, write [CHECK: postage] and do the sum without it. Do not use pressure wording such as "today only" or "last chance".
```
**What good output looks like:**
> **Bundle:** three children's Frugi tops age 4 to 5 (£8, £8, £7 list; £6, £6, £5 floor).
>
> 1. **List total** £23. **Floor total** £17.
> 2. **Postage saving:** £3.20 as one parcel against £8.40 separately, so £5.20 saved.
> 3. **Suggested bundle price £19, accept down to £17.**
> 4. **Line to send:** "I can do all three for £19. They go in one parcel, so it saves on postage for both of us."

*(Example figures only, invented for illustration.)*

**Check before you post:**
- The bundle price is at or above the total of your floors.
- If the platform applies its own bundle discount on top, you have included it in your sums.

---

### R5 Offer strategy
**Use it when:** you want to decide in advance what offers to accept, counter or decline, so you are not deciding at 11pm with a lowballer waiting.
**Paste this:**
```text
Help me set an offer plan for this listing.

My Listing Brief (includes my floor):
[PASTE YOUR LISTING BRIEF HERE]

Platform: [PLATFORM]
My list price: £[AMOUNT]
My reasoning from comps (optional, e.g. from R2): [PASTE OR "NONE"]
Does the platform let me set automatic accept or decline levels? [YES / NO / NOT SURE]

Give me a simple plan:
1. Accept straight away at or above: £...
2. Counter-offer if between: £... and £..., with the counter price I should send.
3. Politely decline below: £...
4. If auto accept or decline is available, the levels I could set (and a reminder to check the settings in the app).
5. One short, polite line for each case that I could send.

Rules: UK English, pounds. Never go below my floor. Do not suggest fake scarcity or pressure ("someone else is interested", "ends tonight") unless I tell you it is true. Keep replies friendly and brief.
```
**What good output looks like:**
> **Item:** Le Creuset 20 cm casserole, list £65, floor £48.
>
> 1. **Accept** at £58 or more.
> 2. **Counter** offers from £48 to £57 at £56.
> 3. **Decline** below £48.
> 4. **Auto settings:** accept £58, decline under £45 (a little below your floor so you still see near misses). Check how your app's offer settings work.
> 5. **Lines:**
>    - Accept: "Thanks, happy to accept. It will be posted within [CHECK: dispatch time]."
>    - Counter: "Thanks for the offer. The lowest I can do is £56, as it is heavy to post."
>    - Decline: "Thanks, but that is too low for me. You are welcome to make another offer."

**Check before you post:**
- Every figure is at or above your floor.
- Any reason you give (like heavy postage) is true.

---

### R6 Planned price drop schedule
**Use it when:** an item has not sold and you want a calm plan for reducing it, rather than panic-dropping or leaving it forever.
**Paste this:**
```text
Make a price drop plan for an item that has not sold yet.

My Listing Brief (includes my floor):
[PASTE YOUR LISTING BRIEF HERE]

Platform: [PLATFORM]
Current price: £[AMOUNT]
Listed for: [NUMBER] days
Views, likes or watchers so far (if the app shows them): [NUMBERS OR "NOT SURE"]
My sold comps (optional): [PASTE OR "NONE"]

Give me:
1. First, a quick check of things other than price that could be holding it back (cover photo, title, missing measurements, postage cost). Base this only on my brief, and write [CHECK: ...] for anything you cannot see.
2. A drop plan with dates in weeks from today, the price at each step, and the point where I stop at my floor.
3. What to do if it still has not sold at the floor (bundle it, relist fresh with new photos, sell elsewhere, donate).

Rules: UK English, pounds. Never go below my floor. Keep drops simple (round numbers). Do not tell me any step will make it sell. If my platform lets me send offers to people who liked or watched the item, mention it as an option to check in the app, not as a guarantee.
```
**What good output looks like:**
> **Item:** cream Zara linen shirt, size S, listed 21 days at £14, 40 views, 2 likes, floor £8.
>
> 1. **Check first:** your brief has no chest measurement [CHECK: add pit to pit and length]. Linen creases, so check the cover photo is not crumpled.
> 2. **Plan:**
>    - Week 1: fix measurements and cover photo, keep at £14.
>    - Week 2: £12. Consider sending an offer to the two likers if the app allows it.
>    - Week 4: £10.
>    - Week 6: £8 (floor). Stop here.
> 3. **If still unsold:** bundle it with other size S linen, relist with fresh photos in spring, or donate.

**Check before you post:**
- The plan stops at your floor.
- You fix any listing problems before dropping the price.

---

### R7 Fee and postage maths
**Use it when:** you want to know what you actually keep after fees, postage and packaging, before you set a price or accept an offer.
**Paste this:**
```text
Work out what I keep from a sale. I will give you the current fees myself.

Platform: [PLATFORM]
Sale price: £[AMOUNT]
Postage the buyer pays: £[AMOUNT OR "NONE, INCLUDED IN PRICE"]
My actual postage cost: £[AMOUNT]
Packaging cost: £[AMOUNT OR "0"]
Fees I copied from the platform's current fee page today (paste exactly, e.g. percentage, fixed fee per order, whether it applies to postage too, payment processing):
[PASTE CURRENT FEE DETAILS HERE]
What I paid for the item (optional): £[AMOUNT OR "NOT SURE"]

Show me, as a simple table:
1. Money in (sale plus postage paid by buyer).
2. Each fee, with the sum shown.
3. Postage and packaging out.
4. What I keep.
5. If I gave a cost price: what is left after that cost.
Then tell me the lowest sale price at which I would still keep £[TARGET AMOUNT] after costs, using the same fees.

Rules:
- UK English, pounds, round to the nearest penny.
- Use ONLY the fee details I pasted. Do not use fees from your own knowledge, they may be out of date. If my fee details are unclear, write [CHECK: ...] and explain what is unclear.
- This is a sum, not advice. Do not call the result "profit" unless I gave a cost price, and do not promise any outcome.
- Remind me that fees and rules change, so I should check the platform's current fee page each time.
```
**What good output looks like:**
> **Item:** Tefal kettle. Sale £15, buyer pays £3.50 postage, actual postage £3.20, packaging £0.30. Fees pasted by the seller (invented for this example): 10% of total including postage, plus £0.30 per order.
>
> | Line | Sum | £ |
> |---|---|---|
> | Money in | 15.00 + 3.50 | 18.50 |
> | Percentage fee | 10% of 18.50 | 1.85 |
> | Fixed fee | | 0.30 |
> | Postage out | | 3.20 |
> | Packaging | | 0.30 |
> | **You keep** | 18.50 minus 5.65 | **12.85** |
>
> To keep at least £10 with these fees, the lowest sale price is about £11.84 [shown working: (10 + 0.30 + 3.20 + 0.30) divided by 0.9, minus 3.50].
> Fees and rules change: check the platform's current fee page before relying on this.

*(The fee figures above are invented to show the maths. They are not any platform's real fees.)*

**Check before you post:**
- You pasted today's fees from the platform's own help pages.
- You weighed the parcel and checked the real postage price.
- You noted whether you sell as a private seller or a business, as fees can differ (check the current fee page).

---

### R8 Is it worth listing on its own?
**Use it when:** you have a low-value item and are not sure whether to list it alone, bundle it, or let it go.
**Paste this:**
```text
Help me decide whether this item is worth listing on its own.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

Sold comps I found (optional): [PASTE OR "NONE"]
What I keep from a sale at that price (from R7, optional): £[AMOUNT OR "NOT SURE"]
Roughly how long listing, messaging and packing takes me per item: [MINUTES]
Other similar items I have that could go with it: [LIST OR "NONE"]

Compare four options in a short table: list alone, bundle with similar items, list as part of a job lot, or donate or recycle. For each, give: effort, likely money kept (only from my numbers, otherwise [CHECK]), and one line on when it makes sense.
Then give a one-line recommendation.

Rules: UK English, pounds. Only use my numbers. Do not promise anything will sell. Be practical, not preachy.
```
**What good output looks like:**
> **Item:** paperback thriller, good condition. Comps £2 to £3 sold. You keep about £0.60 after postage. 15 minutes per item.
>
> | Option | Effort | Money kept | When it makes sense |
> |---|---|---|---|
> | Alone | 15 min | about £0.60 | Rarely, unless it is a sought-after edition |
> | Bundle of 5 same author | 20 min | [CHECK: find bundle comps] | When you have a set |
> | Job lot of 20 | 30 min | [CHECK] | Clearing a shelf |
> | Donate | 5 min | £0 | When time matters more |
>
> **Recommendation:** hold it back for a same-author bundle, and search sold bundles before pricing.

*(Example figures only, invented for illustration.)*

**Check before you post:**
- Bundle and job lot titles still list every item accurately.
- Job lot photos show everything included.
