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
    fig = plt.figure(figsize=(26, 15), dpi=300)
    ax = fig.add_axes([0.02, 0.05, 0.96, 0.88])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_ROOF_FILL = '#f1f5f9'     # Soft pastel grey for roof blocks (Mái che)
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#ffffff'    # Pure white stair fill for upper floors

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Exact format per spec, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 12 - An Giang', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = -0.5, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 7.5, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 8.6, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 15.0, lg_x + 15.8], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 15.0, lg_x + 15.8], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 16.1, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Roof (Mái che)
    ax.add_patch(patches.Rectangle((lg_x + 22.0, lg_y), 0.8, 0.3, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_WALL, linewidth=0.8, zorder=1))
    ax.text(lg_x + 23.1, lg_y + 0.05, 'Mái che', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (TÒA 1 ACTIVE FLOOR 2)
    # ---------------------------------------------------------
    # TÒA 1: Front Main Building Corridor (X: 0 to 27.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 27.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # TÒA 1: Rear Stair & Passage Space (X: 11.0 to 16.0, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((11.0, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOF BLOCKS FOR 1-STORY BUILDINGS (TÒA 2 & TÒA 3)
    # ---------------------------------------------------------
    # TÒA 2 (Rear Courtroom Roof Block): X: 3.5 to 23.5, Y: 6.2 to 13.2
    ax.add_patch(patches.Rectangle((3.5, 6.2), 20.0, 7.0, facecolor=COLOR_ROOF_FILL, edgecolor='none', zorder=2))
    ax.text(13.5, 9.7, 'MÁI CHE', color=COLOR_TEXT_MUTED, fontsize=13.0, fontweight='bold', ha='center', va='center', zorder=5)

    # TÒA 3 (Side Building Roof Block): X: 29.5 to 37.5, Y: -4.9 to 5.4
    ax.add_patch(patches.Rectangle((29.5, -4.9), 8.0, 10.3, facecolor=COLOR_ROOF_FILL, edgecolor='none', zorder=2))
    ax.text(33.5, 0.25, 'MÁI CHE', color=COLOR_TEXT_MUTED, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 5. ROOM DEFINITIONS (TÒA 1 FLOOR 2 ROOMS)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # North-West Wing (Y: 0.9 to 5.4)
        {
            'id': 'P10', 'name': 'Phòng làm việc 10',
            'x': 0.0, 'y': 0.9, 'w': 11.0, 'h': 4.5,
            'text_center': (5.5, 3.15),
            'door': (9.5, 0.9, 0.8, 'N_IN_RIGHT')
        },
        # South-West Wing (Y: -4.9 to -0.9)
        {
            'id': 'P11', 'name': 'Phòng làm việc 11',
            'x': 0.0, 'y': -4.9, 'w': 11.0, 'h': 4.0,
            'text_center': (5.5, -2.9),
            'door': (9.5, -0.9, 0.8, 'S_IN_RIGHT')
        },
        # Center-South Room (Replaces South Front Lobby on Floor 2 per Spec)
        {
            'id': 'P_CS', 'name': 'Phòng làm việc',
            'x': 11.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (13.5, -2.9),
            'door': (14.5, -0.9, 0.8, 'S_IN_RIGHT')
        },
        # North-East Wing (Y: 0.9 to 5.4)
        {
            'id': 'P12', 'name': 'Phòng làm việc 12',
            'x': 16.0, 'y': 0.9, 'w': 11.0, 'h': 4.5,
            'text_center': (21.5, 3.15),
            'door': (16.7, 0.9, 0.8, 'N_IN_RIGHT')
        },
        # South-East Wing (Y: -4.9 to -0.9)
        {
            'id': 'P13', 'name': 'Phòng làm việc 13',
            'x': 16.0, 'y': -4.9, 'w': 11.0, 'h': 4.0,
            'text_center': (21.5, -2.9),
            'door': (16.7, -0.9, 0.8, 'S_IN_RIGHT')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 6. STAIRCASE GRAPHIC FOR FLOOR 2 (PURE WHITE FILL & 2 FLIGHTS)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 12.2, 1.4, 2.6, 2.6
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

    # Staircase label cleanly positioned in open stair hall
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.25, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # Labels for Corridor
    ax.text(5.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(21.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 7. DRAW WALLS FOR ALL 3 BUILDINGS (STAIR HALL ENTRANCE UNBLOCKED)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # --- TÒA 1 EXTERIOR WALLS (FULL CLOSED BOUNDARY ON FLOOR 2) ---
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)                     # West outer wall (Continuous)
    draw_wall(27.0, -4.9 - W, W, 10.3 + 2*W)                    # East outer wall (Continuous)
    draw_wall(-W, 5.4, 27.0 + 2*W, W)                          # North outer wall (Continuous)
    draw_wall(-W, -4.9 - W, 27.0 + 2*W, W)                     # South outer wall (Continuous)

    # --- TÒA 2 ROOF CONTOUR WALLS ---
    draw_wall(3.5 - W, 6.2 - W, W, 7.0 + 2*W)                  # West outer wall
    draw_wall(23.5, 6.2 - W, W, 7.0 + 2*W)                     # East outer wall
    draw_wall(3.5 - W, 13.2, 20.0 + 2*W, W)                   # North outer wall
    draw_wall(3.5 - W, 6.2 - W, 20.0 + 2*W, W)                # South outer wall

    # --- TÒA 3 ROOF CONTOUR WALLS ---
    draw_wall(29.5 - W, -4.9 - W, W, 10.3 + 2*W)              # West outer wall
    draw_wall(37.5, -4.9 - W, W, 10.3 + 2*W)                  # East outer wall
    draw_wall(29.5 - W, 5.4, 8.0 + 2*W, W)                    # North outer wall
    draw_wall(29.5 - W, -4.9 - W, 8.0 + 2*W, W)                # South outer wall

    # --- TÒA 1 CORRIDOR WALL LINES & PARTITIONS ---
    def draw_h_wall_with_doors(y_center, x_start, x_end, door_spans):
        cur_x = x_start
        for ds, de in sorted(door_spans):
            if ds > cur_x:
                draw_wall(cur_x, y_center - PART_THICKNESS/2, ds - cur_x, PART_THICKNESS)
            cur_x = max(cur_x, de)
        if cur_x < x_end:
            draw_wall(cur_x, y_center - PART_THICKNESS/2, x_end - cur_x, PART_THICKNESS)

    # Tòa 1 North Corridor Wall (Y = 0.9): UNBLOCKED BETWEEN X = 11.0 AND 16.0 FOR STAIR HALL!
    n_doors = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == 0.9]
    draw_h_wall_with_doors(0.9, 0.0, 11.0, [d for d in n_doors if d[0] < 11.0])
    # X: 11.0 to 16.0 is 100% OPEN (NO WALL BLOCKING STAIR HALL ENTRANCE!)
    draw_h_wall_with_doors(0.9, 16.0, 27.0, [d for d in n_doors if d[0] >= 16.0])

    # Tòa 1 South Corridor Wall (Y = -0.9)
    s_doors = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == -4.9]
    draw_h_wall_with_doors(-0.9, 0.0, 27.0, s_doors)

    # Tòa 1 Vertical Partitions
    draw_wall(11.0 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)  # NW & Stair hall
    draw_wall(16.0 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)  # Stair hall & NE
    draw_wall(11.0 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0) # SW & Center-South room
    draw_wall(16.0 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)# Center-South room & SE

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

    # Tòa 1 North Windows (Y = 5.4)
    draw_window(4.0, 5.4, 3.0, W, is_horizontal=True)             # P10 window
    draw_window(12.25, 5.4, 2.5, W, is_horizontal=True)           # Rear stair hall window
    draw_window(20.0, 5.4, 3.0, W, is_horizontal=True)            # P12 window

    # Tòa 1 South Windows (Y = -4.9 - W)
    draw_window(4.0, -4.9 - W, 3.0, W, is_horizontal=True)        # P11 window
    draw_window(12.25, -4.9 - W, 2.5, W, is_horizontal=True)      # Center-South room window
    draw_window(20.0, -4.9 - W, 3.0, W, is_horizontal=True)       # P13 window

    # Corridor End Windows (West & East Facades on Floor 2)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(27.0, -0.6, W, 1.2, is_horizontal=False)

    # ---------------------------------------------------------
    # 9. DRAW DOORS & SWINGS
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
    # 10. DRAW ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 40.0)
    ax.set_ylim(-8.5, 15.0)

    # Output directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(script_dir, "mat_bang_tang_2.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 2 floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang2()
