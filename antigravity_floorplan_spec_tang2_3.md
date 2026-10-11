# QUY CHUẨN THIẾT KẾ MẶT BẰNG TẦNG 2 & TẦNG 3 (UPPER FLOORS SPECIFICATION)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, bộ mã màu, đồ họa nét vẽ và cách bố trí tự động riêng cho **MẶT BẰNG TẦNG 2, TẦNG 3 VÀ CÁC TẦNG TRÊN**.

---

## 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES FOR UPPER FLOORS)

1. **Trục Sảnh & Hành lang chính:**
   * Tầng 2 & 3 **KHÔNG CÓ SẢNH** ở vị trí trung tâm phía Nam (`X: 7.5m` đến `12.5m`, `Y: -4.9m` đến `-0.9m`). Vị trí này được thiết kế thành một **Phòng** chức năng độc lập (có vách ngăn hành lang, cửa đi từ hành lang và cửa sổ hướng ra mặt tiền).
   * Phía Bắc là sảnh cầu thang bộ nội bộ.
   * **Hành lang (East & West)**: Hai đầu hành lang có **TƯỜNG BAO CHE KÍN** (kèm cửa sổ kính lấy sáng ở 2 đầu) để đảm bảo an toàn kết cấu tầng trên.

2. **Lối ra vào & Ngoại thất:**
   * **KHÔNG CÓ BẬC THANG NGOẠI THẤT** ở mặt trước, mặt sau cũng như 2 đầu hành lang.
   * Tường bao ngoại thất chạy liên tục, khép kín.

3. **Cầu thang bộ Tầng 2 & Tầng 3 (Upper Floor Staircase Graphic):**
   * Nền ô cầu thang **tô màu trắng thuần** (`#ffffff`), phân biệt với nền xám xanh nhạt của sảnh thang.
   * Vẽ 2 vế thang đối xứng kẻ các đường bậc ngang song song, có nét phân vế ở giữa.

---

## 2. BỘ MÃ MÀU & ĐỒ HỌA (COLOR PALETTE & GRAPHICS)

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Nền Cầu thang Tầng 2/3 (`COLOR_STAIR_FILL`)**: `#ffffff` (White)
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a`
* **Chữ phụ (`COLOR_TEXT_MUTED`)**: `#64748b`

---

## 3. THUẬT TOÁN XUẤT BẢN VẼ TẦNG 2 & 3 (EXPORT RULES)

* Định dạng: PNG 300 DPI (`dpi=300`).
* Khung viền: `bbox_inches='tight'`, `facecolor='#ffffff'`.
* File xuất demo: [mat_bang_tang_2.png](file:///c:/Users/Tam/Desktop/BanVeThietKe/mat_bang_tang_2.png), [mat_bang_tang_3.png](file:///c:/Users/Tam/Desktop/BanVeThietKe/mat_bang_tang_3.png)
