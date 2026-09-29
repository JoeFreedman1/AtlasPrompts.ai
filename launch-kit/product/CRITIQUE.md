# Critique of The Well Listed Kit

Internal document. Not shipped to buyers.

## Round 1

Reviewer brief: read as a paying customer. A busy UK reseller, around 40 items a week on Vinted and eBay and a few on Depop, who has just paid £19 and has seen plenty of "650+ prompts" packs that turn out to be padding. Every prompt was tested in our heads against free ChatGPT on a phone: can it be pasted in one go, does it give the AI one clear job, does it contradict itself, and do the examples obey the prompt's own rules?

Baseline before fixes: 13 modules, 88 prompts in the library, PDF guide 214 A4 pages.

The 10 weaknesses, most serious first.

### 1. There is no real fast path, and the one starter prompt is not in the library

Evidence:
- The only "do it now" prompt is "The 5-minute starter prompt" at `00-start-here.md` lines 51 to 87. It sits below a 13-row contents table and a templates table, so on a phone it is several screens down.
- Its heading ("### The 5-minute starter prompt") has no ID, so `build.py` skips it. It is missing from `prompt-library.html` and `all-prompts.txt`, which is exactly where a phone user looks first.
- Step 1 of the 5 minutes is "Open Module 01, copy the brief for your category and fill in what you know" (line 55). That is a second document and a 20-line form before the AI has done anything.
- There is no all-in-one prompt for any platform. To list one jumper on Vinted the "proper" route is B1, T2, D2, K4 and C3: five pastes.

Planned fix: put a one-page "Quick start: your first listing in 5 minutes" at the very top of `00-start-here.md`, built on a single all-in-one prompt that has the fill-in facts built into it (no separate brief needed). Add one all-in-one prompt per platform with IDs the build can see: A1 Vinted, A2 eBay UK, A3 Depop, A4 Etsy, A5 Amazon UK, A6 TikTok Shop UK. Point READ-ME-FIRST.txt at it.

### 2. The worked examples break the rules the prompts set, and the running example contradicts itself

Evidence:
- T1's example titles (`02-titles.md` lines 118 to 120) add "Crew Neck", "Long Sleeve", "Knit Pullover", "Soft" and "Casual" to a brief that only says grey Next wool-blend jumper, size 12. The prompt's own rule 2 says "Use ONLY facts in my Listing Brief", and B1's example (`01-listing-brief.md` line 260) marks the style as `[CHECK: style, e.g. crew neck...]`.
- The same Next jumper has a pit to pit of 51 cm (`03` line 121), 52 cm (`08` line 70) and 50 cm (`09` line 56), and a composition of "60% polyester, 30% acrylic, 10% wool" (`03` line 128) while every title calls it "Wool Blend". Selling 10% wool as "wool blend" in the title is the kind of thing that gets a Vinted "not as described" claim.
- Worked example 2 (`11-worked-examples.md` line 92) says "Used, fully working" in the brief while also listing a loose controller stick, against our own tip at `01` line 124 ("never describe electronics as fully working unless you have tested every function"). The title then says "Tested Working".
- Worked example 3 description adds "thrown and glazed by hand in our studio" and "The holders get warm when in use" (`11` lines 182 and 188). Neither is in the brief.
- Worked example 4 reply says "It's a men's M" (`11` line 274) while the brief's category line says `[CHECK: or Women, depending on the cut]` (line 255), and opens with "Hi!" against our no-exclamation-mark rule.
- Worked example 5 search terms include "bamboo" for a beech stand (`11` line 324), which K5 rule 7 forbids.

Planned fix: make every example obey its prompt. Give the Next jumper one consistent set of facts everywhere (pit to pit 51 cm, length 63 cm, sleeve 58 cm, 60% acrylic and 40% wool). Remove the invented details and correct the replies.

### 3. It is padded: 214 pages is too many for a busy seller

