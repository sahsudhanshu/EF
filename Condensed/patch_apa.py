# -*- coding: utf-8 -*-
"""Switch the paper to APA author-year citations with an alphabetical reference list (as in the TA's reference paper and journal article),
add the roadmap sentence to 1.4 and the institution line on the title block."""
p = 'Condensed/build_short_paper.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)


# ---- citation labels and APA in-text citations
i = s.index("def cite(m):"); j = s.index("doc = Document()")
new_cite = '''OVERRIDE = {9: 'World Bank, 2025b', 38: 'World Bank, 2025a', 37: 'Development Research Group, 2025', 39: 'Google Play Store, 2026',
            40: 'World Bank, n.d.-b', 41: 'World Bank, n.d.-a', 42: 'Reserve Bank of India, 2020', 47: 'Apple Inc., 2026',
            48: 'Google Play Store & Apple App Store, 2026', 45: 'World Bank, n.d.-c', 46: 'Press Information Bureau, 2026'}


def label(k):
    """APA parenthetical label, e.g. 'Suri & Jack, 2016' or 'Demirguc-Kunt et al., 2017'."""
    if k in OVERRIDE:
        return OVERRIDE[k]
    t = REFS[k]
    head = t[:t.index(' (')]
    year = re.match(r'\\((\\d{4}|n\\.d\\.)', t[len(head) + 1:]).group(1)
    names = re.findall(r"(?:^|, |& )([^,&]+?), (?:[A-Z]\\.(?:[ -]|(?=,)|$))+", head + ',')
    if not names:
        names = [head.rstrip('.')]
    if len(names) == 1:
        a = names[0]
    elif len(names) == 2:
        a = names[0] + ' & ' + names[1]
    else:
        a = names[0] + ' et al.'
    return f'{a}, {year}'


def cite(m):
    labs = []
    for k in m.group(1).split(','):
        k = int(k)
        assert k in REFS, k
        if k not in order:
            order.append(k)
        labs.append(label(k))
    return '(' + '; '.join(sorted(set(labs), key=lambda x: x.lower())) + ')'


def cites(t):
    return re.sub(r'\\{(\\d+(?:,\\d+)*)\\}', cite, t)


'''
s = s[:i] + new_cite + s[j:]

# ---- year suffixes for same-author same-year entries (APA)
SUFFIX_CODE = ("REFS.update(SHORT)" + chr(10) +
               "for _k, _a, _b in [(38, '(2025)', '(2025a)'), (9, '(2025)', '(2025b)'), (41, '(n.d.)', '(n.d.-a)'), (40, '(n.d.)', '(n.d.-b)')]:" + chr(10) +
               "    REFS[_k] = REFS[_k].replace(_a, _b, 1)" + chr(10))
rep("REFS.update(SHORT)" + chr(10), SUFFIX_CODE)

# ---- alphabetical reference list, no numbers
i = s.index("H1('References')")
j = s.index("doc.core_properties.title")
s = s[:i] + '''H1('References')
for k in sorted(order, key=lambda x: re.sub(r'[^a-z0-9 ]', '', REFS[x].lower().replace('ü', 'u'))):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.35); p.paragraph_format.first_line_indent = Inches(-0.35)
    p.paragraph_format.space_after = Pt(2); p.paragraph_format.line_spacing = 1.0
    add_runs(p, REFS[k])
''' + s[j:]

# ---- title block: institution (as on the TA's reference paper) and course
rep("P('Group 31, Entrepreneurial Finance', align='c')", "P('Group 31, Entrepreneurial Finance | Indian Institute of Information Technology, Allahabad', align='c')")

# ---- roadmap sentence at the end of 1.4 (as in the journal article)
rep("RQ6: What price, cost and customer numbers would let an institution-funded safety service break even?\")",
    "RQ6: What price, cost and customer numbers would let an institution-funded safety service break even? \"\n  \"The paper is organised as follows. Section 2 reviews the literature, Section 3 sets out the methodology, Section 4 reports the results, Section 5 discusses their academic, policy and managerial implications and limitations, and Section 6 concludes.\")")
open(p, 'w', encoding='utf-8').write(s)
print('apa patched')
