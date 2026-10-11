# QUY CHUẨN THIẾT KẾ MẶT BẰNG TÒA ÁN HÌNH CHỮ H (H-SHAPED ARCHITECTURAL FLOORPLAN SPECIFICATION)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, bộ mã màu, đồ họa nét vẽ và thuật toán chia phòng tự động dành riêng cho công trình **TÒA ÁN CÓ HÌNH DÁNG HÌNH CHỮ H** (Tổ hợp 2 khối nhà hình chữ I đặt song song và kết nối thông suốt ở trục trung tâm).

---

## 1. NGUYÊN TẮC CỐT LÕI KHUNG KIẾN TRÚC HÌNH CHỮ H

1. **Khối phía Nam (Tòa A - Khối Hành chính / Làm việc):**
   * Cấu trúc hình chữ I với thân giữa và 2 cánh hồi Đông & Tây nhô rộng về 2 phía Nam và Bắc.
   * Hành lang chính nằm ngang xuyên suốt trung tâm (`Y: -0.9m` đến `0.9m`), mở thoát hiểm 2 đầu hồi ra ngoài sân với bậc tam cấp.
   * Phía Nam: Bố trí Sảnh đón chính trung tâm nhô rộng kèm bậc tam cấp và tường má sảnh.
   * Phía Bắc: Bố trí Cầu thang bộ trung tâm và lối thông sang Nhịp cầu nối.
   * Bố trí các phòng làm việc chuyên môn (Phòng 101, Phòng 102...) lấp đầy 100% diện tích hai bên hành lang.

2. **Nhịp cầu nối trung tâm (Connecting Central Corridor & Bridge):**
   * Nằm ở trục trung tâm, kết nối liên hoàn từ hành lang Tòa A sang sảnh khối Xét xử Tòa B.
   * Nền tô màu xám xanh nhạt (`#eef4f7`) liền khối.
   * Tạo 2 khoảng sân trong (Courtyards) thông thoáng hai bên lấy gió và ánh sáng tự nhiên.

3. **Khối phía Bắc (Tòa B - Khối Xét xử):**
   * Cấu trúc hình chữ I song song với Tòa A.
   * Bố trí 2 đại phòng xét xử / hội trường lớn: `Phòng xử án 1` ở Cánh Tây và `Phòng xử án 2` ở Cánh Đông.
   * Sảnh trung tâm khối xét xử đón tiếp trực tiếp từ cầu nối, mở cửa chính vào 2 phòng xử án và có lối thoát sảnh sau ra sân vườn.

---

## 2. BỘ MÃ MÀU & ĐỒ HỌA QUY CHUẨN

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang & Sảnh (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Nền Cầu thang Tầng 1 (`COLOR_STAIR_FILL`)**: `#eef4f7` (Đồng nhất nền Sảnh)
* **Cánh cửa & Cung mở (`COLOR_DOOR_SWING`)**: `#334155` (Nét thẳng + Cung tròn 90°)
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a` (Font 10 – 12 bold)
* **Chữ phụ & Chú thích (`COLOR_TEXT_MUTED`)**: `#64748b` (Font 9.0 – 9.5)

---

## 3. THUẬT TOÁN XUẤT BẢN VẼ

* Tiêu đề: `MẶT BẰNG TẦNG {X}  —  {TÊN TÒA ÁN / ĐỊA ĐIỂM}` (Font 20 bold, không subtitle).
* Không in con số kích thước phòng lên bản vẽ.
* Định dạng file xuất: PNG 300 DPI (`dpi=300`), `bbox_inches='tight'`, `facecolor='#ffffff'`.
