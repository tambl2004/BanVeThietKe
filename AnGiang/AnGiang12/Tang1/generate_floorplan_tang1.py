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
    fig = plt.figure(figsize=(26, 15), dpi=300)
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

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Exact format per spec, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 12 - An Giang', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (3 DISTINCT BUILDINGS)
    # ---------------------------------------------------------
    # TÒA 1: Front Main Building Corridor (X: 0 to 27.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 27.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # TÒA 1: Front Main Lobby Space (X: 11.0 to 16.0, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((11.0, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # TÒA 1 -> TÒA 2: Rear Passage leading to Rear Courtroom Block (X: 11.0 to 16.0, Y: 0.9 to 6.2)
    ax.add_patch(patches.Rectangle((11.0, 0.9), 5.0, 5.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # TÒA 1 -> TÒA 3: Connecting Corridor (X: 27.0 to 29.5, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((27.0, -0.9), 2.5, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # TÒA 3: Side Building Corridor (X: 29.5 to 37.5, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((29.5, -0.9), 8.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (DISTRIBUTED ACROSS 3 BUILDING BLOCKS)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- TÒA 1: NORTH-WEST WING ---
        {
            'id': 'P1', 'name': 'Phòng làm việc 1',
            'x': 0.0, 'y': 0.9, 'w': 3.667, 'h': 4.5,
            'text_center': (1.8335, 3.15),
            'door': (0.5, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P2', 'name': 'Phòng làm việc 2',
            'x': 3.667, 'y': 0.9, 'w': 3.667, 'h': 4.5,
            'text_center': (5.5005, 3.15),
            'door': (4.167, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P3', 'name': 'Phòng làm việc 3',
            'x': 7.334, 'y': 0.9, 'w': 3.666, 'h': 4.5,
            'text_center': (9.167, 3.15),
            'door': (7.834, 0.9, 0.8, 'N_IN_RIGHT')
        },

        # --- TÒA 1: SOUTH-WEST WING ---
        {
            'id': 'P5', 'name': 'Phòng làm việc 5',
            'x': 0.0, 'y': -4.9, 'w': 5.5, 'h': 4.0,
            'text_center': (2.75, -2.9),
            'door': (0.8, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P6', 'name': 'Phòng làm việc 6',
            'x': 5.5, 'y': -4.9, 'w': 5.5, 'h': 4.0,
            'text_center': (8.25, -2.9),
            'door': (6.3, -0.9, 0.8, 'S_IN_RIGHT')
        },

        # --- TÒA 1: NORTH-EAST WING ---
        {
            'id': 'P4', 'name': 'Phòng làm việc 4',
            'x': 16.0, 'y': 0.9, 'w': 3.667, 'h': 4.5,
            'text_center': (17.8335, 3.15),
            'door': (16.5, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P7', 'name': 'Phòng làm việc 7',
            'x': 19.667, 'y': 0.9, 'w': 3.667, 'h': 4.5,
            'text_center': (21.5005, 3.15),
            'door': (20.167, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P8', 'name': 'Phòng làm việc 8',
            'x': 23.334, 'y': 0.9, 'w': 3.666, 'h': 4.5,
            'text_center': (25.167, 3.15),
            'door': (23.834, 0.9, 0.8, 'N_IN_RIGHT')
        },

        # --- TÒA 1: SOUTH-EAST WING ---
        {
            'id': 'P9', 'name': 'Phòng làm việc 9',
            'x': 16.0, 'y': -4.9, 'w': 11.0, 'h': 4.0,
            'text_center': (21.5, -2.9),
            'door': (16.5, -0.9, 0.8, 'S_IN_RIGHT')
        },

        # --- TÒA 2: REAR TRIAL BLOCK (1 SINGLE DOOR TO PHÒNG XỬ 1) ---
        {
            'id': 'PX1', 'name': 'Phòng xử 1',
            'x': 3.5, 'y': 6.2, 'w': 20.0, 'h': 7.0,
            'text_center': (13.5, 9.7),
            'door': (13.0, 6.2, 1.0, 'N_IN_RIGHT')  # Single clean entrance door
        },

        # --- TÒA 3: SIDE BUILDING BLOCK ---
        {
            'id': 'P15', 'name': 'Phòng làm việc 15',
            'x': 29.5, 'y': 0.9, 'w': 8.0, 'h': 4.5,
            'text_center': (33.5, 3.15),
            'door': (30.2, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P16', 'name': 'Phòng làm việc 16',
            'x': 29.5, 'y': -4.9, 'w': 8.0, 'h': 4.0,
            'text_center': (33.5, -2.9),
            'door': (30.2, -0.9, 0.8, 'S_IN_RIGHT')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE STEPS
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 12.2, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # Front Main Entrance Steps at Tòa 1 (South: Y = -4.9 to -5.7)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([11.0, 16.0], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Outdoor Side Steps at West Exit (X = 0) and Tòa 3 East Exit (X = 37.5)
    for i in range(5):
        dx = -0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    for i in range(5):
        dx = 37.5 + 0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([37.5, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([37.5, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Labels for Lobby and Corridor
    ax.text(13.5, -2.9, 'SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(5.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(21.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(33.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS FOR ALL 3 BUILDING BLOCKS (FIXED ALL 3 ISSUES)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # --- TÒA 1 EXTERIOR WALLS ---
    draw_wall(-W, -4.9 - W, W, 4.0 + W)   # West outer wall (South segment, stops at Y = -0.9)
    draw_wall(-W, 0.9, W, 4.5 + W)        # West outer wall (North segment, starts at Y = 0.9)
    
    draw_wall(27.0, -4.9 - W, W, 4.0 + W) # Tòa 1 East wall (South segment, stops exactly at Y = -0.9 - NO BLOCKING CORRIDOR!)
    draw_wall(27.0, 0.9, W, 4.5 + W)      # Tòa 1 East wall (North segment, starts exactly at Y = 0.9 - NO BLOCKING CORRIDOR!)

    # Tòa 1 North Top Wall (opening for central passage at X: 11.0 to 16.0)
    draw_wall(-W, 5.4, 11.0 + W + PART_THICKNESS/2, W)
    draw_wall(16.0 - PART_THICKNESS/2, 5.4, 11.0 + W + PART_THICKNESS/2, W)

    # Tòa 1 South Bottom Wall (opening for main front entrance at X: 11.0 to 16.0)
    draw_wall(-W, -4.9 - W, 11.0 + W + PART_THICKNESS/2, W)
    draw_wall(16.0 - PART_THICKNESS/2, -4.9 - W, 11.0 + W + PART_THICKNESS/2, W)

    # South Front Entrance Side Wall Cheeks
    draw_wall(11.0 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)
    draw_wall(16.0 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)

    # Passage Side Walls connecting Tòa 1 to Tòa 2 (Y: 5.4 to 6.2)
    draw_wall(11.0 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)
    draw_wall(16.0 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)

    # --- TÒA 2 (REAR COURTROOM BLOCK) EXTERIOR WALLS & SINGLE DOOR OPENING ---
    draw_wall(3.5 - W, 6.2 - W, W, 7.0 + 2*W)                     # West outer wall
    draw_wall(23.5, 6.2 - W, W, 7.0 + 2*W)                        # East outer wall
    draw_wall(3.5 - W, 13.2, 20.0 + 2*W, W)                      # North outer wall

    # Tòa 2 South Wall (Y = 6.2) with EXACTLY 1 CLEAN DOOR OPENING (X = 13.0 to 14.0)
    # Left segment: X = 3.5 - W to 13.0
    draw_wall(3.5 - W, 6.2 - W, (13.0 - (3.5 - W)), W)
    # Right segment: X = 14.0 to 23.5 + W
    draw_wall(14.0, 6.2 - W, ((23.5 + W) - 14.0), W)

    # --- TÒA 3 (SIDE BUILDING BLOCK) EXTERIOR WALLS ---
    draw_wall(29.5 - W, 0.9, W, 4.5 + W)                          # West wall (North segment, starts at Y = 0.9)
    draw_wall(29.5 - W, -4.9 - W, W, 4.0 + W)                     # West wall (South segment, stops at Y = -0.9)
    draw_wall(37.5, -4.9 - W, W, 4.0 + W)                         # East outer wall (South segment)
    draw_wall(37.5, 0.9, W, 4.5 + W)                              # East outer wall (North segment)
    draw_wall(29.5 - W, 5.4, 8.0 + 2*W, W)                       # North outer wall
    draw_wall(29.5 - W, -4.9 - W, 8.0 + 2*W, W)                   # South outer wall

    # --- CORRIDOR WALL LINES & CONNECTING CORRIDOR SOLID WALLS ---
    def draw_h_wall_with_doors(y_center, x_start, x_end, door_spans):
        cur_x = x_start
        for ds, de in sorted(door_spans):
            if ds > cur_x:
                draw_wall(cur_x, y_center - PART_THICKNESS/2, ds - cur_x, PART_THICKNESS)
            cur_x = max(cur_x, de)
        if cur_x < x_end:
            draw_wall(cur_x, y_center - PART_THICKNESS/2, x_end - cur_x, PART_THICKNESS)

    # Tòa 1 North Corridor Wall
    n_doors_t1_l = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == 0.9 and r['x'] < 11.0]
    draw_h_wall_with_doors(0.9, 0.0, 11.0, n_doors_t1_l)

    n_doors_t1_r = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == 0.9 and 16.0 <= r['x'] < 27.0]
    draw_h_wall_with_doors(0.9, 16.0, 27.0, n_doors_t1_r)

    # Tòa 1 South Corridor Wall
    s_doors_t1_l = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == -4.9 and r['x'] < 11.0]
    draw_h_wall_with_doors(-0.9, 0.0, 11.0, s_doors_t1_l)

    s_doors_t1_r = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == -4.9 and 16.0 <= r['x'] < 27.0]
    draw_h_wall_with_doors(-0.9, 16.0, 27.0, s_doors_t1_r)

    # CONNECTING CORRIDOR WALLS (X: 27.0 to 29.5) - SOLID CONTINUOUS WALLS ALONG TOP & BOTTOM!
    draw_wall(27.0, 0.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)
    draw_wall(27.0, -0.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)

    # Tòa 3 Corridor Walls (Y = 0.9 and Y = -0.9)
    n_doors_t3 = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == 0.9 and r['x'] >= 29.5]
    draw_h_wall_with_doors(0.9, 29.5, 37.5, n_doors_t3)

    s_doors_t3 = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == -4.9 and r['x'] >= 29.5]
    draw_h_wall_with_doors(-0.9, 29.5, 37.5, s_doors_t3)

    # Tòa 1 Vertical Partitions
    draw_wall(11.0 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)  # NW & Passage
    draw_wall(16.0 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)  # Passage & NE
    draw_wall(11.0 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0) # SW & Front Lobby
    draw_wall(16.0 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)# Front Lobby & SE

    draw_wall(3.667 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5) # NW P1 & P2
    draw_wall(7.334 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5) # NW P2 & P3
    draw_wall(5.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)  # SW P5 & P6

    draw_wall(19.667 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)# NE P4 & P7
    draw_wall(23.334 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)# NE P7 & P8

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

    # Tòa 1 & Tòa 3 Windows
    for r in rooms:
        if r['id'] == 'PX1':
            continue
        if r['y'] == 0.9: # North rooms -> window on Y = 5.4
            win_w = min(1.4, r['w'] * 0.45)
            win_x = r['x'] + (r['w'] - win_w) / 2.0
            draw_window(win_x, 5.4, win_w, W, is_horizontal=True)
        elif r['y'] == -4.9: # South rooms -> window on Y = -4.9 - W
            win_w = min(2.0, r['w'] * 0.45)
            win_x = r['x'] + (r['w'] - win_w) / 2.0
            draw_window(win_x, -4.9 - W, win_w, W, is_horizontal=True)

    # Tòa 2 (Rear Courtroom) Windows
    draw_window(7.0, 13.2, 3.0, W, is_horizontal=True)
    draw_window(17.0, 13.2, 3.0, W, is_horizontal=True)
    draw_window(3.5 - W, 8.5, W, 2.5, is_horizontal=False)
    draw_window(23.5, 8.5, W, 2.5, is_horizontal=False)

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode == 'N_IN_RIGHT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'N_IN_LEFT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
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
        if r['id'] == 'PX1':
            ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=14.0, fontweight='bold', ha='center', va='center', zorder=15)
        else:
            font_sz = 8.0 if r['w'] < 4.0 else 9.0
            ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 40.0)
    ax.set_ylim(-8.5, 15.0)

    # Output directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(script_dir, "mat_bang_tang_1.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 1 floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang1()
