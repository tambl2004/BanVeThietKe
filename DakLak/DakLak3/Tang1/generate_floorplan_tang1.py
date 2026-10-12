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
    font_size: float

def create_floorplan_tang1(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_1.png')

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 18), dpi=300)
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

    WALL_THICKNESS = 0.22           # Exterior wall identifier
    PART_THICKNESS = 0.12           # Interior wall identifier
    W = WALL_THICKNESS

    # Geometry bounds
    X_MIN = 0.0
    X_MAX = 32.0

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Single-line title, font 20 bold, NO subtitle line
    fig.text(0.04, 0.965, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 3 - Đắk Lắk', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.04, 0.96], [0.948, 0.948], transform=fig.transFigure, color='#e2e8f0', linewidth=1.2)
    fig.lines.append(header_line)

    # Legend Box at Bottom Center
    lg_x, lg_y = 5.0, -8.0
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.38, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.06, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall (Exterior heavy wall)
    ax.add_patch(patches.Rectangle((lg_x + 7.5, lg_y + 0.09), 1.2, 0.20, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 9.0, lg_y + 0.06, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window (Two parallel lines, white background)
    ax.add_patch(patches.Rectangle((lg_x + 14.5, lg_y + 0.06), 1.2, 0.26, facecolor='#ffffff', edgecolor='none', zorder=1))
    ax.plot([lg_x + 14.5, lg_x + 15.7], [lg_y + 0.28, lg_y + 0.28], color=COLOR_WALL, linewidth=1.2, zorder=2)
    ax.plot([lg_x + 14.5, lg_x + 15.7], [lg_y + 0.10, lg_y + 0.10], color=COLOR_WALL, linewidth=1.2, zorder=2)
    ax.text(lg_x + 16.0, lg_y + 0.06, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 21.0, lg_x + 21.0], [lg_y + 0.02, lg_y + 0.34], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=1)
    arc_lg = patches.Arc((lg_x + 21.0, lg_y + 0.02), 0.64, 0.64, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 22.3, lg_y + 0.06, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # === TÒA A (KHỐI VĂN PHÒNG PHÍA NAM) ===
    # Horizontal central corridor (X: 0.0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((X_MIN, -0.9), X_MAX - X_MIN, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # South Main Lobby (X: 13.5 to 18.5, Y: -4.5 to -0.9)
    ax.add_patch(patches.Rectangle((13.5, -4.5), 5.0, 3.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # North Rear Lobby & Stair Hall (X: 13.5 to 18.5, Y: 0.9 to 4.5)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 3.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Corridor labels for Tòa A
    bbox_corr = dict(boxstyle='round,pad=0.2', facecolor=COLOR_FILL_CORRIDOR, edgecolor='none')
    ax.text(6.75, 0.0, 'HÀNH LANG', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6, bbox=bbox_corr)
    ax.text(25.25, 0.0, 'HÀNH LANG', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6, bbox=bbox_corr)
    ax.text(16.0, -2.7, 'SẢNH CHÍNH', fontsize=11, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6)

    # South Main Entrance Steps (Y: -4.5 down to -5.7)
    for i in range(5):
        dy = -4.5 - 0.24 * (i + 1)
        dx_min = 13.5 - i * 0.12
        dx_max = 18.5 + i * 0.12
        ax.plot([dx_min, dx_max], [dy, dy], color=COLOR_WALL, linewidth=1.0, zorder=3)
        ax.plot([dx_min, dx_min], [-4.5, dy], color=COLOR_WALL, linewidth=1.0, zorder=3)
        ax.plot([dx_max, dx_max], [-4.5, dy], color=COLOR_WALL, linewidth=1.0, zorder=3)

    # North Rear Exit Steps Tòa A (Y: 4.5 to 6.2)
    for i in range(5):
        dy = 4.5 + 0.28 * (i + 1)
        ax.plot([14.0, 18.0], [dy, dy], color=COLOR_WALL, linewidth=1.0, zorder=3)

    # Lateral corridor exit steps (East & West of Tòa A)
    for i in range(4):
        sx = X_MIN - (i + 1) * 0.18
        ax.plot([sx, sx], [-0.9, 0.9], color=COLOR_WALL, linewidth=1.0, zorder=3)
    for i in range(4):
        sx = X_MAX + (i + 1) * 0.18
        ax.plot([sx, sx], [-0.9, 0.9], color=COLOR_WALL, linewidth=1.0, zorder=3)

    # === TÒA B (KHỐI HỘI TRƯỜNG XÉT XỬ PHÍA BẮC) ===
    # Horizontal distribution corridor of Tòa B (X: 0.0 to 32.0, Y: 10.0 to 11.8)
    ax.add_patch(patches.Rectangle((X_MIN, 10.0), X_MAX - X_MIN, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Corridor labels for Tòa B
    ax.text(11.5, 10.9, 'HÀNH LANG PHÂN PHỐI', fontsize=9.5, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6, bbox=bbox_corr)
    ax.text(27.5, 10.9, 'HÀNH LANG', fontsize=9.5, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6, bbox=bbox_corr)

    # Entrance steps to Tòa B corridor from Courtyard (Y: 9.0 to 10.0)
    for i in range(4):
        dy = 10.0 - 0.22 * (i + 1)
        ax.plot([13.5 - i * 0.1, 18.5 + i * 0.1], [dy, dy], color=COLOR_WALL, linewidth=1.0, zorder=3)
        ax.plot([13.5 - i * 0.1, 13.5 - i * 0.1], [10.0, dy], color=COLOR_WALL, linewidth=1.0, zorder=3)
        ax.plot([18.5 + i * 0.1, 18.5 + i * 0.1], [10.0, dy], color=COLOR_WALL, linewidth=1.0, zorder=3)

    # Lateral exit steps for Tòa B (East & West)
    for i in range(4):
        sx = X_MIN - (i + 1) * 0.18
        ax.plot([sx, sx], [10.0, 11.8], color=COLOR_WALL, linewidth=1.0, zorder=3)
    for i in range(4):
        sx = X_MAX + (i + 1) * 0.18
        ax.plot([sx, sx], [10.0, 11.8], color=COLOR_WALL, linewidth=1.0, zorder=3)

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (13 PHÒNG TÒA A + 2 PHÒNG TÒA B)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA A: 13 PHÒNG TẦNG 1 ===
        # --- Dãy phía Bắc Tòa A (Y: 0.9 to 4.5, h = 3.6) ---
        {
            'id': 'T1_101', 'name': 'Phòng Kế toán 101',
            'x': 0.0, 'y': 0.9, 'w': 4.5, 'h': 3.6,
            'text_center': (2.25, 2.7), 'font_size': 9.0
        },
        {
            'id': 'T1_103', 'name': 'Phòng Thẩm phán 103',
            'x': 4.5, 'y': 0.9, 'w': 3.0, 'h': 3.6,
            'text_center': (6.0, 2.7), 'font_size': 8.5
        },
        {
            'id': 'T1_105', 'name': 'Phòng CNTT 105',
            'x': 7.5, 'y': 0.9, 'w': 3.0, 'h': 3.6,
            'text_center': (9.0, 2.7), 'font_size': 8.5
        },
        {
            'id': 'T1_107', 'name': 'Phòng Văn thư 107',
            'x': 10.5, 'y': 0.9, 'w': 3.0, 'h': 3.6,
            'text_center': (12.0, 2.7), 'font_size': 8.5
        },
        # [Cầu thang bộ Tòa A gọn gàng ở giữa: X: 14.6 to 17.4, Y: 1.3 to 4.0]
        {
            'id': 'T1_109', 'name': 'Phòng Tiếp dân 109',
            'x': 18.5, 'y': 0.9, 'w': 3.0, 'h': 3.6,
            'text_center': (20.0, 2.7), 'font_size': 8.5
        },
        {
            'id': 'T1_111', 'name': 'Phòng Thẩm phán 111',
            'x': 21.5, 'y': 0.9, 'w': 3.0, 'h': 3.6,
            'text_center': (23.0, 2.7), 'font_size': 8.5
        },
        {
            'id': 'T1_113', 'name': 'Phòng Thẩm phán 113',
            'x': 24.5, 'y': 0.9, 'w': 3.0, 'h': 3.6,
            'text_center': (26.0, 2.7), 'font_size': 8.5
        },
        {
            'id': 'T1_115', 'name': 'Phòng Thẩm phán 115',
            'x': 27.5, 'y': 0.9, 'w': 4.5, 'h': 3.6,
            'text_center': (29.75, 2.7), 'font_size': 9.0
        },

        # --- Dãy phía Nam Tòa A (Y: -4.5 to -0.9, h = 3.6) ---
        {
            'id': 'T1_102', 'name': 'Phòng Kho 102',
            'x': 0.0, 'y': -4.5, 'w': 4.5, 'h': 3.6,
            'text_center': (2.25, -2.7), 'font_size': 9.0
        },
        {
            'id': 'T1_104', 'name': 'Phòng Thẩm phán 104',
            'x': 4.5, 'y': -4.5, 'w': 4.5, 'h': 3.6,
            'text_center': (6.75, -2.7), 'font_size': 9.0
        },
        {
            'id': 'T1_106', 'name': 'Phòng Phó Chánh VP 106',
            'x': 9.0, 'y': -4.5, 'w': 4.5, 'h': 3.6,
            'text_center': (11.25, -2.7), 'font_size': 8.5
        },
        # [Sảnh chính Tòa A: X: 13.5 to 18.5, Y: -4.5 to -0.9]
        {
            'id': 'T1_108', 'name': 'Phòng Phó chánh án 108',
            'x': 18.5, 'y': -4.5, 'w': 6.75, 'h': 3.6,
            'text_center': (21.875, -2.7), 'font_size': 9.5
        },
        {
            'id': 'T1_110', 'name': 'Phòng Thẩm phán 110',
            'x': 25.25, 'y': -4.5, 'w': 6.75, 'h': 3.6,
            'text_center': (28.625, -2.7), 'font_size': 9.5
        },

        # === TÒA B: 02 PHÒNG HỘI TRƯỜNG XÉT XỬ ===
        {
            'id': 'T1_HT_A', 'name': 'PHÒNG HỘI TRƯỜNG XÉT XỬ A',
            'x': 0.0, 'y': 11.8, 'w': 23.0, 'h': 7.2,
            'text_center': (11.5, 15.4), 'font_size': 13.0
        },
        {
            'id': 'T1_HT_B', 'name': 'PHÒNG HỘI TRƯỜNG\nXÉT XỬ B',
            'x': 23.0, 'y': 11.8, 'w': 9.0, 'h': 7.2,
            'text_center': (27.5, 15.4), 'font_size': 11.0
        },
    ]

    # Draw room fills and room labels
    for r in rooms:
        ax.add_patch(patches.Rectangle((r['x'], r['y']), r['w'], r['h'], 
                                       facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))
        ax.text(r['text_center'][0], r['text_center'][1], r['name'], 
                fontsize=r['font_size'], fontweight='bold', color=COLOR_TEXT_MAIN, 
                ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 5. COMPACT STAIRCASE TÒA A (NHỎ GỌN NHƯ MẪU HẢI PHÒNG)
    # ---------------------------------------------------------
    # Staircase dimensions: 2.8m wide x 2.7m high, centered in North hall (X: 13.5 to 18.5)
    stair_w, stair_h = 2.8, 2.7
    stair_x = 16.0 - stair_w / 2.0  # 14.6m
    stair_y = 1.3                   # leaves sides & back completely open
    
    # Staircase background matches lobby tone (#eef4f7)
    ax.add_patch(patches.Rectangle((stair_x, stair_y), stair_w, stair_h, 
                                   facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3))
    
    # Central divider spine running vertically down the middle
    mid_x = 16.0
    ax.plot([mid_x, mid_x], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Landing step (Full width at top of flight)
    ax.plot([stair_x, stair_x + stair_w], [stair_y + stair_h - 0.35, stair_y + stair_h - 0.35], 
            color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Horizontal step treads (8 steps per flight)
    num_treads = 8
    flight_h = stair_h - 0.35
    for i in range(num_treads):
        ty = stair_y + i * (flight_h / num_treads)
        ax.plot([stair_x, mid_x - 0.04], [ty, ty], color=COLOR_WALL, linewidth=0.75, zorder=4)
        ax.plot([mid_x + 0.04, stair_x + stair_w], [ty, ty], color=COLOR_WALL, linewidth=0.75, zorder=4)

    # Staircase label underneath box
    ax.text(mid_x, stair_y - 0.22, "Cầu thang", fontsize=8.5, color=COLOR_TEXT_MAIN, ha='center', va='top', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS & OPENINGS HELPER FUNCTIONS
    # ---------------------------------------------------------
    # Tường ngoài đậm hơn tường trong: LINEWIDTH_EXTERIOR = 4.0, LINEWIDTH_INTERIOR = 1.4
    def draw_wall_segment(p1: Tuple[float, float], p2: Tuple[float, float], 
                          cutouts: Optional[List[Tuple[float, float]]] = None, thickness: float = 0.12):
        cutouts = cutouts or []
        x1, y1 = p1
        x2, y2 = p2
        # Determine linewidth: exterior heavy wall vs interior lighter partition
        lw = 4.0 if thickness >= 0.20 else 1.4

        if abs(x1 - x2) < 0.001:  # Vertical wall
            y_min, y_max = min(y1, y2), max(y1, y2)
            # CRITICAL FIX: Strictly clamp cutouts inside [y_min, y_max]
            valid_cutouts = []
            for c1, c2 in cutouts:
                ca = max(y_min, min(c1, c2))
                cb = min(y_max, max(c1, c2))
                if cb > ca + 0.01:
                    valid_cutouts.append((ca, cb))
            valid_cutouts.sort(key=lambda c: c[0])

            current_y = y_min
            for cy_start, cy_end in valid_cutouts:
                if cy_start > current_y + 0.01:
                    ax.plot([x1, x1], [current_y, cy_start], color=COLOR_WALL, linewidth=lw, zorder=4, solid_capstyle='butt')
                current_y = max(current_y, cy_end)
            if current_y < y_max - 0.01:
                ax.plot([x1, x1], [current_y, y_max], color=COLOR_WALL, linewidth=lw, zorder=4, solid_capstyle='butt')
        else:  # Horizontal wall
            x_min, x_max = min(x1, x2), max(x1, x2)
            # CRITICAL FIX: Strictly clamp cutouts inside [x_min, x_max]
            valid_cutouts = []
            for c1, c2 in cutouts:
                ca = max(x_min, min(c1, c2))
                cb = min(x_max, max(c1, c2))
                if cb > ca + 0.01:
                    valid_cutouts.append((ca, cb))
            valid_cutouts.sort(key=lambda c: c[0])

            current_x = x_min
            for cx_start, cx_end in valid_cutouts:
                if cx_start > current_x + 0.01:
                    ax.plot([current_x, cx_start], [y1, y1], color=COLOR_WALL, linewidth=lw, zorder=4, solid_capstyle='butt')
                current_x = max(current_x, cx_end)
            if current_x < x_max - 0.01:
                ax.plot([current_x, x_max], [y1, y1], color=COLOR_WALL, linewidth=lw, zorder=4, solid_capstyle='butt')

    # CỬA SỔ CHUẨN ĐỒ HỌA: NỀN TRẮNG CHE VÁCH + 2 ĐƯỜNG KẺ SONG SONG MẢNH
    def draw_window(x: float, y: float, w: float, orientation: str):
        if orientation == 'H':
            ax.add_patch(patches.Rectangle((x - w/2, y - 0.16), w, 0.32, 
                                           facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x - w/2, x + w/2], [y + 0.09, y + 0.09], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x - w/2, x + w/2], [y - 0.09, y - 0.09], color=COLOR_WALL, linewidth=1.2, zorder=12)
        else:
            ax.add_patch(patches.Rectangle((x - 0.16, y - w/2), 0.32, w, 
                                           facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x + 0.09, x + 0.09], [y - w/2, y + w/2], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x - 0.09, x - 0.09], [y - w/2, y + w/2], color=COLOR_WALL, linewidth=1.2, zorder=12)

    def draw_door(x: float, y: float, width: float, direction: str):
        door_x = x - width / 2.0
        if direction == 'IN_NORTH':
            ax.add_patch(patches.Rectangle((x - width/2, y - 0.12), width, 0.24, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=6))
            ax.plot([door_x, door_x], [y, y + width], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=7)
            arc = patches.Arc((door_x, y), width*2, width*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.2, linestyle='--', zorder=7)
            ax.add_patch(arc)
        elif direction == 'IN_SOUTH':
            ax.add_patch(patches.Rectangle((x - width/2, y - 0.12), width, 0.24, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=6))
            ax.plot([door_x, door_x], [y, y - width], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=7)
            arc = patches.Arc((door_x, y), width*2, width*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.2, linestyle='--', zorder=7)
            ax.add_patch(arc)
        elif direction == 'DOUBLE_IN_NORTH':
            half_w = width / 2.0
            ax.add_patch(patches.Rectangle((x - half_w, y - 0.12), width, 0.24, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=6))
            ax.plot([x - half_w, x - half_w], [y, y + half_w], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=7)
            arc_l = patches.Arc((x - half_w, y), half_w*2, half_w*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.2, linestyle='--', zorder=7)
            ax.add_patch(arc_l)
            ax.plot([x + half_w, x + half_w], [y, y + half_w], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=7)
            arc_r = patches.Arc((x + half_w, y), half_w*2, half_w*2, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, linewidth=1.2, linestyle='--', zorder=7)
            ax.add_patch(arc_r)

    # ---------------------------------------------------------
    # 7. DRAW WALLS & DOORS FOR TÒA A
    # ---------------------------------------------------------
    # Doors for Tòa A North Row (Y = 0.9)
    doors_t1_north = [
        (3.5, 0.9, 0.9),    # 101
        (6.0, 0.9, 0.85),   # 103
        (9.0, 0.9, 0.85),   # 105
        (12.0, 0.9, 0.85),  # 107
        (20.0, 0.9, 0.85),  # 109
        (23.0, 0.9, 0.85),  # 111
        (26.0, 0.9, 0.85),  # 113
        (28.5, 0.9, 0.9),   # 115
    ]
    cutouts_t1_n = [(dx - dw/2, dx + dw/2) for dx, dy, dw in doors_t1_north]

    # Doors for Tòa A South Row (Y = -0.9)
    doors_t1_south = [
        (3.5, -0.9, 0.9),    # 102
        (6.75, -0.9, 0.9),   # 104
        (11.25, -0.9, 0.9),  # 106
        (20.5, -0.9, 1.0),   # 108
        (27.5, -0.9, 1.0),   # 110
    ]
    cutouts_t1_s = [(dx - dw/2, dx + dw/2) for dx, dy, dw in doors_t1_south]

    # Draw doors Tòa A
    for dx, dy, dw in doors_t1_north:
        draw_door(dx, dy, dw, 'IN_NORTH')
    for dx, dy, dw in doors_t1_south:
        draw_door(dx, dy, dw, 'IN_SOUTH')

    # Corridor internal walls Tòa A: ONLY draw 0 to 13.5 and 18.5 to 32.0 (Leaves 13.5 to 18.5 100% open)
    draw_wall_segment((0.0, 0.9), (13.5, 0.9), cutouts=cutouts_t1_n, thickness=PART_THICKNESS)
    draw_wall_segment((18.5, 0.9), (32.0, 0.9), cutouts=cutouts_t1_n, thickness=PART_THICKNESS)

    draw_wall_segment((0.0, -0.9), (13.5, -0.9), cutouts=cutouts_t1_s, thickness=PART_THICKNESS)
    draw_wall_segment((18.5, -0.9), (32.0, -0.9), cutouts=cutouts_t1_s, thickness=PART_THICKNESS)

    # Room partition dividers Tòa A North Row (Vertical - interior light walls)
    for px in [4.5, 7.5, 10.5, 21.5, 24.5, 27.5]:
        draw_wall_segment((px, 0.9), (px, 4.5), thickness=PART_THICKNESS)
    
    # Room partition dividers Tòa A South Row (Vertical - interior light walls)
    for px in [4.5, 9.0, 25.25]:
        draw_wall_segment((px, -4.5), (px, -0.9), thickness=PART_THICKNESS)

    # Flanking structural walls of sảnh đón Nam & sảnh sau Bắc (X = 13.5 & 18.5 - THICK WALLS)
    # South lobby wall (X = 13.5 & 18.5 from Y = -0.9 to -4.5 and down to -5.7)
    draw_wall_segment((13.5, -5.7), (13.5, -0.9), thickness=WALL_THICKNESS)
    draw_wall_segment((18.5, -5.7), (18.5, -0.9), thickness=WALL_THICKNESS)

    # North stair/exit hall wall (X = 13.5 & 18.5 from Y = 0.9 to 6.2 - THICK WALLS)
    draw_wall_segment((13.5, 0.9), (13.5, 6.2), thickness=WALL_THICKNESS)
    draw_wall_segment((18.5, 0.9), (18.5, 6.2), thickness=WALL_THICKNESS)

    # North Rear Exit Hook walls (Turn inward 0.5m at Y = 6.2m - THICK WALLS)
    draw_wall_segment((13.5, 6.2), (14.0, 6.2), thickness=WALL_THICKNESS)
    draw_wall_segment((18.0, 6.2), (18.5, 6.2), thickness=WALL_THICKNESS)

    # Exterior walls Tòa A (HEAVY WALLS: thickness = WALL_THICKNESS, lw = 4.0)
    # North exterior wall (Y = 4.5)
    draw_wall_segment((0.0, 4.5), (13.5, 4.5), thickness=WALL_THICKNESS)
    draw_wall_segment((18.5, 4.5), (32.0, 4.5), thickness=WALL_THICKNESS)

    # South exterior wall (Y = -4.5)
    draw_wall_segment((0.0, -4.5), (13.5, -4.5), thickness=WALL_THICKNESS)
    draw_wall_segment((18.5, -4.5), (32.0, -4.5), thickness=WALL_THICKNESS)

    # East & West exterior walls Tòa A (Corridor opens to outside: cutouts at -0.9 to 0.9)
    draw_wall_segment((0.0, -4.5), (0.0, 4.5), cutouts=[(-0.9, 0.9)], thickness=WALL_THICKNESS)
    draw_wall_segment((32.0, -4.5), (32.0, 4.5), cutouts=[(-0.9, 0.9)], thickness=WALL_THICKNESS)

    # ---------------------------------------------------------
    # 8. DRAW WALLS & DOORS FOR TÒA B
    # ---------------------------------------------------------
    # Doors for Tòa B Rooms (along corridor wall Y = 11.8)
    draw_door(11.5, 11.8, 1.8, 'DOUBLE_IN_NORTH')
    draw_door(27.5, 11.8, 1.0, 'IN_NORTH')

    cutouts_tb_corr = [(11.5 - 0.9, 11.5 + 0.9), (27.5 - 0.5, 27.5 + 0.5)]

    # Horizontal wall separating Tòa B corridor and rooms (Y = 11.8 - interior partition)
    draw_wall_segment((0.0, 11.8), (32.0, 11.8), cutouts=cutouts_tb_corr, thickness=PART_THICKNESS)

    # Partition dividing Room HT A and Room HT B (Vertical at X = 23.0, Y: 11.8 to 19.0 - heavy partition)
    draw_wall_segment((23.0, 11.8), (23.0, 19.0), thickness=WALL_THICKNESS)

    # Exterior walls Tòa B (HEAVY WALLS: thickness = WALL_THICKNESS, lw = 4.0)
    # North exterior wall (Y = 19.0)
    draw_wall_segment((0.0, 19.0), (32.0, 19.0), thickness=WALL_THICKNESS)

    # South exterior wall of corridor (Y = 10.0, central opening at X = 13.5 to 18.5)
    draw_wall_segment((0.0, 10.0), (32.0, 10.0), cutouts=[(13.5, 18.5)], thickness=WALL_THICKNESS)

    # East & West exterior walls Tòa B (Corridor opens to outside: cutouts at 10.0 to 11.8)
    draw_wall_segment((0.0, 10.0), (0.0, 19.0), cutouts=[(10.0, 11.8)], thickness=WALL_THICKNESS)
    draw_wall_segment((32.0, 10.0), (32.0, 19.0), cutouts=[(10.0, 11.8)], thickness=WALL_THICKNESS)

    # ---------------------------------------------------------
    # 9. WINDOWS (CỬA SỔ CHUẨN ĐỒ HỌA: 2 NÉT SONG SONG MẢNH)
    # ---------------------------------------------------------
    # Windows for Tòa A North Wall (Y = 4.5)
    # 101, 103, 105, 107
    draw_window(2.25, 4.5, 1.6, 'H')
    draw_window(6.0, 4.5, 1.4, 'H')
    draw_window(9.0, 4.5, 1.4, 'H')
    draw_window(12.0, 4.5, 1.4, 'H')
    # 109, 111, 113, 115
    draw_window(20.0, 4.5, 1.4, 'H')
    draw_window(23.0, 4.5, 1.4, 'H')
    draw_window(26.0, 4.5, 1.4, 'H')
    draw_window(29.75, 4.5, 1.6, 'H')

    # Windows for Tòa A South Wall (Y = -4.5)
    # 102, 104, 106
    draw_window(2.25, -4.5, 1.6, 'H')
    draw_window(6.75, -4.5, 1.8, 'H')
    draw_window(11.25, -4.5, 1.8, 'H')
    # 108 (Phó chánh án - 2 cửa sổ cân đối)
    draw_window(20.25, -4.5, 1.5, 'H')
    draw_window(23.5, -4.5, 1.5, 'H')
    # 110 (Thẩm phán - 2 cửa sổ cân đối)
    draw_window(27.0, -4.5, 1.5, 'H')
    draw_window(30.25, -4.5, 1.5, 'H')

    # Windows for Tòa A West Wall (X = 0.0)
    draw_window(0.0, 2.7, 1.4, 'V')
    draw_window(0.0, -2.7, 1.4, 'V')

    # Windows for Tòa A East Wall (X = 32.0)
    draw_window(32.0, 2.7, 1.4, 'V')
    draw_window(32.0, -2.7, 1.4, 'V')

    # Windows for Tòa B North Wall (Y = 19.0)
    # Room HT A (X: 0 to 23m): 5 cửa sổ cách đều
    for wx in [3.0, 7.5, 12.0, 16.5, 20.5]:
        draw_window(wx, 19.0, 1.8, 'H')
    # Room HT B (X: 23 to 32m): 2 cửa sổ cách đều
    for wx in [25.5, 29.5]:
        draw_window(wx, 19.0, 1.6, 'H')

    # Windows for Tòa B West Wall (X = 0.0)
    draw_window(0.0, 14.0, 1.8, 'V')
    draw_window(0.0, 17.0, 1.8, 'V')

    # Windows for Tòa B East Wall (X = 32.0)
    draw_window(32.0, 14.0, 1.6, 'V')
    draw_window(32.0, 17.0, 1.6, 'V')

    # Windows for Tòa B South Wall (along corridor Y = 10.0)
    for wx in [4.5, 9.0, 23.0, 27.5]:
        draw_window(wx, 10.0, 1.5, 'H')

    # ---------------------------------------------------------
    # 10. SAVE HIGH-RES OUTPUT
    # ---------------------------------------------------------
    ax.set_xlim(-2.5, 34.5)
    ax.set_ylim(-9.0, 21.0)
    
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Floorplan Floor 1 saved successfully to: {out_img_path}")

if __name__ == '__main__':
    target_dir = r'c:\Users\Tam\Desktop\BanVeThietKe\DakLak\DakLak3\Tang1'
    create_floorplan_tang1(target_dir)
