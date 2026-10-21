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
    fig.text(0.04, 0.94, 'MẶT BẰNG TẦNG 2  —  Tòa nhà 3  —  Tòa án nhân dân khu vực 3 - Thanh Hóa', 
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
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (TẦNG 2 MÀU #eef4f7)
    # ---------------------------------------------------------
    # Main Horizontal Corridor (X: 0 to 20, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # South Central Open Lobby Space (X: 7.5 to 12.5, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((7.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # North Rear Stair Hall Space (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TÒA 3 TẦNG 2 - 4 PHÒNG THƯ KÝ)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === DÃY BẮC (North Wing: Y > 0.9m) ===
        # 1. Cánh Tây Bắc: Phòng thư ký (KT: 3x8)
        {
            'id': 'T3_T2_TK1', 'name': 'Phòng thư ký',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'door': (6.0, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 11.5
        },
        # 2. Cánh Đông Bắc: Phòng thư ký (KT: 3x8)
        {
            'id': 'T3_T2_TK2', 'name': 'Phòng thư ký',
            'x': 12.5, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (16.25, 3.15),
            'door': (13.5, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 11.5
        },

        # === DÃY NAM (South Wing: Y < -0.9m) ===
        # 3. Cánh Tây Nam: Phòng thư ký (KT: 3x8)
        {
            'id': 'T3_T2_TK3', 'name': 'Phòng thư ký',
            'x': 0.0, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (3.75, -2.9),
            'door': (6.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 11.5
        },
        # 4. Cánh Đông Nam: Phòng thư ký (KT: 3x8)
        {
            'id': 'T3_T2_TK4', 'name': 'Phòng thư ký',
            'x': 12.5, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (16.25, -2.9),
            'door': (13.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 11.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHIC (UPPER FLOOR SPEC: PURE WHITE BACKGROUND)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
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

    # South Central Open Space Label (Sảnh thoáng / Thông tầng hướng sáng)
    ax.text(10.0, -2.9, 'SẢNH THOÁNG', color=COLOR_TEXT_MAIN, fontsize=11.5, fontweight='bold', ha='center', va='center', zorder=5)

    # Corridor labels
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (ENCLOSED EXTERIOR, NO OUTDOOR STAIRS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Wall (Continuous enclosing corridor West end)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2 * W)

    # Rightmost Vertical Exterior Wall (Continuous enclosing corridor East end)
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2 * W)

    # North Top Wall (Continuous across entire North facade)
    draw_wall(-W, 5.4, 20.0 + 2 * W, W)

    # South Bottom Wall (Continuous across entire South facade)
    draw_wall(-W, -4.9 - W, 20.0 + 2 * W, W)

    # North Corridor Wall Line (Y = 0.9, with door cutouts)
    draw_wall(0.0, 0.9 - P/2, 6.0, P)             # TK1 left wall
    draw_wall(6.85, 0.9 - P/2, 7.5 - 6.85, P)     # TK1 right wall segment
    # Central Hall open from 7.5 to 12.5
    draw_wall(12.5, 0.9 - P/2, 1.0, P)            # TK2 left wall segment (12.5 to 13.5)
    draw_wall(14.35, 0.9 - P/2, 20.0 - 14.35, P)  # TK2 right wall (14.35 to 20.0)

    # South Corridor Wall Line (Y = -0.9, with door cutouts)
    draw_wall(0.0, -0.9 - P/2, 6.0, P)            # TK3 left wall
    draw_wall(6.85, -0.9 - P/2, 7.5 - 6.85, P)    # TK3 right wall segment
    # South Central Sảnh thoáng OPEN from 7.5 to 12.5 (no horizontal partition)
    draw_wall(12.5, -0.9 - P/2, 1.0, P)           # TK4 left wall segment (12.5 to 13.5)
    draw_wall(14.35, -0.9 - P/2, 20.0 - 14.35, P) # TK4 right wall (14.35 to 20.0)

    # Internal Vertical Partitions enclosing 4 corner rooms
    draw_wall(7.5 - P/2, 0.9, P, 4.5)             # West room (TK1) & North Stair hall
    draw_wall(12.5 - P/2, 0.9, P, 4.5)            # North Stair hall & East room (TK2)
    draw_wall(7.5 - P/2, -4.9, P, 4.0)            # West room (TK3) & South Sảnh thoáng
    draw_wall(12.5 - P/2, -4.9, P, 4.0)           # South Sảnh thoáng & East room (TK4)

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

    # Top Windows (North Facade: Y = 5.4)
    draw_window(1.8, 5.4, 2.2, W, is_horizontal=True)     # Phòng thư ký window 1
    draw_window(4.5, 5.4, 2.2, W, is_horizontal=True)     # Phòng thư ký window 2
    draw_window(8.75, 5.4, 2.5, W, is_horizontal=True)    # Rear stair hall window
    draw_window(13.3, 5.4, 2.2, W, is_horizontal=True)    # Phòng thư ký window 1
    draw_window(16.3, 5.4, 2.2, W, is_horizontal=True)    # Phòng thư ký window 2

    # Bottom Windows (South Front Facade: Y = -4.9 - W)
    draw_window(1.8, -4.9 - W, 2.2, W, is_horizontal=True)  # Phòng thư ký window 1
    draw_window(4.5, -4.9 - W, 2.2, W, is_horizontal=True)  # Phòng thư ký window 2
    draw_window(8.75, -4.9 - W, 2.5, W, is_horizontal=True) # Sảnh thoáng front window
    draw_window(13.3, -4.9 - W, 2.2, W, is_horizontal=True) # Phòng thư ký window 1
    draw_window(16.3, -4.9 - W, 2.2, W, is_horizontal=True) # Phòng thư ký window 2

    # Side Windows (West and East Facades)
    draw_window(-W, 2.2, W, 2.0, is_horizontal=False)      # West Facade Upper (TK1)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)     # West Corridor End Window
    draw_window(-W, -3.8, W, 2.0, is_horizontal=False)     # West Facade Lower (TK3)

    draw_window(20.0, 2.2, W, 2.0, is_horizontal=False)    # East Facade Upper (TK2)
    draw_window(20.0, -0.6, W, 1.2, is_horizontal=False)   # East Corridor End Window
    draw_window(20.0, -3.8, W, 2.0, is_horizontal=False)   # East Facade Lower (TK4)

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
    # 9. DRAW ROOM LABELS (FULL ROOM NAME FROM SURVEY DATA)
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 11.5)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 22.0)
    ax.set_ylim(-8.5, 8.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Toa 3 Floor 2 floorplan PNG at {out_img_path}")
    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang2()
