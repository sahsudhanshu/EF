# -*- coding: utf-8 -*-
p = 'Condensed/build_short_deck.py'
s = open(p, encoding='utf-8').read()
i = s.index("# 7 ---------------------------------------------------------------- results: adoption")
j = s.index("# 8 ---------------------------------------------------------------- results: exposure")
new = '''# 7 ---------------------------------------------------------------- results: adoption
s = slide('4  Results: access vs active use', 'Access is not the same as active digital use',
          'Account 89.0, phone 66.5, digital payment 48.5: a 40.6-point gap between owning an account and making or receiving a digital payment. Women 42.7 vs men 54.1 (11.5 points). Denominator: all 3,000 adults, survey-weighted. The survey does not show why women use less.')
cd = CategoryChartData(); cd.categories = ['Account ownership', 'Phone ownership', 'Digital payment use']
cd.add_series('Share of adults (%)', (89.0, 66.5, 48.5))
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.6), Inches(1.65), Inches(7.3), Inches(3.3), cd); ch = gf.chart
style_chart(ch, legend=False, size=14); ch.category_axis.reverse_order = True; ch.value_axis.maximum_scale = 100; ch.plots[0].gap_width = 55
pts = ch.plots[0].series[0].points
for k, c in enumerate([TEAL, BLUE, AMBER]):
    pts[k].format.fill.solid(); pts[k].format.fill.fore_color.rgb = c
ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.number_format = '0.0"%"'; ch.plots[0].data_labels.number_format_is_linked = False; ch.plots[0].data_labels.font.size = Pt(16); ch.plots[0].data_labels.font.bold = True
box(s, 0.6, 5.1, 7.3, 1.35, PALE); box(s, 0.6, 5.1, 0.08, 1.35, TEAL)
text(s, 0.85, 5.15, 6.9, 1.25, 'Core finding: 89.0% owned an account, but only 48.5% made or received a digital payment, a 40.6 percentage-point gap (from unrounded results). Phone ownership is 66.5%.', 15, False, INK, anchor=MSO_ANCHOR.MIDDLE)
text(s, 8.3, 1.7, 4.4, 0.4, 'GENDER DIFFERENCE IN DIGITAL PAYMENT USE', 12, True, TEAL)
stat(s, 8.3, 2.15, 2.1, '42.7%', 'women made or received digital payments', TEAL, 1.85)
stat(s, 10.6, 2.15, 2.1, '54.1%', 'men made or received digital payments', BLUE, 1.85)
bullets(s, 8.3, 4.2, 4.4, 2.3, ['Gap|11.5 percentage points in the sample.', 'Caution|the survey does not show whether access, confidence or social factors cause the gap.'], 14, 8)
src(s, 'Account, phone and digital payment shares refer to all 3,000 surveyed adults; survey-weighted. Source: authors\\' calculations, India Global Findex 2024 microdata.')

# 7b --------------------------------------------------------------- device lock by group
s = slide('4  Results: device protection', 'Device-lock adoption differs sharply by group',
          'Lock 57.7 overall (n = 2,141 valid phone owners). Age 15-24 75.7, highest income quintile 75.2, men 62.7, women 50.3, lowest income quintile 40.6, ages 60+ 22.9. Subgroups overlap; denominator is phone owners, not all adults. A lock protects a handset, not judgment.')
cd = CategoryChartData(); cd.categories = ['Age 15–24', 'Highest income quintile', 'Men', 'Women', 'Lowest income quintile', 'Age 60+']
cd.add_series('Phone has a lock (% of phone owners)', (75.7, 75.2, 62.7, 50.3, 40.6, 22.9))
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.6), Inches(1.65), Inches(7.6), Inches(4.85), cd); ch = gf.chart
style_chart(ch, legend=False, size=14); ch.category_axis.reverse_order = True; ch.value_axis.maximum_scale = 100; ch.plots[0].gap_width = 50
pts = ch.plots[0].series[0].points
for k, c in enumerate([TEAL, TEAL, BLUE, BLUE, AMBER, AMBER]):
    pts[k].format.fill.solid(); pts[k].format.fill.fore_color.rgb = c
ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.number_format = '0.0"%"'; ch.plots[0].data_labels.number_format_is_linked = False; ch.plots[0].data_labels.font.size = Pt(15); ch.plots[0].data_labels.font.bold = True
stat(s, 8.6, 1.75, 4.1, '57.7%', 'of phone owners with valid responses report a PIN, password or fingerprint lock (n = 2,141)', NAVY, 1.9)
bullets(s, 8.6, 3.9, 4.1, 2.6, ['Age gap|75.7% at ages 15 to 24 vs 22.9% at 60 and above.', 'Careful|subgroups overlap, and lock shares use phone owners as the denominator, not all adults.'], 14, 8)
src(s, 'Survey-weighted, phone owners with valid responses. Source: authors\\' calculations, India Global Findex 2024 microdata.')

'''
s = s[:i] + new + s[j:]
open(p, 'w', encoding='utf-8').write(s)
print('deck patched')
