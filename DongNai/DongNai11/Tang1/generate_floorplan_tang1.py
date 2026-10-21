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

COURT_NAME = "Tòa án nhân dân khu vực 11 - Đồng Nai"

def create_floorplan_tang1():
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
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND (CENTERED LEGEND AT BOTTOM)
    # ---------------------------------------------------------
    fig.text(0.03, 0.96, f'MẶT BẰNG TẦNG 1  —  {COURT_NAME}',
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.03, 0.97], [0.94, 0.94], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box Centered at Bottom
    lg_x, lg_y = 12.0, -23.5
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.0, 0.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.4, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.add_patch(patches.Rectangle((lg_x + 9.0, lg_y + 0.12), 1.0, 0.16, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 10.4, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 18.0, lg_x + 19.2], [lg_y + 0.25, lg_y + 0.25], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 18.0, lg_x + 19.2], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 19.6, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 24.5, lg_x + 24.5], [lg_y + 0.05, lg_y + 0.45], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=1)
    arc_lg = patches.Arc((lg_x + 24.5, lg_y + 0.05), 0.8, 0.8, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.1)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 25.6, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILLS
    # ---------------------------------------------------------
    # === TÒA A CORRIDORS & SẢNH ===
    # Horizontal corridor: X: 0.0 to 40.0, Y: 10.1 to 11.9
    ax.add_patch(patches.Rectangle((0.0, 10.1), 40.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Central Lobby & Stair Hall: X: 21.0 to 27.0, Y: 6.1 to 16.4
    ax.add_patch(patches.Rectangle((21.0, 6.1), 6.0, 10.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === TÒA B CORRIDOR & WAITING AREA ===
    # Vertical Corridor: X: 5.0 to 7.0, Y: -11.0 to 3.0
    ax.add_patch(patches.Rectangle((5.0, -11.0), 2.0, 14.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Sảnh chờ tiếp dân: X: 7.0 to 12.0, Y: -11.0 to -4.0
    ax.add_patch(patches.Rectangle((7.0, -11.0), 5.0, 7.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS & BACKGROUND FILLS
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA A (KHỐI NHÀ CHÍNH PHÍA BẮC - 11 PHÒNG KHẢO SÁT) ===
        # North Row West (Y: 11.9 to 16.4)
        {
            'id': 'TA_N1', 'name': 'Phòng phó Chánh án\nHoàng Ngọc Bạn',
            'x': 0.0, 'y': 11.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 14.15),
            'door': (5.8, 11.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'TA_N2', 'name': 'Phòng phó Chánh án\nNguyễn Trần Ánh Nguyệt',
            'x': 7.5, 'y': 11.9, 'w': 6.5, 'h': 4.5,
            'text_center': (10.75, 14.15),
            'door': (12.2, 11.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'TA_N3', 'name': 'Phòng Thẩm phán\nVũ Thị Phượng',
            'x': 14.0, 'y': 11.9, 'w': 7.0, 'h': 4.5,
            'text_center': (17.5, 14.15),
            'door': (15.5, 11.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 8.5
        },

        # North Row East (Y: 11.9 to 16.4)
        {
            'id': 'TA_N4', 'name': 'Phòng Thẩm phán\nNguyễn Thị Bích Vân',
            'x': 27.0, 'y': 11.9, 'w': 6.5, 'h': 4.5,
            'text_center': (30.25, 14.15),
            'door': (28.2, 11.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'TA_N5', 'name': 'Phòng Thư ký\nTrần Minh Toản',
            'x': 33.5, 'y': 11.9, 'w': 6.5, 'h': 4.5,
            'text_center': (36.75, 14.15),
            'door': (34.7, 11.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 8.5
        },

        # South Row West (Y: 6.1 to 10.1)
        {
            'id': 'TA_S1', 'name': 'Phòng Thư ký\nNguyễn Thị Tường Vì',
            'x': 0.0, 'y': 6.1, 'w': 7.0, 'h': 4.0,
            'text_center': (3.5, 8.1),
            'door': (5.5, 10.1, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'TA_S2', 'name': 'Phòng Thư ký\nPhạm Thị Thùy Duyên',
            'x': 7.0, 'y': 6.1, 'w': 7.0, 'h': 4.0,
            'text_center': (10.5, 8.1),
            'door': (12.2, 10.1, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'TA_S3', 'name': 'Phòng Thư ký\nNguyễn Thị Như Ý',
            'x': 14.0, 'y': 6.1, 'w': 7.0, 'h': 4.0,
            'text_center': (17.5, 8.1),
            'door': (15.5, 10.1, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.5
        },

        # South Row East (Y: 6.1 to 10.1)
        {
            'id': 'TA_S4', 'name': 'Phòng Thư ký\nNguyễn Tú Anh',
            'x': 27.0, 'y': 6.1, 'w': 6.5, 'h': 4.0,
            'text_center': (30.25, 8.1),
            'door': (28.2, 10.1, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'TA_S5', 'name': 'Phòng nghị án',
            'x': 33.5, 'y': 6.1, 'w': 6.5, 'h': 4.0,
            'text_center': (36.75, 8.1),
            'door': (34.7, 10.1, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },

        # Tòa A East End: Phòng xét xử (X: 40.0 to 48.0, Y: 6.1 to 16.4)
        {
            'id': 'TA_XX', 'name': 'Phòng xét xử',
            'x': 40.0, 'y': 6.1, 'w': 8.0, 'h': 10.3,
            'text_center': (44.0, 11.25),
            'door': (40.0, 11.5, 1.0, 'ROOM_RIGHT_IN'),
            'font_size': 11.0
        },

        # === TÒA B (CÁNH TÂY - TÒA HÀNH CHÍNH TƯ PHÁP, 4 PHÒNG) ===
        {
            'id': 'TB_1', 'name': 'Phòng tiếp dân',
            'x': 0.0, 'y': -4.0, 'w': 5.0, 'h': 7.0,
            'text_center': (2.5, -0.5),
            'door': (5.0, 1.4, 0.85, 'ROOM_LEFT_IN'),
            'font_size': 8.5
        },
        {
            'id': 'TB_2', 'name': 'Phòng hòa giải',
            'x': 7.0, 'y': -4.0, 'w': 5.0, 'h': 7.0,
            'text_center': (9.5, -0.5),
            'door': (7.0, 1.4, 0.85, 'ROOM_RIGHT_IN'),
            'font_size': 8.5
        },
        {
            'id': 'TB_3', 'name': 'Phòng hòa giải',
            'x': 0.0, 'y': -11.0, 'w': 5.0, 'h': 7.0,
            'text_center': (2.5, -7.5),
            'door': (5.0, -5.6, 0.85, 'ROOM_LEFT_IN'),
            'font_size': 8.5
        },
        {
            'id': 'TB_4', 'name': 'Phòng Hành chính tư pháp',
            'x': 0.0, 'y': -19.0, 'w': 12.0, 'h': 8.0,
            'text_center': (6.0, -15.0),
            'door': (5.5, -11.0, 1.0, 'S_IN_RIGHT'),
            'font_size': 9.5
        },

        # === TÒA XÉT XỬ (CÁNH ĐÔNG - NHÀ XÉT XỬ, 2 PHÒNG XÉT XỬ LỚN) ===
        {
            'id': 'TX_1', 'name': 'Phòng xét xử hình sự',
            'x': 36.0, 'y': -8.0, 'w': 12.0, 'h': 11.0,
            'text_center': (42.0, -2.5),
            'door': (36.0, -0.5, 1.2, 'DOUBLE_EAST_IN'),
            'font_size': 11.0
        },
        {
            'id': 'TX_2', 'name': 'Phòng xét xử dân sự',
            'x': 36.0, 'y': -19.0, 'w': 12.0, 'h': 11.0,
            'text_center': (42.0, -13.5),
            'door': (36.0, -11.5, 1.2, 'DOUBLE_EAST_IN'),
            'font_size': 11.0
        },
    ]

    # Draw Room Background Fills
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES & ENTRANCE/EXIT STEPS
    # ---------------------------------------------------------
    # === TÒA A STAIRCASES & STEPS ===
    stair_a_x, stair_a_y, stair_a_w, stair_a_h = 22.5, 11.9, 3.0, 3.5
    stair_a_bg = patches.Rectangle((stair_a_x, stair_a_y), stair_a_w, stair_a_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_a_bg)

    for i in range(10):
        sy = stair_a_y + i * (stair_a_h / 9.0)
        ax.plot([stair_a_x, stair_a_x + stair_a_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
    ax.plot([stair_a_x + stair_a_w / 2.0, stair_a_x + stair_a_w / 2.0], [stair_a_y, stair_a_y + stair_a_h * (8.0/9.0)], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair_a_x + stair_a_w / 2.0, stair_a_y - 0.35, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=8.5, ha='center', va='top', zorder=5)

    # Front Main Entrance Steps at Tòa A (South: Y = 5.3 to 6.1)
    for sy in np.linspace(5.3, 6.1, 6):
        ax.plot([21.0, 27.0], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Rear Exit Steps at Tòa A (North: Y = 16.4 to 17.2)
    for sy in np.linspace(16.4, 17.2, 6):
        ax.plot([21.0, 27.0], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # West End Steps at Tòa A Corridor (X = -0.8 to 0.0)
    for i in range(5):
        dx = -0.16 * (i + 1)
        ax.plot([dx, 0.0], [11.9, 11.9], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [10.1, 10.1], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [10.1, 11.9], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Tòa B Entrance Steps (North end of corridor)
    for sy in np.linspace(3.0, 3.8, 5):
        ax.plot([5.0, 7.0], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Nhà xét xử Entrance Steps (Courtyard West side for each Courtroom)
    for sx in np.linspace(35.2, 36.0, 5):
        ax.plot([sx, sx], [-1.7, 0.7], color=COLOR_WALL, linewidth=0.8, zorder=4)
        ax.plot([sx, sx], [-12.7, -10.3], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Labels for Lobbies, Corridors and Rooms
    ax.text(24.0, 8.1, 'SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(10.5, 11.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(33.5, 11.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(6.0, -4.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', rotation=90, zorder=5)
    ax.text(9.5, -7.5, 'SẢNH CHỜ TIẾP DÂN', color=COLOR_TEXT_MAIN, fontsize=8.0, fontweight='bold', ha='center', va='center', zorder=5)

    # Building Header Titles
    ax.text(24.0, 17.8, 'TÒA NHÀ CHÍNH', fontsize=12.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(6.0, -21.2, 'TÒA HÀNH CHÍNH TƯ PHÁP', fontsize=10.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(42.0, -21.2, 'TÒA XÉT XỬ', fontsize=11.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')

    # ---------------------------------------------------------
    # 6. DRAW STRUCTURAL WALLS (SOLID FILLED PATTERNS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # === TÒA A EXTERIOR WALLS ===
    draw_wall(-W, 6.1 - W, W, 4.0 + W)                # West lower outer wall
    draw_wall(-W, 11.9, W, 4.5 + W)                   # West upper outer wall
    draw_wall(48.0, 6.1 - W, W, 10.3 + 2*W)           # East outer wall
    draw_wall(-W, 16.4, 21.0 + W + P/2, W)            # North outer wall West
    draw_wall(27.0 - P/2, 16.4, 21.0 + W + P/2, W)    # North outer wall East
    draw_wall(-W, 6.1 - W, 21.0 + W + P/2, W)         # South outer wall West
    draw_wall(27.0 - P/2, 6.1 - W, 21.0 + W + P/2, W) # South outer wall East

    # South Front Entrance Side Walls
    draw_wall(21.0 - P/2, 5.3, P, 0.8)
    draw_wall(27.0 - P/2, 5.3, P, 0.8)

    # North Rear Exit Side Walls with Inward Hooks
    draw_wall(21.0 - P/2, 16.4, P, 0.8)
    draw_wall(27.0 - P/2, 16.4, P, 0.8)
    draw_wall(21.0, 17.2 - W, 0.5, W)                 # Inward hook left
    draw_wall(26.5, 17.2 - W, 0.5, W)                 # Inward hook right

    # Tòa A Interior Corridor Walls
    draw_wall(0.0, 11.9 - P/2, 21.0, P)               # North corridor line West
    draw_wall(27.0, 11.9 - P/2, 13.0, P)              # North corridor line East
    draw_wall(0.0, 10.1 - P/2, 21.0, P)               # South corridor line West
    draw_wall(27.0, 10.1 - P/2, 13.0, P)              # South corridor line East
    draw_wall(40.0 - P/2, 6.1, P, 10.3)               # West wall of Phòng xét xử (separating from corridor & rooms)

    # Tòa A Vertical Partition Walls
    draw_wall(7.5 - P/2, 11.9, P, 4.5)                # TA_N1 / TA_N2
    draw_wall(14.0 - P/2, 11.9, P, 4.5)               # TA_N2 / TA_N3
    draw_wall(21.0 - P/2, 11.9, P, 4.5)               # TA_N3 / Cầu thang
    draw_wall(27.0 - P/2, 11.9, P, 4.5)               # Cầu thang / TA_N4
    draw_wall(33.5 - P/2, 11.9, P, 4.5)               # TA_N4 / TA_N5

    draw_wall(7.0 - P/2, 6.1, P, 4.0)                 # TA_S1 / TA_S2
    draw_wall(14.0 - P/2, 6.1, P, 4.0)                # TA_S2 / TA_S3
    draw_wall(21.0 - P/2, 6.1, P, 4.0)                # TA_S3 / Sảnh
    draw_wall(27.0 - P/2, 6.1, P, 4.0)                # Sảnh / TA_S4
    draw_wall(33.5 - P/2, 6.1, P, 4.0)                # TA_S4 / TA_S5

    # === TÒA B EXTERIOR & INTERIOR WALLS ===
    draw_wall(-W, -19.0 - W, W, 22.0 + 2*W)           # West outer wall
    draw_wall(12.0, -19.0 - W, W, 22.0 + 2*W)         # East outer wall
    draw_wall(-W, 3.0, 5.0 + W, W)                    # North outer wall left
    draw_wall(7.0, 3.0, 5.0 + W, W)                   # North outer wall right
    draw_wall(-W, -19.0 - W, 12.0 + 2*W, W)           # South outer wall

    draw_wall(5.0 - P/2, -11.0, P, 14.0)              # Vertical corridor left wall
    draw_wall(7.0 - P/2, -4.0, P, 7.0)                # Vertical corridor right wall (upper)

    draw_wall(0.0, -4.0 - P/2, 5.0, P)                # Left divider TB_1 / TB_3
    draw_wall(7.0, -4.0 - P/2, 5.0, P)                # Right divider TB_2 / Sảnh chờ
    draw_wall(0.0, -11.0 - P/2, 12.0, P)              # Divider above Phòng Hành chính tư pháp

    # === TÒA XÉT XỬ EXTERIOR & INTERIOR WALLS ===
    draw_wall(36.0 - W, -19.0 - W, W, 22.0 + 2*W)     # West outer wall
    draw_wall(48.0, -19.0 - W, W, 22.0 + 2*W)         # East outer wall
    draw_wall(36.0 - W, 3.0, 12.0 + 2*W, W)           # North outer wall
    draw_wall(36.0 - W, -19.0 - W, 12.0 + 2*W, W)     # South outer wall
    draw_wall(36.0, -8.0 - P/2, 12.0, P)              # Central divider TX_1 / TX_2

    # ---------------------------------------------------------
    # 7. DRAW WINDOWS (PARALLEL LINES CUTOUTS)
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

    # Tòa A Windows
    draw_window(2.0, 16.4, 3.5, W, is_horizontal=True)
    draw_window(9.0, 16.4, 3.5, W, is_horizontal=True)
    draw_window(15.5, 16.4, 3.5, W, is_horizontal=True)
    draw_window(28.5, 16.4, 3.5, W, is_horizontal=True)
    draw_window(35.0, 16.4, 3.5, W, is_horizontal=True)
    draw_window(42.0, 16.4, 4.0, W, is_horizontal=True)   # Phòng xét xử North window
    draw_window(48.0, 9.0, W, 4.5, is_horizontal=False)   # Phòng xét xử East window
    draw_window(42.0, 6.1 - W, 4.0, W, is_horizontal=True)# Phòng xét xử South window

    draw_window(2.0, 6.1 - W, 3.0, W, is_horizontal=True)
    draw_window(9.0, 6.1 - W, 3.0, W, is_horizontal=True)
    draw_window(16.0, 6.1 - W, 3.0, W, is_horizontal=True)
    draw_window(28.5, 6.1 - W, 3.0, W, is_horizontal=True)
    draw_window(35.0, 6.1 - W, 3.0, W, is_horizontal=True)

    # Tòa B Windows
    draw_window(1.2, 3.0, 2.5, W, is_horizontal=True)                 # TB_1 North
    draw_window(8.2, 3.0, 2.5, W, is_horizontal=True)                 # TB_2 North
    draw_window(-W, -1.5, W, 2.5, is_horizontal=False)                # TB_1 West
    draw_window(12.0, -1.5, W, 2.5, is_horizontal=False)              # TB_2 East
    draw_window(-W, -8.5, W, 2.5, is_horizontal=False)                # TB_3 West
    draw_window(12.0, -8.5, W, 2.5, is_horizontal=False)              # Sảnh chờ East
    draw_window(-W, -16.0, W, 3.0, is_horizontal=False)               # TB_4 West
    draw_window(12.0, -16.0, W, 3.0, is_horizontal=False)             # TB_4 East
    draw_window(4.5, -19.0 - W, 3.0, W, is_horizontal=True)           # TB_4 South

    # Tòa Xét Xử Windows
    draw_window(39.5, 3.0, 5.0, W, is_horizontal=True)                # TX_1 North
    draw_window(48.0, -3.5, W, 4.0, is_horizontal=False)              # TX_1 East
    draw_window(48.0, -14.5, W, 4.0, is_horizontal=False)             # TX_2 East
    draw_window(39.5, -19.0 - W, 5.0, W, is_horizontal=True)          # TX_2 South

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode in ['ROOM_LEFT_IN']:
            ax.add_patch(patches.Rectangle((x - 0.15, y - size - 0.05), 0.30, size + 0.10, facecolor='#ffffff', edgecolor='none', zorder=13))
            ax.plot([x, x - size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode in ['ROOM_RIGHT_IN']:
            ax.add_patch(patches.Rectangle((x - 0.15, y - size - 0.05), 0.30, size + 0.10, facecolor='#ffffff', edgecolor='none', zorder=13))
            ax.plot([x, x + size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'N_IN_RIGHT':
            ax.add_patch(patches.Rectangle((x - 0.05, y - 0.15), size + 0.10, 0.30, facecolor='#ffffff', edgecolor='none', zorder=13))
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_RIGHT':
            ax.add_patch(patches.Rectangle((x - 0.05, y - 0.15), size + 0.10, 0.30, facecolor='#ffffff', edgecolor='none', zorder=13))
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'DOUBLE_EAST_IN':
            # Double door on West wall of courtroom, opening East into room
            leaf = size / 2.0
            ax.add_patch(patches.Rectangle((x - 0.15, y - leaf - 0.05), 0.30, size + 0.10, facecolor='#ffffff', edgecolor='none', zorder=13))
            # Upper leaf: hinge at (x, y + leaf), opens down-in
            ax.plot([x, x + leaf], [y + leaf, y + leaf], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc1 = patches.Arc((x, y + leaf), leaf*2, leaf*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc1)
            # Lower leaf: hinge at (x, y - leaf), opens up-in
            ax.plot([x, x + leaf], [y - leaf, y - leaf], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc2 = patches.Arc((x, y - leaf), leaf*2, leaf*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc2)

    # Draw Doors for all Rooms
    for r in rooms:
        if r['door'] is not None:
            dx, dy, dsize, dmode = r['door']
            draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 9. ROOM TEXT LABELS
    # ---------------------------------------------------------
    for r in rooms:
        if r['name']:
            cx, cy = r['text_center']
            font_sz = r.get('font_size', 8.5)
            ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Adjust Canvas Bounds
    ax.set_xlim(-3.0, 51.0)
    ax.set_ylim(-24.5, 20.5)

    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "mat_bang_tang_1.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 1 đã được xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang1()
