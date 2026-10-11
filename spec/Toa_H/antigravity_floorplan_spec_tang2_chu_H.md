# QUY CHUẨN THIẾT KẾ MẶT BẰNG TÒA ÁN HÌNH CHỮ H — TẦNG 2 (H-SHAPED COMPLEX UPPER FLOOR 2 SPECIFICATION)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, phân bổ mặt bằng, đồ họa kiến trúc và thuật toán sinh bản vẽ tự động dành riêng cho **MẶT BẰNG TẦNG 2 — CÔNG TRÌNH TÒA ÁN HÌNH CHỮ H** (gồm Tòa 1 Khối Hành chính/Văn phòng phía Nam và Tòa 2 Khối Xét xử phía Bắc, liên kết thông suốt qua Nhịp cầu nối trung tâm).

---

## 1. NGUYÊN TẮC CỐT LÕI KHUNG KIẾN TRÚC TẦNG 2 HÌNH CHỮ H

Công trình gồm 3 phân khu kiến trúc chính được tích hợp liền khối trên hệ tọa độ chuẩn:
* **Hệ tọa độ tổng thể**: Chiều ngang `X: 0.0m` đến `48.0m`.
* **Cánh Hồi Tây (West Wing)**: `X: 0.0m` đến `8.0m`.
* **Cánh Hồi Đông (East Wing)**: `X: 40.0m` đến `48.0m`.
* **Nhịp Cầu Nối / Trục Trung Tâm**: `X: 21.0m` đến `27.0m` (rộng `6.0m`).

```
         0.0m            8.0m            21.0m       27.0m           40.0m           48.0m
Y=22.2m  +---------------+                                               +---------------+
         |               |                                               |               |
         |               +---------------+---------------+---------------+               |
Y=20.6m  |                               |               |                               |
         |    PHÒNG 1    |    PHÒNG 2    | SẢNH TR.TÂM B |  SẢNH TẦNG 2  |    PHÒNG 3    |
         |  (Cánh Tây)   |  (Thân Tây)   | (Cầu thang B) |  (Phía Đông)  |  (Cánh Đông)  |
Y=13.2m  |               +---------------+               |               |               |
         |               |   HÀNH LANG   |               |               |               |
Y=11.0m  +---------------+---------------+-------+-------+---------------+---------------+
Y=9.4m   |               |        (SÂN TRONG)    |   |   |   (SÂN TRONG) |               |
         +---------------+                       | C |   |               +---------------+
                                                 | Ầ |   |
                                                 | U |   |
Y=4.5m                   +---------------+-------+ N +---+---------------+
Y=6.2m   +---------------+               |       | Ố |   |               +---------------+
         |                               |   A   | I |   |                               |
Y=0.9m   +---------------+---------------+-------+-------+---------------+---------------+
         |                          HÀNH LANG TÒA 1                                      |
Y=-0.9m  +---------------+---------------+---------------+---------------+---------------+
         |                               |  SẢNH TẦNG 2  |                               |
Y=-4.5m  +---------------+---------------+---------------+---------------+---------------+
         |               |                                               |               |
Y=-6.2m  +---------------+                                               +---------------+
```

---

## 2. CHI TIẾT CẤU TRÚC 3 KHỐI KIẾN TRÚC Ở TẦNG 2

### A. Tòa 1 — Khối Văn phòng / Làm việc phía Nam (Tòa A)
1. **Khung bao & Kích thước**:
   * Chiều ngang `X: 0.0m` đến `48.0m`.
   * Cánh Hồi Tây (`X: 0.0m` đến `8.0m`) & Cánh Hồi Đông (`X: 40.0m` đến `48.0m`): Nhô sâu `Y: -6.2m` đến `6.2m`.
   * Thân giữa (`X: 8.0m` đến `40.0m`): Chiều sâu `Y: -4.5m` đến `4.5m`.
