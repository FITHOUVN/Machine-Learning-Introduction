# -*- coding: utf-8 -*-
"""Chuong 2, muc B. Thuc hanh -- dien gia tri thieu, ghep bang, can bang nhan.

Sinh lai dung cac con so trong bang tu so khop in trong giao trinh.
Cau (d) va (e) can thu vien imbalanced-learn.
Chay: python thuc-hanh-chuong-2.py
"""
import os

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

GOC = os.path.dirname(os.path.abspath(__file__))
TEP = os.path.join(GOC, '..', '..', 'datasets', 'raw',
                   'dmml_hoatdong_sinhvien.csv')

bang = pd.read_csv(TEP)
COT_SO = ['Tuoi', 'SoGioLamThem', 'DiemChuyenCan', 'SoLanNopBai',
          'TyLeHocTrucTuyen', 'TyLeNopMuon']

# --- (a) ghep hai bang mo phong hai nguon du lieu
ho_so = bang[['MaSV', 'Tuoi', 'MienCuTru']]
con_lai = [c for c in bang.columns if c not in ('MaSV', 'Tuoi', 'MienCuTru')]
hoat_dong = bang[['MaSV'] + con_lai].head(760)
print('--- (a) ghep bang ---')
for cach in ('inner', 'left', 'outer'):
    g = pd.merge(ho_so, hoat_dong, on='MaSV', how=cach)
    print('%-6s %4d ban ghi, %2d o thieu o DiemChuyenCan'
          % (cach, len(g), int(g['DiemChuyenCan'].isna().sum())))

# --- (b) dien gia tri thieu
print('\n--- (b) dien gia tri thieu ---')
print('do lech chuan Tuoi tren 764 gia tri khong thieu: %.4f'
      % bang['Tuoi'].std())
trung_vi = bang[['Tuoi', 'SoGioLamThem', 'TyLeHocTrucTuyen']].median()
print('trung vi: Tuoi %.1f  SoGioLamThem %.1f  TyLeHocTrucTuyen %.3f'
      % (trung_vi['Tuoi'], trung_vi['SoGioLamThem'],
         trung_vi['TyLeHocTrucTuyen']))
da_dien = {}
for cach in ('median', 'mean'):
    imp = SimpleImputer(strategy=cach)
    X = pd.DataFrame(imp.fit_transform(bang[COT_SO]), columns=COT_SO)
    da_dien[cach] = X
    print('%-7s con thieu %d o, std Tuoi %.4f'
          % (cach, int(X.isna().sum().sum()), X['Tuoi'].std()))

# --- (c) tao nhan
print('\n--- (c) nhan NguyCoRatCao ---')
X = da_dien['median'].copy()
y = (X['DiemChuyenCan'] < 40).astype(int)
print('lop 0: %d   lop 1: %d   ty le lop thieu so %.2f%%'
      % (int((y == 0).sum()), int((y == 1).sum()), 100.0 * y.mean()))
y50 = (X['DiemChuyenCan'] < 50).astype(int)
print('neu lay nguong 50 nhu Chang 4: %.2f%%' % (100.0 * y50.mean()))
X = X.drop(columns=['DiemChuyenCan'])

# --- (d) SMOTE dung cach: chi tren tap huan luyen
try:
    from imblearn.over_sampling import SMOTE
except ImportError:
    print('\nkhong co imbalanced-learn: bo qua cau (d) va (e)')
    raise SystemExit(0)

print('\n--- (d) SMOTE tren tap huan luyen ---')
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)
print('train truoc SMOTE: lop 0 = %d, lop 1 = %d'
      % (int((y_tr == 0).sum()), int((y_tr == 1).sum())))
sm = SMOTE(k_neighbors=5, random_state=42)
X_sm, y_sm = sm.fit_resample(X_tr, y_tr)
print('train sau  SMOTE: lop 0 = %d, lop 1 = %d, tong %d (sinh them %d)'
      % (int((y_sm == 0).sum()), int((y_sm == 1).sum()), len(y_sm),
         len(y_sm) - len(y_tr)))
print('test giu nguyen: lop 0 = %d, lop 1 = %d'
      % (int((y_te == 0).sum()), int((y_te == 1).sum())))

# --- (e) lam sai co kiem soat: SMOTE truoc khi chia
print('\n--- (e) SMOTE truoc khi chia (sai) ---')
X_all, y_all = SMOTE(k_neighbors=5, random_state=42).fit_resample(X, y)
print('sau SMOTE toan bo: lop 0 = %d, lop 1 = %d, tong %d'
      % (int((y_all == 0).sum()), int((y_all == 1).sum()), len(y_all)))
_, _, y_tr2, y_te2 = train_test_split(
    X_all, y_all, test_size=0.2, stratify=y_all, random_state=42)
print('test cua cach sai: %d ban ghi (lop 0 = %d, lop 1 = %d)'
      % (len(y_te2), int((y_te2 == 0).sum()), int((y_te2 == 1).sum())))
