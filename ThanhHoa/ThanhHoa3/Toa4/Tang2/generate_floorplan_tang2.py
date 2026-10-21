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

def create_floorplan_tang2(output_dir: str = None):
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, "mat_bang_tang_2.png")

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(18, 11), dpi=300)
    ax = fig.add_axes([0.03, 0.08, 0.94, 0.82])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Architectural Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#ffffff'    # Floor 2 stair fill is pure white per Spec

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single line, font 20 bold, NO subtitle line)
    fig.text(0.04, 0.94, 'MẶT BẰNG TẦNG 2  —  Tòa nhà 4  —  Tòa án nhân dân khu vực 3 - Thanh Hóa', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.04, 0.96], [0.915, 0.915], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = -0.5, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 5.5, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 6.6, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 10.5, lg_x + 11.3], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 10.5, lg_x + 11.3], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 11.6, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 15.0, lg_x + 15.0], [lg_y + 0.02, lg_y + 0.32], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 15.0, lg_y + 0.02), 0.60, 0.60, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 16.3, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. LOBBY & CORRIDOR BACKGROUND FILL (OPEN CIRCULATION)
    # ---------------------------------------------------------
    # Central Hall / Lobby (X: 10.0 to 15.0, Y: -4.9 to 5.4)
    ax.add_patch(patches.Rectangle((10.0, -4.9), 5.0, 10.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # East Wing Corridor & Stair Hall (X: 15.0 to 20.0, Y: -0.9 to 5.4)
    ax.add_patch(patches.Rectangle((15.0, -0.9), 5.0, 6.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (PHÒNG XÉT XỬ DÂN SỰ & PHÒNG KẾ TOÁN)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # 1. Cánh Tây: Phòng xét xử dân sự (KT: 10x5)
        {
            'id': 'T4_XXDS', 'name': 'Phòng xét xử dân sự',
            'x': 0.0, 'y': -4.9, 'w': 10.0, 'h': 10.3,
            'text_center': (5.0, 0.25),
            'door': (10.0, -1.0, 1.4, 'DOUBLE_W'),
            'font_size': 13.5
        },
        # 2. Cánh Đông Nam: Phòng kế toán (KT: 3x4)
        {
            'id': 'T4_KT', 'name': 'Phòng kế toán',
            'x': 15.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (17.5, -2.9),
            'door': (16.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 11.5
        },
    ]

    # Draw Room Backgrounds (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHIC (UPPER FLOOR SPEC: PURE WHITE BACKGROUND)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 16.2, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, 
                                 edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    # Horizontal tread lines for left and right flights
    gap = 0.35
    flight_w = (stair_w - gap) / 2.0
    left_x1, left_x2 = stair_x, stair_x + flight_w
    right_x1, right_x2 = stair_x + flight_w + gap, stair_x + stair_w

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([left_x1, left_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
        ax.plot([right_x1, right_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Vertical line down the middle of left flight & right flight
    mid_left = left_x1 + flight_w / 2.0
    mid_right = right_x1 + flight_w / 2.0
    ax.plot([mid_left, mid_left], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([mid_right, mid_right], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Staircase label underneath box
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # Central Hall / Lobby label
    ax.text(12.5, 0.0, 'HÀNH LANG SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (ENCLOSED EXTERIOR, NO OUTDOOR STAIRS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Wall (West facade continuous)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2 * W)

    # Rightmost Vertical Exterior Wall (East facade continuous)
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2 * W)

    # North Top Wall (Continuous across entire North facade)
    draw_wall(-W, 5.4, 20.0 + 2 * W, W)

    # South Bottom Wall (Continuous across entire South facade)
    draw_wall(-W, -4.9 - W, 20.0 + 2 * W, W)

    # Partition Wall at X = 10.0 separating Trial Room from Central Lobby
    # Double door at Y = -1.0 (from Y: -1.7 to -0.3, size = 1.4m)
    draw_wall(10.0 - P/2, -4.9, P, 3.2)               # Segment from -4.9 to -1.7
    draw_wall(10.0 - P/2, -0.3, P, 5.4 - (-0.3))      # Segment from -0.3 to 5.4

    # Partition Wall at X = 15.0 (West wall of Phòng kế toán)
    draw_wall(15.0 - P/2, -4.9, P, 4.0)               # West wall of Phòng kế toán (Y: -4.9 to -0.9)
    # Staircase is open to the lobby (no wall between X = 15.0 and stair hall)

    # North Corridor Wall of Phòng kế toán (along Y = -0.9)
    # Door at X = 16.5 to 17.35 (size 0.85m)
    draw_wall(15.0, -0.9 - P/2, 1.5, P)               # Segment from 15.0 to 16.5
    draw_wall(17.35, -0.9 - P/2, 20.0 - 17.35, P)     # Segment from 17.35 to 20.0

    # ---------------------------------------------------------
    # 7. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    # Double door into Phòng xét xử dân sự at X = 10.0, Y = -1.0
    d_x, d_y = 10.0, -1.0
    half_d = 0.7
    ax.plot([d_x - half_d, d_x], [d_y - half_d, d_y - half_d], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
    ax.plot([d_x - half_d, d_x], [d_y + half_d, d_y + half_d], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
    arc1 = patches.Arc((d_x, d_y - half_d), half_d * 2, half_d * 2, angle=0, theta1=90, theta2=180, 
                       color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
    arc2 = patches.Arc((d_x, d_y + half_d), half_d * 2, half_d * 2, angle=0, theta1=180, theta2=270, 
                       color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
    ax.add_patch(arc1)
    ax.add_patch(arc2)

    # Single door into Phòng kế toán at X = 16.5, Y = -0.9
    kd_x, kd_y, kd_sz = 16.5, -0.9, 0.85
    ax.plot([kd_x, kd_x], [kd_y, kd_y - kd_sz], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
    arc_kd = patches.Arc((kd_x, kd_y), kd_sz * 2, kd_sz * 2, angle=0, theta1=270, theta2=360, 
                         color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
    ax.add_patch(arc_kd)

    # ---------------------------------------------------------
    # 8. DRAW WINDOWS ON EXTERIOR WALLS
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

    # Top Windows (North Facade: Y = 5.4)
    draw_window(1.8, 5.4, 2.5, W, is_horizontal=True)      # Phòng xét xử dân sự window 1
    draw_window(5.8, 5.4, 2.5, W, is_horizontal=True)      # Phòng xét xử dân sự window 2
    draw_window(11.2, 5.4, 2.5, W, is_horizontal=True)     # Central Hall North window
    draw_window(16.2, 5.4, 2.5, W, is_horizontal=True)     # Stair Hall North window

    # Bottom Windows (South Front Facade: Y = -4.9 - W)
    draw_window(1.8, -4.9 - W, 2.5, W, is_horizontal=True)  # Phòng xét xử dân sự window 1
    draw_window(5.8, -4.9 - W, 2.5, W, is_horizontal=True)  # Phòng xét xử dân sự window 2
    draw_window(11.2, -4.9 - W, 2.5, W, is_horizontal=True) # Central Hall South window
    draw_window(16.2, -4.9 - W, 2.5, W, is_horizontal=True) # Phòng kế toán South window

    # Side Windows
    # West Facade (X = -W)
    draw_window(-W, 2.2, W, 2.0, is_horizontal=False)       # Trial Room West window North
    draw_window(-W, -1.0, W, 2.0, is_horizontal=False)      # Trial Room West window Center
    draw_window(-W, -4.2, W, 2.0, is_horizontal=False)      # Trial Room West window South

    # East Facade (X = 20.0)
    draw_window(20.0, 2.2, W, 2.0, is_horizontal=False)     # Stair hall East window
    draw_window(20.0, -0.6, W, 1.2, is_horizontal=False)    # Corridor East window
    draw_window(20.0, -3.8, W, 2.0, is_horizontal=False)    # Phòng kế toán East window

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 11.5)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, 
                fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 22.0)
    ax.set_ylim(-8.5, 8.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Toa 4 Floor 2 floorplan PNG at {out_img_path}")
    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang2()
