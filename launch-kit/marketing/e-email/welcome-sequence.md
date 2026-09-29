# Welcome sequence: The UK Listing Cheat Sheet (W1 to W7)

Seven plain emails for everyone who signs up for the free cheat sheet. Each one teaches one useful thing with a prompt the reader can use the same day, then mentions the kit in one light line. This sequence runs forever, so it never mentions the launch price. Where a price is needed it says [CURRENT_PRICE].

Note: these emails are called W1 to W7. The kit also has prompts called W01 to W08 (batch workflow, Module 10). They are not related; the emails never refer to those prompt IDs.

---

## How to load this into MailerLite (plain English, about 20 minutes)

You only do this once. After that it runs by itself for every new sign-up.

**Before you start, have ready:**
- The cheat sheet download link (replace [CHEAT_SHEET_LINK] with it).
- The Gumroad product link (replace [GUMROAD_PRODUCT_LINK] with it).
- The kit's current price as shown on Gumroad (replace [CURRENT_PRICE], for example "£19"). This is typed text, so if you ever change the price on Gumroad, come back and change it in W6 and W7 too. During the 14-day launch window, type the launch price; on the day it ends, change it to £19.
- Your footer postal address (replace [FOOTER_ADDRESS]). See "Footer" below.

**Step 1: make a group.** In MailerLite go to Subscribers, then Groups, and create a group called "Cheat sheet". Connect your sign-up form to this group (in the form settings, choose "Cheat sheet" as the group new subscribers join).

**Step 2: create the automation.** Go to Automations and create a new automation from scratch. Name it "Welcome sequence". For the trigger, choose "When subscriber joins a group" and pick "Cheat sheet".

**Step 3: add the emails and waits in this order.** In MailerLite each "Delay" step waits from the previous step, not from the sign-up. So the waits below are the gaps between emails, and they add up to the days shown.

| Step | What to add | Arrives on |
|---|---|---|
| 1 | Email W1 | Straight after sign-up |
| 2 | Delay: 1 day | |
| 3 | Email W2 | Day 1 |
| 4 | Delay: 2 days | |
| 5 | Email W3 | Day 3 |
| 6 | Delay: 2 days | |
| 7 | Email W4 | Day 5 |
| 8 | Delay: 2 days | |
| 9 | Email W5 | Day 7 |
| 10 | Delay: 2 days | |
| 11 | Email W6 | Day 9 |
| 12 | Delay: 3 days | |
| 13 | Email W7 | Day 12 |

**Step 4: set up each email.** For each email step:
- **Sender name:** Well Listed. **Sender email:** the brand address, [BRAND_EMAIL] (a brand Gmail or, better, an address on your own domain, which is less likely to land in spam). Never a personal name or personal address.
- **Subject** and **preview text:** copy from below. MailerLite's free plan may not include A/B testing inside automations; if it does not, use the main subject now and try the alternative later by swapping it for a month and comparing open rates.
- **Content:** choose the plain text or simplest "rich text" editor option, not a designed template. Paste the body exactly as written. Turn any [LINK] placeholder into a real link.
- The prompts inside the emails sit between "copy from here" lines so they stay readable in plain text.

**Step 5: add a condition so buyers stop getting sales lines (optional but kind).** If you can connect Gumroad to MailerLite (through Zapier or by adding buyers to a "Customers" group by hand), add "Customers" as an exit condition. If not, that is fine: the kit lines are one sentence each.

**Step 6: test it.** Sign up with a spare email address. Check W1 arrives, the cheat sheet link works, and the footer shows your address and an unsubscribe link. Then turn the automation on.

### Footer (required on every email)

- **Unsubscribe link:** MailerLite adds an unsubscribe link to every email footer automatically. Do not remove it. UK law (PECR and UK GDPR) says every marketing email must give an easy way to opt out.
- **Postal address:** MailerLite asks for a physical postal address and shows it in the footer. Put [FOOTER_ADDRESS] there. Use a business address, PO box or registered office service if you would rather not show your home address (see ASSUMPTIONS.md point 12).
- **Suggested footer text:** "You are getting this because you downloaded The UK Listing Cheat Sheet from Well Listed. Well Listed is independent and not affiliated with eBay, Vinted, Depop, Etsy, Amazon or TikTok. [FOOTER_ADDRESS]. Unsubscribe any time with the link below."

---

