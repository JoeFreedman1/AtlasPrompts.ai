# Module 06: Pricing

These prompts replace a guess with a short written reason you can stand behind. They help you set a sensible price from real evidence and do the sums properly. They cannot promise a sale or a price: buyers decide that.

## The rule: you find the sold prices, the AI does the maths

AI chat tools do not know what your item sold for last week. Ask "what is this worth?" and you get a confident guess. Instead:

1. **Look up sold listings yourself** on the platform you sell on. On eBay, search and turn on the "Sold items" filter. Elsewhere, look for items marked sold. An asking price is not a sold price.
2. **Copy 5 to 10 comparable items** into your notes: title, sold price, postage, condition and date if shown. Close matches beat lots of matches.
3. **Paste them into the prompt** with your Listing Brief.

Do not use scraping tools, bots or browser add-ons that harvest listings. Most platforms' terms forbid it, and ten minutes of looking gives better comps because you can see which items really match.

**A good comp** is the same brand and model or style, a similar size and condition, sold in the last few months, with postage noted. "Similar" items from another brand, new-with-tags items against your worn one, and unsold asking prices are weak comps.

---

### R01 Tidy my sold comps
**Use it when:** You have copied a messy pile of sold listings into your notes and want a clean table before pricing.
**Paste this:**
```text
Put the sold listings I copied into a clean table so I can compare them with my item.

Columns: Title (shortened), Sold £, Postage £ (or "free" or [CHECK]), Total £, Condition, Size or model, Date sold (or [CHECK]), Match to my item (Good, Partial, Poor) with a one-line reason.

Rules:
- UK English, pounds.
- Only use numbers in what I pasted. Never invent a price, date or condition. Missing details become [CHECK].
- If something looks like an asking price, flag it [CHECK: sold or asking?].
- Good matches first. Below the table, list comps to drop and why.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

Sold listings I copied (messy is fine):
[PASTE YOUR SOLD LISTINGS HERE]
```
**What good output looks like** for the Next jumper (invented figures):

> | Title | Sold £ | Postage £ | Total £ | Condition | Match |
> |---|---|---|---|---|---|
> | Next grey wool blend jumper, 12 | 12.00 | 2.99 | 14.99 | Good | Good: same style and size |
> | Next wool mix jumper grey NWT, 12 | 22.00 | 3.20 | 25.20 | New with tags | Poor: new, yours is worn |
>
> **Drop:** the NWT one.

**Check before you post:**
- You have at least three Good matches before moving on to R02.

### R02 Price from my sold comps
**Use it when:** You have your tidied comps and want a list price, a realistic range and a floor.
**Paste this:**
```text
Suggest a price for my item using only the sold listings I found.

Platform: [PLATFORM]
Buyer pays postage on top, or included in my price? [ON TOP / INCLUDED]

Give me:
1. The sold range from Good matches only, lowest to highest, and the median.
2. Whether my item is better, the same or worse than those matches, from my brief only.
3. A list price, a likely accepted price, and my floor from the brief. If my floor is above what the comps support, say so.
4. Two or three lines of reasoning I can save.

Rules:
- UK English, pounds, show the sums. Write ranges as "£10 to £14".
- Use only the numbers I pasted, no outside price knowledge.
- Fewer than three Good matches: say the evidence is thin and what to search for.
- Say "based on these comps", never "this will sell for".

My Listing Brief (includes my floor):
[PASTE YOUR LISTING BRIEF HERE]

My sold comps (ideally the table from R01):
[PASTE COMPS HERE]
```
**What good output looks like** for Clarks black leather Chelsea boots, UK 6, floor £18 (invented figures):

> 1. **Good matches sold for** £20 to £32. Median £25.
> 2. **Condition:** similar to most. The heel scuff puts you slightly below the two best.
> 3. **List at £28, expect offers around £22 to £25, floor £18.**
> 4. **Reasoning:** five Good matches, median £25. A little above median leaves room for offers.

**Check before you post:**
- Your floor still covers fees and postage (use R07).

