# QUY CHUẨN THIẾT KẾ MẶT BẰNG KIẾN TRÚC GIẢN LƯỢC (SIMPLIFIED ARCHITECTURAL FLOORPLAN SPECIFICATION)

Bộ quy chuẩn thiết kế bản vẽ mặt bằng 2D cho công trình Tòa án được phân chia thành 2 tài liệu riêng biệt cho từng khối tầng:

---

## 1. PHÂN BẢN QUY CHUẨN THEO TẦNG

1. **[Quy chuẩn Thiết kế Mặt bằng Tầng 1 (antigravity_floorplan_spec_tang1.md)](file:///c:/Users/Tam/Desktop/BanVeThietKe/antigravity_floorplan_spec_tang1.md)**:
   * **Sảnh đón & Lối ra vào**: Có Sảnh chính ở phía Nam kết nối thông với hành lang. Lối ra trước & sau mở rộng nền Sảnh (`#eef4f7`).
   * **Bức tường lối ra phía sau (Mặt Bắc)**: Tường biên kéo dài và quay móc vuông góc vào trong.
   * **Cầu thang bộ Tầng 1**: Nền ô thang **hứng trọn màu xám xanh của Sảnh (`#eef4f7`)**, vạch phân vế chạy từ bậc 2 xuống đáy.
   * **Hành lang**: Hai đầu hành lang mở hoàn toàn thoát ra ngoài sân.

2. **[Quy chuẩn Thiết kế Khối nhà Xét xử phía Bắc (antigravity_floorplan_spec_xetxu.md)](file:///c:/Users/Tam/Desktop/BanVeThietKe/antigravity_floorplan_spec_xetxu.md)**:
   * **Khối nhà xét xử biệt lập phía Bắc**: Dành riêng cho công trình có 2 Phòng Xét xử (Phòng Xét xử dân sự & Phòng Xét xử hình sự) đặt tại khối nhà phía sau (`Y: 6.2m` đến `12.2m`), kết nối qua Sảnh sau Tầng 1 (`X: 13.5m` đến `18.5m`).
   * **Khoảng mở vách tường**: Cắt khoảng hở tường tại vị trí cửa ra vào phòng xét xử, không để nét tường đè qua cửa.

4. **[Quy chuẩn Thiết kế Mặt bằng Tòa nhà Hình chữ I (antigravity_floorplan_spec_chu_I.md)](file:///c:/Users/Tam/Desktop/BanVeThietKe/antigravity_floorplan_spec_chu_I.md)**:
   * **Khung kiến trúc H-Shape/I-Shape**: Thân giữa nhỏ hơn, 2 cánh hồi Đông & Tây nhô rộng hơn về cả 2 phía Bắc & Nam.
   * **Bố trí Sảnh & Cầu thang**: Sảnh đón chính phía Nam, Cầu thang bộ trung tâm phía Bắc đối diện Sảnh.
   * **Phòng họp & Cụm kỹ thuật**: Phòng họp lớn và các cụm WC, Cầu thang phụ/KT đặt tại 2 khối cánh hồi.

---

## 2. QUY CHUẨN CHUNG CHO TOÀN BỘ CÁC TẦNG

* **Tiêu đề bản vẽ (Header Title)**: 
  * Cú pháp tiêu đề chính: `MẶT BẰNG TẦNG {X}  —  {Tên công trình}` (Ví dụ: `MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 11 - Hải Phòng`).
  * Loại bỏ hoàn toàn dòng chữ phụ `"KHUNG KIẾN TRÚC GIẢN LƯỢC  |  Phòng - Hành Lang - Cầu thang"`.
* **Hiển thị tên phòng (Room Labeling)**:
  * Phải ghi tên đầy đủ của từng phòng (ví dụ: `Phòng Phó chánh án`, `Phòng nhận đơn khởi kiện`, `Phòng Văn thư lưu trữ`...) căn giữa trong lòng phòng. Tuyệt đối KHÔNG ghi chữ `"Phòng"` chung chung.
* **Kích thước & Tỷ lệ phòng (Relative Sizing)**:
  * Số liệu kích thước khảo sát chỉ sử dụng để **ước lượng tỷ lệ tương đối giữa các phòng** (ví dụ: Phòng Phó chánh án rộng hơn Phòng Phó chánh văn phòng một chút). 
  * Phân chia không gian phòng lấp đầy toàn bộ khung kiến trúc tòa nhà, tuyệt đối **KHÔNG để trống/bỏ trống không gian phòng**.
  * Tuyệt đối **KHÔNG in/ghi thông số kích thước (VD: 7,8 x 3,6m)** lên ảnh bản vẽ.
* **Color Palette**:
  * `COLOR_WALL`: `#1e293b`
  * `COLOR_FILL_CORRIDOR`: `#eef4f7`
  * `COLOR_ROOM_FILL`: `#ffffff`
  * `COLOR_DOOR_SWING`: `#334155`
  * `COLOR_TEXT_MAIN`: `#0f172a`
  * `COLOR_TEXT_MUTED`: `#64748b`
* **Cửa đi**: Nét cánh cửa + cung tròn $90^\circ$ mở vào trong lòng phòng.
* **Cửa sổ**: Vạch cắt đường đôi song song trên tường bao ngoại thất.
* **Xuất file**: PNG 300 DPI, `bbox_inches='tight'`, `facecolor='#ffffff'`.