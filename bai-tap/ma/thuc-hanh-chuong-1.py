# -*- coding: utf-8 -*-
"""Chuong 1, muc B. Thuc hanh -- doc va mo ta du lieu cua du an.

Sinh lai dung cac con so trong bang tu so khop in trong giao trinh.
Chay: python thuc-hanh-chuong-1.py
"""
import os

import pandas as pd

GOC = os.path.dirname(os.path.abspath(__file__))
TEP = os.path.join(GOC, '..', '..', 'datasets', 'raw',
                   'dmml_hoatdong_sinhvien.csv')

bang = pd.read_csv(TEP)

# (a) kich thuoc va kieu du lieu
print('so dong, so cot:', bang.shape)
print(bang.dtypes.to_string())

# (b) thong ke mo ta
print('\n--- describe ---')
print(bang.describe().to_string())

# (c) gia tri thieu
thieu = bang.isna().sum()
print('\n--- gia tri thieu tung cot ---')
print(thieu[thieu > 0].to_string())
print('tong gia tri thieu:', int(thieu.sum()))
so_thieu_moi_dong = bang.isna().sum(axis=1)
print('so ban ghi co it nhat 1 o thieu:', int((so_thieu_moi_dong > 0).sum()))
print('so ban ghi thieu tu 2 o tro len:',
      int((so_thieu_moi_dong >= 2).sum()))

# cac con so khong the dung
print('\nTuoi nho nhat / lon nhat:',
      bang['Tuoi'].min(), '/', bang['Tuoi'].max())
print('SoGioLamThem lon nhat:', bang['SoGioLamThem'].max())
print('Tuoi trung binh: %.3f' % bang['Tuoi'].mean())
print('Tuoi trung vi:', bang['Tuoi'].median())

# (d) phan bo tuoi -- hinh khong in o day, xem notebook cua nguoi hoc

# (e) phan bo mien cu tru
dem = bang['MienCuTru'].value_counts()
ty_le = bang['MienCuTru'].value_counts(normalize=True) * 100
print('\n--- MienCuTru ---')
for mien in dem.index:
    print('%-6s %4d  %.2f%%' % (mien, dem[mien], ty_le[mien]))
