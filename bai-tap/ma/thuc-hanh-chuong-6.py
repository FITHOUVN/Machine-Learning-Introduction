# -*- coding: utf-8 -*-
"""Chuong 6, muc B. Thuc hanh -- chi so danh gia cho bai toan da lop mat
can bang.

Phan dau la doan ma tao tap du lieu ma de bai nhac den: muoi lop chu so cua
tap Digits duoc gop thanh ba lop roi lay mau de phan bo con 1265, 174 va 60.
Cau (f) can thu vien imbalanced-learn.
Chay: python thuc-hanh-chuong-6.py
"""
import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import (average_precision_score, classification_report,
                             confusion_matrix, f1_score)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# --- tao tap du lieu
X_goc, y_goc = load_digits(return_X_y=True)
nhom = {0: range(0, 7), 1: [8], 2: [9]}   # gop 10 lop thanh 3 lop
y_moi = np.full(len(y_goc), -1)
for lop, chu_so in nhom.items():
    for c in chu_so:
        y_moi[y_goc == c] = lop
so_mau = {0: 1265, 1: 174, 2: 60}         # lay mau de mat can bang
rng = np.random.RandomState(42)
chon = []
for lop, n in so_mau.items():
    idx = np.where(y_moi == lop)[0]
    chon.append(rng.choice(idx, min(n, len(idx)), replace=False))
chon = np.sort(np.concatenate(chon))
X, y = X_goc[chon], y_moi[chon]
ten_lop = ['0-6', '8', '9']

# --- (a) chia tap
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42)
print('(a) phan bo ca tap:', np.bincount(y).tolist())
print('    phan bo tap kiem tra:', np.bincount(y_te).tolist())


def bao_cao(ten, mh, X_fit, y_fit):
    mh.fit(X_fit, y_fit)
    du_doan = mh.predict(X_te)
    xs = mh.predict_proba(X_te)
    print('\n--- %s ---' % ten)
    print(classification_report(y_te, du_doan, target_names=ten_lop,
                                zero_division=0))
    print('ma tran nham lan:\n', confusion_matrix(y_te, du_doan))
    ket = {}
    for nhan, cach in (('Macro F1', 'macro'), ('Micro F1', 'micro'),
                       ('Weighted F1', 'weighted')):
        ket[nhan] = f1_score(y_te, du_doan, average=cach, zero_division=0)
    ket['Accuracy'] = (du_doan == y_te).mean()
    ket['F1 lop 9'] = f1_score(y_te, du_doan, average=None,
                               zero_division=0)[2]
    print('  '.join('%s %.4f' % (k, v) for k, v in ket.items()))
    for i in range(3):
        moc = (y_te == i).mean()
        pr = average_precision_score((y_te == i).astype(int), xs[:, i])
        print('  lop %-4s PR-AUC %.4f   moc ty le lop duong %.4f'
              % (ten_lop[i], pr, moc))
    return ket


cay = DecisionTreeClassifier(max_depth=4, random_state=42)
k1 = bao_cao('Cay max_depth = 4', cay, X_tr, y_tr)

try:
    from imblearn.over_sampling import SMOTE
    X_sm, y_sm = SMOTE(random_state=42).fit_resample(X_tr, y_tr)
    print('\nsau SMOTE tren tap huan luyen:', np.bincount(y_sm).tolist())
    k2 = bao_cao('Cay max_depth = 4 sau SMOTE',
                 DecisionTreeClassifier(max_depth=4, random_state=42),
                 X_sm, y_sm)
except ImportError:
    print('\nkhong co imbalanced-learn: bo qua cau (f)')
    k2 = None

k3 = bao_cao('Cay khong gioi han do sau',
             DecisionTreeClassifier(random_state=42), X_tr, y_tr)

print('\n(g) bang ba cau hinh')
print('%-28s %9s %9s %9s %11s %9s'
      % ('Cau hinh', 'Accuracy', 'Macro F1', 'Micro F1', 'Weighted F1',
         'F1 lop 9'))
for ten, k in (('max_depth = 4', k1), ('max_depth = 4 + SMOTE', k2),
               ('khong gioi han do sau', k3)):
    if k is None:
        continue
    print('%-28s %9.4f %9.4f %9.4f %11.4f %9.4f'
          % (ten, k['Accuracy'], k['Macro F1'], k['Micro F1'],
             k['Weighted F1'], k['F1 lop 9']))
