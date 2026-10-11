# QUY CHUẨN THIẾT KẾ MẶT BẰNG TẦNG 1 (GROUND FLOOR SPECIFICATION)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, bộ mã màu, đồ họa nét vẽ và cách bố trí tự động riêng cho **MẶT BẰNG TẦNG 1** (Tầng trệt tòa án).

---

## 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES FOR FLOOR 1)

1. **Trục Sảnh & Hành lang chính:**
   * Tầng 1 có **SẢNH** đón trung tâm ở phía Nam (`X: 7.5m` đến `12.5m`, `Y: -4.9m` đến `-0.9m`).
   * Phía Bắc sảnh kết nối trực tiếp với sảnh cầu thang bộ và hành lang dẫn ra nhà xét xử phía sau (`X: 7.5m` đến `12.5m`, `Y: 0.9m` đến `5.4m`).
   * **Hành lang (East & West)**: Hai đầu hành lang mở hoàn toàn thoát ra sân ngoài.

2. **Lối ra vào Ngoại thất Mặt trước & Mặt sau (Outdoor Entrance & Rear Exit Walls & Steps):**
   * **Mặt trước (South Main Entrance - Phía Nam)**:
     * Nằm ngoài đường biên tòa nhà (`Y < -4.9m`).
     * Bậc tam cấp thể hiện bằng các đường kẻ ngang song song nằm ngoài mép tường (`Y: -4.9m` đến `-5.7m`) trải rộng từ `X = 7.5m` đến `12.5m`.
     * Hai bên mép được xây dựng bằng khối **Tường kết cấu dày màu tối** (`COLOR_WALL`) dọc theo `X = 7.5m` và `X = 12.5m` kéo dài từ `Y = -4.9m` xuống `Y = -5.7m`.
   * **Mặt sau (North Rear Exit to Trial Building - Phía Bắc)**:
     * Nằm ngoài đường biên tòa nhà (`Y > 5.4m`).
     * Bậc thang thể hiện bằng các đường kẻ ngang song song kéo dài từ `Y: 5.4m` đến `6.2m` trải rộng từ `X = 7.5m` đến `12.5m`.
     * Hai bên mép được xây dựng bằng khối **Tường kết cấu dày màu tối** (`COLOR_WALL`) dọc theo `X = 7.5m` và `X = 12.5m` kéo dài lên `Y = 6.2m`.
     * Tại đỉnh trên cùng (`Y = 6.2m`), hai nét tường **quay móc vuông góc vào trong** (`0.5m`).
     * Trong lòng sảnh sau (giữa `Y = 0.9m` và `5.4m`) là không gian sảnh thoáng tô màu `#eef4f7`.

3. **Cầu thang bộ Tầng 1 (Floor 1 Staircase Graphic):**
   * Nền ô cầu thang **tô trùng màu xám xanh nhạt của Sảnh** (`#eef4f7`), không tô màu trắng.
   * Bậc thang trên cùng (Landing step) kẻ ngang liền mạch full chiều rộng ô thang.
   * Đường vạch dọc phân vế chạy từ bậc 2 xuống đáy ô thang (không chạm nét kẻ ngang trên cùng).

---

## 2. BỘ MÃ MÀU & ĐỒ HỌA (COLOR PALETTE & GRAPHICS)

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang & Sảnh (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Nền Cầu thang Tầng 1 (`COLOR_STAIR_FILL`)**: `#eef4f7` (Trùng màu Sảnh)
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a`
* **Chữ phụ (`COLOR_TEXT_MUTED`)**: `#64748b`

---

## 3. THUẬT TOÁN XUẤT BẢN VẼ TẦNG 1 (EXPORT RULES)

* **Tên phòng**: Ghi chính xác tên đầy đủ của từng phòng từ bảng khảo sát vào trung tâm từng ô phòng (ví dụ: `Phòng Phó chánh án`, `Phòng nhận đơn khởi kiện`...). KHÔNG ghi chữ `"Phòng"` chung chung.
* **Tỷ lệ & Kích thước**: Dùng thông số kích thước để ước lượng tỷ lệ tương đối giữa các phòng nhằm lấp đầy toàn bộ khung kiến trúc tòa nhà, không để khoảng hở/bỏ trống phòng. KHÔNG đưa số liệu kích thước (VD: 7,8 × 3,6m) lên ảnh bản vẽ.
* Định dạng: PNG 300 DPI (`dpi=300`).
* Khung viền: `bbox_inches='tight'`, `facecolor='#ffffff'`.
* File xuất demo: [mat_bang_tang_1.png](file:///c:/Users/Tam/Desktop/BanVeThietKe/mat_bang_tang_1.png)
