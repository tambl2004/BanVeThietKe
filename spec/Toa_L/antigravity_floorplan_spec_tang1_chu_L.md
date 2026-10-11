# QUY CHUẨN THIẾT KẾ MẶT BẰNG TẦNG 1 — TÒA ÁN NHÂN DÂN KHU VỰC 7 AN GIANG (NHÀ CHỮ L CÓ CỬA THÔNG)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, bộ mã màu, đồ họa nét vẽ và cách bố trí tự động riêng cho **MẶT BẰNG TẦNG 1 TÒA ÁN NHÂN DÂN KHU VỰC 7 - AN GIANG** (gồm Tòa 1 - Khối nhà chính và Tòa 2 - Khối nhà phụ kết nối bằng Cửa thông hành lang).

---

## 1. NGUYÊN TẮC CỐT LÕI & CẤU TRÚC HÌNH HỌC (CORE GEOMETRY & ARCHITECTURE)

1. **Cấu trúc 2 Tòa nhà chữ L đặt sát nhau (Connected Buildings Layout):**
   * **Tòa chính (Tòa 1 - Main Building Block)**: Khối nhà nằm ngang phía Tây (`X: 0.0m` đến `20.0m`, `Y: -4.9m` đến `5.4m`).
   * **Tòa phụ (Tòa 2 - Secondary Building Block)**: Khối nhà dọc đặt sát phía Đông (`X: 20.8m` đến `28.8m`, `Y: -12.5m` đến `5.4m`). Mép trên đỉnh Tòa 2 trùng phẳng với Tòa 1 (`Y = 5.4m`).
   * **Khe co giãn / Khoảng hở hẹp**: Giữa 2 tòa là khe hở hẹp `0.8m` (`X: 20.0m` đến `20.8m`).

2. **Hành lang & Lối cửa thông nối (Connecting Passage):**
   * **Cửa thông nối (Connecting Passage)**: Vị trí kết nối giữa hành lang ngang Tòa 1 và hành lang dọc Tòa 2 (`X: 20.0m` đến `20.8m`, `Y: -0.9m` đến `0.9m`).
   * Nền lối đi thông phòng tô màu xám xanh `#eef4f7` liền khối từ Tòa 1 sang Tòa 2.
   * Tường hai bên khe co giãn cắt khoảng mở cửa thông hành lang, tường biên lối nối khép kín 2 đầu `Y = 0.9m` và `Y = -0.9m`.

3. **Cầu thang bộ Tòa 1 & Tòa 2 (Staircases):**
   * **Tòa 1**: Ô cầu thang trung tâm sảnh sau (`X: 8.7m` đến `11.3m`, `Y: 1.4m` đến `4.0m`).
   * **Tòa 2**: Ô cầu thang phía trên bên phải hành lang Tòa 2 (`X: 25.7m` đến `28.8m`, `Y: -1.8m` đến `0.9m`), thông với hành lang dọc Tòa 2.

4. **Yêu cầu Nét vẽ & Cửa ra vào (Clean Wall Openings & Doors):**
   * **Tuyệt đối KHÔNG** vẽ nét tường cắt đè qua cửa ra vào của bất kỳ phòng nào ở Tòa 1 và Tòa 2.
   * **Tuyệt đối KHÔNG** vẽ tường chặn lối vào ô cầu thang ở Tòa 2.
   * **Tuyệt đối KHÔNG** hiển thị nhãn chữ `TÒA 1 — KHỐI NHÀ CHÍNH` hoặc `TÒA 2 — KHỐI NHÀ PHỤ` phía trên các khối nhà. Chỉ giữ lại Tiêu đề chính duy nhất ở góc trên bên trái.
   * **Loại bỏ cửa sổ** trên vách tường phía Tây Tòa 2 (mặt nhìn qua khe co giãn sang Tòa 1).

5. **Phân bổ Các Phòng Khảo sát An Giang 7 (Tầng 1):**
   * **Tòa 1 (5 phòng)**: `Phòng làm việc` (11.5 x 6), `Phòng họp` (15 x 6.5), `Phòng làm việc` (5.7 x 3.7), `Phòng làm việc` (4.5 x 3.5), `Phòng xử án` (11.5 x 6).
   * **Tòa 2 (5 phòng làm việc + 1 Cầu thang)**: 5 x `Phòng làm việc` + 1 `Cầu thang`.
   * Hiển thị chính xác tên phòng từ Bảng khảo sát căn giữa lòng phòng. KHÔNG ghi chữ `"Phòng"` chung chung, KHÔNG in số liệu kích thước (VD: 11.5 x 6m) lên ảnh bản vẽ.

---

## 2. BỘ MÃ MÀU & ĐỒ HỌA (COLOR PALETTE & GRAPHICS)

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang & Sảnh (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a`
* **Chữ phụ (`COLOR_TEXT_MUTED`)**: `#64748b`

---

## 3. QUY CHUẨN XUẤT BẢN VẼ (EXPORT RULES)

* **Tiêu đề bản vẽ**: `MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 7 - An Giang` (Font 20 bold).
* **Định dạng file**: PNG 300 DPI (`dpi=300`), `bbox_inches='tight'`, `facecolor='#ffffff'`.
