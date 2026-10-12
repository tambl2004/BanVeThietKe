import os
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
    fig = plt.figure(figsize=(24, 17), dpi=300)
    ax = fig.add_axes([0.03, 0.05, 0.94, 0.89])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Architectural Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 staircase matching lobby background

    WALL_THICKNESS = 0.20           # 200mm exterior wall
    PART_THICKNESS = 0.10           # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    X_MAX = 32.0                    # Tòa 1 length = 32.0m

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.04, 0.962, 'MẶT BẰNG TẦNG 1  —  TÒA ÁN NHÂN DÂN KHU VỰC 9 - CÀ MAU', 
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.04, 0.96], [0.945, 0.945], transform=fig.transFigure, color='#e2e8f0', linewidth=1.1)
    fig.lines.append(header_line)

    # Legend Box Centered at Bottom
    lg_x, lg_y = 4.0, -8.2
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 7.0, lg_y + 0.10), 1.2, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 8.5, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 14.0, lg_x + 15.2], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 14.0, lg_x + 15.2], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 15.5, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 20.5, lg_x + 20.5], [lg_y + 0.02, lg_y + 0.32], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 20.5, lg_y + 0.02), 0.60, 0.60, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 21.8, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (SEAMLESS INTEGRATION)
    # ---------------------------------------------------------
    # === TÒA 1 CORRIDOR & LOBBY ===
    # Horizontal Central Corridor (X: 0.0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # South Main Lobby (X: 13.5 to 18.5, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((13.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # North Central Hall / Staircase Space (X: 13.5 to 18.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === CONNECTING LOBBY PASSAGE TO TÒA 2 ===
    # Passage neck connecting Tòa 1 to Tòa 2 (X: 13.5 to 18.5, Y: 5.4 to 7.0)
    ax.add_patch(patches.Rectangle((13.5, 5.4), 5.0, 1.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === TÒA 2: FOYER GIỮA & SẢNH CHỜ XÉT XỬ CÁNH ĐÔNG ===
    # Central Courtroom Lobby / Staircase Hall (X: 13.5 to 18.5, Y: 7.0 to 15.0)
    ax.add_patch(patches.Rectangle((13.5, 7.0), 5.0, 8.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Cánh Đông Tòa 2: Sảnh chờ xét xử / Hành lang sảnh rộng (X: 18.5 to 30.5, Y: 7.0 to 15.0)
    ax.add_patch(patches.Rectangle((18.5, 7.0), 12.0, 8.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (ALL 10 ROOMS FROM SURVEY PROMPT)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # =========================================================
        # === TÒA 1: KHỐI NHÀ CHÍNH PHÍA TRƯỚC (9 PHÒNG) ===
        # =========================================================
        # --- CÁNH TÂY TÒA 1 (4 PHÒNG) ---
        # 1. Phòng Hòa giải (KT survey: 10m x 4m - phòng lớn nhất dãy Bắc Tây)
        {
            'id': 'T1_HOAGIAI', 'name': 'Hòa giải',
            'x': 0.0, 'y': 0.9, 'w': 9.0, 'h': 4.5,
            'text_center': (4.5, 3.15),
            'door': (7.8, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.0
        },
        # 2. Tp. Nhựt (KT survey: 3.5m x 3m - 1 người)
        {
            'id': 'T1_TP_NHUT', 'name': 'Tp. Nhựt',
            'x': 9.0, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (11.25, 3.15),
            'door': (12.2, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        # 3. Văn phòng (KT survey: 6m x 4m - 3 người)
        {
            'id': 'T1_VANPHONG', 'name': 'Văn phòng',
            'x': 0.0, 'y': -4.9, 'w': 6.5, 'h': 4.0,
            'text_center': (3.25, -2.9),
            'door': (5.2, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        # 4. Tp. Đẹp (KT survey: 6m x 4m - 1 người)
        {
            'id': 'T1_TP_DEP', 'name': 'Tp. Đẹp',
            'x': 6.5, 'y': -4.9, 'w': 7.0, 'h': 4.0,
            'text_center': (10.0, -2.9),
            'door': (12.2, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 10.5
        },

        # --- CÁNH ĐÔNG TÒA 1 (5 PHÒNG) ---
        # 5. Tp. Liêm (KT survey: 4.8m x 3m - 2 người)
        {
            'id': 'T1_TP_LIEM', 'name': 'Tp. Liêm',
            'x': 18.5, 'y': 0.9, 'w': 6.5, 'h': 4.5,
            'text_center': (21.75, 3.15),
            'door': (19.8, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        # 6. Tp. Đang (KT survey: 4.8m x 3.5m - 2 người)
        {
            'id': 'T1_TP_DANG', 'name': 'Tp. Đang',
            'x': 25.0, 'y': 0.9, 'w': 7.0, 'h': 4.5,
            'text_center': (28.5, 3.15),
            'door': (26.2, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        # 7. Kế toán (KT survey: 4m x 3m - 1 người)
        {
            'id': 'T1_KETOAN', 'name': 'Kế toán',
            'x': 18.5, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (20.75, -2.9),
            'door': (19.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        # 8. Thư ký Ngân (KT survey: 3.5m x 3m - 1 người)
        {
            'id': 'T1_TK_NGAN', 'name': 'Thư ký Ngân',
            'x': 23.0, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (25.25, -2.9),
            'door': (24.2, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        # 9. Tp. An (KT survey: 4m x 4m - 1 người)
        {
            'id': 'T1_TP_AN', 'name': 'Tp. An',
            'x': 27.5, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (29.75, -2.9),
            'door': (28.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 10.0
        },

        # =========================================================
        # === TÒA 2: KHỐI NHÀ XÉT XỬ PHÍA BẮC (CÁNH TÂY: PHÒNG XỬ ÁN) ===
        # =========================================================
        # 10. Xét xử (KT survey: 12m x 6m - phòng xét xử quy mô đại hội trường)
        {
            'id': 'T2_XETXU', 'name': 'Phòng xét xử',
            'x': 1.5, 'y': 7.0, 'w': 12.0, 'h': 8.0,
            'text_center': (7.5, 11.0),
            'door': (13.5, 10.5, 1.2, 'DOUBLE_W'),
            'font_size': 13.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff` cho các phòng chức năng)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES & ENTRANCE/EXIT STEPS
    # ---------------------------------------------------------
    # === CẦU THANG BỘ TÒA 1 (NORTH HALL TÒA 1) ===
    stair1_x, stair1_y, stair1_w, stair1_h = 14.7, 1.4, 2.6, 2.6
    stair1_bg = patches.Rectangle((stair1_x, stair1_y), stair1_w, stair1_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair1_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair1_y + i * (stair1_h / num_treads)
        ax.plot([stair1_x, stair1_x + stair1_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid1_x = stair1_x + stair1_w / 2.0
    top1_step_y = stair1_y + (num_treads - 1) * (stair1_h / num_treads)
    ax.plot([mid1_x, mid1_x], [stair1_y, top1_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(mid1_x, stair1_y - 0.25, 'Cầu thang bộ', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='top', zorder=5)

    # === CẦU THANG BỘ TÒA 2 (KHỐI XÉT XỬ DẪN LÊN TẦNG 2) ===
    # Đặt đồng trục tại sảnh trung tâm Tòa 2 (X: 14.7 to 17.3, Y: 10.2 to 14.0)
    stair2_x, stair2_y, stair2_w, stair2_h = 14.7, 10.2, 2.6, 3.6
    stair2_bg = patches.Rectangle((stair2_x, stair2_y), stair2_w, stair2_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair2_bg)

    num_treads_2 = 11
    for i in range(num_treads_2 + 1):
        sy = stair2_y + i * (stair2_h / num_treads_2)
        ax.plot([stair2_x, stair2_x + stair2_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid2_x = stair2_x + stair2_w / 2.0
    top2_step_y = stair2_y + (num_treads_2 - 1) * (stair2_h / num_treads_2)
    ax.plot([mid2_x, mid2_x], [stair2_y, top2_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Arrow indicating direction UP to Floor 2
    ax.annotate('', xy=(mid2_x - 0.65, stair2_y + 2.8), xytext=(mid2_x - 0.65, stair2_y + 0.8),
                arrowprops=dict(arrowstyle="->", color=COLOR_WALL, lw=1.2), zorder=6)
    ax.text(mid2_x - 0.65, stair2_y + 1.8, 'LÊN', color=COLOR_TEXT_MUTED, fontsize=7.5, ha='center', va='center', zorder=6,
            bbox=dict(boxstyle='square,pad=0.1', facecolor='#ffffff', edgecolor='none'))

    # Staircase label for Courtroom Block
    ax.text(mid2_x, stair2_y - 0.35, 'Cầu thang khối xét xử\n(Lên tầng 2)', color=COLOR_TEXT_MAIN, 
            fontsize=8.0, fontweight='bold', ha='center', va='top', zorder=5)

    # === BẬC TAM CẤP NGOẠI THẤT ===
    # 1. Mặt tiền Tòa 1 (South Main Entrance: Y = -4.9 to -5.7m, X = 13.5 to 18.5m)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([13.5, 18.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # 2. Hai đầu hành lang Đông & Tây Tòa 1 (Outdoor side steps)
    for i in range(5):
        dx = -0.22 * (i + 1)
        dy = 0.9 + i * 0.08
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    for i in range(5):
        dx = X_MAX + 0.22 * (i + 1)
        dy = 0.9 + i * 0.08
        ax.plot([X_MAX, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([X_MAX, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # 3. Lối ra sau sảnh Tòa 2 (North Rear Exit: Y = 15.0 to 15.8m, X = 13.5 to 18.5m)
    for sy in [15.0, 15.16, 15.32, 15.48, 15.64, 15.80]:
        ax.plot([13.5, 18.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Nhãn Sảnh & Hành lang
    ax.text(16.0, -2.9, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.0, 7.8, 'SẢNH XÉT XỬ', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    
    # Nhãn Hành lang sảnh chờ cánh Đông Tòa 2
    ax.text(24.5, 11.0, 'SẢNH CHỜ XÉT XỬ', color=COLOR_TEXT_MAIN, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW STRUCTURAL WALLS & PARTITIONS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # ==========================
    # === TƯỜNG BAO TÒA 1 ===
    # ==========================
    # Vách ngoài biên Tây (X = -W) - hở ở hành lang Y: -0.9 to 0.9
    draw_wall(-W, -4.9 - W, W, 4.0 + W)
    draw_wall(-W, 0.9, W, 4.5 + W)

    # Vách ngoài biên Đông (X = 32.0) - hở ở hành lang Y: -0.9 to 0.9
    draw_wall(X_MAX, -4.9 - W, W, 4.0 + W)
    draw_wall(X_MAX, 0.9, W, 4.5 + W)

    # Tường bao Nam Tòa 1 (Y = -4.9 - W) - mở sảnh tại X: 13.5 to 18.5
    draw_wall(-W, -4.9 - W, 13.5 + W + P/2, W)
    draw_wall(18.5 - P/2, -4.9 - W, (X_MAX - 18.5) + W + P/2, W)

    # Tường má Sảnh Nam Tòa 1 (Y: -4.9 down to -5.7)
    draw_wall(13.5 - P/2, -5.7, P, 0.8)
    draw_wall(18.5 - P/2, -5.7, P, 0.8)

    # Tường bao Bắc Tòa 1 (Y = 5.4m) - mở nối sang Tòa 2 tại X: 13.5 to 18.5
    draw_wall(-W, 5.4, 13.5 + W + P/2, W)
    draw_wall(18.5 - P/2, 5.4, (X_MAX - 18.5) + W + P/2, W)

    # Vách ngăn hành lang Bắc Tòa 1 (Y = 0.9m) có chừa cửa
    draw_wall(0.0, 0.9 - P/2, 7.8, P)
    draw_wall(8.7, 0.9 - P/2, 3.5, P)
    draw_wall(13.0, 0.9 - P/2, 0.5, P)
    # X: 13.5 to 18.5 thông sảnh
    draw_wall(18.5, 0.9 - P/2, 1.3, P)
    draw_wall(20.7, 0.9 - P/2, 5.5, P)
    draw_wall(27.1, 0.9 - P/2, 4.9, P)

    # Vách ngăn hành lang Nam Tòa 1 (Y = -0.9m) có chừa cửa
    draw_wall(0.0, -0.9 - P/2, 5.2, P)
    draw_wall(6.1, -0.9 - P/2, 6.1, P)
    draw_wall(13.0, -0.9 - P/2, 0.5, P)
    # X: 13.5 to 18.5 thông sảnh
    draw_wall(18.5, -0.9 - P/2, 1.3, P)
    draw_wall(20.7, -0.9 - P/2, 3.5, P)
    draw_wall(25.1, -0.9 - P/2, 3.7, P)
    draw_wall(29.7, -0.9 - P/2, 2.3, P)

    # Vách ngăn phòng nội bộ Tòa 1
    draw_wall(9.0 - P/2, 0.9, P, 4.5)     # Hòa giải & Tp. Nhựt
    draw_wall(13.5 - P/2, 0.9, P, 4.5)    # Tp. Nhựt & Sảnh giữa
    draw_wall(18.5 - P/2, 0.9, P, 4.5)    # Sảnh giữa & Tp. Liêm
    draw_wall(25.0 - P/2, 0.9, P, 4.5)    # Tp. Liêm & Tp. Đang

    draw_wall(6.5 - P/2, -4.9, P, 4.0)    # Văn phòng & Tp. Đẹp
    draw_wall(13.5 - P/2, -4.9, P, 4.0)   # Tp. Đẹp & Sảnh chính
    draw_wall(18.5 - P/2, -4.9, P, 4.0)   # Sảnh chính & Kế toán
    draw_wall(23.0 - P/2, -4.9, P, 4.0)   # Kế toán & Thư ký Ngân
    draw_wall(27.5 - P/2, -4.9, P, 4.0)   # Thư ký Ngân & Tp. An

    # ==========================
    # === SẢNH NỐI & TÒA 2 (CÂN ĐỐI 2 BÊN) ===
    # ==========================
    # Vách cổ nối Tây (X = 13.5m, Y: 5.4 to 7.0)
    draw_wall(13.5 - P/2, 5.4, P, 1.6)

    # Vách cổ nối Đông (X = 18.5m, Y: 5.4 to 7.0)
    draw_wall(18.5 - P/2, 5.4, P, 1.6)

    # Vách ngăn Sảnh giữa với Phòng Xét xử (X = 13.5m, Y: 7.0 to 15.0) - CẮT KHOẢNG MỞ CỬA TẠI Y: 10.5 TO 11.7
    draw_wall(13.5 - P/2, 7.0, P, 3.5)
    draw_wall(13.5 - P/2, 11.7, P, 3.3)


    # --- TƯỜNG NGOẠI THẤT CÁNH TÂY TÒA 2 (PHÒNG XÉT XỬ) ---
    # Tường Nam Tây Tòa 2 (Y = 7.0 - W, X: 1.5 - W to 13.5)
    draw_wall(1.5 - W, 7.0 - W, 12.0 + W + P/2, W)
    # Tường Tây Tòa 2 (X = 1.5 - W, Y: 7.0 - W to 15.0 + W)
    draw_wall(1.5 - W, 7.0 - W, W, 8.0 + 2*W)
    # Tường Bắc Tây Tòa 2 (Y = 15.0m, X: 1.5 - W to 13.5 + P/2)
    draw_wall(1.5 - W, 15.0, 12.0 + W + P/2, W)

    # --- TƯỜNG NGOẠI THẤT CÁNH ĐÔNG TÒA 2 (SẢNH CHỜ XÉT XỬ) ---
    # Tường Nam Đông Tòa 2 (Y = 7.0 - W, X: 18.5 to 30.5 + W)
    draw_wall(18.5 - P/2, 7.0 - W, 12.0 + W + P/2, W)
    # Tường Đông Tòa 2 (X = 30.5m, Y: 7.0 - W to 15.0 + W)
    draw_wall(30.5, 7.0 - W, W, 8.0 + 2*W)
    # Tường Bắc Đông Tòa 2 (Y = 15.0m, X: 18.5 - P/2 to 30.5 + W)
    draw_wall(18.5 - P/2, 15.0, 12.0 + W + P/2, W)

    # --- TƯỜNG MÁ LỐI RA SAU TÒA 2 (X = 13.5 TO 18.5) & MÓC VUÔNG GÓC VÀO TRONG ---
    draw_wall(13.5 - P/2, 15.0, P, 0.8)
    draw_wall(18.5 - P/2, 15.0, P, 0.8)
    # Móc vuông góc vào trong tại Y = 15.8m (0.5m)
    draw_wall(13.5 - P/2, 15.8 - P, 0.5, P)
    draw_wall(18.5 + P/2 - 0.5, 15.8 - P, 0.5, P)

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

    # Windows on Tòa 1 North Wall (Y = 5.4m)
    draw_window(1.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(5.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(10.2, 5.4, 2.0, W, is_horizontal=True)
    draw_window(20.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(27.5, 5.4, 2.0, W, is_horizontal=True)

    # Windows on Tòa 1 South Wall (Y = -4.9m - W)
    draw_window(1.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(4.5, -4.9 - W, 1.6, W, is_horizontal=True)
    draw_window(8.0, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(11.0, -4.9 - W, 1.6, W, is_horizontal=True)
    draw_window(19.8, -4.9 - W, 1.8, W, is_horizontal=True)
    draw_window(24.2, -4.9 - W, 1.8, W, is_horizontal=True)
    draw_window(28.8, -4.9 - W, 1.8, W, is_horizontal=True)

    # Windows on Tòa 1 East/West end walls
    draw_window(-W, 2.0, W, 1.8, is_horizontal=False)
    draw_window(-W, -3.8, W, 1.8, is_horizontal=False)
    draw_window(X_MAX, 2.0, W, 1.8, is_horizontal=False)
    draw_window(X_MAX, -3.8, W, 1.8, is_horizontal=False)

    # Windows on Tòa 2 (Khối xét xử & Sảnh chờ)
    # Tường Tây Tòa 2 (X = 1.5 - W)
    draw_window(1.5 - W, 8.5, W, 1.8, is_horizontal=False)
    draw_window(1.5 - W, 11.5, W, 1.8, is_horizontal=False)
    # Tường Nam Cánh Tây Tòa 2 (Y = 7.0 - W)
    draw_window(3.5, 7.0 - W, 2.2, W, is_horizontal=True)
    draw_window(8.5, 7.0 - W, 2.2, W, is_horizontal=True)
    # Tường Bắc Cánh Tây Tòa 2 (Y = 15.0m)
    draw_window(3.5, 15.0, 2.2, W, is_horizontal=True)
    draw_window(8.5, 15.0, 2.2, W, is_horizontal=True)

    # Tường Đông Tòa 2 (X = 30.5m)
    draw_window(30.5, 8.5, W, 1.8, is_horizontal=False)
    draw_window(30.5, 11.5, W, 1.8, is_horizontal=False)
    # Tường Nam Cánh Đông Tòa 2 (Y = 7.0 - W)
    draw_window(20.5, 7.0 - W, 2.2, W, is_horizontal=True)
    draw_window(25.5, 7.0 - W, 2.2, W, is_horizontal=True)
    # Tường Bắc Cánh Đông Tòa 2 (Y = 15.0m)
    draw_window(20.5, 15.0, 2.2, W, is_horizontal=True)
    draw_window(25.5, 15.0, 2.2, W, is_horizontal=True)

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
        elif dtype == 'DOUBLE_W':
            # Double door at X=13.5 opening westward into Courtroom
            leaf = dw / 2.0
            # Bottom leaf
            ax.plot([hx, hx - leaf], [hy, hy], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_b = patches.Arc((hx, hy), leaf * 2, leaf * 2, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc_b)
            # Top leaf
            ax.plot([hx, hx - leaf], [hy + dw, hy + dw], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_t = patches.Arc((hx, hy + dw), leaf * 2, leaf * 2, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc_t)

    for r in rooms:
        if r['door']:
            dx, dy, dw, dtype = r['door']
            draw_door(dx, dy, dw, dtype)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS (FULL ROOM NAMES FROM SURVEY PROMPT)
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'], 
                fontweight='bold', ha='center', va='center', zorder=20)

    # Save high-resolution PNG (300 DPI, white background, tight bounding box)
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Floorplan CaMau 9 Tầng 1 successfully generated at: {out_img_path}")

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau9\Tang1"
    create_floorplan_tang1(target_dir)
