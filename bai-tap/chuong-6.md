# Chương 6 — Đánh giá và xây dựng mô hình

> Tệp này thuộc **Sách bài tập** của học phần. Nội dung dưới đây được chuyển
> nguyên văn từ phần luyện tập cuối Chương 6 của giáo trình, khi phần đó được
> rút gọn để sách in còn đúng ba phần: câu hỏi ôn tập lý thuyết, một bài thực
> hành, và một chặng của dự án. Mọi câu dẫn "Mục x.y" đều trỏ về giáo trình.

## B. Bài tập tính tay

Làm bằng giấy và bút. Trình bày từng bước tính toán. Có thể dùng máy tính
cầm tay hoặc Python để kiểm lại kết quả, nhưng phần trình bày phải cho thấy
cách tính.

**Bài b1**

Lọc spam email: Một công ty triển khai bộ lọc spam và quan sát kết quả trên 10 000 email trong tháng:

- 9 000 email hợp lệ, 1 000 email spam thực sự
- Mô hình bắt được 850 spam (đúng), bỏ sót 150 spam
- Mô hình báo nhầm 200 email hợp lệ là spam.
- (a) Lập ma trận nhầm lẫn. Tính Accuracy, Precision, Recall, F1
- (b) Trong bối cảnh lọc spam, phép đo nào quan trọng nhất? Vì sao?
- (c) Đề xuất cách điều chỉnh ngưỡng để tăng phép đo quan trọng nhất. Chấp nhận đánh đổi gì?
- (d) Nếu các email công việc bị chặn nhầm gây thiệt hại 500 000 VND mỗi email và mỗi spam lọt qua tốn 10 000 VND, tính tổng thiệt hại của mô hình hiện tại

**Bài b2**

Chẩn đoán quá khớp: Sinh viên A huấn luyện 3 mô hình cây quyết định trên tập dữ liệu 500 mẫu, được kết quả:

- Mô hình 1: Accuracy train 75%, Accuracy test 73%, độ sâu 3
- Mô hình 2: Accuracy train 92%, Accuracy test 89%, độ sâu 7
- Mô hình 3: Accuracy train 100%, Accuracy test 70%, độ sâu 20.
- (a) Cho biết tình trạng của mỗi mô hình (vừa phải, quá khớp, thiếu khớp). Giải thích dựa vào số liệu
- (b) Đề xuất cách xử lý cho từng mô hình
- (c) Nếu phải chọn một mô hình để triển khai, nên chọn mô hình nào? Vì sao?
- (d) Vẽ phác learning curve dự đoán cho mỗi mô hình

**Bài b3**

Chọn ngưỡng cho mô hình sàng lọc: Một mô hình sàng lọc ung thư phổi trả về xác suất bệnh cho mỗi bệnh nhân. Tại các ngưỡng khác nhau:

- Ngưỡng 0,3: Sensitivity = 0,95, Specificity = 0,60
- Ngưỡng 0,5: Sensitivity = 0,85, Specificity = 0,80
- Ngưỡng 0,7: Sensitivity = 0,70, Specificity = 0,95 (a) Vẽ tay 3 điểm trên hệ trục ROC.
- (b) Trong bối cảnh sàng lọc (kiểm tra dân số rộng), nên chọn ngưỡng nào? Vì sao?
- (c) Trong bối cảnh chẩn đoán xác nhận (đã có triệu chứng), nên chọn ngưỡng nào?
- (d) Nếu chi phí xét nghiệm xác nhận cao và bệnh viện ngân sách hạn chế, chọn ngưỡng nào?

## C. Bài tập trên máy

Nộp cho mọi bài trong mục C: một tệp Jupyter Notebook chạy lại được từ đầu đến cuối, ghi rõ phiên bản Python và các thư viện đã dùng; các hình đã xuất thành tệp ảnh; và một ghi chú 300 đến 500 từ nêu kết quả chính kèm nhận xét. Mỗi bài trình bày thành một phần riêng, đánh số câu trả lời theo đúng các mục (a), (b), (c) của đề. Nêu rõ tập kiểm tra chỉ được dùng một lần sau khi đã khóa cấu hình và ngưỡng.

**Bài C.2**

Tối ưu siêu tham số với Grid Search và Random Search: Yêu cầu: dùng tập dữ liệu Breast Cancer Wisconsin của scikit-learn (load_breast_cancer), chia tập huấn luyện 70% và tập kiểm tra 30% với stratify = y và random_state = 42.

- (a) Tạo Pipeline gồm StandardScaler và một thuật toán phân lớp đã học (Cây quyết định, KNN hoặc hồi quy Logistic)
- (b) Định nghĩa lưới siêu tham số gồm 2 đến 3 siêu tham số, mỗi siêu tham số 4 đến 5 giá trị
- (c) Chạy Grid Search với 5-fold CV. Báo cáo tổ hợp tốt nhất và điểm tốt nhất. Đếm tổng số lần huấn luyện
- (d) Định nghĩa các phân phối tương ứng cho Random Search. Chạy Random Search với N = 50. So sánh với Grid Search về thời gian và chất lượng
Chỉ dùng tập huấn luyện vừa chia để tìm kiếm siêu tham số. Dành tập test cho mô hình đã khóa sau toàn bộ quá trình lựa chọn.

- (e) Vẽ heatmap kết quả Grid Search (nếu có đúng 2 siêu tham số). Heatmap giúp hiểu thêm điều gì so với chỉ biết tổ hợp tốt nhất?

**Bài C.3**

Triển khai mô hình thành REST API: Yêu cầu: triển khai mô hình tối ưu từ Bài C.2 ở trên.

