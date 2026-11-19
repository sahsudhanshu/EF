# -*- coding: utf-8 -*-
p = 'Group_31/revised/build_structured_paper.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)


rep("The document review points the same way:",
    "For RQ5, the app reviews show that user grievances are dominated by unpaid rewards (about half of fraud-keyword reviews), failed or unrefunded payments and weak support or account-blocking experiences, while reviews describing unauthorised access or theft are very rare (6 of 5,758). "
    "Two readings are plausible: genuine scam victims may not write app-store reviews, or the apps' reviewers focus on service failures. The reviews therefore do not measure scam prevalence, but they do show where trust breaks down (refunds, support and verification), which fits the trust and dispute-resolution themes in the documents {wbtrust}. "
    "They also show that safety controls can create friction: 104 reviews describe device-lock or security-alert prompts, mostly for one app, so a lock requirement that cannot be met or recognised can block legitimate use. The document review points the same way:")
rep("(Table \" + str(T['sens']) + \"). The base case offers",
    "(Table \" + str(T['sens']) + \"). The base case offers") if False else None
# peer interpretation in discussion
rep("This comparison is indicative only:",
    "Against peer economies (Table \" + str(T['peers']) + \"), India combines near-top account ownership with below-peer phone ownership, a middling lock share and the lowest reported unsolicited-request share among economies with a value, which may reflect lower phone-based contact, differences in recall or reporting, or the smaller share of phone owners. The data cannot separate these explanations. "
    "This comparison is indicative only:")
rep("The qualitative component is a secondary document review, and all financial inputs",
    "The qualitative component rests on a secondary document review and on public app reviews, which are self-selected, cover seven weeks, come from five apps with unequal review counts, are English-language and keyword-coded by a single coder, and are not linked to Findex respondents. "
    "No interviews or surveys of our own were conducted. Peer values are published aggregates without sampling errors. All financial inputs")
rep("Priority extensions are (i) consent-based interviews",
    "Priority extensions are (i) consent-based interviews")
rep("The contribution of the study is therefore",
    "App reviews added that user grievances concern rewards, refunds, support and verification far more than third-party fraud, and a peer comparison placed India near the top on account ownership but below peers on phone ownership. "
    "The contribution of the study is therefore")
open(p, 'w', encoding='utf-8').write(s)
print('ok')