### R03 Adjust for condition and extras
**Use it when:** Your item is not quite like the comps (better or worse condition, no box, extra accessories) and you want a fair adjustment.
**Paste this:**
```text
My item differs from the comps I found. Help me adjust the price fairly.

How my item differs (my own words):
[E.G. "NO ORIGINAL BOX, BUT COMES WITH A SPARE CHARGER"]

1. For each difference: up, down or no clear difference, with a one-line reason a buyer would recognise.
2. If the comps show the effect (boxed sold higher than unboxed), use those numbers and show the sum. If not, say "the comps do not show this" and label your suggestion a judgement, not evidence.
3. Give an adjusted list price and floor.

UK English, pounds. Only numbers I pasted. Never guess a "collector's value". Never suggest describing the item as better than my brief.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]

My closest sold comps:
[PASTE COMPS HERE]
```
**What good output looks like** for a turquoise Switch Lite, light screen scratches, no box, with a case (invented figures):

> 1. **No box:** down. Boxed comps sold at £95 and £100, unboxed at £82 and £85: about £12 to £15 less.
> 2. **Screen scratches:** down. The comps do not show this. Judgement: price towards the lower end of unboxed.
> 3. **Case:** small plus, not shown in the comps.
>
> **Adjusted list £85, floor £75.**

**Check before you post:**
- The differences (no box, scratches, extras) are in your description too.

### R04 Bundle pricing
**Use it when:** You want to sell several items together, or a buyer asks for a bundle price.
**Paste this:**
```text
Help me price a bundle.

Items (one line each, with my list price and floor):
[PASTE ITEMS HERE]
Platform: [PLATFORM]
Postage as one parcel: £[AMOUNT OR "NOT SURE"]
Postage if sent separately (total): £[AMOUNT OR "NOT SURE"]
Platform bundle discount switched on? [YES, WITH % / NO / NOT SURE]

Give me:
1. The total of list prices and the total of floors.
2. The postage saving from one parcel, if I gave both figures.
3. A bundle price and the lowest bundle price to accept, never below the total of my floors.
4. One friendly line to send the buyer, based on the postage saving, with no pressure.

UK English, pounds, show the sums. Use only my numbers; missing postage becomes [CHECK: postage]. No "today only" or "last chance".
```
**What good output looks like** for three Frugi tops, age 4 to 5 (£8, £8, £7 list; £6, £6, £5 floor), invented figures:

> 1. **List total** £23. **Floor total** £17.
> 2. **Postage saving:** £8.40 separately against £3.20 as one parcel, so £5.20.
> 3. **Bundle £19, accept down to £17.**
> 4. "I can do all three for £19. They go in one parcel, so it saves on postage."

**Check before you post:**
- If the platform takes its own bundle discount off on top, you have included it in the sums.

### R05 Offer strategy
**Use it when:** You want to decide in advance which offers to accept, counter or decline, so you are not deciding at 11pm with a lowballer waiting.
**Paste this:**
```text
Help me set an offer plan for this listing.

Platform: [PLATFORM]
List price: £[AMOUNT]
My reasoning from comps (optional): [PASTE OR "NONE"]
Can the app auto-accept or auto-decline offers? [YES / NO / NOT SURE]

Give me:
1. Accept straight away at or above: £...
2. Counter if between £... and £..., and the counter price to send.
3. Decline below: my floor.
4. If auto settings exist, the levels to set, with a reminder to check how they work in the app.
5. One short, polite line for each case.

UK English, pounds. Never accept or counter below my floor. No fake scarcity or pressure ("someone else is interested") unless I say it is true.

My Listing Brief (includes my floor):
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like** for a Le Creuset casserole, list £65, floor £48:

> 1. **Accept** at £58 or more.
> 2. **Counter** offers from £48 to £57 at £56.
> 3. **Decline** below £48.
> 4. **Auto settings:** auto-accept at £58. Auto-decline below £48, or set it a little lower (say £45) if you want near misses to reach you so you can counter at your floor yourself.
> 5. Counter: "Thanks for the offer. The lowest I can do is £56, as it is heavy to post."

**Check before you post:**
- Any reason you give (like heavy postage) is true.

### R06 Planned price drop schedule
**Use it when:** An item has not sold and you want a calm plan for reducing it, rather than panic-dropping or leaving it forever.
**Paste this:**
```text
Make a price drop plan for an item that has not sold.

Platform: [PLATFORM]
Current price: £[AMOUNT]
Listed for: [NUMBER] days
Views, likes or watchers (if shown): [NUMBERS OR "NOT SURE"]

