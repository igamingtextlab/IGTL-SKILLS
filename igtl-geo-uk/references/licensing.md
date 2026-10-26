# Licence, territory and operators without a GB licence

Read this file when the text names an operator, brand or domain; mentions a licence, lawfulness, the regulator, the UK as a whole or Northern Ireland, or white label; and when the Gambling Commission licence is not confirmed.

Sources and effective dates of the rules are in `sources.md`.

## 1. Territory

- The Gambling Commission licenses and regulates gambling only in Great Britain: England, Scotland and Wales [Requirement].
- **Northern Ireland** [Requirement]: the Gambling Commission does not regulate online gambling there, but remote gambling may not be advertised to consumers in Northern Ireland without a Gambling Commission licence. If the text addresses players in Northern Ireland, do not promise them Gambling Commission protection or oversight; describe protection measures according to the operator's actual terms [Fact].
- The Republic of Ireland, the Isle of Man, Jersey, Guernsey/Alderney and Gibraltar are separate jurisdictions. Do not apply GB rules to them.
- Do not write "UK-wide licence", "licensed across the UK" or "legal in the UK" as a statement about the whole United Kingdom.

## 2. Checking status in the register

The main source is the Gambling Commission public register (Register of gambling businesses). You can search by company name, trading name, domain and account number; the register can be downloaded as Excel or CSV.

1. **Legal entity**: the company in the operator's footer or T&Cs matches the Account name in the register; the account number in the footer matches the number in the register.
2. **Domain**: the domain the text is about is listed under Domain names in that entry with the status Active or White label. The status Inactive does not confirm a current licence for the domain.
3. **Activity**: the activity in the entry matches the product in the text. The entry marks it as Remote, for example "Casino (Remote)" for slots, table and live games, or "General Betting Standard - Real Event (Remote)" for sports betting. Copy the name from the register; do not reconstruct it.
4. **Licence status**: Active. The other register statuses (Pending, Suspended, Expired, Lapsed, Surrendered, Forfeited, Revoked, Revoked (Non payment of fee)) do not confirm an active licence.
5. **Source**: the register entry and the check date. If the text mentions sanctions, rely on the regulatory actions section of the same entry.

Licence status is a dynamic critical fact (`SKILL.md`, section 3). If time has passed between the check and publication, open the entry again; give the date of the latest check in the report.

**White label** [Fact]: if the domain appears in the register with the status White label, the licensee is the company whose entry lists the domain; the brand operates under its licence. Name the company from the register as the licensee.

The Gambling Commission warns that domains and trading names are entered in the register by the companies themselves and does not guarantee their accuracy. A discrepancy between the site and the register is something to tell the task owner about; do not pick the convenient version.

## 3. Three possible outcomes

- **Confirmed active licence**: all items match → wording from the table below.
- **Insufficient data**: an item was not found or could not be checked, including when the domain is not in the register → the British licence is not confirmed. Carry on with the brief without attributing a Gambling Commission licence or lawfulness in GB to the operator. List the missing confirmations in the Research & QA Report. A missing entry does not by itself prove there is no licence: the domain may have been registered under another name.
- **Officially confirmed absence, termination or suspension of the licence**: the register shows, for this legal entity and domain, a status under which the licence is not in force, or there is an official Gambling Commission notice → section 5. **Give the specific status from the source**; do not reduce it to a general "no licence":
  * absence: an official Gambling Commission notice that the operator has no licence; the status Pending (application made, licence not yet in force);
  * termination: Expired, Lapsed, Surrendered, Forfeited, Revoked, Revoked (Non payment of fee);
  * suspension: Suspended.
  In the report: status, source and date, for example "Register status: Suspended (checked 23 October 2026)". If the brief requires the status to be mentioned in the text itself, use the exact status: do not call a suspended licence absent, and do not describe a revoked licence as one that never existed.

