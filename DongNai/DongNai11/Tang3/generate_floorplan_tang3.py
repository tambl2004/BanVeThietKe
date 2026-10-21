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

def create_floorplan_tang3():
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
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND (CENTERED LEGEND AT BOTTOM)
    # ---------------------------------------------------------
    fig.text(0.03, 0.96, f'MẶT BẰNG TẦNG 3  —  {COURT_NAME}',
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

    ax.plot([lg_x + 22.0, lg_x + 22.0], [lg_y + 0.05, lg_y + 0.45], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=1)
    arc_lg = patches.Arc((lg_x + 22.0, lg_y + 0.05), 0.8, 0.8, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.1)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 23.1, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.add_patch(patches.Rectangle((lg_x + 30.0, lg_y), 1.0, 0.4, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=0.8, linestyle='--', zorder=1))
    ax.text(lg_x + 31.4, lg_y + 0.05, 'Mái che', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR BACKGROUND FILLS
    # ---------------------------------------------------------
    # Tòa A Horizontal Corridor (closed ends): X: 0.0 to 48.0, Y: 10.1 to 11.9
    ax.add_patch(patches.Rectangle((0.0, 10.1), 48.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS & BACKGROUND FILLS
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === DÃY BẮC TÒA A (Y: 11.9 to 16.4) ===
        # West Wing: Phòng Phó Chánh án Đào Hùng Dũng (KT mở rộng sang trọng phủ kín cánh Tây)
        {
            'id': 'T3_PCA', 'name': 'Phòng Phó Chánh án\nĐào Hùng Dũng',
            'x': 0.0, 'y': 11.9, 'w': 21.0, 'h': 4.5,
            'text_center': (10.5, 14.15),
            'door': (18.5, 11.9, 0.90, 'N_IN_RIGHT'),
            'font_size': 11.0
        },

        # East Wing: 2 Phòng Thẩm phán
        {
            'id': 'T3_TP_TRUONG', 'name': 'Phòng Thẩm phán\nĐỗ Tấn Trường',
            'x': 27.0, 'y': 11.9, 'w': 10.5, 'h': 4.5,
            'text_center': (32.25, 14.15),
            'door': (28.5, 11.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T3_TP_HOA', 'name': 'Phòng Thẩm phán\nMai Danh Hòa',
            'x': 37.5, 'y': 11.9, 'w': 10.5, 'h': 4.5,
            'text_center': (42.75, 14.15),
            'door': (39.0, 11.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.5
        },

        # === DÃY NAM TÒA A (Y: 6.1 to 10.1) ===
        # Hội trường lớn phía Tây
        {
            'id': 'T3_HOITRUONG', 'name': 'Hội trường',
            'x': 0.0, 'y': 6.1, 'w': 21.0, 'h': 4.0,
            'text_center': (10.5, 8.1),
            'door': (18.5, 10.1, 0.90, 'S_IN_RIGHT'),
            'font_size': 11.0
        },

        # Phòng sinh hoạt chung trung tâm (khu vực sảnh cũ)
        {
            'id': 'T3_SHC', 'name': 'Phòng sinh hoạt chung',
            'x': 21.0, 'y': 6.1, 'w': 6.0, 'h': 4.0,
            'text_center': (24.0, 8.1),
            'door': (22.5, 10.1, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.5
        },

        # Phòng họp lớn phía Đông
        {
            'id': 'T3_PHONGHOP', 'name': 'Phòng họp',
            'x': 27.0, 'y': 6.1, 'w': 21.0, 'h': 4.0,
            'text_center': (37.5, 8.1),
            'door': (28.5, 10.1, 0.90, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
    ]

    # Draw Room Background Fills
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES & ROOF AREAS (MÁI CHE TÒA B & TÒA XÉT XỬ)
    # ---------------------------------------------------------
    # === TÒA A STAIRCASES (WHITE BACKGROUND FOR TẦNG 3) ===
    stair_a_x, stair_a_y, stair_a_w, stair_a_h = 22.5, 11.9, 3.0, 3.5
    stair_a_bg = patches.Rectangle((stair_a_x, stair_a_y), stair_a_w, stair_a_h, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_a_bg)

    for i in range(10):
        sy = stair_a_y + i * (stair_a_h / 9.0)
        ax.plot([stair_a_x, stair_a_x + stair_a_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
    ax.plot([stair_a_x + stair_a_w / 2.0, stair_a_x + stair_a_w / 2.0], [stair_a_y, stair_a_y + stair_a_h * (8.0/9.0)], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair_a_x + stair_a_w / 2.0, stair_a_y - 0.35, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=8.5, ha='center', va='top', zorder=5)

    # === TÒA B ROOF (MÁI CHE) ===
    tb_roof = patches.Rectangle((0.0, -19.0), 12.0, 22.0, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=1.5, zorder=2)
    ax.add_patch(tb_roof)
    ax.plot([0.0, 6.0], [-19.0, -8.0], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([12.0, 6.0], [-19.0, -8.0], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([0.0, 6.0], [3.0, -8.0], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([12.0, 6.0], [3.0, -8.0], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.text(6.0, -8.0, 'MÁI CHE', color=COLOR_TEXT_MUTED, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # === TÒA XÉT XỬ ROOF (MÁI CHE) ===
    tx_roof = patches.Rectangle((36.0, -19.0), 12.0, 22.0, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=1.5, zorder=2)
    ax.add_patch(tx_roof)
    ax.plot([36.0, 42.0], [-19.0, -8.0], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([48.0, 42.0], [-19.0, -8.0], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([36.0, 42.0], [3.0, -8.0], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.plot([48.0, 42.0], [3.0, -8.0], color='#cbd5e1', linestyle='--', linewidth=1.0, zorder=3)
    ax.text(42.0, -8.0, 'MÁI CHE', color=COLOR_TEXT_MUTED, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # Labels for Corridors
    ax.text(10.5, 11.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(37.5, 11.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)

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

    # === TÒA A EXTERIOR WALLS (FULLY ENCLOSED WITH END WALLS) ===
    draw_wall(-W, 6.1 - W, W, 10.3 + 2*W)             # West outer wall (closed)
    draw_wall(48.0, 6.1 - W, W, 10.3 + 2*W)           # East outer wall (closed)
    draw_wall(-W, 16.4, 48.0 + 2*W, W)                # North outer wall (flat, closed)
    draw_wall(-W, 6.1 - W, 48.0 + 2*W, W)             # South outer wall (flat, closed)

    # Tòa A Interior Corridor Walls
    draw_wall(0.0, 11.9 - P/2, 21.0, P)               # North corridor line West
    draw_wall(27.0, 11.9 - P/2, 21.0, P)              # North corridor line East
    draw_wall(0.0, 10.1 - P/2, 48.0, P)               # South corridor line full length

    # Tòa A Vertical Partition Walls
    draw_wall(21.0 - P/2, 11.9, P, 4.5)               # T3_PCA / Cầu thang
    draw_wall(27.0 - P/2, 11.9, P, 4.5)               # Cầu thang / T3_TP_TRUONG
    draw_wall(37.5 - P/2, 11.9, P, 4.5)               # T3_TP_TRUONG / T3_TP_HOA

    draw_wall(21.0 - P/2, 6.1, P, 4.0)                # T3_HOITRUONG / T3_SHC
    draw_wall(27.0 - P/2, 6.1, P, 4.0)                # T3_SHC / T3_PHONGHOP

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
    draw_window(4.0, 16.4, 5.0, W, is_horizontal=True)
    draw_window(12.0, 16.4, 5.0, W, is_horizontal=True)
    draw_window(22.5, 16.4, 3.0, W, is_horizontal=True)  # Stair window at North
    draw_window(30.0, 16.4, 4.5, W, is_horizontal=True)
    draw_window(40.5, 16.4, 4.5, W, is_horizontal=True)

    draw_window(4.0, 6.1 - W, 5.0, W, is_horizontal=True)
    draw_window(12.0, 6.1 - W, 5.0, W, is_horizontal=True)
    draw_window(22.5, 6.1 - W, 3.0, W, is_horizontal=True)
    draw_window(30.0, 6.1 - W, 5.0, W, is_horizontal=True)
    draw_window(38.0, 6.1 - W, 5.0, W, is_horizontal=True)

    # Tòa A End Corridor Windows (East & West)
    draw_window(-W, 10.55, W, 0.9, is_horizontal=False)
    draw_window(48.0, 10.55, W, 0.9, is_horizontal=False)

    # End Room Windows (East & West Outer Walls)
    draw_window(-W, 13.5, W, 2.0, is_horizontal=False)
    draw_window(-W, 7.5, W, 2.0, is_horizontal=False)
    draw_window(48.0, 13.5, W, 2.0, is_horizontal=False)
    draw_window(48.0, 7.5, W, 2.0, is_horizontal=False)

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode == 'N_IN_RIGHT':
            ax.add_patch(patches.Rectangle((x - 0.05, y - 0.15), size + 0.10, 0.30, facecolor='#ffffff', edgecolor='none', zorder=13))
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_RIGHT':
            ax.add_patch(patches.Rectangle((x - 0.05, y - 0.15), size + 0.10, 0.30, facecolor='#ffffff', edgecolor='none', zorder=13))
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
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
    output_path = os.path.join(output_dir, "mat_bang_tang_3.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 3 đã được xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang3()
