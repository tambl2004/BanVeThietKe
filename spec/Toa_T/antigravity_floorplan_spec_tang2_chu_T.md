# QUY CHUẨN THIẾT KẾ MẶT BẰNG TÒA ÁN HÌNH CHỮ T — TẦNG 2 (T-SHAPED UPPER FLOOR SPECIFICATION)

Tài liệu này định nghĩa toàn bộ khung kết cấu hình học, quy chuẩn nét vẽ, bộ mã màu và phương pháp phân bổ phòng chức năng cho **MẶT BẰNG TẦNG 2 (TÒA ÁN HÌNH CHỮ T)**. Cấu trúc gồm Khối Tòa 1 (chính phía Nam) kết hợp Khối Tòa 2 (phía Bắc với hành lang trung tâm giữa 2 dãy phòng).

---

## 1. NGUYÊN TẮC KẾT CẤU & ĐẶC THÙ MẶT BẰNG TẦNG 2

1. **Khối Tòa 1 (Chính phía Nam):**
   * **Tọa độ tổng thể**: `X: 0.0m` đến `32.0m`, `Y: -4.9m` đến `5.4m`.
   * **Hành lang ngang trung tâm**: `Y: -0.9m` đến `0.9m` (rộng `1.8m`, tô màu `#eef4f7`, ghi nhãn `HÀNH LANG`).
   * **Hai đầu hành lang Đông & Tây (`X = 0.0m` và `X = 32.0m`)**: Được bọc kín bằng tường ngoại thất kết cấu (`#1e293b`), có cửa sổ kính lấy sáng ở chính giữa đầu hành lang. KHÔNG có bậc cấp thoát ra ngoài.
   * **Khu vực trung tâm phía Nam (`X: 13.5m` đến `18.5m`, `Y: -4.9m` đến `-0.9m`)**: Chuyển thành **Phòng chức năng độc lập** (không còn sảnh mở đón khách như Tầng 1), bọc kín tường phía Nam tại `Y = -4.9m` (có cửa sổ mặt tiền), không có bậc thang ngoài trời.
   * **Khu vực sảnh thang trung tâm (`X: 13.5m` đến `18.5m`, `Y: 0.9m` đến `5.4m`)**: Nối lên tầng trên. Ô cầu thang bộ (`X: 14.7m` đến `17.3m`, `Y: 1.4m` đến `4.0m`) được tô nền màu **trắng thuần** (`#ffffff`).

2. **Khối Tòa 2 (Phía Bắc / Mặt sau):**
   * **Tọa độ tổng thể**: `X: 3.5m` đến `28.5m`, `Y: 6.2m` đến `14.5m`.
   * **Lối kết nối trung tâm giữa Tòa 1 và Tòa 2**: Mở hoàn toàn không gian thông nhau (`X: 13.5m` đến `18.5m`, `Y: 5.4m` đến `9.5m`), **TUYỆT ĐỐI KHÔNG BẮT TƯỜNG CHẶN** ở `Y = 6.2m`.
   * **Sảnh / Hành lang dọc kéo dài**: Chạy liên tục từ `Y: 0.9m` lên tận tường sau phía Bắc `Y: 14.5m` (`X: 13.5m` đến `18.5m`), tô toàn bộ màu xám xanh nhạt sảnh/hành lang (`#eef4f7`), có cửa sổ thông thoáng ở đỉnh `Y = 14.5m`.
   * **Hành lang ngang Tòa 2**: `Y: 9.5m` đến `11.0m` (rộng `1.5m`, tô màu `#eef4f7`, ghi nhãn `HÀNH LANG`).
   * **Cấu trúc phân bổ phòng Tòa 2**: Các phòng chức năng được chia đều nằm ở 2 bên hành lang trung tâm Tòa 2:
     * *Dãy phòng phía Bắc Tòa 2*: `Y: 11.0m` đến `14.5m` (chia thành các ô phòng từ `X: 3.5m` đến `28.5m`, ô trống trung tâm `X: 13.5m` đến `18.5m` là không gian sảnh/hành lang mở).
     * *Dãy phòng phía Nam Tòa 2*: `Y: 6.2m` đến `9.5m` (chia thành các ô phòng từ `X: 3.5m` đến `28.5m`).

---

## 2. NGUYÊN TẮC BỐ TRÍ PHÒNG DỰA TRÊN SỐ LIỆU KHẢO SÁT (`prompt.md`)

Mỗi công trình tòa án có số lượng và loại phòng khác nhau. Danh sách phòng từ dữ liệu khảo sát được phân bổ vào các cánh không gian kiến trúc theo quy tắc:
* **Tòa 1 - Dãy phía Bắc (`Y: 0.9m` đến `5.4m`)**: Ưu tiên bố trí các phòng lãnh đạo lớn (`Phòng Chánh án`, `Phòng Phó Chánh án`) hoặc phòng làm việc diện tích rộng.
* **Tòa 1 - Dãy phía Nam (`Y: -4.9m` đến `-0.9m`)**: Bố trí các `Phòng Thẩm phán`, `Phòng Thư ký` và ô phòng trung tâm mặt tiền (`X: 13.5m` đến `18.5m`).
* **Tòa 2 - Hai dãy Bắc & Nam (`Y: 6.2m` đến `14.5m`)**: Bố trí các `Phòng Phó Chánh án`, `Phòng Thẩm phán`, `Phòng Thư ký` độc lập hai bên hành lang ngang Tòa 2.

---

## 3. BỘ MÃ MÀU & ĐỒ HỌA (COLOR PALETTE)

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang & Sảnh nối (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Nền Cầu thang Tầng 2 (`COLOR_STAIR_FILL`)**: `#ffffff` (White)
* **Cánh cửa & Nét quét (`COLOR_DOOR_SWING`)**: `#334155`
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a`
* **Chữ phụ (`COLOR_TEXT_MUTED`)**: `#64748b`

---

## 4. THUẬT TOÁN XUẤT BẢN VẼ (EXPORT RULES)

* Định dạng: PNG 300 DPI (`dpi=300`), `bbox_inches='tight'`, `facecolor='#ffffff'`.
* Thư mục đích: `BacNinh/BacNinh7/Tang2/`
* Mã nguồn Python: `generate_floorplan_tang2.py`
* Ảnh xuất bản vẽ: `mat_bang_tang_2.png`
