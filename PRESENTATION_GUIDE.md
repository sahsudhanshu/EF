# Group 31 presentation guide: three parts, speaking scripts and a crash course

**Deck:** `Group_31_Final_Submission/slides/Group_31_Presentation_Final.pptx` (19 slides, speaker notes included)
**Paper:** `Group_31_Final_Submission/Research_Report.pdf` (15 pages, 9 figures)
**Topic:** *Mobile Banking: Financial Inclusion vs Cybersecurity Risks*

This file has five parts:

1. [How the deck is split](#1-how-the-deck-is-split) (who presents which slides, and how long)
2. [Crash course: the ideas you must understand](#2-crash-course-the-ideas-you-must-understand) (plain language, with worked examples)
3. [Part 1 script](#3-part-1-script-slides-1-to-6) / [Part 2 script](#4-part-2-script-slides-7-to-12) / [Part 3 script](#5-part-3-script-slides-13-to-19)
4. [Numbers cheat sheet](#6-numbers-cheat-sheet)
5. [Questions the TA may ask, with answers](#7-questions-the-ta-may-ask-with-answers) and [what never to say](#8-what-never-to-say)

You can swap the names of the three presenters; the parts are written so any of you can take any part. Each part is about 5 minutes, so the full talk is about 15 minutes. Read the crash course first, then your own script, then the Q&A.

---

## 1. How the deck is split

| Part | Suggested presenter | Slides | Theme | Time |
|---|---|---|---|---|
| **Part 1: Why and how** | Rushal Verma | 1 to 6 | The question, the literature, the data and the method | about 5 min |
| **Part 2: What the survey shows** | Vichanshu Raj | 7 to 12 | Access, protection, exposure, groups, peers | about 5 min |
| **Part 3: What users say, what it means, what to build** | Sudhanshu | 13 to 19 | App reviews, interview studies, discussion, venture, limits, conclusion | about 5 min |

**Handover lines** (say these so the change of speaker feels natural):
- Part 1 to Part 2: "So that is the question and the data. Vichanshu will now show what the survey found."
- Part 2 to Part 3: "So the survey shows where inclusion and risk diverge. Sudhanshu will show what users say in their own words, and what we would build."

**Everyone should know slides 2, 3, 6 and 19 well.** The TA may ask any of you about the overall question, the research questions, how the coding was checked, or the conclusion.

---

## 2. Crash course: the ideas you must understand

Read this section slowly once. Every idea is explained with an example from our own project.

### 2.1 The big picture in three sentences

India has made it easy to open a bank account, and almost everyone has one. But owning an account is different from using it digitally, and using it digitally is different from using it safely. We ask whether more digital banking comes with more cybersecurity risk, for whom, and whether a business could help.

### 2.2 Financial inclusion: three different levels

| Level | Question | Our measure | Result |
|---|---|---|---|
| **Access** | Do you own an account? | Account ownership | 89.0% |
| **Use** | Do you actually make or receive digital payments? | Digital payment use | 48.5% |
| **Safe use** | Do you have basic protection? Are you being targeted? | Phone lock; unsolicited money requests | 57.7% have a lock; 9.4% of phone owners got a request |

The key message: **access is nearly universal, use is lower, safe use is uneven.** The gap between 89.0% and 48.5% is **40.6 percentage points**.

### 2.3 The data we used

**Global Findex** is a survey run by the World Bank every few years in many countries. It asks ordinary adults about accounts, payments, savings, loans and (in the latest round) phones and scams.

- **The India file** has 3,000 adults aged 15 and over, interviewed in 2024. Each row is one person. This is called **microdata**.
- **Peer indicators**: published country totals from the same survey for India and other countries (China, Indonesia, Bangladesh, Pakistan, Brazil, South Africa and groups). We download them from the World Bank website.
- **App reviews**: public reviews people wrote about payment and bank apps. We collected 14,088 (5,758 Google Play payment apps, 2,090 App Store payment apps, 6,240 for eight bank apps). We did not keep names.
- **Interview studies**: five published research studies where other researchers interviewed Indian users, merchants and fraud victims. We read them and summarised the themes.
- **Documents**: three official documents (two from the World Bank, one from the Reserve Bank of India).

**Why not do our own interviews?** It was not feasible in a term project, and we say so openly. Published studies are our substitute, and we label them as secondary evidence.

### 2.4 Survey weights (why percentages are "weighted")

Our 3,000 people are a sample of India. If, say, rural people were slightly over-sampled, simple counting would give a distorted picture. The World Bank gives each person a **weight** (a number saying how many people in India that person represents). A **weighted percentage** uses those weights so the result describes the adult population, not just the 3,000 people.

Example: "89.0% own an account" is a weighted percentage. We also show the **unweighted counts** (2,710 out of 3,000) so people can see the sample size. The two are not the same, and that is normal.

### 2.5 Percent vs percentage points

- 89.0% minus 48.5% = **40.6 percentage points** (we use unrounded numbers, so it is 40.6 not 40.5).
- If a value goes from 4.3% to 13.1%, it rose by **8.8 percentage points**, which is about **3 times** as high (a ratio).
Never say "40.6 percent difference". Say "40.6 percentage points".

### 2.6 "Reported exposure" is not fraud

The survey asks: *"In the past 12 months, did you receive a phone call or text message asking you for money?"* (asked of phone owners). That is **exposure to a possible scam attempt**. It is **not** proof of fraud, and it does not say anyone lost money. Always say "reported unsolicited requests", never "fraud victims".

Likewise, "45 of 219 people who got a request said they sent money" does **not** tell us how much they lost.

### 2.7 Device lock

The survey asks phone owners whether their phone has a PIN, password or fingerprint lock. A lock protects the **handset** if it is lost or stolen. It does **not** stop a scammer who persuades you to send money. Remember this: it explains why locks and scams are different problems.

### 2.8 Logistic regression and the odds ratio (the hardest idea; take your time)

We want to know: **are people who use digital payments more likely to report a request, after taking account of age, gender, education, income, work and urban/rural?** A **logistic regression** is a standard method for a yes/no outcome. It estimates an **odds ratio** (OR) for each factor.

- **Odds** = chance of "yes" divided by chance of "no".
- Example: 13.1% of payment users reported a request. Odds = 13.1 / 86.9 = about 0.15.
- 4.3% of non-users reported one. Odds = 4.3 / 95.7 = about 0.045.
- Odds ratio = 0.15 / 0.045 = about **3.3** before adjustment. Our model, which adjusts for other factors, gives **3.45**.

**How to say it in one sentence:** "After adjusting for age, gender, education, income, work and urban or rural residence, the odds of reporting a request were about three and a half times higher for payment users." Do **not** say "3.45 times more likely" (that mixes up odds and probability) and do **not** say "digital payments cause scams".

- **Interval 2.24 to 5.30**: the range of plausible values. Because it does not include 1.00 (which would mean no difference), the association is distinguishable from zero.
- **Women vs men OR 0.47**: women had lower odds of reporting a request than men, after adjustment. We do not know why (fewer contacts? less reporting?). Say that we cannot tell.

### 2.9 Why the intervals are "approximate" (design effect)

A proper survey analysis uses information about how the sample was drawn (strata and clusters). The public file does **not** include it. So our intervals assume everyone is independent, which makes them somewhat too narrow. As a safety check we computed:
- the **Kish design effect** from the weights alone = **1.43** (so our 2,145 phone owners are worth about 1,501 independent people);
- what happens if we assume extra clustering (variance multiplied by 1.5, 2 or 3).

Result: the payment-user result and the gender result survive even at factor 3; the tertiary-education result does **not**. That is why we call the model **exploratory**.

### 2.10 Spearman rank correlation (slide 10)

We have 18 demographic groups (women, men, age bands, education levels, income quintiles, rural, urban, working, not working). For each we know three numbers: inclusion (payment use), risk (request exposure), protection (device lock). A **Spearman rank correlation** asks: if we rank the groups by inclusion, do they rank the same way on risk? It runs from -1 to +1.

- **0.38** between payment use and exposure: weak to moderate. More included groups are only somewhat more exposed.
- **0.63** between payment use and lock use: moderately strong. More included groups tend to have better protection.

**Caution:** the 18 groups overlap (a person can be a woman, aged 25 to 39 and in the top income quintile all at once), so this is a description, not a statistical test.

### 2.11 Fisher exact test (RQ3)

Among the 219 people who got a request, 25.0% of those with a lock (39 of 170) and 8.9% of those without (6 of 49) said they sent money. A **Fisher exact test** checks whether a difference like that could be due to chance in a small sample. Result: **p = 0.11**. A p-value below 0.05 is the usual cut-off, so this is **not significant**. We therefore make **no claim** that locks protect or harm. Only 45 people sent money in total.

### 2.12 Coding app reviews, and "kappa"

Reviews are free text. We turned them into numbers in two steps:

1. **Keyword dictionaries** (for example "fraud", "scam", "refund", "blocked"). These are fast but crude: people write "scam" for many things.
2. **Reading**: every review that contained a fraud-type word (118 on Google Play, 57 on the App Store, 65 for bank apps) was read and placed in **one of seven categories**: rewards not honoured; money debited or failed payment; blocked account, mis-selling or poor grievance handling; spam, permissions or intrusive security; general accusation; praise; unauthorised access or theft.

**Why a second coder?** If only one person codes, their bias is invisible. A second coder who does not see the first labels shows whether the categories are reliable.

- **Agreement**: share of reviews given the same category (for example 112 of 118 = 94.9%).
- **Cohen's kappa**: agreement after removing the part that would happen by luck. 0 = chance level, 1 = perfect. Rough guide: 0.6 to 0.8 substantial, above 0.8 almost perfect. Ours: 0.93 (Google Play), 0.78 (App Store), 0.84 (bank apps).

**Exactly what was checked (say it precisely):**
- First pass: one coder.
- Blind AI second pass on all three review sets.
- A human coder outside the group re-coded 40 of the 118 Google Play reviews: 38 agreed (95.0%, kappa 0.93).
- A further second coder, described by the group as **a person who used software, including AI tools, as an aid but made each coding decision**, coded all 122 App Store and bank-app fraud-keyword reviews: 83.6% agreement with the first pass (kappa 0.80).

### 2.13 Chi-square test and the Holm adjustment (slide 13 background)

We compare bank apps with payment apps: are fraud keywords rarer in bank apps? A **chi-square test** answers that for each theme. Because we run six tests, the chance of a false alarm grows, so the **Holm adjustment** makes the cut-off stricter. After this, bank and payment apps differ for fraud keywords, failed payments, safety language and security friction, but **not** for support (p = 0.87) or account blocking (p = 0.12).

### 2.14 Cross-sectional means "no causation"

A **cross-sectional** survey is a snapshot at one moment. It can show that two things go together. It cannot show which came first or that one caused the other. So we write "associated with", never "causes".

### 2.15 Peer comparison

We compare India with other economies using published totals. These come **without sampling errors**, and one value (India's request share) was not published, so we used ours (9.4%) and marked it. That is why we say the comparison is **indicative**.

### 2.16 The business idea in plain words

A **multilingual payment-safety companion**: short audio and visual explanations, a checklist before paying, and verified routes to support and official reporting. **Banks, payment providers or merchant networks pay** a subscription; **users pay nothing**. It does **not** hold money, does **not** ask for OTP or PIN, and does **not** promise to recover money.

### 2.17 The finance numbers, step by step (all **assumptions**, not findings)

| Input | Value |
|---|---|
| Fee per institution per month | INR 50,000 (0.50 lakh) |
| Variable cost per institution per month | INR 10,000 (0.10 lakh) |
| Cost to win a new institution | INR 2 lakh |
| Fixed cost per month, Year 1 | INR 3 lakh (grows 20% a year) |

(1 lakh = 100,000 rupees.)

- **Contribution per institution** = 50,000 minus 10,000 = **INR 40,000 a month** (80% of the fee).
- **Payback on winning a customer** = 2 lakh divided by 0.40 lakh = **5 months**.
- **Break-even (steady state)** = fixed cost divided by contribution = 3 / 0.40 = 7.5, so **8 institutions** to cover fixed costs.
- **Break-even while growing** (winning one new institution every month, which costs 2 lakh) = (3 + 2) / 0.40 = 12.5, so **13 institutions**.
- **Base case Year 1** (worked example): average 4 institutions. Revenue = 4 × 12 × 0.5 = 24 lakh. Costs = fixed 36 + variable 4 × 12 × 0.1 = 4.8 + acquisition 8 new × 2 = 16, total 56.8. Result: **minus 32.80 lakh**. Year 2: zero. Year 3: **plus 52.16 lakh**.
- **Seed of INR 75 lakh**: covers the Year 1 loss (32.80), build (10), pilot (5), a cash reserve (12) and contingency (15.2). In the **conservative** case losses plus build costs reach 81.80 lakh by Year 2, which is **more than 75**.
- **Sensitivity** means: change one assumption and see what happens. If the fee falls to INR 40,000, break-even rises from 8 to 10 institutions.

**Why "illustrative"?** No bank has agreed to pay anything. These numbers show what must be true for the idea to work, so the first real step is a paid pilot.

### 2.18 Vocabulary list (one line each)

- **Microdata**: one row per person.
- **Weighted**: adjusted so the sample represents the population.
- **Exposure**: reported call or message asking for money.
- **Odds ratio**: how much higher or lower the odds are for one group, after adjustment.
- **Kappa**: agreement corrected for chance.
- **Blind coder**: someone who does not see the earlier labels.
- **Secondary evidence**: evidence collected by other people.
- **Illustrative**: example numbers from assumptions, not forecasts.
- **Cross-sectional**: one moment in time.

---

## 3. Part 1 script (slides 1 to 6)

**Presenter: Rushal Verma. About 5 minutes.**

### Slide 1: Title (15 seconds)
> "Good morning. We are Group 31. Our topic is mobile banking: financial inclusion versus cybersecurity risks. We used India's 2024 Global Findex survey, public app reviews and published interview studies, and we finish with an idea for entrepreneurs. I am Rushal, and my teammates are Vichanshu and Sudhanshu."

### Slide 2: Inclusion brings new users, and new targets (45 seconds)
> "India has brought most adults into the formal financial system. But three things are different: owning an account measures access, making digital payments measures activity, and being safe is a third thing. When millions of new users arrive, each is also a possible target and may not have the habits of experienced users. Our gap is that few national studies show adoption, device safeguards and scam exposure together, and fewer ask what a business could do about it. One term to remember: 'reported exposure' means someone says they got a call or message asking for money. It is not proof of fraud."

*Key points to land:* three levels (access, use, safe use); "exposure is not fraud".

### Slide 3: One central question, six research questions (60 seconds)
> "Our central question is: does more inclusion mean more cybersecurity risk, and for whom? We break it into six questions. One: how do ownership, digital payment use and device protection differ by gender, age and income, and how does India compare with other countries? Two: are payment users more likely to report unsolicited requests, after adjustment? Three: among people who got a request, is having a phone lock linked to fewer people sending money? Four: which groups have the biggest gap between payment use and protection? Five: what do app reviews, official documents and published interview studies tell us about grievances? Six: what price and costs would let a safety service break even? The first four come from our progress report; five and six cover the qualitative and business parts."

### Slide 4: 35 academic sources, one gap (45 seconds)
> "We reviewed 35 academic sources in four strands. First, inclusion and mobile money: for example, M-PESA in Kenya helped households share risk and lifted about two percent of households out of poverty. Second, adoption and trust: people use mobile banking when it is useful, easy and credible. Third, security behaviour: phishing exploits ordinary behaviour, and awareness campaigns often fail. Fourth, cyber-risk economics: security is under-provided because those who bear losses are not those who can prevent them. We also drew on entrepreneurial finance: lenders ration credit when they cannot see borrower quality, and digital data can help. The gap: no recent national view of India joins adoption, protection and scam exposure, adds what users say, and links it to a venture."

*If asked for an example paper:* Suri and Jack (2016, Science) on M-PESA; Davis (1989) on technology acceptance; Dhamija et al. (2006) on why phishing works.

### Slide 5: Seven public sources, no data of our own (60 seconds)
> "We used only public data. One: the India Global Findex microdata, 3,000 adults surveyed in 2024, weighted so it represents the adult population. Two: published Findex country indicators for ten economies, so we can compare India with peers. Three, four and five: 14,088 public app reviews, 5,758 on Google Play and 2,090 on the App Store for five payment apps, and 6,240 for eight bank apps. Six: five published interview studies in India. Seven: three official documents from the World Bank and the Reserve Bank of India. We did not conduct interviews or surveys ourselves, and we did not keep reviewers' names, emails or phone numbers."


### Slide 6: Analysis and coding reliability (75 seconds)
> "For the survey we report weighted shares, a logistic regression, and a comparison across 18 groups. For the reviews we used keyword dictionaries and then read every review that contained a fraud-type word and placed it in one of seven categories. To check we were consistent we used second coders. A blind AI second pass agreed on 94.9 percent of Google Play reviews, 82.5 percent of App Store reviews and 87.7 percent of bank-app reviews. A human coder outside our group re-coded 40 Google Play reviews and agreed 95 percent of the time. A further second coder, a person who used software, including AI tools, as an aid but made each decision, coded all 122 App Store and bank-app reviews and agreed 83.6 percent with our first pass, kappa 0.80. Kappa corrects for agreement by chance, and values near 0.8 are considered strong. I will now hand over to Vichanshu, who will show what the survey found."

*Be ready:* "Why did you need a second coder?" (to check our labels are reliable); "Why not interviews?" (not feasible; we used published studies and say so).

---

## 4. Part 2 script (slides 7 to 12)

**Presenter: Vichanshu Raj. About 5 minutes.**

### Slide 7: Access is not the same as active digital use (60 seconds)
> "Here are the first results. 89.0 percent of adults own an account, 66.5 percent own a phone, but only 48.5 percent made or received a digital payment. That is a 40.6 percentage-point gap between owning an account and using it digitally. On the right: 42.7 percent of women made or received a digital payment against 54.1 percent of men, an 11.5-point gap. The survey does not tell us why. It could be access, confidence or social factors. All of this is weighted, and refers to all 3,000 adults."

### Slide 8: Device-lock adoption differs sharply by group (60 seconds)
> "Among phone owners, 57.7 percent report a PIN, password or fingerprint lock. But it varies a lot. 75.7 percent of 15 to 24 year-olds have one against only 22.9 percent of people aged 60 and over. 75.2 percent in the highest income quintile against 40.6 percent in the lowest. Men 62.7, women 50.3. These groups overlap, and the denominator is phone owners, not all adults. Remember that a lock protects the handset, not a person's judgment about a call."

### Slide 9: Payment users report more unsolicited money requests (75 seconds)
> "Now the key link between inclusion and risk. 13.1 percent of phone-owning payment users reported an unsolicited request for money, against 4.3 percent of non-users. After adjusting for age, gender, education, income, work and urban or rural residence, the odds ratio is 3.45, interval 2.24 to 5.30. In plain words: the odds were about three and a half times higher for payment users. Women had lower odds than men, 0.47. This is an association, not proof that digital payments cause scams, and requests are not verified fraud. We also tested robustness: the payment-user and gender results hold even if we assume strong clustering; the tertiary-education result does not. Finally, among 219 people who reported a request, 45 said they sent money; with a lock 25.0 percent, without 8.9 percent, but that difference is not statistically significant, p equals 0.11."

*Key phrase:* "odds about three and a half times higher", not "three and a half times more likely".

### Slide 10: Inclusion and exposure: a weak link across groups (75 seconds)
> "We then looked across 18 groups, such as women, men, age bands, education levels and income quintiles. Each dot is a group: horizontal is inclusion, vertical is reported exposure. The rank correlation is only 0.38, so the link is weak to moderate. Exposure is highest among tertiary-educated adults, 17.9 percent, who are the most included. But it is also high in the lowest income quintile, 12.5 percent, which is among the least included. It is lowest at ages 60 and over, 4.1 percent, and among women, 5.7 percent. Protection follows inclusion more closely, rank correlation 0.63. So risk is not just the price of inclusion; it clusters where inclusion outruns safeguards and where people have little margin for loss. These groups overlap, so this is descriptive."

### Slide 11: Protection lags use at older ages (45 seconds)
> "This chart puts payment use beside lock use for the same groups. The biggest gap is at ages 60 and over: payment use is 56.6 percent but only 22.9 percent have a lock, a gap of 33.7 points. For ages 15 to 24 it is reversed: 43.5 percent use payments and 75.7 percent have locks, minus 32.1 points. The denominators differ, so this tells us where to test guidance, not the precise size of a risk."

### Slide 12: India: top-tier accounts, below-peer phone ownership (45 seconds)
> "Compared with other economies using published 2024 figures: India's account ownership of 89.0 percent is second only to China. Its phone ownership, 66.5 percent, is second lowest, above only Pakistan. Its lock share is 57.6 percent, in the middle. India's request share, 9.4 percent from our own data, is lower than the peers we could compare, which range from 12.7 to 32.4 percent. This may reflect fewer phone contacts, recall, or reporting. It is indicative only, because published totals come without sampling errors. Over to Sudhanshu."

*Be ready:* the 9.4 is from our microdata because the World Bank website does not publish India's value.

---

## 5. Part 3 script (slides 13 to 19)

**Presenter: Sudhanshu. About 5 minutes.**

### Slide 13: Reviews: rewards, refunds and blocks, not theft (75 seconds)
> "We now look at what users say in their own words, using 14,088 public app reviews. We read every review that contained a fraud-type word. On Google Play payment apps, half of those, 50.8 percent, were about cashback or rewards not being paid. On the App Store it was 29.8 percent. For bank apps it was only 4.6 percent; there the biggest group, 38.5 percent, was about blocked accounts, mis-selling, unexpected charges or poor complaint handling. Reviews describing unauthorised access or theft were about 0.1 percent of all reviews. In bank apps, security prompts such as SIM binding, fingerprint set-up and root-detection checks were a recurring source of one-star reviews. Caution: reviews are self-selected, so this shows where trust breaks down, not how common scams are."

### Slide 14: Published studies: social engineering, slow redress (60 seconds)
> "Reviews rarely capture scam victims, so we also used five published interview studies from India. Social engineering, trust in the counterparty or bank, and low awareness appear in all five. Weak support and slow redress appear in four. Examples: 45 of 46 participants in one study said trust in the receiver matters; in another, 12 of 24 merchants reported fake payment confirmations; and in a survey of fraud victims, of 91 who reported fraud, 59 could not recover their money. The official documents agree: trust, consumer protection and protecting credentials like OTPs and PINs."

### Slide 15: Risk concentrates where inclusion outruns safeguards (60 seconds)
> "Putting it together. First, a mixed answer: payment users report more requests, but across groups the link is weak and exposure is also high among the poorest. Second, safeguards lag at older ages. Third, friction is also a risk: security prompts can lock out legitimate users. Fourth, policy: track active and safe use not just accounts, evaluate awareness campaigns on behaviour, and make providers responsible for warnings, refunds and complaints."

### Slide 16: Venture idea: a multilingual payment-safety companion (50 seconds)
> "For entrepreneurs, this suggests a narrow pilot: a multilingual payment-safety companion. The institution pays; users pay nothing. It offers short audio and visual explanations, a pre-payment checklist and verified routes to support and official reporting. It does not hold money, ask for OTPs or PINs, or promise recovery. We propose months one and two for discovery, three to five for a controlled pilot, and scaling only after a paid commitment. No pilot has been run."

### Slide 17: Break-even at 8 institutions, 13 while growing (60 seconds)
> "A simple financial model, and these are assumptions, not findings. Charging INR 50,000 a month per institution, with INR 10,000 of variable cost, gives INR 40,000 contribution, an 80 percent margin. Winning a customer costs INR 2 lakh, paid back in 5 months. With fixed costs of INR 3 lakh a month, eight institutions break even in steady state, and thirteen while we are still winning one every month. The base case loses INR 32.8 lakh in Year 1, breaks even in Year 2 and earns 52.2 lakh in Year 3; the conservative case never breaks even in three years. A fee cut to INR 40,000 raises break-even from 8 to 10. A seed of INR 75 lakh covers the base case, but the conservative case needs 81.8 lakh by Year 2."

### Slide 18: Limitations and next steps (40 seconds)
> "Our limits: the survey is a snapshot and self-reported; requests are not verified fraud; intervals are approximate because the public file lacks design variables; reviews are self-selected and coded with AI help and only sample human checks; we did no interviews of our own; and the finance inputs are assumptions. Next steps: consent-based interviews with merchants, users and bank budget owners, an evaluated pilot, design-based estimates and peer-country data."

### Slide 19: Conclusion (40 seconds)
> "To conclude: account access is broad, 89.0 percent, but only 48.5 percent use digital payments and 57.7 percent of phone owners have a lock. Payment users report more unsolicited requests, odds ratio 3.45, but across groups the link is weak. Reviews and published studies point to rewards, refunds, blocks, support and security prompts far more than reported theft. The opportunity is an institution-funded safety service, tested first through a pilot. The next step is evidence on willingness to pay, retention and effectiveness. Thank you. We are happy to take questions."

---

## 6. Numbers cheat sheet

| What | Number |
|---|---|
| Survey size | 3,000 adults (2,145 phone owners; 2,141 valid lock answers) |
| Account ownership | **89.0%** |
| Phone ownership | **66.5%** |
| Digital payment use | **48.5%** (gap 40.6 points) |
| Women / men digital payment | 42.7% / 54.1% |
| Phone lock overall | **57.7%** |
| Lock: women / men | 50.3% / 62.7% |
| Lock: age 15 to 24 / 60+ | 75.7% / 22.9% |
| Lock: lowest / highest income | 40.6% / 75.2% |
| Request: all phone owners | 9.4% |
| Request: payment users / non-users | **13.1% / 4.3%** |
| Odds ratio (payment users) | **3.45** (2.24 to 5.30) |
| Odds ratio (women vs men) | 0.47 (0.32 to 0.69) |
| Sent money after request | 45 of 219 = 21.0% |
| Lock vs sending money | 25.0% vs 8.9%, Fisher p = 0.11 |
| Kish design effect | 1.43 (effective n about 1,501) |
| Rank correlations (18 groups) | 0.38 (payment use vs exposure), 0.63 (payment use vs lock) |
| Exposure highest / lowest | tertiary 17.9%, lowest income 12.5%; ages 60+ 4.1%, women 5.7% |
| Largest gaps (payment minus lock) | ages 60+ +33.7 points; ages 15 to 24 −32.1 |
| Peers: India account / phone / lock | 89.0 / 66.5 / 57.6 (request 9.4 our data) |
| Reviews | 14,088 total: 5,758 + 2,090 payment apps, 6,240 bank apps |
| Fraud-keyword reviews | 118 (Play), 57 (App Store), 65 (bank) |
| Reward/cashback share of those | 50.8% (Play), 29.8% (App Store), 4.6% (bank) |
| Blocked/grievance share (bank apps) | 38.5% |
| Unauthorised access / theft | 6, 2, 3 reviews (about 0.1% of reviews) |
| Agreement (kappa) | Play 94.9% (0.93), App Store 82.5% (0.78), bank 87.7% (0.84) |
| Human check | 40 Play reviews: 95.0% (0.93); 122 App Store + bank: 83.6% (0.80) |
| Published studies | 5 studies; 5 of 5 on social engineering, trust, awareness; 4 of 5 on weak redress |
| Finance | fee 50,000; variable 10,000; acquisition 2 lakh; fixed 3 lakh/month |
| Contribution / payback | 40,000 a month (80%) / 5 months |
| Break-even | 8 institutions; 13 while growing |
| Base case | −32.80, 0.00, +52.16 lakh (Years 1 to 3) |
| Seed | INR 75 lakh; conservative case needs 81.80 lakh by Year 2 |

---

## 7. Questions the TA may ask, with answers

**Q1. Why did you choose this topic?**
Mobile banking has brought most Indians into formal finance, but digital scams are a visible concern. We wanted to see whether inclusion and risk really move together, and what an entrepreneur could build.

**Q2. Does your result prove digital payments cause scams?**
No. It is a snapshot survey, so we can only say payment users report more requests, even after adjustment. We do not know the direction or cause, and reporting may differ between groups.

**Q3. What does an odds ratio of 3.45 mean?**
The odds of reporting a request were about 3.45 times as high for payment users as for non-users, after adjusting for age, gender, education, income, work and urban or rural residence. For example, raw odds were about 0.15 against 0.045.

**Q4. Why are the intervals "approximate"?**
The public file has no information on strata and clusters, so we assumed independent respondents. We checked sensitivity: the payment and gender results survive even a large assumed clustering effect; the tertiary-education result does not.

**Q5. Why use app reviews? Are they representative?**
No, they are self-selected. We use them for unprompted user language and to see where trust breaks down (refunds, support, blocks, security prompts). They do not measure how common scams are, and we say so.

**Q6. Why no interviews of your own?**
It was not feasible in a term project, and we did not want to collect personal data without review. We used five published India interview studies instead, labelled as secondary evidence, and list own interviews as future work.

**Q7. Who coded the reviews? How do you know it is reliable?**
One coder did the first pass. A blind AI second pass agreed on 94.9, 82.5 and 87.7 percent. A human outside the group re-coded 40 Google Play reviews with 95 percent agreement. A further second coder, a person who used software including AI tools as an aid but made each decision, coded 122 App Store and bank-app reviews with 83.6 percent agreement. The full classifications are in our results folder so they can be audited.

**Q8. What is kappa?**
Agreement corrected for chance. Our values of 0.78 to 0.93 are considered strong.

**Q9. Why is the finance model not real?**
No bank has committed to pay. The numbers are assumptions that show what must be true for the idea to work. That is why the first step is a paid pilot.

**Q10. How do you get "8 institutions"?**
Fixed costs are INR 3 lakh a month and each institution contributes INR 0.40 lakh a month (fee 0.50 minus variable cost 0.10). 3 divided by 0.40 is 7.5, rounded up to 8. While winning one new customer a month at INR 2 lakh each, (3 + 2) / 0.40 = 12.5, so 13.

**Q11. How big is the market?**
We did not measure a total addressable market. As context, India had about 741 banks live on the UPI network in July 2026 (government factsheet), so 40 institutions in Year 3 would be about 5 percent. It is not a validated figure, and buyers could also be payment apps and fintechs.

**Q12. Why is the paper only 12 pages?**
We kept it to the TA's structure and condensed the long tables into figures and short text, about 15 pages including references. The detailed tables, including the full 18-group table, and the extra analysis are in the results files and the notebook.

**Q13. What is the main contribution?**
A transparent picture of where access and safe use diverge in India, combining a national survey with what users say, and a testable venture idea with explicit assumptions.

**Q14. What would you do next?**
Consent-based interviews with merchants, users and bank budget owners; an evaluated pilot with pre-set outcomes; design-based estimates; peer-country microdata; a finance model with churn, tax and cash flow.

**Q15. Why are women's odds of reporting a request lower even though they use digital payments less?**
We cannot tell from this data. They may have fewer contacts exposed, or they may report less. We flag it rather than guess.

**Q16. Is the phone lock useful then?**
For protecting a lost or stolen handset, yes. It does not stop deception. Our comparison of lock and sending money was not significant (p = 0.11), so we make no claim either way. We also saw reviews where lock requirements locked out legitimate users.

**Q17. Where does the data come from, and can we reproduce it?**
World Bank Global Findex (microdata under its access terms), the World Bank open data API, and public app stores. Scripts, the notebook and results are in the submission folder. The microdata file itself is not redistributed.

**Q18. How is your entrepreneurial angle different from just a fraud study?**
We show where users and merchants lack safe, supported access and propose an institution-funded service, with break-even logic, funding needs and risks. Entrepreneurial finance also frames the problem: lenders and providers cannot see user quality or risk, and digital data can ease that.

---

## 8. What never to say

- "Digital payments **cause** scams" or "locks **prevent** losses". We only found associations, and the lock result was not significant.
- "**Fraud victims**" when you mean people who reported an unsolicited request.
- "3.45 times more **likely**". Say "odds about 3.45 times as high".
- "The reviews show how common scams are". They show where trust breaks down.
- "Our finance numbers are forecasts". They are illustrative assumptions.
- "A human checked all the coding". Only **40** Google Play reviews had a human outside the group; the **122** App Store and bank-app reviews had a second coder described as a person who used software, including AI tools, as an aid but made each decision.
- "We interviewed users". We did not; we used five published studies.
- Any number you do not remember. Say "I would check the exact figure in our paper" and look at the cheat sheet.

---

## 9. Practice plan (one hour in total)

1. **15 minutes:** read the crash course (section 2) aloud with a teammate; explain odds ratio, kappa and break-even to each other without notes.
2. **15 minutes:** each person reads their own script twice, then says it again in their own words with the slides open.
3. **15 minutes:** full run-through with handovers, with a timer (target 15 minutes).
4. **15 minutes:** the TA question game: each person asks the other two five questions from section 7 and the answerer must reply in under 30 seconds.

**Delivery tips:** look at the audience and not the slide; say the number and then what it means; pause after each slide title; do not read the small print; if you forget a number, give the idea first and check the cheat sheet afterwards.