2. **Đặc thù Kiến trúc Tầng 2 của Tòa 1**:
   * **BỊT KÍN ĐẦU HỒI HÀNH LANG**: Hai đầu hồi Đông và Tây (`X = 0.0m` và `X = 48.0m`) tại trục hành lang `Y: -0.9m` đến `0.9m` được xây tường bao kín kết cấu (`#1e293b`), **loại bỏ hoàn toàn bậc tam cấp ngoại thất**. Bố trí cửa sổ kính lấy sáng ở chính giữa hai đầu hồi.
   * **KHÔNG CÒN BẬC TAM CẤP SẢNH CHÍNH**: Bỏ toàn bộ bậc tam cấp phía Nam.
   * **CHUYỂN ĐỔI SẢNH ĐÓN PHÍA NAM THÀNH SẢNH TẦNG 2**: Không gian `X: 21.0m` đến `27.0m`, `Y: -4.5m` đến `-0.9m` đóng vai trò là `SẢNH TẦNG 2` trong nhà, thông suốt với hành lang ngang, bố trí cửa sổ mặt tiền phía Nam.
   * **CẦU THANG BỘ TÒA 1 (CẦU THANG A)**:
     * Vị trí: `X: 23.5m` đến `26.8m`, `Y: 1.2m` đến `4.2m` (đối diện Sảnh tầng 2 qua hành lang).
     * **Nền ô thang tô màu trắng thuần (`#ffffff`)** theo đúng quy chuẩn tầng cao.
     * Vẽ vạch phân vế thang, các bậc thang ngang và mũi tên chỉ hướng kèm nhãn `Cầu thang A\n(Xuống tầng 1)`.
3. **Phân bổ Phòng làm việc Tòa 1**:
   * Dãy Nam (`Y: -4.5m` đến `-0.9m`): Bố trí các phòng làm việc bám hai bên sảnh trung tâm.
   * Dãy Bắc (`Y: 0.9m` đến `4.5m`): Bố trí các phòng làm việc bám hai bên khu cầu thang.
   * Hai cánh Tây và Đông: Chia phòng làm việc lớn ở đầu hồi.

---

### B. Nhịp Cầu Nối Trung Tâm (Connecting Bridge Link)
1. **Kích thước & Tọa độ**:
   * Chiều ngang: `X: 21.0m` đến `27.0m` (rộng `6.0m`).
   * Chiều dọc: `Y: 4.5m` (mép sau Tòa 1) đến `Y: 11.0m` (mép trước Tòa 2).
2. **Quy cách kiến trúc**:
   * Nền hành lang tô màu xám xanh nhạt (`#eef4f7`) liền khối, kết nối dòng lưu thông giữa Tòa 1 và Tòa 2.
   * Hai bên là vách tường chịu lực kiên cố (`#1e293b`), **tuyệt đối KHÔNG trổ cửa sổ** để đảm bảo an toàn kết cấu và tầm nhìn thẩm mỹ hướng ra hai sân trong.
   * Ghi nhãn chính giữa: `HÀNH LANG CẦU NỐI\n(THÔNG 2 TÒA)` (Font 10 bold, màu `#0f172a`).

---

### C. Tòa 2 — Khối Xét xử phía Bắc (Tòa B)
1. **Kích thước & Khung bao**:
   * Chiều ngang `X: 0.0m` đến `48.0m`.
   * Hai Cánh Hồi Tây & Đông: `Y: 9.4m` đến `22.2m` (cao `12.8m`).
   * Thân giữa Tòa 2: `Y: 11.0m` đến `20.6m` (cao `9.6m`).
2. **NGUYÊN TẮC QUAN TRỌNG VỀ TẦNG CAO**:
   * Do công trình có Tầng 3 và Tầng 4, **TUYỆT ĐỐI KHÔNG GHI NHÃN "MÁI CHE"** tại Tòa 2 trên mặt bằng Tầng 2.
   * **LOẠI BỎ TOÀN BỘ BẬC TAM CẤP SẢNH SAU NGOẠI THẤT**: Mặt sau Tòa 2 (`Y = 20.6m` và `Y = 22.2m`) xây tường kín kết hợp cửa sổ, không có cửa ra ngoài sân vườn.
