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

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    X_MAX = 32.0            # Main building length = 32.0m

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 4 - An Giang', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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

    # Rear Connecting Lobby Passage leading to Rear Trial Block (X: 13.5 to 18.5, Y: 0.9 to 12.2)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 11.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (SINGLE-LINE ROOM LABELS, NO WRAPPING)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- NORTH WING (Y > 0.9) ---
        {
            'id': 'P1_1', 'name': 'Phòng Kế toán',
            'x': 0.0, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (1.35, 3.15),
            'door': (1.8, 0.9, 0.7, 'N_IN_RIGHT'),
            'font_size': 7.2
        },
        {
            'id': 'P1_2', 'name': 'Phòng Phó Chánh văn phòng',
            'x': 2.7, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (4.05, 3.15),
            'door': (4.5, 0.9, 0.7, 'N_IN_RIGHT'),
            'font_size': 6.2
        },
        {
            'id': 'P1_3', 'name': 'Phòng Thẩm phán',
            'x': 5.4, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (6.75, 3.15),
            'door': (7.2, 0.9, 0.7, 'N_IN_RIGHT'),
            'font_size': 7.0
        },
        {
            'id': 'P1_4', 'name': 'Phòng Thẩm phán',
            'x': 8.1, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (9.45, 3.15),
            'door': (9.9, 0.9, 0.7, 'N_IN_RIGHT'),
            'font_size': 7.0
        },
        {
            'id': 'P1_5', 'name': 'Phòng Phó Chánh án',
            'x': 10.8, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (12.15, 3.15),
            'door': (12.6, 0.9, 0.7, 'N_IN_RIGHT'),
            'font_size': 6.5
        },
        {
            'id': 'P1_6', 'name': 'Phòng Chánh án',
            'x': 18.5, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (19.85, 3.15),
            'door': (18.9, 0.9, 0.7, 'N_IN_RIGHT'),
            'font_size': 7.0
        },
        {
            'id': 'P1_7', 'name': 'Phòng Chánh văn phòng',
            'x': 21.2, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (22.55, 3.15),
            'door': (21.6, 0.9, 0.7, 'N_IN_RIGHT'),
            'font_size': 6.5
        },
        {
            'id': 'P1_8', 'name': 'Phòng Thẩm tra viên',
            'x': 23.9, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (25.25, 3.15),
            'door': (24.3, 0.9, 0.7, 'N_IN_RIGHT'),
            'font_size': 6.8
        },
        {
            'id': 'P1_9', 'name': 'Phòng Thẩm phán',
            'x': 26.6, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (27.95, 3.15),
            'door': (27.0, 0.9, 0.7, 'N_IN_RIGHT'),
            'font_size': 7.0
        },
        {
            'id': 'P1_10', 'name': 'Phòng Thẩm phán',
            'x': 29.3, 'y': 0.9, 'w': 2.7, 'h': 4.5,
            'text_center': (30.65, 3.15),
            'door': (29.7, 0.9, 0.7, 'N_IN_RIGHT'),
            'font_size': 7.0
        },

        # --- SOUTH WING (Y < -0.9) ---
        {
            'id': 'P1_11', 'name': 'Phòng Thư ký',
            'x': 0.0, 'y': -4.9, 'w': 2.7, 'h': 4.0,
            'text_center': (1.35, -2.9),
            'door': (1.8, -0.9, 0.7, 'S_IN_RIGHT'),
            'font_size': 7.2
        },
        {
            'id': 'P1_12', 'name': 'Phòng Thư ký',
            'x': 2.7, 'y': -4.9, 'w': 2.7, 'h': 4.0,
            'text_center': (4.05, -2.9),
            'door': (4.5, -0.9, 0.7, 'S_IN_RIGHT'),
            'font_size': 7.2
        },
        {
            'id': 'P1_13', 'name': 'Phòng Thư ký',
            'x': 5.4, 'y': -4.9, 'w': 2.7, 'h': 4.0,
            'text_center': (6.75, -2.9),
            'door': (7.2, -0.9, 0.7, 'S_IN_RIGHT'),
            'font_size': 7.2
        },
        {
            'id': 'P1_14', 'name': 'Phòng Thư ký',
            'x': 8.1, 'y': -4.9, 'w': 2.7, 'h': 4.0,
            'text_center': (9.45, -2.9),
            'door': (9.9, -0.9, 0.7, 'S_IN_RIGHT'),
            'font_size': 7.2
        },
        {
            'id': 'P1_15', 'name': 'Phòng Thư ký',
            'x': 10.8, 'y': -4.9, 'w': 2.7, 'h': 4.0,
            'text_center': (12.15, -2.9),
            'door': (12.6, -0.9, 0.7, 'S_IN_RIGHT'),
            'font_size': 7.2
        },
        {
            'id': 'P1_16', 'name': 'Phòng Cán bộ hợp đồng',
            'x': 18.5, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (21.875, -2.9),
            'door': (19.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P1_17', 'name': 'Phòng Thẩm phán',
            'x': 25.25, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (28.625, -2.9),
            'door': (26.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },

        # --- REAR TRIAL BLOCK (KHỐI NHÀ XÉT XỬ PHÍA BẮC, Y: 6.2m TO 12.2m) ---
        {
            'id': 'P1_18', 'name': 'Phòng Xét xử dân sự',
            'x': 3.5, 'y': 6.2, 'w': 10.0, 'h': 6.0,
            'text_center': (8.5, 9.2),
            'door': (13.5, 8.5, 1.0, 'E_IN_UP'),
            'font_size': 9.5
        },
        {
            'id': 'P1_19', 'name': 'Phòng Xét xử hình sự',
            'x': 18.5, 'y': 6.2, 'w': 10.0, 'h': 6.0,
            'text_center': (23.5, 9.2),
            'door': (18.5, 8.5, 1.0, 'W_IN_UP'),
            'font_size': 9.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 14.7, 1.4, 2.6, 2.6
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

    # Front Main Entrance Steps at Bottom (South: Y = -4.9 to -5.7)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([13.5, 18.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([13.5, 13.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([18.5, 18.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)

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

    # Main Building Exterior Walls
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

    # South Front Entrance Side Wall Cheeks
    draw_wall(13.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)
    draw_wall(18.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)

    # REAR TRIAL BLOCK CONNECTING SIDE WALLS (WITH OPENINGS FOR COURTROOM DOORS AT Y: 8.5 to 9.5m)
    draw_wall(13.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 3.1)
    draw_wall(13.5 - PART_THICKNESS/2, 9.5, PART_THICKNESS, 2.7)

    draw_wall(18.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 3.1)
    draw_wall(18.5 - PART_THICKNESS/2, 9.5, PART_THICKNESS, 2.7)

    # Left Courtroom Exterior Walls (X: 3.5m to 13.5m, Y: 6.2m to 12.2m)
    draw_wall(3.5 - W, 6.2 - W, W, 6.0 + 2*W)                     # West outer wall
    draw_wall(3.5 - W, 12.2, 10.0 + W, W)                         # North outer wall
    draw_wall(3.5 - W, 6.2 - W, 10.0 + W, W)                     # South outer wall

    # Right Courtroom Exterior Walls (X: 18.5m to 28.5m, Y: 6.2m to 12.2m)
    draw_wall(28.5, 6.2 - W, W, 6.0 + 2*W)                        # East outer wall
    draw_wall(18.5, 12.2, 10.0 + W, W)                            # North outer wall
    draw_wall(18.5, 6.2 - W, 10.0 + W, W)                        # South outer wall

    # Rear Block Top North Wall across central passage (Y = 12.2m)
    draw_wall(13.5, 12.2, 5.0, W)

    # Main Building Corridor Wall Lines (Y = 0.9 & Y = -0.9) - PRECISION ALIGNED WITH DOOR OPENINGS
    # North Corridor Line Y = 0.9
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 1.8, PART_THICKNESS)
    draw_wall(2.5, 0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(5.2, 0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(7.9, 0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(10.6, 0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(13.3, 0.9 - PART_THICKNESS/2, 0.2, PART_THICKNESS)

    draw_wall(18.5, 0.9 - PART_THICKNESS/2, 0.4, PART_THICKNESS)
    draw_wall(19.6, 0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(22.3, 0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(25.0, 0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(27.7, 0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(30.4, 0.9 - PART_THICKNESS/2, 1.6, PART_THICKNESS)

    # South Corridor Line Y = -0.9
    draw_wall(0.0, -0.9 - PART_THICKNESS/2, 1.8, PART_THICKNESS)
    draw_wall(2.5, -0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(5.2, -0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(7.9, -0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(10.6, -0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(13.3, -0.9 - PART_THICKNESS/2, 0.2, PART_THICKNESS)

    draw_wall(18.5, -0.9 - PART_THICKNESS/2, 1.3, PART_THICKNESS)
    draw_wall(20.6, -0.9 - PART_THICKNESS/2, 5.9, PART_THICKNESS)
    draw_wall(27.3, -0.9 - PART_THICKNESS/2, 4.7, PART_THICKNESS)

    # Main Building Internal Vertical Partitions
    draw_wall(2.7 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(5.4 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(8.1 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(10.8 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(13.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(18.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(21.2 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(23.9 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(26.6 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(29.3 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    draw_wall(2.7 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(5.4 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(8.1 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(10.8 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(13.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(18.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(25.25 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

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

    # Main Building Windows
    draw_window(0.8, 5.4, 1.2, W, is_horizontal=True)    # P1_1
    draw_window(3.5, 5.4, 1.2, W, is_horizontal=True)    # P1_2
    draw_window(6.2, 5.4, 1.2, W, is_horizontal=True)    # P1_3
    draw_window(8.9, 5.4, 1.2, W, is_horizontal=True)    # P1_4
    draw_window(11.6, 5.4, 1.2, W, is_horizontal=True)   # P1_5
    draw_window(19.3, 5.4, 1.2, W, is_horizontal=True)   # P1_6
    draw_window(22.0, 5.4, 1.2, W, is_horizontal=True)   # P1_7
    draw_window(24.7, 5.4, 1.2, W, is_horizontal=True)   # P1_8
    draw_window(27.4, 5.4, 1.2, W, is_horizontal=True)   # P1_9
    draw_window(30.1, 5.4, 1.2, W, is_horizontal=True)   # P1_10

    draw_window(0.8, -4.9 - W, 1.2, W, is_horizontal=True) # P1_11
    draw_window(3.5, -4.9 - W, 1.2, W, is_horizontal=True) # P1_12
    draw_window(6.2, -4.9 - W, 1.2, W, is_horizontal=True) # P1_13
    draw_window(8.9, -4.9 - W, 1.2, W, is_horizontal=True) # P1_14
    draw_window(11.6, -4.9 - W, 1.2, W, is_horizontal=True)# P1_15
    draw_window(20.5, -4.9 - W, 2.5, W, is_horizontal=True)# P1_16
    draw_window(27.2, -4.9 - W, 2.5, W, is_horizontal=True)# P1_17

    # Rear Courtroom Windows
    draw_window(6.5, 12.2, 4.0, W, is_horizontal=True)    # Left Courtroom
    draw_window(21.5, 12.2, 4.0, W, is_horizontal=True)   # Right Courtroom
    draw_window(3.5 - W, 8.2, W, 2.0, is_horizontal=False)
    draw_window(28.5, 8.2, W, 2.0, is_horizontal=False)

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
    ax.set_ylim(-8.0, 14.2)

    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\AnGiang\AnGiang4\Tang1"
    os.makedirs(target_dir, exist_ok=True)
    out_path = os.path.join(target_dir, "mat_bang_tang_1.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {out_path}")

if __name__ == "__main__":
    create_floorplan_tang1()
