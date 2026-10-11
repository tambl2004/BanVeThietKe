# QUY CHUẨN THIẾT KẾ MẶT BẰNG TẦNG 2 — NHÀ CHỮ L (UPPER FLOOR 2 SPECIFICATION)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, bộ mã màu, đồ họa nét vẽ và cách bố trí tự động riêng cho **MẶT BẰNG TẦNG 2 ĐỐI VỚI CÁC CÔNG TRÌNH NHÀ CHỮ L** (gồm Tòa 1 - Khối nhà chính và Tòa 2 - Khối nhà phụ độc lập ở tầng cao).

---

## 1. NGUYÊN TẮC CỐT LÕI & CẤU TRÚC HÌNH HỌC (CORE GEOMETRY & UPPER FLOOR 2 RULES)

1. **Cấu trúc 2 Tòa nhà chữ L độc lập (L-Shaped Separate Upper Floors Layout):**
   * **Tòa chính (Tòa 1 - Main Building Block)**: Khối nhà nằm ngang phía Tây (`X: 0.0m` đến `20.0m`, `Y: -4.9m` đến `5.4m`).
   * **Tòa phụ (Tòa 2 - Secondary Building Block)**: Khối nhà dọc đặt sát phía Đông (`X: 20.8m` đến `28.8m`, `Y: -12.5m` đến `5.4m`). Mép trên đỉnh Tòa 2 trùng phẳng với Tòa 1 (`Y = 5.4m`).
   * **Khe co giãn / Khoảng hở hẹp**: Giữa 2 tòa là khe hở hẹp `0.8m` (`X: 20.0m` đến `20.8m`) thông suốt từ trước ra sau.

2. **BỊT KÍN TƯỜNG & BỐ TRÍ TÒA 2 Ở TẦNG CAO (NO CONNECTING PASSAGE & TÒA 2 STAIRCASE):**
   * **Tường bịt kín khe co giãn**: Tòa 1 (phía Đông `X = 20.0m`) và Tòa 2 (phía Tây `X = 20.8m`) được xây tường bao khép kín hoàn toàn. Không có lối đi thông giữa 2 tòa ở tầng 2 & 3.
   * **Lấp đầy không gian phía Tây Tòa 2**: `Phòng làm việc` phía trên bên trái Tòa 2 được mở rộng lấp đầy lên phía Bắc (`Y` kéo dài từ `-6.7m` lên đến `0.9m`), không để trống vị trí lối nối cũ.
   * **Bố trí Cầu thang bộ Tòa 2**: Phía trên bên phải hành lang Tòa 2 (`X: 25.7m` đến `28.8m`, `Y: -1.8m` đến `0.9m`) được bố trí thêm **Cầu thang bộ** riêng cho Tòa 2 (nền trắng `#ffffff`, kẻ bậc ngang và vách chia vế thang).

3. **Đặc thù Thiết kế Tầng 2 (Upper Floor 2 Modifications):**
   * **KHÔNG CÓ SẢNH CHÍNH NGOẠI THẤT Ở TẦNG 2**: Vị trí trung tâm phía Nam Tòa 1 (`X: 7.5m` đến `12.5m`, `Y: -4.9m` đến `-0.9m`) được chuyển đổi thành **Phòng chức năng khép kín** (có vách ngăn hành lang tại `Y = -0.9m`, cửa đi từ hành lang và cửa sổ mặt tiền phía Nam).
   * **BỎ TOÀN BỘ BẬC TAM CẤP NGOẠI THẤT**: Loại bỏ tất cả bậc thang ngoại thất ở sảnh chính phía Nam, sảnh sau phía Bắc, lối ra hành lang phía Tây Tòa 1 và sảnh phía Nam Tòa 2.
   * **BỊT KÍN ĐẦU HÀNH LANG TẦNG 2**: Đầu hành lang phía Tây Tòa 1 (`X = 0.0m`), đít hành lang phía Đông Tòa 1 (`X = 20.0m`) và phía Nam Tòa 2 (`Y = -12.5m`) được xây tường bao kín (`W = 0.20m`) và bố trí cửa sổ lấy sáng ngoại thất.
   * **Cầu thang bộ Tòa 1 & Tòa 2**: Nền ô cầu thang tô màu trắng thuần (`#ffffff`), vẽ các đường bậc ngang song song kèm vách chia vế thang.

4. **Yêu cầu Nét vẽ Tường & Cửa ra vào (Clean Wall Openings & Doors):**
   * **Tuyệt đối KHÔNG** vẽ nét tường cắt đè qua cửa ra vào của bất kỳ phòng nào ở Tòa 1 và Tòa 2.
   * **Tuyệt đối KHÔNG** hiển thị nhãn chữ `TÒA 1 — KHỐI NHÀ CHÍNH` hoặc `TÒA 2 — KHỐI NHÀ PHỤ` phía trên các khối nhà. Chỉ giữ lại Tiêu đề chính duy nhất ở góc trên bên trái (`MẶT BẰNG TẦNG 2  —  [Tên Công Trình]`).
   * **Loại bỏ cửa sổ** trên vách tường phía Tây Tòa 2 (mặt nhìn qua khe co giãn sang Tòa 1).
   * Vẽ đầy đủ nét tường ranh giới bao quanh các phòng và vách ngăn hành lang.

5. **Hiển thị Tên phòng & Nhãn số liệu:**
   * Hiển thị chính xác tên phòng từ Bảng khảo sát căn giữa lòng phòng. KHÔNG ghi chữ `"Phòng"` chung chung, KHÔNG in số liệu kích thước (VD: 11.5 x 6m) lên ảnh bản vẽ.

---

## 2. BỘ MÃ MÀU & ĐỒ HỌA (COLOR PALETTE & GRAPHICS)

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang & Sảnh (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Nền Cầu thang Tầng 2 (`COLOR_STAIR_FILL`)**: `#ffffff` (White)
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a`
* **Chữ phụ (`COLOR_TEXT_MUTED`)**: `#64748b`

---

## 3. QUY CHUẨN XUẤT BẢN VẼ TẦNG 2 (EXPORT RULES)

* **Tiêu đề bản vẽ**: `MẶT BẰNG TẦNG 2  —  [Tên Tòa án / Khu vực]` (Font 20 bold).
* **Định dạng file**: PNG 300 DPI (`dpi=300`), `bbox_inches='tight'`, `facecolor='#ffffff'`.
