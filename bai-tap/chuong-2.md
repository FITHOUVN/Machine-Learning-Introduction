# Chương 2 — Tiền xử lý dữ liệu

> Tệp này thuộc **Sách bài tập** của học phần. Nội dung dưới đây được chuyển
> nguyên văn từ phần luyện tập cuối Chương 2 của giáo trình, khi phần đó được
> rút gọn để sách in còn đúng ba phần: câu hỏi ôn tập lý thuyết, một bài thực
> hành, và một chặng của dự án. Mọi câu dẫn "Mục x.y" đều trỏ về giáo trình.

## B. Bài tập tính tay

Làm bằng giấy và bút. Trình bày từng bước tính toán. Có thể dùng máy tính
cầm tay hoặc Python để kiểm lại kết quả, nhưng phần trình bày phải cho thấy
cách tính.

**Bài B.1. Phân tích vấn đề trong tập dữ liệu y tế**

Một bệnh viện chuyên về tim mạch cung cấp bảng sau với dữ liệu của 8 bệnh nhân:

- BN001: Nguyễn A, 65, Nam, 145, 220, có;
- BN002: Trần B, 58, Nữ, 135, 195, có
- BN003: Lê C, 42, Nam, 120, 180, không
- BN004: Phạm D, 55, Nam, (thiếu), 210, có
- BN005: Hoàng E, 350, Nữ, 130, 200, không
- BN006: Đỗ F, 50, Nam, 140, (thiếu), có
- BN007: Bùi G, 60, Nữ, 138, 205, có
- BN008: Nguyễn A, 65, Nam, 145, 220, có
- Các cột: Mã, Họ tên, Tuổi, Giới tính, Huyết áp, Cholesterol, Bệnh tim
- (a) Xác định tất cả các vấn đề có trong tập dữ liệu này, phân loại theo năm nhóm đã học
- (b) Với mỗi vấn đề, đề xuất cách xử lý cụ thể (xóa, thay thế, mã hóa, v.v.) và giải thích lý do
- (c) Sau khi xử lý, tập dữ liệu còn bao nhiêu bản ghi? Tỷ lệ bệnh nhân có bệnh tim trong tập sau xử lý có cân bằng không?

**Bài B.2. Chọn phương pháp phù hợp**

Cho năm tình huống xử lý dữ liệu sau:

- (a) Một cột “loại sản phẩm” trên sàn TMĐT có 5 000 giá trị duy nhất, được dùng làm đầu vào cho mô hình dự đoán doanh số
- (b) Cột “mức độ hài lòng” trong khảo sát: Rất kém, Kém, Bình thường, Tốt, Rất tốt
- (c) Dữ liệu thu nhập tháng của khách hàng (đơn vị triệu đồng) có một số giá trị thiếu, phân phối lệch phải với một số ngoại lai cực đoan
- (d) Dữ liệu nhịp tim ghi nhận liên tục từ đồng hồ thông minh, có khoảng 0,5% giá trị thiếu phân bố ngẫu nhiên (do mất kết nối)
- (e) Tập ảnh chụp X-quang phổi có 4 000 ảnh, mỗi ảnh có khoảng 100 000 điểm ảnh. Với mỗi tình huống, hãy chọn kỹ thuật tiền xử lý phù hợp nhất từ các kỹ thuật đã học trong Chương 2, và giải thích lý do

**Bài B.3. Phát hiện vấn đề trong quy trình**

Một nhóm sinh viên báo cáo quy trình tiền xử lý dữ liệu chấm điểm tín dụng như sau:

- Bước 1. Tải toàn bộ dữ liệu (10 000 bản ghi) từ tệp CSV
- Bước 2. Xóa tất cả các bản ghi có ít nhất một giá trị thiếu, còn lại 8 500 bản ghi
- Bước 3. Tính trung bình và độ lệch chuẩn của các cột số trên 8 500 bản ghi
- Bước 4. Áp dụng Standardization với các tham số vừa tính
- Bước 5. Áp dụng SMOTE để cân bằng tỷ lệ nhãn (từ 5% nợ xấu lên 50%)
- Bước 6. Chia dữ liệu thành 70% tập huấn luyện và 30% tập kiểm tra
- Bước 7. Huấn luyện mô hình trên tập huấn luyện và đánh giá trên tập kiểm tra.
- (a) Quy trình trên có ít nhất ba lỗi nghiêm trọng. Hãy chỉ ra các lỗi và giải thích tại sao chúng là vấn đề
- (b) Đề xuất một quy trình sửa lại đúng, trình bày từng bước theo thứ tự

