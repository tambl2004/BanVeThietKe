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

    # Tòa 2 West corridor divider height:
    Y_B_CORR_DIV = 13.2

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.04, 0.962, 'MẶT BẰNG TẦNG 2  —  TÒA ÁN NHÂN DÂN KHU VỰC 6 - CÀ MAU', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.04, 0.96], [0.945, 0.945], transform=fig.transFigure, color='#e2e8f0', linewidth=1.2)
    fig.lines.append(header_line)

    # Legend Box at Bottom Center (4 items: Hành lang/sảnh, Tường/vách, Cửa sổ, Cửa đi mở vào)
    lg_x, lg_y = 11.0, -8.6
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
    # 3. CORRIDOR & LOBBY BACKGROUND FILLS (PASTEL BLUE-GREY)
    # ---------------------------------------------------------
    # --- Tòa 1 ---
    # Horizontal Corridor
    ax.add_patch(patches.Rectangle((0.0, Y_A_CORR_BOT), X_MAX, Y_A_CORR_TOP - Y_A_CORR_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Sảnh Tầng 2 Tòa 1 (phía Nam)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_A_BODY_BOT), X_BRIDGE_R - X_BRIDGE_L, Y_A_CORR_BOT - Y_A_BODY_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Sảnh thang Tòa 1 (phía Bắc)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_A_CORR_TOP), X_BRIDGE_R - X_BRIDGE_L, Y_A_BODY_TOP - Y_A_CORR_TOP, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # --- Nhịp cầu nối trung tâm ---
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_BRIDGE_BOT), X_BRIDGE_R - X_BRIDGE_L, Y_BRIDGE_TOP - Y_BRIDGE_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # --- Tòa 2 (Khối Xét xử) ---
    # Central Lobby (X: 21.0 to 27.0, Y: 11.0 to 20.6)
    ax.add_patch(patches.Rectangle((X_BRIDGE_L, Y_B_BODY_BOT), X_BRIDGE_R - X_BRIDGE_L, Y_B_BODY_TOP - Y_B_BODY_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Hành lang Tây (X: 8.0 to 21.0, Y: 11.0 to 13.2) - dẫn từ Sảnh trung tâm sang Cánh Tây
    ax.add_patch(patches.Rectangle((8.0, Y_B_BODY_BOT), 13.0, Y_B_CORR_DIV - Y_B_BODY_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Sảnh Đông (X: 27.0 to 40.0, Y: 11.0 to 20.6) - rộng thoáng kết nối sang Cánh Đông
    ax.add_patch(patches.Rectangle((27.0, Y_B_BODY_BOT), 13.0, Y_B_BODY_TOP - Y_B_BODY_BOT, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TÒA 1: 10 PHÒNG | TÒA 2: ĐÚNG 3 PHÒNG THEO HÌNH VẼ USER)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = []

    # === TÒA 1 (10 PHÒNG LÀM VIỆC) ===
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

    # === TÒA 2 (ĐÚNG 3 PHÒNG THEO 3 KHU VỰC ĐƯỢC KHOANH CHỮ X) ===
    # Draw Room Background Fills (Pure White `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # 1. Phòng 1 (Cánh Tây - trọn vẹn cánh hồi Tây, X: 0.0 to 8.0, Y: 9.4 to 22.2)
    ax.add_patch(patches.Rectangle((0.0, Y_B_WING_BOT), 8.0, Y_B_WING_TOP - Y_B_WING_BOT, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))

    # 2. Phòng 2 (Thân Tây - nửa Bắc thân Tây, X: 8.0 to 21.0, Y: 13.2 to 20.6)
    ax.add_patch(patches.Rectangle((8.0, Y_B_CORR_DIV), 13.0, Y_B_BODY_TOP - Y_B_CORR_DIV, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))

    # 3. Phòng 3 (Cánh Đông - trọn vẹn cánh hồi Đông, X: 40.0 to 48.0, Y: 9.4 to 22.2)
    ax.add_patch(patches.Rectangle((40.0, Y_B_WING_BOT), 8.0, Y_B_WING_TOP - Y_B_WING_BOT, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHICS (UPPER FLOOR SPEC: PURE WHITE BACKGROUND)
    # ---------------------------------------------------------
    # --- Cầu thang A (Tòa 1): X: 23.5 to 26.5, Y: 1.2 to 4.2 ---
    stair_a_x, stair_a_y, stair_a_w, stair_a_h = 23.5, 1.2, 3.0, 3.0
    ax.add_patch(patches.Rectangle((stair_a_x, stair_a_y), stair_a_w, stair_a_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.2, zorder=6))
    ax.plot([stair_a_x + stair_a_w/2, stair_a_x + stair_a_w/2], [stair_a_y, stair_a_y + stair_a_h], color=COLOR_WALL, linewidth=1.0, zorder=7)
    num_steps = 7
    for i in range(1, num_steps):
        sy = stair_a_y + i * (stair_a_h / num_steps)
        ax.plot([stair_a_x, stair_a_x + stair_a_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=7)
    ax.annotate('', xy=(stair_a_x + stair_a_w*0.5, stair_a_y + 0.3), xytext=(stair_a_x + stair_a_w*0.5, stair_a_y + stair_a_h - 0.3),
                arrowprops=dict(arrowstyle="->", color=COLOR_WALL, lw=1.2), zorder=8)
    ax.text(stair_a_x + stair_a_w/2, stair_a_y - 0.25, 'Cầu thang A\n(Xuống tầng 1)', color=COLOR_TEXT_MUTED, fontsize=8.0, ha='center', va='top', zorder=8)

    # --- Cầu thang B (Tòa 2): X: 23.5 to 26.5, Y: 13.5 to 16.5 ---
    stair_b_x, stair_b_y, stair_b_w, stair_b_h = 23.5, 13.5, 3.0, 3.0
    ax.add_patch(patches.Rectangle((stair_b_x, stair_b_y), stair_b_w, stair_b_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.2, zorder=6))
    ax.plot([stair_b_x + stair_b_w/2, stair_b_x + stair_b_w/2], [stair_b_y, stair_b_y + stair_b_h], color=COLOR_WALL, linewidth=1.0, zorder=7)
    for i in range(1, num_steps):
        sy = stair_b_y + i * (stair_b_h / num_steps)
        ax.plot([stair_b_x, stair_b_x + stair_b_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=7)
    ax.annotate('', xy=(stair_b_x + stair_b_w*0.5, stair_b_y + 0.3), xytext=(stair_b_x + stair_b_w*0.5, stair_b_y + stair_b_h - 0.3),
                arrowprops=dict(arrowstyle="->", color=COLOR_WALL, lw=1.2), zorder=8)
    ax.text(stair_b_x + stair_b_w/2, stair_b_y - 0.25, 'Cầu thang B\n(Xuống tầng 1)', color=COLOR_TEXT_MUTED, fontsize=8.0, ha='center', va='top', zorder=8)

    # ---------------------------------------------------------
    # 6. STRUCTURAL WALLS & PARTITIONS (DARK SLATE)
    # ---------------------------------------------------------
    def draw_wall(x1: float, y1: float, x2: float, y2: float, thick: float = W, z: int = 10):
        if abs(y1 - y2) < 1e-4:  # Horizontal
            xmin, xmax = min(x1, x2), max(x1, x2)
            ax.add_patch(patches.Rectangle((xmin, y1 - thick/2), xmax - xmin, thick, facecolor=COLOR_WALL, edgecolor='none', zorder=z))
        elif abs(x1 - x2) < 1e-4:  # Vertical
            ymin, ymax = min(y1, y2), max(y1, y2)
            ax.add_patch(patches.Rectangle((x1 - thick/2, ymin), thick, ymax - ymin, facecolor=COLOR_WALL, edgecolor='none', zorder=z))

    # --- TÒA 1 NGOẠI THẤT (ENCLOSED SOLID WALLS FOR UPPER FLOOR) ---
    # South Facade:
    draw_wall(0.0, Y_A_WING_BOT, 8.0, Y_A_WING_BOT)
    draw_wall(8.0, Y_A_WING_BOT, 8.0, Y_A_BODY_BOT)
    draw_wall(8.0, Y_A_BODY_BOT, 40.0, Y_A_BODY_BOT)
    draw_wall(40.0, Y_A_WING_BOT, 40.0, Y_A_BODY_BOT)
    draw_wall(40.0, Y_A_WING_BOT, 48.0, Y_A_WING_BOT)

    # West & East Ends:
    draw_wall(0.0, Y_A_WING_BOT, 0.0, Y_A_WING_TOP)
    draw_wall(48.0, Y_A_WING_BOT, 48.0, Y_A_WING_TOP)

    # North Facade:
    draw_wall(0.0, Y_A_WING_TOP, 8.0, Y_A_WING_TOP)
    draw_wall(8.0, Y_A_BODY_TOP, 8.0, Y_A_WING_TOP)
    draw_wall(8.0, Y_A_BODY_TOP, X_BRIDGE_L, Y_A_BODY_TOP)
    draw_wall(X_BRIDGE_R, Y_A_BODY_TOP, 40.0, Y_A_BODY_TOP)
    draw_wall(40.0, Y_A_BODY_TOP, 40.0, Y_A_WING_TOP)
    draw_wall(40.0, Y_A_WING_TOP, 48.0, Y_A_WING_TOP)

    # --- NHỊP CẦU NỐI TRUNG TÂM (WALLS ON BOTH SIDES) ---
    draw_wall(X_BRIDGE_L, Y_BRIDGE_BOT, X_BRIDGE_L, Y_BRIDGE_TOP)
    draw_wall(X_BRIDGE_R, Y_BRIDGE_BOT, X_BRIDGE_R, Y_BRIDGE_TOP)

    # --- TÒA 2 (KHỐI XÉT XỬ) NGOẠI THẤT ---
    # South Facade:
    draw_wall(0.0, Y_B_WING_BOT, 8.0, Y_B_WING_BOT)
    draw_wall(8.0, Y_B_WING_BOT, 8.0, Y_B_BODY_BOT)
    draw_wall(8.0, Y_B_BODY_BOT, X_BRIDGE_L, Y_B_BODY_BOT)
    draw_wall(X_BRIDGE_R, Y_B_BODY_BOT, 40.0, Y_B_BODY_BOT)
    draw_wall(40.0, Y_B_WING_BOT, 40.0, Y_B_BODY_BOT)
    draw_wall(40.0, Y_B_WING_BOT, 48.0, Y_B_WING_BOT)

    # West & East Ends:
    draw_wall(0.0, Y_B_WING_BOT, 0.0, Y_B_WING_TOP)
    draw_wall(48.0, Y_B_WING_BOT, 48.0, Y_B_WING_TOP)

    # North Facade:
    draw_wall(0.0, Y_B_WING_TOP, 8.0, Y_B_WING_TOP)
    draw_wall(8.0, Y_B_BODY_TOP, 8.0, Y_B_WING_TOP)
    draw_wall(8.0, Y_B_BODY_TOP, 40.0, Y_B_BODY_TOP)
    draw_wall(40.0, Y_B_BODY_TOP, 40.0, Y_B_WING_TOP)
    draw_wall(40.0, Y_B_WING_TOP, 48.0, Y_B_WING_TOP)

    # --- TÒA 1 NỘI THẤT VÁCH NGĂN ---
    # Corridor Horizontal Walls with door gaps:
    # South Corridor Wall (Y = -0.9m)
    draw_wall(0.0, Y_A_CORR_BOT, 6.2, Y_A_CORR_BOT, thick=P)
    draw_wall(7.1, Y_A_CORR_BOT, 9.2, Y_A_CORR_BOT, thick=P)
    draw_wall(10.1, Y_A_CORR_BOT, 15.8, Y_A_CORR_BOT, thick=P)
    draw_wall(16.7, Y_A_CORR_BOT, 21.0, Y_A_CORR_BOT, thick=P)
    draw_wall(27.0, Y_A_CORR_BOT, 31.3, Y_A_CORR_BOT, thick=P)
    draw_wall(32.2, Y_A_CORR_BOT, 37.6, Y_A_CORR_BOT, thick=P)
    draw_wall(38.5, Y_A_CORR_BOT, 40.9, Y_A_CORR_BOT, thick=P)
    draw_wall(41.8, Y_A_CORR_BOT, 48.0, Y_A_CORR_BOT, thick=P)

    # North Corridor Wall (Y = 0.9m)
    draw_wall(0.0, Y_A_CORR_TOP, 6.2, Y_A_CORR_TOP, thick=P)
    draw_wall(7.1, Y_A_CORR_TOP, 9.2, Y_A_CORR_TOP, thick=P)
    draw_wall(10.1, Y_A_CORR_TOP, 21.0, Y_A_CORR_TOP, thick=P)
    draw_wall(27.0, Y_A_CORR_TOP, 37.6, Y_A_CORR_TOP, thick=P)
    draw_wall(38.5, Y_A_CORR_TOP, 40.9, Y_A_CORR_TOP, thick=P)
    draw_wall(41.8, Y_A_CORR_TOP, 48.0, Y_A_CORR_TOP, thick=P)

    # Tòa 1 Vertical Partitions:
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

    # --- TÒA 2 (KHỐI XÉT XỬ) NỘI THẤT VÁCH NGĂN ---
    # 1. Divider Wall at X = 8.0m (Separating Room 1 - West Wing from West Body):
    # Upper segment (separates Room 1 from Room 2): Y: 13.2 to 20.6
    draw_wall(8.0, Y_B_CORR_DIV, 8.0, Y_B_BODY_TOP, thick=P)
    # Lower segment (corridor wall leading into Room 1 with door gap at Y: 11.5 - 12.5m)
    draw_wall(8.0, Y_B_BODY_BOT, 8.0, 11.5, thick=P)
    draw_wall(8.0, 12.5, 8.0, Y_B_CORR_DIV, thick=P)

    # 2. Divider Wall at Y = 13.2m (South wall of Room 2, dividing Room 2 from West Corridor):
    # Door gap at X: 17.5 to 18.5m
    draw_wall(8.0, Y_B_CORR_DIV, 17.5, Y_B_CORR_DIV, thick=P)
    draw_wall(18.5, Y_B_CORR_DIV, 21.0, Y_B_CORR_DIV, thick=P)

    # 3. Divider Wall at X = 21.0m (East wall of Room 2, dividing Room 2 from Central Lobby):
    draw_wall(21.0, Y_B_CORR_DIV, 21.0, Y_B_BODY_TOP, thick=P)

    # 4. Divider Wall at X = 40.0m (Separating Room 3 - East Wing from East Sảnh):
    # Door gap at Y: 15.35 to 16.35m
    draw_wall(40.0, Y_B_BODY_BOT, 40.0, 15.35, thick=P)
    draw_wall(40.0, 16.35, 40.0, Y_B_BODY_TOP, thick=P)

    # ---------------------------------------------------------
    # 7. WINDOWS (WHITE OPENING CUT WITH DOUBLE PARALLEL LINES)
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
    draw_window_h(2.5, 5.5, Y_A_WING_BOT)
    draw_window_h(9.5, 13.0, Y_A_BODY_BOT)
    draw_window_h(16.0, 19.5, Y_A_BODY_BOT)
    draw_window_h(22.5, 25.5, Y_A_BODY_BOT)  # Window for Sảnh Tầng 2
    draw_window_h(28.5, 32.0, Y_A_BODY_BOT)
    draw_window_h(35.0, 38.5, Y_A_BODY_BOT)
    draw_window_h(42.5, 45.5, Y_A_WING_BOT)

    # North Windows:
    draw_window_h(2.5, 5.5, Y_A_WING_TOP)
    draw_window_h(11.0, 18.0, Y_A_BODY_TOP)
    draw_window_h(30.0, 37.0, Y_A_BODY_TOP)
    draw_window_h(42.5, 45.5, Y_A_WING_TOP)

    # East & West End Corridor Windows:
    draw_window_v(0.0, -0.6, 0.6)
    draw_window_v(48.0, -0.6, 0.6)

    # --- Windows Tòa 2 (Khối Xét xử) ---
    # North Windows:
    draw_window_h(2.0, 6.0, Y_B_WING_TOP)       # Room 1 (West Wing) North window
    draw_window_h(10.0, 14.0, Y_B_BODY_TOP)     # Room 2 (West Body) North window 1
    draw_window_h(15.0, 19.0, Y_B_BODY_TOP)     # Room 2 (West Body) North window 2
    draw_window_h(22.5, 25.5, Y_B_BODY_TOP)     # Central Lobby North window
    draw_window_h(29.0, 33.0, Y_B_BODY_TOP)     # East Sảnh North window 1
    draw_window_h(34.0, 38.0, Y_B_BODY_TOP)     # East Sảnh North window 2
    draw_window_h(42.0, 46.0, Y_B_WING_TOP)     # Room 3 (East Wing) North window

    # South Windows:
    draw_window_h(2.0, 6.0, Y_B_WING_BOT)       # Room 1 (West Wing) South window
    draw_window_h(10.0, 14.0, Y_B_BODY_BOT)     # West Corridor South window 1 (courtyard view)
    draw_window_h(15.0, 19.0, Y_B_BODY_BOT)     # West Corridor South window 2 (courtyard view)
    draw_window_h(29.0, 33.0, Y_B_BODY_BOT)     # East Sảnh South window 1 (courtyard view)
    draw_window_h(34.0, 38.0, Y_B_BODY_BOT)     # East Sảnh South window 2 (courtyard view)
    draw_window_h(42.0, 46.0, Y_B_WING_BOT)     # Room 3 (East Wing) South window

    # West & East Facade Windows:
    draw_window_v(0.0, 17.5, 20.5)              # Room 1 West window 1
    draw_window_v(0.0, 11.0, 14.0)              # Room 1 West window 2
    draw_window_v(48.0, 17.5, 20.5)             # Room 3 East window 1
    draw_window_v(48.0, 11.0, 14.0)             # Room 3 East window 2

    # ---------------------------------------------------------
    # 8. DOORS & DOOR SWINGS
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
        elif mode == 'W_IN_UP':
            ax.plot([x - size, x], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'E_IN_UP':
            ax.plot([x + size, x], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)

    # Draw Doors for Tòa 1 Rooms:
    for r in rooms:
        dx, dy, dsize, dmode = r['door']
        draw_door(dx, dy, dsize, dmode)

    # Draw Doors for Tòa 2 Rooms (ĐÚNG 3 PHÒNG THEO HÌNH VẼ KHOANH CHỮ X):
    # 1. Phòng 1 (Cánh Tây - West Wing): cửa tại vách X = 8.0, Y = 11.5, mở vào trong Cánh Tây
    draw_door(8.0, 11.5, 0.9, 'W_IN_UP')

    # 2. Phòng 2 (Thân Tây - West Body): cửa tại vách Y = 13.2, X = 17.5, mở vào trong lòng Phòng 2
    draw_door(17.5, Y_B_CORR_DIV, 0.9, 'N_IN_RIGHT')

    # 3. Phòng 3 (Cánh Đông - East Wing): cửa tại vách X = 40.0, Y = 15.35, mở vào trong Cánh Đông
    draw_door(40.0, 15.35, 0.9, 'E_IN_UP')

    # ---------------------------------------------------------
    # 9. ROOM & CIRCULATION LABELS (STRICTLY CLEAN, SINGLE-LINE)
    # ---------------------------------------------------------
    # Tòa 1 Rooms Labels (10 Phòng):
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 10.0)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                fontweight='bold', ha='center', va='center', zorder=15)

    # Tòa 2 Rooms Labels (ĐÚNG 3 PHÒNG LÀM VIỆC THEO 3 KHU VỰC KHOANH CHỮ X):
    # Phòng 1 (Cánh Tây):
    ax.text(4.0, 15.8, 'Phòng làm việc', color=COLOR_TEXT_MAIN, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=15)
    # Phòng 2 (Thân Tây):
    ax.text(14.5, 16.9, 'Phòng làm việc', color=COLOR_TEXT_MAIN, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=15)
    # Phòng 3 (Cánh Đông):
    ax.text(44.0, 15.8, 'Phòng làm việc', color=COLOR_TEXT_MAIN, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=15)

    # Circulation Labels:
    # Tòa 1 Hành lang:
    ax.text(14.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=15)
    ax.text(33.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=15)
    ax.text(24.0, -2.7, 'SẢNH TẦNG 2', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=15)

    # Bridge Link Label:
    ax.text(24.0, 7.75, 'HÀNH LANG CẦU NỐI\n(THÔNG 2 TÒA)', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=15)

    # Tòa 2 Circulation Labels:
    ax.text(24.0, 18.6, 'SẢNH TRUNG TÂM\n(TẦNG 2)', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=15)
    ax.text(14.5, 12.1, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=15)
    ax.text(33.5, 15.8, 'SẢNH TẦNG 2', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=15)

    # ---------------------------------------------------------
    # 10. EXPORT OUTPUTS
    # ---------------------------------------------------------
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Successfully generated floorplan image at: {out_img_path}")

if __name__ == '__main__':
    target_dir = r'c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau6\Tang2'
    create_floorplan_tang2(target_dir)
