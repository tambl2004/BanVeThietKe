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

def create_floorplan_tang1(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_1.png')

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
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
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 staircase matches lobby background
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

    # Tòa 1 (Tòa A - Khối Hành chính phía Nam) Vertical coordinates:
    Y_A_CORR_BOT = -0.9
    Y_A_CORR_TOP = 0.9
    Y_A_BODY_BOT = -4.5
    Y_A_BODY_TOP = 4.5
    Y_A_WING_BOT = -6.2
    Y_A_WING_TOP = 6.2

    # Central Connecting Bridge Link:
    Y_BRIDGE_BOT = 4.5
    Y_BRIDGE_TOP = 11.0

    # Tòa 2 (Tòa B - Khối Xét xử phía Bắc) Vertical coordinates:
    Y_B_BODY_BOT = 11.0
    Y_B_BODY_TOP = 20.6
    Y_B_WING_BOT = 9.4
    Y_B_WING_TOP = 22.2

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line per Spec)
    fig.text(0.04, 0.962, 'MẶT BẰNG TẦNG 1  —  TÒA ÁN NHÂN DÂN KHU VỰC 6 - CÀ MAU', 
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
    # Tòa 1 Horizontal Corridor (X: 0.0 to 48.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, Y_A_CORR_BOT), X_MAX, Y_A_CORR_TOP - Y_A_CORR_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 South Main Entrance Lobby (X: 21.0 to 27.0, Y: -4.5 to -0.9)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_A_BODY_BOT), X_BRIDGE_R - X_BRIDGE_L, Y_A_CORR_BOT - Y_A_BODY_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 North Stair Hall (X: 21.0 to 27.0, Y: 0.9 to 4.5)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_A_CORR_TOP), X_BRIDGE_R - X_BRIDGE_L, Y_A_BODY_TOP - Y_A_CORR_TOP, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Central Connecting Bridge Link (X: 21.0 to 27.0, Y: 4.5 to 11.0)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_BRIDGE_BOT), X_BRIDGE_R - X_BRIDGE_L, Y_BRIDGE_TOP - Y_BRIDGE_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 Central Lobby & Stair Hall (X: 21.0 to 27.0, Y: 11.0 to 20.6)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_B_BODY_BOT), X_BRIDGE_R - X_BRIDGE_L, Y_B_BODY_TOP - Y_B_BODY_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (10 PHÒNG TÒA 1 & TÒA XÉT XỬ)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = []

    # === TÒA 1 (10 PHÒNG LÀM VIỆC THEO SỐ LIỆU KHẢO SÁT) ===
    # --- Dãy Nam Tòa 1 (Y < -0.9m) : 6 Phòng ---
    rooms.append({
        'id': 'T1_P1', 'name': 'Phòng làm việc',
        'x': 0.0, 'y': Y_A_WING_BOT, 'w': 8.0, 'h': Y_A_CORR_BOT - Y_A_WING_BOT,
        'text_center': (4.0, (Y_A_WING_BOT + Y_A_CORR_BOT)/2.0),
        'door': (6.2, Y_A_CORR_BOT, 0.9, 'S_IN_RIGHT'),
        'font_size': 10.5
    })
    rooms.append({
        'id': 'T1_P2', 'name': 'Phòng làm việc',
        'x': 8.0, 'y': Y_A_BODY_BOT, 'w': 6.5, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
        'text_center': (11.25, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0),
        'door': (9.2, Y_A_CORR_BOT, 0.9, 'S_IN_RIGHT'),
        'font_size': 10.0
    })
    rooms.append({
        'id': 'T1_P3', 'name': 'Phòng làm việc',
        'x': 14.5, 'y': Y_A_BODY_BOT, 'w': 6.5, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
        'text_center': (17.75, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0),
        'door': (15.8, Y_A_CORR_BOT, 0.9, 'S_IN_RIGHT'),
        'font_size': 10.0
    })
    rooms.append({
        'id': 'T1_P4', 'name': 'Phòng làm việc',
        'x': 27.0, 'y': Y_A_BODY_BOT, 'w': 6.5, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
        'text_center': (30.25, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0),
        'door': (32.2, Y_A_CORR_BOT, 0.9, 'S_IN_LEFT'),
        'font_size': 10.0
    })
    rooms.append({
        'id': 'T1_P5', 'name': 'Phòng làm việc',
        'x': 33.5, 'y': Y_A_BODY_BOT, 'w': 6.5, 'h': Y_A_CORR_BOT - Y_A_BODY_BOT,
        'text_center': (36.75, (Y_A_BODY_BOT + Y_A_CORR_BOT)/2.0),
        'door': (38.5, Y_A_CORR_BOT, 0.9, 'S_IN_LEFT'),
        'font_size': 10.0
    })
    rooms.append({
        'id': 'T1_P6', 'name': 'Phòng làm việc',
        'x': 40.0, 'y': Y_A_WING_BOT, 'w': 8.0, 'h': Y_A_CORR_BOT - Y_A_WING_BOT,
        'text_center': (44.0, (Y_A_WING_BOT + Y_A_CORR_BOT)/2.0),
        'door': (41.8, Y_A_CORR_BOT, 0.9, 'S_IN_LEFT'),
        'font_size': 10.5
    })

    # --- Dãy Bắc Tòa 1 (Y > 0.9m) : 4 Phòng ---
    rooms.append({
        'id': 'T1_P7', 'name': 'Phòng làm việc',
        'x': 0.0, 'y': Y_A_CORR_TOP, 'w': 8.0, 'h': Y_A_WING_TOP - Y_A_CORR_TOP,
        'text_center': (4.0, (Y_A_CORR_TOP + Y_A_WING_TOP)/2.0),
        'door': (6.2, Y_A_CORR_TOP, 0.9, 'N_IN_RIGHT'),
        'font_size': 10.5
    })
    rooms.append({
        'id': 'T1_P8', 'name': 'Phòng làm việc',
        'x': 8.0, 'y': Y_A_CORR_TOP, 'w': 13.0, 'h': Y_A_BODY_TOP - Y_A_CORR_TOP,
        'text_center': (14.5, (Y_A_CORR_TOP + Y_A_BODY_TOP)/2.0),
        'door': (9.2, Y_A_CORR_TOP, 0.9, 'N_IN_RIGHT'),
        'font_size': 11.0
    })
    rooms.append({
        'id': 'T1_P9', 'name': 'Phòng làm việc',
        'x': 27.0, 'y': Y_A_CORR_TOP, 'w': 13.0, 'h': Y_A_BODY_TOP - Y_A_CORR_TOP,
        'text_center': (33.5, (Y_A_CORR_TOP + Y_A_BODY_TOP)/2.0),
        'door': (38.5, Y_A_CORR_TOP, 0.9, 'N_IN_LEFT'),
        'font_size': 11.0
    })
    rooms.append({
        'id': 'T1_P10', 'name': 'Phòng làm việc',
        'x': 40.0, 'y': Y_A_CORR_TOP, 'w': 8.0, 'h': Y_A_WING_TOP - Y_A_CORR_TOP,
        'text_center': (44.0, (Y_A_CORR_TOP + Y_A_WING_TOP)/2.0),
        'door': (41.8, Y_A_CORR_TOP, 0.9, 'N_IN_LEFT'),
        'font_size': 10.5
    })

    # === TÒA 2 (KHỐI XÉT XỬ: 2 ĐẠI PHÒNG XỬ ÁN + 3 PHÒNG LÀM VIỆC) ===
    # 1. Phòng xử án 1 (Trọn vẹn Cánh Tây & Nửa Tây Tòa B)
    rooms.append({
        'id': 'P_XUAN_1', 'name': 'Phòng xử án 1',
        'x': 0.0, 'y': Y_B_BODY_BOT, 'w': 21.0, 'h': Y_B_BODY_TOP - Y_B_BODY_BOT,
        'text_center': (10.5, (Y_B_BODY_BOT + Y_B_BODY_TOP)/2.0),
        'door': (21.0, 15.0, 1.0, 'W_DOUBLE'),
        'font_size': 13.5
    })

    # 2. Phòng xử án 2 (Thân Đông Tòa B)
    rooms.append({
        'id': 'P_XUAN_2', 'name': 'Phòng xử án 2',
        'x': 27.0, 'y': Y_B_BODY_BOT, 'w': 13.0, 'h': Y_B_BODY_TOP - Y_B_BODY_BOT,
        'text_center': (33.5, (Y_B_BODY_BOT + Y_B_BODY_TOP)/2.0),
        'door': (27.0, 15.0, 1.0, 'E_DOUBLE'),
        'font_size': 13.0
    })

    # 3. 3 Phòng làm việc ở Cánh Đông Tòa Xét xử (KT chuẩn khảo sát: 6,3m x 3,6m)
    # Phòng 1 phía Bắc cánh Đông:
    rooms.append({
        'id': 'T2_P1', 'name': 'Phòng làm việc',
        'x': 40.0, 'y': 18.0, 'w': 8.0, 'h': Y_B_WING_TOP - 18.0,
        'text_center': (44.0, (18.0 + Y_B_WING_TOP)/2.0),
        'door': (40.0, 19.05, 0.9, 'E_IN_UP'),
        'font_size': 10.0
    })
    # Phòng 2 trung tâm cánh Đông:
    rooms.append({
        'id': 'T2_P2', 'name': 'Phòng làm việc',
        'x': 40.0, 'y': 13.6, 'w': 8.0, 'h': 18.0 - 13.6,
        'text_center': (44.0, (13.6 + 18.0)/2.0),
        'door': (40.0, 15.35, 0.9, 'E_IN_UP'),
        'font_size': 10.0
    })
    # Phòng 3 phía Nam cánh Đông:
    rooms.append({
        'id': 'T2_P3', 'name': 'Phòng làm việc',
        'x': 40.0, 'y': Y_B_WING_BOT, 'w': 8.0, 'h': 13.6 - Y_B_WING_BOT,
        'text_center': (44.0, (Y_B_WING_BOT + 13.6)/2.0),
        'door': (40.0, 11.55, 0.9, 'E_IN_UP'),
        'font_size': 10.0
    })

    # Draw Room Background Fills (Pure White `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # Tòa 2 West Wing Extensions Background Fill (Projections for West Wing of Courtroom 1)
    ax.add_patch(patches.Rectangle((0.0, Y_B_WING_BOT), 8.0, Y_B_BODY_BOT - Y_B_WING_BOT, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))
    ax.add_patch(patches.Rectangle((0.0, Y_B_BODY_TOP), 8.0, Y_B_WING_TOP - Y_B_BODY_TOP, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS (FLOOR 1 SPECIFIC)
    # ---------------------------------------------------------
    def draw_staircase(stair_x, stair_y, stair_w, stair_h, num_treads=8, label="Cầu thang"):
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

    # Staircase 1: Tòa 1 (Lên tầng 2)
    draw_staircase(23.5, 1.3, 3.0, 2.8, num_treads=8, label="Cầu thang A")

    # Staircase 2: Tòa 2 (Khối xét xử)
    draw_staircase(23.5, 11.6, 3.0, 2.8, num_treads=8, label="Cầu thang B")

    # --- Steps / Bậc Tam Cấp ---
    # 1. Main South Entrance Steps (Tòa 1: Y = -4.5 down to -5.7)
    for sy in [-4.5, -4.7, -4.9, -5.1, -5.3, -5.5, -5.7]:
        ax.plot([X_BRIDGE_L, X_BRIDGE_R], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([X_BRIDGE_L, X_BRIDGE_L], [-4.5, -5.7], color=COLOR_WALL, linewidth=1.3, zorder=4)
    ax.plot([X_BRIDGE_R, X_BRIDGE_R], [-4.5, -5.7], color=COLOR_WALL, linewidth=1.3, zorder=4)

    # 2. Outdoor Side Steps at Tòa 1 Corridor Ends (West & East Exits)
    for i in range(5):
        dx = -0.22 * (i + 1)
        dy = 0.9 + i * 0.08
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    for i in range(5):
        dx = X_MAX + 0.22 * (i + 1)
        dy = 0.9 + i * 0.08
        ax.plot([X_MAX, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([X_MAX, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # 3. Rear North Exit Steps (Tòa 2: Y = 20.6 up to 21.6)
    for sy in [20.6, 20.8, 21.0, 21.2, 21.4, 21.6]:
        ax.plot([X_BRIDGE_L, X_BRIDGE_R], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([X_BRIDGE_L, X_BRIDGE_L], [20.6, 21.6], color=COLOR_WALL, linewidth=1.3, zorder=4)
    ax.plot([X_BRIDGE_L, X_BRIDGE_L + 0.5], [21.6, 21.6], color=COLOR_WALL, linewidth=1.3, zorder=4)
    ax.plot([X_BRIDGE_R, X_BRIDGE_R], [20.6, 21.6], color=COLOR_WALL, linewidth=1.3, zorder=4)
    ax.plot([X_BRIDGE_R, X_BRIDGE_R - 0.5], [21.6, 21.6], color=COLOR_WALL, linewidth=1.3, zorder=4)

    # ---------------------------------------------------------
    # 6. LABELS FOR LOBBY, CORRIDORS & BRIDGE
    # ---------------------------------------------------------
    ax.text(24.0, -2.7, 'SẢNH ĐÓN CHÍNH', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
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

    # === TÒA 1 EXTERIOR WALLS ===
    # West Wing (X: 0.0 to 8.0, Y: -6.2 to 6.2)
    draw_wall(-W, Y_A_WING_BOT - W, W, (Y_A_CORR_BOT - Y_A_WING_BOT) + W)
    draw_wall(-W, Y_A_CORR_TOP, W, (Y_A_WING_TOP - Y_A_CORR_TOP) + W)
    draw_wall(-W, Y_A_WING_BOT - W, X_WING_L + W, W)
    draw_wall(X_WING_L - P/2, Y_A_WING_BOT, P, Y_A_BODY_BOT - Y_A_WING_BOT)
    draw_wall(-W, Y_A_WING_TOP, X_WING_L + W, W)
    draw_wall(X_WING_L - P/2, Y_A_BODY_TOP, P, Y_A_WING_TOP - Y_A_BODY_TOP)

    # East Wing (X: 40.0 to 48.0, Y: -6.2 to 6.2)
    draw_wall(X_MAX, Y_A_WING_BOT - W, W, (Y_A_CORR_BOT - Y_A_WING_BOT) + W)
    draw_wall(X_MAX, Y_A_CORR_TOP, W, (Y_A_WING_TOP - Y_A_CORR_TOP) + W)
    draw_wall(X_WING_R, Y_A_WING_BOT - W, (X_MAX - X_WING_R) + W, W)
    draw_wall(X_WING_R - P/2, Y_A_WING_BOT, P, Y_A_BODY_BOT - Y_A_WING_BOT)
    draw_wall(X_WING_R, Y_A_WING_TOP, (X_MAX - X_WING_R) + W, W)
    draw_wall(X_WING_R - P/2, Y_A_BODY_TOP, P, Y_A_WING_TOP - Y_A_BODY_TOP)

    # Main Body South Bottom Wall (with entrance opening at X: 21.0 to 27.0)
    draw_wall(X_WING_L, Y_A_BODY_BOT - W, X_BRIDGE_L - X_WING_L, W)
    draw_wall(X_BRIDGE_R, Y_A_BODY_BOT - W, X_WING_R - X_BRIDGE_R, W)
    draw_wall(X_BRIDGE_L - P/2, -5.7, P, 1.2)
    draw_wall(X_BRIDGE_R - P/2, -5.7, P, 1.2)

    # Main Body North Top Wall (with bridge opening at X: 21.0 to 27.0)
    draw_wall(X_WING_L, Y_A_BODY_TOP, X_BRIDGE_L - X_WING_L, W)
    draw_wall(X_BRIDGE_R, Y_A_BODY_TOP, X_WING_R - X_BRIDGE_R, W)

    # === CENTRAL CONNECTING BRIDGE LINK WALLS ===
    # Solid structural side walls, strictly NO windows per spec
    draw_wall(X_BRIDGE_L - W, Y_BRIDGE_BOT, W, Y_BRIDGE_TOP - Y_BRIDGE_BOT)
    draw_wall(X_BRIDGE_R, Y_BRIDGE_BOT, W, Y_BRIDGE_TOP - Y_BRIDGE_BOT)

    # === TÒA 2 EXTERIOR WALLS ===
    # West Wing of Tòa 2 (X: 0.0 to 8.0, Y: 9.4 to 22.2)
    draw_wall(-W, Y_B_WING_BOT - W, W, (Y_B_WING_TOP - Y_B_WING_BOT) + 2*W)
    draw_wall(-W, Y_B_WING_BOT - W, X_WING_L + W, W)
    draw_wall(X_WING_L - P/2, Y_B_WING_BOT, P, Y_B_BODY_BOT - Y_B_WING_BOT)
    draw_wall(-W, Y_B_WING_TOP, X_WING_L + W, W)
    draw_wall(X_WING_L - P/2, Y_B_BODY_TOP, P, Y_B_WING_TOP - Y_B_BODY_TOP)

    # East Wing of Tòa 2 (X: 40.0 to 48.0, Y: 9.4 to 22.2)
    draw_wall(X_MAX, Y_B_WING_BOT - W, W, (Y_B_WING_TOP - Y_B_WING_BOT) + 2*W)
    draw_wall(X_WING_R, Y_B_WING_BOT - W, (X_MAX - X_WING_R) + W, W)
    draw_wall(X_WING_R - P/2, Y_B_WING_BOT, P, Y_B_BODY_BOT - Y_B_WING_BOT)
    draw_wall(X_WING_R, Y_B_WING_TOP, (X_MAX - X_WING_R) + W, W)
    draw_wall(X_WING_R - P/2, Y_B_BODY_TOP, P, Y_B_WING_TOP - Y_B_BODY_TOP)

    # Main Body South Wall of Tòa 2 (Y = 11.0)
    draw_wall(X_WING_L, Y_B_BODY_BOT - W, X_BRIDGE_L - X_WING_L, W)
    draw_wall(X_BRIDGE_R, Y_B_BODY_BOT - W, X_WING_R - X_BRIDGE_R, W)

    # Main Body North Wall of Tòa 2 (Y = 20.6)
    draw_wall(X_WING_L, Y_B_BODY_TOP, X_BRIDGE_L - X_WING_L, W)
    draw_wall(X_BRIDGE_R, Y_B_BODY_TOP, X_WING_R - X_BRIDGE_R, W)

    # === TÒA 1 INTERNAL CORRIDOR WALLS (WITH DOOR CUTS) ===
    # 1. South Corridor Wall (Y = -0.9m)
    draw_wall(0.0, Y_A_CORR_BOT - P/2, 6.2, P)
    draw_wall(7.1, Y_A_CORR_BOT - P/2, 2.1, P)
    draw_wall(10.1, Y_A_CORR_BOT - P/2, 5.7, P)
    draw_wall(16.7, Y_A_CORR_BOT - P/2, 4.3, P)
    draw_wall(27.0, Y_A_CORR_BOT - P/2, 4.3, P)
    draw_wall(32.2, Y_A_CORR_BOT - P/2, 5.4, P)
    draw_wall(38.5, Y_A_CORR_BOT - P/2, 2.4, P)
    draw_wall(41.8, Y_A_CORR_BOT - P/2, 6.2, P)

    # 2. North Corridor Wall (Y = 0.9m)
    draw_wall(0.0, Y_A_CORR_TOP - P/2, 6.2, P)
    draw_wall(7.1, Y_A_CORR_TOP - P/2, 2.1, P)
    draw_wall(10.1, Y_A_CORR_TOP - P/2, 10.9, P)
    draw_wall(27.0, Y_A_CORR_TOP - P/2, 10.6, P)
    draw_wall(38.5, Y_A_CORR_TOP - P/2, 2.4, P)
    draw_wall(41.8, Y_A_CORR_TOP - P/2, 6.2, P)

    # === TÒA 1 VERTICAL PARTITIONS ===
    # South row partitions (Y: -4.5 to -0.9)
    draw_wall(8.0 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)
    draw_wall(14.5 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)
    draw_wall(21.0 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)
    draw_wall(27.0 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)
    draw_wall(33.5 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)
    draw_wall(40.0 - P/2, Y_A_BODY_BOT, P, Y_A_CORR_BOT - Y_A_BODY_BOT)

    # North row partitions (Y: 0.9 to 4.5)
    draw_wall(8.0 - P/2, Y_A_CORR_TOP, P, Y_A_BODY_TOP - Y_A_CORR_TOP)
    draw_wall(21.0 - P/2, Y_A_CORR_TOP, P, Y_A_BODY_TOP - Y_A_CORR_TOP)
    draw_wall(27.0 - P/2, Y_A_CORR_TOP, P, Y_A_BODY_TOP - Y_A_CORR_TOP)
    draw_wall(40.0 - P/2, Y_A_CORR_TOP, P, Y_A_BODY_TOP - Y_A_CORR_TOP)

    # === TÒA 2 PARTITION WALLS ===
    # 1. Left partition at X = 21.0m (Double door cut at Y: 14.5 to 16.5)
    draw_wall(X_BRIDGE_L - P/2, Y_B_BODY_BOT, P, 14.5 - Y_B_BODY_BOT)
    draw_wall(X_BRIDGE_L - P/2, 16.5, P, Y_B_BODY_TOP - 16.5)

    # 2. Right partition at X = 27.0m (Double door cut at Y: 14.5 to 16.5)
    draw_wall(X_BRIDGE_R - P/2, Y_B_BODY_BOT, P, 14.5 - Y_B_BODY_BOT)
    draw_wall(X_BRIDGE_R - P/2, 16.5, P, Y_B_BODY_TOP - 16.5)

    # 3. East partition at X = 40.0m dividing Courtroom 2 from 3 Office Rooms
    # With door cuts for the 3 office rooms:
    # Door 3 at Y: 11.55 to 12.45
    # Door 2 at Y: 15.35 to 16.25
    # Door 1 at Y: 19.05 to 19.95
    draw_wall(X_WING_R - P/2, Y_B_BODY_BOT, P, 11.55 - Y_B_BODY_BOT)
    draw_wall(X_WING_R - P/2, 12.45, P, 15.35 - 12.45)
    draw_wall(X_WING_R - P/2, 16.25, P, 19.05 - 16.25)
    draw_wall(X_WING_R - P/2, 19.95, P, Y_B_BODY_TOP - 19.95)

    # 4. Horizontal partitions in East Wing (dividing the 3 Office Rooms)
    draw_wall(X_WING_R, 13.6 - P/2, X_MAX - X_WING_R, P)
    draw_wall(X_WING_R, 18.0 - P/2, X_MAX - X_WING_R, P)

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

    # Windows on Tòa 1 South facade
    draw_window(2.5, Y_A_WING_BOT - W, 3.0, W)   # P1
    draw_window(9.5, Y_A_BODY_BOT - W, 3.0, W)   # P2
    draw_window(16.0, Y_A_BODY_BOT - W, 3.0, W)  # P3
    draw_window(28.5, Y_A_BODY_BOT - W, 3.0, W)  # P4
    draw_window(35.0, Y_A_BODY_BOT - W, 3.0, W)  # P5
    draw_window(42.5, Y_A_WING_BOT - W, 3.0, W)  # P6

    # Windows on Tòa 1 North facade
    draw_window(2.5, Y_A_WING_TOP, 3.0, W)       # P7
    draw_window(10.5, Y_A_BODY_TOP, 3.5, W)      # P8
    draw_window(15.5, Y_A_BODY_TOP, 3.5, W)      # P8
    draw_window(29.0, Y_A_BODY_TOP, 3.5, W)      # P9
    draw_window(34.5, Y_A_BODY_TOP, 3.5, W)      # P9
    draw_window(42.5, Y_A_WING_TOP, 3.0, W)      # P10

    # Windows on Tòa 2 Facades
    # Courtroom 1 Windows: West Wing outer walls & Main body walls
    draw_window(2.5, Y_B_WING_BOT - W, 3.0, W)
    draw_window(12.0, Y_B_BODY_BOT - W, 4.0, W)
    draw_window(2.5, Y_B_WING_TOP, 3.0, W)
    draw_window(12.0, Y_B_BODY_TOP, 4.0, W)
    draw_window(-W, 14.5, W, 3.0, is_horizontal=False)

    # Courtroom 2 Windows (Main body walls)
    draw_window(31.5, Y_B_BODY_BOT - W, 4.0, W)
    draw_window(31.5, Y_B_BODY_TOP, 4.0, W)

    # East Wing 3 Office Rooms Windows (East outer wall & South/North projections)
    draw_window(42.5, Y_B_WING_BOT - W, 3.0, W)  # South office
    draw_window(42.5, Y_B_WING_TOP, 3.0, W)      # North office
    draw_window(X_MAX, 11.0, W, 1.8, is_horizontal=False)  # South office East window
    draw_window(X_MAX, 15.0, W, 1.8, is_horizontal=False)  # Center office East window
    draw_window(X_MAX, 19.2, W, 1.8, is_horizontal=False)  # North office East window

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
        elif mode == 'E_IN_UP':
            # Door on vertical partition X = 40.0 opening into East room
            ax.plot([x, x + size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'W_DOUBLE':
            # Grand double door opening into West Courtroom
            ax.plot([x, x - size], [16.5, 16.5], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc1 = patches.Arc((x, 16.5), size*2, size*2, angle=0, theta1=180, theta2=270,
                               color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc1)
            ax.plot([x, x - size], [14.5, 14.5], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc2 = patches.Arc((x, 14.5), size*2, size*2, angle=0, theta1=90, theta2=180,
                               color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc2)
        elif mode == 'E_DOUBLE':
            # Grand double door opening into East Courtroom
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
    print(f"Successfully generated floorplan image at: {out_img_path}")

if __name__ == '__main__':
    target_dir = r'c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau6\Tang1'
    create_floorplan_tang1(target_dir)
