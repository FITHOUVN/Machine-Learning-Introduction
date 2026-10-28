## Bài thực hành Chương 3 trên WEKA: khai phá luật kết hợp

Mục này trình bày trọn vẹn bài thực hành khai phá luật kết hợp trên WEKA Explorer, tương ứng với phần thực hành của Chương 3 của giáo trình. Thân chương thực hiện bài này bằng Python với thư viện mlxtend (Mục 3.4 của giáo trình); Mục này là bản làm bằng giao diện đồ họa, đọc được độc lập và không cần đọc trước Mục 3.4 của giáo trình.

Dữ liệu: tệp supermarket.arff có sẵn trong thư mục data của WEKA (bảng các tập dữ liệu có sẵn trong [01-su-dung-weka.md](01-su-dung-weka.md)), gồm 4 627 giao dịch của một chuỗi siêu thị New Zealand và 217 thuộc tính, trong đó 216 thuộc tính là sản phẩm và một thuộc tính total cho biết giỏ hàng thuộc nhóm giá trị thấp hay cao. Mỗi giao dịch được biểu diễn dưới dạng nhị phân: với mỗi sản phẩm, ô mang giá trị t nếu sản phẩm có trong giao dịch và để trống nếu không.

Mục tiêu: khai phá các luật kết hợp từ dữ liệu giỏ hàng, đọc được các chỉ số Support, Confidence, Lift và Conviction mà WEKA in ra, sau đó diễn giải kết quả để rút ra nhận định kinh doanh. Mục WEKA Explorer trong [01-su-dung-weka.md](01-su-dung-weka.md) đã mô tả các thành phần của tab Associate; Mục này chỉ bàn phần thao tác và phần đọc kết quả.

### Tham số của Apriori trong WEKA

Nhấn vào dòng chữ Apriori trong khung Associator để mở hộp thoại tham số. Năm tham số cần lưu ý:

- lowerBoundMinSupport: ngưỡng Support tối thiểu, mặc định 0,1; hạ ngưỡng này để tìm thêm luật
- upperBoundMinSupport: ngưỡng Support khởi đầu của quá trình tìm luật, mặc định 1,0
- minMetric: ngưỡng tối thiểu của chỉ số đã chọn ở metricType, mặc định 0,9
- numRules: số luật tối đa cần xuất, mặc định 10
- metricType: chỉ số đo độ mạnh của luật, mặc định Confidence; có thể chọn Lift, Leverage hoặc Conviction (đã trình bày ở Mục 3.3.1 của giáo trình)

**Cơ chế hạ ngưỡng của Apriori trong WEKA**

Apriori của WEKA không chạy với một ngưỡng Support cố định. Thuật toán bắt đầu từ upperBoundMinSupport, hạ ngưỡng dần theo bước delta và tìm lại, cho tới khi đủ numRules luật hoặc chạm lowerBoundMinSupport. Vì vậy ngưỡng in ra ở dòng Minimum support của phần kết quả thường không bằng lowerBoundMinSupport đã đặt, và dòng Number of cycles performed cho biết thuật toán đã hạ ngưỡng bao nhiêu lần. Đây là điểm khác biệt đáng chú ý so với mlxtend ở Mục 3.4 của giáo trình: trong mlxtend người dùng chốt ngưỡng một lần và thuật toán chạy đúng một lượt với ngưỡng đó.

### Các bước chạy Apriori trên tập dữ liệu Supermarket

- Bước 1. Khởi động WEKA GUI Chooser và chọn Explorer. Trong tab Preprocess, nhấn Open file và chọn tệp supermarket.arff. WEKA hiển thị 4 627 instances và 217 attributes.
- Bước 2. Nhấn lần lượt vào các thuộc tính trong khu Attributes để xem mức độ phổ biến của từng sản phẩm. Một số sản phẩm như bread and cake, vegetables, milk xuất hiện trong phần lớn giao dịch, nhiều sản phẩm khác rất hiếm; quan sát này giúp ước lượng một ngưỡng Support hợp lý trước khi chạy.
- Bước 3. Chuyển sang tab Associate. Apriori đã được chọn sẵn trong khung Associator; nhấn vào dòng chữ Apriori để mở hộp thoại tham số.
- Bước 4. Đặt lowerBoundMinSupport = 0,1, minMetric = 0,9 và numRules = 20, giữ metricType = Confidence, rồi nhấn OK.
- Bước 5. Nhấn Start. Sau vài giây, kết quả xuất hiện trong khung Associator output.
- Bước 6. Đọc kết quả: phần đầu liệt kê số tập mục phổ biến tìm được ở mỗi cỡ, phần sau là danh sách các luật mạnh kèm chỉ số. Nhấn chuột phải vào mục tương ứng trong khung Result list và chọn Save result buffer để lưu kết quả cho lần đối chiếu sau.

