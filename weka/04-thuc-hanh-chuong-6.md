## Bài thực hành Chương 6 trên WEKA: đánh giá mô hình và chống quá khớp

Mục này trình bày trọn vẹn bài thực hành đánh giá mô hình và chống quá khớp trên WEKA Explorer, tương ứng với các Phần 6.4.A của giáo trình đến 6.4.E của Chương 6 của giáo trình. Thân chương thực hiện bài này bằng Python với scikit-learn; Mục này là bản làm bằng giao diện đồ họa và đọc được độc lập.

Dữ liệu: tệp breast-cancer.arff trong thư mục data của WEKA (bảng các tập dữ liệu có sẵn trong [01-su-dung-weka.md](01-su-dung-weka.md)). Đây là bộ Ljubljana, gồm 286 mẫu và 9 thuộc tính danh mục dùng để dự đoán, cùng thuộc tính nhãn class với hai giá trị no-recurrence-events (201 mẫu) và recurrence-events (85 mẫu); lớp cần phát hiện chỉ chiếm 29,7% dữ liệu.

Mục tiêu: đánh giá đầy đủ một mô hình trên bài toán phân lớp nhị phân mất cân bằng, phát hiện quá khớp bằng cách so sánh kết quả trên tập huấn luyện với kết quả kiểm chứng chéo, giảm quá khớp bằng cắt tỉa cây, áp dụng chính quy hóa cho hồi quy logistic và tối ưu siêu tham số.

Lưu ý khi đối chiếu: không so sánh trực tiếp các con số trong mục này với các con số Python in ở Chương 6 của giáo trình. J48 là cài đặt của C4.5 và cắt tỉa sẵn, còn DecisionTreeClassifier là cài đặt của CART và không cắt tỉa sẵn; hai công cụ cũng chia mười phần theo hai cách khác nhau; và từ Phần 6.4.D của giáo trình trở đi Chương 6 của giáo trình chuyển sang bộ Wisconsin Diagnostic thay vì bộ Ljubljana. Khoảng chênh giữa tập huấn luyện và kiểm chứng chéo là ví dụ rõ nhất: J48 ở cấu hình mặc định chênh 0,35 điểm phần trăm vì đã cắt tỉa sẵn, còn DecisionTreeClassifier ở cấu hình mặc định chênh 33,07 điểm phần trăm vì không cắt tỉa. Hai con số khác nhau vì hai cấu hình khác nhau, không phải vì một bên chạy sai.

### Đánh giá đầy đủ một mô hình (đối chiếu Phần 6.4.A của giáo trình)

- Bước 1. Trong tab Preprocess, mở breast-cancer.arff và chọn class làm thuộc tính nhãn.
- Bước 2. Chuyển sang tab Classify, chọn Test options là Cross-validation với Folds = 10; mở More options và đặt seed = 1.
- Bước 3. Nhấn Choose và chọn trees > J48; giữ cấu hình mặc định.
- Bước 4. Nhấn Start và chờ kết quả trong Classifier output.
- Bước 5. Ghi Precision, Recall, F1 và ROC Area của từng lớp; đối chiếu với số đếm trong Confusion Matrix.
- Bước 6. Nhấn chuột phải vào mục kết quả trong Result list, chọn Visualize Threshold Curve và chọn lớp recurrence-events để xem đường cong ROC; lưu khối kết quả bằng Save result buffer.

**Kết quả J48 mặc định, kiểm chứng chéo 10 phần**

```
Correctly Classified Instances        216              75.5245 %
Incorrectly Classified Instances       70              24.4755 %
Kappa statistic                        0.2826
Mean absolute error                    0.3676
Root mean squared error                0.4324
Total Number of Instances             286

=== Detailed Accuracy By Class ===
Class                TP     FP     Prec   Recall F1     MCC    ROC    PRC
no-recurrence-events 0.960  0.729  0.757  0.960  0.846  0.339  0.584  0.736
recurrence-events    0.271  0.040  0.742  0.271  0.397  0.339  0.584  0.436
Weighted Avg.        0.755  0.524  0.752  0.755  0.713  0.339  0.584  0.647

=== Confusion Matrix ===
    a   b   <-- classified as
 193   8 |  a = no-recurrence-events
  62  23 |  b = recurrence-events
```

