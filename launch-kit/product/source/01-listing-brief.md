# Module 01: The Listing Brief

The Listing Brief is a short block of facts about one item. You fill it in once, save it in your notes app, and paste it into any prompt in this kit. An AI tool can only be as accurate as what you give it: "blue jumper, good condition" gets guesses, a proper brief leaves nothing to guess.

## How to fill in a brief (about 2 minutes)

1. Have the item and a tape measure in front of you.
2. Copy the brief that matches your item (general, or a category version below).
3. Fill in what you know. **Blank is better than wrong.** A blank becomes a [CHECK: ...] you can fix. A wrong line becomes a "not as described" return.
4. Write flaws plainly: where, what, how big. "Small pale mark on left cuff, about 5 mm" is perfect.

A brief is about the item, never about people. No buyer names, addresses or order details.

---

## The master Listing Brief (general)

```text
LISTING BRIEF
Platform(s): [EBAY UK / VINTED / DEPOP / ETSY / AMAZON UK / TIKTOK SHOP]
What it is (plain words): 
Brand / maker: 
Model, style name or product number: 
Size (as on the label): 
Measurements (cm): 
Colour: 
Material (from the label): 
Condition: New with tags / New without tags / Excellent / Very good / Good / Fair
Flaws (where, what, how big): 
Included (box, cables, dust bag, spare buttons): 
Not included: 
Age or era (only if known): 
Smoke-free / pet-free home (only if true): 
Postage (service and who pays): 
Price I want: 
Lowest I will accept (private, never shared): 
Anything else a buyer would ask: 
```

**About the condition line:** this is our honest six-step scale (Module 03 explains each grade). Platforms use their own names, so you pick the nearest match when you list. Vinted's lowest option, for example, is "Satisfactory".

Every prompt that writes buyer-facing copy is told never to reveal your lowest price.

---

## Category extras

The master brief works for anything. For these categories, add the extra lines buyers ask about most (or ask B5 to build a brief for your own category).

**Clothing, shoes and accessories.** Measurements beat sizes: a size 12 from 2024 is not a size 12 from 1985.

```text
CLOTHING EXTRAS
Size on label (UK / EU / US as printed): 
Measurements, laid flat (cm):
  Pit to pit (armpit seam to armpit seam): 
  Length (top of shoulder by the collar to hem): 
  Sleeve (shoulder seam to cuff): 
  Waist (straight across; say if doubled): 
  Inside leg (crotch seam to hem): 
Fabric (copy the care label, e.g. 60% acrylic, 40% wool): 
Fit / cut (e.g. oversized, cropped, high waisted): 
Tags attached? (yes / no / cut label): 
Era (only if known: "tag style suggests 1990s" is fine, a guessed year is not): 
```

**Electronics.** Buyers want to know it works, what comes with it, and whether anything is locked.

```text
ELECTRONICS EXTRAS
Exact model name and number (label or settings screen): 
Tested? How? (e.g. "powered on, Wi-Fi connected, played a video for 10 minutes"): 
Not tested (e.g. "Bluetooth not tested"): 
Faults or quirks: 
Battery health (figure if shown, or "not checked"): 
Factory reset and accounts removed? (yes / no): 
Network lock (phones: unlocked / locked / not checked): 
```

Never write "fully working" unless you tested every function. "Tested and working: power, screen, Wi-Fi. Not tested: Bluetooth" is honest and protects you.

**Books, music and media.** Only write "first edition" if the copyright page supports it, in its exact words.

```text
MEDIA EXTRAS
Format (hardback, paperback, vinyl LP, CD, DVD, game): 
Edition, printing and year of this copy (copyright page or label): 
ISBN / catalogue number: 
Region (DVD, Blu-ray, games): 
Signed or inscribed? (only if true, say where): 
Flaws (foxing, inscriptions, stickers, creases, scratches, ring wear): 
Tested? (e.g. "disc plays without skipping"): 
```

**Homeware.** Run a fingertip round every rim and hold china up to the light: hairline cracks and tiny chips cause most homeware claims.

```text
HOMEWARE EXTRAS
Maker's mark or backstamp (copy it exactly): 
Pattern or range (only if marked or confirmed): 
Dimensions (height, width, diameter, capacity): 
Flaws (chips, crazing, hairline cracks, stains, wobble): 
Oven / dishwasher safe? (only if the base or box says so): 
Set or single? (how many pieces, all matching?): 
```

**Toys and collectables.** "Rare" and "limited edition" only if the item or box says so. Collectors check.

```text
TOYS AND COLLECTABLES EXTRAS
Name, set number or series (from the box or item): 
Complete? (what is present, what is missing, pieces counted?): 
Box and instructions (present, condition, sealed or opened): 
Batteries and tested? (lights, sounds, motors): 
Age guidance on box (copy exactly): 
```

**Handmade.** "Soothing" candles and "healing" crystals are health claims. Describe what it is made of, not what it does to the body.

