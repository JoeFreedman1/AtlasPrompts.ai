# The £5 a day ad test: plain English plan

This is a small, careful test, not a growth plan. Its only job is to answer one question: **can £5 a day of ads bring email sign-ups or sales for less than a sale is worth to us?** The ads are in `ads.md` (A01 to A20). The decision numbers come from `STOP-KEEP-SCALE.md` and are copied exactly below.

Everything here is planning, not a forecast. Ads can lose money, and a brand-new account often gets nothing from them in the first fortnight. That is normal and is why the budget is capped.

---

## 1. Before you start: the owner must do these

**Only the owner can set up the ad accounts.** The daily operator (or any AI helper) must never create an ad account, enter card details or accept terms on the owner's behalf.

1. **Create the ad account yourself**, using the brand email (not a personal one where you can avoid it):
   - Meta: create a Facebook Page for Well Listed (if you have not already), then open Meta Business Suite and Ads Manager and follow the set-up steps. Meta needs a personal Facebook profile behind the Page to log in; the profile is never shown on the ads.
   - TikTok: go to TikTok Ads Manager (ads.tiktok.com) and sign up as a business with the brand email.
2. **Enter the payment details yourself.** Use a card you control. Set a **spending limit** in the billing settings if the platform offers one (Meta calls it an "account spending limit"). Set it to £70 for the first test.
3. **Check whether VAT is added** to your ad spend in the billing settings. The £5 a day in this plan is the budget you set in Ads Manager; any VAT is on top.
4. **Check the minimum daily budget** in Ads Manager when you create the campaign. We could not verify the current UK minimums overnight (see `research/tools-and-fees.md`). What we found:
   - **Meta:** commonly reported as a low daily minimum (around £1 a day for some goals, higher for others). £5 a day should be allowed, but check.
   - **TikTok:** historically quoted as around $50 a day per campaign and $20 a day per ad group (with local currency equivalents). If that is still true, **a £5 a day test is not possible in TikTok Ads Manager.** If Ads Manager will not accept £5, do not raise the budget. Either test Meta only, or use TikTok's in-app **Promote** feature on an existing organic post (it has its own, lower minimum: check in the app) and treat it as the TikTok test.
5. **Read and accept** each platform's advertising policies yourself. Our ads are written to follow them, but you are the advertiser.

---

## 2. When to start

Do **not** start ads until all of these are true:

- [ ] The sales page is live and works on a phone (buy button opens Gumroad).
- [ ] The cheat sheet sign-up works: you signed up with a spare email and the cheat sheet arrived.
- [ ] The welcome emails are sending.
- [ ] You have posted organically for at least 14 days, so the brand's profile does not look empty when people tap through.

**Recommended start:**

- **Day 15 onwards (full price £19):** the main test. Kit ads and cheat sheet ads are both allowed.
- **Earlier (days 1 to 14) is allowed only for cheat sheet ads**, which drive to the free sign-up. Do not run kit ads at the £12 launch price: at about £9.86 kept per sale, there is very little room to pay for ads, and the launch price ending would make the ad wrong halfway through the test.

---

## 3. One platform at a time

Run **one platform per 14-day test**. Two platforms at £2.50 a day each gives too little data on both.

- **Start with Meta** (Facebook and Instagram) because the low minimum budget makes £5 a day workable.
- **Then TikTok** in a later fortnight, only if the budget minimum allows £5 a day or you use Promote (see section 1).

---

## 4. How to build it in Ads Manager

Ads Manager has three levels. Think of it as a box, inside a box, inside a box.

| Level | What it is | What to set |
|---|---|---|
| **Campaign** | The goal | Meta: objective **Traffic**. TikTok: objective **Traffic**. Name it `WL test 01 Meta` (or `WL test 01 TikTok`). Turn off any "campaign budget" option; set the budget at the next level instead |
| **Ad set** (TikTok: **ad group**) | Who sees it, where, and the money | One ad set only. Budget **£5 a day** (daily budget, not lifetime). Location: **United Kingdom**. Age: **18 and over** (no upper limit). Gender: all. Detailed targeting and interests: **none** (broad). Language: English. Placements: automatic (Meta: Advantage+ placements). Optimise for: **Landing page views** (if not offered, choose **Link clicks**). Name it `UK 18+ broad` |
| **Ad** | The thing people see | **3 or 4 ads** inside the one ad set, each named with its ID from `ads.md`, e.g. `A12 time kit` |

**Why broad targeting?** With £5 a day, narrow interests make ads more expensive and give the platform too little room to find people. Leave it broad and let the ad itself (UK sellers, eBay, Vinted) attract the right people. Never target by anything personal (financial situation, health and so on): the platforms do not allow it for most ads and it is not what we want.

### How to split £5 a day across 3 or 4 ads