## W1: Your cheat sheet, and how to use it in 2 minutes

- **Send:** immediately after sign-up (automation step 1)
- **Subject:** Your UK Listing Cheat Sheet is here
- **Alternative subject (for testing):** Here is your cheat sheet (and a 2-minute way to use it)
- **Preview text:** Download link inside, plus two lines to paste when the AI makes things up.

**Body:**

~~~text
Hi,

Here is your free UK Listing Cheat Sheet:

[CHEAT_SHEET_LINK]

It has four parts: the Listing Brief template, 10 free prompts (F1 to F10), a character-limit table, and a 7-point checklist to run before you post.

The quickest way to use it (about 2 minutes):

1. Copy the Listing Brief into your notes app. That is your template from now on.
2. Pick one item you want to sell today. Fill in the brief with the item in front of you. Leave a line blank if you do not know it. Blank is better than wrong.
3. Open any free AI chat tool, paste one of the prompts with your brief, and read the draft next to the item.
4. Run the 7-point checklist, then post.

Today's lesson: what to type when the AI gets it wrong.

AI tools love to fill gaps with guesses. When that happens, do not start again. Reply with one of these:

----- copy from here -----
Remove anything that is not in my brief. Use [CHECK: ...] for anything missing.
----- to here -----

----- copy from here -----
Rewrite in UK English. Plain and factual, no hype words, no exclamation marks.
----- to here -----

And if a long chat starts forgetting the rules, open a new chat and paste the full prompt again. One chat per item keeps details from one listing leaking into the next.

Over the next couple of weeks we will send you a few short emails, each with one habit and one prompt you can use straight away.

The Well Listed team

P.S. The cheat sheet is the free taster of The Well Listed Kit. No need to think about that yet. Try the brief first.
~~~

---

## W2: The Listing Brief habit

- **Send:** day 1 (automation: wait 1 day after W1)
- **Subject:** The 2-minute habit behind every good listing
- **Alternative subject (for testing):** Why your AI listings keep inventing things
- **Preview text:** Give the AI facts, not guesses. Plus a prompt that asks the questions buyers will.

**Body:**

~~~text
Hi,

Generic AI listings go wrong for one reason: the AI is given too little, so it guesses. That is where the invented "100% wool", the wrong size and the "stunning vintage piece" come from.

The fix is the Listing Brief from your cheat sheet. A short block of facts about one item, filled in before you write a word.

Three habits make it work:

1. Have the item and a tape measure in front of you.
2. Write flaws as where, what, how big. "Pale mark on left cuff, about 5 mm" is perfect. "Minor wear" is not.
3. Leave blanks. A blank becomes a [CHECK] you can fix. A wrong line becomes a "not as described" return.

Today's prompt: once your brief is filled in, let the AI play the fussy buyer before a real one does.

----- copy from here -----
Here is a Listing Brief for an item I am selling on [PLATFORM] in the UK. Act as a careful, fussy buyer in this category.
1. List up to 8 questions a serious buyer would ask before buying, most important first.
2. For each, say whether my brief already answers it (Yes / No / Partly).
3. For every No or Partly, tell me exactly what to check or measure, and how.
4. Do not write the listing. Do not invent answers.
5. UK English, short lines.

My Listing Brief:
[PASTE YOUR LISTING BRIEF HERE]
----- to here -----

Add the answers to your brief, not just the listing, so every platform gets them. "Unsure" is a fair answer. A guess is not.

The Well Listed team

P.S. This is a shortened version of prompt B04 from The Well Listed Kit, which also has extra brief lines for clothing, children's clothing, electronics, books, homeware, toys and handmade: [GUMROAD_PRODUCT_LINK]
~~~

---

## W3: Condition notes that prevent "not as described"

- **Send:** day 3 (automation: wait 2 days after W2)
- **Subject:** "Minor wear" is how disputes start
- **Alternative subject (for testing):** How to describe flaws so buyers are not surprised
- **Preview text:** Location, type, size, photo. And a prompt that rewrites rushed flaw notes.

**Body:**

~~~text
Hi,

A "not as described" dispute often starts with a flaw the buyer did not expect. Not always a hidden one. Often just a vague one.

Compare:

Weak: Minor wear
Strong: Light rubbing on both heels, about 1 cm, see photo 5

Weak: Small mark
Strong: Pale grey mark on the front, below the left pocket, about 5 mm. May wash out, not tested

