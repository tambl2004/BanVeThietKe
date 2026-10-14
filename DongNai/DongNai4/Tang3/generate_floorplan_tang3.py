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

def create_floorplan_tang3():
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(22, 11), dpi=300)
    ax = fig.add_axes([0.03, 0.08, 0.94, 0.82])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#ffffff'     # Pure white for stair background in Floor 3

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 3  —  Tòa án nhân dân khu vực 4 - Đồng Nai', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = 1.0, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 6.0, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 7.1, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 11.5, lg_x + 12.5], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.4, zorder=1)
    ax.plot([lg_x + 11.5, lg_x + 12.5], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.4, zorder=1)
    ax.text(lg_x + 12.8, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 16.5, lg_x + 16.5], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 16.5, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 17.5, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (ENCLOSED ENDS)
    # ---------------------------------------------------------
    # Horizontal Corridor (X: 0 to 35, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 35.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Stair & Hall Space (X: 15.0 to 20.0, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((15.0, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 3 - TÒA ÁN KHU VỰC 4 - ĐỒNG NAI)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === North Wing (Y > 0.9) ===
        # West of stairs (X: 0.0 to 15.0)
        {
            'id': 'P3_TKN', 'name': 'Phòng thư ký nam',
            'x': 0.0, 'y': 0.9, 'w': 7.0, 'h': 4.5,
            'text_center': (3.5, 3.15),
            'door': (5.8, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P3_KT', 'name': 'Phòng kế toán',
            'x': 7.0, 'y': 0.9, 'w': 4.0, 'h': 4.5,
            'text_center': (9.0, 3.15),
            'door': (7.8, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'P3_TP_N1', 'name': 'Phòng Thẩm phán',
            'x': 11.0, 'y': 0.9, 'w': 4.0, 'h': 4.5,
            'text_center': (13.0, 3.15),
            'door': (11.8, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        # East of stairs (X: 20.0 to 35.0)
        {
            'id': 'P3_TP_N2', 'name': 'Phòng Thẩm phán',
            'x': 20.0, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (21.875, 3.15),
            'door': (20.5, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'P3_TP_N3', 'name': 'Phòng Thẩm phán',
            'x': 23.75, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (25.625, 3.15),
            'door': (24.25, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'P3_TP_N4', 'name': 'Phòng Thẩm phán',
            'x': 27.5, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (29.375, 3.15),
            'door': (28.0, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'P3_TP_N5', 'name': 'Phòng Thẩm phán',
            'x': 31.25, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (33.125, 3.15),
            'door': (31.75, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.0
        },

        # === South Wing (Y < -0.9) ===
        {
            'id': 'P3_PCA1', 'name': 'Phòng Phó Chánh án',
            'x': 0.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (2.5, -2.9),
            'door': (3.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'P3_TP_S1', 'name': 'Phòng Thẩm phán',
            'x': 5.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (7.5, -2.9),
            'door': (5.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'P3_TP_S2', 'name': 'Phòng Thẩm phán',
            'x': 10.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (12.5, -2.9),
            'door': (10.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'P3_TP_S3', 'name': 'Phòng Thẩm phán',
            'x': 15.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (17.5, -2.9),
            'door': (15.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'P3_TP_S4', 'name': 'Phòng Thẩm phán',
            'x': 20.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (22.5, -2.9),
            'door': (20.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'P3_PCA2', 'name': 'Phòng Phó Chánh án',
            'x': 25.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (27.5, -2.9),
            'door': (25.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'P3_PCA3', 'name': 'Phòng Phó Chánh án',
            'x': 30.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (32.5, -2.9),
            'door': (30.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.2
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHIC (UPPER FLOOR - WHITE BACKGROUND)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 16.2, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    gap = 0.35
    flight_w = (stair_w - gap) / 2.0
    left_x1, left_x2 = stair_x, stair_x + flight_w
    right_x1, right_x2 = stair_x + flight_w + gap, stair_x + stair_w

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([left_x1, left_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
        ax.plot([right_x1, right_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_left = left_x1 + flight_w / 2.0
    mid_right = right_x1 + flight_w / 2.0
    ax.plot([mid_left, mid_left], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([mid_right, mid_right], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # Labels for Corridor
    ax.text(7.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(27.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (CLOSED EXTERIOR ENCLOSURE FOR UPPER FLOOR)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Wall (Continuous)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2 * W)

    # Rightmost Vertical Exterior Wall (Continuous)
    draw_wall(35.0, -4.9 - W, W, 10.3 + 2 * W)

    # Topmost Horizontal Exterior Wall (North Facade)
    draw_wall(-W, 5.4, 35.0 + 2 * W, W)

    # Bottommost Horizontal Exterior Wall (South Facade)
    draw_wall(-W, -4.9 - W, 35.0 + 2 * W, W)

    # Corridor North Horizontal Wall (Y = 0.9 - W, split for doors & stair hall)
    draw_wall(0.0, 0.9 - W, 5.8, W)
    draw_wall(6.65, 0.9 - W, 1.15, W)
    draw_wall(8.65, 0.9 - W, 3.15, W)
    draw_wall(12.65, 0.9 - W, 2.35, W)
    # Opening for stair hall at X = 15.0 to 20.0
    draw_wall(20.0, 0.9 - W, 0.5, W)
    draw_wall(21.35, 0.9 - W, 2.9, W)
    draw_wall(25.1, 0.9 - W, 2.9, W)
    draw_wall(28.85, 0.9 - W, 2.9, W)
    draw_wall(32.6, 0.9 - W, 2.4, W)

    # Corridor South Horizontal Wall (Y = -0.9, split for 7 doors)
    draw_wall(0.0, -0.9, 3.8, W)
    draw_wall(4.65, -0.9, 1.15, W)
    draw_wall(6.65, -0.9, 4.15, W)
    draw_wall(11.65, -0.9, 4.15, W)
    draw_wall(16.65, -0.9, 4.15, W)
    draw_wall(21.65, -0.9, 4.15, W)
    draw_wall(26.65, -0.9, 4.15, W)
    draw_wall(31.65, -0.9, 3.35, W)

    # Interior Partitions (North Wing)
    draw_wall(7.0 - PART_THICKNESS/2.0, 0.9, PART_THICKNESS, 4.5)
    draw_wall(11.0 - PART_THICKNESS/2.0, 0.9, PART_THICKNESS, 4.5)
    draw_wall(15.0 - PART_THICKNESS, 0.9, PART_THICKNESS, 4.5)
    draw_wall(20.0, 0.9, PART_THICKNESS, 4.5)
    draw_wall(23.75 - PART_THICKNESS/2.0, 0.9, PART_THICKNESS, 4.5)
    draw_wall(27.5 - PART_THICKNESS/2.0, 0.9, PART_THICKNESS, 4.5)
    draw_wall(31.25 - PART_THICKNESS/2.0, 0.9, PART_THICKNESS, 4.5)

    # Interior Partitions (South Wing)
    draw_wall(5.0 - PART_THICKNESS/2.0, -4.9, PART_THICKNESS, 4.0)
    draw_wall(10.0 - PART_THICKNESS/2.0, -4.9, PART_THICKNESS, 4.0)
    draw_wall(15.0 - PART_THICKNESS/2.0, -4.9, PART_THICKNESS, 4.0)
    draw_wall(20.0 - PART_THICKNESS/2.0, -4.9, PART_THICKNESS, 4.0)
    draw_wall(25.0 - PART_THICKNESS/2.0, -4.9, PART_THICKNESS, 4.0)
    draw_wall(30.0 - PART_THICKNESS/2.0, -4.9, PART_THICKNESS, 4.0)

    # ---------------------------------------------------------
    # 7. DRAW WINDOWS
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

    # North Windows
    draw_window(2.5, 5.4, 2.0, W, is_horizontal=True)    # P3_TKN
    draw_window(8.25, 5.4, 1.5, W, is_horizontal=True)   # P3_KT
    draw_window(12.25, 5.4, 1.5, W, is_horizontal=True)  # P3_TP_N1
    draw_window(16.5, 5.4, 2.0, W, is_horizontal=True)   # Stair Hall
    draw_window(21.1, 5.4, 1.5, W, is_horizontal=True)   # P3_TP_N2
    draw_window(24.85, 5.4, 1.5, W, is_horizontal=True)  # P3_TP_N3
    draw_window(28.6, 5.4, 1.5, W, is_horizontal=True)   # P3_TP_N4
    draw_window(32.35, 5.4, 1.5, W, is_horizontal=True)  # P3_TP_N5

    # South Windows
    for i in range(7):
        wx = i * 5.0 + 1.5
        draw_window(wx, -4.9 - W, 2.0, W, is_horizontal=True)

    # Corridor End Windows
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(35.0, -0.6, W, 1.2, is_horizontal=False)

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode == 'N_IN_RIGHT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_RIGHT':
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)

    for r in rooms:
        dx, dy, dsize, dmode = r['door']
        draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 9.2)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                fontweight='bold', ha='center', va='center', zorder=15)

    ax.set_xlim(-3.0, 38.0)
    ax.set_ylim(-7.5, 7.5)

    out_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\DongNai\DongNai4\Tang3"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mat_bang_tang_3.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 3 đã xuất thành công tại: {out_path}")

if __name__ == "__main__":
    create_floorplan_tang3()
