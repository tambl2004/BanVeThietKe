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

def create_floorplan_tang1(output_dir: str = None):
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, "mat_bang_tang_1.png")

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 15), dpi=300)
    ax = fig.add_axes([0.02, 0.06, 0.96, 0.86])
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
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 stair fill matches lobby color per Spec

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 1 - Điện Biên', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.03, 0.97], [0.925, 0.925], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = 1.0, -7.8
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.1, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.add_patch(patches.Rectangle((lg_x + 7.5, lg_y + 0.15), 1.2, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 9.0, lg_y + 0.1, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 15.0, lg_x + 16.2], [lg_y + 0.25, lg_y + 0.25], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 15.0, lg_x + 16.2], [lg_y + 0.10, lg_y + 0.10], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 16.6, lg_y + 0.1, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 22.0, lg_x + 22.0], [lg_y + 0.05, lg_y + 0.45], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 22.0, lg_y + 0.05), 0.8, 0.8, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 23.4, lg_y + 0.1, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Main Horizontal Corridor (X: 0 to 32, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 32.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Central Lobby (South: X: 13.5 to 18.5, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((13.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    # Rear Circulation & Stair Hall (North: X: 13.5 to 18.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Corridor labels
    bbox_style = dict(boxstyle='round,pad=0.2', facecolor=COLOR_FILL_CORRIDOR, edgecolor='none')
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5, bbox=bbox_style)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5, bbox=bbox_style)
    ax.text(16.0, -2.9, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (7 ROOMS AS SURVEY DATA)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- CÁNH TÂY NAM (South West Wing): Phòng xét xử Dân sự (lớn) ---
        {
            'id': 'T1_XXDS', 'name': 'Phòng xét xử Dân sự',
            'x': 0.0, 'y': -4.9, 'w': 13.5, 'h': 4.0,
            'text_center': (6.75, -2.9),
            'door': (6.05, -0.9, 1.4, 'DOUBLE_S_IN'),
            'font_size': 12.0
        },
        # --- CÁNH TÂY BẮC (North West Wing): 3 phòng làm việc ---
        # Mỗi cửa cách vách phải 0.3m má tường
        {
            'id': 'T1_CV', 'name': 'Phòng Chánh văn Phòng',
            'x': 0.0, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (2.25, 3.15),
            'door': (3.3, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'T1_PCV', 'name': 'Phòng Phó Chánh văn Phòng',
            'x': 4.5, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (6.75, 3.15),
            'door': (7.8, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'T1_TK1', 'name': 'Phòng Thư ký viên',
            'x': 9.0, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (11.25, 3.15),
            'door': (12.3, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        # --- CÁNH ĐÔNG BẮC (North East Wing): Tổ hành chính tư pháp + Tiếp công dân ---
        {
            'id': 'T1_HCTP', 'name': 'Phòng Tổ hành chính tư pháp\n+ Tiếp công dân',
            'x': 18.5, 'y': 0.9, 'w': 13.5, 'h': 4.5,
            'text_center': (25.25, 3.15),
            'door': (24.65, 0.9, 1.2, 'DOUBLE_N_IN'),
            'font_size': 11.5
        },
        # --- CÁNH ĐÔNG NAM (South East Wing): 2 phòng làm việc ---
        # Mỗi cửa cách vách trái 0.3m má tường
        {
            'id': 'T1_TK2', 'name': 'Phòng Thư ký viên',
            'x': 18.5, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (21.875, -2.9),
            'door': (18.8, -0.9, 0.9, 'S_IN_LEFT'),
            'font_size': 10.5
        },
        {
            'id': 'T1_VT', 'name': 'Phòng Văn thư',
            'x': 25.25, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (28.625, -2.9),
            'door': (25.55, -0.9, 0.9, 'S_IN_LEFT'),
            'font_size': 10.5
        },
    ]

    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS (FLOOR 1 SPECIFIC)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 14.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # 1. Front Main Entrance Steps at South (Y = -4.9 to -5.7, X = 13.5 to 18.5)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([13.5, 18.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([13.5, 13.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([18.5, 18.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # 2. Rear Exit Steps at North (Y = 5.4 to 6.2, X = 13.5 to 18.5)
    for sy in [5.4, 5.56, 5.72, 5.88, 6.04, 6.20]:
        ax.plot([13.5, 18.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([13.5, 13.5], [5.4, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([18.5, 18.5], [5.4, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)
    # North exit inward wall hooks at top end (0.5m inward)
    ax.plot([13.5, 14.0], [6.20, 6.20], color=COLOR_WALL, linewidth=1.4, zorder=4)
    ax.plot([18.0, 18.5], [6.20, 6.20], color=COLOR_WALL, linewidth=1.4, zorder=4)

    # 3. Side Outdoor Steps at Corridor Ends
    for sx in [0.0, -0.16, -0.32, -0.48, -0.64, -0.80]:
        ax.plot([sx, sx], [-0.9, 0.9], color=COLOR_WALL, linewidth=0.8, zorder=4)
    for sx in [32.0, 32.16, 32.32, 32.48, 32.64, 32.80]:
        ax.plot([sx, sx], [-0.9, 0.9], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # ---------------------------------------------------------
    # 6. DRAW WALLS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior Leftmost Walls (West)
    draw_wall(-W, 0.9, W, 4.5 + W)
    draw_wall(-W, -4.9 - W, W, 4.0 + W)

    # Exterior Rightmost Walls (East)
    draw_wall(32.0, 0.9, W, 4.5 + W)
    draw_wall(32.0, -4.9 - W, W, 4.0 + W)

    # North Top Wall (with opening at X: 13.5 to 18.5)
    draw_wall(-W, 5.4, 13.5 + W + P/2, W)
    draw_wall(18.5 - P/2, 5.4, 13.5 + W + P/2, W)

    # South Bottom Wall (with opening at X: 13.5 to 18.5)
    draw_wall(-W, -4.9 - W, 13.5 + W + P/2, W)
    draw_wall(18.5 - P/2, -4.9 - W, 13.5 + W + P/2, W)

    # Structural Cheeks & Hooks
    draw_wall(13.5 - P/2, -5.7, P, 0.8)
    draw_wall(18.5 - P/2, -5.7, P, 0.8)
    draw_wall(13.5 - P/2, 5.4, P, 0.8)
    draw_wall(18.5 - P/2, 5.4, P, 0.8)
    draw_wall(13.5 - P/2, 6.2 - P, 0.5, P)
    draw_wall(18.5 + P/2 - 0.5, 6.2 - P, 0.5, P)

    # Horizontal Corridor Partitions:
    # 1. North Corridor Wall (Y = 0.9 - P/2)
    # Openings:
    # - Door T1_CV: 3.3 to 4.2
    # - Door T1_PCV: 7.8 to 8.7
    # - Door T1_TK1: 12.3 to 13.2
    draw_wall(0.0, 0.9 - P/2, 3.3, P)
    draw_wall(4.2, 0.9 - P/2, 7.8 - 4.2, P)
    draw_wall(8.7, 0.9 - P/2, 12.3 - 8.7, P)
    draw_wall(13.2, 0.9 - P/2, 13.5 - 13.2, P)

    # East North: opening at double door 24.65 to 25.85 (1.2m)
    draw_wall(18.5, 0.9 - P/2, 24.65 - 18.5, P)
    draw_wall(25.85, 0.9 - P/2, 32.0 - 25.85, P)

    # 2. South Corridor Wall (Y = -0.9 - P/2)
    # West South: opening at double door 6.05 to 7.45 (1.4m)
    draw_wall(0.0, -0.9 - P/2, 6.05, P)
    draw_wall(7.45, -0.9 - P/2, 13.5 - 7.45, P)

    # East South: openings at 18.8 to 19.7 (0.9m) and 25.55 to 26.45 (0.9m)
    draw_wall(18.5, -0.9 - P/2, 18.8 - 18.5, P)
    draw_wall(19.7, -0.9 - P/2, 25.55 - 19.7, P)
    draw_wall(26.45, -0.9 - P/2, 32.0 - 26.45, P)

    # Vertical Room Partitions:
    draw_wall(4.5 - P/2, 0.9, P, 4.5)
    draw_wall(9.0 - P/2, 0.9, P, 4.5)
    draw_wall(13.5 - P/2, 0.9, P, 4.5)
    draw_wall(18.5 - P/2, 0.9, P, 4.5)

    draw_wall(13.5 - P/2, -4.9, P, 4.0)
    draw_wall(18.5 - P/2, -4.9, P, 4.0)
    draw_wall(25.25 - P/2, -4.9, P, 4.0)

    # ---------------------------------------------------------
    # 7. DRAW WINDOWS ON EXTERIOR WALLS
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

    # North Facade Windows (Y = 5.4)
    draw_window(1.2, 5.4, 2.1, W, is_horizontal=True)    # Chánh văn phòng
    draw_window(5.7, 5.4, 2.1, W, is_horizontal=True)    # Phó Chánh văn phòng
    draw_window(10.2, 5.4, 2.1, W, is_horizontal=True)   # Thư ký viên
    draw_window(20.5, 5.4, 2.2, W, is_horizontal=True)   # Tổ HCTP 1
    draw_window(24.5, 5.4, 2.2, W, is_horizontal=True)   # Tổ HCTP 2
    draw_window(28.5, 5.4, 2.2, W, is_horizontal=True)   # Tổ HCTP 3

    # South Facade Windows (Y = -4.9 - W)
    draw_window(2.0, -4.9 - W, 2.4, W, is_horizontal=True)  # Xét xử dân sự 1
    draw_window(6.0, -4.9 - W, 2.4, W, is_horizontal=True)  # Xét xử dân sự 2
    draw_window(10.0, -4.9 - W, 2.4, W, is_horizontal=True) # Xét xử dân sự 3
    draw_window(20.5, -4.9 - W, 2.2, W, is_horizontal=True) # Thư ký viên
    draw_window(27.0, -4.9 - W, 2.2, W, is_horizontal=True) # Văn thư

    # West & East Facade Windows
    draw_window(-W, 2.0, W, 2.2, is_horizontal=False)     # West Upper
    draw_window(-W, -3.8, W, 2.2, is_horizontal=False)    # West Lower
    draw_window(32.0, 2.0, W, 2.2, is_horizontal=False)   # East Upper
    draw_window(32.0, -3.8, W, 2.2, is_horizontal=False)  # East Lower

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode == 'N_IN_RIGHT':
            pivot_x = x + size
            ax.plot([pivot_x, pivot_x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((pivot_x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_LEFT':
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360,
                              color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'DOUBLE_S_IN':
            half = size / 2.0
            p_left = x
            ax.plot([p_left, p_left], [y, y - half], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_left = patches.Arc((p_left, y), half*2, half*2, angle=0, theta1=270, theta2=360,
                                   color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc_left)
            p_right = x + size
            ax.plot([p_right, p_right], [y, y - half], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_right = patches.Arc((p_right, y), half*2, half*2, angle=0, theta1=180, theta2=270,
                                    color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc_right)
        elif mode == 'DOUBLE_N_IN':
            half = size / 2.0
            p_left = x
            ax.plot([p_left, p_left], [y, y + half], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_left = patches.Arc((p_left, y), half*2, half*2, angle=0, theta1=0, theta2=90,
                                   color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc_left)
            p_right = x + size
            ax.plot([p_right, p_right], [y, y + half], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_right = patches.Arc((p_right, y), half*2, half*2, angle=0, theta1=90, theta2=180,
                                    color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
            ax.add_patch(arc_right)

    for r in rooms:
        dx, dy, dsize, dmode = r['door']
        draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 11.0)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.5, 34.5)
    ax.set_ylim(-8.5, 8.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 1 floorplan PNG at {out_img_path}")
    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang1()
