<p align="center">
  <img src="https://igamingtextlab.com/assets/Logo%20Header.svg" width="220" alt="iGamingTextLab" />
</p>

<h1 align="center">AU Content Check</h1>

<p align="center">
  A free Claude skill for checking iGaming texts for Australia (en-AU). It finds localisation errors, unverified facts and wording that needs further checking before you publish.<br/>
  By <a href="https://igamingtextlab.com/?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-au-header">iGamingTextLab</a> · version 2.3 · rules checked against official sources 13–24 November 2026
</p>

<p align="center">
  <a href="https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-geo-au.skill">
    <img src="https://img.shields.io/badge/%E2%AC%87%20Download%20the%20skill-iGamingTextLab--geo--au.skill-black?style=for-the-badge" alt="Download iGamingTextLab-geo-au.skill" />
  </a>
</p>

<p align="center">
  <b><a href="https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-geo-au.skill">Download iGamingTextLab-geo-au.skill</a></b>
  · open it in Claude · click <b>Save skill</b>
</p>

> 🎁 **Get $40 in free credit** to test iGamingTextLab services — Australian iGaming copy written or checked by our editors.
> [Register at client.igamingtextlab.com →](https://client.igamingtextlab.com/haai-register?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-au-cta)

## What it checks

- **Licence claims.** Licences are checked in the ACMA register or the licensing authority's register; links between the licence and a domain or app are checked separately. Catches "licensed by ACMA" and outdated authority names.
- **Products under the Interactive Gambling Act.** Online casinos, pokies, poker and online in-play betting presented as legal for people in Australia.
- **Inducements.** Sign-up offers in public or affiliate texts, "Not available in NSW" disclaimers, cash out advertising.
- **Payments.** Credit cards and crypto at licensed bookmakers; methods that are not in the Australian cashier.
- **Figures.** "Instant withdrawals", unsupported "more than X" claims, RTP and payout calculations.
- **Player protection.** BetStop, deposit limits, identity verification.
- **Advertising.** Mandatory taglines and 1800 858 858, well-known people in betting ads, 2026 reform dates.
- **Localisation.** British and American terms (acca, free bet, £, GAMSTOP), quotation marks, date and time formats.

## Install

You need Claude with **Code execution and file creation** and **web search** turned on. On Team and Enterprise plans, the organisation owner controls whether custom skills can be uploaded.

1. [Download `iGamingTextLab-geo-au.skill`](https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-geo-au.skill).
2. Open the file in Claude (desktop or web) and click **Save skill**.
   Or upload it manually: **Customize > Skills**, click **+**, then **Create skill** and **Upload a skill**, and choose the file. Don't unzip it.
3. Turn the skill on.

## First request

Open a new chat and paste a text you already have:

```
Use the igtl-geo-au skill. Check this text for Australia; don't rewrite it.
Brand: [brand]. Domain: [domain].
Where it will be published: [public page / affiliate site / operator's logged-in area].
[text]
```

Write "Check and fix" to get a corrected version as well. You can write the request in any language: the summary comes back in that language, and the text for Australia stays in Australian English.

## Reading the result

Every reply starts with a short summary:

- **Status:** "Checks passed" or "Needs a human check", with the reason: a fix, a fact confirmation or a decision on how a rule applies. In an audit, the status is about your original text; when Claude writes or edits, it is about the final text.
- **Fix now:** each remark quotes the text, names the problem, gives the rule type and source, and says what to do.
- **Check before publishing:** source checks (what to confirm and in which official document) and questions about how a rule applies to your platform, offer or payment scheme, which are for your compliance team or lawyer.
- **OK** (full texts only): what was confirmed, with the exact source page and date.

`[VERIFY-n]` in a text marks a missing confirmed fact. For the full report with sources for every fact, ask: "Show the full report".

Rule types in remarks: **Requirement** (law, codes, licence conditions), **iGTL Rule** (mandatory iGamingTextLab editorial rule), **Fact** (the operator's own terms), **iGTL Default** (style setting your brief can change).

## What else it can do

| Request | Result |
| :---- | :---- |
| "Check…" | Remarks and status; the text is not rewritten |
| "Write…" | Summary and a draft based on checked facts |
| "Fix…" | Corrected text with a summary of changes |
| "Adapt this UK text for Australia…" | Localised draft; facts changed only on the basis of a source |

## Limits

- The skill checks wording. It is not legal advice and does not assess whether an offer, campaign, platform or affiliate payment scheme is lawful.
- "Checks passed" means the skill's checks were passed. It is not legal approval or clearance to publish.
- Texts that promote services prohibited under the Interactive Gambling Act to people in Australia (for example, offshore casinos) always get "Needs a human check".
- Australia only. Out of scope: stand-alone texts about lotteries, keno and land-based gambling.
- Without web search, the skill does the language part and marks licences, promotions, limits and payment methods as unconfirmed.

## Updates

An installed skill does not update itself. When a new version is released, download it from [Releases](https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest) and upload it again. Facts about operators are checked live in every task when web search is on. The rules come from a register inside the skill (`references/sources.md`) with a source and check date for every rule.

## Need an editor?

Still have unverified facts? Send to [order@igamingtextlab.com](mailto:order@igamingtextlab.com):

- the source text;
- the skill's report;
- the brand, the domain and where the text will be published.

You'll get an estimate of the editorial review needed: which facts and wording need checking and how long it will take.

## Feedback and bug reports

Did you manage to check your text? What got in the way? Write to [order@igamingtextlab.com](mailto:order@igamingtextlab.com). For a bug report, attach your request, Claude's reply and the skill version.

## About iGamingTextLab

iGamingTextLab writes, edits and localises iGaming content in 68 languages for 103 markets.

- 🎁 [Register & get $40 credit](https://client.igamingtextlab.com/haai-register?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-au-footer)
- 🌐 [igamingtextlab.com](https://igamingtextlab.com/?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-au-site)
- ✉️ [order@igamingtextlab.com](mailto:order@igamingtextlab.com)
- 💬 [Telegram](https://t.me/igamingtextlab)
- 📦 [All free iGTL skills](https://github.com/igamingtextlab/IGTL-SKILLS#available-skills)

[CC BY 4.0](../LICENSE) © iGamingTextLab
