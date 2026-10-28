# Chương 1 — Tổng quan về khai phá dữ liệu và máy học

> Tệp này thuộc **Sách bài tập** của học phần. Nội dung dưới đây được chuyển
> nguyên văn từ phần luyện tập cuối Chương 1 của giáo trình, khi phần đó được
> rút gọn để sách in còn đúng ba phần: câu hỏi ôn tập lý thuyết, một bài thực
> hành, và một chặng của dự án. Mọi câu dẫn "Mục x.y" đều trỏ về giáo trình.

## B. Bài tập tính tay

Làm bằng giấy và bút. Trình bày từng bước tính toán. Có thể dùng máy tính
cầm tay hoặc Python để kiểm lại kết quả, nhưng phần trình bày phải cho thấy
cách tính.

**Bài B.1. Nhận diện loại bài toán**

Cho năm tình huống thực tế sau đây:

(a) Dự đoán giá thuê nhà tại Hà Nội dựa trên diện tích, vị trí, số phòng ngủ và năm xây

(b) Nhóm các khách hàng của một sàn thương mại điện tử thành các phân khúc có hành vi mua sắm tương tự, để gửi khuyến mãi phù hợp với từng phân khúc

(c) Tìm ra các cặp sản phẩm thường được mua cùng nhau trên một sàn bán lẻ trực tuyến

(d) Phát hiện các giao dịch chuyển khoản bất thường trong hệ thống ngân hàng

(e) Dự đoán một sinh viên có hoàn thành học kỳ hay không, dựa trên dữ liệu học tập trong sáu tuần đầu. Với mỗi tình huống, hãy trả lời:

- Bài toán thuộc nhóm nào trong năm nhóm đã học (phân lớp, hồi quy, phân cụm, khai phá luật kết hợp, phát hiện bất thường)?
- Đây là bài toán mô tả hay dự đoán?
- Sử dụng học có giám sát hay học không giám sát?
- Đầu vào và đầu ra cụ thể là gì?

**Bài B.2. Phân tích thách thức trong một bài toán thực tế**

Một công ty bán lẻ trực tuyến muốn xây dựng hệ thống gợi ý sản phẩm tự động cho khách hàng dựa trên lịch sử mua hàng. Công ty có khoảng 200 000 khách hàng đăng ký, hơn 50 000 sản phẩm, và lịch sử mua hàng được lưu trữ trong ba năm qua. Hãy phân tích các vấn đề sau:

(a) Các nguồn dữ liệu cần thu thập là gì? Dạng dữ liệu chính là có cấu trúc, bán cấu trúc hay không cấu trúc?

(b) Dữ liệu có mất cân bằng không? Nếu có, hãy xác định các nhóm có số lượng mẫu chênh lệch.

(c) Tính giải thích được của mô hình có quan trọng trong bài toán này không? Vì sao?

(d) Quyền riêng tư của khách hàng cần được đảm bảo như thế nào?

(e) Mô hình triển khai có cần được cập nhật theo thời gian không? Giải thích lý do liên quan đến hiện tượng dữ liệu trôi hoặc khái niệm trôi

**Bài B.3. Áp dụng tính toán**

Trong một lớp 100 sinh viên Khoa Công nghệ Thông tin, 65 sinh viên đã hoàn thành môn học và 35 sinh viên không hoàn thành. Sau đó, người ta quan sát thêm đặc trưng “số lần đăng nhập hệ thống học tập trực tuyến dưới 5 lần mỗi tuần trong nửa kỳ đầu”. Trong số 35 sinh viên không hoàn thành, 28 người có đặc trưng này. Trong số 65 sinh viên hoàn thành, 13 người có đặc trưng này.

(a) Tính entropy của tập 100 sinh viên theo trạng thái hoàn thành môn học, trình bày từng bước

(b) Một sinh viên có đặc trưng vừa nêu. Hãy dùng định lý Bayes để tính xác suất sinh viên đó không hoàn thành môn học, trình bày từng bước (tính P(B) qua công thức xác suất toàn phần, sau đó áp dụng Bayes)

(c) So sánh xác suất hậu nghiệm vừa tính với xác suất tiên nghiệm (tỷ lệ không hoàn thành chung). Việc quan sát đặc trưng này làm thay đổi niềm tin theo hướng nào và mức nào?

**Bài B.4. Làm việc với ma trận và khoảng cách**

Một siêu thị thu thập dữ liệu của bốn khách hàng thân thiết, mỗi khách hàng được mô tả bằng ba đặc trưng: số lần mua trong một tháng (cột 1), tổng chi tiêu trong tháng tính theo triệu đồng (cột 2), và số sản phẩm khác nhau đã mua (cột 3). Dữ liệu cụ thể:

- KH-1: (8, 5, 12)
- KH-2: (3, 2, 6)
- KH-3: (10, 7, 15)
- KH-4: (2, 1, 4)
(a) Biểu diễn dữ liệu này dưới dạng ma trận X và ghi rõ kích thước của ma trận. Ý nghĩa của hàng và cột trong ma trận là gì?

(b) Tính khoảng cách Euclidean giữa KH-1 và mỗi khách hàng còn lại, trình bày từng bước cho từng cặp. Sắp xếp các khách hàng còn lại theo độ gần với KH-1, từ gần nhất đến xa nhất

(c) Tính khoảng cách Manhattan giữa KH-1 và mỗi khách hàng còn lại theo từng bước. So sánh thứ tự sắp xếp với kết quả ở câu (b)

(d) Tính giá trị trung bình của mỗi đặc trưng (trung bình theo cột) trên cả bốn khách hàng. Khách hàng nào (KH-1, KH-2, KH-3 hay KH-4) gần nhất với “khách hàng trung bình” này theo khoảng cách Euclidean?

- (e) Gợi ý mở rộng: nếu các đặc trưng có thang đo khác nhau (số lần mua, triệu đồng, số sản phẩm), điều này có thể ảnh hưởng đến kết quả tính khoảng cách như thế nào? Tham khảo lại Mục 1.4.4 của giáo trình về vấn đề lấn át
