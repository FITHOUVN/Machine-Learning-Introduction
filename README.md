# Gói dữ liệu — Nhập môn Khai phá dữ liệu và Máy học

Dữ liệu đi kèm giáo trình **Nhập môn Khai phá dữ liệu và Máy học**
(Khoa Công nghệ Thông tin, Trường Đại học Mở Hà Nội — mã học phần 7E1015.22).

## Cách lấy

Bấm **Code → Download ZIP**, hoặc:

```bash
git clone https://github.com/FITHOUVN/Machine-Learning-Introduction.git
```

Giải nén rồi mở terminal **tại thư mục gốc** của kho, và giữ nguyên cấu trúc
thư mục. Mọi đường dẫn trong giáo trình đều tính từ đây, ví dụ
`pd.read_csv('datasets/raw/dmml_sinhvien.csv')`.

Khi làm bài, hãy ghi lại **mã commit** của kho trong báo cáo. Dữ liệu có thể
được cập nhật; ghi mã commit để sau này tái lập được đúng con số đã nộp.

## Cấu trúc

```
datasets/
  raw/     dữ liệu cho các bài thực hành lớn và dự án sáu chặng
  micro/   dữ liệu của các ví dụ tính tay trong sách
```

## `datasets/raw/` — thực hành và dự án

| Tệp | Dùng ở | Kích thước |
|---|---|---|
| `dmml_sinhvien.csv` | Mục 2.7 (toàn bộ Phần A–E), Mục 2.4, Phụ lục B | 200 × 8 |
| `dmml_hoatdong_sinhvien.csv` | Dự án sáu chặng, từ Chương 1 đến Chương 6 | 800 × 8 |
| `ung_thu_vu_wdbc.csv` | bản dự phòng khi không có mạng | 569 × 31 |

### `dmml_sinhvien.csv` — đăng ký môn học

Mô phỏng thông tin đăng ký môn học của 200 sinh viên. Dữ liệu được thiết kế để
minh họa đúng các vấn đề tiền xử lý của Chương 2: giá trị thiếu, ngoại lai do
lỗi nhập liệu, và nhãn mất cân bằng.

| Cột | Kiểu | Miền giá trị | Ghi chú |
|---|---|---|---|
| `MaSV` | định danh | SV001–SV200 | không đưa vào ma trận đặc trưng |
| `Tuoi` | số thực | 5–150 | **12 giá trị thiếu**; ba ngoại lai 5, 99, 150 |
| `DiemTB_HK1` | số thực | 1,52–4,00 | thang điểm 4 |
| `SoTinChi` | số nguyên | 12, 15, 18, 21, 24 | |
| `SoBuoiVangMat` | số nguyên | 0–7 | |
| `NganhHoc` | phân loại | CNTT, HTTT, ATTT | |
| `HinhThucDangKy` | phân loại | Truc tiep, Truc tuyen | |
| `KetQua` | nhãn | Dat (170), Khong dat (30) | mất cân bằng 85/15 |

Ba giá trị tuổi 5, 99 và 150 là lỗi nhập liệu được cố ý đưa vào để minh họa
phương pháp IQR ở Mục 2.3.2; sau khi loại bỏ còn 197 bản ghi.

### `dmml_hoatdong_sinhvien.csv` — hoạt động học tập (dự án)

Ghi nhận hoạt động học tập của 800 sinh viên, dùng xuyên suốt dự án sáu chặng
"Hệ thống cảnh báo sớm và hỗ trợ sinh viên". Đây là dữ liệu tổng hợp, không
phải hồ sơ sinh viên thật, nhưng được thiết kế theo đặc thù của một trường đại
học mở, nơi phần lớn người học vừa đi làm vừa đi học.