### Khối kết quả và cách đọc

Khối kết quả dưới đây là kết quả WEKA in ra với cấu hình mặc định (numRules = 10); khi đặt numRules = 20 như ở Bước 4, phần thống kê đầu ra có thể khác đôi chút.

```
Apriori
=======

Minimum support: 0.15 (694 instances)
Minimum metric <confidence>: 0.9
Number of cycles performed: 17

Generated sets of large itemsets:
Size of set of large itemsets L(1): 44
Size of set of large itemsets L(2): 380
Size of set of large itemsets L(3): 910
Size of set of large itemsets L(4): 633
Size of set of large itemsets L(5): 105
Size of set of large itemsets L(6): 1

Best rules found:
1. biscuits=t frozen foods=t fruit=t total=high 788
       ==> bread and cake=t 723
   <conf:(0.92)> lift:(1.27) lev:(0.03) conv:(3.35)

2. baking needs=t biscuits=t fruit=t total=high 760
       ==> bread and cake=t 696
   <conf:(0.92)> lift:(1.27) lev:(0.03) conv:(3.28)
```

Dòng Minimum support: 0,15 (694 instances) cho biết thuật toán đã hạ ngưỡng xuống 0,15 sau 17 lần tìm, tức 694 trong 4 627 giao dịch. Với luật thứ nhất, 788 giao dịch thỏa vế trái và 723 trong số đó chứa bread and cake, nên Confidence = 723/788 ≈ 0,9175, được WEKA làm tròn thành 0,92; Support của cả luật là 723/4 627 ≈ 0,1563. Lift = 1,27 cho biết tần suất của vế phải trong nhóm thỏa vế trái cao hơn khoảng 27% so với tần suất nền. Chỉ số này cho thấy liên hệ thuận trong dữ liệu, không tự chứng minh ý nghĩa thống kê hay quan hệ nhân quả.

Khi đối chiếu khối kết quả này với kết quả mlxtend ở Mục 3.4.2 của giáo trình, bốn chỉ số Support, Confidence, Lift và Leverage trùng khít tới từng chữ số; riêng Conviction thì không. WEKA in conv:(3,35) và conv:(3,28) cho hai luật trên, còn mlxtend cho 3,40 và 3,33, vì hai công cụ dùng quy ước tính Conviction khác nhau. Đây là chênh lệch về cách tính, không phải lỗi của một trong hai công cụ.

**Lưu ý vận hành**

Nếu nhiều luật có vế phải là mặt hàng phổ biến, đổi metricType sang Lift hoặc lọc kết quả theo Lift và theo số giao dịch hỗ trợ. Không dùng upperBoundMinSupport để loại mặt hàng phổ biến: tham số này là ngưỡng khởi đầu của quá trình hạ ngưỡng, không phải ngưỡng chặn trên của từng mặt hàng. Các luật chứa total=high mô tả liên hệ với giỏ hàng giá trị cao; cần kiểm tra tính khả dụng của thuộc tính này trước khi dùng để đề xuất khuyến mãi.

### Chạy lại bằng FPGrowth

Sau Apriori, nên lặp lại bài thực hành với FPGrowth: trong khung Associator nhấn Choose, chọn FPGrowth, đặt các tham số tương đương rồi nhấn Start. Tập mục phổ biến và các luật mạnh thường giống nhau giữa hai thuật toán; khác biệt nằm ở tốc độ. Trên Supermarket với khoảng 4 600 giao dịch, chênh lệch thời gian không nhiều, nhưng với hàng trăm nghìn giao dịch thì rõ rệt. Tên và giá trị mặc định của tham số FPGrowth khác Apriori, cần chỉnh đúng để so sánh công bằng.

