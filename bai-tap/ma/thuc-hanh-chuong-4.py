# -*- coding: utf-8 -*-
"""Chuong 4, muc B. Thuc hanh -- so sanh ba thuat toan tren nhan mat can bang.

Sinh lai dung cac con so trong bang tu so khop in trong giao trinh.
Chay: python thuc-hanh-chuong-4.py
"""
import os

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import cohen_kappa_score, confusion_matrix
from sklearn.model_selection import (StratifiedKFold, cross_val_predict,
                                     cross_val_score)
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

GOC = os.path.dirname(os.path.abspath(__file__))
TEP = os.path.join(GOC, '..', '..', 'datasets', 'raw', 'dmml_sinhvien.csv')

COT_SO = ['Tuoi', 'DiemTB_HK1', 'SoTinChi', 'SoBuoiVangMat']
COT_PL = ['NganhHoc', 'HinhThucDangKy']

bang = pd.read_csv(TEP)
print('(a) kich thuoc:', bang.shape)
print('    phan bo nhan:', bang['KetQua'].value_counts().to_dict())

X = bang[COT_SO + COT_PL]
y = (bang['KetQua'] == 'Khong dat').astype(int)   # lop duong: Khong dat

tien_xu_ly = ColumnTransformer([
    ('so', Pipeline([('dien', SimpleImputer(strategy='median')),
                     ('chuan', StandardScaler())]), COT_SO),
    ('pl', OneHotEncoder(handle_unknown='ignore'), COT_PL)])

cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
MO_HINH = [
    ('Cay quyet dinh', DecisionTreeClassifier(criterion='entropy',
                                              max_depth=3, random_state=42)),
    ('Naive Bayes', GaussianNB()),
    ('KNN k = 5', KNeighborsClassifier(n_neighbors=5)),
    ('Doi sanh', DummyClassifier(strategy='most_frequent')),
]

print('\n%-16s %8s %8s %8s %8s %8s' % ('Mo hinh', 'Acc', 'std', 'Kappa',
                                       'Sens', 'Spec'))
for ten, mh in MO_HINH:
    pipe = Pipeline([('tien', tien_xu_ly), ('mh', mh)])
    diem = cross_val_score(pipe, X, y, cv=cv, scoring='accuracy')
    du_doan = cross_val_predict(pipe, X, y, cv=cv)
    tn, fp, fn, tp = confusion_matrix(y, du_doan).ravel()
    sens = tp / (tp + fn) if tp + fn else float('nan')
    spec = tn / (tn + fp) if tn + fp else float('nan')
    print('%-16s %8.4f %8.4f %8.4f %8.4f %8.4f'
          % (ten, diem.mean(), diem.std(), cohen_kappa_score(y, du_doan),
             sens, spec))
    print('    tim duoc %d trong %d sinh vien khong dat'
          % (tp, int(y.sum())))
np.set_printoptions(legacy='1.25')
