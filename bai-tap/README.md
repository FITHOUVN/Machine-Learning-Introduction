# Sách bài tập — Khai phá dữ liệu và máy học

Thư mục này là **Sách bài tập** của học phần. Nó giữ toàn bộ kho bài tập cuối
chương, phần mà sách in không chứa nữa.

## Quan hệ với giáo trình

Mỗi chương của giáo trình kết thúc bằng mục **Luyện tập** gồm đúng ba phần:

| Phần trong sách in | Nội dung |
|---|---|
| A. Câu hỏi ôn tập lý thuyết | các câu hỏi tự kiểm, in đủ trong sách |
| B. Thực hành | **một** bài trên máy, có bảng tự so khớp |
| C. Dự án | một chặng của dự án xuyên suốt sáu chương |

Những bài còn lại — bài tập tính tay và các bài trên máy không được chọn vào
mục B — nằm trong thư mục này, nguyên văn, kèm mọi gợi ý, đáp án và khối
"Kết quả đối chiếu" đi với chúng.

Cách dùng: học lý thuyết trong giáo trình, làm phần A và phần B ngay trong
sách, rồi mở tệp chương tương ứng ở đây để luyện thêm.

## Mục lục

| Tệp | Chương | Bài tính tay | Bài trên máy |
|---|---|---|---|
| [chuong-1.md](chuong-1.md) | 1. Tổng quan về khai phá dữ liệu và máy học | B.1 – B.4 | — |
| [chuong-2.md](chuong-2.md) | 2. Tiền xử lý dữ liệu | B.1 – B.4 | Thực hành 2.1 |
| [chuong-3.md](chuong-3.md) | 3. Khai phá luật kết hợp | B.1 – B.4 | Thực hành 3.2 |
| [chuong-4.md](chuong-4.md) | 4. Phân lớp dữ liệu | B.1 – B.5 | C.2, C.3 |
| [chuong-5.md](chuong-5.md) | 5. Phân cụm dữ liệu | B1 – B10 | — |
| [chuong-6.md](chuong-6.md) | 6. Đánh giá và xây dựng mô hình | b1 – b3 | C.2, C.3, C.4 |

Tổng cộng 37 bài: 30 bài tính tay và 7 bài trên máy.

## Cách đánh số

Số hiệu bài **giữ nguyên như trong giáo trình trước khi rút gọn**, nên không
cần bảng đối chiếu số cũ với số mới. Hai điểm cần biết:

- Mỗi chương từ 1 đến 6 đều có một bài trên máy mang số **C.1** vẫn ở lại
  trong sách in, tại mục B. Thực hành. Vì vậy các tệp ở đây bắt đầu từ C.2.
- Bảng dữ liệu 14 ngày của Bài B.1 và Bài B.2 Chương 4 trong sách in là
  Bảng 4.14; ở đây nó được gọi là Bảng B.1, vì số hiệu bảng của sách không
  còn ý nghĩa ngoài sách.

## Quan hệ với thư mục `ma`

Hai thư mục khác nhau về mục đích:

- `ma` ở gốc kho — bản mã đầy đủ của **các mục thực hành trong thân chương**
  (Mục 2.7, 3.4, 4.4, 5.4 và 6.4), dạng Jupyter Notebook. Không chứa lời giải
  bài tập.
- `bai-tap/ma` — mã tái lập các con số của **bảng tự so khớp** ở mục
  B. Thực hành của sáu chương. Mỗi tệp chạy độc lập, không cần tham số:

| Tệp | Dùng cho | Dữ liệu | Thư viện thêm |
|---|---|---|---|
| [ma/thuc-hanh-chuong-1.py](ma/thuc-hanh-chuong-1.py) | Chương 1 | `datasets/raw/dmml_hoatdong_sinhvien.csv` | — |
| [ma/thuc-hanh-chuong-2.py](ma/thuc-hanh-chuong-2.py) | Chương 2 | `datasets/raw/dmml_hoatdong_sinhvien.csv` | imbalanced-learn |
| [ma/thuc-hanh-chuong-3.py](ma/thuc-hanh-chuong-3.py) | Chương 3 | tự sinh, hạt giống 2026 | mlxtend |
| [ma/thuc-hanh-chuong-4.py](ma/thuc-hanh-chuong-4.py) | Chương 4 | `datasets/raw/dmml_sinhvien.csv` | — |
| [ma/thuc-hanh-chuong-5.py](ma/thuc-hanh-chuong-5.py) | Chương 5 | `sklearn.datasets.load_wine` | — |
| [ma/thuc-hanh-chuong-6.py](ma/thuc-hanh-chuong-6.py) | Chương 6 | `sklearn.datasets.load_digits` | imbalanced-learn |

Chạy một tệp:

```
python bai-tap/ma/thuc-hanh-chuong-1.py
```

Các con số trong tệp này được đo bằng scikit-learn 1.9.0, pandas 3.0.3,
numpy 2.4.6, mlxtend 0.25.0 và imbalanced-learn 0.14.2. Đổi phiên bản thư
viện có thể làm lệch vài chữ số thập phân cuối.

Thư mục `bai-tap/ma` **không** chứa lời giải của các bài trong thư mục này.