A client's statement that there is no licence, without such confirmation, gives the outcome "insufficient data". In the report, write: "According to the client, there is no British licence; this has not been independently verified." For the text, both outcomes ("insufficient data" and officially confirmed absence, termination or suspension) mean the same thing: you do not attribute an active British licence to the operator, and you apply section 5.

**Single confirmation rule:**
- the existence of an active licence for the right product and domain is confirmed only by a register entry;
- absence, revocation or suspension is confirmed by the register status or by an official Gambling Commission notice;
- an unavailable register does not cancel an official notice you have found.

If the register cannot be reached by any route and there is no official notice, the outcome is "insufficient data". Do not write that you checked the register, and do not give a register check date.

## 4. Wording

| What is confirmed | Wording | Not allowed |
| :---- | :---- | :---- |
| Active, domain and activity match | "[Company] is licensed and regulated in Great Britain by the Gambling Commission under account number [N]." | extending it to the operator's other products, domains and brands |
| White label | "[Brand] is operated by [Company], which is licensed and regulated in Great Britain by the Gambling Commission under account number [N]." | calling the brand the licensee |
| Neutral, for reviews and FAQ | "holds a Gambling Commission licence for [activity] (account number [N])" | "legal in the UK" without territory and product |
| Licence not confirmed | do not write about a British licence | see section 3 and section 5 |

- The Gambling Commission gives the template "licensed and regulated in Great Britain by the Gambling Commission under account number…" as the wording licensees display in their footer.
- The regulator's official name is the Gambling Commission. "UK Gambling Commission" and "UKGC" are common informal names; they are acceptable after the first mention if the client uses them [iGTL Standard].
- Licences from the MGA, Gibraltar, the Isle of Man, Alderney, Curaçao and other regulators are not a British licence. Do not present them as permission to serve players in GB.
- If an operator has several activities, name the licence for each product separately. A betting licence does not confirm a casino licence, and vice versa.
- Before writing, record what is being reviewed: the whole brand or a specific offer, product, domain or app.
- Do not conclude that other products are absent because the register lists only one activity.
- "Activity from" in the register is the date the licence for that product was most recently granted, not the date the brand was founded. Do not calculate a licence expiry date.
- Status cannot be inferred from signs: a .co.uk domain, prices in pounds, a GAMSTOP logo, a helpline in the footer or the absence of credit cards in the cashier prove neither that a licence exists nor that it does not.

## 5. Operator without a confirmed Gambling Commission licence

- Do the task in the format of the brief. An unconfirmed or absent British status is not, in itself, a reason to refuse the text automatically.
- Distinguish "insufficient data" from officially confirmed absence, termination or suspension; in the second case, give the specific status from the source. Briefly state the outcome of the check and the missing information in the report. Do not repeat the legal note in every fragment.
- **Risk of advertising unlicensed gambling** [Requirement: Gambling Act 2005, s.330]: advertising gambling that requires a Gambling Commission licence when there is no such licence is a criminal offence. It also covers people who take part in or facilitate the advertising if they know or should know that it is unlawful. If the text addresses players in GB and encourages them to sign up with an operator whose licence is not confirmed, add this risk in one line to the manual checks section of the report. The decision to publish rests with the client and their lawyer; until that decision, the status of the piece is NEEDS VERIFICATION.
- **GAMSTOP** [iGTL Standard]: do not write texts that position the operator as a way around GAMSTOP or self-exclusion ("casinos not on GAMSTOP" as a selling point). Do not address advertising calls to self-excluded players or minors.
- Do not attribute an unconfirmed licence to the operator, and do not call the offer "UK-licensed", "UKGC-regulated" or "legal in the UK".
- Describe a foreign licence from verified data: regulator, legal entity, entry in that regulator's register, link to the domain [Fact].
- Describe actual features and terms from verified data. Do not apply the restrictions on British licensees to the operator, and do not present their absence as a lawful exemption from the requirements.

The skill checks the text within the scope of its instructions and does not confirm that publishing it is legally permissible.
