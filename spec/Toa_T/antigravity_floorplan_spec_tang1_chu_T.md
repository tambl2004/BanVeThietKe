# QUY CHUẨN THIẾT KẾ MẶT BẰNG TÒA ÁN HÌNH CHỮ T — TẦNG 1 (T-SHAPED BUILDING SPECIFICATION)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, bộ mã màu, đồ họa nét vẽ và phân bổ danh mục phòng chuẩn dành riêng cho công trình **Tòa án nhân dân khu vực 7- Bắc Ninh (Tầng 1)** cấu trúc hình chữ T (Khối Tòa 1 chính kết hợp Khối Tòa 2 hành lang giữa hai bên phòng).

---

## 1. THÀNH PHẦN KIẾN TRÚC & PHÂN BỔ PHÒNG CHỨC NĂNG

### A. Tòa 1 (Chính) — Khối nhà chính phía Nam (6 Phòng):
* **Tọa độ tổng thể**: `X: 0.0m` đến `32.0m`, `Y: -4.9m` đến `5.4m`.
* **Hành lang ngang trung tâm**: `Y: -0.9m` đến `0.9m` (rộng `1.8m`, tô màu `#eef4f7`, ghi nhãn `HÀNH LANG`), có sảnh bậc cấp 2 đầu hồi (`X = 0.0m` và `X = 32.0m`).
* **Sảnh chính trung tâm**: `X: 13.5m` đến `18.5m`, `Y: -4.9m` đến `-0.9m` (bậc cấp sảnh mặt tiền phía Nam `Y: -4.9m` đến `-5.7m`).
* **Cầu thang trung tâm**: Bố trí tại sảnh dọc (`X: 14.7m` đến `17.3m`, `Y: 1.4m` đến `4.0m`).
* **Danh mục 6 phòng Tòa 1 (Ghi trên 1 dòng đơn)**:
  * **Dãy phía Bắc Tòa 1 (`Y: 0.9m` đến `5.4m`)**:
    * *Cánh Tây*: `Phòng Hội trường xét xử` ($X: 0.0 \to 13.5m$)
    * *Cánh Đông*: `Phòng xét xử` ($X: 18.5 \to 32.0m$)
  * **Dãy phía Nam Tòa 1 (`Y: -4.9m` đến `-0.9m`)**:
    * *Cánh Tây*: `Phòng Kế toán` ($X: 0.0 \to 4.5m$), `Phòng Phó Chánh văn phòng` ($X: 4.5 \to 9.0m$), `Phòng Chánh văn phòng` ($X: 9.0 \to 13.5m$).
    * *Cánh Đông*: `Phòng Hội trường xét xử` ($X: 18.5 \to 32.0m$).

### B. Tòa 2 (Mặt sau của sảnh chính) — Rear Block Central Corridor (5 Phòng độc lập):
* **Tọa độ tổng thể**: `X: 3.5m` đến `28.5m`, `Y: 6.2m` đến `14.5m`.
* **Hành lang trung tâm Tòa 2**: `Y: 9.5m` đến `11.0m` (rộng `1.5m`, tô màu `#eef4f7`, ghi nhãn `HÀNH LANG`), nối thẳng vuông góc từ sảnh dọc trung tâm (`X: 13.5m` đến `18.5m`).
* **Danh mục 5 phòng Tòa 2 (Phân bổ 2 bên hành lang trung tâm Tòa 2, ghi trên 1 dòng đơn)**:
  * **Dãy phòng phía Bắc Tòa 2 (`Y: 11.0m` đến `14.5m`)**:

  * **Dãy phòng phía Nam Tòa 2 (`Y: 6.2m` đến `9.5m`)**:
   
---

## 2. BỘ MÃ MÀU & ĐỒ HỌA (COLOR PALETTE)

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang & Sảnh nối (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a`
* **Chữ phụ (`COLOR_TEXT_MUTED`)**: `#64748b`

---

## 3. THUẬT TOÁN XUẤT BẢN VẼ (EXPORT RULES)

* Định dạng: PNG 300 DPI (`dpi=300`), `bbox_inches='tight'`, `facecolor='#ffffff'`.
* Mã nguồn Python: `generate_floorplan_tang1.py`.