Give me:
1. First, anything other than price that could be holding it back (cover photo, title, missing measurements, postage), from my brief only. [CHECK: ...] for anything you cannot see.
2. A drop plan in weeks from today, with the price at each step, stopping at my floor.
3. What to do if it has not sold at the floor (bundle, relist with new photos, sell elsewhere, donate).

UK English, pounds, round numbers. Never below my floor. Do not say any step will make it sell. If the app lets me send offers to people who liked it, mention that as an option to check.

My Listing Brief (includes my floor):
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like** for a cream Zara linen shirt, size S, listed 21 days at £14, 2 likes, floor £8:

> 1. **First:** no chest measurement in your brief [CHECK: add pit to pit and length]. Check the cover photo is not crumpled.
> 2. **Week 1:** fix those, keep £14. **Week 2:** £12, and send an offer to the likers if the app allows. **Week 4:** £10. **Week 6:** £8, stop.
> 3. **If still unsold:** bundle with other size S linen, relist in spring, or donate.

**Check before you post:**
- You fix listing problems before you drop the price.

### R07 Fee and postage maths
**Use it when:** You want to know what you actually keep after fees, postage and packaging, before you set a price or accept an offer. Makers: put your materials (and time, if you want it counted) in the cost line.
**Paste this:**
```text
Work out what I keep from a sale, using fees I copy from the platform myself.

Platform: [PLATFORM]
Sale price: £[AMOUNT]
Postage the buyer pays: £[AMOUNT OR "NONE, INCLUDED"]
My actual postage cost: £[AMOUNT]
Packaging: £[AMOUNT OR "0"]
Fees copied from the platform's fee page today (percentage, fixed fee, whether it applies to postage):
[PASTE CURRENT FEE DETAILS HERE]
What the item cost me (optional): £[PRICE PAID, OR FOR MAKERS: MATERIALS + SHARE OF KILN OR TOOLS + TIME AT A RATE I CHOOSE, EACH LISTED]
Amount I want to keep: £[TARGET AMOUNT]

Show a simple table: money in, each fee with its sum, postage and packaging out, what I keep, and what is left after cost if I gave one. Then the lowest sale price that still keeps my target amount.

Rules:
- UK English, pounds, nearest penny.
- Use ONLY the fees I pasted, never your own knowledge. Unclear fees become [CHECK: ...].
- This is a sum, not advice. Only call it "profit" if I gave a cost. If I listed making costs, add them up and show each one.
```
**What good output looks like** for a sale at £15, buyer pays £3.50 postage, real postage £3.20, packaging £0.30, and fees invented for this example (10% of the total including postage, plus £0.30 per order):

> | Line | Sum | £ |
> |---|---|---|
> | Money in | 15.00 + 3.50 | 18.50 |
> | Percentage fee | 10% of 18.50 | 1.85 |
> | Fixed fee | | 0.30 |
> | Postage and packaging | 3.20 + 0.30 | 3.50 |
> | **You keep** | 18.50 minus 5.65 | **12.85** |
>
> To keep at least £10, the lowest sale price is £11.84: (10 + 0.30 + 3.20 + 0.30) divided by 0.9, minus 3.50, rounded up.

*(The fees above are invented to show the maths. They are not any platform's real fees.)*

**Check before you post:**
- You pasted today's fees from the platform's own pages, and weighed the parcel.
- Fees can differ for private and business sellers.

### R08 Is it worth listing on its own?
**Use it when:** You have a low-value item and are not sure whether to list it alone, bundle it or let it go.
**Paste this:**
```text
Help me decide whether this item is worth listing on its own.

Sold comps (optional): [PASTE OR "NONE"]
What I keep at that price (from R07, optional): £[AMOUNT OR "NOT SURE"]
Minutes it takes me to list, message and pack one item: [MINUTES]
Similar items I could put with it: [LIST OR "NONE"]

Compare in a short table: list alone, bundle, job lot, donate or recycle. For each: effort, money kept (from my numbers only, otherwise [CHECK]) and when it makes sense. Then a one-line recommendation.

UK English, pounds. Only my numbers. Do not promise anything will sell. Practical, not preachy.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**Check before you post:**
- Bundle and job lot listings still list every item accurately.
