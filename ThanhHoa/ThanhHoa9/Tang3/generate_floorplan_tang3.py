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

def create_floorplan_tang3(court_name: str = COURT_NAME):
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
    COLOR_ROOF_FILL = '#f8fafc'     # Light grey-blue for roof (Mái che)
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#ffffff'    # Floor 3 stair fill is pure white per spec

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.02, 0.95, f'MẶT BẰNG TẦNG 3  —  {court_name}',
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.02, 0.98], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box Centered at Bottom (Includes Mái che)
    lg_x, lg_y = 12.0, -8.6
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

    ax.add_patch(patches.Rectangle((lg_x + 22.0, lg_y), 0.9, 0.35, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=1.0, linestyle='--', zorder=1))
    ax.text(lg_x + 23.2, lg_y + 0.05, 'Mái che', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Building Titles
    ax.text(4.0, 7.4, 'TÒA A1 (MÁI CHE KHỐI 2 TẦNG)', fontsize=11.5, fontweight='bold', color=COLOR_TEXT_MUTED, ha='center', va='center')
    ax.text(25.0, 5.3, 'TÒA A2 (KHỐI HÀNH CHÍNH TRUNG TÂM)', fontsize=12.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(46.0, 7.4, 'TÒA A3 (MÁI CHE KHỐI 1 TẦNG)', fontsize=11.5, fontweight='bold', color=COLOR_TEXT_MUTED, ha='center', va='center')

    # Courtyard Labels
    ax.text(10.0, 0.0, 'KHOẢNG SÂN\nNỘI BỘ', fontsize=8.5, color='#94a3b8', fontweight='bold', ha='center', va='center')
    ax.text(40.0, 0.0, 'KHOẢNG SÂN\nNỘI BỘ', fontsize=8.5, color='#94a3b8', fontweight='bold', ha='center', va='center')

    # ---------------------------------------------------------
    # 3. CORRIDOR & HALL BACKGROUND FILLS
    # ---------------------------------------------------------
    # Enclosed Horizontal Corridor (X: 12.0 to 38.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((12.0, -0.9), 26.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Central Stair Hall Space (X: 22.0 to 28.0, Y: 0.9 to 4.5)
    ax.add_patch(patches.Rectangle((22.0, 0.9), 6.0, 3.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 3 - TÒA A2 - 8 PHÒNG)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA A2 DÃY PHÍA BẮC (Y: 0.9 to 4.5m) ===
        {
            'id': 'T3_A2_PCA', 'name': 'Phòng Phó\nChánh án',
            'x': 12.0, 'y': 0.9, 'w': 5.5, 'h': 3.6,
            'text_center': (14.75, 2.7),
            'door': (13.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T3_A2_TP', 'name': 'Phòng\nThẩm phán',
            'x': 17.5, 'y': 0.9, 'w': 4.5, 'h': 3.6,
            'text_center': (19.75, 2.7),
            'door': (18.5, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T3_A2_TK1', 'name': 'Phòng\nthư ký',
            'x': 28.0, 'y': 0.9, 'w': 5.0, 'h': 3.6,
            'text_center': (30.5, 2.7),
            'door': (29.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T3_A2_TK2', 'name': 'Phòng\nthư ký',
            'x': 33.0, 'y': 0.9, 'w': 5.0, 'h': 3.6,
            'text_center': (35.5, 2.7),
            'door': (34.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },

        # === TÒA A2 DÃY PHÍA NAM (Y: -4.5 to -0.9m) ===
        {
            'id': 'T3_A2_LT1', 'name': 'Phòng\nlưu trữ',
            'x': 12.0, 'y': -4.5, 'w': 6.5, 'h': 3.6,
            'text_center': (15.25, -2.7),
            'door': (13.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T3_A2_PCVP', 'name': 'Phòng Phó chánh\nvăn phòng',
            'x': 18.5, 'y': -4.5, 'w': 6.5, 'h': 3.6,
            'text_center': (21.75, -2.7),
            'door': (20.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'T3_A2_SH', 'name': 'Phòng\nsố hoá',
            'x': 25.0, 'y': -4.5, 'w': 6.5, 'h': 3.6,
            'text_center': (28.25, -2.7),
            'door': (26.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T3_A2_LT2', 'name': 'Phòng lưu trữ\ntài liệu',
            'x': 31.5, 'y': -4.5, 'w': 6.5, 'h': 3.6,
            'text_center': (34.75, -2.7),
            'door': (33.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. TÒA A1 & TÒA A3 (MÁI CHE - ĐỘC LẬP)
    # ---------------------------------------------------------
    # TÒA A1 Roof block: X = 0.0 to 8.0, Y = -6.5 to 6.5
    roof_a1 = patches.Rectangle((0.0, -6.5), 8.0, 13.0, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=2.4, zorder=2)
    ax.add_patch(roof_a1)
    ax.plot([0.0, 4.0], [-6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.plot([8.0, 4.0], [-6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.plot([0.0, 4.0], [6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.plot([8.0, 4.0], [6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.text(4.0, 0.0, 'MÁI CHE\n(TÒA A1)', color=COLOR_TEXT_MUTED, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # TÒA A3 Roof block: X = 42.0 to 50.0, Y = -6.5 to 6.5
    roof_a3 = patches.Rectangle((42.0, -6.5), 8.0, 13.0, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=2.4, zorder=2)
    ax.add_patch(roof_a3)
    ax.plot([42.0, 46.0], [-6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.plot([50.0, 46.0], [-6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.plot([42.0, 46.0], [6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.plot([50.0, 46.0], [6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.text(46.0, 0.0, 'MÁI CHE\n(TÒA A3)', color=COLOR_TEXT_MUTED, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. STAIRCASE (TÒA A2 - TẦNG 3 NỀN TRẮNG `#ffffff`, 2 VẾ ĐỐI XỨNG)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 23.5, 1.3, 3.0, 3.2
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Center railing divider running full height
    mid_x = stair_x + stair_w / 2.0
    ax.plot([mid_x, mid_x], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)

    ax.text(mid_x, stair_y - 0.25, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.0, ha='center', va='top', zorder=5)

    # ---------------------------------------------------------
    # 7. EXTERIOR WALLS & INTERIOR PARTITIONS (TÒA A2 ENCLOSED)
    # ---------------------------------------------------------
    def draw_wall(x1, y1, x2, y2, lw=2.4):
        ax.plot([x1, x2], [y1, y2], color=COLOR_WALL, linewidth=lw, solid_capstyle='butt', zorder=5)

    def draw_part(x1, y1, x2, y2, lw=1.2):
        ax.plot([x1, x2], [y1, y2], color=COLOR_WALL, linewidth=lw, solid_capstyle='butt', zorder=5)

    # ================== TÒA A2 (ENCLOSED) ==================
    # North wall: Continuous from 12.0 to 38.0 at Y = 4.5
    draw_wall(12.0, 4.5, 38.0, 4.5)
    # South wall: Continuous from 12.0 to 38.0 at Y = -4.5
    draw_wall(12.0, -4.5, 38.0, -4.5)
    # West wall: Enclosed at X = 12.0 from -4.5 to 4.5
    draw_wall(12.0, -4.5, 12.0, 4.5)
    # East wall: Enclosed at X = 38.0 from -4.5 to 4.5
    draw_wall(38.0, -4.5, 38.0, 4.5)

    # A2 Corridor walls:
    # North (Y = 0.9):
    draw_part(12.0, 0.9, 13.2, 0.9)
    draw_part(14.05, 0.9, 18.5, 0.9)
    draw_part(19.35, 0.9, 22.0, 0.9)
    # (X = 22.0 to 28.0 is Open Stair Hall)
    draw_part(28.0, 0.9, 29.2, 0.9)
    draw_part(30.05, 0.9, 34.2, 0.9)
    draw_part(35.05, 0.9, 38.0, 0.9)

    # South (Y = -0.9):
    draw_part(12.0, -0.9, 13.5, -0.9)
    draw_part(14.35, -0.9, 20.0, -0.9)
    draw_part(20.85, -0.9, 26.5, -0.9)
    draw_part(27.35, -0.9, 33.0, -0.9)
    draw_part(33.85, -0.9, 38.0, -0.9)

    # North Partitions:
    draw_part(17.5, 0.9, 17.5, 4.5)
    draw_part(22.0, 0.9, 22.0, 4.5)
    draw_part(28.0, 0.9, 28.0, 4.5)
    draw_part(33.0, 0.9, 33.0, 4.5)

    # South Partitions:
    draw_part(18.5, -4.5, 18.5, -0.9)
    draw_part(25.0, -4.5, 25.0, -0.9)
    draw_part(31.5, -4.5, 31.5, -0.9)

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

    # Windows on Tòa A2:
    draw_window_v(12.0, -0.4, 0.4)  # West corridor end window
    draw_window_h(13.5, 16.0, 4.5)
    draw_window_h(18.5, 21.0, 4.5)
    draw_window_h(24.0, 26.0, 4.5)  # Stair hall window
    draw_window_h(29.5, 31.5, 4.5)
    draw_window_h(34.5, 36.5, 4.5)

    draw_window_h(13.5, 16.5, -4.5)
    draw_window_h(20.0, 23.0, -4.5)
    draw_window_h(26.5, 29.5, -4.5)
    draw_window_h(33.0, 36.0, -4.5)
    draw_window_v(38.0, -0.4, 0.4)  # East corridor end window

    # ---------------------------------------------------------
    # 10. LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'],
                fontweight='bold', ha='center', va='center', zorder=7)

    # Corridor Labels
    ax.text(17.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=7)
    ax.text(33.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=7)

    # ---------------------------------------------------------
    # 11. EXPORT DRAWING
    # ---------------------------------------------------------
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(out_dir, 'mat_bang_tang_3.png')
    plt.savefig(out_file, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Bản vẽ Tầng 3 đã xuất thành công tại: {out_file}")

if __name__ == '__main__':
    create_floorplan_tang3()
