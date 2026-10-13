# QUY CHUẨN THIẾT KẾ MẶT BẰNG TÒA ÁN HỢP KHỐI HÌNH CHỮ T (1 TÒA DUY NHẤT)
## (UNIFIED T-SHAPED COURTHOUSE COMPLEX — REAR BLOCK SMALLER THAN FRONT BLOCK)

Tài liệu này định nghĩa toàn bộ quy tắc hình học, hệ trục tọa độ, bộ mã màu, đồ họa nét vẽ và thuật toán chia phòng tự động dành cho công trình **TÒA ÁN NHÂN DÂN CÓ CẤU TRÚC HỢP KHỐI 1 TÒA DUY NHẤT** với đặc thù **Tòa sau nhỏ hơn Tòa trước (thụt vào cân đối hai đầu hồi)**, điển hình như công trình Trụ sở Tòa án nhân dân huyện Nậm Pồ / Khu vực 5 - Điện Biên.

---

## 1. NGUYÊN TẮC CỐT LÕI KHUNG KIẾN TRÚC (CORE GEOMETRY & ARCHITECTURE)

Công trình là **MỘT TÒA NHÀ DUY NHẤT (SINGLE UNIFIED BUILDING)**, gồm Khối nhà văn phòng phía trước (Tòa 1 - Khối A) kết hợp Khối xét xử phía sau (Tòa 2 - Khối B) qua nhịp Sảnh nối trung gian thông suốt:

```
                                  [HƯỚNG BẮC - PHÍA SAU]
          X = 0.0m     X = 4.5m          X = 13.5m   X = 18.5m         X = 27.5m     X = 32.0m
                       ┌─────────────────────┬───────────┬─────────────────────┐
                       │                     │  SẢNH SAU │                     │
                       │  PHÒNG XÉT XỬ DÂN SỰ│   XÉT XỬ  │ PHÒNG XÉT XỬ HÌNH SỰ│
Y = 18.0m              │    (HỘI TRƯỜNG 1)   │ TRUNG TÂM │    (HỘI TRƯỜNG 2)   │
                       │                     │           │                     │
Y = 8.0m               └───┬─────────────────┴───┬───┬───┴─────────────────┬───┘
                           │   SÂN TRONG TÂY     │ SẢNH NỐI│ SÂN TRONG ĐÔNG    │
                           │(Lấy sáng/thông gió) │LIỀN KHỐI│(Lấy sáng/thông gió│
Y = 5.4m  ═════════════════╧═════════════════════╧═══╧═══╧═════════════════╧═════════════════
          │                                      │       │                                 │
          │         CÁNH TÂY (VĂN PHÒNG)         │ CẦU   │       CÁNH ĐÔNG (VĂN PHÒNG)     │
Y = 0.9m  ├──────────────────────────────────────┤ THANG ├─────────────────────────────────┤
          │         HÀNH LANG TRUNG TÂM          │ SẢNH  │       HÀNH LANG TRUNG TÂM       │
Y = -0.9m ├──────────────────────────────────────┼───────┼─────────────────────────────────┤
          │         CÁC PHÒNG LÀM VIỆC           │ SẢNH  │       CÁC PHÒNG LÀM VIỆC        │
Y = -4.9m ═══════════════════════════════════════╧══ ĐÓN ╧═════════════════════════════════
                                                 │TAM CẤP│
Y = -5.7m                                        └───────┘
                                  [HƯỚNG NAM - MẶT TIỀN]
```

### A. Tòa 1 (Khối A — Khối Nhà Văn Phòng Phía Trước):
1. **Quy mô & Tọa độ hình học**:
   * Chiều ngang tổng thể: `X: 0.0m` đến `32.0m` (dài `32.0m`, lớn hơn tòa sau).
   * Chiều sâu tổng thể: `Y: -4.9m` đến `5.4m` (sâu `10.3m`).
2. **Hệ trục giao thông ngang & Sảnh**:
   * **Hành lang trung tâm**: `Y: -0.9m` đến `0.9m` (rộng `1.8m`), tô màu `#eef4f7`, ghi nhãn `HÀNH LANG`.
   * **Hai đầu hồi Đông & Tây**: Mở hoàn toàn ra ngoài sân thoát hiểm, trang bị bậc tam cấp ngoài mép tường (`X < 0.0m` và `X > 32.0m`).
   * **Sảnh đón chính Mặt tiền phía Nam**:
     - Tọa độ sảnh: `X: 13.5m` đến `18.5m`, `Y: -4.9m` đến `-0.9m` (rộng `5.0m`).
     - Bậc tam cấp trải rộng từ `Y: -4.9m` xuống `-5.7m` (4 bậc).
     - Tường má sảnh màu tối (`#1e293b`) chạy dọc biên `X = 13.5m` và `X = 18.5m` từ `Y = -4.9m` xuống `-5.7m`.
