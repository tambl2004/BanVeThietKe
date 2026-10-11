# QUY CHUẨN THIẾT KẾ MẶT BẰNG TÒA ÁN HÌNH CHỮ I (I-SHAPED ARCHITECTURAL FLOORPLAN SPECIFICATION)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, bộ mã màu, đồ họa nét vẽ và thuật toán chia phòng tự động dành riêng cho công trình **TÒA ÁN CÓ HÌNH DÁNG HÌNH CHỮ I** (Layout H-shape/I-shape hai cánh hồi).

---

## 1. NGUYÊN TẮC CỐT LÕI KHUNG KIẾN TRÚC HÌNH CHỮ I (CORE GEOMETRY & LAYOUT)

1. **Phân chia Khối công trình (Building Segmentation):**
   * **Thân giữa (Center Main Block):** Có chiều sâu nhỏ hơn (`Y: -4.4m` đến `4.4m`). 
     * Phía Nam: Bố trí **SẢNH** đón chính trung tâm nhô rộng (`X: 10.5m` đến `15.5m`, `Y: -4.9m` đến `-0.9m`).
     * Phía Bắc: Bố trí **CẦU THANG BỘ TRUNG TÂM** đối diện Sảnh qua hành lang (`X: 10.5m` đến `15.5m`, `Y: 0.9m` đến `4.9m`).
     * Dọc hai bên Sảnh và Cầu thang là các dãy **Phòng chức năng nhỏ/vừa** lấp đầy khoảng giữa.
   * **Hai Cánh Hồi (East & West Wings):** Nhô rộng hơn theo chiều dọc cả về phía Bắc lẫn phía Nam (`Y: -6.2m` đến `6.2m`).
     * **Cánh Trái (West Wing - `X: 0.0m` đến `5.0m`):** 
       * Phía Bắc (`Y > 0.9m`): Bố trí phòng làm việc lớn (VD: `Phòng Phó Chánh An`).
       * Phía Nam (`Y < -0.9m`): Bố trí phòng làm việc lớn chiếm trọn diện tích cánh hồi (VD: `Phòng Thẩm Phán`).
     * **Cánh Phải (East Wing - `X: 20.0m` me đến `25.0m`):** Bố trí các phòng chức năng theo danh sách khảo sát thực tế.
     * **Nhà vệ sinh (WC):** Chỉ thể hiện khi có trong danh sách khảo sát phòng. Nếu không có WC, diện tích góc cánh hồi sẽ được giải phóng toàn bộ cho phòng làm việc chuyên môn.

2. **Hành lang chính & Lối ra vào Sảnh (Corridor & Lobby Exits):**
   * Trục **HÀNH LANG** nằm ngang xuyên suốt trung tâm tòa nhà (`Y: -0.9m` đến `0.9m`).
   * **SẢNH chính trung tâm (`X: 10.0m` đến `15.0m`):** Mở hoàn toàn 100% ở hai đầu Nam (lối vào chính) và Bắc (lối ra sau), **tuyệt đối KHÔNG vẽ tường chặn nằm ngang** tại ranh giới bậc tam cấp lối ra vào Sảnh.
   * **Căn chỉnh chân tường các phòng phía Nam:** Tất cả các tường bao phía Nam của dãy phòng thân giữa phải nằm trên cùng một đường thẳng ngang liên tục (`Y = -4.4m`), không bị giật cấp / lệch tường.
   * **Hai đầu hồi (Đông & Tây):** Mở hoàn toàn thoát ra sân ngoài, thể hiện bằng các bậc tam cấp bên ngoài mép tường (`X < 0.0m` và `X > 26.0m`).
   * **Mặt trước (South Main Entrance):**
     * Nằm tại Sảnh chính (`X: 10.5m` đến `15.5m`).
     * Bậc tam cấp trải dài ngoài mép tường (`Y: -4.9m` xuống `-5.7m`).
     * Tường má sảnh màu tối (`#1e293b`) chạy dọc `X = 10.5m` và `X = 15.5m` từ `Y = -4.9m` xuống `-5.7m`.
   * **Mặt sau (North Rear Exit):**
     * Bậc thang kéo dài từ `Y: 4.9m` lên `5.7m` trải rộng `X: 10.5m` đến `15.5m`.
     * Tường má phía Bắc kéo dài lên `Y = 5.7m` và **quay móc vuông góc vào trong (`0.5m`)** tại đỉnh.

3. **Nền Sảnh & Cầu thang Tầng 1:**
   * Nền Sảnh chính, Hành lang và Ô Cầu thang bộ trung tâm Tầng 1 được tô trùng màu xám xanh nhạt (`#eef4f7`).
   * Ô cầu thang có vạch phân vế dọc chạy từ bậc 2 xuống đáy thang.

---

## 2. BỘ MÃ MÀU & ĐỒ HỌA QUY CHUẨN (COLOR PALETTE & GRAPHICS)

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang & Sảnh (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Nền Cầu thang Tầng 1 (`COLOR_STAIR_FILL`)**: `#eef4f7` (Trùng màu Sảnh)
* **Cánh cửa & Cung mở (`COLOR_DOOR_SWING`)**: `#334155` (Nét thẳng + Cung tròn 90°)
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a` (Font 10 bold / regular)
* **Chữ phụ & Chú thích (`COLOR_TEXT_MUTED`)**: `#64748b` (Font 9.5)

---

## 3. THUẬT TOÁN BỐ TRÍ VÀ XUẤT BẢN VẼ (EXPORT RULES)

1. **Hiển thị Tên phòng:**
   * Ghi tên đầy đủ của từng phòng từ Bảng khảo sát (VD: `Phòng`, `Phòng họp`, `WC`, `KT`, `Cầu thang`...) vào trung tâm từng ô phòng.
   * KHÔNG để trống bất kỳ không gian phòng nào.
2. **Kích thước & Tỷ lệ:**
   * Phân chia diện tích các phòng tương đối theo tỷ lệ khảo sát (đặc biệt Phòng họp bố trí tại vị trí cánh hồi rộng).
   * Tuyệt đối **KHÔNG in/ghi con số kích thước** (VD: 5x4m) lên ảnh bản vẽ.
3. **Định dạng file xuất:**
   * File mã nguồn Python: `generate_floorplan_tang1.py`
   * File ảnh PNG: 300 DPI, `bbox_inches='tight'`, `facecolor='#ffffff'`, tên file `mat_bang_tang_1.png`.
