<p align="center">
  <img src="https://igamingtextlab.com/assets/Logo%20Header.svg" width="220" alt="iGamingTextLab" />
</p>

<h1 align="center">iGaming GEO: Germany (DE)</h1>

<p align="center">
  A free Claude skill for writing, editing and checking German-language iGaming content for the German market.<br/>
  By <a href="https://igamingtextlab.com/?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-germany-header">iGamingTextLab</a> · regulatory content current as of October 2026
</p>

<p align="center">
  <a href="https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-geo-germany.skill">
    <img src="https://img.shields.io/badge/%E2%AC%87%20Download%20the%20skill-iGamingTextLab--geo--germany.skill-black?style=for-the-badge" alt="Download iGamingTextLab-geo-germany.skill" />
  </a>
</p>

<p align="center">
  <b><a href="https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-geo-germany.skill">Download iGamingTextLab-geo-germany.skill</a></b>
  · open it in Claude · click <b>Save skill</b>
</p>

> 🎁 **Get $40 in free credit** to test iGamingTextLab services — German iGaming copy written or checked by our editors.
> [Register at client.igamingtextlab.com →](https://client.igamingtextlab.com/haai-register?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-germany-cta)

## What it's for

- Operator, slot and sportsbook reviews
- Bonus pages and landing pages
- Comparisons, FAQs and meta tags

Germany only. Austria and Switzerland are separate markets, and DE rules are not carried over to them.

**Scope.** The skill is responsible for the accuracy and quality of the wording. It does not assess whether an operator's offer or ad campaign is legal, and it does not replace legal advice. A text that passes the checklist is not automatically cleared for advertising the operator.

## Installation

You need a Claude plan with skills (Free, Pro, Max, Team or Enterprise) and code execution turned on.

1. Turn on **Code execution and file creation** in **Settings → Capabilities**. On Team and Enterprise plans, an owner enables "Code execution and file creation" and "Skills" in **Organization settings → Plugins & skills** (Policy tab).
2. [Download `iGamingTextLab-geo-germany.skill`](https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-geo-germany.skill).
3. Open the file in Claude (desktop or web) and click **Save skill**.
   Or upload it manually: **Customize → Skills → + → Create skill → Upload a skill**. Upload the file as is, don't unzip it.
4. Check that the skill's toggle is on.

## How to use

Claude picks the skill automatically when a request matches. To make sure it's used, name it in your prompt: "Use the igtl-geo-germany skill…".

Give Claude what you have: the brief, operator name and domain, product, length, du or Sie, bonus terms. The more facts you provide, the fewer open questions come back.

With web search available, Claude checks the official GGL Whitelist and operator pages itself wherever it can access them. If it can't access a source, it doesn't pretend to have checked: the operator's status stays "not confirmed", and the missing information is listed separately.

**Example prompts**

```
Use the igtl-geo-germany skill. Write a review of the slots offer at [brand] ([domain]) for players in Germany. About 1,200 words, du-form. Brief: …
```

```
Use igtl-geo-germany to check this German bonus page. List only significant issues and suggest corrected wording: [text]
```

```
Use igtl-geo-germany. Write five FAQ answers about deposit limits for a German sports betting page.
```

```
Use igtl-geo-germany. Write a meta title and meta description for a review of [brand] Sportwetten.
```

## What you get

- The text in German (de-DE), or corrections to a text you provided.
- A short comment with the operator status result (for texts about an operator) and only the significant open issues. The checklist runs internally and isn't printed in full.
- If an essential fact can't be confirmed, the text stays a draft, with `[уточнить: …]` ("to clarify") placeholders where that fact is needed.
- Volatile data (bonuses, payment methods, withdrawal times) is dated "Stand: TT.MM.JJJJ", the actual check date rather than the generation date.

## What's inside

### Three types of rules

The skill keeps these apart:

- **Requirement**: a mandatory rule from the law, an applicable regulator decision or the operator's permit conditions. GGL FAQs and guidance help interpret rules but don't create requirements of their own, so they're cited as "according to GGL guidance".
- **Fact**: verified for a specific operator on its site, cashier, lobby, AGB or Bonusbedingungen.
- **iGTL Standard**: an iGamingTextLab editorial rule. It's not a legal requirement and is never presented as one.

### Missing data

- No guessing. Status, limits, features, withdrawal times and bonus terms come only from a verified source.
- If a page won't load, the skill tries other routes: a search on the official domain, another section of the site, a current official document.
- Placeholders are used only where the text can't be written correctly without the missing fact. Optional unconfirmed details are left out.
- Public information is researched by the skill itself. The client is asked only about things that need their data, access or a decision on the brief.

### Operator status via the GGL Whitelist

Five points are checked: the legal entity (matched against the Impressum or AGB), the domain, the product, the territory (Vertriebsgebiet), and the source with the check date.

There are three possible results: "confirmed", "insufficient data" and "established that there is no permit". A Whitelist entry that can't be found means "not confirmed", not "no permit". A confirmed status comes with ready-made German wording for each type of permit.

Common pitfalls the skill catches:

- Zuständigkeit (the responsible authority) isn't necessarily the authority that issued the permit.
- "GGL-Casino" is an error for a slots offer.
- A permit for one product doesn't extend to the operator's other products.
- "In Deutschland erlaubt" is used only when the permit covers all of Germany.
- Status is never inferred from indirect signals. A .de domain, payment methods or a helpline in the footer prove nothing either way.

### Product rules that don't transfer between products

**Slots (virtuelle Automatenspiele), GGL permit**

- The words "Casino" and "Casinospiele" aren't used in connection with slots. According to GGL guidance, this also applies to affiliate advertising.
- The base maximum stake is €1 per spin. From 01.07.2026, operators with the required GGL permit may offer higher stakes to players aged 21+: up to €3, or up to €5 under additional conditions, including a 90-day qualification period with that operator. Higher stakes are mentioned only when both the permit and the feature are confirmed. The current decision runs until 31.12.2027.
- The general stake limit, the limit available to a specific player and the maximum bet during bonus wagering are kept apart.
- At German licensees, Autoplay, accumulating jackpots, playing several slots at once and spins shorter than 5 seconds on average aren't described as available.
- Bonus Buy, Gamble and Turbo-Spin are described from the actual German version of the game, not judged by name.
- RTP is given for the game version the operator offers. If only the manufacturer's value is known, it's labelled as such.

**Online poker, GGL permit**

- Slot rules don't carry over to poker.
- Up to four tables, where the permit allows it.
- Human players only, with random assignment to a table with the same game offer.

**Sports betting, GGL permit**

- Live betting: the final result and, only in sports where such events are few per match, the next goal, set or a similar part of the result.
- Not described as available: bets on rule violations and their sanctions (cards, penalties for fouls), and events with mainly minors or amateurs, except major national or international events.
- Markets are taken from the operator's line. Any fee is stated with its exact base, the stake or the winnings, and isn't called a tax without confirmation.

**Online-Casinospiele (roulette, blackjack, live casino)**

- Permits and concessions are issued by the German states, not the GGL. They're valid within the confirmed Vertriebsgebiet: "für Spieler in [Vertriebsgebiet]".

**Player protection, each with its own scope**

- Deposit limit: as a general rule, "bis zu 1.000 € Einzahlungen pro Kalendermonat, anbieterübergreifend". A raised limit is never presented as available to everyone.
- Players' own limits: increases take effect after 7 days, decreases immediately.
- Switching operators: a five-minute wait after the previous operator reports the end of the player's activity.
- Panikknopf: a 24-hour block via OASIS that ends automatically.
- OASIS self-exclusion: one year by default, at least 3 months. It doesn't end automatically.
- Between sections of one licensee: a one-minute wait; winnings can be used in another section only after one hour.

### German language and tone

- Standard German (de-DE), without Austrian or Swiss forms. Either du or Sie, never mixed in one text.
- Duden spelling, „…" quotation marks, natural word order, and checks for calques from English.
- A calm, factual tone: no "MEGA", caps, strings of exclamation marks or artificial urgency. Clear CTAs such as "Bonusbedingungen lesen".
- No repeated explanations across the intro, pros and cons, conclusion and FAQ, and no filler.

### Formats

"100 €" instead of "€100"; "10.000 €" and "2,50 €"; "Quote 2,10"; "RTP von 96,21 %"; "21:00 Uhr"; one percentage format per text.

### Payments and features

- Methods, limits, fees and times come from the cashier and payment terms. A payment method doesn't prove or disprove the operator's status.
- No "anonym einzahlen" at German licensees. A paysafecard PIN voucher is kept distinct from a named paysafecard account.
- The ban on operators lending to players isn't presented as a ban on credit cards.
- giropay is closed. Wero and crypto are mentioned only if they appear in the operator's cashier.
- For withdrawals, processing time is kept separate from the time the money arrives.
- Tax consequences for players aren't described.

### Responsible gambling and advertising

- Footer of a full page (iGTL standard; for the operator's own ads, part of it is set by its permit conditions): "18+", "Glücksspiel kann süchtig machen", a helpline and help website, "Es gelten die AGB / Bonusbedingungen", and the permit line for confirmed licensees.
- Help contacts: the BIÖG helpline 0800 1 37 27 00 (check-dein-spiel.de), Fachverband Glücksspielsucht, and OASIS self-exclusion.
- Advertising: no misleading claims about chances or winnings, no slot "tricks", no gambling as a way out of money problems, and no addressing minors or self-excluded players.

### Operators without a confirmed German permit

- The skill doesn't refuse automatically; it writes to the brief.
- It never attributes an unconfirmed German permit and doesn't use "legal in Deutschland", "GGL-lizenziert" or "auf der Whitelist".
- A foreign licence is described from verified data. German licensee restrictions aren't imposed on the operator.

### Final checklist

19 points: status, licence and territory, terminology, product features, slots, raised stakes, player protection, deposit limit, bonus terms (including the wagering base and maximum bet), tone, payment methods, cards and paysafecard, crypto, withdrawal times, taxes, footer, language and formats, accuracy, and readiness for handover.

Only the points relevant to the format are applied. A full-page footer isn't added to a single paragraph or FAQ answer.

### Sources

The GGL Whitelist, GGL FAQs and download area, the GlüStV 2021, the operator's own pages, check-dein-spiel.de, Duden and DIN 5008. Affiliate comparison sites are used only for competitor analysis, never as a source of facts.

## Keep in mind

- Rules are current as of October 2026. Re-check time-limited rules before relying on them, such as the raised slot stakes decision that runs until 31.12.2027.
- The skill doesn't invent tests, reviews, figures or sources.
- This is not legal advice.

## About iGamingTextLab

iGamingTextLab is an iGaming content studio with 500+ writers and editors, delivering human and human-assisted AI content in 68 languages across 103 markets.

- 🎁 [Register & get $40 credit](https://client.igamingtextlab.com/haai-register?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-germany-footer)
- 🌐 [igamingtextlab.com](https://igamingtextlab.com/?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-germany-site)
- ✉️ [order@igamingtextlab.com](mailto:order@igamingtextlab.com)
- 💬 [Telegram](https://t.me/igamingtextlab)
- 📦 [All free iGTL skills](https://github.com/igamingtextlab/IGTL-SKILLS#available-skills)

[CC BY 4.0](../LICENSE) © iGamingTextLab
