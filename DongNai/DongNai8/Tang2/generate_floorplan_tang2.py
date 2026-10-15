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

COURT_NAME = "Tòa án nhân dân khu vực 8 - Đồng Nai"

def create_floorplan_tang2(court_name: str = COURT_NAME):
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
    X_MAX = 32.0            # Main building length = 32.0m
    Y_TOA2_TOP = 14.5       # Extended rear building height (top Y = 14.5m)
    Y_CORR2_BOT = 9.5       # Tòa 2 central horizontal corridor bottom Y
    Y_CORR2_TOP = 11.0      # Tòa 2 central horizontal corridor top Y

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

    # Legend Item 4: Door
    ax.plot([lg_x + 21.0, lg_x + 21.0], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 21.0, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 22.0, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Main Building Horizontal Corridor (X: 0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Central Vertical Passage leading to Tòa 2 (X: 13.5 to 18.5, Y: 0.9 to 14.5)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, Y_TOA2_TOP - 0.9, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 Central Horizontal Corridor (X: 3.5 to 28.5, Y: 9.5 to 11.0)
    ax.add_patch(patches.Rectangle((3.5, Y_CORR2_BOT), 25.0, Y_CORR2_TOP - Y_CORR2_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 2 - TÒA ÁN KHU VỰC 8 - ĐỒNG NAI)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA 1 (CHÍNH PHÍA NAM - 7 PHÒNG) ===
        # --- North Wing Tòa 1 (Y: 0.9 to 5.4m) ---
        {
            'id': 'P2_PH', 'name': 'Phòng họp',
            'x': 0.0, 'y': 0.9, 'w': 13.5, 'h': 4.5,
            'text_center': (6.75, 3.15),
            'door': (11.8, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'P2_CA', 'name': 'Phòng Chánh Án',
            'x': 18.5, 'y': 0.9, 'w': 6.75, 'h': 4.5,
            'text_center': (21.875, 3.15),
            'door': (19.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P2_PCA', 'name': 'Phòng Phó Chánh Án',
            'x': 25.25, 'y': 0.9, 'w': 6.75, 'h': 4.5,
            'text_center': (28.625, 3.15),
            'door': (26.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },

        # --- South Wing Tòa 1 (Y: -4.9 to -0.9m) ---
        {
            'id': 'P2_P1', 'name': 'Phòng số 1',
            'x': 0.0, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (3.375, -2.9),
            'door': (5.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P2_P2', 'name': 'Phòng số 2',
            'x': 6.75, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (10.125, -2.9),
            'door': (12.0, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P2_P3', 'name': 'Phòng số 3',
            'x': 13.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (16.0, -2.9),
            'door': (14.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P2_P4', 'name': 'Phòng số 4',
            'x': 18.5, 'y': -4.9, 'w': 13.5, 'h': 4.0,
            'text_center': (25.25, -2.9),
            'door': (19.5, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 9.5
        },

        # === TÒA 2 (MẶT SAU PHÍA BẮC - 5 PHÒNG) ===
        # --- North Wing Tòa 2 (Y: 11.0 to 14.5m) ---
        {
            'id': 'P2_P7', 'name': 'Phòng số 7',
            'x': 3.5, 'y': Y_CORR2_TOP, 'w': 5.0, 'h': Y_TOA2_TOP - Y_CORR2_TOP,
            'text_center': (6.0, 12.75),
            'door': (4.5, Y_CORR2_TOP, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P2_P8', 'name': 'Phòng số 8',
            'x': 8.5, 'y': Y_CORR2_TOP, 'w': 5.0, 'h': Y_TOA2_TOP - Y_CORR2_TOP,
            'text_center': (11.0, 12.75),
            'door': (9.5, Y_CORR2_TOP, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P2_P9', 'name': 'Phòng số 9',
            'x': 18.5, 'y': Y_CORR2_TOP, 'w': 10.0, 'h': Y_TOA2_TOP - Y_CORR2_TOP,
            'text_center': (23.5, 12.75),
            'door': (19.5, Y_CORR2_TOP, 0.9, 'N_IN_RIGHT'),
            'font_size': 8.5
        },

        # --- South Wing Tòa 2 (Y: 6.2 to 9.5m) ---
        {
            'id': 'P2_P10', 'name': 'Phòng số 10',
            'x': 3.5, 'y': 6.2, 'w': 10.0, 'h': Y_CORR2_BOT - 6.2,
            'text_center': (8.5, 7.85),
            'door': (4.5, Y_CORR2_BOT, 0.9, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P2_P11', 'name': 'Phòng số 11',
            'x': 18.5, 'y': 6.2, 'w': 10.0, 'h': Y_CORR2_BOT - 6.2,
            'text_center': (23.5, 7.85),
            'door': (19.5, Y_CORR2_BOT, 0.9, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
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

    # Labels for Corridor
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(8.5, 10.25, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(23.5, 10.25, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (EXACT ALIGNED SEGMENTS, NO GAPS OR OVERLAPS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Main Building Exterior Side Walls (Enclosed at ends X=0 and X=32 for Floor 2)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)
    draw_wall(X_MAX, -4.9 - W, W, 10.3 + 2*W)

    # Main Building North Top Wall (Y = 5.4)
    draw_wall(-W, 5.4, 13.5 + W + PART_THICKNESS/2, W)
    draw_wall(18.5 - PART_THICKNESS/2, 5.4, (X_MAX - 18.5) + W + PART_THICKNESS/2, W)

    # Main Building South Bottom Wall (Continuous wall at Y = -4.9 - W across the whole front for Floor 2)
    draw_wall(-W, -4.9 - W, X_MAX + 2*W, W)

    # Tòa 2 Connecting Passage Side Walls (OPEN at Corridor Y: 9.5 to 11.0m)
    # Left Wall at X = 13.5m:
    draw_wall(13.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 4.1)   # From Y=5.4 to 9.5m
    draw_wall(13.5 - PART_THICKNESS/2, 11.0, PART_THICKNESS, 3.5)  # From Y=11.0 to 14.5m
    
    # Right Wall at X = 18.5m:
    draw_wall(18.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 4.1)   # From Y=5.4 to 9.5m
    draw_wall(18.5 - PART_THICKNESS/2, 11.0, PART_THICKNESS, 3.5)  # From Y=11.0 to 14.5m

    # Tòa 2 Exterior Walls
    draw_wall(3.5 - W, 14.5, 25.0 + 2*W, W)                      # North outer wall
    
    # South outer wall of Tòa 2 (OPEN between X=13.5 and 18.5 for passage connecting Tòa 1 & Tòa 2)
    draw_wall(3.5 - W, 6.2 - W, 10.0 + W, W)                     # Left section under South-West room
    draw_wall(18.5, 6.2 - W, 10.0 + W, W)                        # Right section under South-East room

    draw_wall(3.5 - W, 6.2 - W, W, 8.3 + 2*W)                    # West outer wall
    draw_wall(28.5, 6.2 - W, W, 8.3 + 2*W)                      # East outer wall

    # Tòa 1 Corridor Wall Lines (Y = 0.9 & Y = -0.9) - PRECISION ALIGNED WITH DOOR OPENINGS
    # North Corridor Line Y = 0.9
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 11.8, PART_THICKNESS)
    draw_wall(12.7, 0.9 - PART_THICKNESS/2, 0.8, PART_THICKNESS)

    draw_wall(18.5, 0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(20.3, 0.9 - PART_THICKNESS/2, 4.95, PART_THICKNESS)
    draw_wall(26.05, 0.9 - PART_THICKNESS/2, 0.45, PART_THICKNESS)
    draw_wall(27.3, 0.9 - PART_THICKNESS/2, 4.7, PART_THICKNESS)

    # South Corridor Line Y = -0.9
    draw_wall(0.0, -0.9 - PART_THICKNESS/2, 5.5, PART_THICKNESS)
    draw_wall(6.3, -0.9 - PART_THICKNESS/2, 5.7, PART_THICKNESS)
    draw_wall(12.8, -0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)

    draw_wall(13.5, -0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(15.3, -0.9 - PART_THICKNESS/2, 3.2, PART_THICKNESS)

    draw_wall(18.5, -0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(20.4, -0.9 - PART_THICKNESS/2, 11.6, PART_THICKNESS)

    # Tòa 1 Internal Vertical Partitions
    draw_wall(13.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(18.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(25.25 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    draw_wall(6.75 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(13.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(18.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

    # Tòa 2 Corridor Wall Lines (Y = 11.0 & Y = 9.5)
    # North Corridor Line Y = 11.0
    draw_wall(3.5, 11.0 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(5.3, 11.0 - PART_THICKNESS/2, 4.2, PART_THICKNESS)
    draw_wall(10.3, 11.0 - PART_THICKNESS/2, 3.2, PART_THICKNESS)

    draw_wall(18.5, 11.0 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(20.4, 11.0 - PART_THICKNESS/2, 8.1, PART_THICKNESS)

    # South Corridor Line Y = 9.5
    draw_wall(3.5, 9.5 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(5.4, 9.5 - PART_THICKNESS/2, 8.1, PART_THICKNESS)

    draw_wall(18.5, 9.5 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(20.4, 9.5 - PART_THICKNESS/2, 8.1, PART_THICKNESS)

    # Tòa 2 Internal Vertical Partitions
    draw_wall(8.5 - PART_THICKNESS/2, 11.0, PART_THICKNESS, 3.5)

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

    # Tòa 1 Exterior Windows
    draw_window(5.0, 5.4, 3.5, W, is_horizontal=True)      # Phòng họp
    draw_window(20.5, 5.4, 2.0, W, is_horizontal=True)    # Phòng Chánh Án
    draw_window(27.5, 5.4, 2.0, W, is_horizontal=True)    # Phòng Phó Chánh Án

    draw_window(2.5, -4.9 - W, 2.0, W, is_horizontal=True)  # Phòng số 1
    draw_window(9.0, -4.9 - W, 2.0, W, is_horizontal=True)  # Phòng số 2
    draw_window(15.0, -4.9 - W, 2.0, W, is_horizontal=True) # Phòng số 3 (Central front room)
    draw_window(23.5, -4.9 - W, 3.5, W, is_horizontal=True) # Phòng số 4

    # Tòa 1 Corridor End Windows (East & West)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)

    # Tòa 1 Side Windows
    draw_window(-W, 2.5, W, 1.8, is_horizontal=False)      # Phòng họp West
    draw_window(-W, -3.5, W, 1.8, is_horizontal=False)     # Phòng số 1 West
    draw_window(X_MAX, 2.5, W, 1.8, is_horizontal=False)   # Phòng Phó Chánh Án East
    draw_window(X_MAX, -3.5, W, 1.8, is_horizontal=False)  # Phòng số 4 East

    # Tòa 2 Exterior Windows
    draw_window(5.0, 14.5, 1.8, W, is_horizontal=True)     # Phòng số 7
    draw_window(10.0, 14.5, 1.8, W, is_horizontal=True)    # Phòng số 8
    draw_window(15.0, 14.5, 2.0, W, is_horizontal=True)    # Central Rear Hall Window at Y=14.5m
    draw_window(22.5, 14.5, 3.0, W, is_horizontal=True)    # Phòng số 9

    draw_window(7.5, 6.2 - W, 3.0, W, is_horizontal=True)   # Phòng số 10
    draw_window(22.5, 6.2 - W, 3.0, W, is_horizontal=True)  # Phòng số 11

    # Tòa 2 Side Windows
    draw_window(3.5 - W, 12.0, W, 1.5, is_horizontal=False)  # Phòng số 7 West
    draw_window(3.5 - W, 7.0, W, 1.5, is_horizontal=False)   # Phòng số 10 West
    draw_window(28.5, 12.0, W, 1.5, is_horizontal=False)     # Phòng số 9 East
    draw_window(28.5, 7.0, W, 1.5, is_horizontal=False)      # Phòng số 11 East

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
        font_sz = r.get('font_size', 8.5)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 34.0)
    ax.set_ylim(-8.0, 16.5)

    # Output directory
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "mat_bang_tang_2.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang2()
