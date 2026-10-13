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
    Y_TOA2_TOP = 14.5       # Extended rear building height (top Y = 14.5m)
    Y_CORR2_BOT = 9.5       # Tòa 2 central horizontal corridor bottom Y
    Y_CORR2_TOP = 11.0      # Tòa 2 central horizontal corridor top Y

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân tỉnh Đồng Nai', 
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
    ax.plot([lg_x + 22.0, lg_x + 22.0], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 22.0, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 23.0, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Main Building Horizontal Corridor (X: 0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Front Main Lobby Space (X: 13.5 to 18.5, Y: -5.7 to -0.9)
    ax.add_patch(patches.Rectangle((13.5, -5.7), 5.0, 4.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Connecting Lobby Passage leading to Tòa 2 (X: 13.5 to 18.5, Y: 0.9 to 14.5)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, Y_TOA2_TOP - 0.9, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 Central Horizontal Corridor (X: 3.5 to 28.5, Y: 9.5 to 11.0)
    ax.add_patch(patches.Rectangle((3.5, Y_CORR2_BOT), 25.0, Y_CORR2_TOP - Y_CORR2_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 1 — ĐỒNG NAI)
    # Tòa 1: 14 phòng, Tòa 2: 4 phòng (tổng 18 phòng)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA 1 — NORTH WING (Y: 0.9 to 5.4m) ===
        # West Wing: Văn Thư, Lưu Trữ, Kế Toán
        {
            'id': 'P1_VT', 'name': 'Phòng Văn Thư',
            'x': 0.0, 'y': 0.9, 'w': 3.0, 'h': 4.5,
            'text_center': (1.5, 3.15),
            'door': (2.0, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P1_LT', 'name': 'Phòng Lưu Trữ',
            'x': 3.0, 'y': 0.9, 'w': 5.5, 'h': 4.5,
            'text_center': (5.75, 3.15),
            'door': (7.0, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P1_KT', 'name': 'Phòng Kế Toán',
            'x': 8.5, 'y': 0.9, 'w': 5.0, 'h': 4.5,
            'text_center': (11.0, 3.15),
            'door': (12.2, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        # East Wing: Phòng 108, Phòng 110, Phòng photo, Phòng tạp vụ
        {
            'id': 'P1_108', 'name': 'Phòng 108',
            'x': 18.5, 'y': 0.9, 'w': 3.0, 'h': 4.5,
            'text_center': (20.0, 3.15),
            'door': (19.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P1_110', 'name': 'Phòng 110',
            'x': 21.5, 'y': 0.9, 'w': 6.0, 'h': 4.5,
            'text_center': (24.5, 3.15),
            'door': (22.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'P1_PH', 'name': 'Phòng photo',
            'x': 27.5, 'y': 0.9, 'w': 2.3, 'h': 4.5,
            'text_center': (28.65, 3.15),
            'door': (28.2, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P1_TV', 'name': 'Phòng tạp vụ',
            'x': 29.8, 'y': 0.9, 'w': 2.2, 'h': 4.5,
            'text_center': (30.9, 3.15),
            'door': (30.5, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 7.5
        },

        # === TÒA 1 — SOUTH WING (Y: -4.9 to -0.9m) ===
        # West Wing: Phòng 101, Phòng 103, Phòng 105, Phòng Tiếp Dân
        {
            'id': 'P1_101', 'name': 'Phòng 101',
            'x': 0.0, 'y': -4.9, 'w': 3.2, 'h': 4.0,
            'text_center': (1.6, -2.9),
            'door': (2.2, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P1_103', 'name': 'Phòng 103',
            'x': 3.2, 'y': -4.9, 'w': 2.3, 'h': 4.0,
            'text_center': (4.35, -2.9),
            'door': (3.8, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P1_105', 'name': 'Phòng 105',
            'x': 5.5, 'y': -4.9, 'w': 2.3, 'h': 4.0,
            'text_center': (6.65, -2.9),
            'door': (6.1, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P1_TD1', 'name': 'Phòng Tiếp Dân',
            'x': 7.8, 'y': -4.9, 'w': 5.7, 'h': 4.0,
            'text_center': (10.65, -2.9),
            'door': (12.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        # East Wing: Phòng Tiếp Dân, Phòng 107, Phòng 109
        {
            'id': 'P1_TD2', 'name': 'Phòng Tiếp Dân',
            'x': 18.5, 'y': -4.9, 'w': 6.5, 'h': 4.0,
            'text_center': (21.75, -2.9),
            'door': (19.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P1_107', 'name': 'Phòng 107',
            'x': 25.0, 'y': -4.9, 'w': 3.5, 'h': 4.0,
            'text_center': (26.75, -2.9),
            'door': (25.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P1_109', 'name': 'Phòng 109',
            'x': 28.5, 'y': -4.9, 'w': 3.5, 'h': 4.0,
            'text_center': (30.25, -2.9),
            'door': (29.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },

        # === TÒA 2 — REAR BLOCK (Y: 6.2 to 14.5m) ===
        # North Row: Phòng XX 1 (West), Tổ NV 2 (East)
        {
            'id': 'P2_XX1', 'name': 'Phòng XX 1',
            'x': 3.5, 'y': Y_CORR2_TOP, 'w': 10.0, 'h': Y_TOA2_TOP - Y_CORR2_TOP,
            'text_center': (8.5, 12.75),
            'door': (5.5, Y_CORR2_TOP, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'P2_NV2', 'name': 'Tổ NV 2',
            'x': 18.5, 'y': Y_CORR2_TOP, 'w': 10.0, 'h': Y_TOA2_TOP - Y_CORR2_TOP,
            'text_center': (23.5, 12.75),
            'door': (20.0, Y_CORR2_TOP, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.0
        },
        # South Row: Tổ NV 1 (West), Tổ NV 3 (East)
        {
            'id': 'P2_NV1', 'name': 'Tổ NV 1',
            'x': 3.5, 'y': 6.2, 'w': 10.0, 'h': Y_CORR2_BOT - 6.2,
            'text_center': (8.5, 7.85),
            'door': (5.5, Y_CORR2_BOT, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'P2_NV3', 'name': 'Tổ NV 3',
            'x': 18.5, 'y': 6.2, 'w': 10.0, 'h': Y_CORR2_BOT - 6.2,
            'text_center': (23.5, 7.85),
            'door': (20.0, Y_CORR2_BOT, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS (TẦNG 1)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 14.7, 1.4, 2.6, 2.6
    # Floor 1 Staircase fill matches corridor `#eef4f7`
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

    # Outdoor Side Steps at Corridor Ends (East & West Exits of Tòa 1)
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
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.0, 10.25, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Tòa 1 Exterior Side Walls
    draw_wall(-W, -4.9 - W, W, 4.0 + W)
    draw_wall(-W, 0.9, W, 4.5 + W)
    draw_wall(X_MAX, -4.9 - W, W, 4.0 + W)
    draw_wall(X_MAX, 0.9, W, 4.5 + W)

    # Tòa 1 North Top Wall (with opening for rear passage at X: 13.5 to 18.5)
    draw_wall(-W, 5.4, 13.5 + W + PART_THICKNESS/2, W)
    draw_wall(18.5 - PART_THICKNESS/2, 5.4, (X_MAX - 18.5) + W + PART_THICKNESS/2, W)

    # Tòa 1 South Bottom Wall
    draw_wall(-W, -4.9 - W, 13.5 + W + PART_THICKNESS/2, W)
    draw_wall(18.5 - PART_THICKNESS/2, -4.9 - W, (X_MAX - 18.5) + W + PART_THICKNESS/2, W)

    # South Front Entrance Side Wall Cheeks
    draw_wall(13.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)
    draw_wall(18.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)

    # Tòa 2 Connecting Passage Side Walls
    draw_wall(13.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)
    draw_wall(18.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)

    # Tòa 2 Exterior Walls (X: 3.5m to 28.5m, Y: 6.2m to 14.5m)
    draw_wall(3.5 - W, 6.2 - W, W, (Y_TOA2_TOP - 6.2) + 2*W)       # West outer wall
    draw_wall(28.5, 6.2 - W, W, (Y_TOA2_TOP - 6.2) + 2*W)          # East outer wall
    draw_wall(3.5 - W, Y_TOA2_TOP, 25.0 + 2*W, W)                 # North outer wall
    draw_wall(3.5 - W, 6.2 - W, 10.0 + W, W)                     # South outer wall West wing
    draw_wall(18.5, 6.2 - W, 10.0 + W, W)                        # South outer wall East wing

    # Rear Block Top North Wall across central passage (Y = 14.5m)
    draw_wall(13.5, Y_TOA2_TOP, 5.0, W)

    # Tòa 1 Corridor Wall Lines (Y = 0.9 & Y = -0.9) with door cutouts
    # North Corridor Line Y = 0.9 (Doors at: 2.0, 7.0, 12.2 | 19.5, 22.5, 28.2, 30.5)
    # West:
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(2.8, 0.9 - PART_THICKNESS/2, 4.2, PART_THICKNESS)
    draw_wall(7.8, 0.9 - PART_THICKNESS/2, 4.4, PART_THICKNESS)
    draw_wall(13.0, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    # East:
    draw_wall(18.5, 0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(20.3, 0.9 - PART_THICKNESS/2, 2.2, PART_THICKNESS)
    draw_wall(23.3, 0.9 - PART_THICKNESS/2, 4.9, PART_THICKNESS)
    draw_wall(28.95, 0.9 - PART_THICKNESS/2, 1.55, PART_THICKNESS)
    draw_wall(31.25, 0.9 - PART_THICKNESS/2, 0.75, PART_THICKNESS)

    # South Corridor Line Y = -0.9 (Doors at: 2.2, 3.8, 6.1, 12.2 | 19.5, 25.8, 29.5)
    # West:
    draw_wall(0.0, -0.9 - PART_THICKNESS/2, 2.2, PART_THICKNESS)
    draw_wall(3.0, -0.9 - PART_THICKNESS/2, 0.8, PART_THICKNESS)
    draw_wall(4.55, -0.9 - PART_THICKNESS/2, 1.55, PART_THICKNESS)
    draw_wall(6.85, -0.9 - PART_THICKNESS/2, 5.35, PART_THICKNESS)
    draw_wall(13.05, -0.9 - PART_THICKNESS/2, 0.45, PART_THICKNESS)
    # East:
    draw_wall(18.5, -0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(20.35, -0.9 - PART_THICKNESS/2, 5.45, PART_THICKNESS)
    draw_wall(26.6, -0.9 - PART_THICKNESS/2, 2.9, PART_THICKNESS)
    draw_wall(30.3, -0.9 - PART_THICKNESS/2, 1.7, PART_THICKNESS)

    # Tòa 1 Internal Vertical Partitions
    # North Wing:
    draw_wall(3.0 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(8.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(13.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(18.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(21.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(27.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(29.8 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    # South Wing:
    draw_wall(3.2 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(5.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(7.8 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(13.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(18.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(25.0 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(28.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

    # Tòa 2 Horizontal Corridor Wall Lines (Y = 11.0m & Y = 9.5m) with door cutouts
    # North Corridor Line Y = 11.0m (Doors at 5.5, 20.0)
    draw_wall(3.5, Y_CORR2_TOP - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(6.35, Y_CORR2_TOP - PART_THICKNESS/2, 7.15, PART_THICKNESS)

    draw_wall(18.5, Y_CORR2_TOP - PART_THICKNESS/2, 1.5, PART_THICKNESS)
    draw_wall(20.85, Y_CORR2_TOP - PART_THICKNESS/2, 7.65, PART_THICKNESS)

    # South Corridor Line Y = 9.5m (Doors at 5.5, 20.0)
    draw_wall(3.5, Y_CORR2_BOT - PART_THICKNESS/2, 2.0, PART_THICKNESS)
    draw_wall(6.35, Y_CORR2_BOT - PART_THICKNESS/2, 7.15, PART_THICKNESS)

    draw_wall(18.5, Y_CORR2_BOT - PART_THICKNESS/2, 1.5, PART_THICKNESS)
    draw_wall(20.85, Y_CORR2_BOT - PART_THICKNESS/2, 7.65, PART_THICKNESS)

    # Tòa 2 Internal Vertical Partitions
    draw_wall(13.5 - PART_THICKNESS/2, Y_CORR2_TOP, PART_THICKNESS, Y_TOA2_TOP - Y_CORR2_TOP)
    draw_wall(18.5 - PART_THICKNESS/2, Y_CORR2_TOP, PART_THICKNESS, Y_TOA2_TOP - Y_CORR2_TOP)
    draw_wall(13.5 - PART_THICKNESS/2, 6.2, PART_THICKNESS, Y_CORR2_BOT - 6.2)
    draw_wall(18.5 - PART_THICKNESS/2, 6.2, PART_THICKNESS, Y_CORR2_BOT - 6.2)

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

    # Tòa 1 North Windows (Y = 5.4)
    draw_window(0.8, 5.4, 1.4, W, is_horizontal=True)    # Văn Thư
    draw_window(4.5, 5.4, 2.5, W, is_horizontal=True)    # Lưu Trữ
    draw_window(9.8, 5.4, 2.4, W, is_horizontal=True)    # Kế Toán
    draw_window(19.3, 5.4, 1.4, W, is_horizontal=True)   # Phòng 108
    draw_window(23.0, 5.4, 3.0, W, is_horizontal=True)   # Phòng 110
    draw_window(28.0, 5.4, 1.2, W, is_horizontal=True)   # Photo
    draw_window(30.3, 5.4, 1.2, W, is_horizontal=True)   # Tạp vụ

    # Tòa 1 South Windows (Y = -4.9 - W)
    draw_window(0.9, -4.9 - W, 1.4, W, is_horizontal=True)   # 101
    draw_window(3.6, -4.9 - W, 1.4, W, is_horizontal=True)   # 103
    draw_window(5.9, -4.9 - W, 1.4, W, is_horizontal=True)   # 105
    draw_window(9.2, -4.9 - W, 2.8, W, is_horizontal=True)   # Tiếp Dân West
    draw_window(20.2, -4.9 - W, 3.0, W, is_horizontal=True)  # Tiếp Dân East
    draw_window(25.8, -4.9 - W, 1.8, W, is_horizontal=True)  # 107
    draw_window(29.3, -4.9 - W, 1.8, W, is_horizontal=True)  # 109

    # Tòa 2 Windows
    draw_window(6.5, Y_TOA2_TOP, 4.0, W, is_horizontal=True)    # XX 1 North
    draw_window(21.5, Y_TOA2_TOP, 4.0, W, is_horizontal=True)   # NV 2 North
    draw_window(6.5, 6.2 - W, 4.0, W, is_horizontal=True)      # NV 1 South
    draw_window(21.5, 6.2 - W, 4.0, W, is_horizontal=True)     # NV 3 South
    draw_window(3.5 - W, 12.0, W, 1.8, is_horizontal=False)    # XX 1 West
    draw_window(3.5 - W, 7.0, W, 1.8, is_horizontal=False)     # NV 1 West
    draw_window(28.5, 12.0, W, 1.8, is_horizontal=False)       # NV 2 East
    draw_window(28.5, 7.0, W, 1.8, is_horizontal=False)        # NV 3 East

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
        if r['name']:
            cx, cy = r['text_center']
            font_sz = r.get('font_size', 8.5)
            ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                    fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 34.0)
    ax.set_ylim(-8.0, 16.5)

    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "mat_bang_tang_1.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 1 đã xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang1()
