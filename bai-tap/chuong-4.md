# Chương 4 — Phân lớp dữ liệu

> Tệp này thuộc **Sách bài tập** của học phần. Nội dung dưới đây được chuyển
> nguyên văn từ phần luyện tập cuối Chương 4 của giáo trình, khi phần đó được
> rút gọn để sách in còn đúng ba phần: câu hỏi ôn tập lý thuyết, một bài thực
> hành, và một chặng của dự án. Mọi câu dẫn "Mục x.y" đều trỏ về giáo trình.

## B. Bài tập tính tay

Làm bằng giấy và bút. Trình bày từng bước tính toán. Có thể dùng máy tính
cầm tay hoặc Python để kiểm lại kết quả, nhưng phần trình bày phải cho thấy
cách tính.

**Bài B.1. Tính entropy và information gain**

Cho một tập dữ liệu 14 ngày với đặc trưng “thời tiết” (Nắng/Mưa/Râm) và nhãn “chơi tennis” (Có/Không). Phân bố như sau: 9 ngày Có, 5 ngày Không

- Trong các ngày Nắng (5 ngày): 2 Có, 3 Không
- Trong các ngày Mưa (5 ngày): 3 Có, 2 Không
- Trong các ngày Râm (4 ngày): 4 Có, 0 Không - cả bốn ngày đều Có
- (a) Tính entropy của tập gốc
- (b) Tính entropy của mỗi nhóm con sau khi chia theo thời tiết
- (c) Tính information gain của đặc trưng “thời tiết”
- (d) Nếu có thêm đặc trưng “gió” (mạnh/yếu) với gain = 0,048, đặc trưng nào sẽ được chọn để chia trước? Vì sao?
Bảng B.1 dưới đây là dữ liệu đầy đủ của 14 ngày. Bài B.1 chỉ cần cột “thời tiết” và cột nhãn; Bài B.2 cần cả bốn đặc trưng để chạy tiếp các bước đệ quy của ID3.

*Bảng B.1. Dữ liệu 14 ngày dùng cho Bài B.1 và Bài B.2 (trong giáo trình cũ là Bảng 4.14)*

| Ngày | Thời tiết | Nhiệt độ | Độ ẩm | Gió | Chơi tennis |
|---|---|---|---|---|---|
| N1 | Nắng | Nóng | Cao | Yếu | Không |
| N2 | Nắng | Nóng | Cao | Mạnh | Không |
| N3 | Râm | Nóng | Cao | Yếu | Có |
| N4 | Mưa | Dịu | Cao | Yếu | Có |
| N5 | Mưa | Mát | Vừa | Yếu | Có |
| N6 | Mưa | Mát | Vừa | Mạnh | Không |
| N7 | Râm | Mát | Vừa | Mạnh | Có |
| N8 | Nắng | Dịu | Cao | Yếu | Không |
| N9 | Nắng | Mát | Vừa | Yếu | Có |
| N10 | Mưa | Dịu | Vừa | Yếu | Có |
| N11 | Nắng | Dịu | Vừa | Mạnh | Có |
| N12 | Râm | Dịu | Cao | Mạnh | Có |
| N13 | Râm | Nóng | Vừa | Yếu | Có |
| N14 | Mưa | Dịu | Cao | Mạnh | Không |

Một chi tiết đáng chú ý khi làm Bài B.2: cả bốn ngày Râm đều “Có”. Nhánh đó là nút thuần nên thuật toán dừng ngay, không chia tiếp - đúng điều kiện dừng ở Bước 7 của thuật toán ID3 (Mục 4.2.3 của giáo trình). Hai nhánh Nắng và Mưa thì còn lẫn cả hai nhãn nên phải lặp lại quy trình trên từng nhánh với ba đặc trưng còn lại.

**Bài B.2. Áp dụng ID3 xây cây quyết định**

Tiếp tục tập dữ liệu 14 ngày ở Bài B.1. Giả sử 4 đặc trưng có sẵn là “thời tiết”, “gió”, “nhiệt độ”, “độ ẩm”, mỗi đặc trưng nhận giá trị rời rạc.

