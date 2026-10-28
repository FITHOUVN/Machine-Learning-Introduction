## Bài thực hành Chương 4 trên WEKA: phân lớp trên tập dữ liệu Iris

Mục này trình bày trọn vẹn bài thực hành phân lớp trên WEKA Explorer, tương ứng với phần thực hành của Chương 4 của giáo trình. Thân chương chạy sáu thuật toán này bằng Python với scikit-learn (Mục 4.4 của giáo trình); Mục này là bản làm bằng giao diện đồ họa và đọc được độc lập.

Dữ liệu: tệp iris.arff trong thư mục data của WEKA (bảng các tập dữ liệu có sẵn trong [01-su-dung-weka.md](01-su-dung-weka.md)), gồm 150 mẫu và 5 thuộc tính, trong đó 4 thuộc tính là đặc trưng và thuộc tính class là nhãn với ba loài. Tệp này theo bản gốc của UCI, còn hai giá trị sai ở mẫu 35 và mẫu 38 so với bản load_iris của scikit-learn đã sửa theo số liệu của Fisher; đối chiếu cho thấy hai mẫu này không làm đổi kết quả của các thuật toán trong mục này.

Mục tiêu: chạy sáu thuật toán phân lớp trên cùng một tập dữ liệu với cùng một cách đánh giá, đọc Classifier output của từng thuật toán và so sánh kết quả.

### Nạp dữ liệu và thiết lập đánh giá chung

- Bước 1. Khởi động WEKA GUI Chooser và chọn Explorer.
- Bước 2. Trong tab Preprocess, nhấn Open file và mở iris.arff trong thư mục data của WEKA (ảnh tab Preprocess trong [01-su-dung-weka.md](01-su-dung-weka.md)).
- Bước 3. Kiểm tra 150 mẫu và 5 thuộc tính; chọn class làm thuộc tính nhãn.
- Bước 4. Chuyển sang tab Classify (ảnh tab Classify trong [01-su-dung-weka.md](01-su-dung-weka.md)).
- Bước 5. Trong Test options, chọn Cross-validation và đặt Folds = 10. Mở More options và đặt seed = 1.
Giữ nguyên thiết lập đánh giá này cho cả sáu thuật toán; chỉ như vậy các kết quả mới so sánh được với nhau. Mỗi lần nhấn Start tạo một mục mới trong khung Result list; nhấn chuột phải vào mục đó để lưu kết quả bằng Save result buffer hoặc chọn Visualize Threshold Curve để xem đường cong ROC. Mục Tự động hóa qua Command Line trong [01-su-dung-weka.md](01-su-dung-weka.md) hướng dẫn cách chạy cùng bài này từ dòng lệnh, không qua giao diện.

### KNN với IBk, k = 5

- Bước 1. Trong tab Classify, nhấn Choose.
- Bước 2. Chọn weka > classifiers > lazy > IBk.
- Bước 3. Nhấn vào dòng cấu hình IBk để mở hộp thoại tham số.
- Bước 4. Đặt KNN = 5 và distanceWeighting = No distance weighting.
- Bước 5. Nhấn OK rồi Start, sau đó đọc Classifier output.
```
Correctly Classified Instances        143              95.3333 %
Incorrectly Classified Instances        7               4.6667 %
Kappa statistic                        0.93
Mean absolute error                    0.041
Root mean squared error                0.1444
Total Number of Instances             150

=== Detailed Accuracy By Class ===
Class           TP     FP     Prec   Recall F1     MCC    ROC    PRC
Iris-setosa     1.000  0.000  1.000  1.000  1.000  1.000  1.000  1.000
Iris-versicolor 0.940  0.040  0.922  0.940  0.931  0.896  0.993  0.983
Iris-virginica  0.920  0.030  0.939  0.920  0.929  0.895  0.993  0.983
Weighted Avg.   0.953  0.023  0.953  0.953  0.953  0.930  0.995  0.989

=== Confusion Matrix ===
    a   b   c   <-- classified as
  50   0   0 |  a = Iris-setosa
   0  47   3 |  b = Iris-versicolor
   0   4  46 |  c = Iris-virginica
```

Accuracy = 95,33%. Iris-setosa được phân lớp hoàn hảo (50 trên 50). Hai lớp Iris-versicolor và Iris-virginica nhầm lẫn qua lại 7 mẫu (3 cộng 4), đúng ở phần chồng lấn giữa hai loài này.

### Naive Bayes

