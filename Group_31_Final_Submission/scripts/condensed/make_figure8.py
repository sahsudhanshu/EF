"""Figure: classification of fraud-keyword reviews by category and dataset (shares, %). Run from the project root."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'Times New Roman'
cats = ['Reward or cashback not honoured', 'Money debited, failed payment', 'Blocked account, mis-selling, grievance', 'Spam, permissions, intrusive security', 'General accusation', 'Praise or no complaint', 'Unauthorised access or theft']
play = np.array([60, 15, 11, 10, 9, 7, 6]) / 118 * 100
app = np.array([17, 11, 10, 7, 6, 4, 2]) / 57 * 100
bank = np.array([3, 4, 25, 13, 14, 3, 3]) / 65 * 100
y = np.arange(len(cats)); h = 0.26
fig, ax = plt.subplots(figsize=(7.4, 3.6))
for off, vals, lab, col in [(-h, play, 'Payment apps, Google Play (n = 118)', '#D98A1F'), (0, app, 'Payment apps, App Store (n = 57)', '#2A5FA5'), (h, bank, 'Bank apps (n = 65)', '#1B8A7E')]:
    ax.barh(y + off, vals, h, label=lab, color=col)
    for yy, v in zip(y + off, vals):
        ax.text(v + 0.6, yy, f'{v:.0f}', va='center', fontsize=8)
ax.set_yticks(y); ax.set_yticklabels(cats, fontsize=9); ax.invert_yaxis()
ax.set_xlabel('Share of fraud-keyword reviews in the dataset (%)', fontsize=9); ax.set_xlim(0, 58)
for s in ('top', 'right'): ax.spines[s].set_visible(False)
ax.legend(fontsize=8, loc='lower right', frameon=False)
plt.tight_layout(); plt.savefig('Condensed/figure8_review_categories.png', dpi=220)
print('ok')
