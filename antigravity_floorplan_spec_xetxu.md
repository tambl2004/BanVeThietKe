# QUY CHUẨN THIẾT KẾ MẶT BẰNG KHỐI NHÀ XÉT XỬ PHÍA BẮC (REAR TRIAL COURTROOM BLOCK SPECIFICATION)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, bộ mã màu, đồ họa nét vẽ và cấu trúc kết nối dành riêng cho các công trình Tòa án có **Khối nhà xét xử biệt lập phía Bắc** (Rear Trial Courtroom Block) kết nối trực tiếp qua Sảnh sau Tầng 1.

---

## 1. THÀNH PHẦN KIẾN TRÚC & NGUYÊN TẮC CỐT LÕI

1. **Khối nhà văn phòng chính (Front Main Building Bar):**
   * Nằm ở phía trước (`Y: -4.9m` đến `5.4m`).
   * Bố trí các phòng làm việc hành chính: Phòng Chánh án, Phó Chánh án, Thẩm phán, Thư ký, Kế toán, Chánh Văn phòng... lấp đầy liền mạch hai cánh Đông & Tây.

2. **Hành lang / Sảnh nối trung tâm (Connecting Lobby Passage):**
   * Nối trực tiếp từ sảnh chính Tầng 1 (`X: 13.5m` đến `18.5m`, chiều rộng `5.0m`) chạy dọc theo trục Bắc (`Y: 0.9m` lên `12.2m`).
   * Nền tô màu xám xanh nhạt (`#eef4f7`) liền khối với Sảnh chính.
   * **Tuyệt đối KHÔNG** ghi dòng chữ phụ `"SẢNH NỐI NHÀ XÉT XỬ"` trên mặt bằng.

3. **Khối nhà xét xử phía Bắc (Rear Trial Block):**
   * Nằm ở tọa độ phía sau (`Y: 6.2m` đến `12.2m`).
   * Chứa 2 Phòng Xét xử chức năng lớn:
     * **Phòng Xét xử dân sự**: Nằm phía Tây sảnh nối (`X: 3.5m` đến `13.5m`, `Y: 6.2m` đến `12.2m`).
     * **Phòng Xét xử hình sự**: Nằm phía Đông sảnh nối (`X: 18.5m` đến `28.5m`, `Y: 6.2m` đến `12.2m`).

4. **Nét tường kết cấu & Cửa đi (Walls & Door Openings):**
   * Tường bao ngoại thất kết cấu màu tối (`COLOR_WALL = '#1e293b'`), độ dày `WALL_THICKNESS = 0.20m`.
   * Vách tường ngăn sảnh nối với phòng xét xử (tại `X = 13.5m` và `X = 18.5m`) **bắt buộc phải CẮT KHOẢNG MỞ CHÓNG CỬA** (`Y: 8.5m` đến `9.5m`). Tuyệt đối **KHÔNG để nét tường đè xuyên qua vạch cửa đi**.
   * Cửa đi mở vào trong lòng phòng xét xử với nét cánh cửa + cung tròn $90^\circ$ (`COLOR_DOOR_SWING = '#334155'`).

5. **Hiển thị Tên phòng & Kích thước:**
   * Hiển thị chính xác tên phòng đầy đủ: `Phòng Xét xử dân sự` và `Phòng Xét xử hình sự` căn giữa lòng phòng (Font size 9.5 bold).
   * Tuyệt đối **KHÔNG in/ghi thông số số liệu kích thước (VD: 6.0m × 10.0m)** lên ảnh bản vẽ.

---

## 2. BỘ MÃ MÀU & ĐỒ HỌA (COLOR PALETTE)

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang & Sảnh nối (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng & Phòng xét xử (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a`
* **Chữ phụ (`COLOR_TEXT_MUTED`)**: `#64748b`

---

## 3. THUẬT TOÁN XUẤT BẢN VẼ (EXPORT RULES)

* Định dạng: PNG 300 DPI (`dpi=300`).
* Khung viền: `bbox_inches='tight'`, `facecolor='#ffffff'`.
* File demo tham chiếu: [demo_xetxu.py](file:///c:/Users/Tam/Desktop/BanVeThietKe/demo_xetxu.py) -> [mat_bang_demo_xetxu.png](file:///c:/Users/Tam/Desktop/BanVeThietKe/mat_bang_demo_xetxu.png)
