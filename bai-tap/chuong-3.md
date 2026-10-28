# Chương 3 — Khai phá luật kết hợp

> Tệp này thuộc **Sách bài tập** của học phần. Nội dung dưới đây được chuyển
> nguyên văn từ phần luyện tập cuối Chương 3 của giáo trình, khi phần đó được
> rút gọn để sách in còn đúng ba phần: câu hỏi ôn tập lý thuyết, một bài thực
> hành, và một chặng của dự án. Mọi câu dẫn "Mục x.y" đều trỏ về giáo trình.

## B. Bài tập tính tay

Làm bằng giấy và bút. Trình bày từng bước tính toán. Có thể dùng máy tính
cầm tay hoặc Python để kiểm lại kết quả, nhưng phần trình bày phải cho thấy
cách tính.

**Bài B.1. Tính support và confidence**

Cho 8 giao dịch của một cửa hàng bánh ngọt:

T1: {bánh kem, trà sữa};

T2: {bánh kem, cà phê, kem};

T3: {trà sữa, cà phê};

T4: {bánh kem, trà sữa, kem};

T5: {cà phê};

T6: {bánh kem, trà sữa, cà phê, kem};

T7: {bánh kem, kem};

T8: {trà sữa, kem}.

- (a) Tính support cho từng mục riêng lẻ: bánh kem, trà sữa, cà phê, kem
- (b) Tính support cho các cặp: {bánh kem, trà sữa}, {bánh kem, kem}, {trà sữa, kem}, {cà phê, kem}
- (c) Tính confidence cho các luật: bánh kem → kem, kem → bánh kem, trà sữa → bánh kem, cà phê → kem
- (d) Với min_support = 0.4 và min_confidence = 0.6, luật nào trong câu (c) là luật mạnh?

**Bài B.2. Chạy Apriori thủ công**

Cho 6 giao dịch:

T1: {A, B, D};

T2: {A, C, D};

T3: {A, B, C, D};

T4: {B, C};

T5: {A, B, D, E};

T6: {A, C, D, E}.

Với min_support = 0.5 (tương ứng 3 giao dịch):

- (a) Tìm L1 (tập mục phổ biến cỡ 1) bằng cách đếm support
- (b) Sinh C2 từ L1, tính support và xác định L2
- (c) Sinh C3 từ L2, áp dụng tính chất Apriori để cắt nhánh sớm, xác định L3
- (d) Sinh tất cả các luật từ L2 và L3. Với min_confidence = 0.7, liệt kê các luật mạnh

**Bài B.3. Xây dựng FP-Tree**

Sử dụng lại dữ liệu của Bài B.2 với min_support = 0.5:

- (a) Đếm support cho từng mục riêng lẻ và sắp xếp giảm dần
- (b) Sắp xếp lại các mục trong từng giao dịch theo thứ tự ở (a)
- (c) Vẽ FP-Tree bằng cách chèn từng giao dịch một, ghi rõ số đếm trên mỗi nút
- (d) Lập bảng tiêu đề (header table) gồm tên mục, tổng support và mô tả vị trí các nút trong cây
- (e) So sánh với kết quả Bài B.2: hai thuật toán có cho cùng tập mục phổ biến không?

**Bài B.4. Luật định lượng**

Cho bảng dữ liệu khách hàng của một showroom xe máy điện:

KH1: tuổi 22, thu nhập 10tr, vùng nông thôn, mua A.

KH2: tuổi 30, thu nhập 25tr, vùng thành thị, mua B

KH3: tuổi 45, thu nhập 60tr, vùng thành thị, mua C

KH4: tuổi 26, thu nhập 12tr, vùng nông thôn, mua A

KH5: tuổi 32, thu nhập 28tr, vùng thành thị, mua B

KH6: tuổi 50, thu nhập 70tr, vùng thành thị, mua C

KH7: tuổi 24, thu nhập 11tr, vùng nông thôn, mua A

- (a) Đề xuất cách phân khoảng cho hai thuộc tính số. Giải thích lý do.
- (b) Chuyển mỗi khách hàng thành một “giao dịch”
- (c) Với min_support = 0.3, tìm tất cả các tập mục phổ biến
- (d) Liệt kê ít nhất 3 luật định lượng có confidence cao và có ý nghĩa thực tế cho showroom

## C. Bài tập trên máy

Nộp cho mọi bài trong mục C: một tệp Jupyter Notebook chạy lại được từ đầu đến cuối, ghi rõ phiên bản Python và các thư viện đã dùng; các hình đã xuất thành tệp ảnh; và một ghi chú 300 đến 500 từ nêu kết quả chính kèm nhận xét. Mỗi bài trình bày thành một phần riêng, đánh số câu trả lời theo đúng các mục (a), (b), (c) của đề. Kèm bảng số tập phổ biến theo cỡ và số luật ở từng ngưỡng để đối chiếu với các con số in trong Mục 3.4 của giáo trình.

