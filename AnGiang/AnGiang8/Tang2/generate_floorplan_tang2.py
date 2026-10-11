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

def create_floorplan_tang2():
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(20, 12), dpi=300)
    ax = fig.add_axes([0.02, 0.05, 0.96, 0.88])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_STAIR_FILL = '#ffffff'    # Pure white for upper floor stair box
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Including Building Name, NO Subtitle line)
    fig.text(0.03, 0.955, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 8 - An Giang', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.938, 0.938], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = -0.5, -7.2
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 6.0, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 7.1, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 12.0, lg_x + 12.8], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 12.0, lg_x + 12.8], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 13.1, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR BACKGROUND FILL
    # ---------------------------------------------------------
    # Tòa 1 Horizontal Corridor (X: 0.0 to 20.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Rear Stair Hall (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (AN GIANG 8 TẦNG 2 SURVEY DATA)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # North Wing (4 rooms)
        {
            'id': 'P1_5', 'name': 'Phòng số 5',
            'x': 0.0, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (1.875, 3.15),
            'door': (2.4, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_6', 'name': 'Phòng số 6',
            'x': 3.75, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (5.625, 3.15),
            'door': (6.0, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_7', 'name': 'Phòng số 7',
            'x': 12.5, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (14.375, 3.15),
            'door': (13.2, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_8', 'name': 'Phòng số 8',
            'x': 16.25, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (18.125, 3.15),
            'door': (17.0, 0.9, 0.8, 'N_IN_RIGHT')
        },

        # South Wing (5 rooms)
        {
            'id': 'P1_9', 'name': 'Phòng số 9',
            'x': 0.0, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (1.875, -2.9),
            'door': (2.4, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_10', 'name': 'Phòng làm việc',
            'x': 3.75, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (5.625, -2.9),
            'door': (6.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
        # Enclosed Central South Room (Floor 2 replaces open lobby)
        {
            'id': 'P1_CTR', 'name': 'Phòng làm việc',
            'x': 7.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (10.0, -2.9),
            'door': (11.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_11', 'name': 'Phòng làm việc',
            'x': 12.5, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (14.375, -2.9),
            'door': (13.2, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_12', 'name': 'Phòng làm việc',
            'x': 16.25, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (18.125, -2.9),
            'door': (17.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHICS (TÒA 1 STAIRS - PURE WHITE BACKGROUND)
    # ---------------------------------------------------------
    stair1_x, stair1_y, stair1_w, stair1_h = 8.7, 1.4, 2.6, 2.6
    stair1_bg = patches.Rectangle((stair1_x, stair1_y), stair1_w, stair1_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair1_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair1_y + i * (stair1_h / num_treads)
        ax.plot([stair1_x, stair1_x + stair1_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid1_x = stair1_x + stair1_w / 2.0
    ax.plot([mid1_x, mid1_x], [stair1_y, stair1_y + stair1_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair1_x + stair1_w / 2.0, stair1_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (CLEAN WALL OPENINGS AT ALL DOORS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior Wall Shell
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)                # West outer wall
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2*W)               # East outer wall
    draw_wall(-W, 5.4, 20.0 + 2*W, W)                    # North outer top wall
    draw_wall(-W, -4.9 - W, 20.0 + 2*W, W)                 # South outer bottom wall

    # Corridor Wall Lines (Y = 0.9 & Y = -0.9)
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)
    draw_wall(3.2, 0.9 - PART_THICKNESS/2, 2.8, PART_THICKNESS)
    draw_wall(6.8, 0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)
    draw_wall(12.5, 0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)
    draw_wall(14.0, 0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)
    draw_wall(17.8, 0.9 - PART_THICKNESS/2, 2.2, PART_THICKNESS)

    draw_wall(0.0, -0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)
    draw_wall(3.2, -0.9 - PART_THICKNESS/2, 2.8, PART_THICKNESS)
    draw_wall(6.8, -0.9 - PART_THICKNESS/2, 4.2, PART_THICKNESS)
    draw_wall(11.8, -0.9 - PART_THICKNESS/2, 1.4, PART_THICKNESS)
    draw_wall(14.0, -0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)
    draw_wall(17.8, -0.9 - PART_THICKNESS/2, 2.2, PART_THICKNESS)

    # Internal Vertical Partitions
    draw_wall(3.75 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(7.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(12.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(16.25 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    draw_wall(3.75 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(7.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(16.25 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

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

    # North Windows
    draw_window(1.0, 5.4, 1.8, W, is_horizontal=True)    # P1_5
    draw_window(4.8, 5.4, 1.8, W, is_horizontal=True)    # P1_6
    draw_window(13.5, 5.4, 1.8, W, is_horizontal=True)   # P1_7
    draw_window(17.2, 5.4, 1.8, W, is_horizontal=True)   # P1_8

    # South Windows
    draw_window(1.0, -4.9 - W, 1.8, W, is_horizontal=True) # P1_9
    draw_window(4.8, -4.9 - W, 1.8, W, is_horizontal=True) # P1_10
    draw_window(9.0, -4.9 - W, 2.0, W, is_horizontal=True) # P1_CTR (Center Room)
    draw_window(13.5, -4.9 - W, 1.8, W, is_horizontal=True)# P1_11
    draw_window(17.2, -4.9 - W, 1.8, W, is_horizontal=True)# P1_12

    # West & East Corridor End Windows
    draw_window(-W, -0.5, W, 1.0, is_horizontal=False)
    draw_window(20.0, -0.5, W, 1.0, is_horizontal=False)

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
    # 9. DRAW ROOM LABELS (FULL ROOM NAME FROM SURVEY DATA)
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = 9.0
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Labels for Corridor
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # Limits & Bounds
    ax.set_xlim(-2.5, 22.5)
    ax.set_ylim(-8.0, 8.5)

    # Save target output in AnGiang/AnGiang8/Tang2
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\AnGiang\AnGiang8\Tang2"
    os.makedirs(target_dir, exist_ok=True)
    out_path = os.path.join(target_dir, "mat_bang_tang_2.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated AnGiang8 Floor 2 floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang2()
