# -*- coding: utf-8 -*-
"""Chuong 3, muc B. Thuc hanh -- sinh du lieu co luat cai san.

Phan dau la doan ma sinh du lieu ma de bai nhac den: 600 giao dich cua mot
quan ca phe voi tam mat hang, hai luat duoc cai san voi Confidence biet truoc.
Hat giong co dinh nen moi nguoi chay ra cung mot tap du lieu.
Chay: python thuc-hanh-chuong-3.py
"""
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
from mlxtend.preprocessing import TransactionEncoder

P_NEN = {'ca phe': 0.35, 'tra sua': 0.30, 'banh ngot': 0.25,
         'sandwich': 0.20, 'salad': 0.30, 'nuoc ep': 0.28,
         'sua chua': 0.12, 'khoai tay': 0.10}


def sinh(hat_giong):
    rng = np.random.default_rng(hat_giong)
    giao_dich = []
    for _ in range(600):
        gd = set()
        while not gd:                  # khong nhan giao dich rong
            gd = {m for m, p in P_NEN.items() if rng.random() < p}
        if 'banh ngot' in gd:          # Luat 1: Confidence muc tieu 0.90
            gd.discard('ca phe')
            if rng.random() < 0.90:
                gd.add('ca phe')
        if 'salad' in gd and 'nuoc ep' in gd:   # Luat 2: muc tieu 0.85
            gd.discard('sua chua')
            if rng.random() < 0.85:
                gd.add('sua chua')
        giao_dich.append(sorted(gd))
    te = TransactionEncoder()
    return pd.DataFrame(te.fit(giao_dich).transform(giao_dich),
                        columns=te.columns_)


def tim_luat(bang_luat, truoc, sau):
    for _, h in bang_luat.iterrows():
        if set(h['antecedents']) == set(truoc) \
                and set(h['consequents']) == set(sau):
            return h
    return None


X = sinh(2026)
print('(a) co ma tran X:', X.shape)
print('Support tam muc don:')
for m in sorted(X.columns):
    print('   %-10s %.4f' % (m, X[m].mean()))

# (b) tap pho bien
tp = apriori(X, min_support=0.05, use_colnames=True)
tp['co'] = tp['itemsets'].apply(len)
print('\n(b) tong tap pho bien o min_support = 0.05:', len(tp))
print('    theo co:', tp['co'].value_counts().sort_index().to_dict())

# (c) hai luat cai san
luat = association_rules(tp, metric='confidence', min_threshold=0.6)
print('\n(c) so luat o min_confidence = 0,6:', len(luat))
for truoc, sau, muc_tieu in ((['banh ngot'], ['ca phe'], 0.90),
                             (['salad', 'nuoc ep'], ['sua chua'], 0.85)):
    h = tim_luat(luat, truoc, sau)
    n_truoc = int(X[truoc].all(axis=1).sum())
    print('    %s => %s  Support %.4f (%d giao dich), Confidence %.4f '
          'tren %d giao dich thoa ve trai, Lift %.4f, lech %.4f'
          % (truoc, sau, h['support'], round(h['support'] * 600),
             h['confidence'], n_truoc, h['lift'],
             abs(h['confidence'] - muc_tieu)))

# (d) anh huong cua nguong
print('\n(d) anh huong cua nguong')
for nguong in (0.20, 0.10, 0.05, 0.03):
    t = apriori(X, min_support=nguong, use_colnames=True)
    r = association_rules(t, metric='confidence', min_threshold=0.6)
    co1 = tim_luat(r, ['banh ngot'], ['ca phe']) is not None
    co2 = tim_luat(r, ['salad', 'nuoc ep'], ['sua chua']) is not None
    print('    nguong %.2f: %3d tap, %2d luat, luat 1 %s, luat 2 %s'
          % (nguong, len(t), len(r), 'co' if co1 else 'khong',
             'co' if co2 else 'khong'))

# (e) cac luat khong duoc cai san
print('\n(e) luat khong duoc cai san o min_support = 0.05')
for _, h in luat.iterrows():
    tr, sa = set(h['antecedents']), set(h['consequents'])
    if (sa == {'ca phe'} and 'banh ngot' in tr and tr != {'banh ngot'}) \
            or sa == {'salad'}:
        print('    %s => %s  Confidence %.4f'
              % (sorted(tr), sorted(sa), h['confidence']))

# (f) fpgrowth va doi hat giong
tp2 = fpgrowth(X, min_support=0.05, use_colnames=True)
bang_a = set(frozenset(s) for s in tp['itemsets'])
bang_f = set(frozenset(s) for s in tp2['itemsets'])
print('\n(f) apriori va fpgrowth cho cung tap pho bien:', bang_a == bang_f)
X7 = sinh(7)
tp7 = apriori(X7, min_support=0.05, use_colnames=True)
luat7 = association_rules(tp7, metric='confidence', min_threshold=0.6)
for truoc, sau in ((['banh ngot'], ['ca phe']),
                   (['salad', 'nuoc ep'], ['sua chua'])):
    h = tim_luat(luat7, truoc, sau)
    print('    hat giong 7: %s => %s  Confidence %.4f'
          % (truoc, sau, h['confidence']) if h is not None
          else '    hat giong 7: khong tim lai duoc %s' % truoc)