- (a) Áp dụng đầy đủ 7 bước của ID3 để xây cây quyết định. Trình bày từng bước với nội dung: đầu vào, hành động, đầu ra, ý nghĩa
- (b) Vẽ cây hoàn chỉnh sau khi thuật toán dừng
- (c) Diễn giải các luật khai phá được từ cây (mỗi đường đi từ gốc đến lá là một luật)
- (d) Đánh giá tính diễn giải của cây: có bao nhiêu cấp? Một bác sĩ thể thao có dễ giải thích cây này cho bệnh nhân không?

**Bài B.3. Naive Bayes với Laplace smoothing**

Cho tập dữ liệu 8 sinh viên với 2 đặc trưng (đi học đầy đủ: Có/Không, làm bài tập: Có/Không) và nhãn (đạt môn: Có/Không):

SV1: đi học=Có, bài tập=Có → đạt=Có

SV2: đi học=Có, bài tập=Có → đạt=Có

SV3: đi học=Có, bài tập=Không → đạt=Có

SV4: đi học=Không, bài tập=Có → đạt=Có

SV5: đi học=Có, bài tập=Không → đạt=Không

SV6: đi học=Không, bài tập=Không → đạt=Không

SV7: đi học=Không, bài tập=Không → đạt=Không

SV8: đi học=Không, bài tập=Không → đạt=Không (a) Tính P(đạt = Có) và P(đạt = Không).

- (b) Tính P(đi học=Có | đạt=Có), P(đi học=Có | đạt=Không), tương tự cho bài tập
- (c) Phân lớp sinh viên mới có đi học=Có, bài tập=Không. Trình bày Bước 3 đầy đủ và cho biết lớp dự đoán
- (d) Có xác suất nào bằng 0 trong tập dữ liệu này không? Áp dụng Laplace smoothing (k=2) và tính lại Bước 3

**Bài B.4. Áp dụng KNN tính thủ công**

Cho tập dữ liệu 6 khách hàng của một ngân hàng với hai đặc trưng (tuổi tính bằng năm, dư nợ thẻ tín dụng tính bằng nghìn đồng) và nhãn rủi ro tín dụng (Cao hoặc Thấp):

KH1: tuổi=58, dư nợ=29 500 → rủi ro=Thấp

KH2: tuổi=50, dư nợ=31 000 → rủi ro=Thấp

KH3: tuổi=20, dư nợ=32 500 → rủi ro=Thấp

KH4: tuổi=29, dư nợ=45 000 → rủi ro=Cao

KH5: tuổi=31, dư nợ=50 000 → rủi ro=Cao

KH6: tuổi=36, dư nợ=150 000 → rủi ro=Cao

(a) Cho khách hàng mới X có tuổi 30 và dư nợ 30 000. Tính khoảng cách Euclidean từ X đến từng khách hàng đã có, trên dữ liệu chưa chuẩn hóa. Với mỗi khách hàng, cho biết đặc trưng tuổi góp bao nhiêu phần trăm vào bình phương khoảng cách.

(b) Với k = 3, phân lớp X. Ba láng giềng gần nhất là những khách hàng nào? Việc không chuẩn hóa dữ liệu gây ra vấn đề gì?

(c) Chuẩn hóa Min-Max về [0, 1] cho cả hai đặc trưng, lấy giá trị nhỏ nhất và lớn nhất trên sáu khách hàng đã có rồi áp dụng cùng phép biến đổi đó cho X. Tính lại sáu khoảng cách và phân lớp X với k = 3.

- (d) So sánh kết quả ở (b) và (c): ba láng giềng gần nhất có đổi không, nhãn dự đoán có đổi không? Đặc trưng nào lấn át khoảng cách trước khi chuẩn hóa, và vì sao chỉ cần xem biên độ của hai cột là đã dự đoán được điều đó?
- Gợi ý: biên độ của tuổi là 38 năm còn biên độ của dư nợ là 120 500 nghìn đồng, chênh nhau khoảng 3 171 lần. Ba láng giềng gần nhất và nhãn dự đoán của X trước khi chuẩn hóa đều khác với sau khi chuẩn hóa; nếu hai lần tính cho cùng một kết quả thì phép tính đã sai ở đâu đó. Có thể đối chiếu bằng KNeighborsClassifier và MinMaxScaler của scikit-learn.

