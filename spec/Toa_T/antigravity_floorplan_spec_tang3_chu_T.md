# QUY CHUẨN THIẾT KẾ MẶT BẰNG TÒA ÁN HÌNH CHỮ T — TẦNG 3 (T-SHAPED FLOOR 3 SPECIFICATION)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, bộ mã màu, đồ họa nét vẽ và cách xử lý mái che cho **MẶT BẰNG TẦNG 3 (TÒA ÁN HÌNH CHỮ T — BẮC NINH 7)**.

---

## 1. ĐẶC THÙ KẾT CẤU TẦNG 3

1. **Khối Tòa 1 (Chính phía Nam):**
   * **Tọa độ tổng thể**: `X: 0.0m` đến `32.0m`, `Y: -4.9m` đến `5.4m`.
   * **Hành lang ngang trung tâm**: `Y: -0.9m` đến `0.9m` (rộng `1.8m`, tô màu `#eef4f7`, ghi nhãn `HÀNH LANG`).
   * **Hai đầu hành lang Đông & Tây (`X = 0.0m` và `X = 32.0m`)**: Được bọc kín bằng tường ngoại thất kết cấu (`#1e293b`), có cửa sổ kính lấy sáng ở chính giữa.
   * **Ô cầu thang bộ**: `X: 14.7m` đến `17.3m`, `Y: 1.4m` đến `4.0m`, tô nền màu **trắng thuần** (`#ffffff`).
   * **Bố trí 8 phòng Tòa 1**:
     - *Dãy Bắc Cánh Tây*: `Phòng Phó Chánh án` ($X: 0.0 \to 13.5m$, $Y: 0.9 \to 5.4m$)
     - *Dãy Bắc Cánh Đông*: 3 `Phòng Thẩm Phán` ($X: 18.5 \to 23.0m$, $23.0 \to 27.5m$, $27.5 \to 32.0m$, $Y: 0.9 \to 5.4m$)
     - *Dãy Nam Cánh Tây*: `Phòng Thẩm Phán` ($X: 0.0 \to 13.5m$, $Y: -4.9 \to -0.9m$)
     - *Dãy Nam Trung tâm*: `Phòng Thư ký` ($X: 13.5 \to 18.5m$, $Y: -4.9 \to -0.9m$)
     - *Dãy Nam Cánh Đông*: 1 `Phòng Thẩm Phán` ($X: 18.5 \to 25.25m$) + 1 `Phòng Thư ký` ($X: 25.25 \to 32.0m$)

2. **Khối Tòa 2 (Phía Bắc / Mái che Tòa 2):**
   * Do Tòa 2 chỉ cao 2 tầng nên ở Tầng 3, Khối Tòa 2 được thể hiện dưới dạng **MÁI CHE**.
   * **Tọa độ mái che**: `X: 3.5m` đến `28.5m`, `Y: 6.2m` đến `14.5m`.
   * **Đồ họa mái che**: Tô nền màu **trắng thuần** (`#ffffff`), viền tường bọc kín, **KHÔNG kẻ nét gạch chéo**, ghi nhãn đơn giản: `MÁI CHE`.
   * **Bức tường Bắc Tòa 1 (`Y = 5.4m`)**: Khép kín chạy suốt từ `X = 0.0m` đến `32.0m` (có cửa sổ nhìn ra mái che tại đoạn `X: 13.5 \to 18.5m`).

---

## 2. BỘ MÃ MÀU & ĐỒ HỌA (COLOR PALETTE)

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang & Sảnh (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Nền Mái che (`COLOR_ROOF_FILL`)**: `#ffffff` (Pure White)
* **Nền Cầu thang Tầng 3 (`COLOR_STAIR_FILL`)**: `#ffffff` (White)
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a`
* **Chữ phụ (`COLOR_TEXT_MUTED`)**: `#64748b`

---

## 3. THUẬT TOÁN XUẤT BẢN VẼ (EXPORT RULES)

* Định dạng: PNG 300 DPI (`dpi=300`), `bbox_inches='tight'`, `facecolor='#ffffff'`.
* Thư mục đích: `BacNinh/BacNinh7/Tang3/`
* Mã nguồn Python: `generate_floorplan_tang3.py`
* Ảnh xuất bản vẽ: `mat_bang_tang_3.png`