Evidence:
- The PDF is 214 A4 pages. Most of the length comes from long example blocks, 2 to 4 "Check before you post" bullets per prompt that repeat each other (for example "Replace every [CHECK]" appears in some form in nearly every module), and the same seven-line rules block restated in every prompt.
- Module intros restate the Listing Brief method three times (`00` lines 134 to 148, `01` lines 3 to 7, and each module's opening paragraph).
- 00 has a full "How to read a prompt" section plus a separate "Listing Brief method" section plus 12 golden rules, all saying much the same.

Planned fix: cut repetition and padding without removing useful prompts. Shorten examples to what shows the shape of a good answer, keep "Check before you post" to 2 or 3 bullets that are specific to that prompt, and compress the repeated rules. Target: well under 150 pages.

### 4. The same content appears in two or three places, sometimes with conflicting numbers

Evidence:
- Two TikTok Shop title prompts: T6 (`02` line 277, "Aim for 60 to 100 characters") and V4 (`08` line 177, "roughly 60 to 120 characters"). Same job, different targets.
- Two keyword stuffing checkers: K7 (`04` line 322) and C10 (`09` line 427).
- The private seller versus trader table appears twice (`07` lines 35 to 42 and `09` lines 516 to 523).
- 19 reply templates in `07` (lines 465 to 526) and 20 different reply templates in `templates/message-snippets.txt`. A buyer gets two slightly different "polite decline" lines and wonders which is right.
- The photo shot list table in `05` (lines 35 to 47) repeats `templates/photo-shot-lists.md`.
- US to UK word lists in `02` (line 81), `04` (lines 52 to 67), D10 and K8.
- Platform limit tables in `02`, `04` and `12`.

Planned fix: one home for each. Remove V4 and C10 (point to T6 and K7). Keep the seller status table in 07 only. Move the best of 07's templates into `message-snippets.txt` and point to it. Point 05 to the shot-list template. Keep the full US to UK table in 04 only and the full limits in 12.

### 5. Many prompts are too long to paste comfortably on a phone, and the placeholders are inconsistent

Evidence:
- The longest prompts run to around 2,000 characters before the seller has pasted anything: C5 Etsy check 2,072, C11 1,993, C6 1,965, C2 1,938, C7 1,896, C8 1,832, W1 1,814, M7 1,624. On a phone that is a lot of scrolling to find the brackets.
- Most prompts spend 6 to 8 lines restating the same rules (UK English, only facts, [CHECK], no hype, no other brands).
- Placeholders vary: `[PASTE YOUR LISTING BRIEF]` (8 times, modules 08) versus `[PASTE YOUR LISTING BRIEF HERE]` (53 times), and T1 has the confusing `[FORMULA, OR WRITE "YOUR CHOICE"]` (`02` line 99).

Planned fix: compress each rules block to a few short lines, cut the per-platform checks (C2 to C7) to the points that differ by platform, keep every prompt comfortably phone-sized (roughly 1,200 characters or fewer), and standardise placeholders in [CAPITALS], using `[PASTE YOUR LISTING BRIEF HERE]` everywhere.

### 6. Some platform facts are stated as fact without a source (breaks writing rule 9)

Evidence (none of these are in `research/platform-rules-uk.md`):
- "Buyers generally have 30 days from delivery" for the eBay Money Back Guarantee (`07` line 46).
- Vinted's Buyer Protection window "2 days at the time of writing" (`07` line 48).
- eBay condition names "from February 2025" (`03` line 29) and an eBay "item conditions by category" help page (`03` line 38).
- "eBay calls it feedback extortion" (`07` line 419).
- "eBay's rules say 'dupe' with a brand name is not allowed" (`09` line 88).

Planned fix: remove the unverified specifics or turn them into "check the current rule in the platform's help pages".

### 7. A few templates are legally shaky on seller status and authenticity

Evidence:
- `templates/stock-and-pricing-tracker.csv` EXAMPLE-002 buys a PS4 at a car boot for £60 to resell for £100 and notes "Private seller". Our own guidance (`07` line 33, C11) says buying to resell makes you likely to be a trader.
- `templates/message-snippets.txt` reply 10 says "It's genuine [BRAND]" with no proof step, against golden rule 2 and C9, which tell sellers to state the proof instead of the word "genuine".
- The CSV and text brief templates use a different condition scale (very good, good, satisfactory) from the master brief in Module 01 (Excellent, Very good, Good, Fair) without saying why.

Planned fix: make the tracker example an item from the seller's own home (no resale), rewrite reply 10 to point at the evidence, and align the condition wording with a short note that Vinted's own option is "Satisfactory".

### 8. Inconsistent labels and headings

Evidence:
- Photo prompts are PH1 to PH8, but `00` says "P photos" (lines 24 and 156) and W6's example says "P prompts" (`10` line 272).
- Module titles are mixed: "# Module 01: The Listing Brief" versus "# 05 Photos", "# 07 Buyer messages".
- Every "**Use it when:**" line starts with a lower-case letter ("you have jotted down...", `01` line 234). The library shows that text raw under each prompt title, so it reads like a broken sentence.

Planned fix: one heading style for modules ("# Module NN: Name"), "PH" everywhere, and every "Use it when" line starting with a capital. Keep all prompt headings in the exact form "### ID Name".

### 9. The reseller core is buried under brand-owner material, with no map

Evidence:
- A second-hand seller does not need Amazon backend search terms, TikTok Shop live run-sheets or Etsy tags, but T5, T6, D4, D5, K2, K5, V4 to V7, C5 to C7 and worked examples 3, 5 and 6 are mixed in with the everyday prompts with no "skip this if" note.
- There is no "which prompt do I need?" route. The 00 contents table (lines 17 to 31) lists what each module covers, not which prompt solves which job.

Planned fix: add a short "Which prompt do I need?" table in 00, organised by job (list an item, price it, reply to a buyer, check it), and a one-line "Skip this module if..." note at the top of the modules aimed at brand owners and new stock.

### 10. Conflicting instructions and a few claims we cannot back

Evidence:
- D2 tells a private Vinted seller "First person plural is fine ('we')" (`03` line 143). Someone selling from their own wardrobe writes "I".
- T1 says "Aim for 70 to 80 characters" and "Do not repeat words", which pushes the AI to pad (hence "Long Sleeve Knit Pullover"), while its own check list warns against padding.
- R5's example sets auto-decline "under £45 (a little below your floor)" (`06` line 220) in a prompt whose rule is "Never go below my floor". It is logically fine (offers between £45 and £48 reach you to decline by hand) but reads as a contradiction.
- Worked example 1 says "Our original '8 quid' guess would have left money on the table without being any quicker to sell" (`11` line 69). We cannot know that, and it leans towards an earnings claim.
- `08` opens "Short videos sell things." That is a sales claim we cannot support.
- M7's example reply tells a buyer "You might find it resells well on here", which reads as brushing them off.

Planned fix: D2 uses "I" or neutral wording. T1 asks for the most useful true words within 80 characters and says not to pad. Reword R5's auto-decline line. Remove the unprovable lines and rewrite the M7 reply.

## Round 1 result

All 10 fixed in `product/source/`, `product/templates/` and `product/READ-ME-FIRST.txt`. `build.py` and `dist/` were not edited.

- Prompts: 88 before, 89 after (6 all-in-one prompts A1 to A6 added; duplicates V4 and C10 removed; padding prompts PH8 cover photo (folded into PH4), V8 week of videos and K8 word pairs (covered by the table in Module 04) removed).
- PDF length: 214 A4 pages before, 136 after (measured with the same Chromium print settings as `build.py`, in a scratch folder).
- Longest prompt: 2,072 characters before (C5), 1,279 after (C11). Every prompt now fits comfortably in a phone chat.
- `check_content.py`: 0 problems. One warning remains, on the deliberate "Sweater | Jumper" row of the US to UK table in Module 04.

### What changed

1. Quick start page at the very top of 00, with A1 to A6 all-in-one prompts (one per platform, facts built in, no separate brief needed) and a "Which prompt do I need?" table. The old unnumbered starter prompt is gone, so the fast path is now in the library. READ-ME-FIRST.txt points at A1 to A6.
2. Examples corrected: the Next jumper has one set of facts everywhere (51 / 63 / 58 cm, 60% acrylic and 40% wool); T1's example titles use only brief facts and stop short of 80 characters rather than pad; worked example 2 lists what was tested instead of "fully working"; example 3 drops the invented "gets warm" and studio lines; example 4's reply says "labelled M" and has no exclamation mark; example 5's search terms drop "bamboo" and title words. All character counts rechecked.
3. Padding cut: examples shortened (and dropped from 14 peripheral prompts where the prompt is self-explanatory), "Check before you post" trimmed to one or two specific points, repeated rules compressed, 00 sections merged, 01's six full category briefs turned into short "extras" blocks, 12 cheatsheet tightened, end-of-module checklists that repeated the intros removed. Example lines that the builder was running together into one paragraph are now bullet lists.
4. Duplicates removed: V4 (use T6), C10 (use K7); seller status table kept in 07 only; the 19 in-guide reply templates replaced by a pointer to `templates/message-snippets.txt`, which gained the two that were missing (late dispatch, sold on another app); 05 points to the shot-list template; the full US to UK table lives in 04; full limits live in 12.
5. Prompts shortened and placeholders standardised on `[PASTE YOUR LISTING BRIEF HERE]`; W4's mixed-case placeholder replaced with `[... OR WRITE "DEFAULT"]`; C2 to C7 cut to what differs by platform.
6. Unverified facts softened or removed: eBay "30 days", Vinted "2 days", eBay's "February 2025" condition names and "item conditions by category" page, "feedback extortion", eBay's "dupe" wording.
7. Tracker EXAMPLE-002 is now the seller's own console (not bought to resell) with a note about trader status; snippet 10 asks for the proof instead of asserting "genuine"; brief templates explain that Vinted's lowest condition option is "Satisfactory".
8. Every module heading is "# Module NN: Name"; photo prompts are PH everywhere; every "Use it when" line starts with a capital; every prompt heading is "### ID Name".
9. "Which prompt do I need?" table in 00; "Skip this if you only sell second-hand" notes on Module 08 and on T5, T6, D5, K5, C6 and C7; worked examples labelled resale or maker.
10. D2 uses "I"; T1 no longer asks for 70 to 80 characters; R5's auto-decline line explains itself; "left money on the table", "Short videos sell things" and the M7 "resells well on here" reply are gone.
