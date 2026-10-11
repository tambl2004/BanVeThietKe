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
    COLOR_STAIR_FILL = '#ffffff'     # Stair fill

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & FOOTER
    # ---------------------------------------------------------
    # Header Title (Including Building Name, NO Subtitle line)
    fig.text(0.04, 0.94, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 11 - Hải Phòng', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Horizontal Corridor (X: 0 to 20, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Stair & Hall Space (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 2 DEMO)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # North Wing (Y > 0.9)
        {
            'id': 'P2_1', 'name': 'Phòng',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'door': (6.2, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P2_2', 'name': 'Phòng',
            'x': 12.5, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (16.25, 3.15),
            'door': (13.0, 0.9, 0.8, 'N_IN_RIGHT')
        },
        # South Wing (Y < -0.9)
        {
            'id': 'P2_3', 'name': 'Phòng',
            'x': 0.0, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (1.875, -2.9),
            'door': (2.4, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P2_4', 'name': 'Phòng',
            'x': 3.75, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (5.625, -2.9),
            'door': (4.5, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P2_7', 'name': 'Phòng',
            'x': 7.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (10.0, -2.9),
            'door': (11.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P2_5', 'name': 'Phòng',
            'x': 12.5, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (14.375, -2.9),
            'door': (13.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P2_6', 'name': 'Phòng',
            'x': 16.25, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (18.125, -2.9),
            'door': (16.8, -0.9, 0.8, 'S_IN_RIGHT')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHIC (NO OUTDOOR STEPS FOR FLOOR 2)
    # ---------------------------------------------------------
    # Central Staircase inside North Hall
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

    # Labels for Corridor
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (UNBLOCKED CORRIDOR EXITS & CLEAN LOBBY CAPS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Wall (Continuous for upper floors to close corridor end)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2 * W)

    # Rightmost Vertical Exterior Wall (Continuous for upper floors to close corridor end)
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2 * W)

    # North Top Wall (Continuous wall across top)
    draw_wall(-W, 5.4, 20.0 + 2*W, W)

    # South Bottom Wall (Continuous wall across bottom)
    draw_wall(-W, -4.9 - W, 20.0 + 2*W, W)

    # North Corridor Wall Line (Y = 0.9)
    draw_wall(0, 0.9 - PART_THICKNESS/2, 6.2, PART_THICKNESS)
    draw_wall(7.0, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    draw_wall(12.5, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    draw_wall(13.8, 0.9 - PART_THICKNESS/2, 6.2, PART_THICKNESS)

    # South Corridor Wall Line (Y = -0.9)
    draw_wall(0, -0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)
    draw_wall(3.2, -0.9 - PART_THICKNESS/2, 1.3, PART_THICKNESS)
    draw_wall(5.3, -0.9 - PART_THICKNESS/2, 5.7, PART_THICKNESS)
    draw_wall(11.8, -0.9 - PART_THICKNESS/2, 1.2, PART_THICKNESS)
    draw_wall(13.8, -0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)
    draw_wall(17.6, -0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)

    # Internal Vertical Partitions
    draw_wall(7.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)   # North West room & Stair hall
    draw_wall(12.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)  # North Stair hall & East room

    draw_wall(3.75 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0) # South P2_3 & P2_4
    draw_wall(7.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)  # South P2_4 & Front Lobby
    draw_wall(12.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0) # South Front Lobby & P2_5
    draw_wall(16.25 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)# South P2_5 & P2_6

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
    draw_window(2.5, 5.4, 2.5, W, is_horizontal=True)    # P2_1
    draw_window(8.75, 5.4, 2.5, W, is_horizontal=True)   # Rear hall window
    draw_window(15.0, 5.4, 2.5, W, is_horizontal=True)   # P2_2

    # Bottom Windows (South Front Facade)
    draw_window(1.0, -4.9 - W, 1.6, W, is_horizontal=True) # P2_3 window
    draw_window(4.8, -4.9 - W, 1.6, W, is_horizontal=True) # P2_4 window
    draw_window(8.75, -4.9 - W, 2.5, W, is_horizontal=True) # Front Portico Balcony Window on Floor 2
    draw_window(13.5, -4.9 - W, 1.6, W, is_horizontal=True) # P2_5 window
    draw_window(17.3, -4.9 - W, 1.6, W, is_horizontal=True) # P2_6 window

    # Corridor End Windows (West & East Facades on Floor 2)
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
    # 9. DRAW ROOM LABELS (ONLY ROOM NAME "Phòng")
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=10.0, ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 22.0)
    ax.set_ylim(-8.5, 8.5)

    # Save output PNG in workspace root
    out_dir = r"c:\Users\Tam\Desktop\BanVeThietKe"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mat_bang_tang_2.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 2 floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang2()
