# Mã nguồn các mục thực hành

Năm tệp Jupyter Notebook dưới đây là **bản đầy đủ, chạy được từ đầu đến
cuối** của năm mục thực hành trong giáo trình **Nhập môn Khai phá dữ liệu và
Máy học** (Khoa Công nghệ Thông tin, Trường Đại học Mở Hà Nội, mã học phần
7E1015.22).

Sách in giữ lại những đoạn mã ngắn mang ý chính — thứ để đọc và hiểu. Những
khối dài hơn hai mươi lăm dòng, gồm phần nhập thư viện, vẽ biểu đồ và định
dạng kết quả, đặt ở đây — thứ để chạy. Mỗi chỗ như vậy trong sách đều ghi rõ
tệp tương ứng.

| Tệp | Mục | Nội dung |
|---|---|---|
| [muc-2-7-tien-xu-ly.ipynb](muc-2-7-tien-xu-ly.ipynb) | 2.7 | Làm sạch, tích hợp, biến đổi, rút gọn chiều, chia tập và cân bằng nhãn |
| [muc-3-4-luat-ket-hop.ipynb](muc-3-4-luat-ket-hop.ipynb) | 3.4 | Apriori và FP-Growth trên tập `supermarket.arff`, rời rạc hóa dữ liệu số |
| [muc-4-4-phan-lop.ipynb](muc-4-4-phan-lop.ipynb) | 4.4 | Sáu thuật toán phân lớp trên tập Iris, kiểm chứng chéo 10 phần |
| [muc-5-4-phan-cum.ipynb](muc-5-4-phan-cum.ipynb) | 5.4 | K-means, Agglomerative, GMM, DBSCAN; chọn số cụm bằng Silhouette và DBI |
| [muc-6-4-danh-gia.ipynb](muc-6-4-danh-gia.ipynb) | 6.4 | Đánh giá mô hình, phát hiện quá khớp, chính quy hóa, tối ưu siêu tham số, đóng gói |

## Cách chạy

Mỗi notebook chạy **tuần tự từ trên xuống**: ô sau dùng lại biến của ô
trước. Chạy lẻ một ô ở giữa sẽ báo lỗi thiếu biến.

Mở terminal **tại thư mục gốc của kho** rồi khởi động Jupyter, vì mọi đường
dẫn dữ liệu trong notebook đều tính từ đó:

```bash
git clone https://github.com/FITHOUVN/Machine-Learning-Introduction.git
cd Machine-Learning-Introduction
python -m pip install -r requirements.txt   # nếu có, hoặc xem Phụ lục B
jupyter notebook ma/
```

Hai ô cuối của `muc-6-4-danh-gia.ipynb` dựng một máy chủ Flask rồi gọi thử
nó. Hai ô đó phải chạy ở **hai tiến trình riêng**: chạy ô máy chủ trong một
cửa sổ terminal, rồi gọi thử từ cửa sổ khác. Chạy nối tiếp trong cùng một
notebook sẽ bị treo, vì máy chủ không tự trả quyền điều khiển.

## Đối chiếu kết quả

Mỗi notebook giữ nguyên các khối **Kết quả đối chiếu** của sách, đặt ngay
dưới ô mã sinh ra chúng. Con số in trong sách và trong notebook là cùng một
lần chạy; nếu máy của người học cho số khác thì nguyên nhân thường là phiên
bản thư viện, không phải lỗi mã — xem phần Môi trường ở
[README của kho](../README.md).

## Lưu ý về bài tập

Thư mục này **chỉ chứa mã của các mục thực hành trong thân sách**. Mã lời
giải cho các bài ở mục "Câu hỏi ôn tập" của từng chương không đặt ở đây, vì
đó là phần người học phải tự viết.
