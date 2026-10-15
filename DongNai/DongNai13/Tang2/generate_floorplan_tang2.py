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

COURT_NAME = "Tòa án nhân dân khu vực 13 - Đồng Nai"

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
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#ffffff'    # Floor 2 stair background is pure white

    WALL_THICKNESS = 0.22  # 220mm exterior structural wall (dày)
    PART_THICKNESS = 0.08  # 80mm interior partition & corridor wall (mỏng, thanh thoát)
    W = WALL_THICKNESS
    P = PART_THICKNESS
    X_MAX = 32.0            # Tòa 1 Main Building Length = 32.0m
    Y_TOA2_TOP = 14.5       # Tòa 2 Top Y = 14.5m

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
    ax.plot([lg_x + 15.0, lg_x + 15.8], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.4, zorder=1)
    ax.plot([lg_x + 15.0, lg_x + 15.8], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.4, zorder=1)
    ax.text(lg_x + 16.1, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 21.0, lg_x + 21.0], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 21.0, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 22.0, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (TẦNG 2)
    # ---------------------------------------------------------
    # Main Building Horizontal Corridor (X: 0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Connecting Passage leading to Tòa 2 (X: 13.5 to 18.5, Y: 0.9 to Y_TOA2_TOP)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, Y_TOA2_TOP - 0.9, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TÒA ÁN KHU VỰC 13 - ĐỒNG NAI: TẦNG 2)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA 1: DÃY PHÍA BẮC (North Wing: Y > 0.9m) ===
        # Cánh Tây Bắc (X: 0.0 to 13.5m)
        {
            'id': 'T2_PCA_CHINH', 'name': 'Phòng Chánh án',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'door': (6.3, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'T2_PPCA', 'name': 'Phòng Phó chánh án',
            'x': 7.5, 'y': 0.9, 'w': 6.0, 'h': 4.5,
            'text_center': (10.5, 3.15),
            'door': (7.9, 0.9, 0.85, 'N_IN_LEFT'),
            'font_size': 9.5
        },

        # Cánh Đông Bắc (X: 18.5 to 32.0m)
        {
            'id': 'T2_PTP1', 'name': 'Phòng Thẩm phán',
            'x': 18.5, 'y': 0.9, 'w': 6.75, 'h': 4.5,
            'text_center': (21.875, 3.15),
            'door': (19.0, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T2_PTP2', 'name': 'Phòng Thẩm phán',
            'x': 25.25, 'y': 0.9, 'w': 6.75, 'h': 4.5,
            'text_center': (28.625, 3.15),
            'door': (25.8, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },

        # === TÒA 1: DÃY PHÍA NAM (South Wing: Y < -0.9m) ===
        # Cánh Tây Nam (X: 0.0 to 13.5m) - 3 Phòng Thư ký
        {
            'id': 'T2_PTK1', 'name': 'Phòng Thư ký',
            'x': 0.0, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (2.25, -2.9),
            'door': (3.3, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T2_PTK2', 'name': 'Phòng Thư ký',
            'x': 4.5, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (6.75, -2.9),
            'door': (7.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T2_PTK3', 'name': 'Phòng Thư ký',
            'x': 9.0, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (11.25, -2.9),
            'door': (12.3, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },

        # Dãy Nam Trung tâm (X: 13.5 to 18.5m) - Phòng Thư ký
        {
            'id': 'T2_PTK_MID', 'name': 'Phòng Thư ký',
            'x': 13.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (16.0, -2.9),
            'door': (14.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },

        # Cánh Đông Nam (X: 18.5 to 32.0m) - 1 Thư ký + 1 Nghị án
        {
            'id': 'T2_PTK5', 'name': 'Phòng Thư ký',
            'x': 18.5, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (21.875, -2.9),
            'door': (19.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T2_PNA', 'name': 'Phòng Nghị án',
            'x': 25.25, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (28.625, -2.9),
            'door': (25.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },

        # === TÒA 2 (KHỐI XÉT XỬ PHÍA BẮC - 2 PHÒNG XÉT XỬ) ===
        # West Wing Tòa 2: Phòng xét xử
        {
            'id': 'T2_XX1', 'name': 'Phòng xét xử',
            'x': 3.5, 'y': 6.2, 'w': 10.0, 'h': Y_TOA2_TOP - 6.2,
            'text_center': (8.5, 10.35),
            'door': (13.5, 9.8, 0.9, 'W_IN_UP'),
            'font_size': 11.0
        },
        # East Wing Tòa 2: Phòng Xét xử
        {
            'id': 'T2_XX2', 'name': 'Phòng Xét xử',
            'x': 18.5, 'y': 6.2, 'w': 10.0, 'h': Y_TOA2_TOP - 6.2,
            'text_center': (23.5, 10.35),
            'door': (18.5, 9.8, 0.9, 'E_IN_UP'),
            'font_size': 11.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHIC (FLOOR 2 - NỀN TRẮNG THUẦN)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 14.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    ax.plot([mid_x, mid_x], [stair_y, stair_y + stair_h * (num_treads - 1) / num_treads], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Stair label
    ax.text(mid_x, stair_y + stair_h / 2.0, 'CẦU THANG', color=COLOR_TEXT_MUTED, fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=5)

    # Labels for Corridor
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.0, 5.5, 'HÀNH LANG NỐI', color=COLOR_TEXT_MUTED, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (PRECISION ALIGNED WITH DOOR OPENINGS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # === TÒA 1: EXTERIOR ENVELOPE WALLS (WALL_THICKNESS = 0.22m) ===
    # Tòa 1 Outer West Wall (ENCLOSED AT CORRIDOR Y: -0.9 to 0.9)
    draw_wall(-W, -4.9 - W, W, (5.4 + 4.9) + 2*W)

    # Tòa 1 Outer East Wall (ENCLOSED AT CORRIDOR Y: -0.9 to 0.9)
    draw_wall(X_MAX, -4.9 - W, W, (5.4 + 4.9) + 2*W)

    # Tòa 1 North Top Wall (Y = 5.4m, open for rear passage at X: 13.5 to 18.5)
    draw_wall(-W, 5.4, 13.5 + W, W)
    draw_wall(18.5, 5.4, (X_MAX - 18.5) + W, W)

    # Tòa 1 South Bottom Wall (Y = -4.9m, ENCLOSED FULL LENGTH from X: -W to X_MAX + W)
    draw_wall(-W, -4.9 - W, X_MAX + 2*W, W)

    # === CONNECTING PASSAGE WALLS (Between Tòa 1 and Tòa 2: Y = 5.4 to 6.2m) ===
    # Solid walls, NO windows!
    draw_wall(13.5 - P, 5.4, P, 0.8)
    draw_wall(18.5, 5.4, P, 0.8)

    # === TÒA 2: CONNECTING PASSAGE & EXTERIOR WALLS ===
    # Left Wall at X = 13.5m (Door entry for Courtroom 1 at Y: 9.8 to 10.7)
    draw_wall(13.5 - P, 6.2, P, 3.6)     # Y: 6.2 to 9.8
    draw_wall(13.5 - P, 10.7, P, 3.8)    # Y: 10.7 to 14.5

    # Right Wall at X = 18.5m (Door entry for Courtroom 2 at Y: 9.8 to 10.7)
    draw_wall(18.5, 6.2, P, 3.6)          # Y: 6.2 to 9.8
    draw_wall(18.5, 10.7, P, 3.8)         # Y: 10.7 to 14.5

    # Tòa 2 Exterior Envelope Walls
    draw_wall(3.5 - W, 6.2 - W, W, (Y_TOA2_TOP - 6.2) + 2*W)       # West outer wall
    draw_wall(28.5, 6.2 - W, W, (Y_TOA2_TOP - 6.2) + 2*W)          # East outer wall
    draw_wall(3.5 - W, Y_TOA2_TOP, 25.0 + 2*W, W)                 # North outer wall
    draw_wall(3.5 - W, 6.2 - W, 10.0 + W, W)                     # South outer wall West wing
    draw_wall(18.5, 6.2 - W, 10.0 + W, W)                        # South outer wall East wing

    # === TÒA 1: INTERIOR CORRIDOR & PARTITION WALLS (PART_THICKNESS = 0.08m) ===
    # 1. North Corridor Line Y = 0.9m
    # Cánh Tây Bắc (X: 0.0 to 13.5): Doors at (6.3 to 7.15), (7.9 to 8.75)
    draw_wall(0.0, 0.9 - P/2, 6.3, P)
    draw_wall(7.15, 0.9 - P/2, 7.9 - 7.15, P)
    draw_wall(8.75, 0.9 - P/2, 13.5 - 8.75, P)

    # Cánh Đông Bắc (X: 18.5 to 32.0): Doors at (19.0 to 19.85), (25.8 to 26.65)
    draw_wall(18.5, 0.9 - P/2, 19.0 - 18.5, P)
    draw_wall(19.85, 0.9 - P/2, 25.8 - 19.85, P)
    draw_wall(26.65, 0.9 - P/2, 32.0 - 26.65, P)

    # 2. South Corridor Line Y = -0.9m
    # Cánh Tây Nam & Center (X: 0.0 to 18.5): Doors at (3.3 to 4.15), (7.8 to 8.65), (12.3 to 13.15), (14.0 to 14.85)
    draw_wall(0.0, -0.9 - P/2, 3.3, P)
    draw_wall(4.15, -0.9 - P/2, 7.8 - 4.15, P)
    draw_wall(8.65, -0.9 - P/2, 12.3 - 8.65, P)
    draw_wall(13.15, -0.9 - P/2, 14.0 - 13.15, P)
    draw_wall(14.85, -0.9 - P/2, 18.5 - 14.85, P)

    # Cánh Đông Nam (X: 18.5 to 32.0): Doors at (19.0 to 19.85), (25.8 to 26.65)
    draw_wall(18.5, -0.9 - P/2, 19.0 - 18.5, P)
    draw_wall(19.85, -0.9 - P/2, 25.8 - 19.85, P)
    draw_wall(26.65, -0.9 - P/2, 32.0 - 26.65, P)

    # 3. Tòa 1 Internal Vertical Partitions
    # West partitions
    draw_wall(7.5 - P/2, 0.9, P, 4.5)        # Between Chánh án & Phó chánh án
    draw_wall(4.5 - P/2, -4.9, P, 4.0)       # Between Thư ký 1 & Thư ký 2
    draw_wall(9.0 - P/2, -4.9, P, 4.0)       # Between Thư ký 2 & Thư ký 3
    draw_wall(13.5 - P/2, 0.9, P, 4.5)       # Main lobby West wall (North)
    draw_wall(13.5 - P/2, -4.9, P, 4.0)      # Between Thư ký 3 & Thư ký trung tâm

    # Center & East partitions
    draw_wall(18.5 - P/2, 0.9, P, 4.5)       # Main lobby East wall (North)
    draw_wall(18.5 - P/2, -4.9, P, 4.0)      # Between Thư ký trung tâm & Thư ký 5
    draw_wall(25.25 - P/2, 0.9, P, 4.5)      # Between Thẩm phán 1 & Thẩm phán 2
    draw_wall(25.25 - P/2, -4.9, P, 4.0)     # Between Thư ký 5 & Phòng Nghị án

    # ---------------------------------------------------------
    # 7. DRAW WINDOWS ON EXTERIOR WALLS
    # ---------------------------------------------------------
    def draw_window_horizontal(x0, x1, y):
        ax.plot([x0, x1], [y + 0.07, y + 0.07], color=COLOR_WALL, linewidth=1.3, zorder=12)
        ax.plot([x0, x1], [y - 0.07, y - 0.07], color=COLOR_WALL, linewidth=1.3, zorder=12)

    def draw_window_vertical(x, y0, y1):
        ax.plot([x + 0.07, x + 0.07], [y0, y1], color=COLOR_WALL, linewidth=1.3, zorder=12)
        ax.plot([x - 0.07, x - 0.07], [y0, y1], color=COLOR_WALL, linewidth=1.3, zorder=12)

    # Tòa 1 North Windows (Y = 5.4 + W/2)
    draw_window_horizontal(2.0, 5.5, 5.4 + W/2)       # Chánh án
    draw_window_horizontal(9.0, 12.0, 5.4 + W/2)      # Phó chánh án
    draw_window_horizontal(20.0, 23.5, 5.4 + W/2)     # Thẩm phán 1
    draw_window_horizontal(27.0, 30.5, 5.4 + W/2)     # Thẩm phán 2

    # Tòa 1 South Windows (Y = -4.9 - W/2)
    draw_window_horizontal(1.2, 3.2, -4.9 - W/2)      # Thư ký 1
    draw_window_horizontal(5.7, 7.7, -4.9 - W/2)      # Thư ký 2
    draw_window_horizontal(10.2, 12.2, -4.9 - W/2)    # Thư ký 3
    draw_window_horizontal(14.5, 17.5, -4.9 - W/2)    # Thư ký trung tâm
    draw_window_horizontal(20.0, 23.5, -4.9 - W/2)    # Thư ký 5
    draw_window_horizontal(27.0, 30.5, -4.9 - W/2)    # Phòng Nghị án

    # Tòa 1 West End Windows (X = -W/2)
    draw_window_vertical(-W/2, -3.9, -1.9)
    draw_window_vertical(-W/2, -0.6, 0.6)             # Corridor West End Window
    draw_window_vertical(-W/2, 2.1, 4.1)

    # Tòa 1 East End Windows (X = X_MAX + W/2)
    draw_window_vertical(X_MAX + W/2, -3.9, -1.9)
    draw_window_vertical(X_MAX + W/2, -0.6, 0.6)      # Corridor East End Window
    draw_window_vertical(X_MAX + W/2, 2.1, 4.1)

    # Tòa 2 Windows
    # West Wall (X = 3.5 - W/2)
    draw_window_vertical(3.5 - W/2, 7.5, 9.5)
    draw_window_vertical(3.5 - W/2, 11.0, 13.0)
    # East Wall (X = 28.5 + W/2)
    draw_window_vertical(28.5 + W/2, 7.5, 9.5)
    draw_window_vertical(28.5 + W/2, 11.0, 13.0)
    # North Wall (Y = Y_TOA2_TOP + W/2)
    draw_window_horizontal(6.0, 9.0, Y_TOA2_TOP + W/2)
    draw_window_horizontal(15.0, 17.0, Y_TOA2_TOP + W/2)   # Corridor window at top!
    draw_window_horizontal(23.0, 26.0, Y_TOA2_TOP + W/2)
    # South Wall Overhangs
    draw_window_horizontal(5.5, 8.5, 6.2 - W/2)
    draw_window_horizontal(23.5, 26.5, 6.2 - W/2)

    # ---------------------------------------------------------
    # 8. DOORS RENDERING (WITH SWING ARCS)
    # ---------------------------------------------------------
    def draw_door(dx, dy, dw, dtype):
        if dtype == 'N_IN_RIGHT':
            ax.plot([dx, dx], [dy, dy + dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((dx, dy), dw*2, dw*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)
        elif dtype == 'N_IN_LEFT':
            hx = dx + dw
            ax.plot([hx, hx], [dy, dy + dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((hx, dy), dw*2, dw*2, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)
        elif dtype == 'S_IN_RIGHT':
            ax.plot([dx, dx], [dy, dy - dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((dx, dy), dw*2, dw*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)
        elif dtype == 'S_IN_LEFT':
            hx = dx + dw
            ax.plot([hx, hx], [dy, dy - dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((hx, dy), dw*2, dw*2, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)
        elif dtype == 'W_IN_UP':
            ax.plot([dx - dw, dx], [dy, dy], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((dx, dy), dw*2, dw*2, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)
        elif dtype == 'E_IN_UP':
            ax.plot([dx, dx + dw], [dy, dy], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((dx, dy), dw*2, dw*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)

    for r in rooms:
        dx, dy, dw, dtype = r['door']
        draw_door(dx, dy, dw, dtype)

    # ---------------------------------------------------------
    # 9. ROOM LABELS & TEXT
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'], 
                fontweight='bold', ha='center', va='center', zorder=20)

    # ---------------------------------------------------------
    # 10. EXPORT & SAVE
    # ---------------------------------------------------------
    output_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\DongNai\DongNai13\Tang2"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "mat_bang_tang_2.png")

    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close(fig)
    print(f"Bản vẽ đã được xuất thành công tại: {output_path}")

if __name__ == '__main__':
    create_floorplan_tang2()
