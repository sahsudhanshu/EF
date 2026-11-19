# Codebook for the second coder (Part A)

You are re-coding public app reviews that contain a fraud-type keyword. Read each review in `PartA_coding_sheet_BLANK.csv` and enter ONE letter in `your_code_letter`. Do not open `PartA_answer_key_DO_NOT_OPEN.csv` until you have finished. Do not discuss individual reviews with the first coders until you are done.

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

# Part B (about 20 minutes)

`PartB_missed_fraud_check_BLANK.csv` has 60 random reviews that the keyword dictionary did NOT flag as fraud. For each, answer `yes` or `no` in `describes_fraud_or_unauthorised_use_yes_no`: does the review describe a scam, theft, hacking or unauthorised use of money or data? This tests whether the keyword search missed real fraud reports.

# When finished

Run, from this folder:

    python3 compute_agreement.py PartA_coding_sheet_BLANK.csv PartA_answer_key_DO_NOT_OPEN.csv PartB_missed_fraud_check_BLANK.csv

Report the numbers in the paper (see `../PLAN.md`, step 2). The coder's name and date go in the paper's acknowledgements or methods ("coded by <name>, a member of the group / an independent peer").