3. **BỐ CỤC CHUẨN 3 PHÒNG LÀM VIỆC TẠI TÒA 2 (THEO QUY HOẠCH KHOANH VÙNG CHỮ X)**:
   * **Phòng 1 (Cánh Tây)**:
     * Tọa độ: `X: 0.0m` đến `8.0m`, `Y: 9.4m` đến `22.2m` (KT: $8.0\text{m} \times 12.8\text{m}$).
     * Vách ngăn phía Đông tại `X = 8.0m`.
     * Cửa đi: Mở tại vách `X = 8.0m`, `Y: 11.5m` đến `12.5m` (mở vào trong phòng), kết nối trực tiếp với Hành lang phía Tây.
     * Cửa sổ: Bố trí ở tường ngoài phía Tây, phía Bắc và phía Nam cánh hồi.
   * **Phòng 2 (Thân Tây phía Bắc)**:
     * Tọa độ: `X: 8.0m` đến `21.0m`, `Y: 13.2m` đến `20.6m` (KT: $13.0\text{m} \times 7.4\text{m}$).
     * Vách ngăn phía Nam tại `Y = 13.2m` ngăn cách với Hành lang nội bộ phía Tây.
     * Vách ngăn phía Đông tại `X = 21.0m` ngăn cách với Sảnh trung tâm Tòa 2.
     * Cửa đi: Mở tại vách `Y = 13.2m`, `X: 17.5m` đến `18.5m` (mở vào trong phòng).
     * Cửa sổ: Bố trí ở tường mặt Bắc (`Y = 20.6m`).
   * **Phòng 3 (Cánh Đông)**:
     * Tọa độ: `X: 40.0m` đến `48.0m`, `Y: 9.4m` đến `22.2m` (KT: $8.0\text{m} \times 12.8\text{m}$).
     * Vách ngăn phía Tây tại `X = 40.0m`.
     * Cửa đi: Mở tại vách `X = 40.0m`, `Y: 15.35m` đến `16.35m` (mở vào trong phòng), thông sang Sảnh tầng 2 phía Đông.
     * Cửa sổ: Bố trí ở tường ngoài phía Đông, phía Bắc và phía Nam cánh hồi.
4. **Không gian Lưu thông & Phụ trợ Tòa 2**:
   * **Hành lang tiếp cận phía Tây**:
     * Tọa độ: `X: 8.0m` đến `21.0m`, `Y: 11.0m` đến `13.2m` (rộng `2.2m`).
     * Nền xám xanh nhạt (`#eef4f7`), dán nhãn `HÀNH LANG`.
     * Bố trí cửa sổ mở ra khoảng sân trong phía Nam (`Y = 11.0m`) lấy gió và ánh sáng tự nhiên.
     * Dẫn thẳng từ Sảnh trung tâm vào cửa Phòng 1 và Phòng 2.
   * **Sảnh trung tâm Tầng 2 & Cầu thang B**:
     * Tọa độ: `X: 21.0m` đến `27.0m`, `Y: 11.0m` đến `20.6m`.
     * Đón nhận trực tiếp luồng giao thông từ Nhịp cầu nối đi sang.
     * Ghi nhãn: `SẢNH TRUNG TÂM\n(TẦNG 2)`.
     * Bố trí **Cầu thang B**: Tọa độ `X: 23.5m` đến `26.8m`, `Y: 14.5m` đến `17.5m`.
     * Nền cầu thang **tô màu trắng (`#ffffff`)**, vẽ vạch chia vế thang và mũi tên kèm chú thích `Cầu thang B\n(Xuống tầng 1)`.
   * **Sảnh tầng 2 phía Đông (Lobby & Waiting Area)**:
     * Tọa độ: `X: 27.0m` đến `40.0m`, `Y: 11.0m` đến `20.6m`.
     * Không gian mở rộng rãi kết nối thông từ Sảnh trung tâm tới Phòng 3 (Cánh Đông).
     * Nền xám xanh nhạt (`#eef4f7`), dán nhãn `SẢNH TẦNG 2` (Font 11 bold).
     * Bố trí cửa sổ ở cả hai mặt tường Bắc (`Y = 20.6m`) và tường Nam (`Y = 11.0m`) nhìn ra sân trong.

---

## 3. QUY CHUẨN CỬA SỔ & CỬA ĐI (DOORS & WINDOWS GRAPHICS)

### A. Cửa sổ (Windows) — QUY CHUẨN MÀU TRẮNG
* **Tuyệt đối KHÔNG vẽ nét màu xanh/cyan** trên bản vẽ mặt bằng.
* **Quy cách thể hiện**:
  * Tạo khoảng mở màu trắng (`facecolor='#ffffff'`, `zorder=11`) khoét xuyên qua chiều dày tường ngoài (`COLOR_WALL`).
  * Kẻ 02 đường nét khung mảnh song song (`color=COLOR_WALL`, `linewidth=1.2`, `zorder=12`) thể hiện khung kính.
  * Bản vẽ phải khớp 100% với ký hiệu mục `Cửa sổ` trong Bảng chú giải (Legend).