3. **Cầu thang bộ trung tâm**:
   * Bố trí tại `X: 14.5m` đến `17.5m`, `Y: 1.2m` đến `4.2m` (đối diện sảnh chính qua hành lang).

### B. Nhịp Sảnh Nối Trung Gian (Connecting Link):
1. **Tọa độ & Liên kết**:
   * Tọa độ: `X: 13.5m` đến `18.5m` (rộng `5.0m`), kéo dài từ `Y: 5.4m` (sau Tòa 1) đến `Y: 8.0m` (trước Tòa 2).
   * Nền sảnh tô màu `#eef4f7` liền mạch, đảm bảo tính chất **1 tòa nhà duy nhất**.
   * Hai vách tường biên dọc `X = 13.5m` và `X = 18.5m` là tường chịu lực kín (`#1e293b`), không trổ cửa sổ.

### C. Hai Khoảng Sân Trong Lấy Sáng (Courtyards / Light Wells):
1. **Tọa độ & Công năng**:
   * **Sân trong Tây**: `X: 4.5m` đến `13.5m`, `Y: 5.4m` đến `8.0m`.
   * **Sân trong Đông**: `X: 18.5m` đến `27.5m`, `Y: 5.4m` đến `8.0m`.
   * Giúp toàn bộ các phòng làm việc phía Bắc của Tòa 1 đón ánh sáng và gió tự nhiên đối lưu.

### D. Tòa 2 (Khối B — Khối Xét Xử Phía Sau Nhỏ Hơn):
1. **Quy mô & Tọa độ hình học**:
   * Chiều ngang: `X: 4.5m` đến `27.5m` (chiều dài `23.0m`, **nhỏ hơn Tòa 1**, thụt vào đều `4.5m` ở cả 2 đầu hồi Đông và Tây).
   * Chiều sâu: `Y: 8.0m` đến `18.0m` (sâu `10.0m`).
2. **Phân bổ không gian**:
   * **Sảnh trung tâm khối xét xử**: `X: 13.5m` đến `18.5m`, `Y: 8.0m` đến `18.0m` (nền `#eef4f7` liền khối từ sảnh nối), cuối sảnh có cửa thoát hiểm ra sân sau với bậc tam cấp từ `Y: 18.0m` lên `18.6m` kèm 2 móc tường vuông góc ($0.5\text{m}$).
   * **Cánh Tây Tòa 2 (`X: 4.5m` đến `13.5m`)**: `Phòng Xét xử Dân sự` (Hội trường 1).
   * **Cánh Đông Tòa 2 (`X: 18.5m` đến `27.5m`)**: `Phòng Xét xử Hình sự` (Hội trường 2).
   * Cửa vào các phòng xét xử là cửa đôi 2 cánh (Double Door) mở từ Sảnh trung tâm tại vách `X = 13.5m` và `X = 18.5m`.

---

## 2. BỘ MÃ MÀU & ĐỒ HỌA QUY CHUẨN (COLOR PALETTE)

* **Tường kết cấu (`COLOR_WALL`)**: `#1e293b` (Dark Slate)
* **Nền Hành lang & Sảnh (`COLOR_FILL_CORRIDOR`)**: `#eef4f7` (Pastel Blue-Grey)
* **Nền Phòng chức năng (`COLOR_ROOM_FILL`)**: `#ffffff` (Pure White)
* **Nền Cầu thang Tầng 1 (`COLOR_STAIR_FILL`)**: `#eef4f7` (Đồng nhất nền Sảnh)
* **Nền Cầu thang Tầng 2, 3...**: `#ffffff` (Tô màu trắng)
* **Cánh cửa & Cung mở (`COLOR_DOOR_SWING`)**: `#334155`
* **Chữ chính (`COLOR_TEXT_MAIN`)**: `#0f172a`
* **Chữ phụ (`COLOR_TEXT_MUTED`)**: `#64748b`

---

## 3. QUY TẮC HIỂN THỊ & XUẤT BẢN VẼ

1. **Tiêu đề bản vẽ**: `MẶT BẰNG TẦNG {X}  —  {TÊN TÒA ÁN / ĐỊA ĐIỂM}` (Font 20 bold).
2. **Tên phòng**: Ghi đầy đủ tên phòng căn giữa trong lòng phòng. Tuyệt đối không ghi số liệu kích thước lên bản vẽ.
3. **Độ phân giải & File xuất**: PNG 300 DPI, `bbox_inches='tight'`, `facecolor='#ffffff'`.
