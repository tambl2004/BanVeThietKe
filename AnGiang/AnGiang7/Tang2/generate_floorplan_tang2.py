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
    COLOR_STAIR_FILL = '#ffffff'    # Pure white for upper floor stair boxes
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
    fig.text(0.03, 0.955, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 7 - An Giang', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.938, 0.938], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = -0.5, -15.2
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 7.5, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 8.6, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 15.0, lg_x + 15.8], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 15.0, lg_x + 15.8], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 16.1, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR BACKGROUND FILL (SEPARATE BUILDINGS ON UPPER FLOORS)
    # ---------------------------------------------------------
    # Tòa 1 Horizontal Corridor (X: 0.0 to 20.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Rear Stair Hall (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 Vertical Corridor (X: 23.9 to 25.7, Y: -12.5 to 0.9)
    ax.add_patch(patches.Rectangle((23.9, -12.5), 1.8, 13.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (AN GIANG 7 TẦNG 2 SURVEY DATA - 15 ROOMS TOTAL + TÒA 2 STAIR)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- TÒA 1 (TÒA CHÍNH - 10 ROOMS) ---
        # North Wing (4 rooms)
        {
            'id': 'P1_1', 'name': 'Phòng làm việc',
            'x': 0.0, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (1.875, 3.15),
            'door': (2.4, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_2', 'name': 'Phòng làm việc',
            'x': 3.75, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (5.625, 3.15),
            'door': (6.0, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_3', 'name': 'Phòng làm việc',
            'x': 12.5, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (14.375, 3.15),
            'door': (13.2, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_4', 'name': 'Phòng làm việc',
            'x': 16.25, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (18.125, 3.15),
            'door': (17.0, 0.9, 0.8, 'N_IN_RIGHT')
        },

        # South Wing (6 rooms including central enclosed room)
        {
            'id': 'P1_5', 'name': 'Phòng làm việc',
            'x': 0.0, 'y': -4.9, 'w': 2.5, 'h': 4.0,
            'text_center': (1.25, -2.9),
            'door': (1.2, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_6', 'name': 'Phòng làm việc',
            'x': 2.5, 'y': -4.9, 'w': 2.5, 'h': 4.0,
            'text_center': (3.75, -2.9),
            'door': (3.7, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_7', 'name': 'Phòng làm việc',
            'x': 5.0, 'y': -4.9, 'w': 2.5, 'h': 4.0,
            'text_center': (6.25, -2.9),
            'door': (6.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
        # Enclosed Central South Room (Floor 2 replaces open lobby)
        {
            'id': 'P1_8', 'name': 'Phòng làm việc',
            'x': 7.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (10.0, -2.9),
            'door': (11.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_9', 'name': 'Phòng làm việc',
            'x': 12.5, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (14.375, -2.9),
            'door': (13.2, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_10', 'name': 'Phòng làm việc',
            'x': 16.25, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (18.125, -2.9),
            'door': (17.0, -0.9, 0.8, 'S_IN_RIGHT')
        },

        # --- TÒA 2 (TÒA PHỤ - 5 ROOMS + 1 CẦU THANG) ---
        # 1. North Top Room
        {
            'id': 'P2_1', 'name': 'Phòng làm việc',
            'x': 20.8, 'y': 0.9, 'w': 8.0, 'h': 4.5,
            'text_center': (24.8, 3.15),
            'door': (23.8, 0.9, 0.8, 'N_IN_RIGHT')
        },
        # 2. Left Wing Upper (EXPANDED TO FILL UP TO Y=0.9)
        {
            'id': 'P2_2', 'name': 'Phòng làm việc',
            'x': 20.8, 'y': -6.7, 'w': 3.1, 'h': 7.6,
            'text_center': (22.35, -2.9),
            'door': (23.9, -1.0, 0.8, 'E_IN_UP')
        },
        # 3. Left Wing Lower
        {
            'id': 'P2_3', 'name': 'Phòng làm việc',
            'x': 20.8, 'y': -12.5, 'w': 3.1, 'h': 5.8,
            'text_center': (22.35, -9.6),
            'door': (23.9, -8.8, 0.8, 'E_IN_UP')
        },
        # 4. Right Wing Middle Room
        {
            'id': 'P2_4', 'name': 'Phòng làm việc',
            'x': 25.7, 'y': -7.2, 'w': 3.1, 'h': 5.4,
            'text_center': (27.25, -4.5),
            'door': (25.7, -3.5, 0.8, 'W_IN_UP')
        },
        # 5. Right Wing Lower Room
        {
            'id': 'P2_5', 'name': 'Phòng làm việc',
            'x': 25.7, 'y': -12.5, 'w': 3.1, 'h': 5.3,
            'text_center': (27.25, -9.8),
            'door': (25.7, -8.8, 0.8, 'W_IN_UP')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHICS (TÒA 1 & TÒA 2 STAIRS - PURE WHITE BACKGROUND)
    # ---------------------------------------------------------
    # --- 5.1 Tòa 1 Central Staircase ---
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

    # --- 5.2 Tòa 2 Upper Right Staircase (OPEN TO CORRIDOR - NO WALL AT X=25.7) ---
    stair2_x, stair2_y, stair2_w, stair2_h = 25.7, -1.8, 3.1, 2.7
    stair2_bg = patches.Rectangle((stair2_x, stair2_y), stair2_w, stair2_h, facecolor=COLOR_STAIR_FILL, edgecolor='none', zorder=3)
    ax.add_patch(stair2_bg)

    # Draw North, East, South outline of Tòa 2 Staircase box (Leaving West X=25.7 completely open)
    ax.plot([stair2_x, stair2_x + stair2_w], [stair2_y + stair2_h, stair2_y + stair2_h], color=COLOR_WALL, linewidth=1.1, zorder=4) # North wall
    ax.plot([stair2_x + stair2_w, stair2_x + stair2_w], [stair2_y, stair2_y + stair2_h], color=COLOR_WALL, linewidth=1.1, zorder=4) # East outer wall
    ax.plot([stair2_x, stair2_x + stair2_w], [stair2_y, stair2_y], color=COLOR_WALL, linewidth=1.1, zorder=4) # South partition wall

    for i in range(num_treads + 1):
        sy = stair2_y + i * (stair2_h / num_treads)
        ax.plot([stair2_x, stair2_x + stair2_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid2_x = stair2_x + stair2_w / 2.0
    ax.plot([mid2_x, mid2_x], [stair2_y, stair2_y + stair2_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair2_x + stair2_w / 2.0, stair2_y + stair2_h / 2.0, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (CLEAN WALL OPENINGS AT ALL DOORS & SEAMLESS JOINTS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # =========================================================
    # --- TÒA 1 (TÒA CHÍNH EXTERIOR WALLS & PARTITIONS) ---
    # =========================================================
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)                # West outer wall
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2*W)               # East outer wall (CLOSED on Floor 2)
    draw_wall(-W, 5.4, 20.0 + 2*W, W)                    # North outer top wall
    draw_wall(-W, -4.9 - W, 20.0 + 2*W, W)                 # South outer bottom wall

    # Tòa 1 Corridor Wall Lines (Y = 0.9 & Y = -0.9)
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)
    draw_wall(3.2, 0.9 - PART_THICKNESS/2, 2.8, PART_THICKNESS)
    draw_wall(6.8, 0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)
    draw_wall(12.5, 0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)
    draw_wall(14.0, 0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)
    draw_wall(17.8, 0.9 - PART_THICKNESS/2, 2.2, PART_THICKNESS)

    draw_wall(0.0, -0.9 - PART_THICKNESS/2, 1.2, PART_THICKNESS)
    draw_wall(2.0, -0.9 - PART_THICKNESS/2, 1.7, PART_THICKNESS)
    draw_wall(4.5, -0.9 - PART_THICKNESS/2, 1.5, PART_THICKNESS)
    draw_wall(6.8, -0.9 - PART_THICKNESS/2, 4.2, PART_THICKNESS)
    draw_wall(11.8, -0.9 - PART_THICKNESS/2, 1.4, PART_THICKNESS)
    draw_wall(14.0, -0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)
    draw_wall(17.8, -0.9 - PART_THICKNESS/2, 2.2, PART_THICKNESS)

    # Tòa 1 Internal Vertical Partitions
    draw_wall(3.75 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(7.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(12.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(16.25 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    draw_wall(2.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(5.0 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(7.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(16.25 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

    # =========================================================
    # --- TÒA 2 (TÒA PHỤ EXTERIOR WALLS & PARTITIONS) ---
    # =========================================================
    draw_wall(20.8 - W, -12.5 - W, W, 17.9 + 2*W)              # West outer wall (CLOSED on Floor 2)
    draw_wall(28.8, -12.5 - W, W, 17.9 + 2*W)                  # East outer wall of Tòa 2
    draw_wall(20.8 - W, 5.4, 8.0 + 2*W, W)                     # North top wall of Tòa 2
    draw_wall(20.8 - W, -12.5 - W, 8.0 + 2*W, W)               # South bottom wall of Tòa 2

    # Tòa 2 North Room South Partition (Y = 0.9) - SEAMLESS OVERLAP AT X=23.9
    draw_wall(20.8 - W, 0.9 - PART_THICKNESS/2, 3.0 + W + PART_THICKNESS/2, PART_THICKNESS)  # X: 20.8-W to 23.8+
    draw_wall(24.6 - PART_THICKNESS/2, 0.9 - PART_THICKNESS/2, 4.2 + W + PART_THICKNESS/2, PART_THICKNESS)  # X: 24.6- to 28.8+W

    # Tòa 2 Left Vertical Corridor Wall (X = 23.9) - PERFECTLY CONNECTED TO Y=0.9 WALL AT TOP
    draw_wall(23.9 - PART_THICKNESS/2, -0.2, PART_THICKNESS, 1.1 + PART_THICKNESS/2) # Y: -0.2 to 0.9+ (SEAMLESS T-JOINT)
    draw_wall(23.9 - PART_THICKNESS/2, -8.0, PART_THICKNESS, 7.0) # Y: -8.0 to -1.0
    draw_wall(23.9 - PART_THICKNESS/2, -12.5, PART_THICKNESS, 3.7)# Y: -12.5 to -8.8

    # Tòa 2 Right Vertical Corridor Wall (X = 25.7) - OPEN AT STAIRCASE (Y: -1.8 to 0.9)
    draw_wall(25.7 - PART_THICKNESS/2, -2.7, PART_THICKNESS, 0.9) # Y: -2.7 to -1.8 (Below staircase open entry)
    draw_wall(25.7 - PART_THICKNESS/2, -8.0, PART_THICKNESS, 4.5) # Y: -8.0 to -3.5
    draw_wall(25.7 - PART_THICKNESS/2, -12.5, PART_THICKNESS, 3.7)# Y: -12.5 to -8.8

    # Tòa 2 Horizontal Room Partitions
    draw_wall(20.8, -6.7 - PART_THICKNESS/2, 3.1, PART_THICKNESS) # P2_2 | P2_3
    draw_wall(25.7, -1.8 - PART_THICKNESS/2, 3.1 + W, PART_THICKNESS) # Staircase South Wall | P2_4
    draw_wall(25.7, -7.2 - PART_THICKNESS/2, 3.1 + W, PART_THICKNESS) # P2_4 | P2_5

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
    draw_window(1.0, 5.4, 1.8, W, is_horizontal=True)    # P1_1
    draw_window(4.8, 5.4, 1.8, W, is_horizontal=True)    # P1_2
    draw_window(13.5, 5.4, 1.8, W, is_horizontal=True)   # P1_3
    draw_window(17.2, 5.4, 1.8, W, is_horizontal=True)   # P1_4

    # Tòa 1 South Windows
    draw_window(0.5, -4.9 - W, 1.5, W, is_horizontal=True) # P1_5
    draw_window(3.0, -4.9 - W, 1.5, W, is_horizontal=True) # P1_6
    draw_window(5.5, -4.9 - W, 1.5, W, is_horizontal=True) # P1_7
    draw_window(9.0, -4.9 - W, 2.0, W, is_horizontal=True) # P1_8 (Center Room)
    draw_window(13.5, -4.9 - W, 1.8, W, is_horizontal=True)# P1_9
    draw_window(17.2, -4.9 - W, 1.8, W, is_horizontal=True)# P1_10

    # Tòa 1 West Corridor End Window & East End Window
    draw_window(-W, -0.5, W, 1.0, is_horizontal=False)
    draw_window(20.0, -0.5, W, 1.0, is_horizontal=False)

    # Tòa 2 North Windows
    draw_window(22.8, 5.4, 4.0, W, is_horizontal=True)   # P2_1

    # Tòa 2 East Outer Windows
    draw_window(28.8, -0.9, W, 1.2, is_horizontal=False) # Staircase Light Window
    draw_window(28.8, -4.8, W, 2.0, is_horizontal=False) # P2_4
    draw_window(28.8, -10.0, W, 2.0, is_horizontal=False)# P2_5

    # Tòa 2 South Corridor End Window
    draw_window(24.3, -12.5 - W, 1.0, W, is_horizontal=True)

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
        elif mode == 'E_IN_UP':
            ax.plot([x, x - size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'W_IN_UP':
            ax.plot([x, x + size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
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
        font_sz = 8.0 if r['w'] < 3.0 else 9.0
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Labels for Corridors
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(24.8, -5.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', rotation=-90, zorder=5)

    # Limits & Bounds
    ax.set_xlim(-2.5, 31.5)
    ax.set_ylim(-16.0, 8.5)

    # Save target output in AnGiang/AnGiang7/Tang2
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\AnGiang\AnGiang7\Tang2"
    os.makedirs(target_dir, exist_ok=True)
    out_path = os.path.join(target_dir, "mat_bang_tang_2.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated AnGiang7 Floor 2 floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang2()
