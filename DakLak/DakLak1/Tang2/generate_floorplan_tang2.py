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
    X_MAX = 32.0            # Main building length = 32.0m
    Y_TOA2_TOP = 14.5       # Extended rear building height (top Y = 14.5m)
    Y_CORR2_BOT = 9.5       # Tòa 2 central horizontal corridor bottom Y
    Y_CORR2_TOP = 11.0      # Tòa 2 central horizontal corridor top Y

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 1 - Đắk Lắk', 
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

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Main Building Horizontal Corridor (X: 0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Central Vertical Passage leading to Tòa 2 (X: 13.5 to 18.5, Y: 0.9 to 14.5)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, Y_TOA2_TOP - 0.9, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 Rear Block Central Horizontal Corridor (X: 3.5 to 28.5, Y: 9.5 to 11.0)
    ax.add_patch(patches.Rectangle((3.5, Y_CORR2_BOT), 25.0, Y_CORR2_TOP - Y_CORR2_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (19 ROOMS IN TÒA 1, 8 ROOMS IN TÒA 2)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA 1 (CHÍNH - 19 PHÒNG) ===
        # --- North Wing Cánh Tây (Y: 0.9 to 5.4m) : 5 phòng (P201 to P205) ---
        {
            'id': 'T1_P201', 'name': 'Phòng 201',
            'x': 0.0, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (1.35, 3.15),
            'door': (1.0, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P202', 'name': 'Phòng 202',
            'x': 2.7, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (4.05, 3.15),
            'door': (3.7, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P203', 'name': 'Phòng 203',
            'x': 5.4, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (6.75, 3.15),
            'door': (6.4, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P204', 'name': 'Phòng 204',
            'x': 8.1, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (9.45, 3.15),
            'door': (9.1, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P205', 'name': 'Phòng 205',
            'x': 10.8, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (12.15, 3.15),
            'door': (11.8, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 8.0
        },

        # --- North Wing Cánh Đông (Y: 0.9 to 5.4m) : 5 phòng (P206 to P210) ---
        {
            'id': 'T1_P206', 'name': 'Phòng 206',
            'x': 18.5, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (19.85, 3.15),
            'door': (19.5, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P207', 'name': 'Phòng 207',
            'x': 21.2, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (22.55, 3.15),
            'door': (22.2, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P208', 'name': 'Phòng 208',
            'x': 23.9, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (25.25, 3.15),
            'door': (24.9, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P209', 'name': 'Phòng 209',
            'x': 26.6, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (27.95, 3.15),
            'door': (27.6, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P210', 'name': 'Phòng 210',
            'x': 29.3, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (30.65, 3.15),
            'door': (30.3, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 8.0
        },

        # --- South Wing Cánh Tây (Y: -4.9 to -0.9m) : 4 phòng (P304, P211, P301, P302) ---
        {
            'id': 'T1_P304', 'name': 'Phòng 304 (Hội trường giao ban)',
            'x': 0.0, 'y': -4.9, 'w': 5.4, 'h': 4.0,
            'text_center': (2.7, -2.9),
            'door': (4.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 7.2
        },
        {
            'id': 'T1_P211', 'name': 'Phòng 211',
            'x': 5.4, 'y': -4.9, 'w': 2.7, 'h': 4.0,
            'text_center': (6.75, -2.9),
            'door': (6.4, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P301', 'name': 'Phòng 301',
            'x': 8.1, 'y': -4.9, 'w': 2.7, 'h': 4.0,
            'text_center': (9.45, -2.9),
            'door': (9.1, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P302', 'name': 'Phòng 302',
            'x': 10.8, 'y': -4.9, 'w': 2.7, 'h': 4.0,
            'text_center': (12.15, -2.9),
            'door': (11.8, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 8.0
        },

        # --- South Wing Trung tâm (X: 13.5 to 18.5m, Y: -4.9 to -0.9m) : 1 phòng ---
        {
            'id': 'T1_NGHIAN_2', 'name': 'Phòng nghị án tầng 2',
            'x': 13.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (16.0, -2.9),
            'door': (14.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },

        # --- South Wing Cánh Đông (Y: -4.9 to -0.9m) : 4 phòng (P303, P305, P306, P309) ---
        {
            'id': 'T1_P303', 'name': 'Phòng 303',
            'x': 18.5, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (20.1875, -2.9),
            'door': (19.5, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P305', 'name': 'Phòng 305',
            'x': 21.875, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (23.5625, -2.9),
            'door': (22.8, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P306', 'name': 'Phòng 306',
            'x': 25.25, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (26.9375, -2.9),
            'door': (26.2, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'T1_P309', 'name': 'Phòng 309',
            'x': 28.625, 'y': -4.9, 'w': 3.375, 'h': 4.0,
            'text_center': (30.3125, -2.9),
            'door': (29.5, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 8.0
        },

        # === TÒA 2 (MẶT SAU - 8 PHÒNG: 7 PHÒNG LÀM VIỆC + 1 PHÒNG HỌP) ===
        # --- North Row Rooms in Tòa 2 (Y: 11.0 to 14.5m) ---
        {
            'id': 'T2_N1', 'name': 'Phòng làm việc',
            'x': 3.5, 'y': Y_CORR2_TOP, 'w': 5.0, 'h': Y_TOA2_TOP - Y_CORR2_TOP,
            'text_center': (6.0, 12.75),
            'door': (4.5, Y_CORR2_TOP, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'T2_N2', 'name': 'Phòng làm việc',
            'x': 8.5, 'y': Y_CORR2_TOP, 'w': 5.0, 'h': Y_TOA2_TOP - Y_CORR2_TOP,
            'text_center': (11.0, 12.75),
            'door': (9.5, Y_CORR2_TOP, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'T2_N3', 'name': 'Phòng làm việc',
            'x': 18.5, 'y': Y_CORR2_TOP, 'w': 5.0, 'h': Y_TOA2_TOP - Y_CORR2_TOP,
            'text_center': (21.0, 12.75),
            'door': (19.5, Y_CORR2_TOP, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'T2_N4', 'name': 'Phòng họp',
            'x': 23.5, 'y': Y_CORR2_TOP, 'w': 5.0, 'h': Y_TOA2_TOP - Y_CORR2_TOP,
            'text_center': (26.0, 12.75),
            'door': (24.5, Y_CORR2_TOP, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },

        # --- South Row Rooms in Tòa 2 (Y: 6.2 to 9.5m) ---
        {
            'id': 'T2_S1', 'name': 'Phòng làm việc',
            'x': 3.5, 'y': 6.2, 'w': 5.0, 'h': Y_CORR2_BOT - 6.2,
            'text_center': (6.0, 7.85),
            'door': (4.5, Y_CORR2_BOT, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'T2_S2', 'name': 'Phòng làm việc',
            'x': 8.5, 'y': 6.2, 'w': 5.0, 'h': Y_CORR2_BOT - 6.2,
            'text_center': (11.0, 7.85),
            'door': (9.5, Y_CORR2_BOT, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'T2_S3', 'name': 'Phòng làm việc',
            'x': 18.5, 'y': 6.2, 'w': 5.0, 'h': Y_CORR2_BOT - 6.2,
            'text_center': (21.0, 7.85),
            'door': (19.5, Y_CORR2_BOT, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'T2_S4', 'name': 'Phòng làm việc',
            'x': 23.5, 'y': 6.2, 'w': 5.0, 'h': Y_CORR2_BOT - 6.2,
            'text_center': (26.0, 7.85),
            'door': (24.5, Y_CORR2_BOT, 0.8, 'S_IN_RIGHT'),
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
    draw_wall(-W, 5.4, 13.5 + W + P/2, W)
    draw_wall(18.5 - P/2, 5.4, (X_MAX - 18.5) + W + P/2, W)

    # Main Building South Bottom Wall (Continuous wall across the whole front for Floor 2)
    draw_wall(-W, -4.9 - W, X_MAX + 2*W, W)

    # Tòa 2 Connecting Passage Side Walls (OPEN at Corridor Y: 9.5 to 11.0m)
    draw_wall(13.5 - P/2, 5.4, P, 4.1)   # From Y=5.4 to 9.5m
    draw_wall(13.5 - P/2, 11.0, P, 3.5)  # From Y=11.0 to 14.5m
    draw_wall(18.5 - P/2, 5.4, P, 4.1)   # From Y=5.4 to 9.5m
    draw_wall(18.5 - P/2, 11.0, P, 3.5)  # From Y=11.0 to 14.5m

    # Tòa 2 Exterior Walls
    draw_wall(3.5 - W, 14.5, 25.0 + 2*W, W)                      # North outer wall
    draw_wall(3.5 - W, 6.2 - W, 10.0 + W, W)                     # Left South outer wall
    draw_wall(18.5, 6.2 - W, 10.0 + W, W)                        # Right South outer wall
    draw_wall(3.5 - W, 6.2 - W, W, 8.3 + 2*W)                    # West outer wall
    draw_wall(28.5, 6.2 - W, W, 8.3 + 2*W)                      # East outer wall

    # Tòa 1 Corridor Wall Lines (Y = 0.9 & Y = -0.9) - ALIGNED WITH DOOR OPENINGS
    # North Corridor Line Y = 0.9 Cánh Tây (P201 to P205 doors at 1.0, 3.7, 6.4, 9.1, 11.8)
    draw_wall(0.0, 0.9 - P/2, 1.0, P)
    draw_wall(1.75, 0.9 - P/2, 1.95, P)
    draw_wall(4.45, 0.9 - P/2, 1.95, P)
    draw_wall(7.15, 0.9 - P/2, 1.95, P)
    draw_wall(9.85, 0.9 - P/2, 1.95, P)
    draw_wall(12.55, 0.9 - P/2, 0.95, P)

    # North Corridor Line Y = 0.9 Cánh Đông (P206 to P210 doors at 19.5, 22.2, 24.9, 27.6, 30.3)
    draw_wall(18.5, 0.9 - P/2, 1.0, P)
    draw_wall(20.25, 0.9 - P/2, 1.95, P)
    draw_wall(22.95, 0.9 - P/2, 1.95, P)
    draw_wall(25.65, 0.9 - P/2, 1.95, P)
    draw_wall(28.35, 0.9 - P/2, 1.95, P)
    draw_wall(31.05, 0.9 - P/2, 0.95, P)

    # South Corridor Line Y = -0.9 Cánh Tây (P304 door at 4.2, P211 at 6.4, P301 at 9.1, P302 at 11.8)
    draw_wall(0.0, -0.9 - P/2, 4.2, P)
    draw_wall(5.05, -0.9 - P/2, 1.35, P)
    draw_wall(7.15, -0.9 - P/2, 1.95, P)
    draw_wall(9.85, -0.9 - P/2, 1.95, P)
    draw_wall(12.55, -0.9 - P/2, 0.95, P)

    # South Corridor Line Y = -0.9 Trung tâm (Phòng nghị án 2 door at 14.5)
    draw_wall(13.5, -0.9 - P/2, 1.0, P)
    draw_wall(15.3, -0.9 - P/2, 3.2, P)

    # South Corridor Line Y = -0.9 Cánh Đông (P303 at 19.5, P305 at 22.8, P306 at 26.2, P309 at 29.5)
    draw_wall(18.5, -0.9 - P/2, 1.0, P)
    draw_wall(20.25, -0.9 - P/2, 2.55, P)
    draw_wall(23.55, -0.9 - P/2, 2.65, P)
    draw_wall(26.95, -0.9 - P/2, 2.55, P)
    draw_wall(30.25, -0.9 - P/2, 1.75, P)

    # Tòa 1 Internal Vertical Partitions
    # North Wing Partitions
    draw_wall(2.7 - P/2, 0.9, P, 4.5)
    draw_wall(5.4 - P/2, 0.9, P, 4.5)
    draw_wall(8.1 - P/2, 0.9, P, 4.5)
    draw_wall(10.8 - P/2, 0.9, P, 4.5)
    draw_wall(13.5 - P/2, 0.9, P, 4.5)

    draw_wall(18.5 - P/2, 0.9, P, 4.5)
    draw_wall(21.2 - P/2, 0.9, P, 4.5)
    draw_wall(23.9 - P/2, 0.9, P, 4.5)
    draw_wall(26.6 - P/2, 0.9, P, 4.5)
    draw_wall(29.3 - P/2, 0.9, P, 4.5)

    # South Wing Partitions
    draw_wall(5.4 - P/2, -4.9, P, 4.0)
    draw_wall(8.1 - P/2, -4.9, P, 4.0)
    draw_wall(10.8 - P/2, -4.9, P, 4.0)
    draw_wall(13.5 - P/2, -4.9, P, 4.0)
    draw_wall(18.5 - P/2, -4.9, P, 4.0)
    draw_wall(21.875 - P/2, -4.9, P, 4.0)
    draw_wall(25.25 - P/2, -4.9, P, 4.0)
    draw_wall(28.625 - P/2, -4.9, P, 4.0)

    # Tòa 2 Corridor Wall Lines (Y = 11.0 & Y = 9.5)
    # North Corridor Line Y = 11.0
    draw_wall(3.5, 11.0 - P/2, 1.0, P)
    draw_wall(5.3, 11.0 - P/2, 4.2, P)
    draw_wall(10.3, 11.0 - P/2, 3.2, P)
    draw_wall(18.5, 11.0 - P/2, 1.0, P)
    draw_wall(20.3, 11.0 - P/2, 4.2, P)
    draw_wall(25.3, 11.0 - P/2, 3.2, P)

    # South Corridor Line Y = 9.5
    draw_wall(3.5, 9.5 - P/2, 1.0, P)
    draw_wall(5.3, 9.5 - P/2, 4.2, P)
    draw_wall(10.3, 9.5 - P/2, 3.2, P)
    draw_wall(18.5, 9.5 - P/2, 1.0, P)
    draw_wall(20.3, 9.5 - P/2, 4.2, P)
    draw_wall(25.3, 9.5 - P/2, 3.2, P)

    # Tòa 2 Internal Vertical Partitions
    draw_wall(8.5 - P/2, 11.0, P, 3.5)
    draw_wall(13.5 - P/2, 11.0, P, 3.5)
    draw_wall(18.5 - P/2, 11.0, P, 3.5)
    draw_wall(23.5 - P/2, 11.0, P, 3.5)

    draw_wall(8.5 - P/2, 6.2, P, 3.3)
    draw_wall(13.5 - P/2, 6.2, P, 3.3)
    draw_wall(18.5 - P/2, 6.2, P, 3.3)
    draw_wall(23.5 - P/2, 6.2, P, 3.3)

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

    # Tòa 1 North Exterior Windows
    for wx in [0.7, 3.4, 6.1, 8.8, 11.5]:
        draw_window(wx, 5.4, 1.3, W, is_horizontal=True)
    for wx in [19.2, 21.9, 24.6, 27.3, 30.0]:
        draw_window(wx, 5.4, 1.3, W, is_horizontal=True)

    # Tòa 1 South Exterior Windows
    draw_window(1.5, -4.9 - W, 2.4, W, is_horizontal=True)  # P304
    draw_window(6.1, -4.9 - W, 1.3, W, is_horizontal=True)  # P211
    draw_window(8.8, -4.9 - W, 1.3, W, is_horizontal=True)  # P301
    draw_window(11.5, -4.9 - W, 1.3, W, is_horizontal=True) # P302
    draw_window(15.0, -4.9 - W, 2.0, W, is_horizontal=True) # Phòng nghị án 2
    draw_window(19.3, -4.9 - W, 1.6, W, is_horizontal=True) # P303
    draw_window(22.7, -4.9 - W, 1.6, W, is_horizontal=True) # P305
    draw_window(26.1, -4.9 - W, 1.6, W, is_horizontal=True) # P306
    draw_window(29.5, -4.9 - W, 1.6, W, is_horizontal=True) # P309

    # Tòa 1 Corridor End Windows (East & West)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)

    # Tòa 2 Exterior Windows
    draw_window(5.0, 14.5, 2.0, W, is_horizontal=True)   # T2_N1
    draw_window(10.0, 14.5, 2.0, W, is_horizontal=True)  # T2_N2
    draw_window(15.0, 14.5, 2.0, W, is_horizontal=True)  # Central Rear Hall Window
    draw_window(20.0, 14.5, 2.0, W, is_horizontal=True)  # T2_N3
    draw_window(25.0, 14.5, 2.0, W, is_horizontal=True)  # T2_N4 Phòng họp

    draw_window(5.0, 6.2 - W, 2.0, W, is_horizontal=True)   # T2_S1
    draw_window(10.0, 6.2 - W, 2.0, W, is_horizontal=True)  # T2_S2
    draw_window(20.0, 6.2 - W, 2.0, W, is_horizontal=True)  # T2_S3
    draw_window(25.0, 6.2 - W, 2.0, W, is_horizontal=True)  # T2_S4

    # Tòa 2 Side Windows
    draw_window(3.5 - W, 12.0, W, 1.5, is_horizontal=False)
    draw_window(3.5 - W, 7.0, W, 1.5, is_horizontal=False)
    draw_window(28.5, 12.0, W, 1.5, is_horizontal=False)
    draw_window(28.5, 7.0, W, 1.5, is_horizontal=False)

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
        font_sz = r.get('font_size', 8.0)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 34.0)
    ax.set_ylim(-8.0, 16.5)

    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "mat_bang_tang_2.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang2()