Every flaw gets four things: what it is, where it is, how big, and which photo shows it.

Two rules that save a lot of bother:
- If you are between two condition grades, pick the lower one. A buyer who gets better than expected is happy. A buyer who gets worse opens a case.
- The grade never replaces the flaw list. "Good" is an opinion. "Two small pulls on the back, about 3 mm each" is a fact.

Today's prompt, for when you have scribbled flaws in a hurry:

----- copy from here -----
Rewrite the flaws below so they are clear and specific for a UK [PLATFORM] listing. For each flaw, write one line with what it is, where it is (say "as worn"), how big (mm or cm) and which photo shows it, if I gave photo numbers.
Rules: UK English. Do not make any flaw sound smaller than I described it, and do not remove any. If size or location is missing, write [CHECK: ...]. No reassurance words like "perfect otherwise". Just facts.

My flaws, as I wrote them:
[PASTE FLAWS]
----- to here -----

Then fill every [CHECK] with a real measurement.

The Well Listed team

P.S. This is based on prompt D07 in The Well Listed Kit. The kit also has a condition grader that matches your grade to each platform's options: [GUMROAD_PRODUCT_LINK]
~~~

---

## W4: Pricing from sold comps you look up yourself

- **Send:** day 5 (automation: wait 2 days after W3)
- **Subject:** Do not ask the AI what your item is worth
- **Alternative subject (for testing):** A calmer way to price second-hand items
- **Preview text:** You find the sold prices. The AI does the maths.

**Body:**

~~~text
Hi,

Ask an AI tool "what is this worth?" and you get a confident guess. It does not know what your item sold for last week.

So split the job. You find the evidence. The AI does the sums.

1. Search for your item on the platform you are selling on. On eBay, turn on the "Sold items" filter. Elsewhere, look for items marked sold. An asking price is not a sold price.
2. Copy 5 to 10 close matches into your notes: title, sold price, postage, condition, date if shown. Same brand, similar size, similar condition beats lots of loose matches.
3. Paste them into this:

----- copy from here -----
Suggest a price for my item using only the sold listings I have found.

My Listing Brief (includes the lowest I will accept):
[PASTE YOUR LISTING BRIEF HERE]
Platform: [PLATFORM]
My sold comps:
[PASTE COMPS HERE]

Give me the sold price range from the good matches, the median, a suggested list price, a likely accepted price, and whether my floor is realistic.
Rules: UK English, pounds, show the sums. Use only the numbers I pasted. If I have fewer than three good matches, say the evidence is thin. Do not promise it will sell. Write ranges as "£10 to £14".
----- to here -----

Please copy comps by hand rather than using scraping tools or add-ons. Platform terms often do not allow them (check the current rules), and ten minutes of looking gives you better matches anyway.

Buyers set the final price. This just gives you a reason you can stand behind.

The Well Listed team

P.S. The kit's pricing module adds comp tidying, bundle pricing, price drops and fee and postage maths: [GUMROAD_PRODUCT_LINK]
~~~

---

## W5: Buyer messages (lowballers and "is this still available?")

- **Send:** day 7 (automation: wait 2 days after W4)
- **Subject:** "Is this still available?" (and the £3 offer on a £20 coat)
- **Alternative subject (for testing):** Two buyer replies you can reuse all week
- **Preview text:** Polite, short, on the platform. Two prompts for the messages that eat evenings.

**Body:**

~~~text
Hi,

Messages eat evenings. Here are two prompts for the most common ones.

First, a privacy habit: before you paste any buyer message into an AI tool, remove their name, username, address and order number. Replace them with [BUYER]. The AI does not need them.

For "Is this still available?":

----- copy from here -----
A buyer on [PLATFORM] has asked if my item is still available. Write a short, friendly reply.
My Listing Brief: [PASTE BRIEF]
Is it still available? [YES / NO]
When I can post: [E.G. NEXT WORKING DAY]
Rules: UK English, under 40 words, answer the question first. Add one useful fact and an easy next step using the platform's own tools. No fake urgency like "lots of interest" unless I have said it is true.
----- to here -----

For a lowball offer:

----- copy from here -----
A buyer on [PLATFORM] has offered much less than my price. My list price: £[AMOUNT]. Their offer: £[AMOUNT]. My floor: £[AMOUNT].
Write two replies under 50 words: a friendly counter-offer and a polite decline.
Rules: UK English, warm and calm, never sarcastic. Never go below my floor. Only give reasons I supply. Do not invent other buyers or deadlines. Suggest the platform's offer button for any counter.
----- to here -----