Accuracy = 216/286 ≈ 75,52%. Với lớp recurrence-events, Recall = 23/85 ≈ 0,271, nghĩa là mô hình bỏ sót 62 trong 85 ca tái phát; Precision = 23/31 ≈ 0,742 và F1 ≈ 0,397. Kappa 0,2826 và ROC Area 0,584 đều thấp. Đây là minh chứng cho luận điểm của Mục 6.1 của giáo trình: Accuracy 75,52% nghe có vẻ khá nhưng mô hình gần như thất bại ở lớp thiểu số, đúng là lớp mà bài toán cần phát hiện. Mục Đọc kết quả output trong [01-su-dung-weka.md](01-su-dung-weka.md) nêu cách đọc từng phần của khối kết quả này.

### Phát hiện quá khớp (đối chiếu Phần 6.4.B của giáo trình)

Mục tiêu của phần này là so sánh kết quả trên tập huấn luyện với kết quả kiểm chứng chéo để phát hiện quá khớp.

- Bước 1. Trong tab Classify, chọn Test options là Use training set.
- Bước 2. Chạy J48 ở cấu hình mặc định và ghi lại Accuracy.
- Bước 3. Đổi Test options sang Cross-validation với Folds = 10, chạy lại và ghi lại Accuracy.
- Bước 4. Nhấn vào dòng cấu hình J48, đặt unpruned = True và giữ các tham số khác, rồi chạy lại hai lượt như trên.
```
Evaluation on training set:   Accuracy  75.8741 %  (217/286)
10-fold cross-validation:     Accuracy  75.5245 %  (216/286)
```

```
J48 -U -M 2      Number of Leaves: 152      Size of the tree: 179

Evaluation on training set:   Accuracy  88.1119 %  (252/286)
10-fold cross-validation:     Accuracy  69.5804 %  (199/286)
```

Ở cấu hình mặc định, hai con số chỉ chênh 0,35 điểm phần trăm, vì J48 mặc định đã cắt tỉa với confidenceFactor = 0,25. Khi tắt cắt tỉa, cây có 152 lá trên 286 mẫu, tức trung bình chưa đầy hai mẫu một lá: Accuracy trên tập huấn luyện tăng lên 88,11% nhưng Accuracy kiểm chứng chéo tụt xuống 69,58%, chênh 18,53 điểm phần trăm, đúng dấu hiệu quá khớp mà Mục 6.2.1 của giáo trình mô tả. Accuracy cao trên tập huấn luyện vì vậy không phải căn cứ để chọn mô hình.

Bảng 1 tổng hợp bốn con số Accuracy thu được từ hai cấu hình J48 trên cùng bộ dữ liệu Ljubljana.

*Bảng 1. Hai cấu hình J48 trên bộ Ljubljana: Accuracy trên tập huấn luyện so với Accuracy kiểm chứng chéo*

| Cấu hình J48 | Accuracy trên tập huấn luyện | Accuracy kiểm chứng chéo 10 phần | Chênh lệch |
|---|---|---|---|
| Mặc định (confidenceFactor = 0,25) | 75,8741% | 75,5245% | 0,35 điểm |
| Không cắt tỉa (unpruned = True, 152 lá) | 88,1119% | 69,5804% | 18,53 điểm |

### Xử lý quá khớp bằng cắt tỉa cây (đối chiếu Phần 6.4.C của giáo trình)

- Bước 1. Choose > trees > J48.
- Bước 2. Nhấn vào dòng cấu hình J48, đặt confidenceFactor = 0,1 để tăng mức cắt tỉa (mặc định 0,25) và minNumObj = 10 để yêu cầu ít nhất 10 mẫu mỗi lá (mặc định 2).
- Bước 3. Chạy lại với Cross-validation 10 phần.

**Kết quả J48 cắt tỉa mạnh, kiểm chứng chéo 10 phần**

```
Correctly Classified Instances        216              75.5245 %
Incorrectly Classified Instances       70              24.4755 %
Kappa statistic                        0.2766
Mean absolute error                    0.3709
Root mean squared error                0.4313
Total Number of Instances             286

=== Detailed Accuracy By Class ===
Class                TP     FP     Prec   Recall F1     MCC    ROC    PRC
no-recurrence-events 0.965  0.741  0.755  0.965  0.847  0.339  0.610  0.753
recurrence-events    0.259  0.035  0.759  0.259  0.386  0.339  0.610  0.443
Weighted Avg.        0.755  0.531  0.756  0.755  0.710  0.339  0.610  0.661

=== Confusion Matrix ===
    a   b   <-- classified as
 194   7 |  a = no-recurrence-events
  63  22 |  b = recurrence-events
```

