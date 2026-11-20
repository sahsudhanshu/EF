# Codebook for the second coder, round 2 (Part C: 122 App Store and bank-app reviews)

You are re-coding public app reviews that contain a fraud-type keyword. Read each review in `PartC_coding_sheet_BLANK.csv` and enter ONE letter in `your_code_letter`. There is no answer key in this folder: do not look for one. Do not discuss individual reviews with the first coders until you are done.

Code what the reviewer actually describes, not the word they use. Many reviews call an app "fraud" or "scam" when they mean something milder.

| Letter | Category | Use when the review mainly describes... |
|---|---|---|
| A | Reward, cashback or offer not honoured | Promised cashback, referral reward, coupon or offer not received or smaller than shown. Called a scam or fraud. |
| B | Money debited, payment failed or refund missing | Money taken but recharge/payment not completed, or refund not returned. |
| C | Blocked account, mis-selling or poor grievance handling | Account blocked, products sold without consent, complaints ignored, no way to reach support. |
| D | Spam, permissions, privacy or intrusive security controls | Notifications/ads, mandatory permissions, data being sold, security prompts that get in the way. |
| E | General accusation, no specific incident | Calls the app a fraud/fake/thief but gives no specific incident. |
| F | Praise or no complaint | Positive review, or mentions fraud only to praise ("no fraud", "blocked a scam"). |
| G | Unauthorised access, theft or hacking (reported or feared) | Says money or data was taken without permission, account hacked, or a phishing/scam message was received. |

Tie-break rules: if a review fits two, pick the one the reviewer spends the most words on. If the reviewer reports a specific loss of money through a failed payment (B) and also calls it a scam, use B. Use E only if nothing more specific is described. Write doubts in `notes`.


Round 2 notes
- The 122 reviews come from the Apple App Store (payment apps) and from bank mobile-banking apps. Many are about banks (charges, blocked accounts, support) rather than payment apps. Category C covers blocked accounts, mis-selling, unexpected charges and poor grievance handling. Category D covers spam calls or notifications, mandatory permissions and security prompts such as 'unauthorised app detected'. Use E only if no specific incident is described.
- It takes about one hour. Two people can split it (C001 to C061 and C062 to C122); each person then fills only their half.
- Enter ONE letter per row in `your_code_letter`. Send the file back; do not discuss individual reviews with the first coders first.