Plenty of people who send low offers are just trying their luck. A calm counter costs you nothing.

One firm rule: keep everything on the platform. If anyone asks to pay by bank transfer or chat on WhatsApp, the answer is no. It removes their protection and yours.

The Well Listed team

P.S. The kit has 12 message prompts, including returns, late parcels and "not as described": [GUMROAD_PRODUCT_LINK]
~~~

---

## W6: What is in the kit, and who it is not for

- **Send:** day 9 (automation: wait 2 days after W5)
- **Subject:** What is in the kit (and who should not buy it)
- **Alternative subject (for testing):** An honest look at The Well Listed Kit
- **Preview text:** Plus a prompt that strips the hype out of any AI description.

**Body:**

~~~text
Hi,

First, today's lesson. If you have an old listing, or one written by a generic AI tool, that says "gorgeous", "must have" or "color", paste it into this:

----- copy from here -----
Rewrite this listing description for a UK [PLATFORM] buyer. Change US spelling and words to UK (colour, trousers, jumper, trainers). Remove hype and filler (stunning, gorgeous, must have, exclamation marks, emoji). Remove or flag with [CHECK: ...] any claim not in my Listing Brief. Keep every flaw, with location and size. Then list what you removed and why.
Old description: [PASTE]
My Listing Brief: [PASTE]
----- to here -----

Now, the kit, since you have been getting these emails for a week and a bit.

The Well Listed Kit is 13 short modules and 90 prompts: all-in-one starter prompts for each platform, briefs, titles, descriptions and condition, keywords and item specifics, photos, pricing, buyer messages, video and TikTok Shop, a pre-post rule checker and a batch workflow. Plus fill-in templates (including 22 ready buyer replies), six worked examples, a platform cheatsheet, a PDF, and a prompt library with copy buttons that works on your phone. It works with the free versions of ChatGPT, Claude, Gemini or Copilot. It is [CURRENT_PRICE], one-off, no subscription, with a 30-day no-questions refund.

It is not for you if:
- You want a promise of more sales. We cannot make one, and nobody honestly can.
- You want software that lists for you. You still bring the item, the facts and the final check.
- You sell outside the UK. It is written for UK buyers, words and rules.
- You are happy with how your listings go now. Keep your money.

The Well Listed team

P.S. If it does sound useful: [GUMROAD_PRODUCT_LINK]
~~~

---

## W7: Last note in this series

- **Send:** day 12 (automation: wait 3 days after W6)
- **Subject:** Last one in this series (plus the check we run before posting)
- **Alternative subject (for testing):** A 1-minute check before you post anything
- **Preview text:** One last prompt, the refund promise, and an easy way to ask us anything.

**Body:**

~~~text
Hi,

This is the last email in the welcome series. One more lesson, then a couple of plain facts.

The lesson: check the finished listing against your brief before posting. AI drafts drift. A "wool blend" becomes "100% wool", a flaw quietly disappears. This catches it:

----- copy from here -----
Check my listing for accuracy against my Listing Brief. You are a careful proofreader, not a copywriter. Do not rewrite it.
Report: 1) anything in the listing that is not in the brief, 2) anything that differs from the brief, 3) any flaw that is missing or sounds milder, 4) anything misleading, 5) any American spellings or sizes.
Label each point Must fix, Should fix or Fine, and finish with "Ready to post" or "Fix first".
My Listing Brief: [PASTE]
My listing: [PASTE]
----- to here -----

Fix every Must fix, not just note it.

The plain facts:
- The Well Listed Kit is [CURRENT_PRICE], one payment, no subscription: [GUMROAD_PRODUCT_LINK]
- If it is not useful, ask for a refund within 30 days of buying by replying to this email or your Gumroad receipt, or emailing [BRAND_EMAIL]. No questions asked.
- We will not chase you with more sales emails from this series. You stay on the list for the occasional tip and update, and you can unsubscribe with the link at the bottom any time.

Got a question about a listing, a prompt, or whether the kit suits what you sell? Just hit reply. A real reply comes back from the Well Listed team (please leave out buyers' names and order details).

Thanks for reading these.

The Well Listed team
~~~