- Bước 1. Choose > bayes > NaiveBayes.
- Bước 2. Giữ cấu hình mặc định (useKernelEstimator = False, useSupervisedDiscretization = False).
- Bước 3. Nhấn Start.
```
Correctly Classified Instances        144              96.0000 %
Incorrectly Classified Instances        6               4.0000 %
Kappa statistic                        0.94
Mean absolute error                    0.0342
Root mean squared error                0.155
Total Number of Instances             150

=== Detailed Accuracy By Class ===
Class           TP     FP     Prec   Recall F1     MCC    ROC    PRC
Iris-setosa     1.000  0.000  1.000  1.000  1.000  1.000  1.000  1.000
Iris-versicolor 0.960  0.040  0.923  0.960  0.941  0.911  0.992  0.983
Iris-virginica  0.920  0.020  0.958  0.920  0.939  0.910  0.992  0.986
Weighted Avg.   0.960  0.020  0.960  0.960  0.960  0.940  0.994  0.989

=== Confusion Matrix ===
    a   b   c   <-- classified as
  50   0   0 |  a = Iris-setosa
   0  48   2 |  b = Iris-versicolor
   0   4  46 |  c = Iris-virginica
```

Accuracy = 96,00%. Kết quả rất tốt dù giả định độc lập giữa các đặc trưng không thỏa: bốn đặc trưng petal và sepal có tương quan với nhau.

### Cây quyết định J48

- Bước 1. Choose > trees > J48, là cài đặt của thuật toán C4.5.
- Bước 2. Giữ cấu hình mặc định (confidenceFactor = 0,25, minNumObj = 2) rồi nhấn Start.
- Bước 3. Nhấn chuột phải vào mục kết quả trong Result list và chọn Visualize tree để xem cây đầy đủ.
- Bước 4. Chạy lại với minNumObj = 6 để quan sát mức giảm độ phức tạp của cây.
Khối Classifier output của lần chạy mặc định chính là khối đã dùng làm ví dụ ở mục Đọc kết quả output trong [01-su-dung-weka.md](01-su-dung-weka.md) nên không in lại ở đây; Accuracy = 96,00%, bằng NaiveBayes.

Cây chỉ dùng hai đặc trưng là petalwidth và petallength, trong đó riêng petalwidth đã tách trọn vẹn Iris-setosa ngay ở nhánh đầu tiên. Hai lá cuối cùng chỉ giữ ba mẫu mỗi lá: đó là phần cây cố gắng phân tách hai loài chồng lấn, và cũng là chỗ cây dễ quá khớp nhất. Với minNumObj = 6, WEKA cắt bỏ nhánh này, cây chỉ còn ba lá mà Accuracy gần như không đổi.

### Mạng nơ-ron với MultilayerPerceptron

- Bước 1. Choose > functions > MultilayerPerceptron.
- Bước 2. Nhấn vào dòng cấu hình và đặt hiddenLayers = a (giá trị mặc định, bằng tổng số đặc trưng và số lớp chia 2), learningRate = 0,3, trainingTime = 500.
- Bước 3. Nhấn Start và chờ; mạng nơ-ron chạy lâu hơn các thuật toán khác.
```
Correctly Classified Instances        146              97.3333 %
Incorrectly Classified Instances        4               2.6667 %
Kappa statistic                        0.96
Mean absolute error                    0.0327
Root mean squared error                0.1291
Total Number of Instances             150

=== Detailed Accuracy By Class ===
Class           TP     FP     Prec   Recall F1     MCC    ROC    PRC
Iris-setosa     1.000  0.000  1.000  1.000  1.000  1.000  1.000  1.000
Iris-versicolor 0.960  0.020  0.960  0.960  0.960  0.940  0.996  0.993
Iris-virginica  0.960  0.020  0.960  0.960  0.960  0.940  0.996  0.993
Weighted Avg.   0.973  0.013  0.973  0.973  0.973  0.960  0.998  0.995

=== Confusion Matrix ===
    a   b   c   <-- classified as
  50   0   0 |  a = Iris-setosa
   0  48   2 |  b = Iris-versicolor
   0   2  48 |  c = Iris-virginica
```

Accuracy = 97,33%, cao nhất trong sáu thuật toán. MultilayerPerceptron của WEKA dùng nơ-ron sigmoid và huấn luyện bằng lan truyền ngược với tốc độ học 0,3 cùng momentum 0,2, trong khi MLPClassifier ở Mục 4.2.4 của giáo trình dùng ReLU ở tầng ẩn và thuật toán tối ưu Adam. Hai công cụ vì vậy không buộc phải cho cùng một con số.

### Các phương pháp kết hợp

**Random Forest**

