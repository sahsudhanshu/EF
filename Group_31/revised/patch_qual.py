# -*- coding: utf-8 -*-
p = 'Group_31/revised/build_structured_paper.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)


rep("It has three components:", "It has five components:")
rep("review 35 academic and ten institutional sources", "review 35 academic papers and several institutional sources")

# ---- 3.3
i = s.index("H2('3.3 Data collection methods')")
j = s.index("H2('3.4 Materials and instruments')")
s = s[:i] + '''H2('3.3 Data collection methods')
P("Four data sources were used. (1) **Survey microdata.** The India microdata were downloaded from the World Bank microdata library on 4 November 2026 under its access conditions {fxdata}. "
  "(2) **Peer-economy aggregates.** Published Global Findex 2025 country values for 2024 (account ownership, mobile phone ownership, phone lock and unsolicited money requests) were retrieved from the World Bank open data API for India, China, Indonesia, Bangladesh, Pakistan, Brazil, South Africa, South Asia, lower-middle-income economies and the world {wdi}; the script fetch_data.py reproduces the download. "
  "(3) **Public app reviews.** The newest English-language reviews in the India Google Play store for PhonePe, Google Pay, Paytm, BHIM and SBI YONO were collected with the google-play-scraper package (up to 3,000 per app; 15,000 retrieved) {reviews}. Only app, date, rating and text were stored; usernames were not, and email addresses and phone numbers in text were masked. "
  "Reviews shorter than 15 characters and duplicates were removed, leaving 5,758 reviews posted between 2 October and 19 November 2026. "
  "(4) **Institutional documents.** Three documents were selected for relevance to trust, shared responsibility and fraud awareness: the World Bank's discussion of trust {wbtrust}, its responsible financial access overview {wbcp} and the Reserve Bank of India's awareness circular {rbi}. "
  "A documented in-app warning feature {gpay}, the national cyber-fraud helpline {mha}, published global aggregates {wbblog} and the NPCI list of live UPI members {npci} were used only for context. "
  "No interviews, focus groups or surveys of our own were conducted. **Justification:** public microdata and open APIs permit transparent reproduction, and public reviews give unprompted user language that the Findex questionnaire cannot provide.", align='j')

''' + s[j:]

# ---- 3.5 qualitative
i = s.index('P("**Qualitative document analysis.**')
j = s.index('P("**Financial model.**')
s = s[:i] + '''P("**Peer comparison.** Published aggregates are set beside our India estimates without statistical testing, because sampling errors and country microdata are not available. India's unsolicited-request share is not published in the API, so the value from our microdata (9.4%) is used and marked.", align='j')
P("**Qualitative analysis.** Two qualitative sources were analysed. First, passages in the three institutional documents {wbtrust,wbcp,rbi} on adoption barriers, protection mechanisms and responsibilities were extracted and grouped into themes. "
  "Second, the 5,758 app reviews were coded in two steps. A dictionary of regular expressions flagged five themes (fraud, scam or unauthorised transactions; money deducted or failed payment; support and complaint handling; account blocking, verification or login barriers; safety and trust language), and a review could carry several themes. "
  "Because keyword matches can mislead, all 118 reviews that matched the fraud keywords were then read in full and assigned to one of seven manually defined categories. A further dictionary counted reviews describing device-lock or security-alert prompts. "
  "The coding was done by a single coder without a second rater, so reliability is untested; the full classification is supplied so that it can be audited. Review text is treated as unprompted user opinion, not as verified evidence of fraud.", align='j')
''' + s[j:]

rep("Responses on unsolicited requests are described as reports", "App reviews are public; no usernames were stored, and short quotations are anonymous. Responses on unsolicited requests are described as reports")

