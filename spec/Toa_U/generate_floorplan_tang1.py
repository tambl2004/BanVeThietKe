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

def create_floorplan_tang1_bacninh9():
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

    # Positioning Offsets per User Instruction
    DY_A = 11.0   # Tòa A & Tòa Xét xử (+11.0m)
    DY_BC = 1.0   # Tòa B & Tòa C (+1.0m)
    DX_B = 18.0   # Tòa B shifted right (+18.0m)
    DX_C = -18.0  # Tòa C shifted left (-18.0m)

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND (CENTERED LEGEND AT BOTTOM)
    # ---------------------------------------------------------
    fig.text(0.03, 0.96, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 9 - Bắc Ninh',
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

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILLS
    # ---------------------------------------------------------
    # === TÒA A CORRIDORS (ẢNH 1) ===
    ax.add_patch(patches.Rectangle((0.0, -0.9 + DY_A), 30.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.add_patch(patches.Rectangle((12.0, -4.9 + DY_A), 6.0, 10.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.add_patch(patches.Rectangle((30.0, -0.9 + DY_A), 2.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === TÒA B CORRIDOR (PUNCH THROUGH NORTH & SOUTH) ===
    ax.add_patch(patches.Rectangle((-13.0 + DX_B, -20.0 + DY_BC), 2.0, 22.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === TÒA C CORRIDOR (PUNCH THROUGH NORTH & SOUTH) ===
    ax.add_patch(patches.Rectangle((59.0 + DX_C, -20.0 + DY_BC), 2.0, 22.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS & BACKGROUND FILLS
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA A (7 PHÒNG - THEO ẢNH 1) ===
        {'id': 'TA_N1', 'name': 'Phòng thẩm phán\nNguyễn Đức Hãnh', 'x': 0.0, 'y': 0.9 + DY_A, 'w': 6.0, 'h': 4.5, 'text_center': (3.0, 3.15 + DY_A), 'door': (4.2, 0.9 + DY_A, 0.8, 'N_IN_RIGHT'), 'font_size': 8.5},
        {'id': 'TA_N2', 'name': 'Phòng thẩm phán\nNguyễn Văn Tuyến', 'x': 6.0, 'y': 0.9 + DY_A, 'w': 6.0, 'h': 4.5, 'text_center': (9.0, 3.15 + DY_A), 'door': (10.2, 0.9 + DY_A, 0.8, 'N_IN_RIGHT'), 'font_size': 8.5},
        {'id': 'TA_N3', 'name': 'Phòng phó chánh án\nNguyễn Sỹ Cây', 'x': 18.0, 'y': 0.9 + DY_A, 'w': 6.0, 'h': 4.5, 'text_center': (21.0, 3.15 + DY_A), 'door': (19.2, 0.9 + DY_A, 0.8, 'N_IN_RIGHT'), 'font_size': 8.5},
        {'id': 'TA_N4', 'name': 'Phòng thư ký\nĐỗ Duy Khải', 'x': 24.0, 'y': 0.9 + DY_A, 'w': 6.0, 'h': 4.5, 'text_center': (27.0, 3.15 + DY_A), 'door': (25.2, 0.9 + DY_A, 0.8, 'N_IN_RIGHT'), 'font_size': 8.5},

        {'id': 'TA_S1', 'name': 'Văn phòng', 'x': 0.0, 'y': -4.9 + DY_A, 'w': 12.0, 'h': 4.0, 'text_center': (6.0, -2.9 + DY_A), 'door': (10.2, -0.9 + DY_A, 0.8, 'S_IN_RIGHT'), 'font_size': 9.0},
        {'id': 'TA_S2', 'name': 'Phòng Chánh VP\nNguyễn Thị Quế', 'x': 18.0, 'y': -4.9 + DY_A, 'w': 6.0, 'h': 4.0, 'text_center': (21.0, -2.9 + DY_A), 'door': (19.2, -0.9 + DY_A, 0.8, 'S_IN_RIGHT'), 'font_size': 7.5},
        {'id': 'TA_S3', 'name': 'Phòng phó Chánh VP\nNguyễn Thanh Thuý', 'x': 24.0, 'y': -4.9 + DY_A, 'w': 6.0, 'h': 4.0, 'text_center': (27.0, -2.9 + DY_A), 'door': (25.2, -0.9 + DY_A, 0.8, 'S_IN_RIGHT'), 'font_size': 7.5},

        # === TÒA XÉT XỬ ===
        {'id': 'TX_1', 'name': 'Phòng xét xử', 'x': 32.0, 'y': -4.9 + DY_A, 'w': 16.0, 'h': 10.3, 'text_center': (40.0, 0.25 + DY_A), 'door': None, 'font_size': 11.5},

        # === TÒA B (KHỐI DỌC - 4 DÃY PHÒNG ĐỐI XỨNG CÂN BẰNG) ===
        # Row 1 (Y: -3.5 to 2.0)
        {'id': 'TB_1', 'name': 'Hội trường xét xử', 'x': -18.0 + DX_B, 'y': -3.5 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (-15.5 + DX_B, -0.75 + DY_BC), 'door': (-13.0 + DX_B, 1.4 + DY_BC, 0.8, 'ROOM_LEFT_IN'), 'font_size': 8.5},
        {'id': 'TB_5', 'name': 'Phòng tiếp dân', 'x': -11.0 + DX_B, 'y': -3.5 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (-8.5 + DX_B, -0.75 + DY_BC), 'door': (-11.0 + DX_B, 1.4 + DY_BC, 0.8, 'ROOM_RIGHT_IN'), 'font_size': 8.5},

        # Row 2 (Y: -9.0 to -3.5)
        {'id': 'TB_2', 'name': 'Phòng phó Chánh án\nTrần Ngọc Anh', 'x': -18.0 + DX_B, 'y': -9.0 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (-15.5 + DX_B, -6.25 + DY_BC), 'door': (-13.0 + DX_B, -4.1 + DY_BC, 0.8, 'ROOM_LEFT_IN'), 'font_size': 8.0},

        # Row 3 (Y: -14.5 to -9.0)
        {'id': 'TB_3', 'name': 'Phòng thẩm phán\nLê Thị Lan Hương', 'x': -18.0 + DX_B, 'y': -14.5 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (-15.5 + DX_B, -11.75 + DY_BC), 'door': (-13.0 + DX_B, -9.6 + DY_BC, 0.8, 'ROOM_LEFT_IN'), 'font_size': 8.0},
        {'id': 'TB_6', 'name': 'Phòng lưu trữ hồ sơ', 'x': -11.0 + DX_B, 'y': -14.5 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (-8.5 + DX_B, -11.75 + DY_BC), 'door': (-11.0 + DX_B, -9.6 + DY_BC, 0.8, 'ROOM_RIGHT_IN'), 'font_size': 8.0},

        # Row 4 (Y: -20.0 to -14.5)
        {'id': 'TB_4', 'name': 'Phòng thư ký', 'x': -18.0 + DX_B, 'y': -20.0 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (-15.5 + DX_B, -17.25 + DY_BC), 'door': (-13.0 + DX_B, -15.1 + DY_BC, 0.8, 'ROOM_LEFT_IN'), 'font_size': 8.5},
        {'id': 'TB_7', 'name': 'Phòng trực / Bảo vệ', 'x': -11.0 + DX_B, 'y': -20.0 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (-8.5 + DX_B, -17.25 + DY_BC), 'door': (-11.0 + DX_B, -15.1 + DY_BC, 0.8, 'ROOM_RIGHT_IN'), 'font_size': 8.0},

        # === TÒA C (KHỐI DỌC - 4 DÃY PHÒNG ĐỐI XỨNG CÂN BẰNG) ===
        # Row 1 (Y: -3.5 to 2.0)
        {'id': 'TC_1', 'name': 'Phòng thẩm tra viên\nBùi Văn Tuyên', 'x': 54.0 + DX_C, 'y': -3.5 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (56.5 + DX_C, -0.75 + DY_BC), 'door': (59.0 + DX_C, 1.4 + DY_BC, 0.8, 'ROOM_LEFT_IN'), 'font_size': 8.0},
        {'id': 'TC_5', 'name': 'Phòng tạp vụ\nVũ Thị Hoè', 'x': 61.0 + DX_C, 'y': -3.5 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (63.5 + DX_C, -0.75 + DY_BC), 'door': (61.0 + DX_C, 1.4 + DY_BC, 0.8, 'ROOM_RIGHT_IN'), 'font_size': 8.0},

        # Row 2 (Y: -9.0 to -3.5)
        {'id': 'TC_2', 'name': 'Phòng thẩm tra viên\nNguyễn Thế Cường', 'x': 54.0 + DX_C, 'y': -9.0 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (56.5 + DX_C, -6.25 + DY_BC), 'door': (59.0 + DX_C, -4.1 + DY_BC, 0.8, 'ROOM_LEFT_IN'), 'font_size': 8.0},
        {'id': 'TC_6', 'name': 'Phòng thư ký', 'x': 61.0 + DX_C, 'y': -9.0 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (63.5 + DX_C, -6.25 + DY_BC), 'door': (61.0 + DX_C, -4.1 + DY_BC, 0.8, 'ROOM_RIGHT_IN'), 'font_size': 8.5},

        # Row 3 (Y: -14.5 to -9.0)
        {'id': 'TC_3', 'name': 'Phòng lái xe\nTrần Văn Phương', 'x': 54.0 + DX_C, 'y': -14.5 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (56.5 + DX_C, -11.75 + DY_BC), 'door': (59.0 + DX_C, -9.6 + DY_BC, 0.8, 'ROOM_LEFT_IN'), 'font_size': 8.0},
        {'id': 'TC_7', 'name': 'Phòng hoà giải', 'x': 61.0 + DX_C, 'y': -14.5 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (63.5 + DX_C, -11.75 + DY_BC), 'door': (61.0 + DX_C, -9.6 + DY_BC, 0.8, 'ROOM_RIGHT_IN'), 'font_size': 8.5},

        # Row 4 (Y: -20.0 to -14.5)
        {'id': 'TC_4', 'name': 'Phòng bảo vệ', 'x': 54.0 + DX_C, 'y': -20.0 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (56.5 + DX_C, -17.25 + DY_BC), 'door': (59.0 + DX_C, -15.1 + DY_BC, 0.8, 'ROOM_LEFT_IN'), 'font_size': 8.5},
        {'id': 'TC_8', 'name': 'Phòng lưu trữ', 'x': 61.0 + DX_C, 'y': -20.0 + DY_BC, 'w': 5.0, 'h': 5.5, 'text_center': (63.5 + DX_C, -17.25 + DY_BC), 'door': (61.0 + DX_C, -15.1 + DY_BC, 0.8, 'ROOM_RIGHT_IN'), 'font_size': 8.5},
    ]

    # Draw Room Background Fills
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES & ENTRANCE/EXIT STEPS
    # ---------------------------------------------------------
    # === TÒA A STAIRCASES & STEPS (ẢNH 1) ===
    stair_a_x, stair_a_y, stair_a_w, stair_a_h = 13.5, 0.9 + DY_A, 3.0, 3.5
    stair_a_bg = patches.Rectangle((stair_a_x, stair_a_y), stair_a_w, stair_a_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_a_bg)

    for i in range(10):
        sy = stair_a_y + i * (stair_a_h / 9.0)
        ax.plot([stair_a_x, stair_a_x + stair_a_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
    ax.plot([stair_a_x + stair_a_w / 2.0, stair_a_x + stair_a_w / 2.0], [stair_a_y, stair_a_y + stair_a_h * (8.0/9.0)], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair_a_x + stair_a_w / 2.0, stair_a_y - 0.35, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=8.5, ha='center', va='top', zorder=5)

    # Front Main Entrance Steps at Tòa A (South: Y = -4.9 + DY_A to -5.7 + DY_A)
    for sy in np.linspace(-4.9 + DY_A, -5.7 + DY_A, 6):
        ax.plot([12.0, 18.0], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Rear Exit Steps at Tòa A (North: Y = 5.4 + DY_A to 6.2 + DY_A)
    for sy in np.linspace(5.4 + DY_A, 6.2 + DY_A, 6):
        ax.plot([12.0, 18.0], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # West End Steps at Tòa A Corridor (X = -0.8 to 0.0)
    for i in range(5):
        dx = -0.2 * (i + 1)
        ax.plot([dx, 0.0], [0.9 + DY_A, 0.9 + DY_A], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-0.9 + DY_A, -0.9 + DY_A], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-0.9 + DY_A, 0.9 + DY_A], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # === TÒA B STAIRCASE (COMPACT IN ROW 2 RIGHT) ===
    stair_b_x, stair_b_y, stair_b_w, stair_b_h = -11.0 + DX_B, -9.0 + DY_BC, 5.0, 5.5
    stair_b_bg = patches.Rectangle((stair_b_x, stair_b_y), stair_b_w, stair_b_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_b_bg)

    for i in range(10):
        sy = stair_b_y + i * (stair_b_h / 9.0)
        ax.plot([stair_b_x, stair_b_x + stair_b_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
    ax.plot([stair_b_x + stair_b_w / 2.0, stair_b_x + stair_b_w / 2.0], [stair_b_y, stair_b_y + stair_b_h * (8.0/9.0)], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair_b_x + stair_b_w / 2.0, stair_b_y + stair_b_h / 2.0, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=5)

    # === TÒA XÉT XỬ SOUTH EXIT STEPS (BẬC THANG RA BÊN NGOÀI - KHOANH ĐỎ) ===
    ax.add_patch(patches.Rectangle((38.0 - 0.05, -4.9 + DY_A - 0.25), 4.10, 0.50, facecolor='#ffffff', edgecolor='none', zorder=13))
    for sy in np.linspace(-4.9 + DY_A, -5.7 + DY_A, 5):
        ax.plot([38.0, 42.0], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # === TÒA B ENTRANCE/EXIT STEPS (TOP & BOTTOM OF CORRIDOR) ===
    for sy in np.linspace(2.0 + W + DY_BC, 2.8 + W + DY_BC, 5):
        ax.plot([-13.0 + DX_B, -11.0 + DX_B], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    for sy in np.linspace(-20.0 - W + DY_BC, -20.8 - W + DY_BC, 5):
        ax.plot([-13.0 + DX_B, -11.0 + DX_B], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # === TÒA C ENTRANCE/EXIT STEPS (TOP & BOTTOM OF CORRIDOR) ===
    for sy in np.linspace(2.0 + W + DY_BC, 2.8 + W + DY_BC, 5):
        ax.plot([59.0 + DX_C, 61.0 + DX_C], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    for sy in np.linspace(-20.0 - W + DY_BC, -20.8 - W + DY_BC, 5):
        ax.plot([59.0 + DX_C, 61.0 + DX_C], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Labels for Lobbies and Corridors
    ax.text(15.0, -2.9 + DY_A, 'SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(6.0, 0.0 + DY_A, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(24.0, 0.0 + DY_A, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(-12.0 + DX_B, -8.5 + DY_BC, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', rotation=90, zorder=5)
    ax.text(60.0 + DX_C, -8.5 + DY_BC, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', rotation=90, zorder=5)

    ax.text(15.0, 6.7 + DY_A, 'TÒA A', fontsize=12.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(40.0, 6.7 + DY_A, 'TÒA XÉT XỬ', fontsize=12.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(-12.0 + DX_B, -22.2 + DY_BC, 'TÒA B', fontsize=11.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(60.0 + DX_C, -22.2 + DY_BC, 'TÒA C', fontsize=11.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')

    # ---------------------------------------------------------
    # 6. DRAW STRUCTURAL WALLS (SOLID FILLED PATTERNS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # === TÒA A EXTERIOR WALLS (ẢNH 1) ===
    draw_wall(-W, -4.9 - W + DY_A, W, 4.0 + W)               # West lower outer wall
    draw_wall(-W, 0.9 + DY_A, W, 4.5 + W)                    # West upper outer wall
    draw_wall(30.0, -4.9 - W + DY_A, W, 4.0 + W)              # East lower outer wall
    draw_wall(30.0, 0.9 + DY_A, W, 4.5 + W)                   # East upper outer wall
    draw_wall(-W, 5.4 + DY_A, 12.0 + W + PART_THICKNESS/2, W)  # North outer wall West
    draw_wall(18.0 - PART_THICKNESS/2, 5.4 + DY_A, 12.0 + W + PART_THICKNESS/2, W) # North outer wall East
    draw_wall(-W, -4.9 - W + DY_A, 12.0 + W + PART_THICKNESS/2, W) # South outer wall West
    draw_wall(18.0 - PART_THICKNESS/2, -4.9 - W + DY_A, 12.0 + W + PART_THICKNESS/2, W) # South outer wall East

    # South Front Entrance Side Walls
    draw_wall(12.0 - PART_THICKNESS/2, -5.7 + DY_A, PART_THICKNESS, 0.8)
    draw_wall(18.0 - PART_THICKNESS/2, -5.7 + DY_A, PART_THICKNESS, 0.8)

    # North Rear Exit Side Walls with Inward Hooks (Ảnh 1)
    draw_wall(12.0 - PART_THICKNESS/2, 5.4 + DY_A, PART_THICKNESS, 0.8)
    draw_wall(18.0 - PART_THICKNESS/2, 5.4 + DY_A, PART_THICKNESS, 0.8)
    draw_wall(12.0, 6.2 - W + DY_A, 0.5, W)                  # Inward hook left
    draw_wall(17.5, 6.2 - W + DY_A, 0.5, W)                  # Inward hook right

    # Tòa A Interior Corridor Walls
    draw_wall(0.0, 0.9 - PART_THICKNESS/2 + DY_A, 12.0, PART_THICKNESS)  # North corridor line West
    draw_wall(18.0, 0.9 - PART_THICKNESS/2 + DY_A, 12.0, PART_THICKNESS) # North corridor line East
    draw_wall(0.0, -0.9 - PART_THICKNESS/2 + DY_A, 12.0, PART_THICKNESS) # South corridor line West
    draw_wall(18.0, -0.9 - PART_THICKNESS/2 + DY_A, 12.0, PART_THICKNESS)# South corridor line East

    # Tòa A Vertical Partition Walls (Nối kín không bị mất tường quanh Sảnh & Cầu thang)
    draw_wall(6.0 - PART_THICKNESS/2, 0.9 + DY_A, PART_THICKNESS, 4.5)   # Divider between TA_N1 and TA_N2
    draw_wall(12.0 - PART_THICKNESS/2, 0.9 + DY_A, PART_THICKNESS, 4.5)  # Divider between TA_N2 and Cầu thang/Sảnh
    draw_wall(18.0 - PART_THICKNESS/2, 0.9 + DY_A, PART_THICKNESS, 4.5)  # Divider between Sảnh/Cầu thang and TA_N3
    draw_wall(24.0 - PART_THICKNESS/2, 0.9 + DY_A, PART_THICKNESS, 4.5)  # Divider between TA_N3 and TA_N4

    draw_wall(12.0 - PART_THICKNESS/2, -4.9 + DY_A, PART_THICKNESS, 4.0) # Divider between TA_S1 (Văn phòng) and Sảnh
    draw_wall(18.0 - PART_THICKNESS/2, -4.9 + DY_A, PART_THICKNESS, 4.0) # Divider between Sảnh and TA_S2
    draw_wall(24.0 - PART_THICKNESS/2, -4.9 + DY_A, PART_THICKNESS, 4.0) # Divider between TA_S2 and TA_S3

    # === CONNECTING PASSAGE BRIDGE (TÒA A -> TÒA XÉT XỬ) ===
    draw_wall(30.0, 0.9 - PART_THICKNESS/2 + DY_A, 2.0, PART_THICKNESS)
    draw_wall(30.0, -0.9 - PART_THICKNESS/2 + DY_A, 2.0, PART_THICKNESS)

    # === TÒA XÉT XỬ EXTERIOR WALLS ===
    draw_wall(32.0 - W, -4.9 - W + DY_A, W, 4.0 + W)
    draw_wall(32.0 - W, 0.9 + DY_A, W, 4.5 + W)
    draw_wall(48.0, -4.9 - W + DY_A, W, 10.3 + 2*W)
    draw_wall(32.0 - W, 5.4 + DY_A, 16.0 + 2*W, W)
    draw_wall(32.0 - W, -4.9 - W + DY_A, 16.0 + 2*W, W)

    # === TÒA B EXTERIOR & INTERIOR WALLS ===
    draw_wall(-18.0 - W + DX_B, -20.0 - W + DY_BC, W, 22.0 + 2*W)    # West outer wall
    draw_wall(-6.0 + DX_B, -20.0 - W + DY_BC, W, 22.0 + 2*W)         # East outer wall
    draw_wall(-18.0 - W + DX_B, 2.0 + DY_BC, 5.0 + W, W)             # Top outer wall left
    draw_wall(-11.0 + DX_B, 2.0 + DY_BC, 5.0 + W, W)                 # Top outer wall right
    draw_wall(-18.0 - W + DX_B, -20.0 - W + DY_BC, 5.0 + W, W)       # Bottom outer wall left
    draw_wall(-11.0 + DX_B, -20.0 - W + DY_BC, 5.0 + W, W)            # Bottom outer wall right

    draw_wall(-13.0 - PART_THICKNESS/2 + DX_B, -20.0 - W + DY_BC, PART_THICKNESS, 22.0 + 2*W)# Vertical corridor left wall
    draw_wall(-11.0 - PART_THICKNESS/2 + DX_B, -20.0 - W + DY_BC, PART_THICKNESS, 22.0 + 2*W)# Vertical corridor right wall

    draw_wall(-18.0 + DX_B, -3.5 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)  # Left divider Row 1/2
    draw_wall(-11.0 + DX_B, -3.5 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)  # Right divider Row 1/2
    draw_wall(-18.0 + DX_B, -9.0 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)  # Left divider Row 2/3
    draw_wall(-11.0 + DX_B, -9.0 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)  # Right divider Row 2/3 (Stair bottom)
    draw_wall(-18.0 + DX_B, -14.5 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS) # Left divider Row 3/4
    draw_wall(-11.0 + DX_B, -14.5 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS) # Right divider Row 3/4

    # === TÒA C EXTERIOR & INTERIOR WALLS ===
    draw_wall(54.0 - W + DX_C, -20.0 - W + DY_BC, W, 22.0 + 2*W)     # West outer wall
    draw_wall(66.0 + DX_C, -20.0 - W + DY_BC, W, 22.0 + 2*W)          # East outer wall
    draw_wall(54.0 - W + DX_C, 2.0 + DY_BC, 5.0 + W, W)              # Top outer wall left
    draw_wall(61.0 + DX_C, 2.0 + DY_BC, 5.0 + W, W)                  # Top outer wall right
    draw_wall(54.0 - W + DX_C, -20.0 - W + DY_BC, 5.0 + W, W)        # Bottom outer wall left
    draw_wall(61.0 + DX_C, -20.0 - W + DY_BC, 5.0 + W, W)            # Bottom outer wall right

    draw_wall(59.0 - PART_THICKNESS/2 + DX_C, -20.0 - W + DY_BC, PART_THICKNESS, 22.0 + 2*W) # Vertical corridor left wall
    draw_wall(61.0 - PART_THICKNESS/2 + DX_C, -20.0 - W + DY_BC, PART_THICKNESS, 22.0 + 2*W) # Vertical corridor right wall

    draw_wall(54.0 + DX_C, -3.5 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)   # Left divider Row 1/2
    draw_wall(61.0 + DX_C, -3.5 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)   # Right divider Row 1/2
    draw_wall(54.0 + DX_C, -9.0 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)   # Left divider Row 2/3
    draw_wall(61.0 + DX_C, -9.0 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)   # Right divider Row 2/3
    draw_wall(54.0 + DX_C, -14.5 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)  # Left divider Row 3/4
    draw_wall(61.0 + DX_C, -14.5 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)  # Right divider Row 3/4

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

    # Tòa A Windows (ẢNH 1)
    draw_window(1.5, 5.4 + DY_A, 3.0, W, is_horizontal=True)
    draw_window(7.5, 5.4 + DY_A, 3.0, W, is_horizontal=True)
    draw_window(19.5, 5.4 + DY_A, 3.0, W, is_horizontal=True)
    draw_window(25.5, 5.4 + DY_A, 3.0, W, is_horizontal=True)

    draw_window(3.0, -4.9 - W + DY_A, 6.0, W, is_horizontal=True)
    draw_window(20.0, -4.9 - W + DY_A, 8.0, W, is_horizontal=True)

    # Tòa Xét Xử Windows (CỬA SỔ TRÊN TƯỜNG BẮC VÀ ĐÔNG CỦA PHÒNG XÉT XỬ)
    draw_window(36.0, 5.4 + DY_A, 8.0, W, is_horizontal=True)        # North window
    draw_window(48.0, -2.5 + DY_A, W, 5.0, is_horizontal=False)     # East window

    # Tòa B Windows
    draw_window(-16.5 + DX_B, 2.0 + DY_BC, 2.5, W, is_horizontal=True)              # Top left window
    draw_window(-9.5 + DX_B, 2.0 + DY_BC, 2.5, W, is_horizontal=True)               # Top right window
    draw_window(-18.0 - W + DX_B, -0.75 + DY_BC, W, 2.5, is_horizontal=False)        # Row 1 West
    draw_window(-18.0 - W + DX_B, -6.25 + DY_BC, W, 2.5, is_horizontal=False)        # Row 2 West
    draw_window(-18.0 - W + DX_B, -11.75 + DY_BC, W, 2.5, is_horizontal=False)       # Row 3 West
    draw_window(-18.0 - W + DX_B, -17.25 + DY_BC, W, 2.5, is_horizontal=False)       # Row 4 West
    draw_window(-6.0 + DX_B, -0.75 + DY_BC, W, 2.5, is_horizontal=False)             # Row 1 East
    draw_window(-6.0 + DX_B, -6.25 + DY_BC, W, 2.5, is_horizontal=False)             # Row 2 East (Staircase)
    draw_window(-6.0 + DX_B, -11.75 + DY_BC, W, 2.5, is_horizontal=False)            # Row 3 East
    draw_window(-6.0 + DX_B, -17.25 + DY_BC, W, 2.5, is_horizontal=False)            # Row 4 East

    # Tòa C Windows
    draw_window(55.5 + DX_C, 2.0 + DY_BC, 2.5, W, is_horizontal=True)               # Top left window
    draw_window(62.5 + DX_C, 2.0 + DY_BC, 2.5, W, is_horizontal=True)               # Top right window
    draw_window(54.0 - W + DX_C, -0.75 + DY_BC, W, 2.5, is_horizontal=False)         # Row 1 West
    draw_window(54.0 - W + DX_C, -6.25 + DY_BC, W, 2.5, is_horizontal=False)         # Row 2 West
    draw_window(54.0 - W + DX_C, -11.75 + DY_BC, W, 2.5, is_horizontal=False)        # Row 3 West
    draw_window(54.0 - W + DX_C, -17.25 + DY_BC, W, 2.5, is_horizontal=False)        # Row 4 West
    draw_window(66.0 + DX_C, -0.75 + DY_BC, W, 2.5, is_horizontal=False)             # Row 1 East
    draw_window(66.0 + DX_C, -6.25 + DY_BC, W, 2.5, is_horizontal=False)             # Row 2 East
    draw_window(66.0 + DX_C, -11.75 + DY_BC, W, 2.5, is_horizontal=False)            # Row 3 East
    draw_window(66.0 + DX_C, -17.25 + DY_BC, W, 2.5, is_horizontal=False)            # Row 4 East

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS (CẮT TƯỜNG SẠCH SẼ & CỬA HOÀN CHỈNH)
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        # White cutout over wall to clear wall lines completely before drawing doors
        if mode in ['ROOM_LEFT_IN', 'ROOM_RIGHT_IN']:
            ax.add_patch(patches.Rectangle((x - 0.15, y - size - 0.05), 0.30, size + 0.10, facecolor='#ffffff', edgecolor='none', zorder=13))
        elif mode in ['N_IN_RIGHT', 'S_IN_RIGHT', 'CORRIDOR_TOP_DOOR']:
            ax.add_patch(patches.Rectangle((x - 0.05, y - 0.15), size + 0.10, 0.30, facecolor='#ffffff', edgecolor='none', zorder=13))
        elif mode == 'EXIT_EAST':
            ax.add_patch(patches.Rectangle((x - 0.15, y - 0.05), 0.30, size + 0.10, facecolor='#ffffff', edgecolor='none', zorder=13))
        elif mode == 'EXIT_SOUTH':
            ax.add_patch(patches.Rectangle((x - 0.05, y - 0.15), size + 0.10, 0.30, facecolor='#ffffff', edgecolor='none', zorder=13))

        # Draw Door Panel & Arc Swing
        if mode == 'N_IN_RIGHT':
            # Door on horizontal wall (Y=y), opens UP (+Y) into North room. Hinge at (x, y).
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_RIGHT':
            # Door on horizontal wall (Y=y), opens DOWN (-Y) into South room. Hinge at (x, y).
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'ROOM_LEFT_IN':
            # Door on vertical wall (X=x), opens WEST (-X) into Left Room. Hinge at (x, y).
            ax.plot([x, x - size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'ROOM_RIGHT_IN':
            # Door on vertical wall (X=x), opens EAST (+X) into Right Room. Hinge at (x, y).
            ax.plot([x, x + size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'CORRIDOR_TOP_DOOR':
            # Wide/Double door opening from top of vertical corridor into top room
            leaf = size / 2.0
            # Left leaf hinged at (x, y), opens UP (+Y)
            ax.plot([x, x], [y, y + leaf], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc1 = patches.Arc((x, y), leaf*2, leaf*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc1)
            # Right leaf hinged at (rx, y), opens UP (+Y)
            rx = x + size
            ax.plot([rx, rx], [y, y + leaf], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc2 = patches.Arc((rx, y), leaf*2, leaf*2, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
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
    print(f"Bản vẽ đã được xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang1_bacninh9()
