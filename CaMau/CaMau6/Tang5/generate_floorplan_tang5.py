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

def create_floorplan_tang5(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_5.png')

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 16), dpi=300)
    ax = fig.add_axes([0.03, 0.04, 0.94, 0.90])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_ROOF_FILL = '#ffffff'     # Pure white for roof block
    COLOR_STAIR_FILL = '#ffffff'    # Pure white stair background for Upper Floors
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text

    WALL_THICKNESS = 0.22           # Exterior wall thickness
    PART_THICKNESS = 0.12           # Interior partition thickness
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # Overall Coordinate Grid (meters)
    X_MIN = 0.0
    X_MAX = 48.0
    X_WING_L = 8.0     # West Wing boundary
    X_WING_R = 40.0    # East Wing boundary
    X_BRIDGE_L = 21.0  # Central Bridge / Lobby West boundary
    X_BRIDGE_R = 27.0  # Central Bridge / Lobby East boundary

    # Tòa 1 Vertical coordinates:
    Y_A_CORR_BOT = -0.9
    Y_A_CORR_TOP = 0.9
    Y_A_BODY_BOT = -4.5
    Y_A_BODY_TOP = 4.5
    Y_A_WING_BOT = -6.2
    Y_A_WING_TOP = 6.2

    # Central Connecting Bridge Link:
    Y_BRIDGE_BOT = 4.5
    Y_BRIDGE_TOP = 11.0

    # Tòa 2 (Khối Xét xử) Vertical coordinates:
    Y_B_BODY_BOT = 11.0
    Y_B_BODY_TOP = 20.6
    Y_B_WING_BOT = 9.4
    Y_B_WING_TOP = 22.2

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.04, 0.962, 'MẶT BẰNG TẦNG 5  —  TÒA ÁN NHÂN DÂN KHU VỰC 6 - CÀ MAU', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.04, 0.96], [0.945, 0.945], transform=fig.transFigure, color='#e2e8f0', linewidth=1.2)
    fig.lines.append(header_line)

    # Legend Box at Bottom Center (5 items: Hành lang/sảnh, Tường/vách, Cửa sổ, Cửa đi mở vào, Mái che)
    lg_x, lg_y = 7.0, -8.6
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.38, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.06, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 7.5, lg_y + 0.11), 1.2, 0.16, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 9.0, lg_y + 0.06, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window (White opening with double border lines)
    ax.add_patch(patches.Rectangle((lg_x + 15.0, lg_y + 0.07), 1.2, 0.22, facecolor='#ffffff', edgecolor='none', zorder=1))
    ax.plot([lg_x + 15.0, lg_x + 16.2], [lg_y + 0.24, lg_y + 0.24], color=COLOR_WALL, linewidth=1.2, zorder=2)
    ax.plot([lg_x + 15.0, lg_x + 16.2], [lg_y + 0.11, lg_y + 0.11], color=COLOR_WALL, linewidth=1.2, zorder=2)
    ax.text(lg_x + 16.5, lg_y + 0.06, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 22.0, lg_x + 22.0], [lg_y + 0.02, lg_y + 0.34], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=1)
    arc_lg = patches.Arc((lg_x + 22.0, lg_y + 0.02), 0.64, 0.64, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 23.3, lg_y + 0.06, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 5: Roof (Mái che)
    ax.add_patch(patches.Rectangle((lg_x + 29.5, lg_y), 1.2, 0.38, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=1.2, zorder=1))
    ax.text(lg_x + 31.0, lg_y + 0.06, 'Mái che', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (PASTEL BLUE-GREY)
    # ---------------------------------------------------------
    # Tòa 1 Horizontal Corridor (X: 0.0 to 48.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, Y_A_CORR_BOT), X_MAX, Y_A_CORR_TOP - Y_A_CORR_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 South Sảnh Tầng 5 (X: 21.0 to 27.0, Y: -4.5 to -0.9)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_A_BODY_BOT), X_BRIDGE_R - X_BRIDGE_L, Y_A_CORR_BOT - Y_A_BODY_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 North Stair Landing (X: 21.0 to 27.0, Y: 0.9 to 4.5)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_A_CORR_TOP), X_BRIDGE_R - X_BRIDGE_L, Y_A_BODY_TOP - Y_A_CORR_TOP, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOF AREA (MÁI CHE TÒA XÉT XỬ & NHỊP CẦU NỐI)
    # ---------------------------------------------------------
    # Footprint polygon of 4-story rear building & bridge:
    roof_poly_coords = [
        (X_BRIDGE_L, Y_BRIDGE_BOT),     # (21.0, 4.5) Bridge at Tòa 1 North Wall
        (X_BRIDGE_L, Y_BRIDGE_TOP),     # (21.0, 11.0) Bridge to Tòa 2 South wall
        (X_WING_L, Y_B_BODY_BOT),       # (8.0, 11.0) Tòa 2 South body West
        (X_WING_L, Y_B_WING_BOT),       # (8.0, 9.4) West wing inner corner
        (X_MIN, Y_B_WING_BOT),          # (0.0, 9.4) West wing South facade
        (X_MIN, Y_B_WING_TOP),          # (0.0, 22.2) West wing outer facade
        (X_WING_L, Y_B_WING_TOP),       # (8.0, 22.2) West wing North facade
        (X_WING_L, Y_B_BODY_TOP),       # (8.0, 20.6) West wing inner corner
        (X_WING_R, Y_B_BODY_TOP),       # (40.0, 20.6) Main body North facade
        (X_WING_R, Y_B_WING_TOP),       # (40.0, 22.2) East wing inner corner
        (X_MAX, Y_B_WING_TOP),          # (48.0, 22.2) East wing North facade
        (X_MAX, Y_B_WING_BOT),          # (48.0, 9.4) East wing outer facade
        (X_WING_R, Y_B_WING_BOT),       # (40.0, 9.4) East wing South facade
        (X_WING_R, Y_B_BODY_BOT),       # (40.0, 11.0) East wing inner corner
        (X_BRIDGE_R, Y_BRIDGE_TOP),     # (27.0, 11.0) Tòa 2 South body East
        (X_BRIDGE_R, Y_BRIDGE_BOT),     # (27.0, 4.5) Bridge at Tòa 1 North Wall
    ]
    roof_patch = patches.Polygon(roof_poly_coords, closed=True, 
                                 facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, 
                                 linewidth=1.8, zorder=2)
    ax.add_patch(roof_patch)

    # Prominent MÁI CHE text label in center of Tòa 2 Roof Block
    ax.text(24.0, 15.8, 'MÁI CHE', color=COLOR_TEXT_MUTED, fontsize=16.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 5. ROOM DEFINITIONS & BACKGROUND FILLS (PURE WHITE)
    # ---------------------------------------------------------
    # TÒA 1: ĐÚNG 10 PHÒNG LÀM VIỆC THEO PROMPT TẦNG 5
    toa1_rooms: List[RoomDict] = [
        # South Row (6 phòng):
        {'id': 'T1_P1', 'name': 'Phòng làm việc', 'x': 0.0, 'y': Y_A_WING_BOT, 'w': 8.0, 'h': Y_A_CORR_BOT - Y_A_WING_BOT,
         'text_center': (4.0, (Y_A_WING_BOT + Y_A_CORR_BOT)/2.0), 'door': (6.2, Y_A_CORR_BOT, 0.9, 'S_IN_RIGHT'), 'font_size': 10.5},
        {'id': 'T1_P2', 'name': 'Phòng làm việc', 'x': 8.0, 'y': Y_A_BODY_BOT, 'w': 6.5, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
         'text_center': (11.25, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0), 'door': (9.2, Y_A_CORR_BOT, 0.9, 'S_IN_RIGHT'), 'font_size': 10.0},
        {'id': 'T1_P3', 'name': 'Phòng làm việc', 'x': 14.5, 'y': Y_A_BODY_BOT, 'w': 6.5, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
         'text_center': (17.75, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0), 'door': (15.8, Y_A_CORR_BOT, 0.9, 'S_IN_RIGHT'), 'font_size': 10.0},
        {'id': 'T1_P4', 'name': 'Phòng làm việc', 'x': 27.0, 'y': Y_A_BODY_BOT, 'w': 6.5, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
         'text_center': (30.25, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0), 'door': (32.2, Y_A_CORR_BOT, 0.9, 'S_IN_LEFT'), 'font_size': 10.0},
        {'id': 'T1_P5', 'name': 'Phòng làm việc', 'x': 33.5, 'y': Y_A_BODY_BOT, 'w': 6.5, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
         'text_center': (36.75, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0), 'door': (38.5, Y_A_CORR_BOT, 0.9, 'S_IN_LEFT'), 'font_size': 10.0},
        {'id': 'T1_P6', 'name': 'Phòng làm việc', 'x': 40.0, 'y': Y_A_WING_BOT, 'w': 8.0, 'h': Y_A_CORR_BOT - Y_A_WING_BOT,
         'text_center': (44.0, (Y_A_WING_BOT + Y_A_CORR_BOT)/2.0), 'door': (41.8, Y_A_CORR_BOT, 0.9, 'S_IN_LEFT'), 'font_size': 10.5},
        # North Row (4 phòng):
        {'id': 'T1_P7', 'name': 'Phòng làm việc', 'x': 0.0, 'y': Y_A_CORR_TOP, 'w': 8.0, 'h': Y_A_WING_TOP - Y_A_CORR_TOP,
         'text_center': (4.0, (Y_A_CORR_TOP + Y_A_WING_TOP)/2.0), 'door': (6.2, Y_A_CORR_TOP, 0.9, 'N_IN_RIGHT'), 'font_size': 10.5},
        {'id': 'T1_P8', 'name': 'Phòng làm việc', 'x': 8.0, 'y': Y_A_CORR_TOP, 'w': 13.0, 'h': Y_A_BODY_TOP - Y_A_CORR_TOP,
         'text_center': (14.5, (Y_A_CORR_TOP + Y_A_BODY_TOP)/2.0), 'door': (9.2, Y_A_CORR_TOP, 0.9, 'N_IN_RIGHT'), 'font_size': 11.0},
        {'id': 'T1_P9', 'name': 'Phòng làm việc', 'x': 27.0, 'y': Y_A_CORR_TOP, 'w': 13.0, 'h': Y_A_BODY_TOP - Y_A_CORR_TOP,
         'text_center': (33.5, (Y_A_CORR_TOP + Y_A_BODY_TOP)/2.0), 'door': (38.5, Y_A_CORR_TOP, 0.9, 'N_IN_LEFT'), 'font_size': 11.0},
        {'id': 'T1_P10', 'name': 'Phòng làm việc', 'x': 40.0, 'y': Y_A_CORR_TOP, 'w': 8.0, 'h': Y_A_WING_TOP - Y_A_CORR_TOP,
         'text_center': (44.0, (Y_A_CORR_TOP + Y_A_WING_TOP)/2.0), 'door': (41.8, Y_A_CORR_TOP, 0.9, 'N_IN_LEFT'), 'font_size': 10.5},
    ]

    for r in toa1_rooms:
        ax.add_patch(patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))

    # ---------------------------------------------------------
    # 6. STAIRCASES (WHITE BACKGROUND FOR UPPER FLOORS)
    # ---------------------------------------------------------
    # --- CẦU THANG A (TÒA 1) ---
    stair_a_x, stair_a_y = 23.5, 1.2
    stair_a_w, stair_a_h = 3.3, 3.0
    num_steps = 11

    ax.add_patch(patches.Rectangle((stair_a_x, stair_a_y), stair_a_w, stair_a_h,
                                   facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.2, zorder=6))
    ax.plot([stair_a_x + stair_a_w/2, stair_a_x + stair_a_w/2], [stair_a_y, stair_a_y + stair_a_h], color=COLOR_WALL, linewidth=1.0, zorder=7)
    for i in range(1, num_steps):
        sy = stair_a_y + i * (stair_a_h / num_steps)
        ax.plot([stair_a_x, stair_a_x + stair_a_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=7)
    ax.annotate('', xy=(stair_a_x + stair_a_w*0.5, stair_a_y + 0.3), xytext=(stair_a_x + stair_a_w*0.5, stair_a_y + stair_a_h - 0.3),
                arrowprops=dict(arrowstyle="->", color=COLOR_WALL, lw=1.2), zorder=8)
    ax.text(stair_a_x + stair_a_w/2, stair_a_y - 0.25, 'Cầu thang A\n(Xuống tầng 4)', color=COLOR_TEXT_MUTED, fontsize=8.0, ha='center', va='top', zorder=8)

    # ---------------------------------------------------------
    # 7. STRUCTURAL WALLS & PARTITIONS (DARK SLATE)
    # ---------------------------------------------------------
    def draw_wall(x1: float, y1: float, x2: float, y2: float, thick: float = W, z: int = 10):
        if abs(y1 - y2) < 1e-4:  # Horizontal
            xmin, xmax = min(x1, x2), max(x1, x2)
            ax.add_patch(patches.Rectangle((xmin, y1 - thick/2), xmax - xmin, thick, facecolor=COLOR_WALL, edgecolor='none', zorder=z))
        elif abs(x1 - x2) < 1e-4:  # Vertical
            ymin, ymax = min(y1, y2), max(y1, y2)
            ax.add_patch(patches.Rectangle((x1 - thick/2, ymin), thick, ymax - ymin, facecolor=COLOR_WALL, edgecolor='none', zorder=z))

    # === TÒA 1 NGOẠI THẤT (ENCLOSED SOLID WALLS) ===
    # South Facade:
    draw_wall(0.0, Y_A_WING_BOT, 8.0, Y_A_WING_BOT)
    draw_wall(8.0, Y_A_WING_BOT, 8.0, Y_A_BODY_BOT)
    draw_wall(8.0, Y_A_BODY_BOT, 40.0, Y_A_BODY_BOT)
    draw_wall(40.0, Y_A_WING_BOT, 40.0, Y_A_BODY_BOT)
    draw_wall(40.0, Y_A_WING_BOT, 48.0, Y_A_WING_BOT)

    # West & East Outer Walls:
    draw_wall(0.0, Y_A_WING_BOT, 0.0, Y_A_WING_TOP)
    draw_wall(48.0, Y_A_WING_BOT, 48.0, Y_A_WING_TOP)

    # North Facade (Enclosed continuous facade with window at stair landing):
    draw_wall(0.0, Y_A_WING_TOP, 8.0, Y_A_WING_TOP)
    draw_wall(8.0, Y_A_BODY_TOP, 8.0, Y_A_WING_TOP)
    draw_wall(8.0, Y_A_BODY_TOP, 40.0, Y_A_BODY_TOP)
    draw_wall(40.0, Y_A_BODY_TOP, 40.0, Y_A_WING_TOP)
    draw_wall(40.0, Y_A_WING_TOP, 48.0, Y_A_WING_TOP)

    # === TÒA 1 NỘI THẤT VÁCH NGĂN (10 PHÒNG) ===
    # South Corridor Wall (Y = -0.9m) with aligned door openings:
    draw_wall(0.0, Y_A_CORR_BOT, 6.2, Y_A_CORR_BOT, thick=P)
    draw_wall(7.1, Y_A_CORR_BOT, 9.2, Y_A_CORR_BOT, thick=P)
    draw_wall(10.1, Y_A_CORR_BOT, 15.8, Y_A_CORR_BOT, thick=P)
    draw_wall(16.7, Y_A_CORR_BOT, 21.0, Y_A_CORR_BOT, thick=P)
    # Sảnh Tầng 5 mở rộng X: 21.0 to 27.0
    draw_wall(27.0, Y_A_CORR_BOT, 31.3, Y_A_CORR_BOT, thick=P)
    draw_wall(32.2, Y_A_CORR_BOT, 37.6, Y_A_CORR_BOT, thick=P)
    draw_wall(38.5, Y_A_CORR_BOT, 40.9, Y_A_CORR_BOT, thick=P)
    draw_wall(41.8, Y_A_CORR_BOT, 48.0, Y_A_CORR_BOT, thick=P)

    # North Corridor Wall (Y = 0.9m) with aligned door openings:
    draw_wall(0.0, Y_A_CORR_TOP, 6.2, Y_A_CORR_TOP, thick=P)
    draw_wall(7.1, Y_A_CORR_TOP, 9.2, Y_A_CORR_TOP, thick=P)
    draw_wall(10.1, Y_A_CORR_TOP, 21.0, Y_A_CORR_TOP, thick=P)
    # Lối thông Cầu thang A tại X: 21.0 to 27.0
    draw_wall(27.0, Y_A_CORR_TOP, 37.6, Y_A_CORR_TOP, thick=P)
    draw_wall(38.5, Y_A_CORR_TOP, 40.9, Y_A_CORR_TOP, thick=P)
    draw_wall(41.8, Y_A_CORR_TOP, 48.0, Y_A_CORR_TOP, thick=P)

    # Vertical Partitions Tòa 1:
    draw_wall(8.0, Y_A_BODY_BOT, 8.0, Y_A_CORR_BOT, thick=P)
    draw_wall(14.5, Y_A_BODY_BOT, 14.5, Y_A_CORR_BOT, thick=P)
    draw_wall(21.0, Y_A_BODY_BOT, 21.0, Y_A_CORR_BOT, thick=P)
    draw_wall(27.0, Y_A_BODY_BOT, 27.0, Y_A_CORR_BOT, thick=P)
    draw_wall(33.5, Y_A_BODY_BOT, 33.5, Y_A_CORR_BOT, thick=P)
    draw_wall(40.0, Y_A_BODY_BOT, 40.0, Y_A_CORR_BOT, thick=P)

    draw_wall(8.0, Y_A_CORR_TOP, 8.0, Y_A_BODY_TOP, thick=P)
    draw_wall(21.0, Y_A_CORR_TOP, 21.0, Y_A_BODY_TOP, thick=P)
    draw_wall(27.0, Y_A_CORR_TOP, 27.0, Y_A_BODY_TOP, thick=P)
    draw_wall(40.0, Y_A_CORR_TOP, 40.0, Y_A_BODY_TOP, thick=P)

    # ---------------------------------------------------------
    # 8. WINDOWS (WHITE OPENING CUT WITH DOUBLE PARALLEL LINES)
    # ---------------------------------------------------------
    def draw_window_h(x1: float, x2: float, y: float, thick: float = W):
        xmin, xmax = min(x1, x2), max(x1, x2)
        # White opening patch cutting through the wall
        ax.add_patch(patches.Rectangle((xmin, y - thick/2 - 0.03), xmax - xmin, thick + 0.06, facecolor='#ffffff', edgecolor='none', zorder=11))
        # Top and bottom frame lines
        ax.plot([xmin, xmax], [y - thick/2 + 0.04, y - thick/2 + 0.04], color=COLOR_WALL, linewidth=1.2, zorder=12)
        ax.plot([xmin, xmax], [y + thick/2 - 0.04, y + thick/2 - 0.04], color=COLOR_WALL, linewidth=1.2, zorder=12)

    def draw_window_v(x: float, y1: float, y2: float, thick: float = W):
        ymin, ymax = min(y1, y2), max(y1, y2)
        # White opening patch cutting through the wall
        ax.add_patch(patches.Rectangle((x - thick/2 - 0.03, ymin), thick + 0.06, ymax - ymin, facecolor='#ffffff', edgecolor='none', zorder=11))
        # Left and right frame lines
        ax.plot([x - thick/2 + 0.04, x - thick/2 + 0.04], [ymin, ymax], color=COLOR_WALL, linewidth=1.2, zorder=12)
        ax.plot([x + thick/2 - 0.04, x + thick/2 - 0.04], [ymin, ymax], color=COLOR_WALL, linewidth=1.2, zorder=12)

    # --- Windows Tòa 1 ---
    # South Windows:
    draw_window_h(2.5, 5.5, Y_A_WING_BOT)       # P1
    draw_window_h(9.5, 13.0, Y_A_BODY_BOT)      # P2
    draw_window_h(16.0, 19.5, Y_A_BODY_BOT)     # P3
    draw_window_h(22.5, 25.5, Y_A_BODY_BOT)     # Sảnh Tầng 5
    draw_window_h(28.5, 32.0, Y_A_BODY_BOT)     # P4
    draw_window_h(35.0, 38.5, Y_A_BODY_BOT)     # P5
    draw_window_h(42.5, 45.5, Y_A_WING_BOT)     # P6

    # North Windows:
    draw_window_h(2.5, 5.5, Y_A_WING_TOP)       # P7
    draw_window_h(11.0, 18.0, Y_A_BODY_TOP)     # P8
    draw_window_h(22.5, 25.5, Y_A_BODY_TOP)     # Stair Landing Window looking to Roof
    draw_window_h(30.0, 37.0, Y_A_BODY_TOP)     # P9
    draw_window_h(42.5, 45.5, Y_A_WING_TOP)     # P10

    # East & West End Corridor Windows:
    draw_window_v(0.0, -0.6, 0.6)
    draw_window_v(48.0, -0.6, 0.6)

    # ---------------------------------------------------------
    # 9. DOORS & DOOR SWINGS
    # ---------------------------------------------------------
    def draw_door(x: float, y: float, size: float, mode: str):
        if mode == 'S_IN_RIGHT':
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_LEFT':
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=180, theta2=270,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'N_IN_RIGHT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'N_IN_LEFT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)

    # Draw Doors for Tòa 1 Rooms:
    for r in toa1_rooms:
        dx, dy, dsize, dmode = r['door']
        draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 10. ROOM & CIRCULATION LABELS (CLEAN, SINGLE-LINE)
    # ---------------------------------------------------------
    # Tòa 1 Room Labels (10 Phòng làm việc):
    for r in toa1_rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 10.0)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                fontweight='bold', ha='center', va='center', zorder=15)

    # Circulation Labels:
    ax.text(14.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=15)
    ax.text(33.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=15)
    ax.text(24.0, -2.7, 'SẢNH TẦNG 5', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=15)

    # ---------------------------------------------------------
    # 11. EXPORT OUTPUTS
    # ---------------------------------------------------------
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Successfully generated floorplan image at: {out_img_path}")

if __name__ == '__main__':
    target_dir = r'c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau6\Tang5'
    create_floorplan_tang5(target_dir)
