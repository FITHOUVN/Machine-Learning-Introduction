# Thực hành bằng WEKA

Thư mục này là phần hướng dẫn chi tiết về WEKA của học phần **Nhập môn Khai
phá dữ liệu và Máy học** (Khoa Công nghệ Thông tin, Trường Đại học Mở Hà
Nội, mã học phần 7E1015.22).

Giáo trình in chỉ giữ phần giới thiệu và hướng dẫn cài đặt WEKA ở Phụ lục A.
Toàn bộ phần thao tác, đọc kết quả và ba bài thực hành đặt ở đây, vì nội
dung đó bám theo giao diện và phiên bản phần mềm nên cần cập nhật theo từng
năm học, trong khi sách in giữ nguyên qua nhiều khóa.

Thân sách thực hành bằng Python với scikit-learn và mlxtend. Ba bài dưới đây
là **bản làm bằng giao diện đồ họa của cùng những bài đó**: đọc được độc
lập, không thay thế phần thực hành bằng Python, và dùng để đối chiếu hai
công cụ trên cùng một tập dữ liệu.

## Nội dung

| Tệp | Nội dung | Ứng với |
|---|---|---|
| [01-su-dung-weka.md](01-su-dung-weka.md) | Định dạng ARFF · WEKA Explorer · quy trình thực hành · cách đọc Classifier output · các tập dữ liệu có sẵn · bộ lọc · dòng lệnh · lỗi thường gặp · tài nguyên học thêm | Phụ lục A |
| [02-thuc-hanh-chuong-3.md](02-thuc-hanh-chuong-3.md) | Khai phá luật kết hợp trên tập `supermarket.arff` | Mục 3.4 |
| [03-thuc-hanh-chuong-4.md](03-thuc-hanh-chuong-4.md) | Phân lớp tập Iris với sáu thuật toán | Mục 4.4 |
| [04-thuc-hanh-chuong-6.md](04-thuc-hanh-chuong-6.md) | Đánh giá mô hình, phát hiện và xử lý quá khớp | Mục 6.4 |
| `hinh/` | Ảnh chụp màn hình các tab và hộp thoại được nhắc trong tài liệu | |

## Dữ liệu

Các tệp `.arff` dùng trong ba bài thực hành nằm ở
[`../datasets/weka/`](../datasets/weka). Chúng vốn có sẵn trong thư mục
`data` của WEKA; bản lưu ở đây để bài thực hành không phụ thuộc vào máy chủ
của Đại học Waikato.

## Cần có trước

Cài WEKA theo hướng dẫn ở **Mục A.2 của giáo trình**. Tài liệu trong thư mục
này giả định WEKA đã chạy được và người học đã mở được cửa sổ WEKA GUI
Chooser.

## Quy ước

Số hiệu bảng và hình trong mỗi tệp là số hiệu riêng của tệp đó, không liên
quan đến số hiệu trong sách in. Khi tài liệu dẫn "Mục 4.4 của giáo trình"
thì đó là mục trong sách, không phải tệp trong thư mục này.

## Tài liệu tham khảo

[1] Witten, I. H., Frank, E., Hall, M. A., & Pal, C. J. (2016). *Data
Mining: Practical Machine Learning Tools and Techniques* (4th ed.). Morgan
Kaufmann.

[2] Bouckaert, R. R., Frank, E., Hall, M., Kirkby, R., Reutemann, P.,
Seewald, A., & Scuse, D. (2018). *WEKA Manual for Version 3-9-3*. University
of Waikato.

[3] WEKA Wiki. https://waikato.github.io/weka-wiki/

[4] Hall, M., Frank, E., Holmes, G., Pfahringer, B., Reutemann, P., &
Witten, I. H. (2009). The WEKA Data Mining Software: An Update. *ACM SIGKDD
Explorations*, 11(1), 10–18.

[5] Witten, I. H. *Data Mining with Weka* MOOC.
https://www.futurelearn.com/courses/data-mining-with-weka