So với cây không cắt tỉa, Accuracy kiểm chứng chéo tăng từ 69,58% lên 75,52%, tức 5,94 điểm phần trăm. Nhưng so với cắt tỉa mặc định thì tăng mức cắt tỉa không cải thiện gì: Accuracy kiểm chứng chéo vẫn là 75,52%, Recall của lớp recurrence-events giảm từ 0,271 xuống 0,259 và Kappa giảm từ 0,2826 xuống 0,2766, tương ứng bỏ sót thêm một ca tái phát. ROC Area tăng từ 0,584 lên 0,610, cho thấy khả năng xếp hạng xác suất cải thiện nhẹ dù kết quả tại ngưỡng quyết định mặc định không khá hơn.

Tăng mức cắt tỉa vì vậy không luôn cải thiện mô hình. Với dữ liệu này, confidenceFactor = 0,25 mặc định của J48 đã phù hợp; cắt tỉa thêm có thể làm mô hình quá đơn giản mà không tăng khả năng khái quát hóa. Mức cắt tỉa nên được chọn bằng tìm kiếm tham số có hệ thống, trình bày ở phần cuối mục này. Muốn biết khoảng chênh huấn luyện – kiểm chứng chéo của riêng cấu hình cắt tỉa mạnh thì phải chạy lại Use training set với chính cấu hình đó; không lấy mức chênh 0,35 điểm của cấu hình mặc định để thay thế.

### Chính quy hóa cho hồi quy logistic (đối chiếu Phần 6.4.D của giáo trình)

WEKA có sẵn hồi quy logistic kèm chính quy hóa L2.

- Bước 1. Choose > functions > Logistic.
- Bước 2. Nhấn vào dòng cấu hình và đặt ridge = 1,0 (mặc định 1,0E-8).
- Bước 3. Chạy với Cross-validation 10 phần, lần lượt với ridge = 0,001, 0,01, 0,1, 1 và 10, ghi lại Accuracy của từng giá trị.
Khi đối chiếu với Mục 6.2.2 của giáo trình cần chú ý hai quy ước ngược chiều nhau: tham số ridge của WEKA cùng chiều với hệ số chính quy hóa, tăng ridge là tăng mức chính quy hóa; còn tham số C của LogisticRegression trong scikit-learn là nghịch đảo của hệ số đó, tăng C là giảm mức chính quy hóa. Logistic của WEKA chỉ cung cấp chính quy hóa L2; muốn thử L1 hoặc ElasticNet thì phải dùng Python như ở Phần 6.4.D của giáo trình.

### Tối ưu siêu tham số (đối chiếu Phần 6.4.E của giáo trình)

WEKA có bộ điều phối CVParameterSelection để dò siêu tham số bằng kiểm chứng chéo.

- Bước 1. Choose > meta > CVParameterSelection.
- Bước 2. Nhấn vào dòng cấu hình, đặt classifier là J48 và CVParameters là 'C 0,1 0,4 4', tức thử confidenceFactor từ 0,1 đến 0,4 theo 4 bước; đặt numFolds = 10.
- Bước 3. Nhấn Start và đọc giá trị tối ưu mà WEKA chọn ở phần đầu của Classifier output.
CVParameterSelection tương ứng với GridSearchCV của scikit-learn (Bảng B.3 của giáo trình). Điểm tốt nhất mà quá trình dò tìm báo về là điểm kiểm chứng chéo dùng để chọn mô hình, chưa phải ước lượng độc lập; sau khi khóa lựa chọn thì phải đánh giá một lần nữa trên tập kiểm tra chưa dùng tới.

Nộp: ba khối Classifier output đã lưu, gồm J48 mặc định, J48 không cắt tỉa và J48 cắt tỉa mạnh; một bảng bốn con số Accuracy theo mẫu Bảng 1 do chính người học chạy; và một trang nhận xét vì sao Accuracy trên tập huấn luyện không dùng được để chọn mô hình.