```text
HANDMADE EXTRAS
Materials (every one, including findings, thread, finish, glaze): 
Personalisation (what can change, character limits): 
Made to order or ready to post, and making time: 
Care instructions: 
Allergy information (e.g. "nickel-free" only if your supplier confirms it): 
Each piece varies? (e.g. hand-dyed): 
Safety notes (e.g. "not a toy", candle safety): 
```

---

## The B prompts

These build a brief from whatever you have: scribbled notes, a voice note, a photo description or a box label. The AI only organises facts and flags gaps. It does not write the listing yet.

### B1 Messy notes to Listing Brief
**Use it when:** You have jotted a few scrappy notes about an item and want a tidy brief.
**Paste this:**
```text
Turn my notes below into a Listing Brief for a UK second-hand seller, using these headings:
Platform(s), What it is, Brand, Model or style, Size, Measurements (cm), Colour, Material, Condition, Flaws, Included, Not included, Age or era, Postage, Price.

Rules:
- UK English.
- Use ONLY facts in my notes. Do not add, assume or improve anything.
- If a heading has no information, write [CHECK: what I need to find out], e.g. [CHECK: measure pit to pit in cm].
- Keep every flaw exactly as serious as I wrote it.
- If I gave inches, show both (e.g. 21 in / 53 cm).
- No sales language. This is a fact sheet.
- At the end, list the 3 most important [CHECK] items a buyer would ask about.

My notes:
[PASTE YOUR NOTES HERE]
```
**What good output looks like:**

For the notes "grey next jumper sz12 wool mix, bit bobbly under arms, vinted, want 12 quid":

> **What it is:** Jumper
> **Brand:** Next
> **Model or style:** [CHECK: crew neck, V-neck or roll neck?]
> **Size:** 12
> **Measurements (cm):** [CHECK: pit to pit, length and sleeve, laid flat]
> **Material:** Wool mix [CHECK: exact composition from the care label]
> **Flaws:** Some bobbling under the arms
> **Top 3 checks:** fabric composition, measurements, any marks or holes besides the bobbling.

**Check before you post:**
- Make sure the AI has not quietly upgraded your words (for example "wool mix" becoming "merino").

### B2 Voice note transcript to Listing Brief
**Use it when:** You talked about the item into your phone (quicker than typing) and have the transcript.
**Paste this:**
```text
Below is a transcript of me talking about an item I am selling in the UK. It will ramble. Turn it into a Listing Brief with these headings:
What it is, Brand, Model or style, Size, Measurements (cm), Colour, Material, Condition, Flaws, Included, Not included, Tested (how), Postage, Price.

Rules:
- UK English.
- Where I corrected myself ("no wait, it's a 14"), use the correction only.
- Use ONLY facts I said. Do not fill gaps with typical details.
- Missing or unclear facts become [CHECK: ...].
- Transcription often mishears brands and numbers. If one looks odd, keep it and add [CHECK: transcript said "X", confirm spelling].
- Keep every flaw at the same level of seriousness. No sales language.

Transcript:
[PASTE TRANSCRIPT HERE]
```
**What good output looks like:**

For "it's a Dualit toaster, um, four slice, cream, works fine, I did two rounds of toast, there's a little dent on the back, no, the side, left side":

> **What it is:** Four-slice toaster
> **Brand:** Dualit [CHECK: model number from the base label]
> **Tested (how):** Toasted two rounds of bread
> **Flaws:** Small dent on the left side [CHECK: size in mm or cm]

**Check before you post:**
- Check brand names and model numbers against the label. Transcription gets them wrong most often.

### B3 Photo description to Listing Brief
**Use it when:** You want to describe what you can see, photo by photo, and turn it into a brief. The AI does not need to see images, so it works in any free tool.
**Paste this:**
```text
I will describe my item photo by photo. Build a UK Listing Brief from my descriptions only, with these headings:
What it is, Brand, Model or style, Size, Measurements (cm), Colour, Material, Condition, Flaws (with location), Labels and markings (exact wording), Included, Postage, Price.

Rules:
- UK English. No sales language.
- Use only what I describe. Do not guess brand, age, material or value.
- For each flaw, record where and how big. If I gave no size, add [CHECK: size of flaw].
- After the brief, list extra photos a buyer would expect that I have not described (care label, base stamp, flaw close-up).

Photo 1: [DESCRIBE]
Photo 2: [DESCRIBE]
Photo 3: [DESCRIBE]
Price: [PRICE]
Postage: [POSTAGE]
```
**What good output looks like:**

> **What it is:** Ceramic milk jug
> **Labels and markings:** base stamp reads "Denby, Made in England" (as described)
> **Flaws:** tiny glaze chip on the rim next to the spout [CHECK: size in mm]
> **Extra photos to take:** the rim chip next to a coin for scale, the base stamp in focus.

**Check before you post:**
- If you are not sure a mark is genuine, say what it reads rather than who made it.

