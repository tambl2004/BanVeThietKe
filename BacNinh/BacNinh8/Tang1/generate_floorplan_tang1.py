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

def create_floorplan_tang1():
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
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#eef4f7'    # Stair fill matching lobby color for floor 1

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    X_MAX = 32.0            # Main building length = 32.0m

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 8 - Bắc Ninh', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Main Building Horizontal Corridor (X: 0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Front Main Lobby Space (X: 13.5 to 18.5, Y: -5.7 to -0.9)
    ax.add_patch(patches.Rectangle((13.5, -5.7), 5.0, 4.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Passage & Exit Lobby (X: 13.5 to 18.5, Y: 0.9 to 6.2)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 5.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (BALANCED DISTRIBUTION BETWEEN NORTH & SOUTH WINGS)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- NORTH WING (Y: 0.9 to 5.4m) - 6 ROOMS TOTAL ---
        # North-West Wing (3 Rooms)
        {
            'id': 'P108', 'name': 'Phòng 108',
            'x': 0.0, 'y': 0.9, 'w': 6.75, 'h': 4.5,
            'text_center': (3.375, 3.15),
            'door': (5.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'P101', 'name': 'Phòng 101',
            'x': 6.75, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (8.4375, 3.15),
            'door': (8.8, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P103', 'name': 'Phòng 103',
            'x': 10.125, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (11.8125, 3.15),
            'door': (12.2, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },

        # North-East Wing (3 Rooms)
        {
            'id': 'PXETXU', 'name': 'Phòng xét xử',
            'x': 18.5, 'y': 0.9, 'w': 6.75, 'h': 4.5,
            'text_center': (21.875, 3.15),
            'door': (19.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'P102', 'name': 'Phòng 102',
            'x': 25.25, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (26.9375, 3.15),
            'door': (27.3, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P104', 'name': 'Phòng 104',
            'x': 28.625, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (30.3125, 3.15),
            'door': (30.7, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },

        # --- SOUTH WING (Y: -4.9 to -0.9m) - 8 ROOMS TOTAL ---
        # South-West Wing (4 Rooms)
        {
            'id': 'P105', 'name': 'Phòng 105',
            'x': 0.0, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (1.6875, -2.9),
            'door': (2.2, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P107', 'name': 'Phòng 107',
            'x': 3.375, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (5.0625, -2.9),
            'door': (5.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P109', 'name': 'Phòng 109',
            'x': 6.75, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (8.4375, -2.9),
            'door': (8.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P112', 'name': 'Phòng 112',
            'x': 10.125, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (11.8125, -2.9),
            'door': (12.2, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.0
        },

        # South-East Wing (4 Rooms)
        {
            'id': 'P114', 'name': 'Phòng 114',
            'x': 18.5, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (20.1875, -2.9),
            'door': (19.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P116', 'name': 'Phòng 116',
            'x': 21.875, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (23.5625, -2.9),
            'door': (22.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P118', 'name': 'Phòng 118',
            'x': 25.25, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (26.9375, -2.9),
            'door': (26.2, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P120', 'name': 'Phòng 120',
            'x': 28.625, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (30.3125, -2.9),
            'door': (29.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS (FLOOR 1 SPEC)
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

    # Front Main Entrance Steps at Bottom (South: Y = -4.9 to -5.7)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([13.5, 18.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([13.5, 13.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([18.5, 18.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # Rear Exit Steps at North (Y = 5.4 to 6.2) with 0.5m Inward Hooks
    for sy in [5.4, 5.56, 5.72, 5.88, 6.04, 6.20]:
        ax.plot([13.5, 18.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([13.5, 13.5], [5.4, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([18.5, 18.5], [5.4, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)
    # Inward hooks at Y = 6.20
    ax.plot([13.5, 14.0], [6.20, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([18.0, 18.5], [6.20, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # Outdoor Side Steps at Corridor Ends (East & West Exits)
    for i in range(5):
        dx = -0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    for i in range(5):
        dx = X_MAX + 0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([X_MAX, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([X_MAX, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Labels for Lobby and Corridor
    ax.text(16.0, -2.9, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (EXACT ALIGNED SEGMENTS, NO GAPS OR OVERLAPS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Main Building Exterior Side Walls (Open at Corridor Y: -0.9 to 0.9 for Floor 1)
    draw_wall(-W, -4.9 - W, W, 4.0 + W)
    draw_wall(-W, 0.9, W, 4.5 + W)
    draw_wall(X_MAX, -4.9 - W, W, 4.0 + W)
    draw_wall(X_MAX, 0.9, W, 4.5 + W)

    # Main Building North Top Wall
    draw_wall(-W, 5.4, 13.5 + W + PART_THICKNESS/2, W)
    draw_wall(18.5 - PART_THICKNESS/2, 5.4, (X_MAX - 18.5) + W + PART_THICKNESS/2, W)

    # Main Building South Bottom Wall
    draw_wall(-W, -4.9 - W, 13.5 + W + PART_THICKNESS/2, W)
    draw_wall(18.5 - PART_THICKNESS/2, -4.9 - W, (X_MAX - 18.5) + W + PART_THICKNESS/2, W)

    # Front Entrance Side Wall Cheeks
    draw_wall(13.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)
    draw_wall(18.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)

    # Rear Exit Side Wall Cheeks (Extend to Y=6.2m with 0.5m Inward Hooks)
    draw_wall(13.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)
    draw_wall(18.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)
    draw_wall(13.5, 6.2 - PART_THICKNESS, 0.5, PART_THICKNESS)
    draw_wall(18.0, 6.2 - PART_THICKNESS, 0.5, PART_THICKNESS)

    # North Corridor Line Y = 0.9 (Doors at X = 5.5, 8.8, 12.2, 19.5, 27.3, 30.7)
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 5.5, PART_THICKNESS)
    draw_wall(6.3, 0.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)
    draw_wall(9.6, 0.9 - PART_THICKNESS/2, 2.6, PART_THICKNESS)
    draw_wall(13.0, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)

    draw_wall(18.5, 0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(20.4, 0.9 - PART_THICKNESS/2, 6.9, PART_THICKNESS)
    draw_wall(28.1, 0.9 - PART_THICKNESS/2, 2.6, PART_THICKNESS)
    draw_wall(31.5, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)

    # South Corridor Line Y = -0.9 (Doors at X = 2.2, 5.5, 8.8, 12.2, 19.5, 22.8, 26.2, 29.5)
    draw_wall(0.0, -0.9 - PART_THICKNESS/2, 2.2, PART_THICKNESS)
    draw_wall(3.0, -0.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)
    draw_wall(6.3, -0.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)
    draw_wall(9.6, -0.9 - PART_THICKNESS/2, 2.6, PART_THICKNESS)
    draw_wall(13.0, -0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)

    draw_wall(18.5, -0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(20.3, -0.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)
    draw_wall(23.6, -0.9 - PART_THICKNESS/2, 2.6, PART_THICKNESS)
    draw_wall(27.0, -0.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)
    draw_wall(30.3, -0.9 - PART_THICKNESS/2, 1.7, PART_THICKNESS)

    # North Wing Vertical Partitions
    draw_wall(6.75 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(10.125 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(13.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(18.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(25.25 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(28.625 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    # South Wing Vertical Partitions
    draw_wall(3.375 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(6.75 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(10.125 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(13.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

    draw_wall(18.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(21.875 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(25.25 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(28.625 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

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

    # North Exterior Windows
    draw_window(2.375, 5.4, 2.0, W, is_horizontal=True)   # P108
    draw_window(7.9375, 5.4, 1.0, W, is_horizontal=True)  # P101
    draw_window(11.3125, 5.4, 1.0, W, is_horizontal=True) # P103

    draw_window(20.875, 5.4, 2.0, W, is_horizontal=True)  # Phòng xét xử
    draw_window(26.4375, 5.4, 1.0, W, is_horizontal=True) # P102
    draw_window(29.8125, 5.4, 1.0, W, is_horizontal=True) # P104

    # South Exterior Windows (1 window per room)
    for i in range(4):
        draw_window(1.1875 + i * 3.375, -4.9 - W, 1.0, W, is_horizontal=True)
    for i in range(4):
        draw_window(19.6875 + i * 3.375, -4.9 - W, 1.0, W, is_horizontal=True)

    # Side Windows
    draw_window(-W, 2.5, W, 1.5, is_horizontal=False)
    draw_window(-W, -3.2, W, 1.5, is_horizontal=False)
    draw_window(X_MAX, 2.5, W, 1.5, is_horizontal=False)
    draw_window(X_MAX, -3.2, W, 1.5, is_horizontal=False)

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
    # 9. DRAW ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 8.0)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 34.0)
    ax.set_ylim(-8.0, 8.5)

    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\BacNinh\BacNinh8\Tang1"
    os.makedirs(target_dir, exist_ok=True)
    out_path = os.path.join(target_dir, "mat_bang_tang_1.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {out_path}")

if __name__ == "__main__":
    create_floorplan_tang1()
