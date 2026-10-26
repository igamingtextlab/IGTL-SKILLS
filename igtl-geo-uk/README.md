<p align="center">
  <img src="https://igamingtextlab.com/assets/Logo%20Header.svg" width="220" alt="iGamingTextLab" />
</p>

<h1 align="center">iGaming GEO: United Kingdom (GB)</h1>

<p align="center">
  A free Claude skill for iGaming texts in British English for the UK market (Great Britain).<br/>
  By <a href="https://igamingtextlab.com/?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-uk-header">iGamingTextLab</a> · version 1.7, updated 23 October 2026
</p>

<p align="center">
  <a href="https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-geo-uk.skill">
    <img src="https://img.shields.io/badge/%E2%AC%87%20Download%20the%20skill-iGamingTextLab--geo--uk.skill-black?style=for-the-badge" alt="Download iGamingTextLab-geo-uk.skill" />
  </a>
</p>

<p align="center">
  <b><a href="https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-geo-uk.skill">Download iGamingTextLab-geo-uk.skill</a></b>
  · open it in Claude · click <b>Save skill</b>
</p>

> 🎁 **Get $40 in free credit** to test iGamingTextLab services — UK iGaming copy written or checked by our editors.
> [Register at client.igamingtextlab.com →](https://client.igamingtextlab.com/haai-register?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-uk-cta)

## What the skill does

It helps you write, edit, audit or localise for GB: operator, slot and sportsbook reviews, bonus pages, landing pages, comparisons, FAQs and meta tags.

It makes sure the text:

- does not attribute a British licence to an operator without an entry in the Gambling Commission register;
- follows the product rules: the slots stake limit of £5 (£2 for players aged 18 to 24), game design requirements, bonus wagering no higher than 10x, the mixed-product ban;
- describes player protection correctly: age and identity checks, financial checks, deposit limits, self-exclusion and GAMSTOP;
- does not offer credit cards or anonymous payments at British licensees;
- follows the CAP Code advertising rules: no appeal to minors, no promises of winning, no pressure to play immediately;
- is written in British English with British formats for amounts, dates, times and odds;
- contains current help contacts;
- does not turn disputed, outdated or unverified data into confident statements: conflicts between sources are resolved through the source hierarchy or passed to the editor as UNVERIFIED;
- has passed a final check before delivery: the same facts match in every section, time limits have a start and an end, promotion and player journey stages are described in full, categorical generalisations are confirmed, and conclusions about reviews are based on a count.

## Who it is for

Authors, editors, SEO specialists and marketers who produce iGaming content for the British market.

## Limits

- **The skill does not replace a lawyer.** It is responsible for the accuracy and correctness of the wording. It does not assess whether an operator's offer or an advertising campaign is lawful. A text that has passed the checklist is not thereby cleared for advertising the operator.
- **Territory: Great Britain** (England, Scotland, Wales). The Gambling Commission does not regulate online gambling in Northern Ireland. Ireland, the Isle of Man, Jersey, Guernsey/Alderney and Gibraltar are treated as separate jurisdictions.
- **Lotteries are out of scope for this version.** They follow separate rules. A lottery counts only as a product type in the mixed-product ban.
- **Current facts need internet access.** Without it, the skill does the language and formatting part and marks the licence, bonuses, limits and payment methods as unverified.

## Installation

Requirement: code execution must be enabled for skills to work in Claude (Code execution and file creation). Individual users enable it in Settings > Capabilities. On Team and Enterprise plans, an organisation owner does this in Organization settings > Plugins & skills, on the Policy tab.

1. [Download `iGamingTextLab-geo-uk.skill`](https://github.com/igamingtextlab/IGTL-SKILLS/releases/latest/download/iGamingTextLab-geo-uk.skill).
2. Open the file in Claude (desktop or web) and click **Save skill**.
   Or upload it manually: Customize > Skills > "+" > "Create skill" > "Upload a skill". Upload the file as is, do not unzip it.
3. Turn the skill on with the toggle in the list.

For Claude to check the Gambling Commission register and operator websites, it needs web search access.

On Team and Enterprise plans, the skill can be shared with colleagues or published to the whole organisation from the skill's menu in Customize > Skills, if the organisation's settings allow it.

## How to use it

Claude uses the skill automatically when a request fits it. To make sure it is used, name the skill in your request: "Use the igtl-geo-uk skill…".

### Modes

| Request | What Claude does | What you get |
| :---- | :---- | :---- |
| "Write…", "Create…" | Gathers data, checks the operator's status, writes the text to the brief | Content Draft and Research & QA Report |
| "Fix…", "Proofread…" | Fixes problems while keeping the meaning, structure and length | Corrected text and a report of changes that affect facts |
| "Check…", "Find errors…" | Does not rewrite the text | Report: findings with location, problem, basis and fix; status of the piece |
| "Adapt for the UK…", "Translate…" | Adapts the language, formats and GB realities; changes facts only on the basis of a source | Content Draft and a report of factual changes with sources |

Modes can be combined: when asked to "check and fix", Claude first gives the findings, then the corrected text.

### Example requests

```
Use the igtl-geo-uk skill. Write a review of [brand] for the UK to the brief below.
Domain: [domain]. Product: casino. Length: 1,500–2,000 words. Keywords: …
```

```
Check this slot review with the igtl-geo-uk skill. Do not rewrite the text.
[text]
```

```
Fix only this FAQ answer: "Can I deposit with a credit card?"
[answer]
```

```
Check and fix this landing page for the UK.
[text]
```

```
Audit the text and give me the completed checklist.
[text]
```

### What to provide with the task

- the brief: format, length, keywords, structure;
- the brand and domain the text is about;
- the product: slots, casino, poker, sports betting or bingo;
- whether the text is advertising or editorial;
- the client's style guide and brand guidelines, including the safer gambling message they use;
- the target audience, if it is not Great Britain.

### How to read the output

- The output has two parts. **Content Draft**: clean text with no internal comments. **Research & QA Report**: status of the piece, verified facts with sources, source conflicts, unverified data and manual checks.
- **Status of the piece:** CHECKS PASSED — editorial review required is given only if all critical facts (licence, legal entity, regulatory restrictions, material bonus terms, availability in GB, key payment terms, player protection) are confirmed by a primary source and current, and no mandatory manual checks remain. Otherwise: NEEDS VERIFICATION. The status reflects the skill's checks and does not guarantee that there are no errors.
- **`[VERIFY-n]`** is the only working mark in the Content Draft: a place where a verified fact is missing. The explanation under the same number is in the report.
- **"Last checked: [date]"** is the actual date changeable data (bonus, payment methods, withdrawal times) was checked.
- **Licence status** is recorded as one of three outcomes:
  - confirmed active licence;
  - insufficient data;
  - officially confirmed absence, termination or suspension of the licence, with the specific status from the source.
- By default, Claude does not output the full checklist or the full fact table (fact, source, date, status CONFIRMED / SECONDARY / UNVERIFIED, criticality, scope, currency, period). Ask for them explicitly if you need them.

## How the skill classifies rules

Each rule in the skill belongs to one of three types:

- **[Requirement]**: legislation, the Gambling Commission's licence conditions and codes of practice (LCCP), technical standards (RTS), the CAP and BCAP advertising codes;
- **[Fact]**: information about the specific operator from its website, cashier, T&Cs and bonus terms;
- **[iGTL Standard]**: iGamingTextLab editorial rules. They are not presented in the text as legal requirements.

In a conflict, this order applies: regulatory requirement, verified fact, the client's brief and style guide, the skill's editorial settings. If the brief asks for wording that is not permitted, Claude writes a permissible version and says what it changed and why.

## Package contents

```
igtl-geo-uk/
├── SKILL.md                         modes, priorities, source hierarchy and conflicts, critical facts, final check, output format, checklist
├── README.md                        this page (not included in the .skill file)
└── references/
    ├── licensing.md                 register, white label, Great Britain and Northern Ireland, operators without a licence
    ├── products.md                  slots, casino games, poker, betting, bingo, game catalogue, casino vs sportsbook, bonuses, current offer check and promotion journey
    ├── player-protection.md         player journey, checks, limits, self-exclusion, GAMSTOP, complaints and ADR, payments, taxes
    ├── style-and-advertising.md     British English, formats, advertising, footer, contacts, final check, links, reviews
    └── sources.md                   rules register, verification statuses, update procedure, change log
```

Claude opens the reference files as needed: `SKILL.md` says which file to read for which task. `README.md` is for people, and Claude does not use it while working.

## Currency of the rules

- The rules were checked against sources on 22–23 October 2026. For each rule, `references/sources.md` gives the source, provision, effective date and verification status.
- If the current primary source differs from the skill's wording, Claude relies on the primary source and reports the discrepancy.
- Open points as of the update date:
  - the start date of the first stage of Financial Risk Assessments has not been announced;
  - no industry Gambling Ombudsman has been set up.
- Four points are confirmed only by secondary sources. They are marked separately in the rules register.

**Updating.** Once a quarter, and before each release of the skill to clients, check for changes on the Gambling Commission pages (LCCP upcoming changes, RTS upcoming changes, news). The update procedure and the change log are kept in `references/sources.md`.

## If the upload fails

- Upload the `.skill` file exactly as downloaded. If you repack it yourself, the archive root must contain the `igtl-geo-uk` folder; separate files at the root break the upload. The folder name must match the `name` field in `SKILL.md`, so do not rename the folder.
- The Claude help article gives a 200-character limit for the skill description (`description`); the Agent Skills specification allows up to 1,024. This skill's description is 691 characters. If the upload is rejected because of the description, it needs to be shortened.
- If there is no upload button on a Team or Enterprise plan, the organisation owner has most likely turned off uploading custom skills, or your role does not allow it.

## Related skills

**[igtl-geo-germany](../igtl-geo-germany/)** applies the same approach to the German market: checking operator status against the GGL Whitelist, product rules, German language and formats.

## Version history

| Version | Date | Main changes |
| :---- | :---- | :---- |
| 1.7 | 23 Oct 2026 | Status READY TO PUBLISH renamed to "CHECKS PASSED — editorial review required"; English version of the skill and README |
| 1.6 | 23 Oct 2026 | Reliability control: dynamic facts, source hierarchy and conflicts, critical facts, UK compliance, claims about work done, link checks; Content Draft and Research & QA Report with the statuses READY TO PUBLISH / NEEDS VERIFICATION; complaints and ADR |
| 1.5 | 23 Oct 2026 | Final check of the finished text: status and scope of facts, article consistency, player journey, full promotion journey, generalisations, reviews |
| 1.4 | 23 Oct 2026 | Precise names for the licence check outcomes, with the specific status |
| 1.3 | 22 Oct 2026 | Single rule for confirming status; self-exclusion split into requirements and recommendations; RTS links corrected |
| 1.2 | 22 Oct 2026 | Verification statuses in the rules register; lotteries taken out of scope; financial checks, limits and urgency rules clarified |
| 1.1 | 22 Oct 2026 | Working modes, priorities, verification standard; reference files moved into `references/`; a number of factual corrections |
| 1.0 | 22 Oct 2026 | First version, based on the structure of igtl-geo-germany |

Detailed change log: `references/sources.md`.

## About iGamingTextLab

iGamingTextLab is an iGaming content studio with 500+ writers and editors, delivering human and human-assisted AI content in 68 languages across 103 markets.

- 🎁 [Register & get $40 credit](https://client.igamingtextlab.com/haai-register?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-uk-footer)
- 🌐 [igamingtextlab.com](https://igamingtextlab.com/?utm_source=github&utm_medium=readme&utm_campaign=igtl-skills&utm_content=geo-uk-site)
- ✉️ [order@igamingtextlab.com](mailto:order@igamingtextlab.com)
- 💬 [Telegram](https://t.me/igamingtextlab)
- 📦 [All free iGTL skills](https://github.com/igamingtextlab/IGTL-SKILLS#available-skills)

[CC BY 4.0](../LICENSE) © iGamingTextLab