- (a) Lưu pipeline tốt nhất ra tệp bằng joblib. Đặt tên tệp phù hợp với quy ước version
- (b) Viết tệp Flask app.py với endpoint /predict nhận dữ liệu JSON và trả về dự đoán cùng xác suất
- (c) Chạy máy chủ và thử gọi từ Python (bằng thư viện requests) với một mẫu dữ liệu
- (d) Viết test case kiểm tra: khi gửi dữ liệu hợp lệ và khi gửi dữ liệu thiếu/sai định dạng
- (e) Cải tiến: thêm endpoint /health trả về trạng thái server và phiên bản mô hình

**Bài C.4. Chính quy hóa L1, L2 và tìm siêu tham số bằng Optuna**

Mục tiêu: nhìn thấy khác biệt thật giữa chính quy hóa L1 và L2 qua số đặc trưng còn lại, rồi so một lần tìm kiếm tự động với lưới giá trị làm tay.

Tập dữ liệu: Breast Cancer Wisconsin (load_breast_cancer trong scikit-learn), 569 mẫu và 30 đặc trưng số. Lớp dương là ác tính: y = (target == 0).astype(int), đúng quy ước đã dùng ở Mục 6.4 của giáo trình.

Chuẩn bị: Optuna không đi kèm scikit-learn. Kiểm bằng lệnh python -c "import optuna"; nếu báo lỗi thì cài bằng python -m pip install optuna. Nếu môi trường không cho cài thêm thư viện, làm câu (e) bằng RandomizedSearchCV của Mục 6.3.1 của giáo trình với cùng không gian tìm kiếm và cùng số tổ hợp, và ghi rõ trong báo cáo là đã dùng phương án dự phòng.

Yêu cầu thực hiện:

- (a) Chia 70% huấn luyện và 30% kiểm tra với stratify = y, random_state = 42. Giữ riêng tập kiểm tra và chỉ dùng một lần ở câu (f). Mọi phép kiểm chứng chéo dùng StratifiedKFold(n_splits=5, shuffle=True, random_state=42).
- (b) Dựng Pipeline gồm StandardScaler và LogisticRegression. Theo quy ước ở Mục 6.4 của giáo trình, l1_ratio = 0.0 là L2 thuần và l1_ratio = 1.0 là L1 thuần, bản L1 cần solver = 'saga' với max_iter lớn.
- (c) Với C lần lượt 0,001; 0,01; 0,1; 1; 10; 100 và cả hai dạng chính quy hóa, lập bảng Accuracy kiểm chứng chéo trên tập huấn luyện kèm số hệ số khác 0 trên 30. Vẽ Accuracy theo C với trục hoành thang logarit cho cả hai dạng trên cùng một hình.
- (d) Đọc bảng: dạng nào không bao giờ triệt tiêu hệ số? Ở giá trị C nào thì L1 giữ dưới 15 đặc trưng mà Accuracy vẫn trên 0,95? Tại C = 0,001, L1 giữ lại bao nhiêu hệ số khác 0 và Accuracy bằng bao nhiêu — so con số đó với tỷ lệ lớp đa số của tập huấn luyện và cho biết đây là quá khớp hay thiếu khớp.
- (e) Dùng Optuna với TPESampler(seed=42) và 40 trial, chỉ số chấm điểm là F1, tìm đồng thời l1_ratio liên tục trong đoạn [0; 1] bằng suggest_float và C trong đoạn [0,001; 100] bằng suggest_float với log=True. Báo cáo tổ hợp tốt nhất và điểm tốt nhất.
- (f) So điểm tốt nhất của Optuna với F1 kiểm chứng chéo của ba cấu hình làm tay tại C = 1: L2, ElasticNet l1_ratio = 0.5 và L1. Nếu Optuna không thắng cấu hình làm tay thì kết luận gì về giá trị của tìm kiếm tự động trên bài toán này? Sau khi đã chốt, fit cấu hình được chọn trên toàn bộ tập huấn luyện và đánh giá một lần duy nhất trên tập kiểm tra.
→ Kết quả đối chiếu. Với scikit-learn 1.9.0, Optuna 4.9.0 và các tham số nêu trên: tập huấn luyện có 398 mẫu, tập kiểm tra 171 mẫu, tỷ lệ ác tính trong tập huấn luyện 0,3719. L2 giữ cả 30 hệ số ở mọi giá trị C, với Accuracy kiểm chứng chéo 0,8667; 0,9521; 0,9698; 0,9824; 0,9623; 0,9547. L1 cho Accuracy 0,6282; 0,6810; 0,9622; 0,9698; 0,9623; 0,9572 và số hệ số khác 0 là 0; 2; 7; 15; 26; 30. Tại C = 0,001 mọi hệ số của L1 bằng 0 nên mô hình luôn dự đoán lớp đa số và Accuracy 0,6282 chính là tỷ lệ lớp đa số 0,6281 — đó là thiếu khớp do phạt quá mạnh. F1 kiểm chứng chéo tại C = 1 là 0,9757 (L2), 0,9622 (ElasticNet l1_ratio = 0.5) và 0,9592 (L1). Optuna 40 trial cho l1_ratio ≈ 0,113 và C ≈ 0,718 với F1 0,9755, tức không vượt cấu hình L2 tại C = 1; RandomizedSearchCV 40 tổ hợp trên cùng không gian cũng cho 0,9755. Trên tập kiểm tra, cấu hình của Optuna giữ 28 trên 30 hệ số và đạt F1 0,9677, còn L2 tại C = 1 đạt 0,9600.

Nộp: một tệp Jupyter Notebook chạy lại được, kèm bảng Accuracy và số hệ số khác 0 theo C cho hai dạng chính quy hóa, hình Accuracy theo C, bảng so Optuna với ba cấu hình làm tay, và khoảng 300 từ trả lời các câu (d) và (f).
