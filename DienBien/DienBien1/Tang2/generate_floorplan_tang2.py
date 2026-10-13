import os
from typing import TypedDict, Tuple, List
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
    door: Tuple[float, float, float, str]
    font_size: float

def create_floorplan_tang2(output_dir: str = None):
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, "mat_bang_tang_2.png")

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 15), dpi=300)
    ax = fig.add_axes([0.02, 0.06, 0.96, 0.86])
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
    COLOR_STAIR_FILL = '#ffffff'    # Pure white stair fill for upper floors per Spec

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 1 - Điện Biên', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.03, 0.97], [0.925, 0.925], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = 1.0, -7.8
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.1, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.add_patch(patches.Rectangle((lg_x + 7.5, lg_y + 0.15), 1.2, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 9.0, lg_y + 0.1, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 15.0, lg_x + 16.2], [lg_y + 0.25, lg_y + 0.25], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 15.0, lg_x + 16.2], [lg_y + 0.10, lg_y + 0.10], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 16.6, lg_y + 0.1, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 22.0, lg_x + 22.0], [lg_y + 0.05, lg_y + 0.45], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 22.0, lg_y + 0.05), 0.8, 0.8, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 23.4, lg_y + 0.1, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Main Horizontal Corridor (X: 0 to 32, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 32.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Rear Stair Hall (North: X: 13.5 to 18.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Corridor labels
    bbox_style = dict(boxstyle='round,pad=0.2', facecolor=COLOR_FILL_CORRIDOR, edgecolor='none')
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5, bbox=bbox_style)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5, bbox=bbox_style)

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (11 ROOMS AS SURVEY DATA)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- DÃY NAM (South Wing): 3 phòng ---
        {
            'id': 'T2_HTH', 'name': 'Phòng hội trường họp',
            'x': 0.0, 'y': -4.9, 'w': 13.5, 'h': 4.0,
            'text_center': (6.75, -2.9),
            'door': (6.05, -0.9, 1.4, 'DOUBLE_S_IN'),
            'font_size': 12.0
        },
        # Vị trí trung tâm: Phòng Chánh án (cửa chính xác từ x=15.5 đến 16.5)
        {
            'id': 'T2_CA', 'name': 'Phòng Chánh án',
            'x': 13.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (16.0, -2.9),
            'door': (15.5, -0.9, 1.0, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
        {
            'id': 'T2_XXHS', 'name': 'Phòng xét xử Hình sự',
            'x': 18.5, 'y': -4.9, 'w': 13.5, 'h': 4.0,
            'text_center': (25.25, -2.9),
            'door': (24.55, -0.9, 1.4, 'DOUBLE_S_IN'),
            'font_size': 12.0
        },

        # --- DÃY BẮC (North Wing): 8 phòng làm việc ---
        # 1. Cánh Tây Bắc (4 phòng: w = 3.375m mỗi phòng, cửa cách vách phải 0.3m má tường)
        {
            'id': 'T2_PCA1', 'name': 'Phòng Phó Chánh án',
            'x': 0.0, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (1.6875, 3.15),
            'door': (2.225, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T2_PCA2', 'name': 'Phòng Phó Chánh án',
            'x': 3.375, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (5.0625, 3.15),
            'door': (5.60, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T2_TP1', 'name': 'Phòng Thẩm phán',
            'x': 6.75, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (8.4375, 3.15),
            'door': (8.975, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T2_TP2', 'name': 'Phòng Thẩm phán',
            'x': 10.125, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (11.8125, 3.15),
            'door': (12.35, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },

        # 2. Cánh Đông Bắc (4 phòng: w = 3.375m mỗi phòng, cửa cách vách trái 0.3m má tường)
        {
            'id': 'T2_TP3', 'name': 'Phòng Thẩm phán',
            'x': 18.5, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (20.1875, 3.15),
            'door': (18.80, 0.9, 0.85, 'N_IN_LEFT'),
            'font_size': 9.5
        },
        {
            'id': 'T2_KT', 'name': 'Phòng Kế toán',
            'x': 21.875, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (23.5625, 3.15),
            'door': (22.175, 0.9, 0.85, 'N_IN_LEFT'),
            'font_size': 9.5
        },
        {
            'id': 'T2_TK1', 'name': 'Phòng Thư ký viên',
            'x': 25.25, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (26.9375, 3.15),
            'door': (25.55, 0.9, 0.85, 'N_IN_LEFT'),
            'font_size': 9.5
        },
        {
            'id': 'T2_TK2', 'name': 'Phòng Thư ký viên',
            'x': 28.625, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (30.3125, 3.15),
            'door': (28.925, 0.9, 0.85, 'N_IN_LEFT'),
            'font_size': 9.5
        },
    ]

    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE (UPPER FLOOR SPEC: PURE WHITE BACKGROUND)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 14.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (CONTINUOUS EXTERIOR WALLS - NO OUTDOOR STEPS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior Leftmost Wall (West): Continuous
    draw_wall(-W, -4.9 - W, W, 10.3 + 2 * W)

    # Exterior Rightmost Wall (East): Continuous
    draw_wall(32.0, -4.9 - W, W, 10.3 + 2 * W)

    # North Top Wall: Continuous across 32m
    draw_wall(-W, 5.4, 32.0 + 2 * W, W)

    # South Bottom Wall: Continuous across 32m
    draw_wall(-W, -4.9 - W, 32.0 + 2 * W, W)

    # Horizontal Corridor Partitions:
    # 1. North Corridor Wall (Y = 0.9 - P/2)
    # West North: openings at doors:
    # - Door 1: 2.225 to 3.075
    # - Door 2: 5.60 to 6.45
    # - Door 3: 8.975 to 9.825
    # - Door 4: 12.35 to 13.20
    draw_wall(0.0, 0.9 - P/2, 2.225, P)
    draw_wall(3.075, 0.9 - P/2, 5.60 - 3.075, P)
    draw_wall(6.45, 0.9 - P/2, 8.975 - 6.45, P)
    draw_wall(9.825, 0.9 - P/2, 12.35 - 9.825, P)
    draw_wall(13.20, 0.9 - P/2, 13.5 - 13.20, P)

    # East North: openings at doors:
    # - Door 5: 18.80 to 19.65
    # - Door 6: 22.175 to 23.025
    # - Door 7: 25.55 to 26.40
    # - Door 8: 28.925 to 29.775
    draw_wall(18.5, 0.9 - P/2, 18.80 - 18.5, P)
    draw_wall(19.65, 0.9 - P/2, 22.175 - 19.65, P)
    draw_wall(23.025, 0.9 - P/2, 25.55 - 23.025, P)
    draw_wall(26.40, 0.9 - P/2, 28.925 - 26.40, P)
    draw_wall(29.775, 0.9 - P/2, 32.0 - 29.775, P)

    # 2. South Corridor Wall (Y = -0.9 - P/2)
    # Door openings:
    # - HTH double door: 6.05 to 7.45 (1.4m)
    # - Phòng Chánh án door: 15.5 to 16.5 (1.0m)
    # - XXHS double door: 24.55 to 25.95 (1.4m)
    draw_wall(0.0, -0.9 - P/2, 6.05, P)
    draw_wall(7.45, -0.9 - P/2, 15.5 - 7.45, P)
    draw_wall(16.5, -0.9 - P/2, 24.55 - 16.5, P)
    draw_wall(25.95, -0.9 - P/2, 32.0 - 25.95, P)

    # Vertical Room Partitions:
    draw_wall(3.375 - P/2, 0.9, P, 4.5)
    draw_wall(6.75 - P/2, 0.9, P, 4.5)
    draw_wall(10.125 - P/2, 0.9, P, 4.5)
    draw_wall(13.5 - P/2, 0.9, P, 4.5)

    draw_wall(18.5 - P/2, 0.9, P, 4.5)
    draw_wall(21.875 - P/2, 0.9, P, 4.5)
    draw_wall(25.25 - P/2, 0.9, P, 4.5)
    draw_wall(28.625 - P/2, 0.9, P, 4.5)

    draw_wall(13.5 - P/2, -4.9, P, 4.0)
    draw_wall(18.5 - P/2, -4.9, P, 4.0)

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

    # North Facade Windows (Y = 5.4)
    draw_window(0.8, 5.4, 1.8, W, is_horizontal=True)    # PCA 1
    draw_window(4.2, 5.4, 1.8, W, is_horizontal=True)    # PCA 2
    draw_window(7.6, 5.4, 1.8, W, is_horizontal=True)    # TP 1
    draw_window(11.0, 5.4, 1.8, W, is_horizontal=True)   # TP 2
    draw_window(14.8, 5.4, 2.4, W, is_horizontal=True)   # Stair Hall North Window
    draw_window(19.3, 5.4, 1.8, W, is_horizontal=True)   # TP 3
    draw_window(22.7, 5.4, 1.8, W, is_horizontal=True)   # KT
    draw_window(26.1, 5.4, 1.8, W, is_horizontal=True)   # TK 1
    draw_window(29.5, 5.4, 1.8, W, is_horizontal=True)   # TK 2

    # South Facade Windows (Y = -4.9 - W)
    draw_window(2.0, -4.9 - W, 2.4, W, is_horizontal=True)   # Hội trường họp 1
    draw_window(6.0, -4.9 - W, 2.4, W, is_horizontal=True)   # Hội trường họp 2
    draw_window(10.0, -4.9 - W, 2.4, W, is_horizontal=True)  # Hội trường họp 3
    draw_window(14.8, -4.9 - W, 2.4, W, is_horizontal=True)  # Phòng Chánh án Front Window
    draw_window(20.5, -4.9 - W, 2.4, W, is_horizontal=True)  # Xét xử hình sự 1
    draw_window(24.5, -4.9 - W, 2.4, W, is_horizontal=True)  # Xét xử hình sự 2
    draw_window(28.5, -4.9 - W, 2.4, W, is_horizontal=True)  # Xét xử hình sự 3

    # West & East Facade Windows
    draw_window(-W, 2.0, W, 2.2, is_horizontal=False)     # West Upper Room
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)    # West Corridor End Window
    draw_window(-W, -3.8, W, 2.2, is_horizontal=False)    # West Lower Room
    draw_window(32.0, 2.0, W, 2.2, is_horizontal=False)   # East Upper Room
    draw_window(32.0, -0.6, W, 1.2, is_horizontal=False)  # East Corridor End Window
    draw_window(32.0, -3.8, W, 2.2, is_horizontal=False)  # East Lower Room

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode == 'N_IN_RIGHT':
            pivot_x = x + size
            ax.plot([pivot_x, pivot_x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((pivot_x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'N_IN_LEFT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_RIGHT':
            pivot_x = x + size
            ax.plot([pivot_x, pivot_x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((pivot_x, y), size*2, size*2, angle=0, theta1=180, theta2=270,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'DOUBLE_S_IN':
            half = size / 2.0
            p_left = x
            ax.plot([p_left, p_left], [y, y - half], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_left = patches.Arc((p_left, y), half*2, half*2, angle=0, theta1=270, theta2=360,
                                   color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc_left)
            p_right = x + size
            ax.plot([p_right, p_right], [y, y - half], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_right = patches.Arc((p_right, y), half*2, half*2, angle=0, theta1=180, theta2=270,
                                    color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc_right)

    for r in rooms:
        dx, dy, dsize, dmode = r['door']
        draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 10.0)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.5, 34.5)
    ax.set_ylim(-8.5, 8.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 2 floorplan PNG at {out_img_path}")
    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang2()