**Bài B.4. Tính toán chuẩn hóa và phát hiện ngoại lai**

Cho 10 giá trị doanh thu (đơn vị triệu đồng) của 10 cửa hàng trong tháng vừa qua: 45, 50, 55, 60, 48, 52, 58, 65, 70, 500

- (a) Tính trung bình và độ lệch chuẩn của 10 giá trị. Tính Z-score cho mỗi giá trị. Giá trị nào là ngoại lai theo ngưỡng |z| > 3?
- (b) Sắp xếp dãy số, tính Q1, Q3, IQR, cận dưới, cận trên. Giá trị nào là ngoại lai theo phương pháp IQR? So sánh kết quả với câu (a)
- (c) Áp dụng Min-Max Scaling cho từng giá trị (với xmin và xmax của 10 giá trị gốc). Tính từng bước cho ba giá trị đầu tiên
- (d) Áp dụng Standardization (Z-score normalization) cho ba giá trị đầu tiên. Cho biết các giá trị này nằm ở phía dương hay âm của trung bình
- (e) Áp dụng capping: thay giá trị 500 bằng giá trị tại cận trên (từ câu b). Tính lại Min-Max Scaling sau khi cap.
- Gợi ý: Với câu (a): chú ý rằng ngoại lai làm tăng chính độ lệch chuẩn. Theo quy ước độ lệch chuẩn tổng thể dùng thống nhất trong cả chương (Mục 2.3.2 của giáo trình), với n = 10 thì |z| không thể vượt cận trên là căn bậc hai của (n − 1), bằng 3,00; trên dãy số của bài này, z của giá trị 500 chỉ đạt khoảng 2,996 nên không giá trị nào vượt ngưỡng 3. Hãy đối chiếu kết luận này với kết quả của phương pháp IQR ở câu (b) để thấy hạn chế che lấp của Z-score

## C. Bài tập trên máy

Nộp cho mọi bài trong mục C: một tệp Jupyter Notebook chạy lại được từ đầu đến cuối, ghi rõ phiên bản Python và các thư viện đã dùng; các hình đã xuất thành tệp ảnh; và một ghi chú 300 đến 500 từ nêu kết quả chính kèm nhận xét. Mỗi bài trình bày thành một phần riêng, đánh số câu trả lời theo đúng các mục (a), (b), (c) của đề. Nếu bài có bước chuẩn hóa hoặc điền giá trị thiếu, phải ghi rõ bước đó được khớp trên tập nào (Mục 2.1.4 của giáo trình).

> ⚒  Thực hành 2.1. Tiền xử lý tập dữ liệu Wine · 90 phút · Notebook và ghi chú 300 đến 500 từ
> Yêu cầu: Tải tập dữ liệu Wine từ Scikit-learn (sklearn.datasets.load_wine). Tập dữ liệu gồm 178 mẫu rượu vang với 13 đặc trưng số và 1 nhãn phân loại (3 loại rượu).
> Thực hiện các bước sau bằng Python:
> (a) Tải dữ liệu và xem thông tin tổng quan: số mẫu, số đặc trưng, phân bố nhãn.
> (b) Kiểm tra dữ liệu thiếu (Wine vốn không có giá trị thiếu, nhưng cần kiểm tra để hình thành thói quen).
> (c) Tính trung bình, độ lệch chuẩn, min, max cho từng đặc trưng. Có những đặc trưng nào có thang đo rất khác biệt?
> (d) Phát hiện ngoại lai bằng IQR cho cột proline, đặc trưng thứ 13 (chỉ số 12 trong Python). Có bao nhiêu ngoại lai?
> (e) Áp dụng StandardScaler cho toàn bộ ma trận đặc trưng. Kiểm tra sau khi chuẩn hóa, các đặc trưng có trung bình xấp xỉ 0 và độ lệch chuẩn xấp xỉ 1 không.
> (f) Áp dụng PCA giảm từ 13 chiều xuống 2 chiều. Hai thành phần chính giữ lại bao nhiêu phần trăm phương sai?
> Nộp: một tệp Jupyter Notebook chạy lại được, trong đó mỗi câu từ (a) đến (f) là một phần riêng có mã nguồn và kết quả in ra; kèm bảng trung bình, độ lệch chuẩn, min và max của 13 đặc trưng; kèm ghi chú 300 đến 500 từ nhận xét về chênh lệch thang đo giữa các đặc trưng và về tỷ lệ phương sai mà hai thành phần chính giữ lại.
