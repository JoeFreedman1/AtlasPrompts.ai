# Product spec: The Well Listed Kit

Internal build spec (not shipped to buyers).

## Promise
Paste in your item's details and get a UK-ready listing, a price check and polite buyer replies, using the free AI tools you already have. Honest, accurate, platform-appropriate copy. We never promise more sales or income.

## Buyer
UK side-business resellers (Vinted, eBay, Depop), small brand owners and crafters (Etsy, Amazon, TikTok Shop), declutterers turning pro. Non-technical, on mobile, time-poor, price-sensitive.

## Core idea: the Listing Brief method
Generic AI output is bad because the input is bad. Every prompt in the kit starts from a **Listing Brief**: a short fill-in block of facts about the item (what it is, brand, size, measurements, colour, material, condition and flaws, what is included, platform, postage, price floor). The AI is told to only use facts from the brief and to write "[CHECK: ...]" where information is missing instead of inventing it. This one habit is the product's big difference from generic packs.

## Prompt format (use exactly this in every module)

```
### [ID] Prompt name
**Use it when:** one line.
**Paste this:**
```text
(the prompt, with [SQUARE BRACKET PLACEHOLDERS] in capitals)
```
**What good output looks like:** a short worked example output for an invented example item.
**Check before you post:** 2 to 4 bullet points.
```

IDs: B = brief, T = titles, D = descriptions and condition, K = keywords, tags and item specifics, P = photos, R = pricing, M = buyer messages, V = video and TikTok Shop, C = rule checker, W = workflow and batch.

## Quality bar
- Around 70 to 80 prompts in total, each genuinely different and useful. Quality over quantity.
- Every prompt works in free ChatGPT, Claude, Gemini or Copilot (no plugins, no browsing assumed, no paid features).
- Every prompt tells the AI: UK English, no invented details, respect the platform's limits, no hype words, no misleading claims.
- Worked examples use invented items (e.g. "grey Next wool-blend jumper, size 12, small bobbling under arms").
- Buyer message prompts must respect UK consumer law and platform rules (no off-platform payment, no pressuring for feedback, no refusing legal rights).
- Pricing prompts work from sold listings the seller looks up and pastes in themselves (no scraping, no automation).
- Plain English for non-technical sellers. Short paragraphs. Mobile-friendly.
- UK English. NEVER em dashes or en dashes.

## Files (markdown in product/source/)
- 00-start-here.md : welcome, what is inside, how to use in 5 minutes, choosing a free AI tool, privacy tips (do not paste buyers' personal data into AI tools), the Listing Brief method, the golden rules.
- 01-listing-brief.md : the master Listing Brief template (general plus variants for clothing, electronics, books/media, homeware, toys/collectables, handmade), and B prompts that turn messy notes, a voice-note transcript, or a photo description into a brief.
- 02-titles.md : T prompts per platform (eBay UK, Vinted, Depop, Etsy, Amazon UK, TikTok Shop), title formula tables, how to test titles.
- 03-descriptions-condition.md : D prompts per platform, honest condition grading scale, flaw disclosure wording, measurements, bundles.
- 04-keywords-tags-specifics.md : K prompts for eBay item specifics, Etsy 13 tags, Depop/Vinted hashtags and search terms, Amazon backend search terms, avoiding keyword stuffing.
- 05-photos.md : P prompts: shot lists per category, flaw photo checklist, backgrounds, photo captions, alt text; rules on not using misleading AI-edited photos.
- 06-pricing.md : R prompts: price from pasted sold comps, bundle pricing, offer strategy, price-drop plan, fee and postage maths.
- 07-buyer-messages.md : M prompts and ready replies: availability, lowball offers, bundle requests, postage questions, delays, returns (private vs trader), item not as described, damaged in post, feedback, difficult buyers.
- 08-video-and-tiktok-shop.md : V prompts: faceless product video scripts, TikTok Shop product titles and descriptions, live selling run-sheet, UGC-free product showcase ideas.
- 09-rule-checker.md : C prompts: pre-post compliance and accuracy check for each platform; banned claims; trademark and counterfeit wording; UK consumer law basics.
- 10-batch-workflow.md : W prompts: list 10 items in one chat session, spreadsheet/CSV output for bulk tools, weekly listing routine, repurpose one listing across platforms.
- 11-worked-examples.md : 6 full before/after examples end to end (brief, title, description, tags, price reasoning, one buyer reply).
- 12-platform-cheatsheet.md : one-page table per platform with limits and rules (from research/platform-rules-uk.md), with "last checked" date and links.

## Templates (product/templates/)
- listing-brief-template.csv, listing-brief-template.txt
- stock-and-pricing-tracker.csv
- message-snippets.txt
- photo-shot-lists.md

## Built outputs (product/dist/)
- Well-Listed-Kit.pdf (full guide)
- prompt-library.html (searchable, copy buttons, works offline)
- all-prompts.txt
