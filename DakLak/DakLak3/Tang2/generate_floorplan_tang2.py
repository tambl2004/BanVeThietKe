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

def create_floorplan_tang2(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_2.png')

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

    WALL_THICKNESS = 0.22           # 220mm exterior wall
    PART_THICKNESS = 0.12           # 120mm interior wall
    W = WALL_THICKNESS

    # Geometry bounds
    X_MIN = 0.0
    X_MAX = 32.0

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Single-line title, font 20 bold, NO subtitle line
    fig.text(0.04, 0.965, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 3 - Đắk Lắk', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.04, 0.96], [0.948, 0.948], transform=fig.transFigure, color='#e2e8f0', linewidth=1.2)
    fig.lines.append(header_line)

    # Legend Box at Bottom Center
    lg_x, lg_y = 4.0, -8.0
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

    # Legend Item 5: Roof (Mái che)
    ax.add_patch(patches.Rectangle((lg_x + 27.5, lg_y + 0.06), 1.2, 0.28, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.2, zorder=1))
    ax.text(lg_x + 29.0, lg_y + 0.06, 'Mái che', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR BACKGROUND FILL FOR TÒA A TẦNG 2
    # ---------------------------------------------------------
    # Central horizontal corridor (X: 0.0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((X_MIN, -0.9), X_MAX - X_MIN, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Stair Hall North (X: 13.5 to 18.5, Y: 0.9 to 4.5) - Open continuous corridor circulation
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 3.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Corridor labels
    bbox_corr = dict(boxstyle='round,pad=0.2', facecolor=COLOR_FILL_CORRIDOR, edgecolor='none')
    ax.text(6.75, 0.0, 'HÀNH LANG', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6, bbox=bbox_corr)
    ax.text(25.25, 0.0, 'HÀNH LANG', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6, bbox=bbox_corr)

    # ---------------------------------------------------------
    # 4. ROOF AREA FOR TÒA B (MÁI CHE - KHỐI 1 TẦNG PHÍA BẮC)
    # ---------------------------------------------------------
    # Footprint of Tòa B Roof: X: 0.0 to 32.0, Y: 10.0 to 19.0
    roof_patch = patches.Rectangle((X_MIN, 10.0), X_MAX - X_MIN, 9.0, 
                                   facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=2.5, zorder=2)
    ax.add_patch(roof_patch)

    # Large MÁI CHE label in center of Tòa B roof footprint
    ax.text(16.0, 14.5, 'MÁI CHE', color=COLOR_TEXT_MUTED, fontsize=18.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 5. ROOM DEFINITIONS (TÒA A: 11 PHÒNG TẦNG 2 ĐÚNG PROMPT)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- Dãy phía Bắc Tòa A (Y: 0.9 to 4.5, h = 3.6) ---
        {
            'id': 'T2_201', 'name': 'Phòng Kho lưu trữ 201',
            'x': 0.0, 'y': 0.9, 'w': 4.5, 'h': 3.6,
            'text_center': (2.25, 2.7), 'font_size': 8.5
        },
        {
            'id': 'T2_203', 'name': 'Phòng Kho lưu trữ 203',
            'x': 4.5, 'y': 0.9, 'w': 4.5, 'h': 3.6,
            'text_center': (6.75, 2.7), 'font_size': 8.5
        },
        {
            'id': 'T2_205', 'name': 'Phòng Kho lưu trữ 205',
            'x': 9.0, 'y': 0.9, 'w': 4.5, 'h': 3.6,
            'text_center': (11.25, 2.7), 'font_size': 8.5
        },
        # [Cầu thang bộ Tầng 2 gọn gàng ở giữa: X: 14.6 to 17.4, Y: 1.3 to 4.0]
        {
            'id': 'T2_209', 'name': 'Phòng Hòa giải viên 209',
            'x': 18.5, 'y': 0.9, 'w': 4.5, 'h': 3.6,
            'text_center': (20.75, 2.7), 'font_size': 8.5
        },
        {
            'id': 'T2_211', 'name': 'Phòng Hòa giải viên 211',
            'x': 23.0, 'y': 0.9, 'w': 4.5, 'h': 3.6,
            'text_center': (25.25, 2.7), 'font_size': 8.5
        },
        {
            'id': 'T2_213', 'name': 'Phòng Lưu trữ 213',
            'x': 27.5, 'y': 0.9, 'w': 4.5, 'h': 3.6,
            'text_center': (29.75, 2.7), 'font_size': 8.5
        },

        # --- Dãy phía Nam Tòa A (Y: -4.5 to -0.9, h = 3.6) ---
        {
            'id': 'T2_202', 'name': 'Phòng Chánh án 202',
            'x': 0.0, 'y': -4.5, 'w': 5.5, 'h': 3.6,
            'text_center': (2.75, -2.7), 'font_size': 9.0
        },
        {
            'id': 'T2_204', 'name': 'Phòng Phó chánh án 204',
            'x': 5.5, 'y': -4.5, 'w': 5.5, 'h': 3.6,
            'text_center': (8.25, -2.7), 'font_size': 9.0
        },
        # Trung tâm phía Nam: PHÒNG HỘI TRƯỜNG HỌP 207 (KT: 10 x 4m)
        {
            'id': 'T2_207', 'name': 'PHÒNG HỘI TRƯỜNG HỌP 207',
            'x': 11.0, 'y': -4.5, 'w': 10.0, 'h': 3.6,
            'text_center': (16.0, -2.7), 'font_size': 10.5
        },
        {
            'id': 'T2_206', 'name': 'Phòng Thẩm phán 206',
            'x': 21.0, 'y': -4.5, 'w': 5.5, 'h': 3.6,
            'text_center': (23.75, -2.7), 'font_size': 9.0
        },
        {
            'id': 'T2_208', 'name': 'Phòng Thư ký 208',
            'x': 26.5, 'y': -4.5, 'w': 5.5, 'h': 3.6,
            'text_center': (29.25, -2.7), 'font_size': 9.0
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
    # 6. COMPACT STAIRCASE TÒA A (FLOOR 2)
    # ---------------------------------------------------------
    # Staircase dimensions: 2.8m wide x 2.7m high, centered in North hall (X: 13.5 to 18.5)
    stair_w, stair_h = 2.8, 2.7
    stair_x = 16.0 - stair_w / 2.0  # 14.6m
    stair_y = 1.3                   # leaves open sides
    
    # Staircase background matches corridor tone (#eef4f7)
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
    # 7. DRAW WALLS & OPENINGS HELPER FUNCTIONS
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
            # Strictly clamp cutouts inside [y_min, y_max]
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
            # Strictly clamp cutouts inside [x_min, x_max]
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

    # FIX CỬA SỔ CHUẨN: NỀN TRẮNG CHE VÁCH + 2 ĐƯỜNG KẺ SONG SONG MẢNH (KHÔNG CÓ NÉT ĐẬM Ở GIỮA)
    def draw_window(x: float, y: float, w: float, orientation: str):
        if orientation == 'H':
            ax.add_patch(patches.Rectangle((x - w/2, y - W/2 - 0.02), w, W + 0.04, 
                                           facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x - w/2, x + w/2], [y + W/2 - 0.02, y + W/2 - 0.02], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x - w/2, x + w/2], [y - W/2 + 0.02, y - W/2 + 0.02], color=COLOR_WALL, linewidth=1.2, zorder=12)
        else:
            ax.add_patch(patches.Rectangle((x - W/2 - 0.02, y - w/2), W + 0.04, w, 
                                           facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x + W/2 - 0.02, x + W/2 - 0.02], [y - w/2, y + w/2], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x - W/2 + 0.02, x - W/2 + 0.02], [y - w/2, y + w/2], color=COLOR_WALL, linewidth=1.2, zorder=12)

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
        elif direction == 'DOUBLE_IN_SOUTH':
            half_w = width / 2.0
            ax.add_patch(patches.Rectangle((x - half_w, y - 0.12), width, 0.24, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=6))
            ax.plot([x - half_w, x - half_w], [y, y - half_w], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=7)
            arc_l = patches.Arc((x - half_w, y), half_w*2, half_w*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.2, linestyle='--', zorder=7)
            ax.add_patch(arc_l)
            ax.plot([x + half_w, x + half_w], [y, y - half_w], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=7)
            arc_r = patches.Arc((x + half_w, y), half_w*2, half_w*2, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, linewidth=1.2, linestyle='--', zorder=7)
            ax.add_patch(arc_r)

    # ---------------------------------------------------------
    # 8. DRAW WALLS & DOORS FOR TÒA A TẦNG 2
    # ---------------------------------------------------------
    # Doors for North Row (Y = 0.9)
    doors_t2_north = [
        (3.5, 0.9, 0.9),    # 201
        (7.5, 0.9, 0.9),    # 203
        (11.5, 0.9, 0.9),   # 205
        (20.0, 0.9, 0.9),   # 209
        (24.5, 0.9, 0.9),   # 211
        (29.0, 0.9, 0.9),   # 213
    ]
    cutouts_t2_n = [(dx - dw/2, dx + dw/2) for dx, dy, dw in doors_t2_north]

    # Doors for South Row (Y = -0.9)
    doors_t2_south = [
        (4.5, -0.9, 0.9),    # 202
        (6.5, -0.9, 0.9),    # 204
        (16.0, -0.9, 1.8),   # 207 (Double door)
        (25.5, -0.9, 0.9),   # 206
        (27.5, -0.9, 0.9),   # 208
    ]
    cutouts_t2_s = [(dx - dw/2, dx + dw/2) for dx, dy, dw in doors_t2_south]

    # Draw doors
    for dx, dy, dw in doors_t2_north:
        draw_door(dx, dy, dw, 'IN_NORTH')
    draw_door(4.5, -0.9, 0.9, 'IN_SOUTH')
    draw_door(6.5, -0.9, 0.9, 'IN_SOUTH')
    draw_door(16.0, -0.9, 1.8, 'DOUBLE_IN_SOUTH')
    draw_door(25.5, -0.9, 0.9, 'IN_SOUTH')
    draw_door(27.5, -0.9, 0.9, 'IN_SOUTH')

    # Corridor internal walls Tòa A
    draw_wall_segment((0.0, 0.9), (13.5, 0.9), cutouts=cutouts_t2_n, thickness=PART_THICKNESS)
    draw_wall_segment((18.5, 0.9), (32.0, 0.9), cutouts=cutouts_t2_n, thickness=PART_THICKNESS)

    # South corridor wall runs continuously with cutouts for doors
    draw_wall_segment((0.0, -0.9), (32.0, -0.9), cutouts=cutouts_t2_s, thickness=PART_THICKNESS)

    # Room partition dividers North Row (Vertical)
    for px in [4.5, 9.0, 23.0, 27.5]:
        draw_wall_segment((px, 0.9), (px, 4.5), thickness=PART_THICKNESS)
    
    # Staircase structural enclosing walls (X = 13.5 and 18.5, Y: 0.9 to 4.5)
    draw_wall_segment((13.5, 0.9), (13.5, 4.5), thickness=WALL_THICKNESS)
    draw_wall_segment((18.5, 0.9), (18.5, 4.5), thickness=WALL_THICKNESS)

    # Room partition dividers South Row (Vertical)
    for px in [5.5, 11.0, 21.0, 26.5]:
        draw_wall_segment((px, -4.5), (px, -0.9), thickness=PART_THICKNESS)

    # Exterior walls Tòa A
    # North exterior wall (Y = 4.5) - continuous from 0 to 32
    draw_wall_segment((0.0, 4.5), (32.0, 4.5), thickness=WALL_THICKNESS)

    # South exterior wall (Y = -4.5) - continuous from 0 to 32
    draw_wall_segment((0.0, -4.5), (32.0, -4.5), thickness=WALL_THICKNESS)

    # East & West exterior walls Tòa A - Fully enclosed on upper floor, with windows for corridor
    draw_wall_segment((0.0, -4.5), (0.0, 4.5), thickness=WALL_THICKNESS)
    draw_wall_segment((32.0, -4.5), (32.0, 4.5), thickness=WALL_THICKNESS)

    # ---------------------------------------------------------
    # 9. WINDOWS FOR TÒA A TẦNG 2 (CỬA SỔ CHUẨN ĐỒ HỌA: 2 NÉT SONG SONG MẢNH)
    # ---------------------------------------------------------
    # Windows for Tòa A North Wall (Y = 4.5)
    # Rooms 201, 203, 205 (X: 0 to 13.5)
    for wx in [2.25, 6.75, 11.25]:
        draw_window(wx, 4.5, 1.6, 'H')
    # Window for Staircase hall at X = 16.0
    draw_window(16.0, 4.5, 1.8, 'H')
    # Rooms 209, 211, 213 (X: 18.5 to 32)
    for wx in [20.75, 25.25, 29.75]:
        draw_window(wx, 4.5, 1.6, 'H')

    # Windows for Tòa A South Wall (Y = -4.5)
    # Room 202, 204
    draw_window(2.75, -4.5, 1.6, 'H')
    draw_window(8.25, -4.5, 1.6, 'H')
    # Room 207 (Hội trường họp: 3 large windows)
    for wx in [13.0, 16.0, 19.0]:
        draw_window(wx, -4.5, 1.8, 'H')
    # Room 206, 208
    draw_window(23.75, -4.5, 1.6, 'H')
    draw_window(29.25, -4.5, 1.6, 'H')

    # Windows for Tòa A West Wall (X = 0.0)
    draw_window(0.0, 2.7, 1.4, 'V')     # Room 201
    draw_window(0.0, 0.0, 1.4, 'V')     # Corridor end window
    draw_window(0.0, -2.7, 1.4, 'V')    # Room 202

    # Windows for Tòa A East Wall (X = 32.0)
    draw_window(32.0, 2.7, 1.4, 'V')    # Room 213
    draw_window(32.0, 0.0, 1.4, 'V')    # Corridor end window
    draw_window(32.0, -2.7, 1.4, 'V')   # Room 208

    # ---------------------------------------------------------
    # 10. SAVE HIGH-RES OUTPUT
    # ---------------------------------------------------------
    ax.set_xlim(-2.5, 34.5)
    ax.set_ylim(-9.0, 21.0)
    
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Floorplan Floor 2 saved successfully to: {out_img_path}")

if __name__ == '__main__':
    target_dir = r'c:\Users\Tam\Desktop\BanVeThietKe\DakLak\DakLak3\Tang2'
    create_floorplan_tang2(target_dir)
