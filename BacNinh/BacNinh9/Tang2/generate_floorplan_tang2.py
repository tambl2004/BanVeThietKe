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

def create_floorplan_tang2_bacninh9():
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
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_ROOF_FILL = '#f1f5f9'     # Light slate-grey for roof areas
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
    fig.text(0.03, 0.96, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 9 - Bắc Ninh',
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.03, 0.97], [0.94, 0.94], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box Centered at Bottom
    lg_x, lg_y = 9.0, -23.5
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.0, 0.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.4, lg_y + 0.05, 'Hành lang', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.add_patch(patches.Rectangle((lg_x + 7.5, lg_y + 0.12), 1.0, 0.16, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 8.9, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 15.0, lg_x + 16.2], [lg_y + 0.25, lg_y + 0.25], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 15.0, lg_x + 16.2], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 16.6, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.add_patch(patches.Rectangle((lg_x + 22.5, lg_y), 1.0, 0.4, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=0.8, linestyle='--', zorder=1))
    ax.text(lg_x + 23.9, lg_y + 0.05, 'Mái che', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILLS
    # ---------------------------------------------------------
    # === TÒA A CORRIDORS & HALL ===
    ax.add_patch(patches.Rectangle((0.0, -0.9 + DY_A), 30.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === TÒA B CORRIDOR ===
    ax.add_patch(patches.Rectangle((-18.0 + DX_B, -13.0 + DY_BC), 12.0, 15.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (CỬA NÂNG CAO TRÁNH ĐÈ LÊN TÊN PHÒNG)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA A (5 PHÒNG MỞ RỘNG TO LÊN TOÀN BỘ TÒA A) ===
        # North Row (Phòng Chánh án & Phòng Phó Chánh án mở rộng 12.0m x 4.5m)
        {'id': 'TA_N1', 'name': 'Phòng Chánh án\nHoàng Tuấn Anh', 'x': 0.0, 'y': 0.9 + DY_A, 'w': 12.0, 'h': 4.5, 'text_center': (6.0, 3.15 + DY_A), 'door': (10.2, 0.9 + DY_A, 0.8, 'N_IN_RIGHT'), 'font_size': 9.5},
        {'id': 'TA_N2', 'name': 'Phòng phó Chánh án\nPhạm Văn Phong', 'x': 18.0, 'y': 0.9 + DY_A, 'w': 12.0, 'h': 4.5, 'text_center': (24.0, 3.15 + DY_A), 'door': (19.2, 0.9 + DY_A, 0.8, 'N_IN_RIGHT'), 'font_size': 9.5},

        # South Row (3 Phòng phủ kín 30.0m chiều dài phía Nam Tòa A)
        {'id': 'TA_S1', 'name': 'Phòng kế toán\nNguyễn Thị Thuỳ Tiên', 'x': 0.0, 'y': -4.9 + DY_A, 'w': 9.0, 'h': 4.0, 'text_center': (4.5, -2.9 + DY_A), 'door': (7.2, -0.9 + DY_A, 0.8, 'S_IN_RIGHT'), 'font_size': 9.0},
        {'id': 'TA_S2', 'name': 'Phòng họp', 'x': 9.0, 'y': -4.9 + DY_A, 'w': 12.0, 'h': 4.0, 'text_center': (15.0, -2.9 + DY_A), 'door': (15.2, -0.9 + DY_A, 0.8, 'S_IN_RIGHT'), 'font_size': 10.5},
        {'id': 'TA_S3', 'name': 'Phòng thư ký\nNguyễn Chí Quân', 'x': 21.0, 'y': -4.9 + DY_A, 'w': 9.0, 'h': 4.0, 'text_center': (25.5, -2.9 + DY_A), 'door': (22.2, -0.9 + DY_A, 0.8, 'S_IN_RIGHT'), 'font_size': 9.0},

        # === TÒA B (VỊ TRÍ CỬA NÂNG CAO LÊN PHÍA TRÊN ĐỂ KHÔNG CHÈN TÊN PHÒNG, CHIỀU CAO 6.0M CHÍNH XÁC VỚI KHUNG TÒA) ===
        # Row 1 (Mở rộng 5.0m x 6.0m vừa khít chiều cao Tòa B, Cửa nâng cao ở Y = 1.2+DY_BC)
        {'id': 'TB_1', 'name': 'Phòng Phó Chánh án\nLương Minh Phương', 'x': -18.0 + DX_B, 'y': -4.0 + DY_BC, 'w': 5.0, 'h': 6.0, 'text_center': (-15.5 + DX_B, -1.0 + DY_BC), 'door': (-13.0 + DX_B, 1.2 + DY_BC, 0.8, 'ROOM_LEFT_IN'), 'font_size': 8.5},
        {'id': 'TB_2', 'name': 'Phòng thư ký\nNguyễn Tiến Phú', 'x': -11.0 + DX_B, 'y': -4.0 + DY_BC, 'w': 5.0, 'h': 6.0, 'text_center': (-8.5 + DX_B, -1.0 + DY_BC), 'door': (-11.0 + DX_B, 1.2 + DY_BC, 0.8, 'ROOM_RIGHT_IN'), 'font_size': 8.5},

        # Row 2 (Phòng Thẩm phán: 5.0m x 7.0m, Cửa nâng cao ở Y = -4.8+DY_BC)
        {'id': 'TB_3', 'name': 'Phòng thẩm phán\nVũ Thị Huyền', 'x': -18.0 + DX_B, 'y': -11.0 + DY_BC, 'w': 5.0, 'h': 7.0, 'text_center': (-15.5 + DX_B, -7.5 + DY_BC), 'door': (-13.0 + DX_B, -4.8 + DY_BC, 0.8, 'ROOM_LEFT_IN'), 'font_size': 8.5},

        # Bottom Large Room (Phòng Phó Chánh án Trần Xuân Suốt: 12.0m x 7.0m)
        {'id': 'TB_4', 'name': 'Phòng phó Chánh án\nTrần Xuân Suốt', 'x': -18.0 + DX_B, 'y': -20.0 + DY_BC, 'w': 12.0, 'h': 7.0, 'text_center': (-12.0 + DX_B, -16.5 + DY_BC), 'door': (-12.0 + DX_B, -13.0 + DY_BC, 1.0, 'S_IN_RIGHT'), 'font_size': 11.0},
    ]

    # Draw Room Background Fills
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES & ROOF AREAS (MÁI CHE TÒA XÉT XỬ & TÒA C)
    # ---------------------------------------------------------
    # === TÒA A STAIRCASES (TẦNG 2 WHITE FILL) ===
    stair_a_x, stair_a_y, stair_a_w, stair_a_h = 13.5, 0.9 + DY_A, 3.0, 3.5
    stair_a_bg = patches.Rectangle((stair_a_x, stair_a_y), stair_a_w, stair_a_h, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_a_bg)

    for i in range(10):
        sy = stair_a_y + i * (stair_a_h / 9.0)
        ax.plot([stair_a_x, stair_a_x + stair_a_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
    ax.plot([stair_a_x + stair_a_w / 2.0, stair_a_x + stair_a_w / 2.0], [stair_a_y, stair_a_y + stair_a_h * (8.0/9.0)], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair_a_x + stair_a_w / 2.0, stair_a_y - 0.35, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=8.5, ha='center', va='top', zorder=5)

    # === TÒA B STAIRCASE (X: -11.0+DX_B, Y: -11.0+DY_BC to -4.0+DY_BC) ===
    stair_b_x, stair_b_y, stair_b_w, stair_b_h = -11.0 + DX_B, -11.0 + DY_BC, 5.0, 7.0
    stair_b_bg = patches.Rectangle((stair_b_x, stair_b_y), stair_b_w, stair_b_h, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_b_bg)

    for i in range(10):
        sy = stair_b_y + i * (stair_b_h / 9.0)
        ax.plot([stair_b_x, stair_b_x + stair_b_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
    ax.plot([stair_b_x + stair_b_w / 2.0, stair_b_x + stair_b_w / 2.0], [stair_b_y, stair_b_y + stair_b_h * (8.0/9.0)], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair_b_x + stair_b_w / 2.0, stair_b_y + stair_b_h / 2.0, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=5)

    # === TÒA XÉT XỬ ROOF (MÁI CHE) ===
    tx_roof = patches.Rectangle((32.0, -4.9 + DY_A), 16.0, 10.3, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=1.5, zorder=2)
    ax.add_patch(tx_roof)
    ax.plot([32.0, 40.0], [-4.9 + DY_A, 0.25 + DY_A], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([48.0, 40.0], [-4.9 + DY_A, 0.25 + DY_A], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([32.0, 40.0], [5.4 + DY_A, 0.25 + DY_A], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([48.0, 40.0], [5.4 + DY_A, 0.25 + DY_A], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.text(40.0, 0.25 + DY_A, 'MÁI CHE', color=COLOR_TEXT_MUTED, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)

    # === TÒA C ROOF (MÁI CHE) ===
    tc_roof = patches.Rectangle((54.0 + DX_C, -20.0 + DY_BC), 12.0, 22.0, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=1.5, zorder=2)
    ax.add_patch(tc_roof)
    ax.plot([54.0 + DX_C, 60.0 + DX_C], [-20.0 + DY_BC, -9.0 + DY_BC], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([66.0 + DX_C, 60.0 + DX_C], [-20.0 + DY_BC, -9.0 + DY_BC], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([54.0 + DX_C, 60.0 + DX_C], [2.0 + DY_BC, -9.0 + DY_BC], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([66.0 + DX_C, 60.0 + DX_C], [2.0 + DY_BC, -9.0 + DY_BC], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.text(60.0 + DX_C, -9.0 + DY_BC, 'MÁI CHE', color=COLOR_TEXT_MUTED, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)

    # Corridor/Lobby Labels
    ax.text(6.0, 0.0 + DY_A, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(24.0, 0.0 + DY_A, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    
    # Tòa B Corridor Labels (Chính giữa hành lang dọc X = -12.0+DX_B)
    ax.text(-12.0 + DX_B, -1.0 + DY_BC, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', rotation=90, zorder=5)
    ax.text(-12.0 + DX_B, -12.0 + DY_BC, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=5)

    # Building Header Titles
    ax.text(15.0, 6.7 + DY_A, 'TÒA A', fontsize=12.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(40.0, 6.7 + DY_A, 'TÒA XÉT XỬ', fontsize=12.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(-12.0 + DX_B, -22.2 + DY_BC, 'TÒA B', fontsize=11.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(60.0 + DX_C, -22.2 + DY_BC, 'TÒA C', fontsize=11.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')

    # ---------------------------------------------------------
    # 6. DRAW STRUCTURAL WALLS (BỔ SUNG ĐẦY ĐỦ TƯỜNG HÀNH LANG TÒA B)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # === TÒA A EXTERIOR & INTERIOR WALLS ===
    draw_wall(-W, -4.9 - W + DY_A, W, 10.3 + 2*W)            # West outer wall
    draw_wall(30.0, -4.9 - W + DY_A, W, 10.3 + 2*W)           # East outer wall
    draw_wall(-W, 5.4 + DY_A, 30.0 + 2*W, W)                 # North outer wall
    draw_wall(-W, -4.9 - W + DY_A, 30.0 + 2*W, W)            # South outer wall

    # Tòa A Interior Corridor & Partition Walls
    draw_wall(0.0, 0.9 - PART_THICKNESS/2 + DY_A, 12.0, PART_THICKNESS)  # North corridor line West
    draw_wall(18.0, 0.9 - PART_THICKNESS/2 + DY_A, 12.0, PART_THICKNESS) # North corridor line East
    draw_wall(0.0, -0.9 - PART_THICKNESS/2 + DY_A, 30.0, PART_THICKNESS) # South corridor line

    draw_wall(12.0 - PART_THICKNESS/2, 0.9 + DY_A, PART_THICKNESS, 4.5)  # Divider TA_N1/Stair
    draw_wall(18.0 - PART_THICKNESS/2, 0.9 + DY_A, PART_THICKNESS, 4.5)  # Divider Stair/TA_N2

    draw_wall(9.0 - PART_THICKNESS/2, -4.9 + DY_A, PART_THICKNESS, 4.0)  # Divider TA_S1/Phòng họp
    draw_wall(21.0 - PART_THICKNESS/2, -4.9 + DY_A, PART_THICKNESS, 4.0) # Divider Phòng họp/TA_S3

    # === TÒA B EXTERIOR & INTERIOR WALLS (BỔ SUNG HOÀN CHỈNH TƯỜNG HÀNH LANG) ===
    draw_wall(-18.0 - W + DX_B, -20.0 - W + DY_BC, W, 22.0 + 2*W)     # West outer wall
    draw_wall(-6.0 + DX_B, -20.0 - W + DY_BC, W, 22.0 + 2*W)          # East outer wall
    draw_wall(-18.0 - W + DX_B, 2.0 + DY_BC, 12.0 + 2*W, W)          # North outer wall
    draw_wall(-18.0 - W + DX_B, -20.0 - W + DY_BC, 12.0 + 2*W, W)     # South outer wall

    # Tường hành lang dọc Tòa B (Chạy liên tục từ Y = -11.0+DY_BC đến Y = 2.0+DY_BC)
    draw_wall(-13.0 - PART_THICKNESS/2 + DX_B, -11.0 + DY_BC, PART_THICKNESS, 13.0) # West corridor wall
    draw_wall(-11.0 - PART_THICKNESS/2 + DX_B, -11.0 + DY_BC, PART_THICKNESS, 13.0) # East corridor wall

    # Tường vách ngang Tòa B
    draw_wall(-18.0 + DX_B, -4.0 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)  # South wall Row 1 West
    draw_wall(-11.0 + DX_B, -4.0 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS)  # South wall Row 1 East
    
    draw_wall(-18.0 + DX_B, -11.0 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS) # South wall Row 2 West
    draw_wall(-11.0 + DX_B, -11.0 - PART_THICKNESS/2 + DY_BC, 5.0, PART_THICKNESS) # South wall Cầu thang
    
    # Tường ngăn phía Bắc của Phòng Trần Xuân Suốt
    draw_wall(-18.0 + DX_B, -13.0 - PART_THICKNESS/2 + DY_BC, 12.0, PART_THICKNESS)

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

    # Tòa A Windows (North & South Outer Walls)
    draw_window(3.0, 5.4 + DY_A, 6.0, W, is_horizontal=True)
    draw_window(21.0, 5.4 + DY_A, 6.0, W, is_horizontal=True)

    draw_window(2.5, -4.9 - W + DY_A, 4.0, W, is_horizontal=True)
    draw_window(12.0, -4.9 - W + DY_A, 6.0, W, is_horizontal=True)
    draw_window(23.5, -4.9 - W + DY_A, 4.0, W, is_horizontal=True)

    # Tòa A End Corridor Windows (East & West)
    draw_window(-W, -0.45 + DY_A, W, 0.9, is_horizontal=False)
    draw_window(30.0, -0.45 + DY_A, W, 0.9, is_horizontal=False)

    # Tòa B Windows
    draw_window(-16.75 + DX_B, 2.0 + DY_BC, 2.5, W, is_horizontal=True)              # Top West room window
    draw_window(-12.5 + DX_B, 2.0 + DY_BC, 1.0, W, is_horizontal=True)               # Top corridor window
    draw_window(-9.75 + DX_B, 2.0 + DY_BC, 2.5, W, is_horizontal=True)               # Top East window

    draw_window(-18.0 - W + DX_B, -0.5 + DY_BC, W, 3.0, is_horizontal=False)        # Row 1 West side window
    draw_window(-18.0 - W + DX_B, -7.5 + DY_BC, W, 3.0, is_horizontal=False)        # Row 2 West side window
    draw_window(-6.0 + DX_B, -0.5 + DY_BC, W, 3.0, is_horizontal=False)             # Row 1 East side window
    draw_window(-6.0 + DX_B, -7.5 + DY_BC, W, 2.5, is_horizontal=False)             # Staircase window

    draw_window(-18.0 - W + DX_B, -12.5 + DY_BC, W, 1.2, is_horizontal=False)       # Gap West window
    draw_window(-6.0 + DX_B, -12.5 + DY_BC, W, 1.2, is_horizontal=False)            # Gap East window

    draw_window(-18.0 - W + DX_B, -17.5 + DY_BC, W, 3.0, is_horizontal=False)       # Bottom room West window
    draw_window(-6.0 + DX_B, -17.5 + DY_BC, W, 3.0, is_horizontal=False)            # Bottom room East window
    draw_window(-13.5 + DX_B, -20.0 - W + DY_BC, 3.0, W, is_horizontal=True)         # Bottom room South window

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS (CHÍNH XÁC KHÔNG LỆCH NÉT)
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode in ['ROOM_LEFT_IN', 'ROOM_RIGHT_IN']:
            ax.add_patch(patches.Rectangle((x - 0.15, y - size - 0.05), 0.30, size + 0.10, facecolor='#ffffff', edgecolor='none', zorder=13))
        elif mode in ['N_IN_RIGHT', 'S_IN_RIGHT']:
            ax.add_patch(patches.Rectangle((x - 0.05, y - 0.15), size + 0.10, 0.30, facecolor='#ffffff', edgecolor='none', zorder=13))

        if mode == 'N_IN_RIGHT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_RIGHT':
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'ROOM_LEFT_IN':
            ax.plot([x, x - size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'ROOM_RIGHT_IN':
            ax.plot([x, x + size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)

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
    output_path = os.path.join(output_dir, "mat_bang_tang_2.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 2 đã được xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang2_bacninh9()
