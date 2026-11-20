"""Extra figures for the 12-page paper (all numbers from the paper's tables). Run from the project root."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'Times New Roman'
TEAL, BLUE, AMBER, NAVY, GREY = '#1B8A7E', '#2A5FA5', '#D98A1F', '#122B45', '#8A94A0'
OUT = 'Condensed/'


def clean(ax):
    for s in ('top', 'right'): ax.spines[s].set_visible(False)


def labels(ax, bars, fmt='{:.1f}%', dx=1.0, fs=10, horizontal=True):
    for b in bars:
        v = b.get_width() if horizontal else b.get_height()
        if horizontal: ax.text(v + dx, b.get_y() + b.get_height() / 2, fmt.format(v), va='center', fontsize=fs)
        else: ax.text(b.get_x() + b.get_width() / 2, v + dx, fmt.format(v), ha='center', fontsize=fs)


# 1 access vs use + gender
fig, (a, b) = plt.subplots(1, 2, figsize=(7.4, 2.7), gridspec_kw={'width_ratios': [1.25, 1]})
bars = a.barh(['Account ownership', 'Phone ownership', 'Digital payment use'], [89.0, 66.5, 48.5], color=[TEAL, BLUE, AMBER], height=0.6)
a.invert_yaxis(); a.set_xlim(0, 108); labels(a, bars); a.set_xlabel('% of all adults (n = 3,000)', fontsize=10); clean(a)
a.tick_params(labelsize=10)
x = np.arange(2); w = 0.35
b1 = b.bar(x - w / 2, [42.7, 50.3], w, color=TEAL, label='Women'); b2 = b.bar(x + w / 2, [54.1, 62.7], w, color=BLUE, label='Men')
b.set_xticks(x); b.set_xticklabels(['Digital payment\n(all adults)', 'Phone lock\n(phone owners)'], fontsize=10); b.set_ylim(0, 80)
labels(b, b1, dx=1, horizontal=False, fs=9); labels(b, b2, dx=1, horizontal=False, fs=9); b.legend(fontsize=9, frameon=False, loc='upper left'); clean(b); b.tick_params(labelsize=10)
plt.tight_layout(); plt.savefig(OUT + 'pfig_access_gender.png', dpi=220); plt.close()

# 2 device lock by group
cats = ['Age 15–24', 'Highest income quintile', 'Men', 'Women', 'Lowest income quintile', 'Age 60+']
vals = [75.7, 75.2, 62.7, 50.3, 40.6, 22.9]
fig, ax = plt.subplots(figsize=(7.0, 2.8))
bars = ax.barh(cats, vals, color=[TEAL, TEAL, BLUE, BLUE, AMBER, AMBER], height=0.62); ax.invert_yaxis(); ax.set_xlim(0, 92)
labels(ax, bars); ax.axvline(57.7, color=NAVY, ls='--', lw=1); ax.text(86, 5.6, 'dashed line: all phone owners, 57.7%', fontsize=9, color=NAVY, ha='right')
ax.set_xlabel('Phone has a PIN, password or fingerprint lock (% of phone owners)', fontsize=10); clean(ax); ax.tick_params(labelsize=10)
plt.tight_layout(); plt.savefig(OUT + 'pfig_lock_groups.png', dpi=220); plt.close()

# 3 exposure and sending money
fig, (a, b) = plt.subplots(1, 2, figsize=(7.2, 2.7))
bars = a.bar(['Payment users', 'Non-users'], [13.1, 4.3], color=[AMBER, BLUE], width=0.55); labels(a, bars, dx=0.3, horizontal=False, fs=11)
a.set_ylim(0, 17); a.set_ylabel('Reported an unsolicited\nmoney request (%)', fontsize=10); clean(a); a.tick_params(labelsize=10)
a.text(0.5, 15.2, 'adjusted odds ratio 3.45\n(2.24 to 5.30)', ha='center', fontsize=9.5, color=NAVY)
bars = b.bar(['With a lock\n(39 of 170)', 'Without a lock\n(6 of 49)'], [25.0, 8.9], color=[TEAL, GREY], width=0.55); labels(b, bars, dx=0.7, horizontal=False, fs=11)
b.set_ylim(0, 33); b.set_ylabel('Sent money after a\nrequest (%)', fontsize=10); clean(b); b.tick_params(labelsize=10)
b.text(0.5, 29.5, 'Fisher exact p = 0.11\n(not significant)', ha='center', fontsize=9.5, color=NAVY)
plt.tight_layout(); plt.savefig(OUT + 'pfig_exposure.png', dpi=220); plt.close()

# 4 payment use vs lock by group
cats = ['Women', 'Men', '15–24', '25–39', '40–59', '60+', 'Income Q1', 'Income Q5']
pay = [42.7, 54.1, 43.5, 51.3, 46.6, 56.6, 34.8, 67.4]; lock = [50.3, 62.7, 75.7, 62.7, 43.6, 22.9, 40.6, 75.2]
x = np.arange(len(cats)); w = 0.38
fig, ax = plt.subplots(figsize=(7.2, 2.9))
b1 = ax.bar(x - w / 2, pay, w, color=BLUE, label='Digital payment use (all adults)'); b2 = ax.bar(x + w / 2, lock, w, color=TEAL, label='Phone lock (phone owners)')
for bb in list(b1) + list(b2): ax.text(bb.get_x() + bb.get_width() / 2, bb.get_height() + 1, f'{bb.get_height():.0f}', ha='center', fontsize=8.5)
ax.set_xticks(x); ax.set_xticklabels(cats, fontsize=10); ax.set_ylim(0, 92); ax.set_ylabel('% of group', fontsize=10); ax.legend(fontsize=9, frameon=False, ncol=2, loc='upper left'); clean(ax)
ax.annotate('+33.7 points', xy=(5, 60), xytext=(5.15, 80), fontsize=9.5, color='#B8860B', ha='center', arrowprops=dict(arrowstyle='-', color='#B8860B'))
plt.tight_layout(); plt.savefig(OUT + 'pfig_gap_groups.png', dpi=220); plt.close()

# 5 published studies: themes
themes = ['Social engineering', 'Trust in counterparty or bank', 'Low awareness or literacy', 'Weak support or redress', 'Family and informal advice', 'Gender, age, vulnerability', 'Protective advice, design cues', 'Merchant and business harms']
counts = [5, 5, 5, 4, 4, 3, 2, 2]
fig, ax = plt.subplots(figsize=(7.0, 2.8))
bars = ax.barh(themes, counts, color=[TEAL] * 3 + [BLUE] * 2 + [AMBER] + [GREY] * 2, height=0.62); ax.invert_yaxis(); ax.set_xlim(0, 5.8)
for bb, v in zip(bars, counts): ax.text(v + 0.08, bb.get_y() + bb.get_height() / 2, f'{v} of 5', va='center', fontsize=10)
ax.set_xlabel('Number of the five published studies reporting the theme', fontsize=10); ax.set_xticks(range(0, 6)); clean(ax); ax.tick_params(labelsize=10)
plt.tight_layout(); plt.savefig(OUT + 'pfig_studies.png', dpi=220); plt.close()

# 6 finance scenarios
fig, ax = plt.subplots(figsize=(7.0, 2.9))
yrs = [1, 2, 3]
for lab, v, c, m in [('Conservative (fee INR 40,000)', [-36.80, -30.00, -17.44], AMBER, 'o'), ('Base (INR 50,000)', [-32.80, 0.00, 52.16], BLUE, 's'), ('Optimistic (INR 60,000)', [-24.00, 48.80, 173.16], TEAL, '^')]:
    ax.plot(yrs, v, marker=m, color=c, lw=2, label=lab)
    for k, (xx, yy) in enumerate(zip(yrs, v)):
        off = {'Conservative (fee INR 40,000)': (-0.2, -16), 'Base (INR 50,000)': (-0.2, 8), 'Optimistic (INR 60,000)': (-0.2, 8)}[lab] if k == 0 else (0.05, 7 if yy >= 0 else -15)
        ax.text(xx + off[0], yy + off[1], f'{yy:.1f}', fontsize=8.5, color=c)
ax.axhline(0, color=NAVY, lw=0.8); ax.set_xticks(yrs); ax.set_xticklabels(['Year 1', 'Year 2', 'Year 3'], fontsize=10); ax.set_xlim(0.8, 3.35); ax.set_ylim(-55, 195)
ax.set_ylabel('Operating surplus or deficit\n(INR lakh)', fontsize=10); ax.legend(fontsize=9, frameon=False, loc='upper left'); clean(ax)
plt.tight_layout(); plt.savefig(OUT + 'pfig_finance.png', dpi=220); plt.close()
print('figures ok')
