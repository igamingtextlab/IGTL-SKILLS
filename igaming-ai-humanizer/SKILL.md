---
name: igaming-ai-humanizer
description: Rewrites or generates iGaming/casino/betting marketing copy (site content, reviews, bonus pages, landing pages, blog posts) so it avoids the lexical, grammatical, structural, and statistical patterns that make text read as AI-generated. Use this skill any time the user asks to "make this sound less AI", "de-AI this text", "humanize this copy", "remove AI markers", "this text smells like GPT/ChatGPT/Claude", asks to write casino/betting/slot review copy from scratch that reads naturally rather than templated, or pastes iGaming marketing text and asks for a rewrite/edit/polish. Also trigger when the user mentions AI detectors, Pangram, Originality.ai, GPTZero, or asks why their content is being flagged as AI-written.
---

# iGaming AI-Humanizer

## Mode A — edit existing text

1. Read the full text.
2. Flag matches against `references/en-markers.md`, `references/ru-markers.md`,
   `references/igaming-lexicon.md` (pick by the text's language). A match is a
   starting point for review, not an automatic rewrite — the words in those
   lists are not banned outright. Judge each occurrence in context: revise it
   when it's an evaluative claim with no factual support, a generic phrase
   that doesn't explain a specific feature or benefit, a repetition of
   information already stated, or wording that doesn't fit the task or
   tone. Leave it as-is when it conveys a concrete fact or accurately
   describes a function — its presence on a list is not by itself a reason
   to change it (e.g. "offers withdrawals in euros" states a real feature
   and stays; "offers an incredible gaming experience" is an unsupported
   claim and gets revised or cut).
3. Where a rewrite is warranted, replace it with a concrete product fact
   (number, condition, mechanic) — never a synonym swap. Use only facts
   already given by the user or present in the source material. If no such
   fact is available, ask the user for one or drop the unsupported claim —
   never invent a fact to fill the gap.
4. Preserve every material fact and condition from the source text as you
   edit: amounts, currencies, percentages, deadlines, wagering requirements,
   minimum deposits, maximum payouts, eligibility requirements, GEOs, and
   qualifiers that change meaning ("up to", "only", "except", "provided
   that", etc.), plus any links, required-verbatim keyword phrases, or
   mandatory structure from the brief. Rewording is fine; dropping or
   softening a condition is not — "a €500 bonus for players" is not an
   acceptable rewrite of "a bonus of up to €500, with a 40x wagering
   requirement within 7 days, for new players from Germany only". If the
   source material is contradictory or unclear about a condition, don't
   guess — ask.
5. Break mechanical structure and rhythm per `references/structure-and-rhythm.md`.
6. Run `references/self-check-checklist.md`.

## Mode B — write from scratch

1. Hold `references/master-prompt.md` in mind for the entire generation.
2. Write with natural, varied rhythm from the first sentence — no clichés from
   `references/*-markers.md` or `references/igaming-lexicon.md`, no listicles,
   no forced symmetry between items.
3. Insert product specifics (RTP, volatility, bonus terms, numbers, provider
   names) instead of evaluative adjectives, using only facts the user provided.
4. Keep every material fact and condition the user provided intact — see
   point 4 of Mode A for what counts as material. If the brief's conditions
   are contradictory or incomplete, ask rather than guess.
5. Run `references/self-check-checklist.md`.

## Replacement principle

Never swap a cliché for a synonym from the same semantic field — replace it
with a fact, and only a fact you actually have.

| Cliché | Replacement (example — use real data, not this one) |
|---|---|
| "offers a seamless gaming experience" | "loads in under 2 seconds on mobile, no lag on spins" |
| "generous bonus" | "100% match up to $500 + 50 free spins on Book of Dead" |
| "wide range of games" | "4,000+ slots from 60+ providers, including Pragmatic Play and NetEnt" |
| «предлагает уникальные функции» | «добавляет мультипликатор x2 при каждом третьем спине без выигрыша» |

No data for a fact? Ask the user for it — never fill the gap with a generic
phrase or a made-up number.

## Resources

- `references/en-markers.md` — English words/phrases/structural patterns
- `references/igaming-lexicon.md` — iGaming lexicon + 10 cliché categories
- `references/ru-markers.md` — Russian-language lexicon, grammar, syntax
  (kept in Russian — these are Russian-language markers)
- `references/structure-and-rhythm.md` — rhythm, punctuation, composition
- `references/master-prompt.md` — standalone prompt block
- `references/self-check-checklist.md` — final pass

## Output format

Return only the complete finished text — no introduction, no change report,
no explanation, no reference to internal checks, whether writing or editing.
If something is genuinely ambiguous or a needed fact is missing, ask for it
before producing the final text, rather than guessing and flagging it after.
