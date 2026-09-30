# Quality checklist (the Phase 8 standard)

Every new piece of content, from any session or subagent, passes this before it is used. Review it as a sceptical marketing director who has seen a thousand "AI side hustle" accounts and is tired of all of them.

## 1. Run the automatic check
`python3 launch-kit/tools/check_content.py` must report **0 problems**. It catches em and en dashes, possible owner identifiers, real-looking email addresses, income claims, fake-review patterns, hype words and American spellings. Warnings are allowed only when deliberate (for example, a post showing "sweater" as a word to avoid).

## 2. Then check by eye
**Identity and faceless**
- [ ] Nothing names, shows or hints at the owner (name, face, voice, handwriting, home, pets, car, area, personal handles, personal email).
- [ ] Screen recordings: no account names, profile pictures, notifications, bookmarks or tabs visible.
- [ ] Works as text on screen, screen recording, stock footage without a face, graphics or AI voiceover.

**Honesty and compliance**
- [ ] No income claims or implied earnings ("make money", "£X a week", "quit your job", "sell more guaranteed").
- [ ] No invented statistics, reviews, testimonials, sales numbers, follower counts, or "our customers say".
- [ ] Every example item, price and message is invented and labelled as an example where it could be mistaken for real.
- [ ] No fake urgency or scarcity. Launch price deadline is real and matches STATE.md.
- [ ] Platform facts match `research/platform-rules-uk.md`, with "check the current rule" where it is not verified.
- [ ] Nothing encourages breaking platform rules (keyword stuffing, off-platform payment, misleading photos, replica or "inspired by" wording, review manipulation).
- [ ] No implied affiliation with eBay, Vinted, Depop, Etsy, Amazon, TikTok or OpenAI. No marketplace logos.
- [ ] Legal topics say "general information, not legal advice".
- [ ] No tax rules, thresholds or HMRC figures anywhere: tax questions only point to gov.uk or an accountant.
- [ ] Affiliate and creator content is disclosed (#ad or "affiliate link").

**Craft**
- [ ] Specific, not generic: a real, concrete example in every post (an item, a before and after, a number from the rules).
- [ ] The hook would stop a UK reseller scrolling, and is not a cliché ("You won't believe", "Stop scrolling", "Here's the secret").
- [ ] Not repetitive: compare with the last 10 posts. Different hook shape, different opening word, different example item.
- [ ] Not salesy: most posts teach; only about 1 in 4 mention the paid kit, softly.
- [ ] UK English throughout (trousers, jumper, postage, colour, £). Plain words. Short sentences.
- [ ] Brand voice: calm, practical, dry British warmth. Banned words absent.
