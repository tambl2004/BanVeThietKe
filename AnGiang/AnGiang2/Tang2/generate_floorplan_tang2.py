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

COURT_NAME = "Tòa án nhân dân khu vực 2 - An Giang"

def create_floorplan_tang2(court_name: str = COURT_NAME):
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 11), dpi=300)
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
    COLOR_STAIR_FILL = '#ffffff'    # Pure white stair fill for upper floors per Spec

    WALL_THICKNESS = 0.22  # 220mm thick exterior walls
    PART_THICKNESS = 0.08  # 80mm thin interior walls/partitions
    W = WALL_THICKNESS
    P = PART_THICKNESS
    X_MAX = 38.0           # Single Building Total Length = 38.0m
    X_LOBBY_L = 16.5       # Center Left X = 16.5m
    X_LOBBY_R = 21.5       # Center Right X = 21.5m

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, f'MẶT BẰNG TẦNG 2  —  {court_name}', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = 1.0, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

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
    # 3. CORRIDOR BACKGROUND FILL (ENCLOSED EXITS)
    # ---------------------------------------------------------
    # Main Horizontal Corridor (X: 0 to 38.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Central Stair Hall Space (X: 16.5 to 21.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((X_LOBBY_L, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 2 - 16 PHÒNG KHU VỰC 2 AN GIANG)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === DÃY PHÍA BẮC (North Wing: Y > 0.9m) ===
        # Cánh Tây Bắc (X: 0.0 to 16.5m)
        {
            # 1. Phòng chánh án (KT: 3,6 x 4,5, SL: 1)
            'id': 'T2_CA', 'name': 'Phòng chánh án',
            'x': 0.0, 'y': 0.9, 'w': 5.0, 'h': 4.5,
            'text_center': (2.5, 3.15),
            'door': (3.8, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            # 2. Phòng làm việc (KT: 3,6 x 4,5, SL: 2)
            'id': 'T2_LV1', 'name': 'Phòng làm việc',
            'x': 5.0, 'y': 0.9, 'w': 5.0, 'h': 4.5,
            'text_center': (7.5, 3.15),
            'door': (6.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            # 3. Phòng phó chánh án (KT: 7,2 x 3, SL: 2)
            'id': 'T2_PCA', 'name': 'Phòng phó chánh án',
            'x': 10.0, 'y': 0.9, 'w': 6.5, 'h': 4.5,
            'text_center': (13.25, 3.15),
            'door': (11.5, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },

        # Cánh Đông Bắc (X: 21.5 to 38.0m) - 4 phòng (KT: 4,8 x 3,1)
        {
            # 4. Phòng làm việc (KT: 4,8 x 3,1, SL: 2)
            'id': 'T2_LV2', 'name': 'Phòng làm việc',
            'x': 21.5, 'y': 0.9, 'w': 4.1, 'h': 4.5,
            'text_center': (23.55, 3.15),
            'door': (22.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 5. Phòng làm việc (KT: 4,8 x 3,1, SL: 2)
            'id': 'T2_LV3', 'name': 'Phòng làm việc',
            'x': 25.6, 'y': 0.9, 'w': 4.1, 'h': 4.5,
            'text_center': (27.65, 3.15),
            'door': (26.6, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 6. Phòng làm việc (KT: 4,8 x 3,1, SL: 2)
            'id': 'T2_LV4', 'name': 'Phòng làm việc',
            'x': 29.7, 'y': 0.9, 'w': 4.1, 'h': 4.5,
            'text_center': (31.75, 3.15),
            'door': (30.7, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 7. Phòng làm việc (KT: 4,8 x 3,1, SL: 2)
            'id': 'T2_LV5', 'name': 'Phòng làm việc',
            'x': 33.8, 'y': 0.9, 'w': 4.2, 'h': 4.5,
            'text_center': (35.9, 3.15),
            'door': (34.8, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 9.5
        },

        # === DÃY PHÍA NAM (South Wing: Y < -0.9m) ===
        # 9 phòng liên tục từ X: 0.0 đến 38.0m
        {
            # 8. Phòng làm việc (KT: 7,2 x 3, SL: 2)
            'id': 'T2_LV6', 'name': 'Phòng làm việc',
            'x': 0.0, 'y': -4.9, 'w': 4.2, 'h': 4.0,
            'text_center': (2.1, -2.9),
            'door': (2.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 9. Phòng làm việc (KT: 7,2 x 3, SL: 2)
            'id': 'T2_LV7', 'name': 'Phòng làm việc',
            'x': 4.2, 'y': -4.9, 'w': 4.2, 'h': 4.0,
            'text_center': (6.3, -2.9),
            'door': (5.2, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 10. Phòng làm việc (KT: 7,2 x 3, SL: 2)
            'id': 'T2_LV8', 'name': 'Phòng làm việc',
            'x': 8.4, 'y': -4.9, 'w': 4.2, 'h': 4.0,
            'text_center': (10.5, -2.9),
            'door': (9.4, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 11. Phòng làm việc (KT: 6,2 x 3,4, SL: 2)
            'id': 'T2_LV9', 'name': 'Phòng làm việc',
            'x': 12.6, 'y': -4.9, 'w': 4.2, 'h': 4.0,
            'text_center': (14.7, -2.9),
            'door': (13.6, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 12. Phòng làm việc (KT: 6,2 x 4,8, SL: 3)
            'id': 'T2_LV10', 'name': 'Phòng làm việc',
            'x': 16.8, 'y': -4.9, 'w': 4.4, 'h': 4.0,
            'text_center': (19.0, -2.9),
            'door': (17.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 13. Phòng làm việc (KT: 6,2 x 3,4, SL: 2)
            'id': 'T2_LV11', 'name': 'Phòng làm việc',
            'x': 21.2, 'y': -4.9, 'w': 4.2, 'h': 4.0,
            'text_center': (23.3, -2.9),
            'door': (22.2, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 14. Phòng làm việc (KT: 6 x 4, SL: 2)
            'id': 'T2_LV12', 'name': 'Phòng làm việc',
            'x': 25.4, 'y': -4.9, 'w': 4.2, 'h': 4.0,
            'text_center': (27.5, -2.9),
            'door': (26.4, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 15. Phòng làm việc (KT: 6 x 2, SL: 2)
            'id': 'T2_LV13', 'name': 'Phòng làm việc',
            'x': 29.6, 'y': -4.9, 'w': 4.2, 'h': 4.0,
            'text_center': (31.7, -2.9),
            'door': (30.6, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            # 16. Phòng làm việc (KT: 6 x 2, SL: 2)
            'id': 'T2_LV14', 'name': 'Phòng làm việc',
            'x': 33.8, 'y': -4.9, 'w': 4.2, 'h': 4.0,
            'text_center': (35.9, -2.9),
            'door': (34.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE (TẦNG 2: PURE WHITE STAIRCASE FILL PER SPEC)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 17.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, 
                                 facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Vertical line down center
    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Staircase label underneath box
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', 
            color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # Labels for Corridor
    ax.text(8.25, 0.0, 'HÀNH LANG', 
            color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(29.75, 0.0, 'HÀNH LANG', 
            color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (PRECISION STRUCTURAL WALLS & PARTITIONS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior West Wall (Continuous, fully enclosed at X = -W)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)

    # Exterior East Wall (Continuous, fully enclosed at X = X_MAX)
    draw_wall(X_MAX, -4.9 - W, W, 10.3 + 2*W)

    # Exterior North Wall (Continuous, fully enclosed at Y = 5.4m)
    draw_wall(-W, 5.4, X_MAX + 2*W, W)

    # Exterior South Wall (Continuous, fully enclosed at Y = -4.9m)
    draw_wall(-W, -4.9 - W, X_MAX + 2*W, W)

    # North Interior Room Partitions (Vertical walls between rooms)
    draw_wall(5.0 - P/2, 0.9, P, 4.5)
    draw_wall(10.0 - P/2, 0.9, P, 4.5)
    draw_wall(X_LOBBY_L - P/2, 0.9, P, 4.5)
    draw_wall(X_LOBBY_R - P/2, 0.9, P, 4.5)
    draw_wall(25.6 - P/2, 0.9, P, 4.5)
    draw_wall(29.7 - P/2, 0.9, P, 4.5)
    draw_wall(33.8 - P/2, 0.9, P, 4.5)

    # South Interior Room Partitions (Vertical walls between rooms)
    draw_wall(4.2 - P/2, -4.9, P, 4.0)
    draw_wall(8.4 - P/2, -4.9, P, 4.0)
    draw_wall(12.6 - P/2, -4.9, P, 4.0)
    draw_wall(16.8 - P/2, -4.9, P, 4.0)
    draw_wall(21.2 - P/2, -4.9, P, 4.0)
    draw_wall(25.4 - P/2, -4.9, P, 4.0)
    draw_wall(29.6 - P/2, -4.9, P, 4.0)
    draw_wall(33.8 - P/2, -4.9, P, 4.0)

    # ---------------------------------------------------------
    # 7. CORRIDOR WALLS WITH CLEAN DOOR CUTOUTS
    # ---------------------------------------------------------
    # North Corridor Wall at Y = 0.9 (from X=0 to 16.5, and 21.5 to 38.0)
    north_doors = [r['door'] for r in rooms if r['y'] > 0.0]
    # West North Corridor Wall (0.0 to 16.5)
    x_curr = 0.0
    for d in sorted([d for d in north_doors if d[0] < X_LOBBY_L], key=lambda item: item[0]):
        dx, dy, dw, _ = d
        if dx > x_curr:
            draw_wall(x_curr, 0.9 - P/2, dx - x_curr, P)
        x_curr = dx + dw
    if x_curr < X_LOBBY_L:
        draw_wall(x_curr, 0.9 - P/2, X_LOBBY_L - x_curr, P)

    # East North Corridor Wall (21.5 to 38.0)
    x_curr = X_LOBBY_R
    for d in sorted([d for d in north_doors if d[0] >= X_LOBBY_R], key=lambda item: item[0]):
        dx, dy, dw, _ = d
        if dx > x_curr:
            draw_wall(x_curr, 0.9 - P/2, dx - x_curr, P)
        x_curr = dx + dw
    if x_curr < X_MAX:
        draw_wall(x_curr, 0.9 - P/2, X_MAX - x_curr, P)

    # South Corridor Wall at Y = -0.9 (full length 0.0 to 38.0 on Tầng 2)
    south_doors = [r['door'] for r in rooms if r['y'] < 0.0]
    x_curr = 0.0
    for d in sorted(south_doors, key=lambda item: item[0]):
        dx, dy, dw, _ = d
        if dx > x_curr:
            draw_wall(x_curr, -0.9 - P/2, dx - x_curr, P)
        x_curr = dx + dw
    if x_curr < X_MAX:
        draw_wall(x_curr, -0.9 - P/2, X_MAX - x_curr, P)

    # ---------------------------------------------------------
    # 8. DOORS & DOOR SWING ARCS
    # ---------------------------------------------------------
    for r in rooms:
        dx, dy, dw, dtype = r['door']
        if dtype == 'N_IN_RIGHT':
            ax.plot([dx, dx], [dy, dy + dw], color=COLOR_DOOR_SWING, linewidth=1.2, zorder=12)
            arc = patches.Arc((dx, dy), 2*dw, 2*dw, angle=0, theta1=0, theta2=90, 
                              color=COLOR_DOOR_SWING, linewidth=0.9, linestyle='-', zorder=12)
            ax.add_patch(arc)
        elif dtype == 'S_IN_RIGHT':
            ax.plot([dx, dx], [dy, dy - dw], color=COLOR_DOOR_SWING, linewidth=1.2, zorder=12)
            arc = patches.Arc((dx, dy), 2*dw, 2*dw, angle=0, theta1=270, theta2=360, 
                              color=COLOR_DOOR_SWING, linewidth=0.9, linestyle='-', zorder=12)
            ax.add_patch(arc)

    # ---------------------------------------------------------
    # 9. WINDOWS (DOUBLE PARALLEL LINES ON EXTERIOR WALLS)
    # ---------------------------------------------------------
    def draw_window(x, y, w, h, is_horizontal=True):
        rect = patches.Rectangle((x, y), w, h, facecolor='#ffffff', edgecolor='none', zorder=15)
        ax.add_patch(rect)
        if is_horizontal:
            ax.plot([x, x + w], [y + h*0.25, y + h*0.25], color=COLOR_WALL, linewidth=1.2, zorder=16)
            ax.plot([x, x + w], [y + h*0.75, y + h*0.75], color=COLOR_WALL, linewidth=1.2, zorder=16)
        else:
            ax.plot([x + w*0.25, x + w*0.25], [y, y + h], color=COLOR_WALL, linewidth=1.2, zorder=16)
            ax.plot([x + w*0.75, x + w*0.75], [y, y + h], color=COLOR_WALL, linewidth=1.2, zorder=16)

    # North exterior windows
    draw_window(1.5, 5.4, 2.0, W)
    draw_window(6.5, 5.4, 2.0, W)
    draw_window(12.2, 5.4, 2.2, W)
    draw_window(22.5, 5.4, 2.0, W)
    draw_window(26.6, 5.4, 2.0, W)
    draw_window(30.7, 5.4, 2.0, W)
    draw_window(34.9, 5.4, 2.0, W)

    # South exterior windows (9 rooms)
    for x_room in [0.0, 4.2, 8.4, 12.6, 16.8, 21.2, 25.4, 29.6, 33.8]:
        draw_window(x_room + 1.1, -4.9 - W, 2.0, W)

    # East & West corridor end windows (Upper floors have corridor windows)
    draw_window(-W, -0.5, W, 1.0, is_horizontal=False)
    draw_window(X_MAX, -0.5, W, 1.0, is_horizontal=False)

    # East & West room side windows
    draw_window(-W, 2.25, W, 1.8, is_horizontal=False)
    draw_window(-W, -3.5, W, 1.8, is_horizontal=False)
    draw_window(X_MAX, 2.25, W, 1.8, is_horizontal=False)
    draw_window(X_MAX, -3.5, W, 1.8, is_horizontal=False)

    # ---------------------------------------------------------
    # 10. ROOM TEXT LABELS (CENTERED, DEEP NAVY, BOLD)
    # ---------------------------------------------------------
    for r in rooms:
        tx, ty = r['text_center']
        ax.text(tx, ty, r['name'], color=COLOR_TEXT_MAIN, 
                fontsize=r['font_size'], fontweight='bold', ha='center', va='center', zorder=20)

    # ---------------------------------------------------------
    # 11. EXPORT IMAGE (300 DPI, WHITE BACKGROUND)
    # ---------------------------------------------------------
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, 'mat_bang_tang_2.png')
    plt.savefig(out_path, dpi=300, facecolor='#ffffff', bbox_inches='tight')
    plt.close()
    print(f"Floorplan Tang 2 successfully generated at: {out_path}")

if __name__ == '__main__':
    create_floorplan_tang2()
