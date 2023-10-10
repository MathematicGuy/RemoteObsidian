

#### ![[Basic concept of Data Structure, Algorithm]]


##### [[DATA STRUCTURE OVERVIEW]]


#### **![[Abstract Data Structure]]**


#### **![[Computational Complexity]]**


#### **Recursion**


### ![[Chap 1 - Data Structure HomeWork]]


>%%
>```annotation-json
>{"created":"2023-06-28T04:06:13.044Z","text":"Lấy n^2 vì n^2 là Lớn Nhất.","updated":"2023-06-28T04:06:13.044Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:7a53d631b58db94c951c238b2a91c2e8"},{"href":"vault:/Slide-DSA-Chapter1.pdf"}],"documentFingerprint":"7a53d631b58db94c951c238b2a91c2e8"},"uri":"vault:/Slide-DSA-Chapter1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter1.pdf","selector":[{"type":"TextPositionSelector","start":20337,"end":20360},{"type":"TextQuoteSelector","exact":"T(n) = n2 + 500 = O(n2)","prefix":"ing value of n. We can see that ","suffix":", with c = 2and n0 being approxi"}]}]}
>```
>%%
>*%%PREFIX%%ing value of n. We can see that%%HIGHLIGHT%% ==T(n) = n2 + 500 = O(n2)== %%POSTFIX%%, with c = 2and n0 being approxi*
>%%LINK%%[[#^47zu6ph87rz|show annotation]]
>%%COMMENT%%
>Lấy n^2 vì n^2 là Lớn Nhất.
>%%TAGS%%
>
^47zu6ph87rz


>%%
>```annotation-json
>{"created":"2023-06-28T04:17:13.200Z","text":"Theo Độ phức tạp thuật toán Omega(n^2) -> TH tốt nhất\n thì F(n) = n^2","updated":"2023-06-28T04:17:13.200Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:7a53d631b58db94c951c238b2a91c2e8"},{"href":"vault:/Slide-DSA-Chapter1.pdf"}],"documentFingerprint":"7a53d631b58db94c951c238b2a91c2e8"},"uri":"vault:/Slide-DSA-Chapter1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter1.pdf","selector":[{"type":"TextPositionSelector","start":22426,"end":22450},{"type":"TextQuoteSelector","exact":"2n2 + 3 = Ω(n2)F(n) = n2","prefix":"10 ≤ cn2 ≤ 2n2 +3, for all n ≥ 0","suffix":"Asymptotic notation•To analyze a"}]}]}
>```
>%%
>*%%PREFIX%%10 ≤ cn2 ≤ 2n2 +3, for all n ≥ 0%%HIGHLIGHT%% ==2n2 + 3 = Ω(n2)F(n) = n2== %%POSTFIX%%Asymptotic notation•To analyze a*
>%%LINK%%[[#^m3d5bniozjp|show annotation]]
>%%COMMENT%%
>Theo Độ phức tạp thuật toán Omega(n^2) -> TH tốt nhất
> thì F(n) = n^2
>%%TAGS%%
>
^m3d5bniozjp





>%%
>```annotation-json
>{"created":"2023-06-28T04:23:39.306Z","text":"Trong chương trình có 3 đoạn -> từng đoạn có độ phức tạp lần lượt O(n^2), O(n^3) và O(nlog(2)).\n\n","updated":"2023-06-28T04:23:39.306Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:7a53d631b58db94c951c238b2a91c2e8"},{"href":"vault:/Slide-DSA-Chapter1.pdf"}],"documentFingerprint":"7a53d631b58db94c951c238b2a91c2e8"},"uri":"vault:/Slide-DSA-Chapter1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter1.pdf","selector":[{"type":"TextPositionSelector","start":23334,"end":23345},{"type":"TextQuoteSelector","exact":"Example 6: ","prefix":"(n) + T2(n) = O(max(f(n), g(n)))","suffix":"In a program with 3 execution st"}]}]}
>```
>%%
>*%%PREFIX%%(n) + T2(n) = O(max(f(n), g(n)))%%HIGHLIGHT%% ==Example 6:== %%POSTFIX%%In a program with 3 execution st*
>%%LINK%%[[#^75mtz3zpi12|show annotation]]
>%%COMMENT%%
>Trong chương trình có 3 đoạn -> từng đoạn có độ phức tạp lần lượt O(n^2), O(n^3) và O(nlog(2)).
>
>
>%%TAGS%%
>
^75mtz3zpi12


>%%
>```annotation-json
>{"created":"2023-06-28T04:24:33.317Z","text":"Ấp dụng quy tắc Tổng nên n^4 sẽ là Nghiệm Chính của O(n^4 + n^2)","updated":"2023-06-28T04:24:33.317Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:7a53d631b58db94c951c238b2a91c2e8"},{"href":"vault:/Slide-DSA-Chapter1.pdf"}],"documentFingerprint":"7a53d631b58db94c951c238b2a91c2e8"},"uri":"vault:/Slide-DSA-Chapter1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter1.pdf","selector":[{"type":"TextPositionSelector","start":23695,"end":23713},{"type":"TextQuoteSelector","exact":"O(n4 + n2) = O(n4)","prefix":"g(n)) is also O(f(n)). Example, ","suffix":", O(n + log2n) = O(n).Computing "}]}]}
>```
>%%
>*%%PREFIX%%g(n)) is also O(f(n)). Example,%%HIGHLIGHT%% ==O(n4 + n2) = O(n4)== %%POSTFIX%%, O(n + log2n) = O(n).Computing*
>%%LINK%%[[#^bvwybtkyvzj|show annotation]]
>%%COMMENT%%
>Ấp dụng quy tắc Tổng nên n^4 sẽ là Nghiệm Chính của O(n^4 + n^2)
>%%TAGS%%
>
^bvwybtkyvzj


>%%
>```annotation-json
>{"created":"2023-06-28T04:46:29.107Z","text":"O(n) * 1 không phải O(n) + 1. Vì trong for loop nên dùng quy tắc tích.","updated":"2023-06-28T04:46:29.107Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:7a53d631b58db94c951c238b2a91c2e8"},{"href":"vault:/Slide-DSA-Chapter1.pdf"}],"documentFingerprint":"7a53d631b58db94c951c238b2a91c2e8"},"uri":"vault:/Slide-DSA-Chapter1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter1.pdf","selector":[{"type":"TextPositionSelector","start":24526,"end":24537},{"type":"TextQuoteSelector","exact":"T(n) = O(n)","prefix":" time complexity of an algorithm","suffix":"T(n) = c1n + c2n2 = O(n2)T(n) = "}]}]}
>```
>%%
>*%%PREFIX%%time complexity of an algorithm%%HIGHLIGHT%% ==T(n) = O(n)== %%POSTFIX%%T(n) = c1n + c2n2 = O(n2)T(n) =*
>%%LINK%%[[#^44gd07xyaq5|show annotation]]
>%%COMMENT%%
>O(n) * 1 không phải O(n) + 1. Vì trong for loop nên dùng quy tắc tích.
>%%TAGS%%
>
^44gd07xyaq5


>%%
>```annotation-json
>{"created":"2023-06-28T04:52:57.631Z","text":"nếu Chạy đến khi i^2 = n thì căn n sẽ là giới hạn -> O(căn(n))\n","updated":"2023-06-28T04:52:57.631Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:7a53d631b58db94c951c238b2a91c2e8"},{"href":"vault:/Slide-DSA-Chapter1.pdf"}],"documentFingerprint":"7a53d631b58db94c951c238b2a91c2e8"},"uri":"vault:/Slide-DSA-Chapter1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter1.pdf","selector":[{"type":"TextPositionSelector","start":24718,"end":24722},{"type":"TextQuoteSelector","exact":"T(n)","prefix":" time complexity of an algorithm","suffix":" = O( 𝑛) T(n) = O(n*n*log2n) = "}]}]}
>```
>%%
>*%%PREFIX%%time complexity of an algorithm%%HIGHLIGHT%% ==T(n)== %%POSTFIX%%= O( 𝑛) T(n) = O(n*n*log2n) =*
>%%LINK%%[[#^e19ngjcrdoc|show annotation]]
>%%COMMENT%%
>nếu Chạy đến khi i^2 = n thì căn n sẽ là giới hạn -> O(căn(n))
>
>%%TAGS%%
>
^e19ngjcrdoc


>%%
>```annotation-json
>{"created":"2023-06-28T05:42:53.009Z","text":"1. O(n)\n2. n^2 * log2(n)","updated":"2023-06-28T05:42:53.009Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:7a53d631b58db94c951c238b2a91c2e8"},{"href":"vault:/Slide-DSA-Chapter1.pdf"}],"documentFingerprint":"7a53d631b58db94c951c238b2a91c2e8"},"uri":"vault:/Slide-DSA-Chapter1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter1.pdf","selector":[{"type":"TextPositionSelector","start":24841,"end":24859},{"type":"TextQuoteSelector","exact":"worst-case runtime","prefix":"plexity of an algorithmFind the ","suffix":" complexity of the following Pyt"}]}]}
>```
>%%
>*%%PREFIX%%plexity of an algorithmFind the%%HIGHLIGHT%% ==worst-case runtime== %%POSTFIX%%complexity of the following Pyt*
>%%LINK%%[[#^kaadltuhkte|show annotation]]
>%%COMMENT%%
>1. O(n)
>2. n^2 * log2(n)
>%%TAGS%%
>
^kaadltuhkte


>%%
>```annotation-json
>{"created":"2023-06-28T05:47:59.163Z","text":"Tiếp tục tính với kết quả tính được trước đó, Đến khi đạt điều kiện cho trước.\n","updated":"2023-06-28T05:47:59.163Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:7a53d631b58db94c951c238b2a91c2e8"},{"href":"vault:/Slide-DSA-Chapter1.pdf"}],"documentFingerprint":"7a53d631b58db94c951c238b2a91c2e8"},"uri":"vault:/Slide-DSA-Chapter1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter1.pdf","selector":[{"type":"TextPositionSelector","start":25861,"end":25870},{"type":"TextQuoteSelector","exact":"Recursion","prefix":"al implementation is as follows:","suffix":"THANK YOU More Information Less "}]}]}
>```
>%%
>*%%PREFIX%%al implementation is as follows:%%HIGHLIGHT%% ==Recursion== %%POSTFIX%%THANK YOU More Information Less*
>%%LINK%%[[#^qm60o0rt3id|show annotation]]
>%%COMMENT%%
>Tiếp tục tính với kết quả tính được trước đó, Đến khi đạt điều kiện cho trước.
>
>%%TAGS%%
>
^qm60o0rt3id