- Put all 3 or 4 ads **in the same ad set** with the single £5 daily budget. The platform shares the £5 between them and quietly moves more money to the ad it thinks is working. That is fine and expected.
- **Do not split into separate ad sets of £1.25 each.** Each would get too few impressions to judge.
- Pick a mix. For the first Meta test we suggest 4 ads: **A12** (time, kit), **A20** (accuracy, kit), **A13** (UK-specific, cheat sheet), **A15** (checklist, cheat sheet). For TikTok: **A02**, **A10**, **A05**, **A08**.
- If, after 4 days, one ad has had almost no spend (under £1), the platform has already decided it likes the others less. Leave it; you can retest it in a future fortnight.
- **Never edit a running ad.** Editing text, image or link resets its learning. To change something, turn the ad off and add a new one.

---

## 5. How to track sales and sign-ups per platform

The ads platforms often cannot see Gumroad sales by themselves. We track them on Gumroad's side with a separate link or code **per platform**.

### Kit ads: a separate Gumroad link or code for each platform

Use **one** of these (option A is best if it works):

- **Option A: a tagged link.** Add a tag to the end of the Gumroad product link, one per platform and ad, for example:
  - Meta: `https://[your-gumroad-link]?utm_source=meta&utm_medium=paid&utm_content=A12`
  - TikTok: `https://[your-gumroad-link]?utm_source=tiktok&utm_medium=paid&utm_content=A02`
  Then check that the sale shows its source in Gumroad's analytics or sales list (look for "referrer" or "UTM" in the Gumroad dashboard). **Test this first** with a spare purchase you then refund, or check Gumroad's help pages, because we could not verify how Gumroad shows these tags.
- **Option B: a discount code per platform.** In Gumroad, create a discount (offer) code used only in that platform's ads, for example `META2` (£2 off) and `TIKTOK2` (£2 off). Mention the code in the ad's on-screen text or primary text. Every sale that uses the code came from that platform. Note: the code lowers the money kept per sale by the discount, so the SCALE numbers get a little harder to reach. Keep the discount small and genuine (no fake "was" prices).

Write down each link or code in `metrics/` so the daily operator can match sales to platforms.

### Cheat sheet ads: count sign-ups per platform

- In MailerLite, make a copy of the cheat sheet sign-up form or landing page for each platform (for example "Cheat sheet: Meta ads"), which adds people to the same "Cheat sheet" group **plus** a second group called "Source: Meta ads". Check that your MailerLite plan includes this.
- Point the cheat sheet ads at that copy. The number of people in "Source: Meta ads" is your ad sign-ups.
- Cost per email sign-up = amount spent on the cheat sheet ads divided by sign-ups in that group.

### Landing page views

"Landing page views" in Meta and TikTok need the platform's tracking pixel on the destination page. Gumroad has a setting for a Facebook (Meta) pixel ID (check the current settings page). Our Netlify site does not have a pixel unless one is added. **If the "Landing page views" column is empty, use "Cost per link click" in its place** for the £0.80 rule. It is a slightly kinder number than the real cost per landing page view, so treat a borderline result as a STOP.

---

## 6. The 14-day schedule

| Day of test | What to do | Time |
|---|---|---|
| **Day 0** (the day before) | Owner creates the ad account, adds payment, sets the £70 spending limit. Make the 3 or 4 ads in Canva or CapCut. Set up the tracking links or codes and the MailerLite source group. Build campaign, ad set and ads, and submit for review | 1 to 2 hours |
| **Day 1** | Ads go live after review. Check each ad is "Active" (not "Rejected"). If one is rejected, read the reason, fix it in a **new** ad, do not argue with the wording in the ad itself | 10 min |
| **Days 2 to 3** | Hands off. Check once a day that spend is around £5 and nothing is rejected. Do not change anything: the platform is learning | 5 min a day |
| **Day 4** | First look. Open the columns in section 7. Any ad with **at least £5 spent and 1,000 impressions** can be judged against the STOP rules. Turn off any STOP ad and add the next untested variation from `ads.md` in its place (same angle mix if you can) | 20 min |
| **Days 5 to 6** | Hands off. Daily 5-minute check | 5 min a day |
| **Day 7** | Weekly review. Judge every ad that has at least £5 spent and 1,000 impressions. STOP, KEEP or SCALE each one. Check Gumroad and MailerLite for sales and sign-ups from this platform. Write the numbers in `metrics/` | 30 min |
| **Days 8 to 9** | Hands off. Daily check | 5 min a day |
| **Day 10** | Judge any new ads added on day 4 or day 7 that have reached the minimum. Apply SCALE only if the rule is met (and at most one budget rise every 3 days) | 20 min |
| **Days 11 to 13** | Hands off. Daily check. Check the running total: stop at £70 | 5 min a day |
| **Day 14** | Final review. Apply the "stop everything" rule. Decide: run a second fortnight on the same platform with the winners, try the other platform, or pause ads and fix the offer and organic content. Write the decision and the reason in `metrics/` | 30 min |