- Bước 1. Choose > trees > RandomForest.
- Bước 2. Giữ numIterations = 100, tức rừng gồm 100 cây.
- Bước 3. Nhấn Start.
```
Correctly Classified Instances        143              95.3333 %
Incorrectly Classified Instances        7               4.6667 %
Kappa statistic                        0.93
Mean absolute error                    0.0408
Root mean squared error                0.1621
Total Number of Instances             150

=== Detailed Accuracy By Class ===
Class           TP     FP     Prec   Recall F1     MCC    ROC    PRC
Iris-setosa     1.000  0.000  1.000  1.000  1.000  1.000  1.000  1.000
Iris-versicolor 0.940  0.040  0.922  0.940  0.931  0.896  0.991  0.984
Iris-virginica  0.920  0.030  0.939  0.920  0.929  0.895  0.991  0.982
Weighted Avg.   0.953  0.023  0.953  0.953  0.953  0.930  0.994  0.989

=== Confusion Matrix ===
    a   b   c   <-- classified as
  50   0   0 |  a = Iris-setosa
   0  47   3 |  b = Iris-versicolor
   0   4  46 |  c = Iris-virginica
```

Accuracy = 95,33%. Trên một tập dữ liệu nhỏ và dễ như Iris, việc gộp 100 cây không mang lại lợi thế so với một cây J48 duy nhất (96,00%); sức mạnh của Random Forest chỉ bộc lộ trên dữ liệu nhiều nhiễu và nhiều đặc trưng hơn.

**AdaBoost**

- Bước 1. Choose > meta > AdaBoostM1.
- Bước 2. Nhấn vào dòng cấu hình và chọn classifier là trees > DecisionStump.
- Bước 3. Giữ numIterations = 50 rồi nhấn Start.
```
Correctly Classified Instances        143              95.3333 %
Incorrectly Classified Instances        7               4.6667 %
```

Accuracy = 95,33%, bằng Random Forest. DecisionStump chỉ là cây một tầng nên mỗi mô hình thành phần rất yếu; AdaBoost bù lại bằng cách gộp nhiều mô hình yếu.

**Stacking**

- Bước 1. Choose > meta > Stacking.
- Bước 2. Nhấn vào dòng cấu hình, thêm J48, IBk và NaiveBayes vào classifiers làm các bộ học cơ sở.
- Bước 3. Đặt metaClassifier là Logistic hoặc giữ mặc định, rồi nhấn Start.

### Tổng hợp kết quả

Bảng 1 tổng hợp Accuracy của sáu thuật toán trên cùng tập dữ liệu Iris với cùng thiết lập kiểm chứng chéo 10 phần và seed = 1.

*Bảng 1. Accuracy của sáu thuật toán trên tập dữ liệu Iris trong WEKA, kiểm chứng chéo 10 phần*

| Thuật toán | Accuracy | Số mẫu phân lớp sai |
|---|---|---|
| IBk (k = 5) | 95,33% | 7 |
| NaiveBayes | 96,00% | 6 |
| J48 | 96,00% | 6 |
| MultilayerPerceptron | 97,33% | 4 |
| RandomForest (100 cây) | 95,33% | 7 |
| AdaBoostM1 (DecisionStump, 50 vòng) | 95,33% | 7 |

Khoảng cách giữa các thuật toán rất nhỏ, chỉ từ 4 đến 7 mẫu sai trên 150: Iris là tập dữ liệu dễ nên nó không phân biệt được các thuật toán. Mục 4.4 của giáo trình bàn đầy đủ các nguyên nhân khiến cùng một tên thuật toán cho con số khác nhau giữa WEKA và scikit-learn.

### Mở rộng với các tập dữ liệu khác của WEKA

Thư mục data của WEKA còn hai tập dữ liệu phân lớp nhị phân thích hợp để lặp lại bài thực hành này: breast-cancer.arff và diabetes.arff (bảng các tập dữ liệu có sẵn trong [01-su-dung-weka.md](01-su-dung-weka.md)). Lưu ý breast-cancer.arff của WEKA là bộ Ljubljana với 286 mẫu và 9 thuộc tính danh mục, dự đoán tái phát; còn hàm load_breast_cancer của scikit-learn cung cấp bộ Wisconsin Diagnostic với 569 mẫu và 30 đặc trưng số, phân biệt u lành và u ác. Hai bộ cùng chủ đề nhưng khác nguồn, khác đặc trưng và khác nhãn dự đoán, nên không so sánh trực tiếp Accuracy giữa chúng. [04-thuc-hanh-chuong-6.md](04-thuc-hanh-chuong-6.md) dùng chính bộ Ljubljana cho bài thực hành đánh giá mô hình.

Nộp: sáu khối Classifier output đã lưu bằng Save result buffer, một bảng tổng hợp Accuracy theo mẫu Bảng 1 do chính người học chạy, ảnh chụp màn hình Classifier output của thuật toán cho kết quả tốt nhất, và một trang nhận xét về nhầm lẫn giữa Iris-versicolor và Iris-virginica.