**Bài B.5. Random Forest biểu quyết**

Một Random Forest có 5 cây quyết định, đang phân lớp một mẫu mới. Kết quả dự đoán từng cây:

- Cây 1: Lớp A (xác suất 0,8)
- Cây 2: Lớp B (xác suất 0,6)
- Cây 3: Lớp A (xác suất 0,7)
- Cây 4: Lớp A (xác suất 0,55)
- Cây 5: Lớp B (xác suất 0,9)
- Quy ước: xác suất ghi kèm mỗi cây là xác suất của chính lớp mà cây đó dự đoán; vì bài toán chỉ có hai lớp, xác suất của lớp còn lại bằng 1 trừ giá trị đó. Ví dụ Cây 2 dự đoán Lớp B với xác suất 0,6 nghĩa là P(Lớp A) = 0,4.
- (a) Theo biểu quyết đa số đơn thuần, mẫu được phân vào lớp nào?
- (b) Theo biểu quyết trung bình xác suất (lấy trung bình các xác suất Lớp A và Lớp B), mẫu được phân vào lớp nào?
- (c) Hai cách biểu quyết có cho cùng kết quả không trong ví dụ này? Phân tích sự khác biệt
- (d) Nếu Random Forest có 100 cây thay vì 5 cây, dự đoán có ổn định hơn không? Vì sao?

## C. Bài tập trên máy

Nộp cho mọi bài trong mục C: một tệp Jupyter Notebook chạy lại được từ đầu đến cuối, ghi rõ phiên bản Python và các thư viện đã dùng; các hình đã xuất thành tệp ảnh; và một ghi chú 300 đến 500 từ nêu kết quả chính kèm nhận xét. Mỗi bài trình bày thành một phần riêng, đánh số câu trả lời theo đúng các mục (a), (b), (c) của đề. Kèm bảng chỉ số của từng thuật toán và ma trận nhầm lẫn, dùng cùng một cách chia dữ liệu cho mọi thuật toán.

**Bài C.2. Random Forest và tầm quan trọng đặc trưng**

Mục tiêu: dùng Random Forest để hiểu đặc trưng nào quan trọng nhất trong một bài toán

Tập dữ liệu: Breast Cancer Wisconsin (load_breast_cancer trong scikit-learn) với 30 đặc trưng và 2 lớp (lành tính/ác tính)

Yêu cầu thực hiện:

1. Tải tập dữ liệu và chia 70-30

- 2. Huấn luyện RandomForestClassifier(n_estimators=100, random_state=42)
- 3. In Accuracy trên tập kiểm tra
- 4. In top 5 đặc trưng quan trọng nhất theo feature_importances_
- 5. Diễn giải kết quả: các đặc trưng top 5 có liên quan đến đặc tính sinh học của ung thư vú không?
- 6. Thử các giá trị max_features khác nhau (1, 5, 'sqrt', 30) và so sánh Accuracy. Lý giải kết quả

**Bài C.3. Ảnh hưởng của k trong KNN**

Mục tiêu: quan sát ảnh hưởng của siêu tham số k trong KNN

Tập dữ liệu: Wine (load_wine trong scikit-learn) với 13 đặc trưng và 3 lớp

Yêu cầu thực hiện:

1. Tải dữ liệu và chia 70% train, 30% test với stratify=y, random_state=42. Giữ riêng test; đặt StandardScaler và KNN trong Pipeline để bộ chuẩn hóa chỉ học từ train của từng fold.

- 2. Trên tập train, dùng StratifiedKFold 5 folds (shuffle=True, random_state=42) để thử k = 1, 3, 5, 7, 9, 15, 25, 50. Ghi Accuracy trung bình và độ lệch chuẩn trên các fold validation.
- 3. Vẽ Accuracy cross-validation theo k, kèm độ lệch chuẩn.
- 4. Chọn k theo kết quả cross-validation, fit lại Pipeline trên toàn bộ train và đánh giá một lần trên test. Không chọn k bằng Accuracy của test.
- 5. Phân tích: k nhỏ quá cho hiệu năng thế nào? k lớn quá thì sao? Có gì liên hệ với trường hợp đúng/sai khi chọn k đã trình bày ở Mục 4.2.1 của giáo trình?
