- [ ] $\implies$

```latex

% ============================================================
\section{Phần 1: Kĩ thuật Boosting}
Một cây quyết định đơn lẻ thường không đủ mạnh để xử lý dữ liệu thực tế: nếu quá nông (Decision Stump) thì chỉ dựa trên một đặc trưng duy nhất, dẫn đến việc bỏ sót thông tin quan trọng; nếu quá sâu thì cây dễ ghi nhớ dữ liệu huấn luyện và mất khả năng khái quát. Chính vì hạn chế này mà các phương pháp \textbf{Ensemble Learning} ra đời, nhằm kết hợp nhiều mô hình con để tận dụng ưu điểm và hạn chế nhược điểm của từng mô hình đơn lẻ.  

\subsection{Điểm yếu của Decision Tree}
Một cây quyết định quá nông (như Decision Stump) chỉ chia dữ liệu dựa trên một đặc trưng duy nhất, ví dụ: “nếu cân nặng $ 70$kg thì dự đoán bệnh tim = Có”. Rõ ràng, dữ liệu thực tế phụ thuộc vào nhiều yếu tố (tuổi, huyết áp, động mạch bị tắc…), do đó cây nông dễ bị \textbf{underfitting}.  
Ngược lại, một cây quyết định quá sâu có thể tạo ra hàng chục hoặc hàng trăm nhánh, phù hợp hoàn hảo với dữ liệu huấn luyện nhưng lại thất bại khi gặp dữ liệu mới (\textbf{overfitting

\textit{Ảnh gợi ý:} Một stump chia dữ liệu thành hai nhóm lớn, vẫn sai nhiều điểm; một cây sâu phân chia cực chi tiết nhưng dự đoán kém trên test.

\subsection{Ensemble Learning là gì}
Thay vì phụ thuộc vào một cây duy nhất, \textbf{Ensemble Learning} kết hợp nhiều mô hình để cải thiện độ chính xác.  
\begin{itemize}
    \item \textbf{Bagging} (vd: Random Forest): các mô hình học độc lập, dựa trên dữ liệu bootstrap khác nhau. Mục đích: giảm phương sai.  
    \item \textbf{Boosting} (vd: AdaBoost, Gradient Boosting): các mô hình học tuần tự, mô hình sau tập trung vào những điểm mà mô hình trước sai. Mục đích: giảm thiên lệch.  
    \item \textbf{Stacking}: kết hợp nhiều loại mô hình khác nhau, đầu ra được đưa vào một “meta-learner” để dự đoán cuối cùng.  
\end{itemize}

Trong đó, Boosting đặc biệt phù hợp với cây quyết định nông (Decision Stump), vì nó biến những mô hình yếu này thành một mô hình mạnh.  

\subsection{Kĩ thuật Boosting}
Boosting là quá trình huấn luyện tuần tự: bắt đầu từ một mô hình yếu, sau đó liên tục bổ sung các mô hình mới tập trung vào những mẫu mà mô hình trước đó dự đoán sai. Qua nhiều vòng lặp, hệ thống dần cải thiện độ chính xác tổng thể.  

Ví dụ trực quan: nhiều “học sinh yếu” khi làm kiểm tra có thể sai rất nhiều, nhưng nếu biết phân công đúng phần mà mỗi người có thế mạnh, cả nhóm có thể đạt điểm cao hơn một học sinh đơn lẻ.  

\textbf{Kết luận:} Boosting ra đời để khắc phục hạn chế của Decision Tree đơn lẻ. Bằng cách kết hợp nhiều stump yếu thành một hệ thống mạnh, Boosting đặt nền tảng cho sự phát triển của AdaBoost.  

% ============================================================
\section{Phần 2: Trực giác đằng sau AdaBoost}
Boosting nói chung có nhiều biến thể, nhưng AdaBoost là một trong những thuật toán đầu tiên và đơn giản nhất, đồng thời cũng rất hiệu quả. Điểm đặc biệt của AdaBoost là cách nó phân bổ trọng số cho từng mô hình con: stump nào dự đoán tốt sẽ có tiếng nói mạnh hơn trong mô hình cuối cùng.  

\subsection{Weak Learner là gì ?}
Trong AdaBoost, mô hình cơ bản nhất thường được chọn là \textbf{Decision Stump} — cây quyết định có độ sâu 1. Một stump chỉ xem xét duy nhất một đặc trưng để đưa ra quyết định, ví dụ: “nếu \textit{ChestPain} = Có thì dự đoán bệnh tim = Có, ngược lại = Không”. Đây rõ ràng là một mô hình rất yếu, nhưng khi kết hợp nhiều stump, AdaBoost có thể xây dựng nên một bộ phân loại mạnh mẽ.  

\textit{Ảnh gợi ý:} Một stump chỉ chia dữ liệu theo một đường thẳng, không thể phân loại chính xác toàn bộ điểm.  

\subsection{For loop của AdaBoost – Quy trình trực quan}
Trong AdaBoost, mô hình được xây dựng theo một chuỗi các bước lặp, mỗi bước dùng một weak learner (thường là decision stump) để cải thiện các lỗi của bước trước. Dưới đây là quy trình chi tiết, kết hợp trực giác và cách cập nhật trọng số.

\begin{enumerate}
  \item \textbf{Khởi tạo trọng số cho tất cả các mẫu:}  
    Ban đầu mỗi mẫu \(x_i\) được gán trọng số \(w_i^{(0)} = \frac{1}{n}\), với \(n\) là số mẫu.  
    Điều này tương đương giả sử rằng \"tất cả mẫu đều khó như nhau\".  
    \vspace{0.3cm}
    % HÌNH ẢNH: Dataset ban đầu với trọng số đều nhau
    \fbox{\parbox[c][200pt][c]{400pt}{\centering Hình ảnh minh họa Dataset ban đầu và trọng số đều nhau (200×400)}}
  
  \item \textbf{Huấn luyện stump đầu tiên (weak learner):}  
    Sử dụng dữ liệu đã cho trọng số, chọn stump (đặc trưng + ngưỡng) sao cho lỗi có trọng số (weighted error) là nhỏ nhất.  
    Stump này sẽ phân loại từng mẫu là đúng hoặc sai theo trọng số hiện tại.  
    \vspace{0.3cm}
    % HÌNH ẢNH: Decision stump đầu tiên được chọn, với phân hoạch dữ liệu
    \fbox{\parbox[c][200pt][c]{400pt}{\centering Hình ảnh stump đầu tiên được chọn (200×400)}}
  
  \item \textbf{Tính lỗi có trọng số của stump:}  
    \[
    \varepsilon_1 = \sum_{i=1}^n w_i^{(0)} \cdot \mathbf{1}(y_i \neq G_1(x_i))
    \]  
    Mẫu sai càng có trọng số lớn càng ảnh hưởng tới lỗi tổng.  
    Trực giác: nếu stump sai trên các mẫu nặng, lỗi sẽ cao → ít được tin tưởng.

  \item \textbf{Tính độ tin cậy của stump (Amount of Say / $\alpha_1$):}  
    \[
    \alpha_1 = \frac{1}{2} \ln \frac{1 - \varepsilon_1}{\varepsilon_1}
    \]  
    Stump có lỗi thấp ⇒ $\alpha$ cao ⇒ ảnh hưởng lớn hơn trong kết quả cuối.  

  \item \textbf{Cập nhật trọng số mẫu:}  
    \[
    w_i^{(1)} \propto w_i^{(0)} \exp\big(-\alpha_1 \, y_i \, G_1(x_i)\big)
    \]  
    - Nếu stump dự đoán sai: \(y_i G_1(x_i) = -1\) ⇒ nhân với \(e^{+\alpha_1}\), trọng số tăng lên.  
    - Nếu dự đoán đúng: nhân với \(e^{-\alpha_1}\), trọng số giảm.  
    Sau đó chuẩn hóa sao cho \(\sum_i w_i^{(1)} = 1\).  
    \vspace{0.3cm}
    % HÌNH ẢNH: Trọng số cập nhật sau stump đầu tiên
    \fbox{\parbox[c][200pt][c]{400pt}{\centering Hình ảnh trọng số sau vòng 1 (200×400)}}

  \item \textbf{Lặp lại các vòng tiếp theo:}  
    Sử dụng trọng số mới \(w_i^{(1)}\), huấn luyện stump thứ hai, tính lỗi, tính $\alpha_2$, cập nhật trọng số \( w_i^{(2)} \), … tiếp tục đến khi đạt số vòng quy định hoặc lỗi tổng không giảm nhiều nữa.  
    \vspace{0.3cm}
    % HÌNH ẢNH: Trọng số sau nhiều vòng, mẫu khó được trọng số lớn
    \fbox{\parbox[c][200pt][c]{400pt}{\centering Hình ảnh minh hoạ vòng lặp tiếp theo (200×400)}}

  \item \textbf{Kết hợp các stump thành mô hình cuối:}  
    Cuối cùng, dự đoán đầu ra cho một mẫu mới bằng cách tính tổng có trọng số của các stump:  
    \[
    F(x) = \operatorname{sign}\Big(\sum_{m=1}^M \alpha_m\,G_m(x)\Big)
    \]  
    Các stump có $\alpha$ cao hơn đóng vai trò lớn hơn trong quyết định cuối cùng.  
\end{enumerate}

\textbf{Kết luận phụ phần “For loop”:}  
Quy trình lặp của AdaBoost giúp mô hình chủ động sửa chữa lỗi trước đó bằng cách tăng trọng số các mẫu khó. Nhờ đó, mỗi stump tiếp theo “tập trung” hơn vào những mẫu mà các stump trước bỏ sót, và kết quả cuối là sự kết hợp có trọng số của các stump giỏi—điều này làm cho AdaBoost mạnh hơn nhiều so với từng stump riêng lẻ.

Trực giác: Các stump sau sẽ “chú ý” nhiều hơn đến các mẫu khó mà stump trước bỏ qua.  

\textit{Ảnh gợi ý:} Flowchart AdaBoost với các bước 1 → 5.

\subsection{Sự khác nhau giữa Random Forest và AdaBoost}
\begin{itemize}
    \item \textbf{Random Forest:} tất cả cây con bỏ phiếu ngang nhau, không phân biệt giỏi/kém. Mỗi cây là một “người bạn” có quyền bình đẳng trong hội đồng.  
    \item \textbf{AdaBoost:} mỗi stump có \textbf{trọng số phiếu khác nhau}, stump nào chính xác hơn thì có “tiếng nói” lớn hơn. Đây giống như một hội đồng mà chuyên gia giỏi sẽ có nhiều ảnh hưởng hơn người yếu.  
\end{itemize}

\textbf{Kết luận:} AdaBoost không chỉ dừng lại ở việc kết hợp nhiều stump, mà còn phân bổ “quyền lực” cho từng stump dựa trên độ chính xác. Đây chính là trực giác cốt lõi giúp nó vượt trội hơn so với Random Forest trong nhiều bài toán.  

```


[1] random forest visual http://www.rhaensch.de/vrf.html

[2] ada vs: https://medium.com/data-science/understanding-adaboost-for-decision-tree-ff8f07d2851

ds tree vs: https://towardsdatascience.com/creating-incredible-decision-tree-visualizations-with-dtreeviz-820c6547b6a9/

