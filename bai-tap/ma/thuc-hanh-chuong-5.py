# -*- coding: utf-8 -*-
"""Chuong 5, muc B. Thuc hanh -- chon so cum va doc chan dung nhom tren Wine.

Sinh lai dung cac con so trong bang tu so khop in trong giao trinh.
Chay: python thuc-hanh-chuong-5.py
"""
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.metrics import davies_bouldin_score, silhouette_score
from sklearn.preprocessing import StandardScaler

du_lieu = load_wine(as_frame=True)
X = du_lieu.data
y_that = du_lieu.target

# (a) thang do cua bon dac trung
print('(a) khoang gia tri va do lech chuan')
for cot in ('proline', 'magnesium', 'malic_acid', 'hue'):
    print('    %-12s min %8.3f  max %8.3f  std %8.3f'
          % (cot, X[cot].min(), X[cot].max(), X[cot].std()))

Xc = StandardScaler().fit_transform(X)

# (b) chon k sau chuan hoa
print('\n(b) sau chuan hoa')
for k in range(2, 7):
    nhan = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(Xc)
    print('    k = %d  Silhouette %.4f  DBI %.4f'
          % (k, silhouette_score(Xc, nhan), davies_bouldin_score(Xc, nhan)))

# (c) khong chuan hoa
print('\n(c) tren du lieu chua chuan hoa')
for k in range(2, 7):
    nhan = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(X)
    print('    k = %d  Silhouette %.4f' % (k, silhouette_score(X, nhan)))

# (d) so K-means voi Agglomerative Ward tai k = 3
K = 3
km = KMeans(n_clusters=K, n_init=10, random_state=42).fit_predict(Xc)
ag = AgglomerativeClustering(n_clusters=K, linkage='ward').fit_predict(Xc)
print('\n(d) tai k = %d' % K)
print('    K-means      Silhouette %.4f  DBI %.4f  co cum %s'
      % (silhouette_score(Xc, km), davies_bouldin_score(Xc, km),
         sorted(np.bincount(km).tolist(), reverse=True)))
print('    Agglo Ward   Silhouette %.4f  DBI %.4f  co cum %s'
      % (silhouette_score(Xc, ag), davies_bouldin_score(Xc, ag),
         sorted(np.bincount(ag).tolist(), reverse=True)))
# khop nhan cum roi dem so mau xep khac nhau
cheo = pd.crosstab(km, ag)
anh_xa = cheo.idxmax(axis=1).to_dict()
khac = int(sum(anh_xa[a] != b for a, b in zip(km, ag)))
print('    so mau hai thuat toan xep khac nhau: %d tren %d' % (khac, len(km)))

# (e) PCA
pca = PCA(n_components=2).fit(Xc)
tl = pca.explained_variance_ratio_
print('\n(e) PCA: %.2f%% va %.2f%%, tong %.2f%%'
      % (tl[0] * 100, tl[1] * 100, tl.sum() * 100))

# (f) chan dung cac cum tren gia tri goc
print('\n(f) chan dung cac cum (gia tri goc)')
chan_dung = X.assign(cum=km).groupby('cum')[
    ['alcohol', 'flavanoids', 'color_intensity', 'proline']].mean()
chan_dung['so_mau'] = np.bincount(km)
print(chan_dung.round(3).to_string())

# (g) bang cheo voi nhan giong nho that
cheo2 = pd.crosstab(km, y_that)
trung = int(cheo2.max(axis=1).sum())
print('\n(g) bang cheo cum voi giong nho that')
print(cheo2.to_string())
print('    %d tren %d mau (%.1f%%) trung voi giong chiem da so trong cum'
      % (trung, len(km), 100.0 * trung / len(km)))