**Daily check (5 minutes):** spend today is about £5; total spend is under the cap; no ad is rejected; sales and sign-ups logged.

---

## 7. STOP, KEEP or SCALE (copied exactly from STOP-KEEP-SCALE.md)

Each ad must have **at least £5 spent and 1,000 impressions** before you judge it.

| Label | Rule | Action |
|---|---|---|
| **STOP** an ad | Link click-through rate under **0.8%** after 1,000 impressions, **or** cost per landing page view over **£0.80** after £5 spend, **or** £20 spent with 0 sales and fewer than 5 email sign-ups | Turn the ad off. Replace it with the next untested variation |
| **KEEP** an ad | Link click-through rate **0.8% or more** and cost per landing page view **£0.80 or less**, or cost per email sign-up **£1.50 or less** | Leave it running unchanged. Do not edit a running ad (it resets learning) |
| **SCALE** an ad | Cost per sale **£8 or less** at full price (**£6 or less** at launch price) across **at least 3 sales in 7 days** | Raise its daily budget by **20%**, no more than once every 3 days, and never more than double in a week |

**Stop everything** if £70 has been spent (14 days at £5) with zero sales: pause ads, and fix the offer and organic content first. Ads amplify something that already works; they rarely fix something that does not.

**Hard cap:** never spend more than the "ad budget cap" written in STATE.md without the owner changing it. Starting cap: £5 a day, £70 per fortnight.

For reference, money kept per sale after fees (from `MONEY.md`): about **£9.86 at £12** and about **£15.95 at £19**. The SCALE thresholds (£6 and £8) leave room for profit under those.

**A note on SCALE with one ad set:** the budget sits on the ad set, not the ad. If one ad meets the SCALE rule, turn off the weaker ads in that ad set and raise the ad set budget by 20% (for example £5 to £6), or duplicate the winning ad into its own new ad set at £6 a day. Any budget rise needs the owner to raise the cap in STATE.md first.

### Where to find each number

Set up a saved column view once, then use it every time.

**Meta Ads Manager** (ads.facebook.com or business.facebook.com, then Ads Manager): click the **Ads** tab so you see one row per ad. Click **Columns**, then **Customise columns**, tick the items below, and save the view as "WL test".

| Number we need | Column name in Meta | Notes |
|---|---|---|
| Amount spent | **Amount spent** | Per ad, for the date range at the top right. Set the date range to "Maximum" or the test dates |
| Impressions | **Impressions** | Times the ad was shown |
| Link click-through rate | **CTR (link click-through rate)** | Not "CTR (all)", which counts any click |
| Cost per landing page view | **Cost per landing page view** | Needs a pixel. If blank, use **CPC (cost per link click)** instead |
| Sales | Gumroad (your tracking link or code) | Count sales for this platform, and by ad if the tag shows `utm_content` |
| Cost per sale | Work it out: amount spent divided by sales | Use the same dates for both |
| Email sign-ups | MailerLite: people in "Source: Meta ads" | For cheat sheet ads |
| Cost per email sign-up | Work it out: amount spent on cheat sheet ads divided by sign-ups | |

**TikTok Ads Manager** (ads.tiktok.com): go to **Campaign**, then the **Ad** tab for one row per ad. Click **Custom columns** and add the items below; save as "WL test".

| Number we need | Column name in TikTok | Notes |
|---|---|---|
| Amount spent | **Cost** | |
| Impressions | **Impressions** | |
| Link click-through rate | **CTR (destination)** | TikTok may label it "CTR (destination)" or just "CTR". Use the one based on clicks to your link, not all clicks |
| Cost per landing page view | **Cost per landing page view** (if the pixel is set up) | If blank, use **CPC (destination)** |
| Sales | Gumroad (your TikTok link or code) | |
| Cost per sale | Amount spent divided by sales | |
| Email sign-ups | MailerLite: people in "Source: TikTok ads" | |

Column names change from time to time. If you cannot find one, search for it inside the column picker.

**If you are using TikTok Promote instead:** open the promoted post in the TikTok app, tap **View data** or **Promote** results. It shows spend, views and link clicks. Work out CTR as link clicks divided by views, and cost per link click as spend divided by link clicks.

---

## 8. Common mistakes to avoid

- Editing a running ad (resets learning). Turn it off and make a new one.
- Judging an ad before it has £5 spent and 1,000 impressions.
- Adding interests to "help". Keep it broad.
- Raising the budget to hit a platform minimum. If £5 is not allowed, test elsewhere.
- Running kit ads at the £12 launch price.
- Letting the budget run past £70 without the owner's say-so.
- Boosting a post that contains anything the ad rules in `ads.md` forbid (income talk, fake screens, logos).
