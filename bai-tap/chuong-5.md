# Chương 5 — Phân cụm dữ liệu

> Tệp này thuộc **Sách bài tập** của học phần. Nội dung dưới đây được chuyển
> nguyên văn từ phần luyện tập cuối Chương 5 của giáo trình, khi phần đó được
> rút gọn để sách in còn đúng ba phần: câu hỏi ôn tập lý thuyết, một bài thực
> hành, và một chặng của dự án. Mọi câu dẫn "Mục x.y" đều trỏ về giáo trình.

## B. Bài tập tính tay

Làm bằng giấy và bút. Trình bày từng bước tính toán. Có thể dùng máy tính
cầm tay hoặc Python để kiểm lại kết quả, nhưng phần trình bày phải cho thấy
cách tính.

**Phân tích tình huống**

B1. Một sàn TMĐT có 1 triệu khách hàng. Cần phân nhóm để có chiến lược tiếp thị khác nhau. Hãy trình bày:

- (a) Chọn các đặc trưng nào?
- (b) Tiền xử lý ra sao?
- (c) Thử thuật toán nào và vì sao? Loại bỏ thuật toán nào và tại sao?
- (d) Đánh giá kết quả bằng chỉ số nào?
B2. Bệnh viện có dữ liệu 5000 bệnh nhân tiểu đường với 12 chỉ số sinh hóa. Muốn phân nhóm để cá nhân hóa điều trị. Một bác sĩ muốn biết chính xác xác suất mỗi bệnh nhân thuộc nhóm 'nguy cơ cao biến chứng' để quyết định mức can thiệp

- (a) Thuật toán nào phù hợp nhất? Vì sao?
- (b) Có nhược điểm gì cần lưu ý?
B3. Một hệ thống phát hiện gian lận giao dịch ngân hàng cần phát hiện các giao dịch bất thường mà không có sẵn nhãn 'gian lận / hợp lệ'. Số lượng giao dịch hợp lệ chiếm > 99%, gian lận rất hiếm. Thuật toán nào phù hợp và làm sao xác định gian lận từ kết quả phân cụm?

B4. Một thư viện trực tuyến có 50 000 sách. Muốn phân loại theo chủ đề tự động dựa trên nội dung. Mỗi sách được biểu diễn bằng vectơ TF-IDF 5000 chiều (rất thưa)

- (a) Khoảng cách nào phù hợp? Vì sao?
- (b) Thuật toán phân cụm nào nên chọn? Vì sao? B5. Giả sử áp dụng K-means k = 3 cho tập dữ liệu và được Silhouette = 0,15. Người khác chạy DBSCAN trên cùng tập dữ liệu được 5 cụm và 30 điểm nhiễu, Silhouette = 0,75 (chỉ tính trên các điểm trong cụm). Hãy diễn giải kết quả này

**Tính toán thủ công trên tập dữ liệu nhỏ**

B6. Cho dữ liệu 6 điểm: A(1, 2), B(2, 1), C(2, 3), D(8, 7), E(9, 8), F(7, 9). Áp dụng K-means với k = 2 và centroid khởi tạo (1, 1) và (8, 8). Thực hiện đầy đủ các vòng lặp đến khi hội tụ. Ghi rõ centroid mỗi vòng.

B7. Cùng dữ liệu trên, áp dụng K-medoids với medoid khởi tạo là A và D. Thực hiện một vòng lặp đầy đủ (gán cụm, thử thay medoid). Báo cáo medoid sau vòng đó.

B8. Cho dữ liệu 5 điểm: P1(0, 0), P2(0, 1), P3(1, 0), P4(3, 3), P5(3, 4). Tính ma trận khoảng cách Euclidean ban đầu. Áp dụng Agglomerative với Single linkage. Vẽ dendrogram (mô tả) và cho biết phân hoạch khi cắt ở độ cao 2.

B9. Lặp lại Bài B8 với Complete linkage và Average linkage. So sánh dendrogram. Phương pháp nào cho cụm chặt hơn?

B10. Cho kết quả phân cụm: Cụm 1 = {(1, 1), (2, 1), (1, 2)}, Cụm 2 = {(8, 8), (9, 9)}. Tính:

- (a) a(điểm (1, 1)) và b(điểm (1, 1)). Từ đó tính s((1, 1))
- (b) Silhouette toàn cục cho toàn bộ 5 điểm
- (c) Davies-Bouldin Index cho phân cụm này
- (d) Phân cụm này tốt hay không? Vì sao?
