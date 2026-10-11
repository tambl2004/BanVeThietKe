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

def create_floorplan_tang1():
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
    COLOR_STAIR_FILL = '#eef4f7'    # Stair fill matching lobby color for floor 1

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Including Building Name, NO Subtitle line)
    fig.text(0.03, 0.955, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 5- Bắc Ninh', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Tòa 1 Horizontal Corridor (X: 0 to 20.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Front Main Lobby Space (X: 7.5 to 12.5, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((7.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Rear Stair & Passage Hall (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # CONNECTING DOORWAY PASSAGE BETWEEN TÒA 1 & TÒA 2 (X: 20.0 to 20.8, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((20.0, -0.9), 0.8, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 Fill: Tòa 2 has 1 room in North wing, rest of Tòa 2 is open CORRIDOR space per user instruction
    ax.add_patch(patches.Rectangle((20.8, -12.5), 8.0, 13.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (BẮC NINH 5 SURVEY DATA)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- TÒA 1 (TÒA CHÍNH - 9 ROOMS) ---
        # North Wing Rooms (Y: 0.9 to 5.4)
        {
            'id': 'P1_1', 'name': 'Phòng Chánh Án',
            'x': 0.0, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (1.875, 3.15),
            'door': (2.4, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_2', 'name': 'Phòng Thẩm Phán',
            'x': 3.75, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (5.625, 3.15),
            'door': (6.2, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_3', 'name': 'Phòng Phó Chánh Án',
            'x': 12.5, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (14.375, 3.15),
            'door': (13.0, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_4', 'name': 'Phòng Thẩm Phán',
            'x': 16.25, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (18.125, 3.15),
            'door': (16.8, 0.9, 0.8, 'N_IN_RIGHT')
        },

        # South Wing Rooms (Y: -4.9 to -0.9) - Note: X=7.5 to 12.5 is open SẢNH CHÍNH (Lobby)
        {
            'id': 'P1_5', 'name': 'Phòng Thẩm Phán',
            'x': 0.0, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (1.875, -2.9),
            'door': (2.4, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_6', 'name': 'Phòng Thẩm Phán',
            'x': 3.75, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (5.625, -2.9),
            'door': (4.5, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_7', 'name': 'Phòng Thẩm Phán',
            'x': 12.5, 'y': -4.9, 'w': 2.5, 'h': 4.0,
            'text_center': (13.75, -2.9),
            'door': (13.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_8', 'name': 'Phòng Thẩm Phán',
            'x': 15.0, 'y': -4.9, 'w': 2.5, 'h': 4.0,
            'text_center': (16.25, -2.9),
            'door': (15.5, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_9', 'name': 'Phòng Thẩm Phán',
            'x': 17.5, 'y': -4.9, 'w': 2.5, 'h': 4.0,
            'text_center': (18.75, -2.9),
            'door': (18.0, -0.9, 0.8, 'S_IN_RIGHT')
        },

        # --- TÒA 2 (TÒA PHỤ - 1 ROOM ONLY PER USER INSTRUCTION) ---
        {
            'id': 'P2_1', 'name': 'Phòng làm việc của phó Chánh án',
            'x': 20.8, 'y': 0.9, 'w': 8.0, 'h': 4.5,
            'text_center': (24.8, 3.15),
            'door': (23.8, 0.9, 0.8, 'N_IN_RIGHT')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS
    # ---------------------------------------------------------
    # --- 5.1 Central Staircase inside Tòa 1 North Hall ---
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Vertical divider line down center starting from step 2
    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Staircase label underneath box
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # --- 5.2 Tòa 2 Upper Right Staircase (X: 25.7 to 28.8, Y: -1.8 to 0.9) ---
    stair2_x, stair2_y, stair2_w, stair2_h = 25.7, -1.8, 3.1, 2.7
    stair2_bg = patches.Rectangle((stair2_x, stair2_y), stair2_w, stair2_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=3)
    ax.add_patch(stair2_bg)

    ax.plot([stair2_x, stair2_x + stair2_w], [stair2_y + stair2_h, stair2_y + stair2_h], color=COLOR_WALL, linewidth=1.1, zorder=4)
    ax.plot([stair2_x + stair2_w, stair2_x + stair2_w], [stair2_y, stair2_y + stair2_h], color=COLOR_WALL, linewidth=1.1, zorder=4)
    ax.plot([stair2_x, stair2_x + stair2_w], [stair2_y, stair2_y], color=COLOR_WALL, linewidth=1.1, zorder=4)

    for i in range(num_treads + 1):
        sy = stair2_y + i * (stair2_h / num_treads)
        ax.plot([stair2_x, stair2_x + stair2_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid2_x = stair2_x + stair2_w / 2.0
    ax.plot([mid2_x, mid2_x], [stair2_y, stair2_y + stair2_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair2_x + stair2_w / 2.0, stair2_y + stair2_h / 2.0, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=5)

    # 1. Tòa 1 Front Main Entrance Steps at Bottom (South: Y = -4.9 to -5.7)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # 2. Tòa 1 Rear Exit Steps at Top (North: Y = 5.4 to 6.2)
    for sy in [5.4, 5.56, 5.72, 5.88, 6.04, 6.20]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Outdoor Side Steps at Tòa 1 West Exit (X = 0.0)
    for i in range(5):
        dx = -0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Outdoor Entrance Steps at Tòa 2 South Exit (Y = -12.5 to -13.3)
    for sy in [-12.5, -12.66, -12.82, -12.98, -13.14, -13.30]:
        ax.plot([23.9, 25.7], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Labels for Lobby and Corridors
    ax.text(10.0, -2.9, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(24.8, -6.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', rotation=-90, zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Tòa 1 Outer Walls
    draw_wall(-W, -4.9 - W, W, 4.0 + W)
    draw_wall(-W, 0.9, W, 4.5 + W)

    draw_wall(20.0, -4.9 - W, W, 4.0 + W)
    draw_wall(20.0, 0.9, W, 4.5 + W)

    draw_wall(-W, 5.4, 7.5 + W + PART_THICKNESS/2, W)
    draw_wall(12.5 - PART_THICKNESS/2, 5.4, 7.5 + W + PART_THICKNESS/2, W)

    draw_wall(-W, -4.9 - W, 7.5 + W + PART_THICKNESS/2, W)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9 - W, 7.5 + W + PART_THICKNESS/2, W)

    # Tòa 1 Entrance / Exit Cheek Walls & Hooks
    draw_wall(7.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)
    draw_wall(12.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)

    draw_wall(7.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)
    draw_wall(12.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)
    draw_wall(7.5 - PART_THICKNESS/2, 6.2 - PART_THICKNESS, 0.5, PART_THICKNESS)
    draw_wall(12.5 + PART_THICKNESS/2 - 0.5, 6.2 - PART_THICKNESS, 0.5, PART_THICKNESS)

    # Tòa 1 Corridor Walls (Y = 0.9 & Y = -0.9)
    # North Corridor Wall Y = 0.9
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)
    draw_wall(3.2, 0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)
    draw_wall(7.0, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    draw_wall(12.5, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    draw_wall(13.8, 0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)
    draw_wall(17.6, 0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)

    # South Corridor Wall Y = -0.9 (NO WALL between 7.5 and 12.5 for open SẢNH CHÍNH)
    draw_wall(0, -0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)
    draw_wall(3.2, -0.9 - PART_THICKNESS/2, 1.3, PART_THICKNESS)
    draw_wall(5.3, -0.9 - PART_THICKNESS/2, 2.2, PART_THICKNESS)
    draw_wall(12.5, -0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    draw_wall(13.8, -0.9 - PART_THICKNESS/2, 1.7, PART_THICKNESS)
    draw_wall(16.3, -0.9 - PART_THICKNESS/2, 1.7, PART_THICKNESS)
    draw_wall(18.8, -0.9 - PART_THICKNESS/2, 1.2, PART_THICKNESS)

    # Tòa 1 Partitions
    draw_wall(3.75 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(7.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(12.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(16.25 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    draw_wall(3.75 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(7.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(15.0 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(17.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

    # Connecting Passage Walls
    draw_wall(20.0, 0.9 - PART_THICKNESS/2, 0.8, PART_THICKNESS)
    draw_wall(20.0, -0.9 - PART_THICKNESS/2, 0.8, PART_THICKNESS)

    # Tòa 2 Outer Walls
    draw_wall(20.8 - W, -12.5 - W, W, 11.6 + W)
    draw_wall(20.8 - W, 0.9, W, 4.5 + W)

    draw_wall(28.8, -12.5 - W, W, 17.9 + 2*W)
    draw_wall(20.8 - W, 5.4, 8.0 + 2*W, W)

    draw_wall(20.8 - W, -12.5 - W, 3.1 + W + PART_THICKNESS/2, W)
    draw_wall(25.7 - PART_THICKNESS/2, -12.5 - W, 3.1 + W + PART_THICKNESS/2, W)

    # Tòa 2 South Entrance Cheeks
    draw_wall(23.9 - PART_THICKNESS/2, -13.3, PART_THICKNESS, 0.8)
    draw_wall(25.7 - PART_THICKNESS/2, -13.3, PART_THICKNESS, 0.8)

    # Tòa 2 North Room Partition (Y = 0.9) with Door for P2_1
    draw_wall(20.8, 0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)
    draw_wall(24.6, 0.9 - PART_THICKNESS/2, 4.2, PART_THICKNESS)

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
    draw_window(1.0, 5.4, 1.6, W, is_horizontal=True)    # P1_1
    draw_window(4.8, 5.4, 1.6, W, is_horizontal=True)    # P1_2
    draw_window(13.5, 5.4, 1.6, W, is_horizontal=True)   # P1_3
    draw_window(17.3, 5.4, 1.6, W, is_horizontal=True)   # P1_4

    # Tòa 1 South Windows
    draw_window(1.0, -4.9 - W, 1.6, W, is_horizontal=True)  # P1_5
    draw_window(4.8, -4.9 - W, 1.6, W, is_horizontal=True)  # P1_6
    draw_window(13.1, -4.9 - W, 1.2, W, is_horizontal=True) # P1_7
    draw_window(15.6, -4.9 - W, 1.2, W, is_horizontal=True) # P1_8
    draw_window(18.1, -4.9 - W, 1.2, W, is_horizontal=True) # P1_9

    # Tòa 2 North Windows
    draw_window(22.8, 5.4, 4.0, W, is_horizontal=True)   # P2_1

    # Tòa 2 East Outer Windows
    draw_window(28.8, -6.0, W, 2.5, is_horizontal=False)

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
        font_sz = 8.5 if r['w'] <= 2.5 else 9.5
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.5, 31.5)
    ax.set_ylim(-16.0, 8.5)

    # Save target output in BacNinh/BacNinh5/Tang1
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\BacNinh\BacNinh5\Tang1"
    os.makedirs(target_dir, exist_ok=True)
    out_path = os.path.join(target_dir, "mat_bang_tang_1.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 1 floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang1()
