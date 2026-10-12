import os
import shutil
from typing import TypedDict, Tuple, List, Optional
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class RoomDict(TypedDict):
    id: str
    name: str
    x: float
    y: float
    w: float
    h: float
    text_center: Tuple[float, float]
    door: Optional[Tuple[float, float, float, str]]
    font_size: float

def create_floorplan_tang1(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_1.png')

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    # Kích thước canvas rộng và thoáng phù hợp quy mô công trình tòa to (35m x 13.5m)
    fig = plt.figure(figsize=(26, 15), dpi=300)
    ax = fig.add_axes([0.03, 0.06, 0.94, 0.88])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Bảng màu kiến trúc chuẩn mực theo Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 staircase matching lobby background

    WALL_THICKNESS = 0.22           # 220mm exterior wall
    PART_THICKNESS = 0.12           # 120mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    X_MAX = 35.0                    # Tổng chiều dài tòa nhà mở rộng = 35.0m
    LOBBY_W = 6.0                   # Sảnh trung tâm rộng 6.0m (X: 14.5 to 20.5)

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Tiêu đề bản vẽ (Chuẩn font 20 bold, KHÔNG có dòng phụ)
    fig.text(0.04, 0.962, 'MẶT BẰNG TẦNG 1  —  TÒA ÁN NHÂN DÂN KHU VỰC 1 - CAO BẰNG', 
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    # Đường phân cách tiêu đề
    header_line = plt.Line2D([0.04, 0.96], [0.945, 0.945], transform=fig.transFigure, color='#e2e8f0', linewidth=1.1)
    fig.lines.append(header_line)

    # Chú thích bản vẽ (Legend) đặt gọn gàng phía dưới
    lg_x, lg_y = 5.5, -9.8
    # Legend 1: Hành lang / sảnh
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend 2: Tường / vách
    ax.add_patch(patches.Rectangle((lg_x + 7.0, lg_y + 0.10), 1.2, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 8.5, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend 3: Cửa sổ
    ax.plot([lg_x + 14.0, lg_x + 15.2], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 14.0, lg_x + 15.2], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 15.5, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend 4: Cửa đi mở vào
    ax.plot([lg_x + 20.5, lg_x + 20.5], [lg_y + 0.02, lg_y + 0.32], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 20.5, lg_y + 0.02), 0.60, 0.60, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 21.8, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (TẦNG 1 MÀU #eef4f7)
    # ---------------------------------------------------------
    # Hành lang trung tâm xuyên suốt (X: 0.0 to 35.0, Y: -1.0 to 1.0, rộng 2.0m)
    ax.add_patch(patches.Rectangle((0.0, -1.0), X_MAX, 2.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Sảnh chính phía Nam (X: 14.5 to 20.5, Y: -7.0 to -1.0, kích thước 6.0m x 6.0m)
    ax.add_patch(patches.Rectangle((14.5, -7.0), LOBBY_W, 6.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Sảnh cầu thang bộ phía Bắc (X: 14.5 to 20.5, Y: 1.0 to 6.5, kích thước 6.0m x 5.5m)
    ax.add_patch(patches.Rectangle((14.5, 1.0), LOBBY_W, 5.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (2 PHÒNG XÉT XỬ LỚN + 4 PHÒNG VĂN PHÒNG)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # =========================================================
        # === DÃY NAM: 2 PHÒNG XÉT XỬ LỚN (ĐỐI XỨNG QUA SẢNH CHÍNH) ===
        # =========================================================
        # 1. Phòng xét xử số 01 (Cánh Tây: 14.5m x 6.0m = 87m2)
        {
            'id': 'T1_XX1', 'name': 'Phòng xét xử số 01',
            'x': 0.0, 'y': -7.0, 'w': 14.5, 'h': 6.0,
            'text_center': (7.25, -4.0),
            'door': (8.5, -1.0, 1.4, 'DOUBLE_S'),
            'font_size': 12.0
        },
        # 2. Phòng xét xử số 02 (Cánh Đông: 14.5m x 6.0m = 87m2)
        {
            'id': 'T1_XX2', 'name': 'Phòng xét xử số 02',
            'x': 20.5, 'y': -7.0, 'w': 14.5, 'h': 6.0,
            'text_center': (27.75, -4.0),
            'door': (26.5, -1.0, 1.4, 'DOUBLE_S'),
            'font_size': 12.0
        },

        # =========================================================
        # === DÃY BẮC: 4 PHÒNG CHỨC NĂNG HÀNH CHÍNH (SÂU 5.5m) ===
        # =========================================================
        # --- CÁNH TÂY (2 PHÒNG) ---
        # 3. Phòng Tiếp dân (KT survey: 6,4x3,3m -> thực tế 7.25m x 5.5m)
        {
            'id': 'T1_TIEPDAN', 'name': 'Phòng Tiếp dân',
            'x': 0.0, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (3.625, 3.75),
            'door': (5.8, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        # 4. Phòng Văn Thư (KT survey: 6,4x3,3m -> thực tế 7.25m x 5.5m)
        {
            'id': 'T1_VANTHU', 'name': 'Phòng Văn Thư',
            'x': 7.25, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (10.875, 3.75),
            'door': (8.5, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },

        # --- CÁNH ĐÔNG (2 PHÒNG) ---
        # 5. Phòng Phó chánh văn phòng - Kế Toán (KT survey: 6,4x3,3m -> thực tế 7.25m x 5.5m)
        {
            'id': 'T1_PHO_CVP_KETOAN', 'name': 'Phòng Phó chánh văn phòng - Kế Toán',
            'x': 20.5, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (24.125, 3.75),
            'door': (21.8, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        # 6. Phòng Thư ký (KT survey: 6,4x3,3m, 3 người -> thực tế 7.25m x 5.5m)
        {
            'id': 'T1_THUKY', 'name': 'Phòng Thư ký',
            'x': 27.75, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (31.375, 3.75),
            'door': (29.0, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        }
    ]

    # Tô màu nền trắng thuần cho các phòng chức năng
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES & OUTDOOR ENTRANCE/EXIT STEPS (TẦNG 1 SPEC)
    # ---------------------------------------------------------
    # === CẦU THANG BỘ TRUNG TÂM TẦNG 1 ===
    # Vị trí đặt tại sảnh thang Bắc (X: 16.1 to 18.9, Y: 1.8 to 5.0)
    stair_x, stair_y, stair_w, stair_h = 16.1, 1.8, 2.8, 3.2
    # Nền ô thang tô trùng màu xám xanh sảnh (#eef4f7) theo đúng Spec Tầng 1
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 10
    # Kẻ các bậc thang ngang
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Bậc trên cùng (Landing step) kẻ liền mạch full chiều rộng ô thang
    # Đường vạch dọc phân vế chạy từ bậc 2 xuống đáy thang (không chạm nét kẻ ngang trên cùng)
    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(mid_x, stair_y - 0.25, 'Cầu thang bộ', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='top', zorder=5)

    # === BẬC TAM CẤP NGOẠI THẤT (TẦNG 1 CHUẨN MỰC) ===
    # 1. Mặt tiền Sảnh chính (Phía Nam: Y = -7.0 to -7.8, X = 14.5 to 20.5)
    for sy in [-7.0, -7.16, -7.32, -7.48, -7.64, -7.80]:
        ax.plot([14.5, 20.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # 2. Mặt sau Sảnh thang (Phía Bắc: Y = 6.5 to 7.3, X = 14.5 to 20.5)
    for sy in [6.5, 6.66, 6.82, 6.98, 7.14, 7.30]:
        ax.plot([14.5, 20.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # 3. Hai đầu hành lang Đông & Tây (Outdoor side steps)
    for i in range(5):
        dx = -0.22 * (i + 1)
        dy = 1.0 + i * 0.08
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    for i in range(5):
        dx = X_MAX + 0.22 * (i + 1)
        dy = 1.0 + i * 0.08
        ax.plot([X_MAX, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([X_MAX, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Nhãn Sảnh chính & Hành lang
    ax.text(17.5, -4.0, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(7.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(27.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW STRUCTURAL WALLS & PARTITIONS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # ==========================
    # === TƯỜNG BAO NGOẠI THẤT ===
    # ==========================
    # Vách ngoài biên Tây (X = -W) - hở ở đầu hành lang Y: -1.0 to 1.0
    draw_wall(-W, -7.0 - W, W, 6.0 + W)
    draw_wall(-W, 1.0, W, 5.5 + W)

    # Vách ngoài biên Đông (X = 35.0) - hở ở đầu hành lang Y: -1.0 to 1.0
    draw_wall(X_MAX, -7.0 - W, W, 6.0 + W)
    draw_wall(X_MAX, 1.0, W, 5.5 + W)

    # Tường bao Nam (Y = -7.0 - W) - mở sảnh tại X: 14.5 to 20.5
    draw_wall(-W, -7.0 - W, 14.5 + W + P/2, W)
    draw_wall(20.5 - P/2, -7.0 - W, (X_MAX - 20.5) + W + P/2, W)

    # Tường má Sảnh chính phía Nam (Y: -7.0 down to -7.8m)
    draw_wall(14.5 - P/2, -7.8, P, 0.8)
    draw_wall(20.5 - P/2, -7.8, P, 0.8)

    # Tường bao Bắc (Y = 6.5m) - mở sảnh sau tại X: 14.5 to 20.5
    draw_wall(-W, 6.5, 14.5 + W + P/2, W)
    draw_wall(20.5 - P/2, 6.5, (X_MAX - 20.5) + W + P/2, W)

    # Tường má Sảnh sau phía Bắc (Y: 6.5 up to 7.3m) kèm NÉT MÓC VUÔNG GÓC VÀO TRONG (0.5m) TẠI ĐỈNH PER SPEC
    draw_wall(14.5 - P/2, 6.5, P, 0.8)
    draw_wall(20.5 - P/2, 6.5, P, 0.8)
    draw_wall(14.5 - P/2, 7.3 - P, 0.5, P)        # Móc vuông góc vào trong mép Tây
    draw_wall(20.5 + P/2 - 0.5, 7.3 - P, 0.5, P)  # Móc vuông góc vào trong mép Đông

    # ==========================
    # === VÁCH NGĂN HÀNH LANG ===
    # ==========================
    # Vách ngăn hành lang Bắc (Y = 1.0m) có chừa cửa cho 4 phòng
    # Cánh Tây: Tiếp dân (5.8m), Văn thư (8.5m)
    draw_wall(0.0, 1.0 - P/2, 5.8, P)
    draw_wall(6.7, 1.0 - P/2, 1.8, P)
    draw_wall(9.4, 1.0 - P/2, 5.1, P)
    # X: 14.5 to 20.5 thông sảnh cầu thang
    # Cánh Đông: Phó CVP - Kế toán (21.8m), Thư ký (29.0m)
    draw_wall(20.5, 1.0 - P/2, 1.3, P)
    draw_wall(22.7, 1.0 - P/2, 6.3, P)
    draw_wall(29.9, 1.0 - P/2, 5.1, P)

    # Vách ngăn hành lang Nam (Y = -1.0m) có chừa cửa đôi cho 2 phòng xét xử
    # Cánh Tây: Phòng xét xử 01 (Cửa đôi tại X: 7.8 to 9.2m)
    draw_wall(0.0, -1.0 - P/2, 7.8, P)
    draw_wall(9.2, -1.0 - P/2, 5.3, P)
    # X: 14.5 to 20.5 thông sảnh chính
    # Cánh Đông: Phòng xét xử 02 (Cửa đôi tại X: 25.8 to 27.2m)
    draw_wall(20.5, -1.0 - P/2, 5.3, P)
    draw_wall(27.2, -1.0 - P/2, 7.8, P)

    # ==========================
    # === VÁCH NGĂN PHÒNG NỘI BỘ ===
    # ==========================
    # Dãy Bắc:
    draw_wall(7.25 - P/2, 1.0, P, 5.5)     # Tiếp dân & Văn thư
    draw_wall(14.5 - P/2, 1.0, P, 5.5)     # Văn thư & Sảnh thang
    draw_wall(20.5 - P/2, 1.0, P, 5.5)     # Sảnh thang & Phó CVP - Kế toán
    draw_wall(27.75 - P/2, 1.0, P, 5.5)    # Phó CVP - Kế toán & Thư ký

    # Dãy Nam:
    draw_wall(14.5 - P/2, -7.0, P, 6.0)    # Phòng xét xử 01 & Sảnh chính
    draw_wall(20.5 - P/2, -7.0, P, 6.0)    # Sảnh chính & Phòng xét xử 02

    # ---------------------------------------------------------
    # 7. DRAW WINDOWS ON EXTERIOR WALLS
    # ---------------------------------------------------------
    def draw_window(x, y, w, h, is_horizontal=True):
        if is_horizontal:
            ax.add_patch(patches.Rectangle((x, y - 0.02), w, h + 0.04, facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x, x + w], [y + 0.03, y + 0.03], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x, x + w], [y + h - 0.03, y + h - 0.03], color=COLOR_WALL, linewidth=1.2, zorder=12)
        else:
            ax.add_patch(patches.Rectangle((x - 0.02, y), w + 0.04, h, facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x + 0.03, x + 0.03], [y, y + h], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x + w - 0.03, x + w - 0.03], [y, y + h], color=COLOR_WALL, linewidth=1.2, zorder=12)

    # Cửa sổ mặt tiền Nam (Phòng xét xử 01 & 02: Mỗi phòng 3 cửa sổ lớn trang trọng, bố trí thoáng đãng)
    # Phòng xét xử 01:
    draw_window(2.2, -7.0 - W, 2.2, W, is_horizontal=True)
    draw_window(6.5, -7.0 - W, 2.2, W, is_horizontal=True)
    draw_window(10.8, -7.0 - W, 2.2, W, is_horizontal=True)
    # Phòng xét xử 02:
    draw_window(22.0, -7.0 - W, 2.2, W, is_horizontal=True)
    draw_window(26.3, -7.0 - W, 2.2, W, is_horizontal=True)
    draw_window(30.6, -7.0 - W, 2.2, W, is_horizontal=True)

    # Cửa sổ mặt sau Bắc (Dãy phòng hành chính: Mỗi phòng 2 cửa sổ vừa vặn, chuẩn mực)
    # Tiếp dân:
    draw_window(1.8, 6.5, 1.8, W, is_horizontal=True)
    draw_window(4.6, 6.5, 1.8, W, is_horizontal=True)
    # Văn thư:
    draw_window(9.0, 6.5, 1.8, W, is_horizontal=True)
    draw_window(11.8, 6.5, 1.8, W, is_horizontal=True)
    # Phó CVP - Kế toán:
    draw_window(22.2, 6.5, 1.8, W, is_horizontal=True)
    draw_window(25.0, 6.5, 1.8, W, is_horizontal=True)
    # Thư ký:
    draw_window(29.4, 6.5, 1.8, W, is_horizontal=True)
    draw_window(32.2, 6.5, 1.8, W, is_horizontal=True)

    # Cửa sổ đầu hồi Tây (X = -W) - Mỗi phòng 1 cửa sổ ngay tâm vách, cách xa tuyệt đối lối ra vào hành lang
    draw_window(-W, -4.9, W, 1.8, is_horizontal=False)  # Phòng xét xử 01 (Y: -4.9 to -3.1)
    draw_window(-W, 2.85, W, 1.8, is_horizontal=False)  # Phòng Tiếp dân (Y: 2.85 to 4.65)

    # Cửa sổ đầu hồi Đông (X = 35.0) - Mỗi phòng 1 cửa sổ ngay tâm vách, cách xa tuyệt đối lối ra vào hành lang
    draw_window(X_MAX, -4.9, W, 1.8, is_horizontal=False)  # Phòng xét xử 02 (Y: -4.9 to -3.1)
    draw_window(X_MAX, 2.85, W, 1.8, is_horizontal=False)  # Phòng Thư ký (Y: 2.85 to 4.65)

    # ---------------------------------------------------------
    # 8. DRAW DOORS (INWARD SWINGING PER SPEC)
    # ---------------------------------------------------------
    def draw_door(hx, hy, dw, dtype):
        if dtype == 'N_IN_RIGHT':
            ax.plot([hx, hx], [hy, hy + dw], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((hx, hy), dw * 2, dw * 2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc)
        elif dtype == 'S_IN_RIGHT':
            ax.plot([hx, hx], [hy, hy - dw], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((hx, hy), dw * 2, dw * 2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc)
        elif dtype == 'DOUBLE_S':
            # Double door at Y=-1.0 opening southward into Courtroom
            leaf = dw / 2.0
            # Left leaf
            ax.plot([hx - leaf, hx - leaf], [hy, hy - leaf], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_l = patches.Arc((hx - leaf, hy), leaf * 2, leaf * 2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc_l)
            # Right leaf
            ax.plot([hx + leaf, hx + leaf], [hy, hy - leaf], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_r = patches.Arc((hx + leaf, hy), leaf * 2, leaf * 2, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc_r)

    for r in rooms:
        if r['door'] is not None:
            hx, hy, dw, dtype = r['door']
            draw_door(hx, hy, dw, dtype)

    # ---------------------------------------------------------
    # 9. ROOM TEXT LABELS
    # ---------------------------------------------------------
    for r in rooms:
        tx, ty = r['text_center']
        ax.text(tx, ty, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'], 
                fontweight='bold', ha='center', va='center', zorder=20)

    # ---------------------------------------------------------
    # 10. EXPORT HIGH-RESOLUTION IMAGE (300 DPI)
    # ---------------------------------------------------------
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Floorplan Cao Bang 1 Tầng 1 successfully generated at: {out_img_path}")

    # Copy ảnh và file code sang thư mục cha CaoBang1 để đồng bộ
    parent_dir = os.path.dirname(output_dir)
    if os.path.basename(parent_dir) == 'CaoBang1':
        parent_img = os.path.join(parent_dir, 'mat_bang_tang_1.png')
        shutil.copyfile(out_img_path, parent_img)
        print(f"Copied floorplan to parent directory: {parent_img}")

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    create_floorplan_tang1(script_dir)
