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

def create_floorplan_tang2(court_name: str = COURT_NAME):
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
    COLOR_STAIR_FILL = '#ffffff'    # Floor 2 stair fill is pure white per spec

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.02, 0.95, f'MẶT BẰNG TẦNG 2  —  {court_name}',
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
    ax.text(4.0, 7.4, 'TÒA A1 (TẦNG 2)', fontsize=11.5, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(25.0, 5.3, 'TÒA A2 (KHỐI HÀNH CHÍNH TRUNG TÂM)', fontsize=12.0, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center')
    ax.text(46.0, 7.4, 'TÒA A3 (MÁI CHE KHỐI 1 TẦNG)', fontsize=11.5, fontweight='bold', color=COLOR_TEXT_MUTED, ha='center', va='center')

    # Courtyard Labels
    ax.text(10.0, 0.0, 'KHOẢNG SÂN\nNỘI BỘ', fontsize=8.5, color='#94a3b8', fontweight='bold', ha='center', va='center')
    ax.text(40.0, 0.0, 'KHOẢNG SÂN\nNỘI BỘ', fontsize=8.5, color='#94a3b8', fontweight='bold', ha='center', va='center')

    # ---------------------------------------------------------
    # 3. CORRIDOR & HALL BACKGROUND FILLS
    # ---------------------------------------------------------
    # === TÒA A1: Internal Enclosed Corridor (X: 0.0 to 8.0, Y: -0.9 to 0.9) ===
    ax.add_patch(patches.Rectangle((0.0, -0.9), 8.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === TÒA A2: Corridor & Stair Hall ===
    # Enclosed Horizontal Corridor (X: 12.0 to 38.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((12.0, -0.9), 26.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Central Stair Hall Space (X: 22.0 to 28.0, Y: 0.9 to 4.5)
    ax.add_patch(patches.Rectangle((22.0, 0.9), 6.0, 3.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 2 - CÁC PHÒNG KHẢO SÁT)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA A1 (5 PHÒNG) ===
        # North Wing (Phòng xét xử dân sự tầng 2: 8.0m x 5.6m)
        {
            'id': 'T2_A1_XXDS', 'name': 'Phòng xét xử\ndân sự tầng 2',
            'x': 0.0, 'y': 0.9, 'w': 8.0, 'h': 5.6,
            'text_center': (4.0, 3.7),
            'door': (6.0, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        # South Wing (4 Phòng chia 2x2 ô)
        {
            'id': 'T2_A1_TK1', 'name': 'Phòng\nthư ký',
            'x': 0.0, 'y': -3.7, 'w': 4.0, 'h': 2.8,
            'text_center': (2.0, -2.3),
            'door': (1.0, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.8
        },
        {
            'id': 'T2_A1_HG', 'name': 'Phòng\nhoà giải',
            'x': 4.0, 'y': -3.7, 'w': 4.0, 'h': 2.8,
            'text_center': (6.0, -2.3),
            'door': (5.0, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.8
        },
        {
            'id': 'T2_A1_TK2', 'name': 'Phòng\nthư ký',
            'x': 0.0, 'y': -6.5, 'w': 4.0, 'h': 2.8,
            'text_center': (2.0, -5.1),
            'door': (1.0, -3.7, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.8
        },
        {
            'id': 'T2_A1_TK3', 'name': 'Phòng\nthư ký',
            'x': 4.0, 'y': -6.5, 'w': 4.0, 'h': 2.8,
            'text_center': (6.0, -5.1),
            'door': (5.0, -3.7, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.8
        },

        # === TÒA A2 (KHỐI THÂN GIỮA) ===
        # Dãy phía Bắc (Y: 0.9 to 4.5m)
        {
            'id': 'T2_A2_TP1', 'name': 'Phòng\nThẩm phán',
            'x': 12.0, 'y': 0.9, 'w': 5.0, 'h': 3.6,
            'text_center': (14.5, 2.7),
            'door': (13.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T2_A2_TP2', 'name': 'Phòng\nThẩm phán',
            'x': 17.0, 'y': 0.9, 'w': 5.0, 'h': 3.6,
            'text_center': (19.5, 2.7),
            'door': (18.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 9.2
        },
        {
            'id': 'T2_A2_PH', 'name': 'Phòng họp',
            'x': 28.0, 'y': 0.9, 'w': 10.0, 'h': 3.6,
            'text_center': (33.0, 2.7),
            'door': (29.2, 0.9, 0.95, 'N_IN_RIGHT'),
            'font_size': 11.0
        },

        # Dãy phía Nam (Y: -4.5 to -0.9m)
        {
            'id': 'T2_A2_TK4', 'name': 'Phòng\nthư ký',
            'x': 12.0, 'y': -4.5, 'w': 5.0, 'h': 3.6,
            'text_center': (14.5, -2.7),
            'door': (13.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'T2_A2_LV1', 'name': 'Phòng\nlàm việc',
            'x': 17.0, 'y': -4.5, 'w': 5.0, 'h': 3.6,
            'text_center': (19.5, -2.7),
            'door': (18.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
        # Central Independent Room at former lobby location (Spec T2/3)
        {
            'id': 'T2_A2_PCA', 'name': 'Phòng Phó\nChánh án',
            'x': 22.0, 'y': -4.5, 'w': 6.0, 'h': 3.6,
            'text_center': (25.0, -2.7),
            'door': (23.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T2_A2_TK5', 'name': 'Phòng\nthư ký',
            'x': 28.0, 'y': -4.5, 'w': 5.0, 'h': 3.6,
            'text_center': (30.5, -2.7),
            'door': (29.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
        {
            'id': 'T2_A2_LV2', 'name': 'Phòng\nlàm việc',
            'x': 33.0, 'y': -4.5, 'w': 5.0, 'h': 3.6,
            'text_center': (35.5, -2.7),
            'door': (34.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. TÒA A3 (MÁI CHE - ĐỘC LẬP)
    # ---------------------------------------------------------
    roof_a3 = patches.Rectangle((42.0, -6.5), 8.0, 13.0, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=2.4, zorder=2)
    ax.add_patch(roof_a3)

    # Diagonal dashed drainage lines
    ax.plot([42.0, 46.0], [-6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.plot([50.0, 46.0], [-6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.plot([42.0, 46.0], [6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)
    ax.plot([50.0, 46.0], [6.5, 0.0], color='#cbd5e1', linestyle='--', linewidth=1.2, zorder=3)

    ax.text(46.0, 0.0, 'MÁI CHE\n(TÒA A3)', color=COLOR_TEXT_MUTED, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. STAIRCASE (TÒA A2 - TẦNG 2 NỀN TRẮNG `#ffffff`, 2 VẾ ĐỐI XỨNG)
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
    # 7. EXTERIOR WALLS & INTERIOR PARTITIONS (ENCLOSED)
    # ---------------------------------------------------------
    def draw_wall(x1, y1, x2, y2, lw=2.4):
        ax.plot([x1, x2], [y1, y2], color=COLOR_WALL, linewidth=lw, solid_capstyle='butt', zorder=5)

    def draw_part(x1, y1, x2, y2, lw=1.2):
        ax.plot([x1, x2], [y1, y2], color=COLOR_WALL, linewidth=lw, solid_capstyle='butt', zorder=5)

    # ================== TÒA A1 (ENCLOSED) ==================
    draw_wall(0.0, -6.5, 0.0, 6.5)
    draw_wall(0.0, 6.5, 8.0, 6.5)
    draw_wall(0.0, -6.5, 8.0, -6.5)
    draw_wall(8.0, -6.5, 8.0, 6.5)  # Enclosed east wall (has window in corridor)

    # A1 Corridor walls (Y = 0.9 & -0.9)
    draw_part(0.0, 0.9, 6.0, 0.9)
    draw_part(6.9, 0.9, 8.0, 0.9)

    draw_part(0.0, -0.9, 1.0, -0.9)
    draw_part(1.8, -0.9, 5.0, -0.9)
    draw_part(5.8, -0.9, 8.0, -0.9)

    # A1 South interior partitions:
    draw_part(4.0, -6.5, 4.0, -0.9)
    draw_part(0.0, -3.7, 1.0, -3.7)
    draw_part(1.8, -3.7, 5.0, -3.7)
    draw_part(5.8, -3.7, 8.0, -3.7)

    # ================== TÒA A2 (ENCLOSED) ==================
    # North wall: Continuous from 12.0 to 38.0 at Y = 4.5
    draw_wall(12.0, 4.5, 38.0, 4.5)
    # South wall: Continuous from 12.0 to 38.0 at Y = -4.5
    draw_wall(12.0, -4.5, 38.0, -4.5)
    # West wall: Enclosed from -4.5 to 4.5 at X = 12.0
    draw_wall(12.0, -4.5, 12.0, 4.5)
    # East wall: Enclosed from -4.5 to 4.5 at X = 38.0
    draw_wall(38.0, -4.5, 38.0, 4.5)

    # A2 Corridor walls:
    # North (Y = 0.9):
    draw_part(12.0, 0.9, 13.2, 0.9)
    draw_part(14.05, 0.9, 18.2, 0.9)
    draw_part(19.05, 0.9, 22.0, 0.9)
    # (X = 22.0 to 28.0 is Open Stair Hall)
    draw_part(28.0, 0.9, 29.2, 0.9)
    draw_part(30.15, 0.9, 38.0, 0.9)

    # South (Y = -0.9):
    draw_part(12.0, -0.9, 13.2, -0.9)
    draw_part(14.05, -0.9, 18.2, -0.9)
    draw_part(19.05, -0.9, 23.2, -0.9)
    draw_part(24.05, -0.9, 29.2, -0.9)
    draw_part(30.05, -0.9, 34.2, -0.9)
    draw_part(35.05, -0.9, 38.0, -0.9)

    # A2 Partitions:
    draw_part(17.0, 0.9, 17.0, 4.5)
    draw_part(22.0, 0.9, 22.0, 4.5)
    draw_part(28.0, 0.9, 28.0, 4.5)

    draw_part(17.0, -4.5, 17.0, -0.9)
    draw_part(22.0, -4.5, 22.0, -0.9)
    draw_part(28.0, -4.5, 28.0, -0.9)
    draw_part(33.0, -4.5, 33.0, -0.9)

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
    draw_window_v(0.0, -0.4, 0.4)   # West corridor window
    draw_window_v(0.0, -5.0, -2.0)  # West lower
    draw_window_h(1.0, 3.0, -6.5)   # South 1
    draw_window_h(5.0, 7.0, -6.5)   # South 2
    draw_window_v(8.0, -0.4, 0.4)   # East corridor window looking into courtyard

    # Windows on Tòa A2:
    draw_window_v(12.0, -0.4, 0.4)  # West corridor end window
    draw_window_h(13.5, 15.5, 4.5)
    draw_window_h(18.5, 20.5, 4.5)
    draw_window_h(24.0, 26.0, 4.5)  # Stair hall window
    draw_window_h(30.0, 32.0, 4.5)
    draw_window_h(34.0, 36.0, 4.5)

    draw_window_h(13.5, 15.5, -4.5)
    draw_window_h(18.5, 20.5, -4.5)
    draw_window_h(23.5, 26.5, -4.5) # Central room window (former lobby)
    draw_window_h(29.5, 31.5, -4.5)
    draw_window_h(34.5, 36.5, -4.5)
    draw_window_v(38.0, -0.4, 0.4)  # East corridor end window

    # ---------------------------------------------------------
    # 10. LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'],
                fontweight='bold', ha='center', va='center', zorder=7)

    # Corridor Labels
    ax.text(4.0, 0.0, 'SẢNH / HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=7)
    ax.text(17.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=7)
    ax.text(33.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=7)

    # ---------------------------------------------------------
    # 11. EXPORT DRAWING
    # ---------------------------------------------------------
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(out_dir, 'mat_bang_tang_2.png')
    plt.savefig(out_file, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Bản vẽ Tầng 2 đã xuất thành công tại: {out_file}")

if __name__ == '__main__':
    create_floorplan_tang2()
