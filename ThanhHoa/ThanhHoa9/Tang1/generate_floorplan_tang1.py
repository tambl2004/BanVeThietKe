import os
from typing import TypedDict, Tuple, List, Optional
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class RoomDict(TypedDict):
    id: str
    name: str
    x: float
    y: float
    w: float
    h: float
    text_center: Tuple[float, float]
    door: Optional[Tuple[float, float, float, str]]
    font_size: float

COURT_NAME = "Tòa án nhân dân khu vực 9 - Thanh Hóa"

def create_floorplan_tang1(court_name: str = COURT_NAME):
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(26, 13), dpi=300)
    ax = fig.add_axes([0.02, 0.08, 0.96, 0.82])
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
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 stair fill matches lobby background

    # 3 Separate Buildings:
    # TÒA A1 (West Wing): X = 0.0 to 8.0, Y = -6.5 to 6.5
    # Sân nội bộ giữa A1 và A2: X = 8.0 to 12.0
    # TÒA A2 (Main Center): X = 12.0 to 38.0, Y = -4.5 to 4.5 (Lobby South to -5.3, Rear North to 5.3)
    # Sân nội bộ giữa A2 và A3: X = 38.0 to 42.0
    # TÒA A3 (East Wing): X = 42.0 to 50.0, Y = -6.5 to 6.5

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.02, 0.95, f'MẶT BẰNG TẦNG 1  —  {court_name}',
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.02, 0.98], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box Centered at Bottom
    lg_x, lg_y = 15.0, -8.6
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.9, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.2, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.add_patch(patches.Rectangle((lg_x + 6.0, lg_y + 0.1), 0.9, 0.14, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 7.2, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 11.5, lg_x + 12.6], [lg_y + 0.24, lg_y + 0.24], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 11.5, lg_x + 12.6], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 12.9, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 16.5, lg_x + 16.5], [lg_y + 0.05, lg_y + 0.40], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 16.5, lg_y + 0.05), 0.7, 0.7, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.1)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 17.5, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Prominent Building Block Titles
    ax.text(4.0, 7.4, 'TÒA A1 (XÉT XỬ DÂN SỰ & TIẾP DÂN)', fontsize=11.5, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(25.0, 6.2, 'TÒA A2 (KHỐI HÀNH CHÍNH TRUNG TÂM)', fontsize=12.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(46.0, 7.4, 'TÒA A3 (XÉT XỬ HÌNH SỰ & HOÀ GIẢI)', fontsize=11.5, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')

    # Courtyard Labels between buildings
    ax.text(10.0, 0.0, 'KHOẢNG SÂN\nNỘI BỘ', fontsize=8.5, color='#94a3b8', fontweight='bold', ha='center', va='center')
    ax.text(40.0, 0.0, 'KHOẢNG SÂN\nNỘI BỘ', fontsize=8.5, color='#94a3b8', fontweight='bold', ha='center', va='center')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILLS
    # ---------------------------------------------------------
    # === TÒA A1: Internal Corridor (X: 0.0 to 8.0, Y: -0.9 to 0.9) ===
    ax.add_patch(patches.Rectangle((0.0, -0.9), 8.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === TÒA A2: Corridor & Main Lobbies ===
    # Horizontal Corridor (X: 12.0 to 38.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((12.0, -0.9), 26.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # South Main Entrance Lobby (X: 22.0 to 28.0, Y: -5.3 to -0.9)
    ax.add_patch(patches.Rectangle((22.0, -5.3), 6.0, 4.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # North Rear Hall & Stairs Passage (X: 22.0 to 28.0, Y: 0.9 to 5.3)
    ax.add_patch(patches.Rectangle((22.0, 0.9), 6.0, 4.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === TÒA A3: Internal Corridor (X: 42.0 to 50.0, Y: -0.9 to 0.9) ===
    ax.add_patch(patches.Rectangle((42.0, -0.9), 8.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (3 TÒA NHÀ - 13 PHÒNG KHẢO SÁT)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA A1 (2 PHÒNG) ===
        {
            'id': 'T1_A1_XXDS', 'name': 'Phòng xét xử\ndân sự tầng 1',
            'x': 0.0, 'y': 0.9, 'w': 8.0, 'h': 5.6,
            'text_center': (4.0, 3.7),
            'door': (6.0, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'T1_A1_TD', 'name': 'Phòng tiếp dân',
            'x': 0.0, 'y': -6.5, 'w': 8.0, 'h': 5.6,
            'text_center': (4.0, -3.7),
            'door': (6.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.5
        },

        # === TÒA A2 (8 PHÒNG) ===
        # Dãy phía Bắc (Y: 0.9 to 4.5m)
        {
            'id': 'T1_A2_PCA1', 'name': 'Phòng Phó\nChánh án',
            'x': 12.0, 'y': 0.9, 'w': 5.0, 'h': 3.6,
            'text_center': (14.5, 2.7),
            'door': (13.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T1_A2_CVP', 'name': 'Phòng Chánh\nvăn phòng',
            'x': 17.0, 'y': 0.9, 'w': 5.0, 'h': 3.6,
            'text_center': (19.5, 2.7),
            'door': (18.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'T1_A2_TP', 'name': 'Phòng\nThẩm phán',
            'x': 28.0, 'y': 0.9, 'w': 5.0, 'h': 3.6,
            'text_center': (30.5, 2.7),
            'door': (29.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T1_A2_KT', 'name': 'Phòng\nKế toán',
            'x': 33.0, 'y': 0.9, 'w': 5.0, 'h': 3.6,
            'text_center': (35.5, 2.7),
            'door': (34.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },

        # Dãy phía Nam (Y: -4.5 to -0.9m)
        {
            'id': 'T1_A2_PH', 'name': 'Phòng họp',
            'x': 12.0, 'y': -4.5, 'w': 10.0, 'h': 3.6,
            'text_center': (17.0, -2.7),
            'door': (20.2, -0.9, 0.95, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
        {
            'id': 'T1_A2_PCA2', 'name': 'Phòng Phó\nChánh án',
            'x': 28.0, 'y': -4.5, 'w': 3.4, 'h': 3.6,
            'text_center': (29.7, -2.7),
            'door': (28.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'T1_A2_CA', 'name': 'Phòng\nChánh án',
            'x': 31.4, 'y': -4.5, 'w': 3.4, 'h': 3.6,
            'text_center': (33.1, -2.7),
            'door': (32.2, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.8
        },
        {
            'id': 'T1_A2_TK', 'name': 'Phòng\nthư ký',
            'x': 34.8, 'y': -4.5, 'w': 3.2, 'h': 3.6,
            'text_center': (36.4, -2.7),
            'door': (35.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.5
        },

        # === TÒA A3 (3 PHÒNG) ===
        {
            'id': 'T1_A3_XXHS', 'name': 'Phòng xét xử\nhình sự',
            'x': 42.0, 'y': 0.9, 'w': 8.0, 'h': 5.6,
            'text_center': (46.0, 3.7),
            'door': (43.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'T1_A3_HGV1', 'name': 'Phòng\nhoà giải viên',
            'x': 42.0, 'y': -6.5, 'w': 4.0, 'h': 5.6,
            'text_center': (44.0, -3.7),
            'door': (42.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.8
        },
        {
            'id': 'T1_A3_HGV2', 'name': 'Phòng\nhoà giải viên',
            'x': 46.0, 'y': -6.5, 'w': 4.0, 'h': 5.6,
            'text_center': (48.0, -3.7),
            'door': (46.8, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.8
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE (TÒA A2 - TẦNG 1 NỀN `#eef4f7`)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 23.5, 1.3, 3.0, 3.2
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Center railing divider running from step 2 down to bottom
    mid_x = stair_x + stair_w / 2.0
    top_landing_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_landing_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    ax.text(mid_x, stair_y - 0.25, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.0, ha='center', va='top', zorder=5)

    # ---------------------------------------------------------
    # 6. EXTERIOR STEPS (TẦNG 1 SPEC)
    # ---------------------------------------------------------
    # TÒA A2 South Main Entrance Steps (X: 22.0 to 28.0, Y: -5.3 down to -6.1)
    for step_y in np.linspace(-5.3, -6.1, 5):
        ax.plot([22.0, 28.0], [step_y, step_y], color=COLOR_WALL, linewidth=0.9, zorder=2)
    ax.plot([22.0, 22.0], [-5.3, -6.1], color=COLOR_WALL, linewidth=2.8, solid_capstyle='butt', zorder=5)
    ax.plot([28.0, 28.0], [-5.3, -6.1], color=COLOR_WALL, linewidth=2.8, solid_capstyle='butt', zorder=5)

    # TÒA A2 North Rear Exit Steps (X: 22.0 to 28.0, Y: 4.5 up to 5.3)
    for step_y in np.linspace(4.5, 5.3, 5):
        ax.plot([22.0, 28.0], [step_y, step_y], color=COLOR_WALL, linewidth=0.8, zorder=2)
    ax.plot([22.0, 22.0], [4.5, 5.3], color=COLOR_WALL, linewidth=2.8, solid_capstyle='butt', zorder=5)
    ax.plot([28.0, 28.0], [4.5, 5.3], color=COLOR_WALL, linewidth=2.8, solid_capstyle='butt', zorder=5)
    ax.plot([22.0, 22.5], [5.3, 5.3], color=COLOR_WALL, linewidth=2.8, solid_capstyle='butt', zorder=5)
    ax.plot([28.0, 27.5], [5.3, 5.3], color=COLOR_WALL, linewidth=2.8, solid_capstyle='butt', zorder=5)

    # TÒA A2 West & East Exit Steps into Courtyards
    for step_x in np.linspace(12.0, 11.2, 5):
        ax.plot([step_x, step_x], [-0.9, 0.9], color=COLOR_WALL, linewidth=0.8, zorder=2)
    for step_x in np.linspace(38.0, 38.8, 5):
        ax.plot([step_x, step_x], [-0.9, 0.9], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # TÒA A1 East Entrance Steps from Courtyard
    for step_x in np.linspace(8.0, 8.8, 5):
        ax.plot([step_x, step_x], [-0.9, 0.9], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # TÒA A3 West Entrance Steps from Courtyard
    for step_x in np.linspace(42.0, 41.2, 5):
        ax.plot([step_x, step_x], [-0.9, 0.9], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # ---------------------------------------------------------
    # 7. EXTERIOR WALLS & INTERIOR PARTITIONS (3 TÒA RIÊNG BIỆT)
    # ---------------------------------------------------------
    def draw_wall(x1, y1, x2, y2, lw=2.4):
        ax.plot([x1, x2], [y1, y2], color=COLOR_WALL, linewidth=lw, solid_capstyle='butt', zorder=5)

    def draw_part(x1, y1, x2, y2, lw=1.2):
        ax.plot([x1, x2], [y1, y2], color=COLOR_WALL, linewidth=lw, solid_capstyle='butt', zorder=5)

    # ================== TÒA A1 (ĐỘC LẬP) ==================
    # West wall: continuous from -6.5 to 6.5
    draw_wall(0.0, -6.5, 0.0, 6.5)
    # North wall: X = 0.0 to 8.0, Y = 6.5
    draw_wall(0.0, 6.5, 8.0, 6.5)
    # South wall: X = 0.0 to 8.0, Y = -6.5
    draw_wall(0.0, -6.5, 8.0, -6.5)
    # East wall: X = 8.0, open at corridor Y = -0.9 to 0.9
    draw_wall(8.0, -6.5, 8.0, -0.9)
    draw_wall(8.0, 0.9, 8.0, 6.5)

    # A1 Corridor walls (Y = 0.9 & -0.9)
    draw_part(0.0, 0.9, 6.0, 0.9)
    draw_part(6.9, 0.9, 8.0, 0.9)
    draw_part(0.0, -0.9, 6.0, -0.9)
    draw_part(6.9, -0.9, 8.0, -0.9)

    # ================== TÒA A2 (ĐỘC LẬP) ==================
    # North wall: X = 12.0 to 22.0 and 28.0 to 38.0 at Y = 4.5
    draw_wall(12.0, 4.5, 22.0, 4.5)
    draw_wall(28.0, 4.5, 38.0, 4.5)

    # South wall: X = 12.0 to 22.0 and 28.0 to 38.0 at Y = -4.5
    draw_wall(12.0, -4.5, 22.0, -4.5)
    draw_wall(22.0, -4.5, 22.0, -5.3)
    draw_wall(28.0, -4.5, 28.0, -5.3)
    draw_wall(28.0, -4.5, 38.0, -4.5)

    # West wall: X = 12.0, open at corridor Y = -0.9 to 0.9
    draw_wall(12.0, -4.5, 12.0, -0.9)
    draw_wall(12.0, 0.9, 12.0, 4.5)

    # East wall: X = 38.0, open at corridor Y = -0.9 to 0.9
    draw_wall(38.0, -4.5, 38.0, -0.9)
    draw_wall(38.0, 0.9, 38.0, 4.5)

    # A2 Corridor walls:
    # North corridor (Y = 0.9):
    draw_part(12.0, 0.9, 13.2, 0.9)
    draw_part(14.05, 0.9, 18.2, 0.9)
    draw_part(19.05, 0.9, 22.0, 0.9)
    draw_part(28.0, 0.9, 29.2, 0.9)
    draw_part(30.05, 0.9, 34.2, 0.9)
    draw_part(35.05, 0.9, 38.0, 0.9)

    # South corridor (Y = -0.9):
    draw_part(12.0, -0.9, 20.2, -0.9)
    draw_part(21.15, -0.9, 22.0, -0.9)
    draw_part(28.0, -0.9, 28.8, -0.9)
    draw_part(29.6, -0.9, 32.2, -0.9)
    draw_part(33.0, -0.9, 35.5, -0.9)
    draw_part(36.3, -0.9, 38.0, -0.9)

    # A2 Vertical Partitions:
    draw_part(17.0, 0.9, 17.0, 4.5)
    draw_part(22.0, 0.9, 22.0, 4.5)
    draw_part(28.0, 0.9, 28.0, 4.5)
    draw_part(33.0, 0.9, 33.0, 4.5)

    draw_part(31.4, -4.5, 31.4, -0.9)
    draw_part(34.8, -4.5, 34.8, -0.9)

    # ================== TÒA A3 (ĐỘC LẬP) ==================
    # West wall: X = 42.0, open at corridor Y = -0.9 to 0.9
    draw_wall(42.0, -6.5, 42.0, -0.9)
    draw_wall(42.0, 0.9, 42.0, 6.5)
    # North wall: X = 42.0 to 50.0, Y = 6.5
    draw_wall(42.0, 6.5, 50.0, 6.5)
    # South wall: X = 42.0 to 50.0, Y = -6.5
    draw_wall(42.0, -6.5, 50.0, -6.5)
    # East wall: continuous from -6.5 to 6.5
    draw_wall(50.0, -6.5, 50.0, 6.5)

    # A3 Corridor walls (Y = 0.9 & -0.9)
    draw_part(42.0, 0.9, 43.5, 0.9)
    draw_part(44.4, 0.9, 50.0, 0.9)
    draw_part(42.0, -0.9, 42.8, -0.9)
    draw_part(43.6, -0.9, 46.8, -0.9)
    draw_part(47.6, -0.9, 50.0, -0.9)

    # A3 South vertical partition:
    draw_part(46.0, -6.5, 46.0, -0.9)

    # ---------------------------------------------------------
    # 8. DOORS (CỬA ĐI MỞ VÀO)
    # ---------------------------------------------------------
    def draw_door(dx, dy, dw, dtype):
        if dtype == 'N_IN_RIGHT':
            ax.plot([dx, dx], [dy, dy + dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=6)
            arc = patches.Arc((dx, dy), 2 * dw, 2 * dw, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=6)
            ax.add_patch(arc)
        elif dtype == 'S_IN_RIGHT':
            ax.plot([dx, dx], [dy, dy - dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=6)
            arc = patches.Arc((dx, dy), 2 * dw, 2 * dw, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=6)
            ax.add_patch(arc)

    for r in rooms:
        if r['door']:
            dx, dy, dw, dtype = r['door']
            draw_door(dx, dy, dw, dtype)

    # ---------------------------------------------------------
    # 9. WINDOWS (CỬA SỔ KÍNH NGOẠI THẤT)
    # ---------------------------------------------------------
    def draw_window_h(x1, x2, y):
        ax.plot([x1, x2], [y + 0.08, y + 0.08], color=COLOR_WALL, linewidth=1.4, zorder=6)
        ax.plot([x1, x2], [y - 0.08, y - 0.08], color=COLOR_WALL, linewidth=1.4, zorder=6)

    def draw_window_v(x, y1, y2):
        ax.plot([x + 0.08, x + 0.08], [y1, y2], color=COLOR_WALL, linewidth=1.4, zorder=6)
        ax.plot([x - 0.08, x - 0.08], [y1, y2], color=COLOR_WALL, linewidth=1.4, zorder=6)

    # Windows on Tòa A1:
    draw_window_h(2.0, 6.0, 6.5)    # North
    draw_window_v(0.0, 2.0, 5.0)    # West upper
    draw_window_v(0.0, -5.0, -2.0)  # West lower
    draw_window_h(2.0, 6.0, -6.5)   # South
    draw_window_v(8.0, 2.0, 5.0)    # East upper
    draw_window_v(8.0, -5.0, -2.0)  # East lower

    # Windows on Tòa A2:
    draw_window_h(13.5, 15.5, 4.5)
    draw_window_h(18.5, 20.5, 4.5)
    draw_window_h(29.5, 31.5, 4.5)
    draw_window_h(34.5, 36.5, 4.5)

    draw_window_h(14.0, 16.0, -4.5)
    draw_window_h(18.0, 20.0, -4.5)
    draw_window_h(29.0, 30.5, -4.5)
    draw_window_h(32.0, 33.5, -4.5)
    draw_window_h(35.5, 37.0, -4.5)

    # Windows on Tòa A3:
    draw_window_h(44.0, 48.0, 6.5)  # North
    draw_window_v(50.0, 2.0, 5.0)   # East upper
    draw_window_v(50.0, -5.0, -2.0) # East lower
    draw_window_h(43.0, 45.0, -6.5) # South 1
    draw_window_h(47.0, 49.0, -6.5) # South 2
    draw_window_v(42.0, 2.0, 5.0)   # West upper
    draw_window_v(42.0, -5.0, -2.0) # West lower

    # ---------------------------------------------------------
    # 10. LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'],
                fontweight='bold', ha='center', va='center', zorder=7)

    # Corridor and Lobby Labels
    ax.text(4.0, 0.0, 'SẢNH / HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=7)
    ax.text(17.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=7)
    ax.text(33.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=7)
    ax.text(25.0, -3.0, 'SẢNH ĐÓN CHÍNH', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=7)
    ax.text(25.0, 5.6, 'LỐI RA SAU', color=COLOR_TEXT_MUTED, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=7)
    ax.text(46.0, 0.0, 'SẢNH / HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=7)

    # ---------------------------------------------------------
    # 11. EXPORT DRAWING
    # ---------------------------------------------------------
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(out_dir, 'mat_bang_tang_1.png')
    plt.savefig(out_file, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Bản vẽ Tầng 1 đã xuất thành công tại: {out_file}")

if __name__ == '__main__':
    create_floorplan_tang1()