### B4 Gap finder: what a buyer will ask
**Use it when:** You have a brief and want to catch the questions buyers will message you about.
**Paste this:**
```text
Here is a Listing Brief for an item I am selling on [PLATFORM] in the UK. Act as a fussy buyer in this category.

1. List up to 8 questions a serious buyer would ask, most important first.
2. For each, say whether my brief answers it: Yes, No or Partly.
3. For every No or Partly, tell me what to check or measure and how, in plain words.

Do not write the listing. Do not invent answers. UK English, short lines.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like:**

For Levi's 501 jeans on eBay UK:

> | Question | Answered? | What to do |
> |---|---|---|
> | Real waist and inside leg? | Partly | Measure the waistband flat and double it. Inside leg from crotch seam to hem. |
> | Any wear at the crotch or hems? | No | Check the inner thighs and back hems. Photograph any thinning. |
> | Original hem or taken up? | No | Look for a factory hem. If unsure, say "unsure". |

**Check before you post:**
- Add the answers to the brief itself, so every platform version gets them.

### B5 Build my own category brief
**Use it when:** You sell a lot of one thing (bikes, prams, golf clubs, board games) and want a brief template made for it.
**Paste this:**
```text
I sell second-hand [CATEGORY] in the UK on [PLATFORM(S)]. Create a reusable Listing Brief template for this category, as a plain text block I can copy into my notes app.

Include:
1. The general fields: platform, what it is, brand, model, size or dimensions, colour, material, condition, flaws, included, postage, price, lowest I will accept (private).
2. Up to 10 extra fields buyers of this category care about, each with a hint on where to find the fact, e.g. "frame size (printed on the seat tube)".
3. A short "safety and legal" list of things I should check before selling this category in the UK, written as questions for me to check in the platform's help pages. Do not state rules as fact.

UK English, plain words, no sales language.
```
**What good output looks like:**

For children's car seats:

> Safety standard label (copy the exact wording):
> Date of manufacture (usually moulded into the shell):
> Ever been in a vehicle collision? (yes / no / unknown):
> ...
> Questions to check: Does the platform allow second-hand car seats? Are there rules on seats with no known history?

**Check before you post:**
- Some categories are restricted or banned on some platforms. Check the prohibited items page before listing.

### B6 Label or box text to Listing Brief
**Use it when:** You have a new or boxed item, or a clear product label, and want the facts copied off it accurately.
**Paste this:**
```text
Below is text I copied from the box, label or manual of an item I am selling in the UK. Extract a Listing Brief with these headings:
What it is, Brand, Model / product number, Specification, Colour, Material, Dimensions, In the box, Safety or age warnings, Condition, Flaws, Postage, Price.

Rules:
- UK English.
- Copy specifications exactly. Do not round, convert or tidy numbers.
- Copy safety warnings and age guidance word for word.
- Leave marketing claims (e.g. "clinically proven") out of the brief. List them separately under "Box claims left out" so I can decide.
- Condition, flaws, postage and price are not on the box: write [CHECK: ...] unless I give them below.

Box or label text:
[PASTE TEXT HERE]

My extra details (condition, flaws, whether opened, postage, price):
[ADD DETAILS]
```
**What good output looks like:**

> **In the box:** 1 handle, 1 brush head, 1 charging base
> **Condition:** New, box opened to check contents, brush head still sealed
> **Box claims left out:** "removes up to 100% more plaque". A manufacturer claim: leave it out unless you are the brand and can support it.

**Check before you post:**
- Check whether the category has hygiene rules on the platform. Opened personal care items often do.

### B7 Brief tidy-up and consistency check
**Use it when:** Your brief is filled in and you want a sanity check before running the title and description prompts.
**Paste this:**
```text
Check my Listing Brief for a UK [PLATFORM] listing. Do not rewrite it into a listing.

Report, in this order:
1. Contradictions (e.g. condition "Excellent" but flaws that sound like "Good").
2. Vague wording a buyer could dispute (e.g. "small mark" with no location or size), with a clearer version using only my facts.
3. Missing facts buyers in this category expect, as [CHECK: ...] lines.
4. Risky claims ("rare", "genuine", "fully working", "vintage" without an era, health claims), one line each on why.
5. US spellings or sizes to change.

UK English, short bullet points. Do not invent facts to fix problems. Ask me instead.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
```
**What good output looks like:**

For a Radley handbag:

> **Contradiction:** condition "Excellent" but "corners rubbed through to the lining". That is nearer Good or Fair.
> **Risky claim:** "100% genuine": only with proof (receipt, bought from the brand). Otherwise state the brand and show the labels.
> **US to UK:** "purse" to "handbag".

**Check before you post:**
- Fix contradictions in the brief itself so every platform version inherits the fix.

---

## Weak brief, strong brief

| Weak | Strong |
|---|---|
| Size M | Size M on label. Pit to pit 54 cm, length 68 cm, laid flat |
| Good condition | Good. Light bobbling under both arms. No holes or marks |
| Small mark | Pale mark on front, left of the buttons, about 5 mm |
| Works | Tested: powers on, connects to Wi-Fi, all buttons respond. Bluetooth not tested |
| Vintage | Care label and tag style suggest 1990s (not confirmed) |
| Genuine | Brand labels shown in photos. Receipt available (only if true) |

Next: Module 02 for titles, 03 for descriptions and 04 for keywords, tags and item specifics.