| Cột | Kiểu | Miền giá trị | Ý nghĩa |
|---|---|---|---|
| `MaSV` | định danh | SV0001–SV0800 | không đưa vào ma trận đặc trưng |
| `Tuoi` | số nguyên | 3–118 | tuổi; **36 giá trị thiếu**, có ngoại lai |
| `SoGioLamThem` | số nguyên | 0–480 | số giờ làm thêm mỗi tháng; **24 giá trị thiếu**, có ngoại lai |
| `DiemChuyenCan` | số thực | 14–100 | điểm chuyên cần |
| `SoLanNopBai` | số nguyên | 2–95 | số lần nộp bài mỗi tháng; có ngoại lai |
| `TyLeHocTrucTuyen` | số thực | 0,264–1,000 | tỷ lệ hoạt động học trực tuyến; **20 giá trị thiếu** |
| `TyLeNopMuon` | số thực | 0,000–0,540 | tỷ lệ bài nộp muộn |
| `MienCuTru` | phân loại | Bac, Trung, Nam | miền cư trú |

Các giá trị tuổi 3 và 118, số giờ làm thêm 390–480 và số lần nộp bài 95 là lỗi
nhập liệu cố ý, phục vụ Chặng 2 (so sánh Z-score với IQR). Z-score và IQR cho
số ngoại lai khác nhau — đó là nội dung cần giải thích, không phải lỗi dữ liệu.

Nhãn `NguyCo` của Chặng 4 không có sẵn trong tệp: người học tự tạo theo quy tắc
`DiemChuyenCan < 50` như đề bài nêu. Khi đó nhóm nguy cơ cao chiếm khoảng 27,6%.

### `ung_thu_vu_wdbc.csv` — Breast Cancer Wisconsin

**Giáo trình không đọc tệp này.** Mọi đoạn mã dùng bộ Wisconsin Diagnostic đều
nạp trực tiếp qua `sklearn.datasets.load_breast_cancer()`, nên bình thường
không cần tới tệp. Tệp được giữ lại chỉ để làm bản dự phòng cho người học
không có mạng khi làm bài.

569 mẫu × 30 đặc trưng. Lưu ý về nhãn: cột `ac_tinh` trong tệp này đã mã hóa
**1 là ác tính** (212 ác tính, 357 lành tính), tức tương đương với
`(target == 0).astype(int)` mà giáo trình hướng dẫn. Nhãn `target` gốc của
scikit-learn thì ngược lại: 0 là ác tính. Nếu đối chiếu kết quả giữa hai
đường, phải thống nhất quy ước nhãn trước.

## `datasets/micro/` — ví dụ tính tay

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

## `datasets/weka/` — tám tập dữ liệu đi kèm WEKA

Đây là **bản sao dự phòng**, giữ nguyên không sửa một ký tự. Nguồn chính thức
là kho của Đại học Waikato, nhóm tác giả WEKA:

```
https://git.cms.waikato.ac.nz/weka/weka/-/raw/main/trunk/wekadocs/data/<tên tệp>
```

Tám tệp này vốn nằm trong thư mục `data` của WEKA sau khi cài đặt. Kho chép
lại để người học tải được trực tiếp mà không cần cài WEKA, và để đường dẫn
trong giáo trình không hỏng nếu kho gốc đổi địa chỉ.

| Tệp | Dùng ở | Bản ghi | Thuộc tính | Lớp |
|---|---|---|---|---|
| `iris.arff` | Chương 4, Chương 5, Phụ lục A | 150 | 4 | 3 |
| `weather.nominal.arff` | Phụ lục A | 14 | 4 | 2 |
| `supermarket.arff` | Mục 3.4 | 4 627 | 217 | – |
| `breast-cancer.arff` | Mục 6.4, Phụ lục A | 286 | 9 | 2 |
| `diabetes.arff` | Phụ lục A, bài tập | 768 | 8 | 2 |
| `vote.arff` | Phụ lục A | 435 | 16 | 2 |
| `glass.arff` | Phụ lục A, bài tập | 214 | 9 | 7 |
| `soybean.arff` | Phụ lục A | 683 | 35 | 19 |

### Ghi công bắt buộc