# ---- Results 4.7-4.9
i = s.index("H2('4.7 Qualitative document review')")
j = s.index("# ================================================================= 5 DISCUSSION")
new = '''H2('4.7 Peer-economy comparison')
P("Among the seven economies in Table " + str(T['peers']) + ", India's account ownership (89.0%) was the second highest after China (89.4%), and above Brazil (86.4%) and South Africa (81.1%). Its phone ownership (66.5%) was the second lowest, above only Pakistan (62.9%). "
  "The share of phone owners with a lock was 57.6% in India, against 47.5% in Bangladesh, 46.4% in Pakistan, 68.5% in South Africa, 69.1% in Indonesia and 78.0% in Brazil; the lower-middle-income value was 57.1%. "
  "The share of phone owners reporting an unsolicited money request was 9.4% in India (our microdata), against 12.7% in Bangladesh, 13.5% in South Africa, 15.0% for lower-middle-income economies, 18.5% in Indonesia, 18.8% in Pakistan and 32.4% in Brazil (Figure " + str(F['peers']) + "). "
  "China and the world aggregate have no published lock or request values.", align='j')
table('peers', 'India compared with peer economies, 2024 (percent)', [
    ['Economy', 'Account (% adults)', 'Own phone (% adults)', 'Phone lock (% phone owners)', 'Unsolicited money request (% phone owners)'],
    ['India', '89.0', '66.5', '57.6', '9.4†'],
    ['China', '89.4', '96.6', 'n/a', 'n/a'],
    ['Indonesia', '56.3', '80.3', '69.1', '18.5'],
    ['Bangladesh', '43.3', '82.4', '47.5', '12.7'],
    ['Pakistan', '27.3', '62.9', '46.4', '18.8'],
    ['Brazil', '86.4', '92.1', '78.0', '32.4'],
    ['South Africa', '81.1', '87.0', '68.5', '13.5'],
    ['South Asia', '77.6', '67.8', '55.2', 'n/a'],
    ['Lower middle income', '70.4', '75.1', '57.1', '15.0'],
    ['World', '78.7', '85.7', 'n/a', 'n/a'],
], [1.4, 1.0, 1.0, 1.4, 1.7], note="Source: World Bank Global Findex 2025 indicators {wdi}. † India's request share is our weighted microdata estimate (9.4%, n = 2,145), because the API publishes no value; the published India lock share (57.6%) differs slightly from our 57.7%. n/a = not published.")
figure('peers', 'figure5.png', "India compared with peer economies on account ownership, phone ownership, phone lock and unsolicited money requests (2024). Source: {wdi}; India's request share from authors' calculations.")

H2('4.8 Qualitative document review')
P("The review produced three themes. **Trust and support:** the World Bank's discussion of trust links trust with awareness of risks and with timely dispute resolution {wbtrust}. "
  "**Shared responsibility:** the World Bank's responsible financial access overview places consumer protection alongside financial capability {wbcp}. "
  "**Awareness and credential protection:** the Reserve Bank of India's circular calls for public-awareness campaigns through multiple channels and highlights protecting credentials such as OTPs and PINs {rbi}. "
  "None of the documents reports primary data from the respondents in this study, and none evaluates the proposed service.", align='j')

H2('4.9 Public app-review analysis')
P("The cleaned dataset contains 5,758 reviews: BHIM 2,273, SBI YONO 1,656, PhonePe 761, Paytm 591 and Google Pay 477. The mean rating was 2.90. At least one theme matched 18.5% of reviews. "
  "Reviews matching the fraud keywords numbered 118 (2.0%) and had a mean rating of 1.36, against 2.93 for the other reviews. Table " + str(T['themes']) + " and Figure " + str(F['themes']) + " give the five themes.", align='j')
table('themes', 'Keyword themes in 5,758 app reviews', [
    ['Theme', 'Reviews', 'Share of reviews', 'Mean rating', 'One-star share'],
    ['Fraud, scam or unauthorised transactions', '118', '2.0%', '1.36', '85.6%'],
    ['Money deducted or failed payment', '133', '2.3%', '1.44', '82.0%'],
    ['Support and complaint handling', '306', '5.3%', '1.49', '81.4%'],
    ['Account blocking, verification or login barriers', '365', '6.3%', '1.58', '75.1%'],
    ['Safety and trust language', '302', '5.2%', '3.21', '35.8%'],
], [2.5, 0.8, 1.1, 0.9, 1.1], note="Source: authors' keyword coding of {reviews}. A review can match several themes.")
figure('themes', 'figure6.png', "Share of app reviews mentioning each keyword theme. Source: authors' coding of {reviews}.")
P("Of the 118 fraud-keyword reviews, manual reading assigned 60 (50.8%) to rewards, cashback or offers not honoured, 15 (12.7%) to money debited, failed payments or missing refunds, 11 (9.3%) to blocked accounts, mis-selling or poor grievance handling, "
  "10 (8.5%) to spam, permissions, privacy or intrusive security controls, 9 (7.6%) to general accusations without an incident, 7 (5.9%) to praise or no complaint, and 6 (5.1%) to unauthorised access, theft or hacking, reported or feared (Table " + str(T['manual']) + "). "
  "The six reviews of unauthorised access or theft are 0.1% of all 5,758 reviews.", align='j')
table('manual', 'Manual classification of the 118 fraud-keyword reviews', [
    ['Category', 'Reviews', 'Share'],
    ['Reward, cashback or offer not honoured (called scam or fraud)', '60', '50.8%'],
    ['Money debited, payment failed or refund missing', '15', '12.7%'],
    ['Blocked account, mis-selling or poor grievance handling', '11', '9.3%'],
    ['Spam, permissions, privacy or intrusive security controls', '10', '8.5%'],
    ['General accusation, no specific incident', '9', '7.6%'],
    ['Praise or no complaint', '7', '5.9%'],
    ['Unauthorised access, theft or hacking (reported or feared)', '6', '5.1%'],
    ['Total', '118', '100.0%'],
], [4.2, 0.9, 0.9], note="Source: authors' classification of {reviews}; one coder, no second rater.")
P("A separate dictionary found 104 reviews (1.8%) describing device-lock or security-alert prompts, 86 for BHIM and 18 for SBI YONO, with a mean rating of 1.88. "
  "Typical wording reports the app asking the user to enable a device lock that is already set.", align='j')

'''
s = s[:i] + new + s[j:]

# ---- market anchor in 4.6
rep("Steady-state break-even is 8 paying institutions,",
    "Against the NPCI list of about 758 live UPI bank and PPI entries {npci}, the Year 3 closing institution counts (18, 40 and 65) equal 2.4%, 5.3% and 8.6% of that list. "
    "Steady-state break-even is 8 paying institutions,")
open(p, 'w', encoding='utf-8').write(s)
print('patched')
