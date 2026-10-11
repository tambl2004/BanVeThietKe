import os
from typing import TypedDict, Tuple, List
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class RoomDict(TypedDict):
    id: str
    name: str
    sub: str
    x: float
    y: float
    w: float
    h: float
    text_center: Tuple[float, float]
    font_size: float

def create_floorplan_tang1(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_1.png')

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
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 stair fill matching lobby color

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.955, 'MẶT BẰNG TẦNG 1  —  TÒA ÁN NHÂN DÂN KHU VỰC 5 - CÀ MAU', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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

    # Legend Item 4: Door
    ax.plot([lg_x + 21.0, lg_x + 21.0], [lg_y + 0.02, lg_y + 0.28], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 21.0, lg_y + 0.02), 0.52, 0.52, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 22.1, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Tòa 1 Horizontal Corridor (X: 0.0 to 20.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Front Main Lobby Space (X: 7.5 to 12.5, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((7.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Rear Stair & Passage Hall (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Connecting Passage between Tòa 1 and Tòa 2 across 0.8m expansion joint (X: 20.0 to 20.8, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((20.0, -0.9), 0.8, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 Vertical Corridor (X: 20.8 to 22.6, Y: -12.5 to 5.4)
    ax.add_patch(patches.Rectangle((20.8, -12.5), 1.8, 17.9, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (ALL 10 ROOMS FROM SURVEY)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA 1 (6 PHÒNG) ===
        # --- North Wing Tòa 1 (Y: 0.9 to 5.4m) ---
        {
            'id': 'T1_P5', 'name': 'Phòng số 5', 'sub': '(KT: 5x3 | 4 ng)',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'font_size': 9.5
        },
        {
            'id': 'T1_P6', 'name': 'Phòng số 6', 'sub': '(KT: 6x3 | 1 ng)',
            'x': 12.5, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (16.25, 3.15),
            'font_size': 9.5
        },

        # --- South Wing Tòa 1 (Y: -4.9 to -0.9m) ---
        {
            'id': 'T1_P1', 'name': 'Phòng số 1', 'sub': '(KT: 5x3 | 1 ng)',
            'x': 0.0, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (1.875, -2.9),
            'font_size': 9.0
        },
        {
            'id': 'T1_P2', 'name': 'Phòng số 2', 'sub': '(KT: 5x3 | 1 ng)',
            'x': 3.75, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (5.625, -2.9),
            'font_size': 9.0
        },
        {
            'id': 'T1_P3', 'name': 'Phòng số 3', 'sub': '(KT: 5x3 | 1 ng)',
            'x': 12.5, 'y': -4.9, 'w': 4.0, 'h': 4.0,
            'text_center': (14.5, -2.9),
            'font_size': 9.0
        },
        {
            'id': 'T1_P4', 'name': 'Phòng số 4', 'sub': '(KT: 4x3 | 2 ng)',
            'x': 16.5, 'y': -4.9, 'w': 3.5, 'h': 4.0,
            'text_center': (18.25, -2.9),
            'font_size': 9.0
        },

        # === TÒA 2 (4 PHÒNG) ===
        # Along East side of Tòa 2 (X: 22.6 to 28.8m, W = 6.2m)
        {
            'id': 'T2_P11', 'name': 'Phòng số 11', 'sub': '(KT: 6x4 | 2 ng)',
            'x': 22.6, 'y': 0.9, 'w': 6.2, 'h': 4.5,
            'text_center': (25.7, 3.15),
            'font_size': 9.5
        },
        {
            'id': 'T2_P12', 'name': 'Phòng số 12', 'sub': '(KT: 6x4 | 2 ng)',
            'x': 22.6, 'y': -3.5, 'w': 6.2, 'h': 4.4,
            'text_center': (25.7, -1.3),
            'font_size': 9.5
        },
        {
            'id': 'T2_P13', 'name': 'Phòng số 13', 'sub': '(KT: 6x4 | 2 ng)',
            'x': 22.6, 'y': -8.0, 'w': 6.2, 'h': 4.5,
            'text_center': (25.7, -5.75),
            'font_size': 9.5
        },
        {
            'id': 'T2_P14', 'name': 'Phòng số 14', 'sub': '(KT: 6x4 | 1 ng)',
            'x': 22.6, 'y': -12.5, 'w': 6.2, 'h': 4.5,
            'text_center': (25.7, -10.25),
            'font_size': 9.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS (TÒA 1 ONLY)
    # ---------------------------------------------------------
    # Central Staircase inside Tòa 1 North Hall (Background matches sảnh fill COLOR_STAIR_FILL)
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
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
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.25, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='top', zorder=5)

    # 1. Tòa 1 Front Main Entrance Steps (South: Y = -4.9 to -5.7)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # 2. Tòa 1 Rear Exit Steps (North: Y = 5.4 to 6.2)
    for sy in [5.4, 5.56, 5.72, 5.88, 6.04, 6.20]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # 3. Outdoor Side Steps at West Exit of Tòa 1
    for i in range(5):
        dx = -0.22 * (i + 1)
        dy = 0.9 + i * 0.08
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Labels for Lobby and Corridors
    ax.text(10.0, -2.9, 'SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(21.7, -5.75, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', rotation=90, zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # ==========================
    # === TÒA 1 WALLS ===
    # ==========================
    # Leftmost Vertical Exterior Walls (Split for corridor opening Y: -0.9 to 0.9)
    draw_wall(-W, -4.9 - W, W, 4.0 + W)  # Bottom-left segment (Y: -4.9-W to -0.9)
    draw_wall(-W, 0.9, W, 4.5 + W)       # Top-left segment (Y: 0.9 to 5.4+W)

    # Tòa 1 North Wall (with opening for rear exit at X: 7.5 to 12.5)
    draw_wall(-W, 5.4, 7.5 + W + P/2, W)
    draw_wall(12.5 - P/2, 5.4, 7.5 + W + P/2, W)

    # Tòa 1 South Wall (with opening for main front entrance at X: 7.5 to 12.5)
    draw_wall(-W, -4.9 - W, 7.5 + W + P/2, W)
    draw_wall(12.5 - P/2, -4.9 - W, 7.5 + W + P/2, W)

    # Tòa 1 East Wall facing expansion joint (Y: -4.9 to -0.9 and Y: 0.9 to 5.4, corridor OPEN at -0.9 to 0.9)
    draw_wall(20.0, -4.9 - W, W, 4.0 + W)
    draw_wall(20.0, 0.9, W, 4.5 + W)

    # Tòa 1 Cheeks & Hooks
    # South Front Entrance Side Wall Cheeks (Y: -4.9 down to -5.7)
    draw_wall(7.5 - P/2, -5.7, P, 0.8)
    draw_wall(12.5 - P/2, -5.7, P, 0.8)

    # North Rear Exit Side Wall Cheeks (Y: 5.4 up to 6.2) & Top Inward Hooks
    draw_wall(7.5 - P/2, 5.4, P, 0.8)
    draw_wall(12.5 - P/2, 5.4, P, 0.8)
    # Top Inward Hooks at Y = 6.2 (0.5m)
    draw_wall(7.5 - P/2, 6.2 - P, 0.5, P)
    draw_wall(12.5 + P/2 - 0.5, 6.2 - P, 0.5, P)

    # Internal Vertical Partitions Tòa 1
    draw_wall(7.5 - P/2, 0.9, P, 4.5)   # Room 5 & Stair hall
    draw_wall(12.5 - P/2, 0.9, P, 4.5)  # Stair hall & Room 6

    draw_wall(3.75 - P/2, -4.9, P, 4.0) # Room 1 & Room 2
    draw_wall(7.5 - P/2, -4.9, P, 4.0)  # Room 2 & Front Lobby
    draw_wall(12.5 - P/2, -4.9, P, 4.0) # Front Lobby & Room 3
    draw_wall(16.5 - P/2, -4.9, P, 4.0) # Room 3 & Room 4

    # North Corridor Wall Line Tòa 1 (Y = 0.9)
    # Room 5: door 6.0 to 6.9
    draw_wall(0.0, 0.9 - P/2, 6.0, P)
    draw_wall(6.9, 0.9 - P/2, 0.6, P)
    # Stair Hall (X: 7.5 to 12.5) is open
    # Room 6: door 13.1 to 14.0
    draw_wall(12.5, 0.9 - P/2, 0.6, P)
    draw_wall(14.0, 0.9 - P/2, 6.0, P)

    # South Corridor Wall Line Tòa 1 (Y = -0.9)
    # Room 1: door 2.5 to 3.4
    draw_wall(0.0, -0.9 - P/2, 2.5, P)
    # Room 2: door 4.5 to 5.4
    draw_wall(3.4, -0.9 - P/2, 1.1, P)
    draw_wall(5.4, -0.9 - P/2, 2.1, P)
    # Front Lobby (X: 7.5 to 12.5) is open
    # Room 3: door 13.5 to 14.4
    draw_wall(12.5, -0.9 - P/2, 1.0, P)
    # Room 4: door 17.5 to 18.4
    draw_wall(14.4, -0.9 - P/2, 3.1, P)
    draw_wall(18.4, -0.9 - P/2, 1.6, P)

    # ==========================================
    # === CONNECTING PASSAGE (X: 20.0 to 20.8) ===
    # ==========================================
    # Closed horizontal edges of connecting bridge
    draw_wall(20.0, 0.9 - P/2, 0.8, P)
    draw_wall(20.0, -0.9 - P/2, 0.8, P)

    # ==========================
    # === TÒA 2 WALLS ===
    # ==========================
    # Tòa 2 Exterior Perimeter
    # North Wall (X: 20.8 to 28.8+W, Y = 5.4)
    draw_wall(20.8, 5.4, 8.0 + W, W)
    # South Wall (X: 20.8 to 28.8+W, Y = -12.5 - W)
    draw_wall(20.8, -12.5 - W, 8.0 + W, W)
    # East Exterior Wall (X = 28.8, Y: -12.5-W to 5.4+W)
    draw_wall(28.8, -12.5 - W, W, 17.9 + 2*W)
    # West Exterior Wall of Tòa 2 facing expansion joint & courtyard:
    # Top segment (Y: 0.9 to 5.4+W)
    draw_wall(20.8 - W, 0.9, W, 4.5 + W)
    # Bottom segment (Y: -12.5-W to -0.9)
    draw_wall(20.8 - W, -12.5 - W, W, 11.6 + W)

    # Tòa 2 Internal Horizontal Partitions between rooms (X: 22.6 to 28.8)
    draw_wall(22.6, 0.9 - P/2, 6.2, P)   # Room 11 & Room 12
    draw_wall(22.6, -3.5 - P/2, 6.2, P)  # Room 12 & Room 13
    draw_wall(22.6, -8.0 - P/2, 6.2, P)  # Room 13 & Room 14

    # Tòa 2 Vertical Corridor Partition Wall (X = 22.6, Y: -12.5 to 5.4) with Door Openings
    # Room 11: door Y: 1.5 to 2.4
    draw_wall(22.6 - P/2, 0.9, P, 0.6)
    draw_wall(22.6 - P/2, 2.4, P, 3.0)
    # Room 12: door Y: -1.0 to -0.1
    draw_wall(22.6 - P/2, -0.1, P, 1.0)
    draw_wall(22.6 - P/2, -3.5, P, 2.5)
    # Room 13: door Y: -5.5 to -4.6
    draw_wall(22.6 - P/2, -4.6, P, 1.1)
    draw_wall(22.6 - P/2, -8.0, P, 2.5)
    # Room 14: door Y: -10.0 to -9.1
    draw_wall(22.6 - P/2, -9.1, P, 1.1)
    draw_wall(22.6 - P/2, -12.5, P, 2.5)

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

    # Tòa 1 Windows
    # North
    draw_window(1.5, 5.4, 2.0, W, is_horizontal=True)    # Room 5 w1
    draw_window(4.5, 5.4, 2.0, W, is_horizontal=True)    # Room 5 w2
    draw_window(14.0, 5.4, 2.0, W, is_horizontal=True)   # Room 6 w1
    draw_window(17.0, 5.4, 2.0, W, is_horizontal=True)   # Room 6 w2
    # South
    draw_window(1.0, -4.9 - W, 1.6, W, is_horizontal=True)  # Room 1
    draw_window(4.8, -4.9 - W, 1.6, W, is_horizontal=True)  # Room 2
    draw_window(13.5, -4.9 - W, 1.8, W, is_horizontal=True) # Room 3
    draw_window(17.3, -4.9 - W, 1.6, W, is_horizontal=True) # Room 4
    # West Gable
    draw_window(-W, 2.0, W, 2.0, is_horizontal=False)   # Room 5 West
    draw_window(-W, -3.8, W, 2.0, is_horizontal=False)  # Room 1 West

    # Tòa 2 Windows
    # North facade
    draw_window(24.5, 5.4, 2.2, W, is_horizontal=True)  # Room 11 North
    # South facade
    draw_window(24.5, -12.5 - W, 2.2, W, is_horizontal=True) # Room 14 South
    draw_window(21.2, -12.5 - W, 1.0, W, is_horizontal=True) # Corridor South window
    # East Exterior facade
    draw_window(28.8, 2.0, W, 2.2, is_horizontal=False)   # Room 11 East
    draw_window(28.8, -2.4, W, 2.2, is_horizontal=False)  # Room 12 East
    draw_window(28.8, -6.9, W, 2.2, is_horizontal=False)  # Room 13 East
    draw_window(28.8, -11.4, W, 2.2, is_horizontal=False) # Room 14 East

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door_h(x1, x2, y, into='north', hinge='left'):
        size = x2 - x1
        if into == 'north':
            if hinge == 'left':
                ax.plot([x1, x1], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x1, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
            else: # hinge == 'right'
                ax.plot([x2, x2], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x2, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
        elif into == 'south':
            if hinge == 'left':
                ax.plot([x1, x1], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x1, y), size*2, size*2, angle=0, theta1=270, theta2=360,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
            else: # hinge == 'right'
                ax.plot([x2, x2], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x2, y), size*2, size*2, angle=0, theta1=180, theta2=270,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)

    def draw_door_v(x, y1, y2, into='east', hinge='bottom'):
        size = y2 - y1
        if into == 'east':
            if hinge == 'bottom':
                ax.plot([x, x + size], [y1, y1], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x, y1), size*2, size*2, angle=0, theta1=0, theta2=90,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
            else: # hinge == 'top'
                ax.plot([x, x + size], [y2, y2], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x, y2), size*2, size*2, angle=0, theta1=270, theta2=360,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)

    # Tòa 1 Doors
    draw_door_h(6.0, 6.9, 0.9, into='north', hinge='left')    # Room 5
    draw_door_h(13.1, 14.0, 0.9, into='north', hinge='right') # Room 6
    draw_door_h(2.5, 3.4, -0.9, into='south', hinge='right')  # Room 1
    draw_door_h(4.5, 5.4, -0.9, into='south', hinge='left')   # Room 2
    draw_door_h(13.5, 14.4, -0.9, into='south', hinge='right')# Room 3
    draw_door_h(17.5, 18.4, -0.9, into='south', hinge='left') # Room 4

    # Tòa 2 Doors (into East rooms)
    draw_door_v(22.6, 1.5, 2.4, into='east', hinge='bottom')  # Room 11
    draw_door_v(22.6, -1.0, -0.1, into='east', hinge='bottom')# Room 12
    draw_door_v(22.6, -5.5, -4.6, into='east', hinge='bottom')# Room 13
    draw_door_v(22.6, -10.0, -9.1, into='east', hinge='bottom')# Room 14

    # ---------------------------------------------------------
    # 9. ROOM LABELS & METADATA
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 9.0)
        # Main room name (bold)
        ax.text(cx, cy + 0.22, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)
        # Secondary info (sub)
        if r['sub']:
            ax.text(cx, cy - 0.28, r['sub'], color=COLOR_TEXT_MUTED, fontsize=font_sz * 0.85, ha='center', va='center', zorder=15)

    # ---------------------------------------------------------
    # 10. AXIS LIMITS & EXPORT
    # ---------------------------------------------------------
    ax.set_xlim(-2.5, 31.5)
    ax.set_ylim(-16.0, 8.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {out_img_path}")

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau5\Tang1"
    create_floorplan_tang1(target_dir)