### Dữ liệu định lượng với FilteredAssociator

Mục 3.2.3 của giáo trình đã chỉ ra rằng các thuộc tính số cần được phân khoảng trước khi đưa vào khai phá luật kết hợp. WEKA cung cấp bộ điều phối FilteredAssociator để tự động hóa việc này.

- Bước 1. Trong tab Associate, nhấn Choose và chọn FilteredAssociator.
- Bước 2. Nhấn vào dòng chữ FilteredAssociator để mở hộp thoại tham số.
- Bước 3. Chọn filter là Discretize (filters > unsupervised > attribute > Discretize); bộ lọc này phân khoảng các thuộc tính số thành các nhóm rời rạc.
- Bước 4. Chọn associator bên trong là Apriori. Nếu dùng FPGrowth, dữ liệu đầu vào phải được biểu diễn bằng các thuộc tính nhị phân và phải chọn đúng giá trị dương; Discretize với nhiều khoảng chưa tạo ra biểu diễn này.
- Bước 5. Đặt các tham số khác như trước và nhấn Start. FilteredAssociator áp dụng Discretize trước, sau đó chạy thuật toán khai phá luật trên dữ liệu đã rời rạc hóa. Kết quả là các luật định lượng, viết theo cú pháp của WEKA dưới dạng tuổi∈[20,30) AND thu nhập∈[20tr,40tr) → mua=Có.
Một lựa chọn thay thế là rời rạc hóa trước ngay trong tab Preprocess bằng bộ lọc Discretize hoặc NumericToNominal (mục Bộ lọc (Filters) trong [01-su-dung-weka.md](01-su-dung-weka.md)), rồi chạy Apriori trên dữ liệu đã chuyển. Mục 3.4.4 của giáo trình trình bày cách làm tương đương bằng Python với pandas.

### Lỗi thường gặp riêng của tab Associate

mục Lỗi thường gặp và cách khắc phục trong [01-su-dung-weka.md](01-su-dung-weka.md) đã nêu các lỗi chung của WEKA, trong đó Lỗi 2 chính là trường hợp Apriori không sinh được luật nào vì dữ liệu còn ở dạng số. Ba tình huống dưới đây là lỗi riêng của khai phá luật kết hợp.

- Đặt ngưỡng Support quá thấp khiến Apriori chạy rất lâu hoặc tràn bộ nhớ: tăng ngưỡng, dùng FPGrowth thay Apriori, hoặc thử trước trên một tập dữ liệu nhỏ hơn
- metricType = Confidence nhưng minMetric quá cao (ví dụ 0,95) khiến không luật nào đạt ngưỡng: hạ minMetric xuống dần
- Hầu hết luật tìm được có vế phải là mặt hàng phổ biến: đổi metricType sang Lift, điều chỉnh minMetric theo thước đo mới và kiểm tra số giao dịch hỗ trợ; không giảm upperBoundMinSupport với mục đích loại mặt hàng
Nộp: khối Associator output đã lưu bằng Save result buffer cho Apriori và cho FPGrowth, kèm một trang nhận xét về năm luật mạnh nhất và về chỉ số đã chọn ở metricType.

Bảng 1 tổng kết khi nào nên dùng WEKA và khi nào nên dùng Python với mlxtend cho khai phá luật kết hợp; Bảng B.3 của giáo trình ở Phụ lục B đối chiếu tên thuật toán tương ứng của hai công cụ.

*Bảng 1. So sánh WEKA và Python cho khai phá luật kết hợp*

| Tiêu chí | WEKA | Python (mlxtend) |
|---|---|---|
| Giao diện | Đồ họa, trực quan | Lập trình |
| Đường cong học tập | Thấp | Trung bình |
| Hỗ trợ Apriori | Có | Có |
| Hỗ trợ FP-Growth | Có | Có |
| Dữ liệu định lượng | FilteredAssociator kèm Discretize | pandas kèm cut hoặc qcut, rồi apriori |
| Tích hợp vào pipeline lớn | Khó | Dễ |
| Phù hợp với | Khám phá nhanh, dạy học | Sản phẩm, ứng dụng thực tế |