### B. Cửa đi (Doors)
* Kích thước cửa đơn chuẩn: Rộng `0.9m`.
* Màu nét: `COLOR_DOOR_SWING = '#334155'`.
* Thể hiện: 01 đoạn thẳng vuông góc tường (thanh cánh cửa mở $90^\circ$, `linewidth=1.4`) + 01 cung tròn $1/4$ đường tròn (`Arc`, `linewidth=1.0`) biểu thị hướng quét mở vào trong phòng.
* **Tuyệt đối KHÔNG để nét tường chạy cắt ngang đè qua lỗ mở cửa đi**.

---

## 4. BỘ MÃ MÀU CHUẨN (COLOR PALETTE)

| Tên biến / Thành phần | Mã màu Hex | Ý nghĩa & Ứng dụng |
| :--- | :--- | :--- |
| `COLOR_WALL` | `#1e293b` | Tường kết cấu bao che ngoại thất & Vách ngăn chia phòng nội thất |
| `COLOR_FILL_CORRIDOR`| `#eef4f7` | Nền hành lang, sảnh đón, nhịp cầu nối (Xám xanh pastel hiện đại) |
| `COLOR_ROOM_FILL` | `#ffffff` | Nền các phòng làm việc, phòng chức năng (Trắng thuần khiết) |
| `COLOR_STAIR_FILL` | `#ffffff` | Nền ô cầu thang tầng trên (Màu trắng, phân biệt với sảnh tầng 1) |
| `COLOR_DOOR_SWING` | `#334155` | Thanh cánh cửa và cung quét mở cửa |
| `COLOR_TEXT_MAIN` | `#0f172a` | Nhãn chữ tên phòng, hành lang, sảnh (Đậm nét navy cao cấp) |
| `COLOR_TEXT_MUTED` | `#64748b` | Chữ ghi chú phụ (Cầu thang, chú giải legend) |

---

## 5. BẢNG CHÚ GIẢI & TIÊU ĐỀ (HEADER & LEGEND)

1. **Tiêu đề bản vẽ (Header Title)**:
   * Đặt tại góc trên bên trái: `fig.text(0.04, 0.962, 'MẶT BẰNG TẦNG 2  —  [TÊN CÔNG TRÌNH / TÒA ÁN]', ...)`
   * Font size: `20`, `fontweight='bold'`, `color='#0f172a'`.
   * Đường kẻ phân cách ngang: `y = 0.945`, `color='#e2e8f0'`, `linewidth=1.2`.
   * **Tuyệt đối KHÔNG có dòng chữ phụ (subtitle)** bên dưới tiêu đề.
2. **Bảng chú giải (Legend)**:
   * Bố trí ở đáy bản vẽ, căn giữa ngang (`y ≈ -8.6m`).
   * Gồm đúng 4 mục tiêu chuẩn:
     1. `Hành lang / sảnh`: Ô chữ nhật màu `#eef4f7`.
     2. `Tường / vách`: Ô chữ nhật đặc màu `#1e293b`.
     3. `Cửa sổ`: 2 vạch song song màu `#1e293b` trên nền mở trắng.
     4. `Cửa đi mở vào`: Nét cánh cửa kèm cung quét $90^\circ$.
3. **Quy cách nhãn tên**:
   * Căn giữa chính xác trọng tâm từng phòng (`ha='center', va='center'`).
   * Ghi đúng tên nghiệp vụ (VD: `Phòng làm việc`), font 10.0 – 12.0 bold.
   * **Tuyệt đối KHÔNG in kích thước mét (VD: 6,3m x 3,6m)** lên ảnh mặt bằng.
   * **Tuyệt đối KHÔNG ghi các nhãn phụ bên ngoài** như "SÂN TRONG", "GIẾNG TRỜI", "KHỐI TÒA A", "KHỐI TÒA B".

---

## 6. XUẤT FILE & MÃ NGUỒN PYTHON

* **Thư mục lưu trữ**: `CaMau/CaMau{KhuVuc}/Tang2` (Ví dụ: `CaMau/CaMau6/Tang2`).
* **Tên file mã nguồn**: `generate_floorplan_tang2.py`.
* **Tên file ảnh xuất bản**: `mat_bang_tang_2.png`.
* **Thông số xuất ảnh**:
  ```python
  plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
  ```
