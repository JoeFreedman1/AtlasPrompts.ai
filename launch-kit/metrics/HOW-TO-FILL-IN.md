# How to fill in the daily metrics

**Takes about 5 minutes a day.** Each morning, add one row for **yesterday** to a file called `metrics/YYYY-MM.csv` (for example `metrics/2026-10.csv`). Copy the header row from `template.csv` the first time. Leave a box empty if you do not have that number yet (for example, no ads running). Never write passwords or card details in these files.

The easiest way on a phone: open the CSV in the GitHub app or website, tap edit, paste a new line at the bottom, and commit. Or type the numbers into a message to Claude and say "add these to today's metrics".

| Column | What it means | Where to find it |
|---|---|---|
| `date` | The day the numbers are for (yesterday), as YYYY-MM-DD | |
| `sales_count` | Number of kits sold | Gumroad: Dashboard, or Analytics, set to "Yesterday" |
| `revenue_gbp` | Money taken before fees, in £ | Gumroad Analytics (sales total) |
| `refunds_count` | Refunds issued | Gumroad: Sales, filter "Refunded" |
| `checkout_page_views` | Views of the Gumroad product page | Gumroad Analytics, "Views" |
| `site_visitors` | Visitors to the sales page | Your free site analytics (see note below). Leave blank if none set up |
| `email_signups_today` | New subscribers from the free cheat sheet | MailerLite: Subscribers, or the form's stats |
| `email_subscribers_total` | Total active subscribers | MailerLite dashboard |
| `tiktok_views` | Total video views yesterday | TikTok app: Profile, menu, TikTok Studio (or Business Suite), Analytics, Overview, set to yesterday. Analytics must be switched on with a Business account |
| `tiktok_profile_views` | People who visited the profile | Same TikTok Analytics screen |
| `tiktok_followers` | Follower total | TikTok profile |
| `instagram_views` | Views across Reels and posts yesterday | Instagram: Professional dashboard, Insights |
| `instagram_followers` | Follower total | Instagram profile |
| `youtube_shorts_views` | Shorts views yesterday | YouTube Studio app, Analytics, Content, Shorts |
| `pinterest_impressions` | Times pins were seen | Pinterest business account: Analytics, Overview |
| `pinterest_outbound_clicks` | Clicks from pins to our site | Same Pinterest screen |
| `link_in_bio_clicks` | Clicks on the bio link | Your link tool's stats (e.g. Linktree free, or TikTok's own bio link clicks in Analytics) |
| `etsy_views` | Views of the Etsy listing (if listed) | Etsy: Shop Manager, Stats |
| `etsy_sales` | Etsy orders | Etsy: Shop Manager, Orders |
| `ad_platform` | `tiktok`, `meta`, or blank | |
| `ad_spend_gbp` | Money spent on ads yesterday | TikTok Ads Manager or Meta Ads Manager, set to yesterday |
| `ad_impressions` | Times ads were shown | Same |
| `ad_clicks` | Link clicks on ads | Same ("Link clicks", not "all clicks") |
| `ad_landing_page_views` | People who actually loaded the page | Meta: "Landing page views". TikTok: leave blank unless tracking is set up |
| `ad_purchases` | Sales you can match to ads | Use a Gumroad discount code or separate product link only used in ads, and count sales that used it |
| `notes` | Anything unusual: a post that took off, a price change, a platform outage | |

**If you run ads on both TikTok and Meta on the same day**, add two rows with the same date, one per platform, and put the non-ad numbers only on the first row.

**Free site analytics:** Netlify's own analytics is a paid add-on. Free options are Cloudflare Web Analytics or GoatCounter (both need a free account, which you create yourself, then paste their small tracking snippet where the sales page says `<!-- ANALYTICS SNIPPET -->`). This is optional in week 1: Gumroad views and email sign-ups are enough to start.
