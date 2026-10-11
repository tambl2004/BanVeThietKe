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

def create_floorplan_tang2(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_2.png')

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 16), dpi=300)
    ax = fig.add_axes([0.03, 0.04, 0.94, 0.90])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Spec Tang 2
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_STAIR_FILL = '#ffffff'    # Pure white stair background for Upper Floors (Spec Tang 2)
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

    # Tòa A Vertical coordinates:
    Y_A_CORR_BOT = -0.9
    Y_A_CORR_TOP = 0.9
    Y_A_BODY_BOT = -4.5
    Y_A_BODY_TOP = 4.5
    Y_A_WING_BOT = -6.2
    Y_A_WING_TOP = 6.2

    # Central Bridge Link:
    Y_BRIDGE_BOT = 4.5
    Y_BRIDGE_TOP = 11.0

    # Tòa B (Khối Xét xử) Vertical coordinates:
    Y_B_BODY_BOT = 11.0
    Y_B_BODY_TOP = 20.6
    Y_B_WING_BOT = 9.4
    Y_B_WING_TOP = 22.2

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.04, 0.962, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân tỉnh Cà Mau', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.04, 0.96], [0.945, 0.945], transform=fig.transFigure, color='#e2e8f0', linewidth=1.2)
    fig.lines.append(header_line)

    # Legend Box at Bottom Center
    lg_x, lg_y = 10.0, -8.6
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.38, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.06, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 8.5, lg_y + 0.11), 1.2, 0.16, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 10.0, lg_y + 0.06, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 17.0, lg_x + 18.2], [lg_y + 0.24, lg_y + 0.24], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 17.0, lg_x + 18.2], [lg_y + 0.09, lg_y + 0.09], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 18.5, lg_y + 0.06, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 24.5, lg_x + 24.5], [lg_y + 0.02, lg_y + 0.34], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=1)
    arc_lg = patches.Arc((lg_x + 24.5, lg_y + 0.02), 0.64, 0.64, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 25.8, lg_y + 0.06, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (PASTEL BLUE-GREY)
    # ---------------------------------------------------------
    # Tòa A Horizontal Corridor (X: 0.0 to 48.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, Y_A_CORR_BOT), X_MAX, Y_A_CORR_TOP - Y_A_CORR_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa A North Stair Hall (X: 21.0 to 27.0, Y: 0.9 to 4.5)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_A_CORR_TOP), X_BRIDGE_R - X_BRIDGE_L, Y_A_BODY_TOP - Y_A_CORR_TOP, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Central Connecting Bridge Link (X: 21.0 to 27.0, Y: 4.5 to 11.0)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_BRIDGE_BOT), X_BRIDGE_R - X_BRIDGE_L, Y_BRIDGE_TOP - Y_BRIDGE_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa B Central Lobby & Stair Hall (X: 21.0 to 27.0, Y: 11.0 to 20.6)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_B_BODY_BOT), X_BRIDGE_R - X_BRIDGE_L, Y_B_BODY_TOP - Y_B_BODY_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TÒA A: 12 PHÒNG | TÒA B: 2 PHÒNG XỬ ÁN)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = []

    # === TÒA A (12 PHÒNG) ===
    # --- Dãy Nam Tòa A (Y < -0.9m) ---
    # Phòng 210: Cánh Tây Nam (Phòng lớn nhất - KT 12x6m, 1 người)
    rooms.append({
        'id': 'P210', 'name': 'Phòng 210',
        'x': 0.0, 'y': Y_A_WING_BOT, 'w': 8.0, 'h': Y_A_CORR_BOT - Y_A_WING_BOT,
        'text_center': (4.0, (Y_A_WING_BOT + Y_A_CORR_BOT)/2.0),
        'door': (6.2, Y_A_CORR_BOT, 0.9, 'S_IN_RIGHT'),
        'font_size': 10.5
    })
    # Phòng 201: Thân Nam trái (KT 10.3x4m, 1 người)
    rooms.append({
        'id': 'P201', 'name': 'Phòng 201',
        'x': 8.0, 'y': Y_A_BODY_BOT, 'w': 7.0, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
        'text_center': (11.5, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0),
        'door': (9.2, Y_A_CORR_BOT, 0.9, 'S_IN_RIGHT'),
        'font_size': 10.0
    })
    # Phòng 202: Thân Nam trái cạnh phòng giữa (KT 6.3x4m, 1 người)
    rooms.append({
        'id': 'P202', 'name': 'Phòng 202',
        'x': 15.0, 'y': Y_A_BODY_BOT, 'w': 6.0, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
        'text_center': (18.0, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0),
        'door': (16.0, Y_A_CORR_BOT, 0.9, 'S_IN_RIGHT'),
        'font_size': 10.0
    })
    # Phòng 204: Vị trí giữa phía Nam (thay thế Sảnh tầng 1 - KT 6.3x4m, 1 người)
    rooms.append({
        'id': 'P204', 'name': 'Phòng 204',
        'x': 21.0, 'y': Y_A_BODY_BOT, 'w': 6.0, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
        'text_center': (24.0, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0),
        'door': (22.2, Y_A_CORR_BOT, 0.9, 'S_IN_RIGHT'),
        'font_size': 10.0
    })
    # Phòng 203: Thân Nam phải cạnh phòng giữa (KT 10.3x4m, 1 người)
    rooms.append({
        'id': 'P203', 'name': 'Phòng 203',
        'x': 27.0, 'y': Y_A_BODY_BOT, 'w': 7.0, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
        'text_center': (30.5, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0),
        'door': (32.0, Y_A_CORR_BOT, 0.9, 'S_IN_LEFT'),
        'font_size': 10.0
    })
    # Phòng 205: Thân Nam phải (KT 6.3x4m, 1 người)
    rooms.append({
        'id': 'P205', 'name': 'Phòng 205',
        'x': 34.0, 'y': Y_A_BODY_BOT, 'w': 6.0, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
        'text_center': (37.0, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0),
        'door': (38.5, Y_A_CORR_BOT, 0.9, 'S_IN_LEFT'),
        'font_size': 10.0
    })
    # Phòng 206: Cánh Đông Nam (KT 8.3x8m, 4 người)
    rooms.append({
        'id': 'P206', 'name': 'Phòng 206',
        'x': 40.0, 'y': Y_A_WING_BOT, 'w': 8.0, 'h': Y_A_CORR_BOT - Y_A_WING_BOT,
        'text_center': (44.0, (Y_A_WING_BOT + Y_A_CORR_BOT)/2.0),
        'door': (41.5, Y_A_CORR_BOT, 0.9, 'S_IN_LEFT'),
        'font_size': 10.5
    })

    # --- Dãy Bắc Tòa A (Y > 0.9m) ---
    # Phòng 208: Cánh Tây Bắc (KT 6.3x6m, 1 người)
    rooms.append({
        'id': 'P208', 'name': 'Phòng 208',
        'x': 0.0, 'y': Y_A_CORR_TOP, 'w': 8.0, 'h': Y_A_WING_TOP - Y_A_CORR_TOP,
        'text_center': (4.0, (Y_A_CORR_TOP + Y_A_WING_TOP)/2.0),
        'door': (6.2, Y_A_CORR_TOP, 0.9, 'N_IN_RIGHT'),
        'font_size': 10.5
    })
    # Phòng 207: Thân Bắc trái (KT 6.3x4m, 1 người)
    rooms.append({
        'id': 'P207', 'name': 'Phòng 207',
        'x': 8.0, 'y': Y_A_CORR_TOP, 'w': 6.5, 'h': Y_A_BODY_TOP - Y_A_CORR_TOP,
        'text_center': (11.25, (Y_A_CORR_TOP + Y_A_BODY_TOP)/2.0),
        'door': (9.2, Y_A_CORR_TOP, 0.9, 'N_IN_RIGHT'),
        'font_size': 10.0
    })
    # Phòng 209: Thân Bắc trái cạnh thang (KT 6.3x6m, 1 người)
    rooms.append({
        'id': 'P209', 'name': 'Phòng 209',
        'x': 14.5, 'y': Y_A_CORR_TOP, 'w': 6.5, 'h': Y_A_BODY_TOP - Y_A_CORR_TOP,
        'text_center': (17.75, (Y_A_CORR_TOP + Y_A_BODY_TOP)/2.0),
        'door': (15.5, Y_A_CORR_TOP, 0.9, 'N_IN_RIGHT'),
        'font_size': 10.0
    })
    # [X: 21.0 to 27.0 là CẦU THANG VÀ LỐI NỐI]
    # Phòng 211: Thân Bắc phải (KT 6.3x4m, 1 người)
    rooms.append({
        'id': 'P211', 'name': 'Phòng 211',
        'x': 27.0, 'y': Y_A_CORR_TOP, 'w': 13.0, 'h': Y_A_BODY_TOP - Y_A_CORR_TOP,
        'text_center': (33.5, (Y_A_CORR_TOP + Y_A_BODY_TOP)/2.0),
        'door': (28.5, Y_A_CORR_TOP, 0.9, 'N_IN_RIGHT'),
        'font_size': 10.5
    })
    # Phòng 212: Cánh Đông Bắc (KT 6.8x6m, 2 người)
    rooms.append({
        'id': 'P212', 'name': 'Phòng 212',
        'x': 40.0, 'y': Y_A_CORR_TOP, 'w': 8.0, 'h': Y_A_WING_TOP - Y_A_CORR_TOP,
        'text_center': (44.0, (Y_A_CORR_TOP + Y_A_WING_TOP)/2.0),
        'door': (40.6, Y_A_CORR_TOP, 0.9, 'N_IN_RIGHT'),
        'font_size': 10.5
    })

    # === TÒA B (KHỐI XÉT XỬ - 2 PHÒNG XỬ ÁN) ===
    rooms.append({
        'id': 'P_XUAN_3', 'name': 'Phòng xử án 3',
        'x': 0.0, 'y': Y_B_BODY_BOT, 'w': 21.0, 'h': Y_B_BODY_TOP - Y_B_BODY_BOT,
        'text_center': (10.5, (Y_B_BODY_BOT + Y_B_BODY_TOP)/2.0),
        'door': (21.0, 15.0, 1.0, 'W_DOUBLE'),
        'font_size': 13.5
    })
    rooms.append({
        'id': 'P_XUAN_4', 'name': 'Phòng xử án 4',
        'x': 27.0, 'y': Y_B_BODY_BOT, 'w': 21.0, 'h': Y_B_BODY_TOP - Y_B_BODY_BOT,
        'text_center': (37.5, (Y_B_BODY_BOT + Y_B_BODY_TOP)/2.0),
        'door': (27.0, 15.0, 1.0, 'E_DOUBLE'),
        'font_size': 13.5
    })

    # Draw Room Background Fills (Pure White `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # Tòa B Wings Extensions Background Fill (Pure White)
    ax.add_patch(patches.Rectangle((0.0, Y_B_WING_BOT), 8.0, Y_B_BODY_BOT - Y_B_WING_BOT, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))
    ax.add_patch(patches.Rectangle((0.0, Y_B_BODY_TOP), 8.0, Y_B_WING_TOP - Y_B_BODY_TOP, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))
    ax.add_patch(patches.Rectangle((40.0, Y_B_WING_BOT), 8.0, Y_B_BODY_BOT - Y_B_WING_BOT, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))
    ax.add_patch(patches.Rectangle((40.0, Y_B_BODY_TOP), 8.0, Y_B_WING_TOP - Y_B_BODY_TOP, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))

    # ---------------------------------------------------------
    # 5. STAIRCASE (TẦNG 2: NỀN TRẮNG THUẦN #ffffff THEO SPEC)
    # ---------------------------------------------------------
    def draw_staircase(stair_x, stair_y, stair_w, stair_h, num_treads=8, label="Cầu thang"):
        # Upper floors staircase background is PURE WHITE
        stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, 
                                     facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
        ax.add_patch(stair_bg)
        for i in range(num_treads + 1):
            sy = stair_y + i * (stair_h / num_treads)
            ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
        mid_x = stair_x + stair_w / 2.0
        top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
        ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)
        ax.text(mid_x, stair_y - 0.25, label, color=COLOR_TEXT_MAIN, fontsize=8.5, ha='center', va='top', zorder=5)

    # Staircase 1: Tòa A (Upper floor)
    draw_staircase(23.5, 1.3, 3.0, 2.8, num_treads=8, label="Cầu thang A")

    # Staircase 2: Tòa B (Upper floor)
    draw_staircase(23.5, 11.6, 3.0, 2.8, num_treads=8, label="Cầu thang B")

    # ---------------------------------------------------------
    # 6. LABELS FOR CORRIDORS & BRIDGE
    # ---------------------------------------------------------
    ax.text(14.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(33.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(24.0, 7.75, 'HÀNH LANG CẦU NỐI\n(THÔNG 2 TÒA)', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(24.0, 18.0, 'SẢNH XÉT XỬ\nTRUNG TÂM', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 7. DRAW WALLS (DARK SLATE STRUCTURAL WALLS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # === TÒA A EXTERIOR WALLS (TẦNG 2: KÍN 2 ĐẦU HÀNH LANG VÀ MẶT NAM) ===
    # West Wing (X: 0.0 to 8.0, Y: -6.2 to 6.2)
    # Left vertical wall: FULL CONTINUOUS WALL (no opening stairs, window is cut in window function)
    draw_wall(-W, Y_A_WING_BOT - W, W, (Y_A_WING_TOP - Y_A_WING_BOT) + 2*W)
    # South wall of West Wing
    draw_wall(-W, Y_A_WING_BOT - W, X_WING_L + W, W)
    # Step-in wall to Main body at X = 8.0m (from Y: -6.2 to -4.5)
    draw_wall(X_WING_L - P/2, Y_A_WING_BOT, P, Y_A_BODY_BOT - Y_A_WING_BOT)
    # North wall of West Wing
    draw_wall(-W, Y_A_WING_TOP, X_WING_L + W, W)
    # Step-in wall to Main body at X = 8.0m (from Y: 4.5 to 6.2)
    draw_wall(X_WING_L - P/2, Y_A_BODY_TOP, P, Y_A_WING_TOP - Y_A_BODY_TOP)

    # East Wing (X: 40.0 to 48.0, Y: -6.2 to 6.2)
    # Right vertical wall: FULL CONTINUOUS WALL
    draw_wall(X_MAX, Y_A_WING_BOT - W, W, (Y_A_WING_TOP - Y_A_WING_BOT) + 2*W)
    # South wall of East Wing
    draw_wall(X_WING_R, Y_A_WING_BOT - W, (X_MAX - X_WING_R) + W, W)
    # Step-in wall from Main body at X = 40.0m (from Y: -6.2 to -4.5)
    draw_wall(X_WING_R - P/2, Y_A_WING_BOT, P, Y_A_BODY_BOT - Y_A_WING_BOT)
    # North wall of East Wing
    draw_wall(X_WING_R, Y_A_WING_TOP, (X_MAX - X_WING_R) + W, W)
    # Step-in wall from Main body at X = 40.0m (from Y: 4.5 to 6.2)
    draw_wall(X_WING_R - P/2, Y_A_BODY_TOP, P, Y_A_WING_TOP - Y_A_BODY_TOP)

    # Main Body South Bottom Wall (Y = -4.5, RUNS FULL CONTINUOUS FROM X=8.0 TO X=40.0)
    draw_wall(X_WING_L, Y_A_BODY_BOT - W, X_WING_R - X_WING_L, W)

    # Main Body North Top Wall (with bridge opening at X: 21.0 to 27.0)
    draw_wall(X_WING_L, Y_A_BODY_TOP, X_BRIDGE_L - X_WING_L, W)
    draw_wall(X_BRIDGE_R, Y_A_BODY_TOP, X_WING_R - X_BRIDGE_R, W)

    # === CENTRAL CONNECTING BRIDGE LINK WALLS (SOLID WALLS, NO WINDOWS) ===
    draw_wall(X_BRIDGE_L - W, Y_BRIDGE_BOT, W, Y_BRIDGE_TOP - Y_BRIDGE_BOT)
    draw_wall(X_BRIDGE_R, Y_BRIDGE_BOT, W, Y_BRIDGE_TOP - Y_BRIDGE_BOT)

    # === TÒA B EXTERIOR WALLS (TẦNG 2: KÍN MẶT BẮC) ===
    # West Wing of Tòa B (X: 0.0 to 8.0, Y: 9.4 to 22.2)
    draw_wall(-W, Y_B_WING_BOT - W, W, (Y_B_WING_TOP - Y_B_WING_BOT) + 2*W)
    draw_wall(-W, Y_B_WING_BOT - W, X_WING_L + W, W)
    draw_wall(X_WING_L - P/2, Y_B_WING_BOT, P, Y_B_BODY_BOT - Y_B_WING_BOT)
    draw_wall(-W, Y_B_WING_TOP, X_WING_L + W, W)
    draw_wall(X_WING_L - P/2, Y_B_BODY_TOP, P, Y_B_WING_TOP - Y_B_BODY_TOP)

    # East Wing of Tòa B (X: 40.0 to 48.0, Y: 9.4 to 22.2)
    draw_wall(X_MAX, Y_B_WING_BOT - W, W, (Y_B_WING_TOP - Y_B_WING_BOT) + 2*W)
    draw_wall(X_WING_R, Y_B_WING_BOT - W, (X_MAX - X_WING_R) + W, W)
    draw_wall(X_WING_R - P/2, Y_B_WING_BOT, P, Y_B_BODY_BOT - Y_B_WING_BOT)
    draw_wall(X_WING_R, Y_B_WING_TOP, (X_MAX - X_WING_R) + W, W)
    draw_wall(X_WING_R - P/2, Y_B_BODY_TOP, P, Y_B_WING_TOP - Y_B_BODY_TOP)

    # Main Body South Wall of Tòa B (Y = 11.0, with bridge opening at X: 21.0 to 27.0)
    draw_wall(X_WING_L, Y_B_BODY_BOT - W, X_BRIDGE_L - X_WING_L, W)
    draw_wall(X_BRIDGE_R, Y_B_BODY_BOT - W, X_WING_R - X_BRIDGE_R, W)

    # Main Body North Wall of Tòa B (Y = 20.6, FULL CONTINUOUS WALL FROM X=8.0 TO X=40.0)
    draw_wall(X_WING_L, Y_B_BODY_TOP, X_WING_R - X_WING_L, W)

    # === TÒA A INTERNAL CORRIDOR WALLS (WITH DOOR CUTS) ===
    # 1. South Corridor Wall (Y = -0.9m)
    # Door cuts: P210(6.2-7.1), P201(9.2-10.1), P202(16.0-16.9), P204(22.2-23.1), P203(31.1-32.0), P205(37.6-38.5), P206(40.6-41.5)
    draw_wall(0.0, Y_A_CORR_BOT - P/2, 6.2, P)
    draw_wall(7.1, Y_A_CORR_BOT - P/2, 2.1, P)
    draw_wall(10.1, Y_A_CORR_BOT - P/2, 5.9, P)
    draw_wall(16.9, Y_A_CORR_BOT - P/2, 5.3, P)
    draw_wall(23.1, Y_A_CORR_BOT - P/2, 8.0, P)
    draw_wall(32.0, Y_A_CORR_BOT - P/2, 5.6, P)
    draw_wall(38.5, Y_A_CORR_BOT - P/2, 2.1, P)
    draw_wall(41.5, Y_A_CORR_BOT - P/2, 6.5, P)

    # 2. North Corridor Wall (Y = 0.9m)
    # Door cuts: P208(6.2-7.1), P207(9.2-10.1), P209(15.5-16.4), P211(28.5-29.4), P212(40.6-41.5)
    draw_wall(0.0, Y_A_CORR_TOP - P/2, 6.2, P)
    draw_wall(7.1, Y_A_CORR_TOP - P/2, 2.1, P)
    draw_wall(10.1, Y_A_CORR_TOP - P/2, 5.4, P)
    draw_wall(16.4, Y_A_CORR_TOP - P/2, 4.6, P)
    # Stair Hall opening at X: 21.0 to 27.0 (no horizontal wall)
    draw_wall(27.0, Y_A_CORR_TOP - P/2, 1.5, P)
    draw_wall(29.4, Y_A_CORR_TOP - P/2, 11.2, P)
    draw_wall(41.5, Y_A_CORR_TOP - P/2, 6.5, P)

    # === TÒA A VERTICAL PARTITIONS ===
    # South row partitions (Y: -4.5 to -0.9)
    draw_wall(8.0 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)   # between 210 and 201
    draw_wall(15.0 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)  # between 201 and 202
    draw_wall(21.0 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)  # between 202 and 204
    draw_wall(27.0 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)  # between 204 and 203
    draw_wall(34.0 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)  # between 203 and 205
    draw_wall(40.0 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)  # between 205 and 206

    # North row partitions (Y: 0.9 to 4.5)
    draw_wall(8.0 - P/2, Y_A_CORR_TOP, P, Y_A_BODY_TOP - Y_A_CORR_TOP)   # between 208 and 207
    draw_wall(14.5 - P/2, Y_A_CORR_TOP, P, Y_A_BODY_TOP - Y_A_CORR_TOP)  # between 207 and 209
    draw_wall(21.0 - P/2, Y_A_CORR_TOP, P, Y_A_BODY_TOP - Y_A_CORR_TOP)  # between 209 and Stair Hall
    draw_wall(27.0 - P/2, Y_A_CORR_TOP, P, Y_A_BODY_TOP - Y_A_CORR_TOP)  # between Stair Hall and 211
    draw_wall(40.0 - P/2, Y_A_CORR_TOP, P, Y_A_BODY_TOP - Y_A_CORR_TOP)  # between 211 and 212

    # === TÒA B PARTITION WALLS (DIVIDING COURTROOMS FROM CENTRAL LOBBY) ===
    # Left partition at X = 21.0m (Double door cut at Y: 14.5 to 16.5)
    draw_wall(X_BRIDGE_L - P/2, Y_B_BODY_BOT, P, 14.5 - Y_B_BODY_BOT)
    draw_wall(X_BRIDGE_L - P/2, 16.5, P, Y_B_BODY_TOP - 16.5)

    # Right partition at X = 27.0m (Double door cut at Y: 14.5 to 16.5)
    draw_wall(X_BRIDGE_R - P/2, Y_B_BODY_BOT, P, 14.5 - Y_B_BODY_BOT)
    draw_wall(X_BRIDGE_R - P/2, 16.5, P, Y_B_BODY_TOP - 16.5)

    # ---------------------------------------------------------
    # 8. DRAW WINDOWS ON EXTERIOR WALLS
    # ---------------------------------------------------------
    def draw_window(x, y, w, h, is_horizontal=True):
        if is_horizontal:
            ax.add_patch(patches.Rectangle((x, y - 0.03), w, h + 0.06, facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x, x + w], [y + 0.04, y + 0.04], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x, x + w], [y + h - 0.04, y + h - 0.04], color=COLOR_WALL, linewidth=1.2, zorder=12)
        else:
            ax.add_patch(patches.Rectangle((x - 0.03, y), w + 0.06, h, facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x + 0.04, x + 0.04], [y, y + h], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x + w - 0.04, x + w - 0.04], [y, y + h], color=COLOR_WALL, linewidth=1.2, zorder=12)

    # Corridor End Windows on Tòa A (West & East End Windows for Upper Floor)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)

    # Windows on Tòa A South facade
    draw_window(2.5, Y_A_WING_BOT - W, 3.0, W)   # P210
    draw_window(10.0, Y_A_BODY_BOT - W, 3.0, W)  # P201
    draw_window(16.5, Y_A_BODY_BOT - W, 2.5, W)  # P202
    draw_window(22.5, Y_A_BODY_BOT - W, 3.0, W)  # P204 (Center Room)
    draw_window(29.0, Y_A_BODY_BOT - W, 3.0, W)  # P203
    draw_window(35.5, Y_A_BODY_BOT - W, 2.5, W)  # P205
    draw_window(42.5, Y_A_WING_BOT - W, 3.0, W)  # P206

    # Windows on Tòa A North facade
    draw_window(2.5, Y_A_WING_TOP, 3.0, W)       # P208
    draw_window(10.0, Y_A_BODY_TOP, 2.5, W)      # P207
    draw_window(16.5, Y_A_BODY_TOP, 2.5, W)      # P209
    draw_window(31.0, Y_A_BODY_TOP, 4.0, W)      # P211
    draw_window(42.5, Y_A_WING_TOP, 3.0, W)      # P212

    # Windows on Tòa B Facades (Courtrooms 3 & 4)
    # Courtroom 3 Windows: West Wing outer walls (Y = 9.4 and Y = 22.2) & Main body walls (Y = 11.0 and Y = 20.6)
    draw_window(2.5, Y_B_WING_BOT - W, 3.0, W)
    draw_window(12.0, Y_B_BODY_BOT - W, 4.0, W)
    draw_window(2.5, Y_B_WING_TOP, 3.0, W)
    draw_window(12.0, Y_B_BODY_TOP, 4.0, W)
    draw_window(-W, 14.5, W, 3.0, is_horizontal=False)

    # Courtroom 4 Windows: East Wing outer walls (Y = 9.4 and Y = 22.2) & Main body walls (Y = 11.0 and Y = 20.6)
    draw_window(32.0, Y_B_BODY_BOT - W, 4.0, W)
    draw_window(42.5, Y_B_WING_BOT - W, 3.0, W)
    draw_window(32.0, Y_B_BODY_TOP, 4.0, W)
    draw_window(42.5, Y_B_WING_TOP, 3.0, W)
    draw_window(X_MAX, 14.5, W, 3.0, is_horizontal=False)

    # Tòa B Rear Center Window (North Stair/Lobby Window)
    draw_window(22.5, Y_B_BODY_TOP, 3.0, W)

    # ---------------------------------------------------------
    # 9. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode == 'S_IN_RIGHT':
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_LEFT':
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=180, theta2=270,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'N_IN_RIGHT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'N_IN_LEFT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'W_DOUBLE':
            ax.plot([x, x - size], [16.5, 16.5], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc1 = patches.Arc((x, 16.5), size*2, size*2, angle=0, theta1=180, theta2=270,
                               color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc1)
            ax.plot([x, x - size], [14.5, 14.5], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc2 = patches.Arc((x, 14.5), size*2, size*2, angle=0, theta1=90, theta2=180,
                               color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc2)
        elif mode == 'E_DOUBLE':
            ax.plot([x, x + size], [16.5, 16.5], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc1 = patches.Arc((x, 16.5), size*2, size*2, angle=0, theta1=270, theta2=360,
                               color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc1)
            ax.plot([x, x + size], [14.5, 14.5], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc2 = patches.Arc((x, 14.5), size*2, size*2, angle=0, theta1=0, theta2=90,
                               color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc2)

    for r in rooms:
        dx, dy, dsize, dmode = r['door']
        draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 10. DRAW ROOM LABELS (STRICTLY SINGLE-LINE LABELS)
    # ---------------------------------------------------------
    for r in rooms:
        if r['name']:
            cx, cy = r['text_center']
            font_sz = r.get('font_size', 10.0)
            ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                    fontweight='bold', ha='center', va='center', zorder=15)

    # Save outputs
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Successfully generated Tang 2 floorplan image at: {out_img_path}")

if __name__ == '__main__':
    target_dir = r'c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau\Tang2'
    create_floorplan_tang2(target_dir)
