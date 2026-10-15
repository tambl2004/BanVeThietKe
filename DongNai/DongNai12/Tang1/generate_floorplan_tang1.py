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

COURT_NAME = "Tòa án nhân dân khu vực 12 - Đồng Nai"

def create_floorplan_tang1(court_name: str = COURT_NAME):
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 12.5), dpi=300)
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
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 stair background matches lobby

    WALL_THICKNESS = 0.22  # 220mm exterior structural wall (dày)
    PART_THICKNESS = 0.08  # 80mm interior partition & corridor wall (mỏng, thanh thoát)
    W = WALL_THICKNESS
    P = PART_THICKNESS

    X_MAX = 41.0           # Tòa 1 Main Building Total Length = 41.0m
    X_LOBBY_L = 18.0       # Lobby Left X = 18.0m
    X_LOBBY_R = 23.0       # Lobby Right X = 23.0m

    # Tòa 2 Coordinates (Khối phòng xét xử 2 phía Bắc: 10m x 6m)
    X_TOA2_L = 15.5
    X_TOA2_R = 25.5
    Y_TOA2_BOT = 7.0       # 1.6m clear open courtyard between Tòa 1 and Tòa 2
    Y_TOA2_TOP = 13.0      # Exact 6.0m depth for Courtroom 2

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, f'MẶT BẰNG TẦNG 1  —  {court_name}', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = 1.0, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 6.0, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 7.1, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 11.5, lg_x + 12.5], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.4, zorder=1)
    ax.plot([lg_x + 11.5, lg_x + 12.5], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.4, zorder=1)
    ax.text(lg_x + 12.8, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 16.5, lg_x + 16.5], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 16.5, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 17.5, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (TẦNG 1)
    # ---------------------------------------------------------
    # Tòa 1: Main Horizontal Corridor (X: 0 to 41.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1: South Main Entrance Lobby Space (X: 18.0 to 23.0, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((X_LOBBY_L, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Connecting Passage from Tòa 1 North to Tòa 2 (X: 18.0 to 23.0, Y: 0.9 to Y_TOA2_BOT)
    ax.add_patch(patches.Rectangle((X_LOBBY_L, 0.9), 5.0, Y_TOA2_BOT - 0.9, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TỔNG CỘNG 16 PHÒNG: TÒA 1 + TÒA 2)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # =========================================================
        # === TÒA 1: DÃY PHÍA BẮC (North Wing: Y > 0.9m) ===
        # =========================================================
        # Cánh Tây Bắc (X: 0.0 to 18.0m) - 4 phòng
        {
            'id': 'T1_P1', 'name': 'Phòng số 1',
            'x': 0.0, 'y': 0.9, 'w': 4.8, 'h': 4.5,
            'text_center': (2.4, 3.15),
            'door': (3.6, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T1_P2', 'name': 'Phòng số 2',
            'x': 4.8, 'y': 0.9, 'w': 4.8, 'h': 4.5,
            'text_center': (7.2, 3.15),
            'door': (5.2, 0.9, 0.85, 'N_IN_LEFT'),
            'font_size': 9.5
        },
        {
            'id': 'T1_PCA_THANH', 'name': 'Phòng số CA (Thanh)',
            'x': 9.6, 'y': 0.9, 'w': 4.4, 'h': 4.5,
            'text_center': (11.8, 3.15),
            'door': (10.0, 0.9, 0.85, 'N_IN_LEFT'),
            'font_size': 9.0
        },
        {
            'id': 'T1_PHOP', 'name': 'Phòng Họp',
            'x': 14.0, 'y': 0.9, 'w': 4.0, 'h': 4.5,
            'text_center': (16.0, 3.15),
            'door': (14.4, 0.9, 0.85, 'N_IN_LEFT'),
            'font_size': 9.5
        },

        # Cánh Đông Bắc (X: 23.0 to 41.0m) - 4 phòng
        {
            'id': 'T1_PTD', 'name': 'Phòng Tiếp dân',
            'x': 23.0, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (25.25, 3.15),
            'door': (23.4, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T1_PTK', 'name': 'Phòng Thư ký',
            'x': 27.5, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (29.75, 3.15),
            'door': (27.9, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T1_PDAO', 'name': 'Phòng Đào',
            'x': 32.0, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (34.25, 3.15),
            'door': (32.4, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T1_PTINH', 'name': 'Phòng Tình',
            'x': 36.5, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (38.75, 3.15),
            'door': (36.9, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },

        # =========================================================
        # === TÒA 1: DÃY PHÍA NAM (South Wing: Y < -0.9m) ===
        # =========================================================
        # Cánh Tây Nam (X: 0.0 to 18.0m) - 4 phòng nhỏ (KT 3x3)
        {
            'id': 'T1_P3_XUYEN', 'name': 'Phòng số 3 (Xuyến)',
            'x': 0.0, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (2.25, -2.9),
            'door': (3.3, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'T1_P4_HA', 'name': 'Phòng số 4 (Hà)',
            'x': 4.5, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (6.75, -2.9),
            'door': (5.0, -0.9, 0.85, 'S_IN_LEFT'),
            'font_size': 9.0
        },
        {
            'id': 'T1_P5_LINH', 'name': 'Phòng số 5 (Linh)',
            'x': 9.0, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (11.25, -2.9),
            'door': (9.5, -0.9, 0.85, 'S_IN_LEFT'),
            'font_size': 9.0
        },
        {
            'id': 'T1_P6_HUE', 'name': 'Phòng số 6 (Huệ)',
            'x': 13.5, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (15.75, -2.9),
            'door': (14.0, -0.9, 0.85, 'S_IN_LEFT'),
            'font_size': 9.0
        },

        # Cánh Đông Nam (X: 23.0 to 41.0m) - 3 phòng
        {
            'id': 'T1_P7_VP', 'name': 'Phòng số 7(VP)',
            'x': 23.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (25.5, -2.9),
            'door': (23.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'T1_PKT', 'name': 'Phòng Kế toán',
            'x': 28.0, 'y': -4.9, 'w': 6.5, 'h': 4.0,
            'text_center': (31.25, -2.9),
            'door': (28.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T1_PDANH', 'name': 'Phòng Danh',
            'x': 34.5, 'y': -4.9, 'w': 6.5, 'h': 4.0,
            'text_center': (37.75, -2.9),
            'door': (35.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },

        # =========================================================
        # === TÒA 2: KHỐI PHÒNG XÉT XỬ PHÍA BẮC (Y: 7.0 to 13.0m) ===
        # =========================================================
        {
            'id': 'T2_XX2', 'name': 'Phòng xét xử 2',
            'x': X_TOA2_L, 'y': Y_TOA2_BOT, 'w': 10.0, 'h': 6.0,
            'text_center': (20.5, (Y_TOA2_BOT + Y_TOA2_TOP) / 2.0),
            'door': (19.65, Y_TOA2_BOT, 0.85, 'T2_DOUBLE_DOOR'),
            'font_size': 11.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHIC (GROUND FLOOR - SẢNH TẦNG 1)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 19.2, 1.4, 2.6, 2.6
    # Staircase background matches lobby tone
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

    # ---------------------------------------------------------
    # 6. EXTERIOR STEPS & OUTDOOR ACCESS
    # ---------------------------------------------------------
    # South Main Entrance Steps (Bậc tam cấp mặt tiền: Y = -4.9 to -5.7m, X = 18.0 to 23.0m)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([X_LOBBY_L, X_LOBBY_R], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Outdoor Side Steps at West & East Corridor Exits (Open Ends)
    # West Corridor Side Steps (X: -1.25 to 0.0, Y: -0.9 to 0.9)
    for i in range(5):
        dx = -0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # East Corridor Side Steps (X: 41.0 to 42.25, Y: -0.9 to 0.9)
    for i in range(5):
        dx = X_MAX + 0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([X_MAX, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([X_MAX, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Corridor & Lobby Annotations
    ax.text(20.5, -2.9, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(9.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(32.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(20.5, 5.5, 'HÀNH LANG NỐI', color=COLOR_TEXT_MUTED, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 7. DRAW WALLS (PRECISION ALIGNED WITH DOOR OPENINGS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # === TÒA 1: EXTERIOR ENVELOPE WALLS (WALL_THICKNESS = 0.22m) ===
    # Tòa 1 Outer West Wall (Open at Corridor Y: -0.9 to 0.9)
    draw_wall(-W, -4.9 - W, W, 4.0 + W)
    draw_wall(-W, 0.9, W, 4.5 + W)

    # Tòa 1 Outer East Wall (Open at Corridor Y: -0.9 to 0.9)
    draw_wall(X_MAX, -4.9 - W, W, 4.0 + W)
    draw_wall(X_MAX, 0.9, W, 4.5 + W)

    # Tòa 1 South Bottom Wall (Y = -4.9m, Open for Main Entrance at X: 18.0 to 23.0)
    draw_wall(-W, -4.9 - W, X_LOBBY_L + W, W)
    draw_wall(X_LOBBY_R, -4.9 - W, (X_MAX - X_LOBBY_R) + W, W)

    # Tòa 1 South Entrance Cheek Walls (flushed with lobby inner edge)
    draw_wall(X_LOBBY_L - P, -5.7, P, 0.8)
    draw_wall(X_LOBBY_R, -5.7, P, 0.8)

    # Tòa 1 North Top Wall (Y = 5.4m, Open for Connecting Passage at X: 18.0 to 23.0)
    draw_wall(-W, 5.4, X_LOBBY_L + W, W)
    draw_wall(X_LOBBY_R, 5.4, (X_MAX - X_LOBBY_R) + W, W)

    # === CONNECTING PASSAGE WALLS (Between Tòa 1 and Tòa 2: Y = 5.4 to Y_TOA2_BOT) ===
    # Left Wall at X = 18.0m (outer face at 18.0 - P)
    draw_wall(X_LOBBY_L - P, 5.4, P, Y_TOA2_BOT - 5.4)
    # Right Wall at X = 23.0m (inner face at 23.0)
    draw_wall(X_LOBBY_R, 5.4, P, Y_TOA2_BOT - 5.4)

    # === TÒA 2: EXTERIOR ENVELOPE WALLS (WALL_THICKNESS = 0.22m) ===
    # Tòa 2 South Wall Segments (at Y = Y_TOA2_BOT):
    # Left overhang segment: X from 15.5 - W to 18.0
    draw_wall(X_TOA2_L - W, Y_TOA2_BOT - W, (X_LOBBY_L - X_TOA2_L) + W, W)
    # Right overhang segment: X from 23.0 to 25.5 + W
    draw_wall(X_LOBBY_R, Y_TOA2_BOT - W, (X_TOA2_R - X_LOBBY_R) + W, W)

    # Tòa 2 Entrance Wall at Y = Y_TOA2_BOT (Between X = 18.0 and 23.0, with double door opening 1.7m at 19.65 to 21.35)
    draw_wall(X_LOBBY_L, Y_TOA2_BOT - P, 19.65 - X_LOBBY_L, P)
    draw_wall(21.35, Y_TOA2_BOT - P, X_LOBBY_R - 21.35, P)

    # Tòa 2 West Wall: X = 15.5 - W to 15.5, Y = Y_TOA2_BOT to Y_TOA2_TOP
    draw_wall(X_TOA2_L - W, Y_TOA2_BOT, W, (Y_TOA2_TOP - Y_TOA2_BOT) + W)

    # Tòa 2 East Wall: X = 25.5 to 25.5 + W, Y = Y_TOA2_BOT to Y_TOA2_TOP
    draw_wall(X_TOA2_R, Y_TOA2_BOT, W, (Y_TOA2_TOP - Y_TOA2_BOT) + W)

    # Tòa 2 North Top Wall: Y = Y_TOA2_TOP to Y_TOA2_TOP + W, X = 15.5 - W to 25.5 + W
    draw_wall(X_TOA2_L - W, Y_TOA2_TOP, (X_TOA2_R - X_TOA2_L) + 2*W, W)

    # === TÒA 1: INTERIOR CORRIDOR & PARTITION WALLS (PART_THICKNESS = 0.08m) ===
    # 1. South Corridor Wall along Y = -0.9m (Partition between South Rooms & Corridor)
    # Cánh Tây Nam (X: 0.0 to 18.0): Doors at (3.3 to 4.15), (5.0 to 5.85), (9.5 to 10.35), (14.0 to 14.85)
    sw_door_segments = [
        (0.0, 3.3),
        (4.15, 5.0),
        (5.85, 9.5),
        (10.35, 14.0),
        (14.85, 18.0)
    ]
    for seg_x0, seg_x1 in sw_door_segments:
        draw_wall(seg_x0, -0.9 - P/2, seg_x1 - seg_x0, P)

    # Cánh Đông Nam (X: 23.0 to 41.0): Doors at (23.5 to 24.35), (28.5 to 29.35), (35.0 to 35.85)
    se_door_segments = [
        (23.0, 23.5),
        (24.35, 28.5),
        (29.35, 35.0),
        (35.85, 41.0)
    ]
    for seg_x0, seg_x1 in se_door_segments:
        draw_wall(seg_x0, -0.9 - P/2, seg_x1 - seg_x0, P)

    # 2. North Corridor Wall along Y = 0.9m (Partition between North Rooms & Corridor)
    # Cánh Tây Bắc (X: 0.0 to 18.0): Doors at (3.6 to 4.45), (5.2 to 6.05), (10.0 to 10.85), (14.4 to 15.25)
    nw_door_segments = [
        (0.0, 3.6),
        (4.45, 5.2),
        (6.05, 10.0),
        (10.85, 14.4),
        (15.25, 18.0)
    ]
    for seg_x0, seg_x1 in nw_door_segments:
        draw_wall(seg_x0, 0.9 - P/2, seg_x1 - seg_x0, P)

    # Cánh Đông Bắc (X: 23.0 to 41.0): Doors at (23.4 to 24.25), (27.9 to 28.75), (32.4 to 33.25), (36.9 to 37.75)
    ne_door_segments = [
        (23.0, 23.4),
        (24.25, 27.9),
        (28.75, 32.4),
        (33.25, 36.9),
        (37.75, 41.0)
    ]
    for seg_x0, seg_x1 in ne_door_segments:
        draw_wall(seg_x0, 0.9 - P/2, seg_x1 - seg_x0, P)

    # 3. Vertical Room Partitions (Tường ngăn giữa các phòng)
    # North Wing vertical partitions (Y: 0.9 to 5.4m)
    for px in [4.8, 9.6, 14.0, 18.0, 23.0, 27.5, 32.0, 36.5]:
        draw_wall(px - P/2, 0.9, P, 4.5)

    # South Wing vertical partitions (Y: -4.9 to -0.9m)
    for px in [4.5, 9.0, 13.5, 18.0, 23.0, 28.0, 34.5]:
        draw_wall(px - P/2, -4.9, P, 4.0)

    # ---------------------------------------------------------
    # 8. WINDOWS SPECIFICATION & RENDERING
    # ---------------------------------------------------------
    def draw_window_horizontal(x0, x1, y):
        # Draw 2 crisp glass lines inside the wall width
        ax.plot([x0, x1], [y + 0.07, y + 0.07], color=COLOR_WALL, linewidth=1.3, zorder=12)
        ax.plot([x0, x1], [y - 0.07, y - 0.07], color=COLOR_WALL, linewidth=1.3, zorder=12)

    def draw_window_vertical(x, y0, y1):
        ax.plot([x + 0.07, x + 0.07], [y0, y1], color=COLOR_WALL, linewidth=1.3, zorder=12)
        ax.plot([x - 0.07, x - 0.07], [y0, y1], color=COLOR_WALL, linewidth=1.3, zorder=12)

    # Windows on Tòa 1 North Wall (Y = 5.4 + W/2)
    t1_north_windows = [
        (1.4, 3.4), (6.2, 8.2), (10.8, 12.8), (15.0, 17.0),
        (24.2, 26.2), (28.7, 30.7), (33.2, 35.2), (37.7, 39.7)
    ]
    for wx0, wx1 in t1_north_windows:
        draw_window_horizontal(wx0, wx1, 5.4 + W/2)

    # Windows on Tòa 1 South Wall (Y = -4.9 - W/2)
    t1_south_windows = [
        (1.2, 3.2), (5.7, 7.7), (10.2, 12.2), (14.7, 16.7),
        (24.5, 26.5), (30.0, 32.5), (36.5, 39.0)
    ]
    for wx0, wx1 in t1_south_windows:
        draw_window_horizontal(wx0, wx1, -4.9 - W/2)

    # Windows on Tòa 1 West End Wall (X = -W/2)
    draw_window_vertical(-W/2, -3.9, -1.9)
    draw_window_vertical(-W/2, 2.1, 4.1)

    # Windows on Tòa 1 East End Wall (X = X_MAX + W/2)
    draw_window_vertical(X_MAX + W/2, -3.9, -1.9)
    draw_window_vertical(X_MAX + W/2, 2.1, 4.1)

    # Windows on Tòa 2 (Khối phòng xét xử 2)
    # West wall (X = X_TOA2_L - W/2)
    draw_window_vertical(X_TOA2_L - W/2, Y_TOA2_BOT + 1.0, Y_TOA2_BOT + 2.6)
    draw_window_vertical(X_TOA2_L - W/2, Y_TOA2_BOT + 3.4, Y_TOA2_BOT + 5.0)
    # East wall (X = X_TOA2_R + W/2)
    draw_window_vertical(X_TOA2_R + W/2, Y_TOA2_BOT + 1.0, Y_TOA2_BOT + 2.6)
    draw_window_vertical(X_TOA2_R + W/2, Y_TOA2_BOT + 3.4, Y_TOA2_BOT + 5.0)
    # North wall (Y = Y_TOA2_TOP + W/2)
    draw_window_horizontal(17.5, 19.5, Y_TOA2_TOP + W/2)
    draw_window_horizontal(21.5, 23.5, Y_TOA2_TOP + W/2)
    # South overhang walls (overlooking courtyard)
    draw_window_horizontal(16.0, 17.5, Y_TOA2_BOT - W/2)
    draw_window_horizontal(23.5, 25.0, Y_TOA2_BOT - W/2)

    # ---------------------------------------------------------
    # 9. DOORS RENDERING (WITH SWING ARCS)
    # ---------------------------------------------------------
    def draw_door(dx, dy, dw, dtype):
        if dtype == 'N_IN_RIGHT':
            # Door at North wall of corridor (Y = 0.9m), hinged at dx, swings inward up-right
            ax.plot([dx, dx], [dy, dy + dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((dx, dy), dw*2, dw*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)
        elif dtype == 'N_IN_LEFT':
            # Door at North wall of corridor, hinged at dx + dw, swings inward up-left
            hx = dx + dw
            ax.plot([hx, hx], [dy, dy + dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((hx, dy), dw*2, dw*2, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)
        elif dtype == 'S_IN_RIGHT':
            # Door at South wall of corridor (Y = -0.9m), hinged at dx, swings inward down-right
            ax.plot([dx, dx], [dy, dy - dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((dx, dy), dw*2, dw*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)
        elif dtype == 'S_IN_LEFT':
            # Door at South wall of corridor, hinged at dx + dw, swings inward down-left
            hx = dx + dw
            ax.plot([hx, hx], [dy, dy - dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((hx, dy), dw*2, dw*2, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)
        elif dtype == 'T2_DOUBLE_DOOR':
            # Double door at Y = Y_TOA2_BOT into Courtroom 2 (centered at X = 20.5m)
            # Left leaf hinged at 19.65m, swings up-right
            ax.plot([19.65, 19.65], [dy, dy + dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc1 = patches.Arc((19.65, dy), dw*2, dw*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc1)
            # Right leaf hinged at 21.35m, swings up-left
            ax.plot([21.35, 21.35], [dy, dy + dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc2 = patches.Arc((21.35, dy), dw*2, dw*2, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc2)

    for r in rooms:
        dx, dy, dw, dtype = r['door']
        draw_door(dx, dy, dw, dtype)

    # ---------------------------------------------------------
    # 10. ROOM LABELS & TEXT
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'], 
                fontweight='bold', ha='center', va='center', zorder=20)

    # ---------------------------------------------------------
    # 11. EXPORT & SAVE
    # ---------------------------------------------------------
    output_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\DongNai\DongNai12\Tang1"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "mat_bang_tang_1.png")

    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close(fig)
    print(f"Bản vẽ đã được xuất thành công tại: {output_path}")

if __name__ == '__main__':
    create_floorplan_tang1()
