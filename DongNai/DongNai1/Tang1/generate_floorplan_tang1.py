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
    fig = plt.figure(figsize=(26, 12), dpi=300)
    ax = fig.add_axes([0.02, 0.06, 0.96, 0.86])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # Building Dimensions (Scaled I-Shape for high room capacity)
    X_MAX = 50.0
    X_WING_L = 8.0
    X_LOBBY_L = 22.0
    X_LOBBY_R = 28.0
    X_WING_R = 42.0

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 1 - Đồng Nai', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.03, 0.97], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    lg_x, lg_y = 0.0, -8.6
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.0, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.3, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.add_patch(patches.Rectangle((lg_x + 8.0, lg_y + 0.1), 1.0, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 9.3, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 16.0, lg_x + 17.2], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 16.0, lg_x + 17.2], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 17.5, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 24.0, lg_x + 24.0], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 24.0, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 25.0, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (I-SHAPE)
    # ---------------------------------------------------------
    # Main Horizontal Corridor (X: 0 to 50, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Front Main Lobby Space (X: 22.0 to 28.0, Y: -4.4 to -0.9)
    ax.add_patch(patches.Rectangle((X_LOBBY_L, -4.4), 6.0, 3.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Stair & Passage Hall Space (X: 22.0 to 28.0, Y: 0.9 to 4.4)
    ax.add_patch(patches.Rectangle((X_LOBBY_L, 0.9), 6.0, 3.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 1 — ĐỒNG NAI 1)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === NORTH ROW (Y > 0.9) ===
        # West: Phòng xét xử (X: 0.0 to 14.0, includes deep West Wing and part of Mid section)
        {
            'id': 'P1_XX', 'name': 'Phòng xét xử',
            'x': 0.0, 'y': 0.9, 'w': 14.0, 'h': 5.3,  # Wings extend to Y=6.2
            'text_center': (7.0, 3.5),
            'door': (12.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.0
        },
        # Phòng Nghị án (X: 14.0 to 18.0)
        {
            'id': 'P1_NA1', 'name': 'Phòng Nghị án',
            'x': 14.0, 'y': 0.9, 'w': 4.0, 'h': 3.5,
            'text_center': (16.0, 2.65),
            'door': (14.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        # Phòng Nghị án 2 (X: 18.0 to 22.0)
        {
            'id': 'P1_NA2', 'name': 'Phòng Nghị án 2',
            'x': 18.0, 'y': 0.9, 'w': 4.0, 'h': 3.5,
            'text_center': (20.0, 2.65),
            'door': (18.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        # East: 5 Phòng làm việc (X: 28.0 to 50.0)
        {
            'id': 'P1_LV1', 'name': 'Phòng làm việc 1',
            'x': 28.0, 'y': 0.9, 'w': 3.5, 'h': 3.5,
            'text_center': (29.75, 2.65),
            'door': (28.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P1_LV2', 'name': 'Phòng làm việc 2',
            'x': 31.5, 'y': 0.9, 'w': 3.5, 'h': 3.5,
            'text_center': (33.25, 2.65),
            'door': (32.0, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P1_LV3', 'name': 'Phòng làm việc 3',
            'x': 35.0, 'y': 0.9, 'w': 3.5, 'h': 3.5,
            'text_center': (36.75, 2.65),
            'door': (35.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P1_LV4', 'name': 'Phòng làm việc 4',
            'x': 38.5, 'y': 0.9, 'w': 3.5, 'h': 3.5,
            'text_center': (40.25, 2.65),
            'door': (39.0, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P1_LV5', 'name': 'Phòng làm việc 5',
            'x': 42.0, 'y': 0.9, 'w': 8.0, 'h': 5.3,  # East Wing extends to Y=6.2
            'text_center': (46.0, 3.55),
            'door': (43.0, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.0
        },

        # === SOUTH ROW (Y < -0.9) ===
        # West: Phòng tiếp đương sự (X: 0.0 to 15.0)
        {
            'id': 'P1_TDS', 'name': 'Phòng tiếp đương sự',
            'x': 0.0, 'y': -6.2, 'w': 15.0, 'h': 5.3,
            'text_center': (7.5, -3.5),
            'door': (13.5, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
        # Phòng Nhận đơn (X: 15.0 to 22.0) - right beside Main Entrance Lobby
        {
            'id': 'P1_ND', 'name': 'Phòng Nhận đơn',
            'x': 15.0, 'y': -4.4, 'w': 7.0, 'h': 3.5,
            'text_center': (18.5, -2.65),
            'door': (16.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        # East: 4 Phòng làm việc đương sự nhỏ (X: 28.0 to 50.0)
        {
            'id': 'P1_DS1', 'name': 'Phòng làm việc đương sự nhỏ 1',
            'x': 28.0, 'y': -4.4, 'w': 4.5, 'h': 3.5,
            'text_center': (30.25, -2.65),
            'door': (28.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P1_DS2', 'name': 'Phòng làm việc đương sự nhỏ 2',
            'x': 32.5, 'y': -4.4, 'w': 4.5, 'h': 3.5,
            'text_center': (34.75, -2.65),
            'door': (33.0, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P1_DS3', 'name': 'Phòng làm việc đương sự nhỏ 3',
            'x': 37.0, 'y': -4.4, 'w': 5.0, 'h': 3.5,
            'text_center': (39.5, -2.65),
            'door': (37.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P1_DS4', 'name': 'Phòng làm việc đương sự nhỏ 4',
            'x': 42.0, 'y': -6.2, 'w': 8.0, 'h': 5.3,
            'text_center': (46.0, -3.55),
            'door': (43.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
    ]

    # Draw Room Background Fills
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES & ENTRANCE/EXIT STEPS (TẦNG 1)
    # ---------------------------------------------------------
    # Central Staircase in North Passage
    stair_x, stair_y, stair_w, stair_h = 23.5, 1.2, 3.0, 2.8
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.0, ha='center', va='top', zorder=5)

    # Front Main Entrance Steps (Y = -4.4 to -5.2, X = 22.0 to 28.0)
    for sy in [-4.4, -4.56, -4.72, -4.88, -5.04, -5.20]:
        ax.plot([X_LOBBY_L, X_LOBBY_R], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Rear North Exit Steps (Y = 4.4 to 5.2, X = 22.0 to 28.0)
    for sy in [4.4, 4.56, 4.72, 4.88, 5.04, 5.20]:
        ax.plot([X_LOBBY_L, X_LOBBY_R], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Corridor End Steps (West exit: X < 0.0, East exit: X > 50.0)
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

    # Labels
    ax.text(25.0, -2.65, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(11.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(35.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior West & East Wing Outer Walls (corridor ends open)
    draw_wall(-W, -6.2 - W, W, 5.3 + W)
    draw_wall(-W, 0.9, W, 5.3 + W)
    draw_wall(X_MAX, -6.2 - W, W, 5.3 + W)
    draw_wall(X_MAX, 0.9, W, 5.3 + W)

    # North Exterior Walls
    draw_wall(-W, 6.2, X_WING_L + W, W)                         # West Wing top wall
    draw_wall(X_WING_L - P/2, 4.4, P, 1.8 + W)                  # West Wing inner vertical wall
    draw_wall(X_WING_L, 4.4, (X_LOBBY_L - X_WING_L) + P/2, W)   # Mid-West North wall
    draw_wall(X_LOBBY_R - P/2, 4.4, (X_WING_R - X_LOBBY_R) + P/2, W) # Mid-East North wall
    draw_wall(X_WING_R - P/2, 4.4, P, 1.8 + W)                  # East Wing inner vertical wall
    draw_wall(X_WING_R, 6.2, (X_MAX - X_WING_R) + W, W)        # East Wing top wall

    # South Exterior Walls
    draw_wall(-W, -6.2 - W, X_WING_L + W, W)                    # West Wing bottom wall
    draw_wall(X_WING_L - P/2, -6.2 - W, P, 1.8 + W)             # West Wing inner vertical wall
    draw_wall(X_WING_L, -4.4 - W, (X_LOBBY_L - X_WING_L) + P/2, W) # Mid-West South wall
    draw_wall(X_LOBBY_R - P/2, -4.4 - W, (X_WING_R - X_LOBBY_R) + P/2, W) # Mid-East South wall
    draw_wall(X_WING_R - P/2, -6.2 - W, P, 1.8 + W)             # East Wing inner vertical wall
    draw_wall(X_WING_R, -6.2 - W, (X_MAX - X_WING_R) + W, W)   # East Wing bottom wall

    # Entrance Cheek Walls
    draw_wall(X_LOBBY_L - P/2, -5.2, P, 0.8)
    draw_wall(X_LOBBY_R - P/2, -5.2, P, 0.8)
    draw_wall(X_LOBBY_L - P/2, 4.4, P, 0.8)
    draw_wall(X_LOBBY_R - P/2, 4.4, P, 0.8)
    # North exit hooks at Y = 5.2
    draw_wall(X_LOBBY_L - P/2, 5.2 - P, 0.5, P)
    draw_wall(X_LOBBY_R + P/2 - 0.5, 5.2 - P, 0.5, P)

    # Corridor Horizontal Partition Walls (Y = 0.9 & Y = -0.9) with door cutouts
    # North Line (Y = 0.9): Doors at 12.5 | 14.5 | 18.5 | 28.5, 32.0, 35.5, 39.0, 43.0
    draw_wall(0.0, 0.9 - P/2, 12.5, P)
    draw_wall(13.4, 0.9 - P/2, 1.1, P)
    draw_wall(15.3, 0.9 - P/2, 3.2, P)
    draw_wall(19.3, 0.9 - P/2, 2.7, P)
    # Mid-East North Line:
    draw_wall(28.0, 0.9 - P/2, 0.5, P)
    draw_wall(29.3, 0.9 - P/2, 2.7, P)
    draw_wall(32.8, 0.9 - P/2, 2.7, P)
    draw_wall(36.3, 0.9 - P/2, 2.7, P)
    draw_wall(39.8, 0.9 - P/2, 3.2, P)
    draw_wall(43.85, 0.9 - P/2, 6.15, P)

    # South Line (Y = -0.9): Doors at 13.5 | 16.0 | 28.5, 33.0, 37.5, 43.0
    draw_wall(0.0, -0.9 - P/2, 13.5, P)
    draw_wall(14.4, -0.9 - P/2, 1.6, P)
    draw_wall(16.85, -0.9 - P/2, 5.15, P)
    # Mid-East South Line:
    draw_wall(28.0, -0.9 - P/2, 0.5, P)
    draw_wall(29.3, -0.9 - P/2, 3.7, P)
    draw_wall(33.8, -0.9 - P/2, 3.7, P)
    draw_wall(38.3, -0.9 - P/2, 4.7, P)
    draw_wall(43.85, -0.9 - P/2, 6.15, P)

    # Internal Vertical Partitions
    # North Wing:
    draw_wall(14.0 - P/2, 0.9, P, 3.5)
    draw_wall(18.0 - P/2, 0.9, P, 3.5)
    draw_wall(22.0 - P/2, 0.9, P, 3.5)
    draw_wall(28.0 - P/2, 0.9, P, 3.5)
    draw_wall(31.5 - P/2, 0.9, P, 3.5)
    draw_wall(35.0 - P/2, 0.9, P, 3.5)
    draw_wall(38.5 - P/2, 0.9, P, 3.5)
    draw_wall(42.0 - P/2, 0.9, P, 5.3)

    # South Wing:
    draw_wall(15.0 - P/2, -4.4, P, 3.5)
    draw_wall(22.0 - P/2, -4.4, P, 3.5)
    draw_wall(28.0 - P/2, -4.4, P, 3.5)
    draw_wall(32.5 - P/2, -4.4, P, 3.5)
    draw_wall(37.0 - P/2, -4.4, P, 3.5)
    draw_wall(42.0 - P/2, -6.2, P, 5.3)

    # ---------------------------------------------------------
    # 7. DRAW WINDOWS
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

    # North Windows
    draw_window(3.0, 6.2, 4.0, W, is_horizontal=True)        # Phòng XX
    draw_window(9.5, 4.4, 3.0, W, is_horizontal=True)        # Phòng XX
    draw_window(15.0, 4.4, 2.0, W, is_horizontal=True)       # Nghị án 1
    draw_window(19.0, 4.4, 2.0, W, is_horizontal=True)       # Nghị án 2
    draw_window(29.0, 4.4, 1.5, W, is_horizontal=True)       # LV 1
    draw_window(32.5, 4.4, 1.5, W, is_horizontal=True)       # LV 2
    draw_window(36.0, 4.4, 1.5, W, is_horizontal=True)       # LV 3
    draw_window(39.5, 4.4, 1.5, W, is_horizontal=True)       # LV 4
    draw_window(44.5, 6.2, 3.5, W, is_horizontal=True)       # LV 5

    # South Windows
    draw_window(3.0, -6.2 - W, 4.0, W, is_horizontal=True)   # Tiếp đương sự
    draw_window(10.0, -4.4 - W, 3.0, W, is_horizontal=True)  # Tiếp đương sự
    draw_window(17.5, -4.4 - W, 2.5, W, is_horizontal=True)  # Nhận đơn
    draw_window(29.2, -4.4 - W, 2.0, W, is_horizontal=True)  # ĐS 1
    draw_window(33.7, -4.4 - W, 2.0, W, is_horizontal=True)  # ĐS 2
    draw_window(38.2, -4.4 - W, 2.0, W, is_horizontal=True)  # ĐS 3
    draw_window(44.5, -6.2 - W, 3.5, W, is_horizontal=True)  # ĐS 4

    # Outer West & East Windows
    draw_window(-W, 3.0, W, 2.0, is_horizontal=False)
    draw_window(-W, -4.5, W, 2.0, is_horizontal=False)
    draw_window(X_MAX, 3.0, W, 2.0, is_horizontal=False)
    draw_window(X_MAX, -4.5, W, 2.0, is_horizontal=False)

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
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                fontweight='bold', ha='center', va='center', zorder=15)

    ax.set_xlim(-3.0, 53.0)
    ax.set_ylim(-9.0, 8.5)

    out_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\DongNai\DongNai1\Tang1"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mat_bang_tang_1.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 1 đã xuất thành công tại: {out_path}")

if __name__ == "__main__":
    create_floorplan_tang1()
