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

### [THÔNG TIN CÔNG TRÌNH & ĐỊA ĐIỂM Tầng 1]
- **Tên Tòa án / Địa điểm:** Tòa án nhân dân khu vực 9 - Thanh Hóa
- **Số Tòa nhà:** 01
- **Tầng vẽ:** 1
- **Chiều cao tầng:** 4m
- **Thư mục lưu file:** ThanhHoa/ThanhHoa9/Tang1


### [BẢNG SỐ LIỆU KHẢO SÁT PHÒNG Tầng 1]
1. Tòa A1
- Phòng tiếp dân
KT: 4x6
SL người: 1
- Phòng xét xử dân sự tầng 1
KT: 6x13

2. Tòa A2
- Phòng phó chánh án
KT: 6x5
SL người: 1
- Phòng họp
KT: 13x5
- Phòng chánh văn - Phòng
KT: 4,5x6
SL người: 1
- Phòng Thẩm phán
KT: 4,5x6
SL người: 1
- Phòng Kế toán
KT: 4,5x6
SL người: 1
- Phòng phó chánh án
KT: 5x7
SL người: 1
- Phòng chánh án
KT: 5x7
SL người: 1
- Phòng thư ký
KT: 4x6
SL người: 1



3. Tòa A3
- Phòng hoà giải viên
KT: 4x7
SL người: 1
- Phòng hoà giải viên
KT: 4x7
SL người: 1
- Phòng xét xử hình sự
KT: 6x23


### [THÔNG TIN CÔNG TRÌNH & ĐỊA ĐIỂM Tầng 2]
- **Tên Tòa án / Địa điểm:** Tòa án nhân dân khu vực 9 - Thanh Hóa
- **Số Tòa nhà:** 01
- **Tầng vẽ:** 2
- **Chiều cao tầng:** 4m
- **Thư mục lưu file:** ThanhHoa/ThanhHoa9/Tang2

### [BẢNG SỐ LIỆU KHẢO SÁT PHÒNG Tầng 2]
1. Tòa A1
- Phòng xét xử dân sự tầng 2
KT: 6x13
- Phòng thư ký
KT: 6x4
SL người: 1
- Phòng hoà giải
KT: 6x4
- Phòng thư ký
KT: 4x6
- Phòng thư ký
KT: 4x6

2. Tòa A2
- Phòng thẩm phán
KT: 4x6
SL người: 1
- Phòng thẩm phán
KT: 4x6
SL người: 1
- Phòng họp
KT: 6x15
- Phòng phó chánh án
KT: 6x7
SL người: 1
- Phòng thư ký
KT: 6x3,5
SL người: 1

3. Tòa A3
(Mái che)

### [THÔNG TIN CÔNG TRÌNH & ĐỊA ĐIỂM Tầng 3]
- **Tên Tòa án / Địa điểm:** Tòa án nhân dân khu vực 9 - Thanh Hóa
- **Số Tòa nhà:** 01
- **Tầng vẽ:** 3
- **Chiều cao tầng:** 4m
- **Thư mục lưu file:** ThanhHoa/ThanhHoa9/Tang3

### [BẢNG SỐ LIỆU KHẢO SÁT PHÒNG Tầng 3]
1. Tòa A1
(Mái che)
2. Tòa A2
- Phòng phó chánh án
KT: 6x8
SL người: 1
- Phòng thẩm phán
KT: 4x6
SL người: 1
- Phòng thư ký
KT: 4x6
SL người: 1
- Phòng thư ký
KT: 4x6
SL người: 1
- Phòng lưu trữ
KT: 4x6
- Phòng phó chánh văn phòng
KT: 4x6
SL người: 1
- Phòng số hoá
KT: 3,5x6
SL người: 1

3. Tòa A3
(Mái che)