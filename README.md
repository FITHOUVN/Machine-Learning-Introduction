# Gói dữ liệu — Nhập môn Khai phá dữ liệu và Máy học

Kho dữ liệu đi kèm giáo trình **Nhập môn Khai phá dữ liệu và Máy học**
(Khoa Công nghệ Thông tin, Trường Đại học Mở Hà Nội — mã học phần 7E1015.22).

## Cách lấy

Bấm **Code → Download ZIP**, hoặc:

```bash
git clone https://github.com/FITHOUVN/Machine-Learning-Introduction.git
```

Giải nén rồi mở terminal **tại thư mục gốc** của kho. Mọi đường dẫn trong
giáo trình đều tính từ đây, ví dụ `pd.read_csv('datasets/micro/ch5_hac_5cuonsach.csv')`.

## Cấu trúc

```
datasets/
  micro/   dữ liệu của các ví dụ tính tay trong sách
  raw/     dữ liệu cho các bài thực hành lớn
```

### `datasets/micro/` — ví dụ tính tay

Mỗi tệp ứng với một ví dụ được giải từng bước trong giáo trình. Số liệu khớp
đúng với sách, nên người học tính tay xong có thể chạy mã để đối chiếu.

| Tệp | Dùng ở | Nội dung |
|---|---|---|
| `ch3_giohang_5giaodich.csv` | Mục 3.1 | 5 giao dịch siêu thị, ma trận nhị phân |
| `ch3_giohang_6giaodich.csv` | Mục 3.2 | 6 giao dịch tiệm tạp hóa (Apriori, FP-Growth) |
| `ch4_knn_10khachhang.csv` | Mục 4.2.1 | 10 khách hàng, nhãn trả nợ đúng/trễ hạn |
| `ch4_nb_6email.csv` | Mục 4.2.2 | 6 email, nhãn rác/hợp lệ |
| `ch4_dtree_10benhnhan.csv` | Mục 4.2.3 | 10 bệnh nhân, nhãn bệnh tim |
| `ch5_kmeans_6khachhang.csv` | Mục 5.2.1 | 6 khách hàng quán cà phê |
| `ch5_fcm_6nguoidung.csv` | Mục 5.2.2 | 6 người dùng ứng dụng nhạc |
| `ch5_dbscan_10tram.csv` | Mục 5.2.3 | 10 trạm thu hồi xe đạp |
| `ch5_hac_5cuonsach.csv` | Mục 5.2.5 | 5 cuốn sách thư viện |

Hai tệp giỏ hàng ở dạng **ma trận nhị phân** (1 là có mặt trong giao dịch,
0 là không), dùng thẳng được với `mlxtend`:

```python
import pandas as pd
from mlxtend.frequent_patterns import apriori

df = pd.read_csv('datasets/micro/ch3_giohang_6giaodich.csv', index_col='GiaoDich')
frequent = apriori(df.astype(bool), min_support=0.5, use_colnames=True)
```

### `datasets/raw/` — bài thực hành lớn

| Tệp | Dùng ở | Nội dung |
|---|---|---|
| `ung_thu_vu_wdbc.csv` | Mục 2.5.1 | Breast Cancer Wisconsin, 569 mẫu × 30 đặc trưng, cột nhãn `ac_tinh` (1 là ác tính) |

## Dữ liệu lấy từ nơi khác

Một số bộ dữ liệu trong giáo trình **không nằm ở kho này**:

- `iris.arff`, `breast-cancer.arff`, `supermarket.arff`, `diabetes.arff`,
  `weather.nominal.arff`, `glass.arff`, `vote.arff` — có sẵn trong thư mục
  `data` của WEKA sau khi cài đặt.
- Iris, Wine, Breast Cancer, Diabetes bản scikit-learn — tải trực tiếp bằng
  `sklearn.datasets.load_*`, không cần tệp ngoài.

## Đang cập nhật

Các tệp sau được giáo trình nhắc tới nhưng chưa có trong kho:

- `datasets/raw/dmml_sinhvien.csv` — dataset chuẩn 200 bản ghi × 8 cột
  dùng cho toàn bộ bài thực hành Mục 2.7
- `datasets/raw/dmml_hoatdong_sinhvien.csv` — dữ liệu hoạt động, dùng ở
  Mục 2.4.1 (tích hợp dữ liệu) và bài tập Chương 2
- `datasets/micro/ch4_logistic_6sinhvien.csv` — 6 sinh viên, các cột
  `MaSV, DiemTB, GioLMS, Dat`, dùng ở Mục 4.2.6

## Giấy phép

Xem tệp `LICENSE`.
