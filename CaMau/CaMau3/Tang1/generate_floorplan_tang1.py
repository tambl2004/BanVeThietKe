import os
from typing import TypedDict, Tuple, List, Optional
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class RoomDict(TypedDict):
    id: str
    name: str
    sub: str
    x: float
    y: float
    w: float
    h: float
    text_center: Tuple[float, float]
    font_size: float

def create_floorplan_tang1(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_1.png')

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 22), dpi=300)
    ax = fig.add_axes([0.03, 0.04, 0.94, 0.90])
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

    WALL_THICKNESS = 0.22           # 220mm exterior wall
    PART_THICKNESS = 0.12           # 120mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.04, 0.965, 'MẶT BẰNG TẦNG 1  —  TÒA ÁN NHÂN DÂN KHU VỰC 3 CÀ MAU', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.04, 0.96], [0.948, 0.948], transform=fig.transFigure, color='#e2e8f0', linewidth=1.2)
    fig.lines.append(header_line)

    # Legend Box at Bottom Center
    lg_x, lg_y = 6.0, -8.6
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.38, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.06, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 8.0, lg_y + 0.11), 1.2, 0.16, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 9.5, lg_y + 0.06, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 15.5, lg_x + 16.7], [lg_y + 0.24, lg_y + 0.24], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 15.5, lg_x + 16.7], [lg_y + 0.09, lg_y + 0.09], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 17.0, lg_y + 0.06, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 22.5, lg_x + 22.5], [lg_y + 0.02, lg_y + 0.34], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=1)
    arc_lg = patches.Arc((lg_x + 22.5, lg_y + 0.02), 0.64, 0.64, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 23.8, lg_y + 0.06, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (PASTEL BLUE-GREY)
    # ---------------------------------------------------------
    # === TÒA 1 CORRIDORS ===
    # Main horizontal corridor (X: 0.0 to 36.0, Y: -1.0 to 1.0)
    ax.add_patch(patches.Rectangle((0.0, -1.0), 36.0, 2.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Main Entrance Lobby (South: X: 15.0 to 21.0, Y: -4.5 to -1.0)
    ax.add_patch(patches.Rectangle((15.0, -4.5), 6.0, 3.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # North Central Hall / Staircase Lobby (X: 15.0 to 21.0, Y: 1.0 to 4.5)
    ax.add_patch(patches.Rectangle((15.0, 1.0), 6.0, 3.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # West transition hall (X: 12.0 to 15.0, Y: -4.5 to 4.5)
    ax.add_patch(patches.Rectangle((12.0, -4.5), 3.0, 9.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # East transition hall (X: 21.0 to 24.0, Y: -4.5 to 4.5)
    ax.add_patch(patches.Rectangle((21.0, -4.5), 3.0, 9.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === TÒA 2 CORRIDORS & FOYERS ===
    # Connecting neck from Tòa 1 to Tòa 2 (X: 15.0 to 21.0, Y: 4.5 to 6.5)
    ax.add_patch(patches.Rectangle((15.0, 4.5), 6.0, 2.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Courtroom Central Foyer (X: 15.0 to 21.0, Y: 6.5 to 13.5)
    ax.add_patch(patches.Rectangle((15.0, 6.5), 6.0, 7.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 Transversal Distribution Corridor (X: 3.0 to 34.0, Y: 13.5 to 15.0)
    ax.add_patch(patches.Rectangle((3.0, 13.5), 31.0, 1.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 West Office Corridor (X: 12.0 to 14.5, Y: 15.0 to 30.0)
    ax.add_patch(patches.Rectangle((12.0, 15.0), 2.5, 15.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 East Office Corridor (X: 21.5 to 24.0, Y: 15.0 to 30.0)
    ax.add_patch(patches.Rectangle((21.5, 15.0), 2.5, 15.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 East Connecting Branch Corridor between shifted rooms and top rooms (X: 21.5 to 34.0, Y: 24.6 to 26.2)
    ax.add_patch(patches.Rectangle((21.5, 24.6), 12.5, 1.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (ALL 19 ROOMS STRICTLY MATCHING PROMPT)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # ==========================================
        # === TÒA 1: KHỐI CHÍNH PHÍA TRƯỚC (7 PHÒNG) ===
        # ==========================================
        # --- Cánh Tây (West Wing) Tòa 1 ---
        {
            'id': 'T1_P1', 'name': 'Hành chính tư pháp', 'sub': '(KT: 5.5x3 | 1 ng)',
            'x': 0.0, 'y': -4.5, 'w': 6.0, 'h': 3.5,
            'text_center': (3.0, -2.75),
            'font_size': 8.5
        },
        {
            'id': 'T1_P2', 'name': 'Chánh văn - Phòng', 'sub': '(KT: 5.5x3.5 | 2 ng)',
            'x': 6.0, 'y': -4.5, 'w': 6.0, 'h': 3.5,
            'text_center': (9.0, -2.75),
            'font_size': 8.5
        },
        {
            'id': 'T1_P3', 'name': 'Phòng Phó Chánh án', 'sub': '(KT: 7.5x3.5 | 1 ng)',
            'x': 0.0, 'y': 1.0, 'w': 7.5, 'h': 3.5,
            'text_center': (3.75, 2.75),
            'font_size': 8.5
        },
        {
            'id': 'T1_P4', 'name': 'Phòng thư ký', 'sub': '(KT: 4.5x3.5 | 2 ng)',
            'x': 7.5, 'y': 1.0, 'w': 4.5, 'h': 3.5,
            'text_center': (9.75, 2.75),
            'font_size': 8.5
        },

        # --- Cánh Đông (East Wing) Tòa 1 ---
        {
            'id': 'T1_P5', 'name': 'Hoà giải đối thoại', 'sub': '(KT: 5.5x3.5 | 6 ng)',
            'x': 24.0, 'y': 1.0, 'w': 6.0, 'h': 3.5,
            'text_center': (27.0, 2.75),
            'font_size': 8.5
        },
        {
            'id': 'T1_P6', 'name': 'Phòng phó chánh toà dân sự', 'sub': '(KT: 5.5x3.5 | 2 ng)',
            'x': 30.0, 'y': 1.0, 'w': 6.0, 'h': 3.5,
            'text_center': (33.0, 2.75),
            'font_size': 8.0
        },
        {
            'id': 'T1_P7', 'name': 'Phòng Thẩm phán', 'sub': '(KT: 3.5x3 | 1 ng)',
            'x': 24.0, 'y': -4.5, 'w': 5.5, 'h': 3.5,
            'text_center': (26.75, -2.75),
            'font_size': 8.5
        },
        {
            'id': 'T1_WC', 'name': 'Khu vệ sinh', 'sub': '(WC Nam - Nữ)',
            'x': 29.5, 'y': -4.5, 'w': 6.5, 'h': 3.5,
            'text_center': (32.75, -2.75),
            'font_size': 8.0
        },

        # ==========================================
        # === TÒA 2: KHỐI PHÍA SAU (12 PHÒNG) ===
        # ==========================================
        # --- Zone Xét xử A & C (Y: 6.5 to 13.5) ---
        {
            'id': 'T2_XXA', 'name': 'Phòng xét xử A', 'sub': '(KT: 12x7)',
            'x': 3.0, 'y': 6.5, 'w': 12.0, 'h': 7.0,
            'text_center': (9.0, 10.0),
            'font_size': 11.0
        },
        {
            'id': 'T2_XXC', 'name': 'Phòng xét xử C', 'sub': '(KT: 13x6.5)',
            'x': 21.0, 'y': 6.5, 'w': 13.0, 'h': 7.0,
            'text_center': (27.5, 10.0),
            'font_size': 11.0
        },

        # --- Zone Trung tâm: Phòng xét xử B (KT: 7x14) ---
        {
            'id': 'T2_XXB', 'name': 'Phòng xét xử B', 'sub': '(KT: 7x14)',
            'x': 14.5, 'y': 15.0, 'w': 7.0, 'h': 15.0,
            'text_center': (18.0, 22.5),
            'font_size': 11.0
        },

        # --- Zone Cánh Tây Tòa 2: 4 Phòng Làm việc (KT: 4.5x3.5) ---
        {
            'id': 'T2_W1', 'name': 'Phòng Thẩm phán', 'sub': '(KT: 4.5x3.5 | 2 ng)',
            'x': 3.0, 'y': 15.0, 'w': 9.0, 'h': 3.75,
            'text_center': (7.5, 16.87),
            'font_size': 8.5
        },
        {
            'id': 'T2_W2', 'name': 'Phòng Thẩm phán', 'sub': '(KT: 4.5x3.5)',
            'x': 3.0, 'y': 18.75, 'w': 9.0, 'h': 3.75,
            'text_center': (7.5, 20.62),
            'font_size': 8.5
        },
        {
            'id': 'T2_W3', 'name': 'Phòng Thẩm phán', 'sub': '(KT: 4.5x3.5 | 2 ng)',
            'x': 3.0, 'y': 22.5, 'w': 9.0, 'h': 3.75,
            'text_center': (7.5, 24.37),
            'font_size': 8.5
        },
        {
            'id': 'T2_W4', 'name': 'Phòng phó chánh toà HGGĐ', 'sub': '(KT: 4.5x3.5 | 2 ng)',
            'x': 3.0, 'y': 26.25, 'w': 9.0, 'h': 3.75,
            'text_center': (7.5, 28.12),
            'font_size': 8.0
        },

        # --- Zone Cánh Đông Tòa 2: 5 Phòng Làm việc ---
        # 3 phòng dịch xuôi dưới để nhường chỗ cho hành lang nối phía trên
        {
            'id': 'T2_E1', 'name': 'Phòng Thẩm phán', 'sub': '(KT: 6.5x3.5 | 3 ng)',
            'x': 24.0, 'y': 15.0, 'w': 10.0, 'h': 3.2,
            'text_center': (29.0, 16.6),
            'font_size': 8.5
        },
        {
            'id': 'T2_E2', 'name': 'Phòng phó chánh toà dân sự', 'sub': '(KT: 6.5x3.5 | 3 ng)',
            'x': 24.0, 'y': 18.2, 'w': 10.0, 'h': 3.2,
            'text_center': (29.0, 19.8),
            'font_size': 8.0
        },
        {
            'id': 'T2_E3', 'name': 'Phòng Phó chánh án', 'sub': '(KT: 4.5x4.5 | 2 ng)',
            'x': 24.0, 'y': 21.4, 'w': 10.0, 'h': 3.2,
            'text_center': (29.0, 23.0),
            'font_size': 8.5
        },
        # 2 phòng phía trên mở cửa ra hành lang nhánh ngang Y: 24.6 -> 26.2
        {
            'id': 'T2_E4', 'name': 'Phòng Phó chánh án', 'sub': '(KT: 4.4x4.5 | 2 ng)',
            'x': 24.0, 'y': 26.2, 'w': 4.8, 'h': 3.8,
            'text_center': (26.4, 28.1),
            'font_size': 7.5
        },
        {
            'id': 'T2_E5', 'name': 'Phòng Thẩm tra viên', 'sub': '(KT: 5.5x4.5 | 5 ng)',
            'x': 28.8, 'y': 26.2, 'w': 5.2, 'h': 3.8,
            'text_center': (31.4, 28.1),
            'font_size': 7.5
        },
    ]

    # Draw pure white room interior fills
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE (ONLY IN TÒA 1 FOR UPPER FLOORS, TÒA 2 HAS NONE)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 16.5, 1.2, 3.0, 3.1
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 10
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)
    # Up arrow on staircase
    ax.annotate('', xy=(mid_x - 0.7, stair_y + 2.5), xytext=(mid_x - 0.7, stair_y + 0.5),
                arrowprops=dict(arrowstyle="->", color=COLOR_WALL, lw=1.2), zorder=6)
    ax.text(mid_x - 0.7, stair_y + 0.3, 'LÊN', color=COLOR_TEXT_MUTED, fontsize=7.5, ha='center', va='top', zorder=6)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.25, 'Cầu thang bộ (Lên tầng 2)', 
            color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', ha='center', va='top', zorder=5)

    # ---------------------------------------------------------
    # 6. EXTERIOR STEPS & RAMPS
    # ---------------------------------------------------------
    # Main Front Entrance Steps (South: Y = -4.5 to -5.5)
    for sy in [-4.5, -4.7, -4.9, -5.1, -5.3, -5.5]:
        ax.plot([15.0, 21.0], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([15.0, 15.0], [-4.5, -5.5], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([21.0, 21.0], [-4.5, -5.5], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # Side Steps at West & East corridor ends of Tòa 1
    for i in range(5):
        dx = -0.25 * (i + 1)
        dy = 1.0 + i * 0.08
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    for i in range(5):
        dx = 36.0 + 0.25 * (i + 1)
        dy = 1.0 + i * 0.08
        ax.plot([36.0, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([36.0, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # ---------------------------------------------------------
    # 7. CORRIDOR & FOYER LABELS
    # ---------------------------------------------------------
    ax.text(18.0, -2.75, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(6.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(30.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(18.0, 5.5, 'SẢNH NỐI', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(18.0, 8.5, 'SẢNH PHÒNG XÉT XỬ', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(18.0, 14.25, 'HÀNH LANG PHÂN PHỐI', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(13.25, 22.5, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', rotation=90, ha='center', va='center', zorder=5)
    ax.text(22.75, 20.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', rotation=90, ha='center', va='center', zorder=5)
    ax.text(29.0, 25.4, 'HÀNH LANG NỐI', color=COLOR_TEXT_MAIN, fontsize=8.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 8. DRAW SOLID STRUCTURAL WALLS WITH EXACT CUTOUTS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # === TÒA 1 PERIMETER WALLS ===
    # West outer wall (X = -W)
    draw_wall(-W, -4.5 - W, W, 3.5 + W)
    draw_wall(-W, 1.0, W, 3.5 + W)

    # East outer wall (X = 36.0)
    draw_wall(36.0, -4.5 - W, W, 3.5 + W)
    draw_wall(36.0, 1.0, W, 3.5 + W)

    # North exterior wall of Tòa 1 (with opening at X: 15.0 to 21.0 for passage)
    draw_wall(-W, 4.5, 15.0 + W, W)
    draw_wall(21.0, 4.5, 15.0 + W, W)

    # South exterior wall of Tòa 1 (with OPEN entrance at X: 15.0 to 21.0, NO DOORS)
    draw_wall(-W, -4.5 - W, 15.0 + W, W)
    draw_wall(21.0, -4.5 - W, 15.0 + W, W)

    # Side cheeks for main entrance steps
    draw_wall(15.0 - P/2, -5.5, P, 1.0)
    draw_wall(21.0 - P/2, -5.5, P, 1.0)

    # === TÒA 1 INTERNAL PARTITIONS & CORRIDOR WALLS ===
    # Corridor Wall Y = 1.0 (North corridor line) with door cutouts:
    # Gap 1: 5.6 to 6.5 (Room P3 door)
    # Gap 2: 8.5 to 9.4 (Room P4 door)
    # Open: 12.0 to 24.0 (Stair & connector hall)
    # Gap 3: 25.0 to 25.9 (Room P5 door)
    # Gap 4: 31.0 to 31.9 (Room P6 door)
    draw_wall(0, 1.0 - P/2, 5.6, P)
    draw_wall(6.5, 1.0 - P/2, 2.0, P)
    draw_wall(9.4, 1.0 - P/2, 2.6, P)

    draw_wall(24.0, 1.0 - P/2, 1.0, P)
    draw_wall(25.9, 1.0 - P/2, 5.1, P)
    draw_wall(31.9, 1.0 - P/2, 4.1, P)

    # Corridor Wall Y = -1.0 (South corridor line) with door cutouts:
    # Gap 1: 4.8 to 5.7 (Room P1 door)
    # Gap 2: 7.2 to 8.1 (Room P2 door)
    # Open: 12.0 to 24.0 (Main entrance lobby)
    # Gap 3: 25.0 to 25.9 (Room P7 door)
    # Gap 4: 30.5 to 31.4 (Room WC door)
    draw_wall(0, -1.0 - P/2, 4.8, P)
    draw_wall(5.7, -1.0 - P/2, 1.5, P)
    draw_wall(8.1, -1.0 - P/2, 3.9, P)

    draw_wall(24.0, -1.0 - P/2, 1.0, P)
    draw_wall(25.9, -1.0 - P/2, 4.6, P)
    draw_wall(31.4, -1.0 - P/2, 4.6, P)

    # Vertical internal partitions in Tòa 1
    # West wing vertical partitions
    draw_wall(6.0 - P/2, -4.5, P, 3.5)
    draw_wall(12.0 - P/2, -4.5, P, 3.5)
    draw_wall(7.5 - P/2, 1.0, P, 3.5)
    draw_wall(12.0 - P/2, 1.0, P, 3.5)

    # East wing vertical partitions
    draw_wall(24.0 - P/2, -4.5, P, 3.5)
    draw_wall(29.5 - P/2, -4.5, P, 3.5)
    draw_wall(24.0 - P/2, 1.0, P, 3.5)
    draw_wall(30.0 - P/2, 1.0, P, 3.5)

    # === TÒA 2 WALLS (COURTROOMS & OFFICES) ===
    # Connecting neck side walls (X: 15.0 & 21.0, Y: 4.5 to 6.5)
    draw_wall(15.0 - P/2, 4.5, P, 2.0)
    draw_wall(21.0 - P/2, 4.5, P, 2.0)

    # Zone 1 (Courtrooms A & C): Exterior Walls
    # West outer wall of Courtroom A (X: 3.0m - W)
    draw_wall(3.0 - W, 6.5 - W, W, 7.0 + W)
    # South outer wall of Courtroom A (Y = 6.5 - W)
    draw_wall(3.0 - W, 6.5 - W, 12.0 + W, W)

    # East outer wall of Courtroom C (X = 34.0)
    draw_wall(34.0, 6.5 - W, W, 7.0 + W)
    # South outer wall of Courtroom C (Y = 6.5 - W)
    draw_wall(21.0, 6.5 - W, 13.0 + W, W)

    # Courtroom Foyer side walls (along X = 15.0 & X = 21.0) with double door cutouts:
    # Gap at Y: 9.0 to 11.0 (Height 2.0m for double doors)
    # West wall (X = 15.0)
    draw_wall(15.0 - P/2, 6.5, P, 2.5)
    draw_wall(15.0 - P/2, 11.0, P, 2.5)

    # East wall (X = 21.0)
    draw_wall(21.0 - P/2, 6.5, P, 2.5)
    draw_wall(21.0 - P/2, 11.0, P, 2.5)

    # Transversal Corridor Wall at Y = 13.5 (North of Courtrooms A & C)
    draw_wall(3.0, 13.5 - P/2, 12.0, P)
    draw_wall(21.0, 13.5 - P/2, 13.0, P)

    # Transversal Corridor Wall at Y = 15.0 (South of Courtroom B & Office blocks)
    # West office entry: solid wall at 3.0 to 12.0
    draw_wall(3.0, 15.0 - P/2, 9.0, P)
    # Courtroom B entrance double door cutouts at 17.1 to 18.9
    draw_wall(14.5, 15.0 - P/2, 2.6, P)
    draw_wall(18.9, 15.0 - P/2, 2.6, P)
    # East office entry: solid wall at 24.0 to 34.0
    draw_wall(24.0, 15.0 - P/2, 10.0, P)

    # === ZONE 2: EXTERIOR WALLS (Y: 15.0 to 30.0) ===
    # West outer wall (X = 3.0 - W, Y: 13.5 to 30.0 + W)
    draw_wall(3.0 - W, 13.5, W, 16.5 + W)
    # East outer wall (X = 34.0, Y: 13.5 to 30.0 + W)
    draw_wall(34.0, 13.5, W, 16.5 + W)

    # North Top Exterior Wall (Y = 30.0m) across entire rear width
    draw_wall(3.0 - W, 30.0, 31.0 + 2*W, W)

    # Internal Vertical Partition separating Courtroom B from West Corridor (X = 14.5)
    draw_wall(14.5 - P/2, 15.0, P, 15.0)
    # Internal Vertical Partition separating Courtroom B from East Corridor (X = 21.5)
    draw_wall(21.5 - P/2, 15.0, P, 15.0)

    # West Office Corridor Wall (X = 12.0) with door cutouts:
    # Door gaps:
    # Room W1: 15.6 to 16.5
    # Room W2: 19.3 to 20.2
    # Room W3: 23.1 to 24.0
    # Room W4: 26.8 to 27.7
    draw_wall(12.0 - P/2, 15.0, P, 0.6)
    draw_wall(12.0 - P/2, 16.5, P, 2.8)
    draw_wall(12.0 - P/2, 20.2, P, 2.9)
    draw_wall(12.0 - P/2, 24.0, P, 2.8)
    draw_wall(12.0 - P/2, 27.7, P, 2.3)

    # West Office Horizontal Partitions (Y = 18.75, 22.5, 26.25)
    draw_wall(3.0, 18.75 - P/2, 9.0, P)
    draw_wall(3.0, 22.5 - P/2, 9.0, P)
    draw_wall(3.0, 26.25 - P/2, 9.0, P)

    # === EAST OFFICE WING WALLS (WITH CONNECTING CORRIDOR BRANCH) ===
    # East Office Corridor Wall (X = 24.0, from Y = 15.0 to 24.6):
    # Door gaps:
    # Room E1: 15.6 to 16.5
    # Room E2: 18.8 to 19.7
    # Room E3: 22.0 to 22.9
    draw_wall(24.0 - P/2, 15.0, P, 0.6)
    draw_wall(24.0 - P/2, 16.5, P, 2.3)
    draw_wall(24.0 - P/2, 19.7, P, 2.3)
    draw_wall(24.0 - P/2, 22.9, P, 1.7)
    # Note: X = 24.0 from Y = 24.6 to 26.2 is OPEN (corridor connection branch!)

    # Horizontal Partitions for shifted Rooms E1, E2, E3
    draw_wall(24.0, 18.2 - P/2, 10.0, P)
    draw_wall(24.0, 21.4 - P/2, 10.0, P)
    # Solid horizontal wall at Y = 24.6 separating Room E3 from connecting branch corridor
    draw_wall(24.0, 24.6 - P/2, 10.0, P)

    # Horizontal Wall at Y = 26.2 (North boundary of branch corridor) with door cutouts:
    # Gap 1: 24.8 to 25.7 (Room E4 door)
    # Gap 2: 29.8 to 30.7 (Room E5 door)
    draw_wall(24.0, 26.2 - P/2, 0.8, P)
    draw_wall(25.7, 26.2 - P/2, 4.1, P)
    draw_wall(30.7, 26.2 - P/2, 3.3, P)

    # Vertical Partition between Room E4 and Room E5 (X = 28.8, from Y = 26.2 to 30.0)
    draw_wall(28.8 - P/2, 26.2, P, 3.8)

    # West wall of Room E4 (Phòng Phó chánh án) (X = 24.0, from Y = 26.2 to 30.0)
    draw_wall(24.0 - P/2, 26.2 - P/2, P, 3.8 + P/2)

    # ---------------------------------------------------------
    # 9. DRAW WINDOWS (SNAPPED ON EXTERIOR WALLS WITH WHITE MASK)
    # ---------------------------------------------------------
    def draw_window(x, y, w, h, is_horizontal=True):
        if is_horizontal:
            ax.add_patch(patches.Rectangle((x, y - 0.02), w, h + 0.04, facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x, x + w], [y + 0.04, y + 0.04], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x, x + w], [y + h - 0.04, y + h - 0.04], color=COLOR_WALL, linewidth=1.2, zorder=12)
        else:
            ax.add_patch(patches.Rectangle((x - 0.02, y), w + 0.04, h, facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x + 0.04, x + 0.04], [y, y + h], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x + w - 0.04, x + w - 0.04], [y, y + h], color=COLOR_WALL, linewidth=1.2, zorder=12)

    # --- Tòa 1 Windows ---
    # South Exterior Wall Windows (Y = -4.5 - W)
    draw_window(1.5, -4.5 - W, 2.5, W, is_horizontal=True)    # T1_P1
    draw_window(7.5, -4.5 - W, 2.5, W, is_horizontal=True)    # T1_P2
    draw_window(25.5, -4.5 - W, 2.2, W, is_horizontal=True)   # T1_P7
    draw_window(31.5, -4.5 - W, 2.5, W, is_horizontal=True)   # T1_WC

    # North Exterior Wall Windows (Y = 4.5)
    draw_window(2.0, 4.5, 3.5, W, is_horizontal=True)         # T1_P3
    draw_window(8.5, 4.5, 2.5, W, is_horizontal=True)         # T1_P4
    draw_window(25.5, 4.5, 3.0, W, is_horizontal=True)        # T1_P5
    draw_window(31.5, 4.5, 3.0, W, is_horizontal=True)        # T1_P6

    # West & East Ends Windows of Tòa 1
    draw_window(-W, -3.5, W, 1.8, is_horizontal=False)
    draw_window(-W, 2.0, W, 1.8, is_horizontal=False)
    draw_window(36.0, -3.5, W, 1.8, is_horizontal=False)
    draw_window(36.0, 2.0, W, 1.8, is_horizontal=False)

    # --- Tòa 2 Windows ---
    # Courtroom A Windows (West wall X = 3.0 - W, South wall Y = 6.5 - W)
    draw_window(3.0 - W, 8.0, W, 3.0, is_horizontal=False)
    draw_window(5.5, 6.5 - W, 4.5, W, is_horizontal=True)

    # Courtroom C Windows (East wall X = 34.0, South wall Y = 6.5 - W)
    draw_window(34.0, 8.0, W, 3.0, is_horizontal=False)
    draw_window(24.5, 6.5 - W, 4.5, W, is_horizontal=True)

    # West Office Wing Windows (West wall X = 3.0 - W, Y: 15.0 to 30.0)
    draw_window(3.0 - W, 16.0, W, 1.8, is_horizontal=False)   # T2_W1
    draw_window(3.0 - W, 19.8, W, 1.8, is_horizontal=False)   # T2_W2
    draw_window(3.0 - W, 23.5, W, 1.8, is_horizontal=False)   # T2_W3
    draw_window(3.0 - W, 27.2, W, 1.8, is_horizontal=False)   # T2_W4

    # East Office Wing Windows (East wall X = 34.0, Y: 15.0 to 30.0)
    draw_window(34.0, 15.8, W, 1.6, is_horizontal=False)      # T2_E1
    draw_window(34.0, 19.0, W, 1.6, is_horizontal=False)      # T2_E2
    draw_window(34.0, 22.2, W, 1.6, is_horizontal=False)      # T2_E3
    draw_window(34.0, 27.2, W, 1.8, is_horizontal=False)      # T2_E5

    # North Rear Wall Windows (Y = 30.0m)
    draw_window(6.0, 30.0, 3.0, W, is_horizontal=True)        # T2_W4 North
    draw_window(16.0, 30.0, 4.0, W, is_horizontal=True)       # Courtroom B North
    draw_window(25.5, 30.0, 2.0, W, is_horizontal=True)       # T2_E4 North
    draw_window(30.0, 30.0, 2.2, W, is_horizontal=True)       # T2_E5 North

    # ---------------------------------------------------------
    # 10. DRAW DOORS & DOOR SWINGS (MATHEMATICALLY SNAPPED TO CUTOUTS)
    # ---------------------------------------------------------
    def draw_door_h(x1, x2, y, into='north', hinge='left'):
        """Door on horizontal wall at y, gap from x1 to x2 (x1 < x2)."""
        size = x2 - x1
        if into == 'north':
            if hinge == 'left':
                ax.plot([x1, x1], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x1, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
            else: # hinge == 'right'
                ax.plot([x2, x2], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x2, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
        elif into == 'south':
            if hinge == 'left':
                ax.plot([x1, x1], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x1, y), size*2, size*2, angle=0, theta1=270, theta2=360,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
            else: # hinge == 'right'
                ax.plot([x2, x2], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x2, y), size*2, size*2, angle=0, theta1=180, theta2=270,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)

    def draw_door_v(x, y1, y2, into='west', hinge='bottom'):
        """Door on vertical wall at x, gap from y1 to y2 (y1 < y2)."""
        size = y2 - y1
        if into == 'west':
            if hinge == 'bottom':
                ax.plot([x, x - size], [y1, y1], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x, y1), size*2, size*2, angle=0, theta1=90, theta2=180,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
            else: # hinge == 'top'
                ax.plot([x, x - size], [y2, y2], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x, y2), size*2, size*2, angle=0, theta1=180, theta2=270,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
        elif into == 'east':
            if hinge == 'bottom':
                ax.plot([x, x + size], [y1, y1], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x, y1), size*2, size*2, angle=0, theta1=0, theta2=90,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
            else: # hinge == 'top'
                ax.plot([x, x + size], [y2, y2], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x, y2), size*2, size*2, angle=0, theta1=270, theta2=360,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)

    # --- TÒA 1 DOORS ---
    # North Corridor Wall Y = 1.0 (Swings into North rooms)
    draw_door_h(5.6, 6.5, 1.0, into='north', hinge='left')    # Room P3
    draw_door_h(8.5, 9.4, 1.0, into='north', hinge='right')   # Room P4
    draw_door_h(25.0, 25.9, 1.0, into='north', hinge='left')  # Room P5
    draw_door_h(31.0, 31.9, 1.0, into='north', hinge='left')  # Room P6

    # South Corridor Wall Y = -1.0 (Swings into South rooms)
    draw_door_h(4.8, 5.7, -1.0, into='south', hinge='left')   # Room P1
    draw_door_h(7.2, 8.1, -1.0, into='south', hinge='right')  # Room P2
    draw_door_h(25.0, 25.9, -1.0, into='south', hinge='left') # Room P7
    draw_door_h(30.5, 31.4, -1.0, into='south', hinge='left') # Room WC

    # --- TÒA 2 COURTROOM DOORS ---
    # Courtroom A Double Doors (X = 15.0, gap Y: 9.0 to 11.0, swings West into Courtroom A)
    draw_door_v(15.0, 9.0, 10.0, into='west', hinge='bottom')
    draw_door_v(15.0, 10.0, 11.0, into='west', hinge='top')

    # Courtroom C Double Doors (X = 21.0, gap Y: 9.0 to 11.0, swings East into Courtroom C)
    draw_door_v(21.0, 9.0, 10.0, into='east', hinge='bottom')
    draw_door_v(21.0, 10.0, 11.0, into='east', hinge='top')

    # Courtroom B Double Doors (Y = 15.0, gap X: 17.1 to 18.9, swings North into Courtroom B)
    draw_door_h(17.1, 18.0, 15.0, into='north', hinge='left')
    draw_door_h(18.0, 18.9, 15.0, into='north', hinge='right')

    # --- TÒA 2 WEST OFFICE DOORS (X = 12.0, swings West into offices) ---
    draw_door_v(12.0, 15.6, 16.5, into='west', hinge='bottom') # Room W1
    draw_door_v(12.0, 19.3, 20.2, into='west', hinge='bottom') # Room W2
    draw_door_v(12.0, 23.1, 24.0, into='west', hinge='bottom') # Room W3
    draw_door_v(12.0, 26.8, 27.7, into='west', hinge='bottom') # Room W4

    # --- TÒA 2 EAST OFFICE DOORS ---
    # Shifted Rooms on Wall X = 24.0 (Swings East into offices)
    draw_door_v(24.0, 15.6, 16.5, into='east', hinge='bottom') # Room E1
    draw_door_v(24.0, 18.8, 19.7, into='east', hinge='bottom') # Room E2
    draw_door_v(24.0, 22.0, 22.9, into='east', hinge='bottom') # Room E3

    # Top Rooms on Connecting Branch Wall Y = 26.2 (Swings North into offices)
    draw_door_h(24.8, 25.7, 26.2, into='north', hinge='left')  # Room E4 (Phó chánh án)
    draw_door_h(29.8, 30.7, 26.2, into='north', hinge='left')  # Room E5 (Thẩm tra viên)

    # ---------------------------------------------------------
    # 11. ROOM LABELS & METADATA
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 8.5)
        # Main room name (bold)
        ax.text(cx, cy + 0.22, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)
        # Secondary info (size / capacity)
        if r['sub']:
            ax.text(cx, cy - 0.28, r['sub'], color=COLOR_TEXT_MUTED, fontsize=font_sz * 0.85, ha='center', va='center', zorder=15)

    # ---------------------------------------------------------
    # 12. AXIS LIMITS & EXPORT
    # ---------------------------------------------------------
    ax.set_xlim(-3.0, 39.0)
    ax.set_ylim(-9.5, 32.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {out_img_path}")

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau3\Tang1"
    create_floorplan_tang1(target_dir)
