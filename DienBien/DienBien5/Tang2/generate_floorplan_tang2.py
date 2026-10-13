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

def create_floorplan_tang2():
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 14), dpi=300)
    ax = fig.add_axes([0.02, 0.06, 0.96, 0.86])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_STAIR_FILL = '#ffffff'    # Pure white for staircase fill on Floor 2
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS
    X_MAX = 32.0           # Main building length = 32.0m
    Y_TOA2_TOP = 14.5      # Rear building height (top Y = 14.5m)

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 5 - Điện Biên', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.925, 0.925], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = -0.5, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 7.5, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 8.6, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 15.0, lg_x + 15.8], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 15.0, lg_x + 15.8], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 16.1, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Tòa 1 Horizontal Corridor (X: 0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Connecting Passage leading to Tòa 2 (X: 13.5 to 18.5, Y: 0.9 to 14.5)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, Y_TOA2_TOP - 0.9, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 2: 7 PHÒNG TÒA 1 + 2 PHÒNG TÒA 2)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA 1: DÃY PHÍA BẮC (Y: 0.9 đến 5.4m) ===
        # 1. Phòng Chánh án (KT: 10 x 6.6, 1 người)
        {
            'id': 'T2_CA', 'name': 'Phòng Chánh án',
            'x': 0.0, 'y': 0.9, 'w': 13.5, 'h': 4.5,
            'text_center': (6.75, 3.15),
            'door': (12.0, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        # 2. Phòng Kế toán (KT: 5 x 4.5, 1 người)
        {
            'id': 'T2_KT', 'name': 'Phòng kế toán',
            'x': 18.5, 'y': 0.9, 'w': 6.75, 'h': 4.5,
            'text_center': (21.875, 3.15),
            'door': (19.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 9.0
        },
        # 3. Phòng Thư ký (KT: 5 x 4.5, 1 người)
        {
            'id': 'T2_TK1', 'name': 'Phòng thư ký',
            'x': 25.25, 'y': 0.9, 'w': 6.75, 'h': 4.5,
            'text_center': (28.625, 3.15),
            'door': (26.2, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 9.0
        },

        # === TÒA 1: DÃY PHÍA NAM (Y: -4.9 đến -0.9m) ===
        # 4. Phòng Thư ký (KT: 4.5 x 3, 1 người)
        {
            'id': 'T2_TK2', 'name': 'Phòng thư ký',
            'x': 0.0, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (3.375, -2.9),
            'door': (5.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        # 5. Phòng Kho 1 (KT: 4.5 x 3)
        {
            'id': 'T2_KHO1', 'name': 'Phòng Kho 1',
            'x': 6.75, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (10.125, -2.9),
            'door': (12.0, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        # 6. Phòng Mạng (KT: 4.5 x 3 - Vị trí trung tâm mặt tiền Tầng 2)
        {
            'id': 'T2_MANG', 'name': 'Phòng mạng',
            'x': 13.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (16.0, -2.9),
            'door': (14.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
        # 7. Phòng Kho 2 (KT: 6.5 x 3)
        {
            'id': 'T2_KHO2', 'name': 'Phòng Kho 2',
            'x': 18.5, 'y': -4.9, 'w': 13.5, 'h': 4.0,
            'text_center': (25.25, -2.9),
            'door': (19.8, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 9.5
        },

        # === TÒA 2: MẶT SAU (Y: 6.2 đến 14.5m) ===
        # 8. Phòng nghị án 2 (KT: 6.5 x 3)
        {
            'id': 'T2_NA2', 'name': 'Phòng nghị án 2',
            'x': 3.5, 'y': 6.2, 'w': 10.0, 'h': Y_TOA2_TOP - 6.2,
            'text_center': (8.5, 10.35),
            'door': (13.5, 9.8, 0.9, 'W_IN_FROM_E'),
            'font_size': 10.0
        },
        # 9. Phòng giam phạm 2 (KT: 6.5 x 3)
        {
            'id': 'T2_GP2', 'name': 'Phòng giam phạm 2',
            'x': 18.5, 'y': 6.2, 'w': 10.0, 'h': Y_TOA2_TOP - 6.2,
            'text_center': (23.5, 10.35),
            'door': (18.5, 9.8, 0.9, 'E_IN_FROM_W'),
            'font_size': 10.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE (TẦNG 2: PURE WHITE STAIRCASE FILL)
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

    # Labels for Corridor
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.0, 7.5, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (WITH EXACT DOOR CUTOUTS & ENCLOSED CORRIDOR ENDS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Tòa 1 Exterior Side Walls (ENCLOSED AT X=0 AND X=32 FOR FLOOR 2)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)
    draw_wall(X_MAX, -4.9 - W, W, 10.3 + 2*W)

    # Tòa 1 North Top Wall (with opening for central passage at X: 13.5 to 18.5)
    draw_wall(-W, 5.4, 13.5 + W + P/2, W)
    draw_wall(18.5 - P/2, 5.4, (X_MAX - 18.5) + W + P/2, W)

    # Tòa 1 South Bottom Wall (CONTINUOUS WALL ACROSS FRONT FOR FLOOR 2, NO OPEN ENTRANCE)
    draw_wall(-W, -4.9 - W, X_MAX + 2*W, W)

    # Tòa 2 Exterior Walls (X: 3.5m to 28.5m, Y: 6.2m to 14.5m)
    draw_wall(3.5 - W, 6.2 - W, W, (Y_TOA2_TOP - 6.2) + 2*W)       # West outer wall
    draw_wall(28.5, 6.2 - W, W, (Y_TOA2_TOP - 6.2) + 2*W)          # East outer wall
    draw_wall(3.5 - W, Y_TOA2_TOP, 25.0 + 2*W, W)                 # North outer wall
    draw_wall(3.5 - W, 6.2 - W, 10.0 + W, W)                     # South outer wall West wing
    draw_wall(18.5, 6.2 - W, 10.0 + W, W)                        # South outer wall East wing

    # Tòa 2 Partition Walls separating central passage from rooms (door openings at Y: 9.8 to 10.7m)
    # Left partition at X = 13.5m:
    draw_wall(13.5 - P/2, 5.4, P, 4.4)                            # From Y=5.4 to 9.8m
    draw_wall(13.5 - P/2, 10.7, P, (Y_TOA2_TOP - 10.7))           # From Y=10.7 to 14.5m
    # Right partition at X = 18.5m:
    draw_wall(18.5 - P/2, 5.4, P, 4.4)                            # From Y=5.4 to 9.8m
    draw_wall(18.5 - P/2, 10.7, P, (Y_TOA2_TOP - 10.7))           # From Y=10.7 to 14.5m

    # Tòa 1 Corridor Wall Lines (Y = 0.9 & Y = -0.9) with door cutouts
    # North Corridor Line Y = 0.9:
    # Door 1 at 12.0 (size 0.9 -> 12.0 to 12.9)
    draw_wall(0.0, 0.9 - P/2, 12.0, P)
    draw_wall(12.9, 0.9 - P/2, 0.6, P)
    # Passage opening at 13.5 to 18.5
    # Door 2 at 19.5 (size 0.8 -> 19.5 to 20.3)
    draw_wall(18.5, 0.9 - P/2, 1.0, P)
    draw_wall(20.3, 0.9 - P/2, 5.9, P)
    # Door 3 at 26.2 (size 0.8 -> 26.2 to 27.0)
    draw_wall(27.0, 0.9 - P/2, (X_MAX - 27.0), P)

    # South Corridor Line Y = -0.9:
    # Door 4 at 5.5 (size 0.8 -> 5.5 to 6.3)
    draw_wall(0.0, -0.9 - P/2, 5.5, P)
    draw_wall(6.3, -0.9 - P/2, 5.7, P)
    # Door 5 at 12.0 (size 0.8 -> 12.0 to 12.8)
    draw_wall(12.8, -0.9 - P/2, 0.7, P)
    # Door 6 at 14.5 (size 0.8 -> 14.5 to 15.3)
    draw_wall(13.5, -0.9 - P/2, 1.0, P)
    draw_wall(15.3, -0.9 - P/2, 3.2, P)
    # Door 7 at 19.8 (size 0.9 -> 19.8 to 20.7)
    draw_wall(18.5, -0.9 - P/2, 1.3, P)
    draw_wall(20.7, -0.9 - P/2, (X_MAX - 20.7), P)

    # Tòa 1 Internal Vertical Partitions
    # North Wing:
    draw_wall(13.5 - P/2, 0.9, P, 4.5)     # West edge of stair hall
    draw_wall(18.5 - P/2, 0.9, P, 4.5)     # East edge of stair hall
    draw_wall(25.25 - P/2, 0.9, P, 4.5)    # Between Kế toán and Thư ký 1
    # South Wing:
    draw_wall(6.75 - P/2, -4.9, P, 4.0)     # Between Thư ký 2 and Kho 1
    draw_wall(13.5 - P/2, -4.9, P, 4.0)     # Between Kho 1 and Phòng Mạng
    draw_wall(18.5 - P/2, -4.9, P, 4.0)     # Between Phòng Mạng and Kho 2

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

    # Tòa 1 North Windows (Y = 5.4m)
    draw_window(3.5, 5.4, 3.0, W, is_horizontal=True)    # Chánh án 1
    draw_window(8.5, 5.4, 3.0, W, is_horizontal=True)    # Chánh án 2
    draw_window(20.5, 5.4, 2.5, W, is_horizontal=True)   # Kế toán
    draw_window(27.0, 5.4, 2.5, W, is_horizontal=True)   # Thư ký 1

    # Tòa 1 South Windows (Y = -4.9 - W)
    draw_window(2.2, -4.9 - W, 2.4, W, is_horizontal=True)   # Thư ký 2
    draw_window(8.8, -4.9 - W, 2.4, W, is_horizontal=True)   # Kho 1
    draw_window(14.8, -4.9 - W, 2.4, W, is_horizontal=True)  # Phòng Mạng (Central window)
    draw_window(21.5, -4.9 - W, 3.0, W, is_horizontal=True)  # Kho 2 window 1
    draw_window(26.5, -4.9 - W, 3.0, W, is_horizontal=True)  # Kho 2 window 2

    # Tòa 1 Corridor End Windows (East & West)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)

    # Tòa 2 Exterior Windows
    # North Windows (Y = 14.5m)
    draw_window(6.5, Y_TOA2_TOP, 3.5, W, is_horizontal=True)    # Nghị án 2 North
    draw_window(14.75, Y_TOA2_TOP, 2.5, W, is_horizontal=True)  # Central Passage End Window
    draw_window(21.5, Y_TOA2_TOP, 3.5, W, is_horizontal=True)   # Giam phạm 2 North

    # South Windows of Tòa 2 (Y = 6.2 - W)
    draw_window(6.5, 6.2 - W, 3.5, W, is_horizontal=True)     # Nghị án 2 South
    draw_window(21.5, 6.2 - W, 3.5, W, is_horizontal=True)    # Giam phạm 2 South

    # Side Windows of Tòa 2
    draw_window(3.5 - W, 7.5, W, 2.0, is_horizontal=False)     # Nghị án 2 West 1
    draw_window(3.5 - W, 11.2, W, 2.0, is_horizontal=False)    # Nghị án 2 West 2
    draw_window(28.5, 7.5, W, 2.0, is_horizontal=False)        # Giam phạm 2 East 1
    draw_window(28.5, 11.2, W, 2.0, is_horizontal=False)       # Giam phạm 2 East 2

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
        elif mode == 'W_IN_FROM_E':
            # Door at vertical wall X = 13.5, opens to West into Room
            ax.plot([x, x - size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'E_IN_FROM_W':
            # Door at vertical wall X = 18.5, opens to East into Room
            ax.plot([x, x + size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)

    for r in rooms:
        if r['door']:
            dx, dy, dsize, dmode = r['door']
            draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS (SINGLE-LINE LABELS, NO WRAPPING)
    # ---------------------------------------------------------
    for r in rooms:
        if r['name']:
            cx, cy = r['text_center']
            font_sz = r.get('font_size', 8.5)
            ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Canvas limits & padding
    ax.set_xlim(-2.0, 34.0)
    ax.set_ylim(-8.0, 16.5)

    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "mat_bang_tang_2.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 2 đã được xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang2()
