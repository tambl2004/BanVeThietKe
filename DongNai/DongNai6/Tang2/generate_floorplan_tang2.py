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

def create_floorplan_tang2():
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
    COLOR_STAIR_FILL = '#ffffff'     # Pure white for stair background in Floor 2

    WALL_THICKNESS = 0.22  # 220mm exterior structural wall (Thick exterior)
    PART_THICKNESS = 0.09  # 90mm interior partition & corridor wall (Thin interior)
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 6 - Đồng Nai', 
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
    # 3. CORRIDOR BACKGROUND FILL (ENCLOSED ENDS)
    # ---------------------------------------------------------
    # Horizontal Corridor (X: 0 to 35, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 35.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Stair Hall Space (X: 15.0 to 20.0, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((15.0, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 2 - TÒA ÁN KHU VỰC 6 - ĐỒNG NAI)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # North Wing (Y > 0.9)
        {
            'id': 'P2_XXB', 'name': 'Phòng xét xử B',
            'x': 0.0, 'y': 0.9, 'w': 15.0, 'h': 4.5,
            'text_center': (7.5, 3.15),
            'door': (13.5, 0.9, 1.0, 'N_IN_RIGHT'),
            'font_size': 11.5
        },
        {
            'id': 'P2_LV6', 'name': 'Phòng làm việc 6',
            'x': 20.0, 'y': 0.9, 'w': 5.0, 'h': 4.5,
            'text_center': (22.5, 3.15),
            'door': (20.5, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P2_LV7', 'name': 'Phòng làm việc 7',
            'x': 25.0, 'y': 0.9, 'w': 5.0, 'h': 4.5,
            'text_center': (27.5, 3.15),
            'door': (25.5, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P2_LV8', 'name': 'Phòng làm việc 8',
            'x': 30.0, 'y': 0.9, 'w': 5.0, 'h': 4.5,
            'text_center': (32.5, 3.15),
            'door': (30.5, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        # South Wing (Y < -0.9) - 4 office rooms evenly distributed across 35m (8.75m each)
        {
            'id': 'P2_LV9', 'name': 'Phòng làm việc 9',
            'x': 0.0, 'y': -4.9, 'w': 8.75, 'h': 4.0,
            'text_center': (4.375, -2.9),
            'door': (7.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P2_LV10', 'name': 'Phòng làm việc 10',
            'x': 8.75, 'y': -4.9, 'w': 8.75, 'h': 4.0,
            'text_center': (13.125, -2.9),
            'door': (9.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P2_LV11', 'name': 'Phòng làm việc 11',
            'x': 17.5, 'y': -4.9, 'w': 8.75, 'h': 4.0,
            'text_center': (21.875, -2.9),
            'door': (18.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P2_LV12', 'name': 'Phòng làm việc 12',
            'x': 26.25, 'y': -4.9, 'w': 8.75, 'h': 4.0,
            'text_center': (30.625, -2.9),
            'door': (27.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
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
    # 6. DRAW WALLS (DISTINCT THICK EXTERIOR & THIN INTERIOR)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # === THICK EXTERIOR WALLS (W = 0.22) ===
    # Leftmost Vertical Exterior Wall (Continuous enclosing the floor)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2 * W)

    # Rightmost Vertical Exterior Wall (Continuous enclosing the floor)
    draw_wall(35.0, -4.9 - W, W, 10.3 + 2 * W)

    # Topmost Horizontal Exterior Wall (North Facade - continuous)
    draw_wall(-W, 5.4, 35.0 + 2 * W, W)

    # Bottommost Horizontal Exterior Wall (South Facade - continuous)
    draw_wall(-W, -4.9 - W, 35.0 + 2 * W, W)

    # === THIN INTERIOR WALLS & PARTITIONS (P = 0.09) ===
    # North Corridor Wall (Placed at Y in [0.9, 0.9 + P])
    draw_wall(0.0, 0.9, 13.5, P)
    draw_wall(14.5, 0.9, 0.5, P)
    # Opening for stair hall at X = 15.0 to 20.0
    draw_wall(20.0, 0.9, 0.5, P)
    draw_wall(21.35, 0.9, 4.15, P)
    draw_wall(26.35, 0.9, 4.15, P)
    draw_wall(31.35, 0.9, 3.65, P)

    # South Corridor Wall (Placed at Y in [-0.9 - P, -0.9])
    draw_wall(0.0, -0.9 - P, 7.2, P)
    draw_wall(8.05, -0.9 - P, 1.45, P)
    draw_wall(10.35, -0.9 - P, 7.85, P)
    draw_wall(19.05, -0.9 - P, 7.95, P)
    draw_wall(27.85, -0.9 - P, 7.15, P)

    # Room Dividing Partitions (North Wing)
    draw_wall(15.0 - P, 0.9, P, 4.5)
    draw_wall(20.0, 0.9, P, 4.5)
    draw_wall(25.0 - P/2.0, 0.9 + P, P, 4.5 - P)
    draw_wall(30.0 - P/2.0, 0.9 + P, P, 4.5 - P)

    # Room Dividing Partitions (South Wing)
    draw_wall(8.75 - P/2.0, -4.9, P, 4.0 - P)
    draw_wall(17.5 - P/2.0, -4.9, P, 4.0 - P)
    draw_wall(26.25 - P/2.0, -4.9, P, 4.0 - P)

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

    # North Facade Windows
    draw_window(3.5, 5.4, 3.0, W, is_horizontal=True)    # P2_XXB
    draw_window(9.5, 5.4, 3.0, W, is_horizontal=True)    # P2_XXB
    draw_window(16.5, 5.4, 2.0, W, is_horizontal=True)   # Stair Hall
    draw_window(21.5, 5.4, 2.0, W, is_horizontal=True)   # P2_LV6
    draw_window(26.5, 5.4, 2.0, W, is_horizontal=True)   # P2_LV7
    draw_window(31.5, 5.4, 2.0, W, is_horizontal=True)   # P2_LV8

    # South Facade Windows
    draw_window(1.5, -4.9 - W, 2.2, W, is_horizontal=True)    # P2_LV9
    draw_window(5.0, -4.9 - W, 2.2, W, is_horizontal=True)    # P2_LV9
    draw_window(10.25, -4.9 - W, 2.2, W, is_horizontal=True)  # P2_LV10
    draw_window(13.75, -4.9 - W, 2.2, W, is_horizontal=True)  # P2_LV10
    draw_window(19.0, -4.9 - W, 2.2, W, is_horizontal=True)   # P2_LV11
    draw_window(22.5, -4.9 - W, 2.2, W, is_horizontal=True)   # P2_LV11
    draw_window(27.75, -4.9 - W, 2.2, W, is_horizontal=True)  # P2_LV12
    draw_window(31.25, -4.9 - W, 2.2, W, is_horizontal=True)  # P2_LV12

    # Corridor End Windows (West and East)
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
        font_sz = r.get('font_size', 10.5)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                fontweight='bold', ha='center', va='center', zorder=15)

    ax.set_xlim(-3.0, 38.0)
    ax.set_ylim(-8.0, 8.5)

    out_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\DongNai\DongNai6\Tang2"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mat_bang_tang_2.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 2 đã xuất thành công tại: {out_path}")

if __name__ == "__main__":
    create_floorplan_tang2()
