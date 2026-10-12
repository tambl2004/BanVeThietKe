# TEMPLATE PROMPT TỰ ĐỘNG HÓA VẼ MẶT BẰNG TÒA ÁN (DÙNG CHO CÁC KHU VỰC & THÔNG SỐ MỚI)

Bạn là trợ lý tự động hóa bản vẽ kỹ thuật kiến trúc. Hãy đọc các file quy chuẩn thiết kế:
- `antigravity_floorplan_spec.md` (Quy chuẩn chung cho toàn bộ các tầng)
- `antigravity_floorplan_spec_tang1.md` (Quy chuẩn chi tiết dành riêng cho Tầng 1)
- `antigravity_floorplan_spec_xetxu.md` (Quy chuẩn chi tiết dành riêng cho Khối nhà Xét xử phía Bắc)
- `antigravity_floorplan_spec_tang2_3.md` (Quy chuẩn chi tiết dành riêng cho Tầng 2, Tầng 3...)

Hãy thực thi các yêu cầu sau:

1. **Đọc dữ liệu khảo sát đầu vào** (Tên tòa án, Tầng, Thư mục lưu, Bảng danh sách phòng).
2. **Viết và thực thi mã Python** (sử dụng thư viện `matplotlib`) tuân thủ chính xác 100% các quy tắc thiết kế:
   - **Tiêu đề bản vẽ (Header Title):** Ghi chính xác theo cú pháp `MẶT BẰNG TẦNG {X}  —  {TÊN TÒA ÁN / ĐỊA ĐIỂM}` (Font 20 bold).
   - **Tuyệt đối KHÔNG** vẽ/ghi dòng chữ phụ `"KHUNG KIẾN TRÚC GIẢN LƯỢC..."` phía dưới tiêu đề.
   - **Tên phòng trên bản vẽ:** Phải ghi tên đầy đủ của từng phòng từ Bảng khảo sát (ví dụ: `Phòng Phó chánh án`, `Phòng nhận đơn khởi kiện`...) vào trung tâm từng ô phòng. **KHÔNG** chỉ ghi chữ `"Phòng"` chung chung.
   - **Xử lý số liệu kích thước phòng:** Số liệu kích thước khảo sát chỉ dùng để **ước lượng tỷ lệ tương đối** giữa các phòng (phòng to/nhỏ hơn) và phân chia lấp đầy toàn bộ khung kiến trúc tòa nhà, tuyệt đối **KHÔNG** để trống/bỏ hở không gian phòng nào. **KHÔNG** đưa/in các con số kích thước (VD: 7,8 × 3,6 m) lên ảnh bản vẽ.
   - **Đặc thù Tầng 1:**
     * Có Sảnh đón phía Nam (`X: 7.5` đến `12.5m`, `Y: -4.9` đến `-0.9m`).
     * Lối ra phía Bắc kết nối nhà xét xử: Khối tường kết cấu màu tối (`#1e293b`) kéo dài dọc `X = 7.5m` và `12.5m` lên `Y = 6.2m`, tại đỉnh `Y = 6.2m` có nét tường **quay móc vuông góc vào trong (`0.5m`)**.
     * Nền ô cầu thang Tầng 1 tô trùng màu xám xanh nhạt của Sảnh (`#eef4f7`).
     * Hai đầu hành lang Đông & Tây mở hoàn toàn thoát ra ngoài sân.
   - **Đặc thù Tầng 2, 3...:**
     * KHÔNG có sảnh phía Nam, vị trí sảnh được chuyển thành **Phòng chức năng độc lập**.
     * Hai đầu hành lang Đông & Tây có tường bao che kín (kèm cửa sổ lấy sáng).
     * Ô cầu thang tô nền màu trắng (`#ffffff`).
3. **Xuất kết quả & Lưu trữ đúng cấu trúc thư mục:**
   - Mã nguồn Python: `generate_floorplan_tangX.py`
   - File ảnh PNG chất lượng cao (300 DPI, `bbox_inches='tight'`, `facecolor='#ffffff'`): `mat_bang_tang_X.png`
   - Lưu cả file Python và file ảnh PNG vào đúng thư mục chỉ định bên dưới.

---

### [THÔNG TIN CÔNG TRÌNH & ĐỊA ĐIỂM]
- **Tên Tòa án / Địa điểm:** Tòa án nhân dân khu vực 9 - Cà Mau
- **Số Tòa nhà:** 02
- **Tầng vẽ:** 2
- **Chiều cao tầng:** 4m
- **Thư mục lưu file:** CaMau/CanMau9/Tang2

---

### [BẢNG SỐ LIỆU KHẢO SÁT PHÒNG]
1. Tòa 1
Tp Phương
KT: 4,8m x 3,5m
SL người: 2
Tp. Bình
KT: 4,8m x 4m
SL người: 1
Tp Đào
KT: 4,8m x 3,5m
SL người: 2
Tp. Tồn
KT: 4,8m x 3,5m
SL người: 1
Kho lưu trữ
KT: 6m x 4,5m
Kho lưu trữ
KT: 6m x 4,5m
Tp. Quy
KT: 5m x 4m
SL người: 1
Tp Thu
KT: 8m x 5m
SL người: 3
Tp Kiệt
KT: 5m x3,5m
SL người: 1
Tp Diễm
KT: 6m x 3,5m
SL người: 1
Thư ký
KT: 4m x 3m
SL người: 1
Tp Tú Anh
KT: 5m x 4m
SL người: 1
Tp Nhi
KT: 6m x 4m
SL người: 1
2. Tòa 2 (xét xử mặt sau)
- Xét xử
KT: 12m x 6m
