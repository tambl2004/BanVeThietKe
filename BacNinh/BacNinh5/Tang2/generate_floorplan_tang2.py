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
    fig = plt.figure(figsize=(24, 16), dpi=300)
    ax = fig.add_axes([0.02, 0.05, 0.96, 0.88])
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
    COLOR_STAIR_FILL = '#ffffff'    # Stair fill white for Floor 2

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Including Building Name, NO Subtitle line)
    fig.text(0.03, 0.955, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 5- Bắc Ninh', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.938, 0.938], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = -0.5, -15.2
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
    # 3. CORRIDOR BACKGROUND FILL (FLOOR 2 SEPARATE BUILDINGS)
    # ---------------------------------------------------------
    # Tòa 1 Horizontal Corridor (X: 0 to 20.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Rear Stair Hall Passage (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 Vertical Corridor (X: 24.8 to 28.8, Y: -12.5 to 5.4 - Extended to North Wall)
    ax.add_patch(patches.Rectangle((24.8, -12.5), 4.0, 17.9, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (BẮC NINH 5 FLOOR 2 SURVEY DATA)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- TÒA 1 (TÒA CHÍNH - 7 ROOMS) ---
        # North Wing Rooms (Y: 0.9 to 5.4)
        {
            'id': 'P1_1', 'name': 'Phòng làm việc\ncủa phó Chánh án',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'door': (6.2, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_2', 'name': 'Phòng làm việc\ncủa phó Chánh án',
            'x': 12.5, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (14.375, 3.15),
            'door': (13.0, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_3', 'name': 'Phòng làm việc\ncủa cán bộ',
            'x': 16.25, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (18.125, 3.15),
            'door': (16.8, 0.9, 0.8, 'N_IN_RIGHT')
        },

        # South Wing Rooms (Y: -4.9 to -0.9)
        {
            'id': 'P1_4', 'name': 'Phòng làm việc\ncủa cán bộ',
            'x': 0.0, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (1.875, -2.9),
            'door': (2.4, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_5', 'name': 'Phòng làm việc\ncủa cán bộ',
            'x': 3.75, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (5.625, -2.9),
            'door': (4.5, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_6', 'name': 'Phòng làm việc\ncủa cán bộ',
            'x': 7.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (10.0, -2.9),
            'door': (11.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_7', 'name': 'Phòng làm việc\ncủa cán bộ',
            'x': 12.5, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (16.25, -2.9),
            'door': (15.5, -0.9, 0.8, 'S_IN_RIGHT')
        },

        # --- TÒA 2 (TÒA PHỤ - 4 ROOMS) ---
        {
            'id': 'P2_1', 'name': 'Phòng làm việc\ncủa cán bộ',
            'x': 20.8, 'y': 0.9, 'w': 4.0, 'h': 4.5,
            'text_center': (22.8, 3.15),
            'door': (24.8, 2.5, 0.8, 'W_IN_UP')
        },
        {
            'id': 'P2_2', 'name': 'Phòng làm việc\ncủa cán bộ',
            'x': 20.8, 'y': -3.5, 'w': 4.0, 'h': 4.4,
            'text_center': (22.8, -1.3),
            'door': (24.8, -1.0, 0.8, 'W_IN_UP')
        },
        {
            'id': 'P2_3', 'name': 'Phòng làm việc\ncủa cán bộ',
            'x': 20.8, 'y': -7.9, 'w': 4.0, 'h': 4.4,
            'text_center': (22.8, -5.7),
            'door': (24.8, -5.0, 0.8, 'W_IN_UP')
        },
        {
            'id': 'P2_4', 'name': 'Phòng làm việc\ncủa Chánh án',
            'x': 20.8, 'y': -12.5, 'w': 8.0, 'h': 4.6,
            'text_center': (24.8, -10.2),
            'door': (25.5, -7.9, 0.8, 'S_IN_RIGHT')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE (WHITE BACKGROUND ON FLOOR 2)
    # ---------------------------------------------------------
    # --- 5.1 Central Staircase inside Tòa 1 North Hall ---
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Vertical divider line down center
    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Staircase label underneath box
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # --- 5.2 Tòa 2 Upper Right Staircase (X: 25.7 to 28.8, Y: -1.8 to 0.9) ---
    stair2_x, stair2_y, stair2_w, stair2_h = 25.7, -1.8, 3.1, 2.7
    stair2_bg = patches.Rectangle((stair2_x, stair2_y), stair2_w, stair2_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair2_bg)

    for i in range(num_treads + 1):
        sy = stair2_y + i * (stair2_h / num_treads)
        ax.plot([stair2_x, stair2_x + stair2_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid2_x = stair2_x + stair2_w / 2.0
    ax.plot([mid2_x, mid2_x], [stair2_y, stair2_y + stair2_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair2_x + stair2_w / 2.0, stair2_y + stair2_h / 2.0, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=5)

    # Labels for Corridors
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(26.8, -5.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', rotation=-90, zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (FLOOR 2 - CLOSED OUTER ENDS & NO PASSAGE)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Tòa 1 Outer Walls (West end X=0 closed, East end X=20 closed)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)   # West outer wall
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2*W)   # East outer wall (Closed gap to Tòa 2)

    draw_wall(-W, 5.4, 20.0 + 2*W, W)         # North outer wall
    draw_wall(-W, -4.9 - W, 20.0 + 2*W, W)    # South outer wall

    # Tòa 1 Corridor Walls (Y = 0.9 & Y = -0.9)
    # North Corridor Wall Y = 0.9
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 6.2, PART_THICKNESS)
    draw_wall(7.0, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    draw_wall(12.5, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    draw_wall(13.8, 0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)
    draw_wall(17.6, 0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)

    # South Corridor Wall Y = -0.9 (CLOSED ON FLOOR 2 WITH ROOM P1_6 AT CENTER)
    draw_wall(0, -0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)
    draw_wall(3.2, -0.9 - PART_THICKNESS/2, 1.3, PART_THICKNESS)
    draw_wall(5.3, -0.9 - PART_THICKNESS/2, 5.7, PART_THICKNESS) # Door for P1_6 at 11.0
    draw_wall(11.8, -0.9 - PART_THICKNESS/2, 3.7, PART_THICKNESS)
    draw_wall(16.3, -0.9 - PART_THICKNESS/2, 3.7, PART_THICKNESS)

    # Tòa 1 Partitions
    draw_wall(7.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(12.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(16.25 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    draw_wall(3.75 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(7.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

    # Tòa 2 Outer Walls (West side X=20.8 closed completely)
    draw_wall(20.8 - W, -12.5 - W, W, 17.9 + 2*W) # West wall of Tòa 2
    draw_wall(28.8, -12.5 - W, W, 17.9 + 2*W)     # East wall of Tòa 2
    draw_wall(20.8 - W, 5.4, 8.0 + 2*W, W)        # North wall of Tòa 2
    draw_wall(20.8 - W, -12.5 - W, 8.0 + 2*W, W)   # South wall of Tòa 2

    # Tòa 2 Internal Partitions (WITH DOOR OPENINGS CUT OUT)
    draw_wall(20.8, 0.9 - PART_THICKNESS/2, 4.0, PART_THICKNESS)   # Partition between P2_1 & P2_2 (X: 20.8 to 24.8)

    # Vertical partition X = 24.8 with openings for door 3 (-5.0), door 2 (-1.0), door 1 (2.5)
    draw_wall(24.8 - PART_THICKNESS/2, -7.9, PART_THICKNESS, 2.9)  # y: -7.9 to -5.0
    draw_wall(24.8 - PART_THICKNESS/2, -4.2, PART_THICKNESS, 3.2)  # y: -4.2 to -1.0
    draw_wall(24.8 - PART_THICKNESS/2, -0.2, PART_THICKNESS, 2.7)  # y: -0.2 to 2.5
    draw_wall(24.8 - PART_THICKNESS/2, 3.3, PART_THICKNESS, 2.1)   # y: 3.3 to 5.4

    draw_wall(20.8, -3.5 - PART_THICKNESS/2, 4.0, PART_THICKNESS)  # Partition between P2_2 & P2_3

    # Partition Y = -7.9 with opening for door 4 (x = 25.5)
    draw_wall(20.8, -7.9 - PART_THICKNESS/2, 4.7, PART_THICKNESS)  # x: 20.8 to 25.5
    draw_wall(26.3, -7.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)  # x: 26.3 to 28.8

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

    # Tòa 1 North Windows
    draw_window(2.5, 5.4, 2.5, W, is_horizontal=True)    # P1_1
    draw_window(13.5, 5.4, 1.6, W, is_horizontal=True)   # P1_2
    draw_window(17.3, 5.4, 1.6, W, is_horizontal=True)   # P1_3

    # Tòa 1 South Windows
    draw_window(1.0, -4.9 - W, 1.6, W, is_horizontal=True)  # P1_4
    draw_window(4.8, -4.9 - W, 1.6, W, is_horizontal=True)  # P1_5
    draw_window(8.75, -4.9 - W, 2.5, W, is_horizontal=True) # P1_6
    draw_window(15.0, -4.9 - W, 2.5, W, is_horizontal=True) # P1_7

    # Tòa 1 Outer End Windows (West X=0 & East X=20)
    draw_window(-W, -0.4, W, 0.8, is_horizontal=False)
    draw_window(20.0, -0.4, W, 0.8, is_horizontal=False)

    # Tòa 2 North & East Windows
    draw_window(21.8, 5.4, 2.0, W, is_horizontal=True)   # P2_1 North window
    draw_window(25.8, 5.4, 2.0, W, is_horizontal=True)   # Corridor North window
    draw_window(28.8, -5.7, W, 2.0, is_horizontal=False)  # P2_3 side window
    draw_window(28.8, -11.2, W, 2.0, is_horizontal=False) # P2_4 Chánh án East window (centered)
    draw_window(23.5, -12.5 - W, 2.5, W, is_horizontal=True) # P2_4 Chánh án South window

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
        elif mode == 'W_IN_UP':
            ax.plot([x, x - size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
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
        font_sz = 8.5 if r['w'] <= 3.75 else 9.5
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.5, 31.5)
    ax.set_ylim(-16.0, 8.5)

    # Save target output in BacNinh/BacNinh5/Tang2
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\BacNinh\BacNinh5\Tang2"
    os.makedirs(target_dir, exist_ok=True)
    out_path = os.path.join(target_dir, "mat_bang_tang_2.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 2 floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang2()
