# Sales site: how it works

The site is live-ready at `https://well-listed.netlify.app`. It collects **no personal data**: there is no sign-up form, the free cheat sheet is a direct download, and every sale goes through Gumroad as merchant of record. **No personal details of the owner appear anywhere in the site or repo.**

## Files
| File | What it is |
|---|---|
| `version-a.html` | Sales page, angle A (accuracy and control). The live home page |
| `version-b.html` | Sales page, angle B (time back). Published at `/b/` for testing, hidden from Google |
| `privacy.html` | Privacy notice: the site collects no personal data; purchases are handled by Gumroad under Gumroad's privacy policy |
| `terms.html` | Terms of sale: sales through Gumroad as merchant of record, 30-day refund, digital download cancellation wording |
| `lead-magnet/uk-listing-cheat-sheet.md` | The free cheat sheet; the build turns it into `/free/uk-listing-cheat-sheet.pdf` and a web version |
| `placeholders.json` | The values filled into the pages (Gumroad link, brand email, launch date, site address, which version is live) |
| `brand-assets/` | Logo and Gumroad cover images (not deployed) |
| `netlify-site/` | The built site that Netlify publishes. Never edit it by hand |

## Making a change
1. Edit the source files above (or `placeholders.json`), or ask Claude to.
2. Run `python3 launch-kit/tools/build_site.py`. It fills the values in, works out the launch end date from `launch_date` (day 14 = launch date plus 13 days), adds the blog and the cheat sheet, and rebuilds `netlify-site/`.
3. Commit and push to `main`. Netlify is connected to the repo and redeploys by itself, but only when something inside `netlify-site/` has changed (see `netlify.toml` at the repo root). Each deploy uses Netlify credits, so batch changes into one push.

## Values in `placeholders.json`
| Key | Current value |
|---|---|
| `GUMROAD_PRODUCT_LINK` | `https://welllisted.gumroad.com/l/well-listed-kit` (every buy button) |
| `BRAND_EMAIL` | `hello.welllisted@gmail.com` |
| `launch_date` | `2026-09-30` (the £12 price ends at 11:59pm on 13 October 2026) |
| `site_url` | `https://well-listed.netlify.app` |
| `live_version` | `A` |

## Day 15 (14 October 2026)
Change the Gumroad price to £19 after 11:59pm on 13 October, then ask Claude to switch both sales pages to £19 and push. Netlify redeploys automatically.

## Switching A and B
Set `live_version` to `"B"`, rebuild and push. Run each version for a full week and compare Gumroad's views to sales.