> ⚒  Thực hành 3.2. Khảo sát ngưỡng và độ đo trên tập dữ liệu Supermarket · 120 phút · Notebook và báo cáo 2 đến 3 trang
> Yêu cầu: Bài này tiếp nối Mục 3.4.2 của giáo trình và làm hoàn toàn bằng Python. Dùng lại ma trận nhị phân X cỡ (4627, 218) đã dựng ở Bước 3 của Mục 3.4.1 của giáo trình, giữ nguyên tham số max_len=6 và môi trường thư viện đã khai ở Mục 3.4.1 của giáo trình. Ghi lại phiên bản mlxtend cùng cấu hình máy, vì câu (c) có đo thời gian chạy.
> (a) Chạy apriori ở bốn ngưỡng min_support: 0,20, ngưỡng 694/4627 của bài thực hành, 0,10 và 0,05. Với mỗi ngưỡng, lập một bảng gồm số tập phổ biến theo từng cỡ, tổng số tập phổ biến, và số luật mà association_rules trả về khi lọc theo metric='confidence' với min_threshold=0.9. Giải thích vì sao tổng số tập phổ biến tăng rất nhanh khi hạ ngưỡng, và vì sao ở một trong bốn ngưỡng bảng luật lại rỗng; đối chiếu cách giải thích với Lỗi 4 ở Mục 3.4.5 của giáo trình.
> (b) Giữ ngưỡng 694/4627 và sinh luật hai lần: lần thứ nhất với metric='confidence' và min_threshold=0.9, lần thứ hai với metric='lift' và min_threshold=1.2. Lấy top 10 của mỗi bảng theo đúng chỉ số đã lọc rồi so hai danh sách: có bao nhiêu luật xuất hiện ở cả hai? Vế phải của top 10 theo Confidence có đặc điểm chung gì? Dùng công thức Lift ở Mục 3.3.1 của giáo trình cùng Support nền của mặt hàng bread and cake (Bước 4, Mục 3.4.2 của giáo trình) để giải thích hiện tượng.
> (c) Đo thời gian chạy của apriori và fpgrowth tại ba ngưỡng 0,20, 0,10 và 0,05; mỗi ngưỡng chạy ba lần và lấy giá trị nhỏ nhất, theo cách đã làm ở Mục 3.4.3 của giáo trình. Lập bảng bốn cột: ngưỡng, thời gian apriori, thời gian fpgrowth, tỷ số thời gian fpgrowth chia cho apriori. Tỷ số đó đổi theo ngưỡng như thế nào, và xu hướng có khớp với nhận xét ở Mục 3.4.3 của giáo trình không?
> (d) Viết báo cáo 2 đến 3 trang gồm: ba bảng số của các câu (a) đến (c); năm luật mà người học cho là đáng dùng nhất kèm lý do chọn; ba đề xuất ứng dụng kinh doanh cho chuỗi siêu thị, mỗi đề xuất dẫn ra luật làm căn cứ.
> Kết quả đối chiếu. Các số dưới đây đo bằng mlxtend 0.25.0 trên ma trận nhị phân (4627, 218) với max_len=6.
> Câu (a), số tập phổ biến: ngưỡng 0,20 cho 640 tập (cỡ 1: 38; cỡ 2: 225; cỡ 3: 297; cỡ 4: 78; cỡ 5: 2); ngưỡng 694/4627 cho 2 073 tập (44; 380; 910; 633; 105; 1); ngưỡng 0,10 cho 10 262 tập (52; 634; 2 598; 3 950; 2 470; 558); ngưỡng 0,05 cho 116 707 tập (71; 1 121; 7 573; 25 119; 42 786; 40 037).
> Câu (a), số luật khi lọc theo metric='confidence' với min_threshold=0.9: ngưỡng 0,20 cho 0 luật, ngưỡng 694/4627 cho 16 luật, ngưỡng 0,10 cho 438 luật, ngưỡng 0,05 cho 10 959 luật. Bảng luật rỗng ở ngưỡng 0,20 vì ở ngưỡng đó không tập phổ biến nào sinh được luật đạt Confidence 0,9.
> Câu (b): ở ngưỡng 694/4627, metric='confidence' với min_threshold=0.9 cho 16 luật, còn metric='lift' với min_threshold=1.2 cho 12 442 luật; hai danh sách top 10 không có luật nào trùng nhau. Cả mười luật trong top theo Confidence đều có vế phải là bread and cake, Confidence từ 0,9051 đến 0,9175 nhưng Lift chỉ từ 1,2576 đến 1,2749. Top mười theo Lift có Lift từ 1,8827 đến 1,9075 trong khi Confidence chỉ từ 0,4258 đến 0,6922; luật dẫn đầu là total=high ⇒ biscuits, frozen foods, tissues-paper prd với Support 0,1604, Confidence 0,4419 và Lift 1,9075.
> Câu (c): thời gian tuyệt đối phụ thuộc máy, chỉ xu hướng là cố định. Trên máy biên soạn, tỷ số thời gian fpgrowth chia cho apriori giảm từ khoảng 13,6 ở ngưỡng 0,20 xuống khoảng 4,3 ở ngưỡng 0,10 và khoảng 1,0 ở ngưỡng 0,05, đúng chiều với nhận xét ở Mục 3.4.3 của giáo trình rằng lợi thế nghiêng dần về FP-Growth khi ngưỡng hạ.
> Nộp: một tệp Jupyter Notebook chạy lại được từ đầu đến cuối và báo cáo 2 đến 3 trang theo câu (d).
