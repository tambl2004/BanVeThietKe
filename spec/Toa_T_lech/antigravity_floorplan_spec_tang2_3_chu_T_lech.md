# QUY CHUẨN THIẾT KẾ MẶT BẰNG TẦNG 2 & TẦNG 3 — TÒA ÁN HỢP KHỐI 1 TÒA DUY NHẤT
## (FLOORS 2 & 3 UNIFIED COURTHOUSE SPECIFICATION — REAR BLOCK SMALLER THAN FRONT BLOCK)

Tài liệu này định nghĩa các quy tắc hình học, đồ họa nét vẽ và phân bổ phòng chuẩn dành riêng cho **TẦNG 2 VÀ TẦNG 3** của công trình **Tòa án nhân dân hợp khối 1 tòa duy nhất (Tòa sau nhỏ hơn Tòa trước)**.

---

## 1. ĐẶC ĐIỂM KIẾN TRÚC KHÁC BIỆT SO VỚI TẦNG 1

1. **Vị trí trên Sảnh đón phía Nam Tòa 1 (`Y: -4.9m` đến `-0.9m`)**:
   * **KHÔNG CÒN SẢNH MỞ**: Không gian này được bao tường kín và chuyển đổi thành **Phòng chức năng độc lập** (ví dụ: `Phòng Chánh án` hoặc `Phòng Phó Chánh án` có diện tích lớn trang trọng ở mặt tiền trung tâm).
   * Cắt vách tường phía Nam để bố trí hệ thống cửa sổ ngoại thất trang trọng hướng ra mặt tiền sân trước.
2. **Hai đầu hồi Hành lang Đông & Tây Tòa 1**:
   * Khép kín bằng tường bao kết cấu (`#1e293b`), **tuyệt đối KHÔNG có bậc tam cấp thoát hiểm** như Tầng 1.
   * Bố trí cửa sổ đôi lấy sáng tự nhiên ở cả hai đầu hồi (`X = 0.0m` và `X = 32.0m`).
3. **Ô Cầu thang bộ**:
   * Nền ô thang được tô **màu trắng (`#ffffff`)** độc lập, không tô màu xám xanh của Sảnh.
   * Thể hiện đầy đủ các bậc thang và vạch lan can tay vịn.
4. **Tòa 2 Phía Bắc (Khối Xét xử Nhỏ Hơn — `X: 4.5m` đến `27.5m`, `Y: 8.0m` đến `18.0m`)**:
   * Thường là không gian thông tầng của hai hội trường xét xử lớn (thể hiện ghi chú hoặc sàn lửng).
   * Trường hợp đổ sàn Tầng 2: Bố trí `Phòng họp hội trường` và các `Phòng Thẩm phán`, `Phòng Nghị án`.

---

## 2. PHÂN BỔ DANH MỤC PHÒNG CHỨC NĂNG TẦNG 2 TIÊU CHUẨN

### A. Tòa 1 Phía Nam:
* **Trung tâm Mặt tiền (`X: 13.5m` đến `18.5m`, `Y: -4.9m` đến `-0.9m`)**: `Phòng Chánh án`.
* **Dãy phòng phía Nam**:
  * Cánh Tây: `Phòng Phó Chánh án`, `Phòng Thẩm phán`.
  * Cánh Đông: `Phòng Phó Chánh án`, `Phòng Thẩm phán`.
* **Dãy phòng phía Bắc**:
  * Cánh Tây (view sân trong Tây): `Phòng Thẩm phán`, `Phòng Thư ký viên`.
  * Cánh Đông (view sân trong Đông): `Phòng Thẩm phán`, `Phòng Thư ký viên`.

### B. Tòa 2 Phía Bắc:
* Cánh Tây: `Phòng Hội trường họp` (hoặc thông tầng xét xử).
* Cánh Đông: `Phòng Hội đồng xét xử & Nghị án`.

---

## 3. BỘ MÃ MÀU & ĐỒ HỌA

* **Tường bao & Vách ngăn (`COLOR_WALL`)**: `#1e293b`
* **Nền Hành lang & Sảnh (`COLOR_FILL_CORRIDOR`)**: `#eef4f7`
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff`
* **Nền Cầu thang Tầng 2, 3 (`COLOR_STAIR_FILL`)**: `#ffffff` (Khác Tầng 1)
* **Cánh cửa & Cung mở (`COLOR_DOOR_SWING`)**: `#334155`
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a`
* **Chữ phụ (`COLOR_TEXT_MUTED`)**: `#64748b`

---

## 4. QUY TẮC HIỂN THỊ & XUẤT BẢN VẼ

* Tiêu đề bản vẽ: `MẶT BẰNG TẦNG {X}  —  {TÊN TÒA ÁN / ĐỊA ĐIỂM}` (Font 20 bold).
* Không in số liệu kích thước lên bản vẽ.
* Định dạng file: PNG 300 DPI, `bbox_inches='tight'`, `facecolor='#ffffff'`.
