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

def create_floorplan_tang2():
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(18, 11), dpi=300)
    ax = fig.add_axes([0.03, 0.08, 0.94, 0.82])
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
    COLOR_STAIR_FILL = '#ffffff'     # Pure white for stair background in Floor 2

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & FOOTER
    # ---------------------------------------------------------
    fig.text(0.04, 0.94, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 2 - Đồng Nai', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.04, 0.96], [0.915, 0.915], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = -0.5, -7.5
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.add_patch(patches.Rectangle((lg_x + 5.5, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 6.6, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 10.5, lg_x + 11.3], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 10.5, lg_x + 11.3], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 11.6, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 15.5, lg_x + 15.5], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 15.5, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 16.5, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Horizontal Corridor (X: 0 to 20, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Stair & Hall Space (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 2 - TÒA ÁN KHU VỰC 2 - ĐỒNG NAI)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # North Wing (Y > 0.9)
        {
            'id': 'P2_A201', 'name': 'A201',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'door': (6.2, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P2_A202', 'name': 'A202',
            'x': 12.5, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (16.25, 3.15),
            'door': (13.0, 0.9, 0.8, 'N_IN_RIGHT')
        },
        # South Wing (Y < -0.9)
        {
            'id': 'P2_A203', 'name': 'A203',
            'x': 0.0, 'y': -4.9, 'w': 5.5, 'h': 4.0,
            'text_center': (2.75, -2.9),
            'door': (4.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P2_A204', 'name': 'A204',
            'x': 5.5, 'y': -4.9, 'w': 5.5, 'h': 4.0,
            'text_center': (8.25, -2.9),
            'door': (9.5, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P2_A205', 'name': 'A205',
            'x': 11.0, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (13.25, -2.9),
            'door': (12.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P2_A206', 'name': 'A206',
            'x': 15.5, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (17.75, -2.9),
            'door': (16.5, -0.9, 0.8, 'S_IN_RIGHT')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHIC (NO OUTDOOR STEPS FOR FLOOR 2)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    gap = 0.35
    flight_w = (stair_w - gap) / 2.0
    left_x1, left_x2 = stair_x, stair_x + flight_w
    right_x1, right_x2 = stair_x + flight_w + gap, stair_x + stair_w

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([left_x1, left_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
        ax.plot([right_x1, right_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_left = left_x1 + flight_w / 2.0
    mid_right = right_x1 + flight_w / 2.0
    ax.plot([mid_left, mid_left], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([mid_right, mid_right], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # Labels for Corridor
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (CLOSED EXTERIOR ENCLOSURE FOR UPPER FLOOR)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Wall
    draw_wall(-W, -4.9 - W, W, 10.3 + 2 * W)

    # Rightmost Vertical Exterior Wall
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2 * W)

    # North Top Wall
    draw_wall(-W, 5.4, 20.0 + 2*W, W)

    # South Bottom Wall
    draw_wall(-W, -4.9 - W, 20.0 + 2*W, W)

    # North Corridor Wall Line (Y = 0.9)
    draw_wall(0, 0.9 - PART_THICKNESS/2, 6.2, PART_THICKNESS)
    draw_wall(7.0, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    draw_wall(12.5, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    draw_wall(13.8, 0.9 - PART_THICKNESS/2, 6.2, PART_THICKNESS)

    # South Corridor Wall Line (Y = -0.9) with door cutouts:
    # Doors at: 4.0, 9.5, 12.0, 16.5
    draw_wall(0, -0.9 - PART_THICKNESS/2, 4.0, PART_THICKNESS)
    draw_wall(4.8, -0.9 - PART_THICKNESS/2, 4.7, PART_THICKNESS)
    draw_wall(10.3, -0.9 - PART_THICKNESS/2, 1.7, PART_THICKNESS)
    draw_wall(12.8, -0.9 - PART_THICKNESS/2, 3.7, PART_THICKNESS)
    draw_wall(17.3, -0.9 - PART_THICKNESS/2, 2.7, PART_THICKNESS)

    # Internal Vertical Partitions
    draw_wall(7.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)   # North A201 & Stair hall
    draw_wall(12.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)  # North Stair hall & A202

    draw_wall(5.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)  # South A203 & A204
    draw_wall(11.0 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0) # South A204 & A205
    draw_wall(15.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0) # South A205 & A206

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

    # Top Windows (North Facade)
    draw_window(2.5, 5.4, 2.5, W, is_horizontal=True)    # A201
    draw_window(9.0, 5.4, 2.0, W, is_horizontal=True)    # Stair Hall
    draw_window(15.0, 5.4, 2.5, W, is_horizontal=True)   # A202

    # Bottom Windows (South Front Facade)
    draw_window(1.8, -4.9 - W, 2.0, W, is_horizontal=True)  # A203
    draw_window(7.2, -4.9 - W, 2.0, W, is_horizontal=True)  # A204
    draw_window(12.2, -4.9 - W, 2.0, W, is_horizontal=True) # A205
    draw_window(16.7, -4.9 - W, 2.0, W, is_horizontal=True) # A206

    # Corridor End Windows
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(20.0, -0.6, W, 1.2, is_horizontal=False)

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode == 'N_IN_RIGHT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_RIGHT':
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)

    for r in rooms:
        dx, dy, dsize, dmode = r['door']
        draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=10.0, 
                fontweight='bold', ha='center', va='center', zorder=15)

    ax.set_xlim(-2.5, 22.5)
    ax.set_ylim(-7.5, 8.0)

    out_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\DongNai\DongNai2\Tang2"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mat_bang_tang_2.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 2 đã xuất thành công tại: {out_path}")

if __name__ == "__main__":
    create_floorplan_tang2()
