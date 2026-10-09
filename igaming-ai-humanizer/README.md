<p align="center">
  <img src="https://igamingtextlab.com/assets/Logo%20Header.svg" width="220" alt="iGamingTextLab" />
</p>

<h1 align="center">iGaming AI Humanizer</h1>

<p align="center">
  A free Claude skill that rewrites or writes iGaming copy without the patterns that make text read as AI-generated. English and Russian.<br/>
  By <a href="https://igamingtextlab.com/?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=humanizer-header">iGamingTextLab</a>
</p>

<p align="center">
  <a href="https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-ai-humanizer.skill">
    <img src="https://img.shields.io/badge/%E2%AC%87%20Download%20the%20skill-iGamingTextLab--ai--humanizer.skill-black?style=for-the-badge" alt="Download iGamingTextLab-ai-humanizer.skill" />
  </a>
</p>

<p align="center">
  <b><a href="https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-ai-humanizer.skill">Download iGamingTextLab-ai-humanizer.skill</a></b>
  · open it in Claude · click <b>Save skill</b>
</p>

> 🎁 **Get $40 in free credit** to test iGamingTextLab services — a live editor reviews your text or writes new copy from your brief.
> [Register at client.igamingtextlab.com →](https://client.igamingtextlab.com/haai-register?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=humanizer-cta)

## What it's for

- Casino, slot and sportsbook reviews
- Bonus pages and landing pages
- Site content and blog posts

Works in two modes: **edit** a text you already have, or **write** a new one
from your brief. English and Russian copy.

The skill removes lexical, grammatical, structural and statistical AI
patterns, plus the iGaming filler every casino site is drowning in
("seamless experience", "unbeatable bonus", "wide range of games").

## Installation

You need a Claude plan with skills (Free, Pro, Max, Team or Enterprise) and code execution turned on.

1. Turn on **Code execution and file creation** in **Settings → Capabilities**. On Team and Enterprise plans, an owner enables "Code execution and file creation" and "Skills" in **Organization settings → Plugins & skills** (Policy tab).
2. [Download `iGamingTextLab-ai-humanizer.skill`](https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-ai-humanizer.skill).
3. Open the file in Claude (desktop or web) and click **Save skill**.
   Or upload it manually: **Customize → Skills → + → Create skill → Upload a skill**. Upload the file as is, don't unzip it.
4. Check that the skill's toggle is on.

No skills on your plan? Open
[`references/master-prompt.md`](references/master-prompt.md) — a
self-contained prompt block you can paste into any Claude conversation or
your own content generator.

## How to use

Claude picks the skill automatically when you ask it to de-AI, humanize or
polish iGaming copy. To make sure it's used, name it in your prompt:
"Use the igaming-ai-humanizer skill…".

Give Claude the facts you have: RTP, volatility, providers, bonus terms,
limits. The skill replaces vague claims with these facts, so the more you
provide, the more specific the text.

**Example prompts**

```
Use igaming-ai-humanizer. This bonus page reads like ChatGPT. Rewrite it and keep every bonus condition: [text]
```

```
Use igaming-ai-humanizer. Write a 1,000-word review of the slot [name]. Facts: RTP 96.2%, high volatility, provider [name], max win 5,000x.
```

```
Use igaming-ai-humanizer. Перепиши этот текст для лендинга казино, чтобы он не звучал как ИИ: [текст]
```

## What you get

- Only the finished text — no introduction, change report or list of checks.
- Every material fact and condition kept: amounts, currencies, percentages,
  deadlines, wagering, minimum deposits, eligibility, GEOs, and qualifiers
  like "up to" or "only". Rewording is fine; dropping a condition is not.
- If a needed fact is missing or the brief contradicts itself, Claude asks
  before writing instead of guessing.

## What's inside

```
igaming-ai-humanizer/
├── SKILL.md                      # entry point, two modes: edit / write from scratch
└── references/
    ├── en-markers.md             # English AI-text markers
    ├── igaming-lexicon.md        # iGaming-specific clichés, 10 categories
    ├── ru-markers.md             # Russian-language markers
    ├── structure-and-rhythm.md   # rhythm, punctuation, composition rules
    ├── master-prompt.md          # standalone prompt block — usable on its own
    └── self-check-checklist.md   # final pass before output
```

### Replacement principle

A cliché is never swapped for a synonym — it's replaced with a fact, and only
a fact you actually provided.

| Cliché | Replacement (example) |
|---|---|
| "offers a seamless gaming experience" | "loads in under 2 seconds on mobile, no lag on spins" |
| "generous bonus" | "100% match up to $500 + 50 free spins on Book of Dead" |
| "wide range of games" | "4,000+ slots from 60+ providers, including Pragmatic Play and NetEnt" |

Words on the marker lists aren't banned outright. A phrase that states a real
feature stays ("offers withdrawals in euros"); an unsupported claim is revised
or cut ("offers an incredible gaming experience").

## Keep in mind

- The skill doesn't invent facts, numbers, reviews or sources.
- It changes how the text reads; it doesn't guarantee any AI-detector score.

## About iGamingTextLab

iGamingTextLab is an iGaming content studio with 500+ writers and editors, delivering human and human-assisted AI content in 68 languages across 103 markets.

- 🎁 [Register & get $40 credit](https://client.igamingtextlab.com/haai-register?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=humanizer-footer)
- 🌐 [igamingtextlab.com](https://igamingtextlab.com/?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=humanizer-site)
- ✉️ [order@igamingtextlab.com](mailto:order@igamingtextlab.com)
- 💬 [Telegram](https://t.me/igamingtextlab)
- 📦 [All free iGTL skills](https://github.com/igamingtextlab/IGTL-SKILLS#available-skills)

[CC BY 4.0](../LICENSE) © iGamingTextLab