Phần đầu mỗi tệp `.arff` chứa nguyên văn thông tin xuất xứ do người tạo dữ
liệu yêu cầu. **Giữ nguyên phần đó khi sao chép hoặc trích dẫn.** Riêng
`breast-cancer.arff` có yêu cầu ghi công tường minh: dữ liệu do Viện Ung bướu,
Trung tâm Y khoa Đại học Ljubljana cung cấp, với lời cảm ơn hai bác sĩ
M. Zwitter và M. Soklic.

`supermarket.arff` không kèm thông tin xuất xứ nào; tệp được phát hành cùng
WEKA và chép lại nguyên trạng từ đó.

### Hai điều cần biết khi đọc bằng Python

**Thứ nhất — ngưỡng Support của WEKA không phải là tỷ lệ.** WEKA hiển thị
`Minimum support: 0.15 (694 instances)`: nó nhân 0,15 × 4 627 = 694,05 rồi
**làm tròn xuống** 694 và lọc theo số đếm đó. `mlxtend` lại lọc theo tỷ lệ,
tức đòi số đếm từ 694,05 trở lên, nghĩa là từ 695. Muốn ra đúng kết quả WEKA
thì phải viết:

```python
nguong = 694 / 4627        # KHÔNG phải 0.15
fi = apriori(X, min_support=nguong, use_colnames=True, max_len=6)
```

Dùng đúng ngưỡng này, `mlxtend` cho lại y hệt WEKA: L(1)=44, L(2)=380,
L(3)=910, L(4)=633, L(5)=105, L(6)=1, và luật mạnh nhất
`biscuits + frozen foods + fruit + total=high` ⇒ `bread and cake` với
788 ⇒ 723, Confidence 0,9175, Lift 1,27.

**Thứ hai — `soybean.arff` không nạp được bằng `scipy.io.arff`.** Dòng khai
báo nhãn của thuộc tính `crop-hist` có một dấu cách thừa trước giá trị cuối
(`, same-lst-sev-yrs`), nên `scipy` coi đó là một nhãn khác với giá trị thật
trong phần dữ liệu và báo lỗi. WEKA bỏ qua dấu cách này. Giáo trình chỉ dùng
`soybean.arff` trong WEKA nên không ảnh hưởng; nếu cần đọc bằng Python thì xóa
dấu cách đó trong bản sao của mình.

## Dữ liệu lấy từ nơi khác

Một số bộ dữ liệu trong giáo trình **không nằm ở kho này**:

- Tám tệp `.arff` của WEKA nay đã có bản sao trong `datasets/weka/`; xem mục
  riêng ở trên. Chúng cũng có sẵn trong thư mục `data` của WEKA sau khi cài.
- Iris, Wine, Breast Cancer, Diabetes bản scikit-learn — tải trực tiếp bằng
  `sklearn.datasets.load_*`, không cần tệp ngoài.

## Môi trường

Các con số đối chiếu in trong giáo trình được kiểm lại với Python 3.11,
scikit-learn 1.8 và 1.9, pandas 2 và 3, NumPy 2, imbalanced-learn 0.14. Cài
thư viện trong một môi trường ảo và lưu danh sách phiên bản thực tế bằng
`python -m pip freeze > requirements-lock.txt` để tái lập kết quả.

Lưu ý: cần scikit-learn **1.8 trở lên**, vì các ví dụ phạt L1 ở Chương 6 dùng
`LogisticRegression(l1_ratio=1.0, solver='saga')`; với bản cũ hơn, tham số này
bị bỏ qua và mô hình âm thầm quay về phạt L2.

## Ghi chú

Tệp `dataset_dangky_monhoc.csv` ở thư mục gốc có nội dung **trùng hoàn toàn**
với `datasets/raw/dmml_sinhvien.csv`, được giữ lại cho các bản phát trước. Hãy
dùng đường dẫn trong `datasets/raw/` như giáo trình hướng dẫn.

## Giấy phép

Xem tệp `LICENSE`.
