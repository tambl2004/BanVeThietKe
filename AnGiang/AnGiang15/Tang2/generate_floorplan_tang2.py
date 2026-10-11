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
    # 1. SETUP CANVAS & CANVAS STYLING (FLOOR 2)
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(22, 12), dpi=300)
    ax = fig.add_axes([0.03, 0.08, 0.94, 0.82])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & FOOTER
    # ---------------------------------------------------------
    # Header Title
    fig.text(0.04, 0.94, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 15 - An Giang', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.04, 0.96], [0.915, 0.915], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = 0.0, -8.8
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 6.0, lg_y + 0.1), 0.8, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 7.1, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 12.0, lg_x + 12.8], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 12.0, lg_x + 12.8], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 13.1, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR BACKGROUND FILL (FLOOR 2: ENCLOSED CORRIDOR)
    # ---------------------------------------------------------
    # Main Horizontal Corridor (X: 0 to 25, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 25.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Stair Hall Passage (X: 10.0 to 15.0, Y: 0.9 to 4.4)
    ax.add_patch(patches.Rectangle((10.0, 0.9), 5.0, 3.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 2 AN GIANG 15 - ALL LABELED "Phòng")
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- LEFT WING (CÁNH TRÁI - X: 0.0 to 5.0) ---
        {
            'id': 'P2_12', 'name': 'Phòng',
            'x': 0.0, 'y': 0.9, 'w': 5.0, 'h': 5.3,
            'text_center': (2.5, 3.55),
            'door': (2.0, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P2_13', 'name': 'Phòng',
            'x': 0.0, 'y': -6.2, 'w': 5.0, 'h': 5.3,
            'text_center': (2.5, -3.55),
            'door': (2.0, -0.9, 0.8, 'S_IN_RIGHT')
        },

        # --- MIDDLE SECTION NORTH (THÂN GIỮA BẮC - Y: 0.9 to 4.4) ---
        {
            'id': 'P2_14', 'name': 'Phòng',
            'x': 5.0, 'y': 0.9, 'w': 2.5, 'h': 3.5,
            'text_center': (6.25, 2.65),
            'door': (5.3, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P2_15', 'name': 'Phòng',
            'x': 7.5, 'y': 0.9, 'w': 2.5, 'h': 3.5,
            'text_center': (8.75, 2.65),
            'door': (7.8, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P2_16', 'name': 'Phòng',
            'x': 15.0, 'y': 0.9, 'w': 2.5, 'h': 3.5,
            'text_center': (16.25, 2.65),
            'door': (15.3, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P2_17', 'name': 'Phòng',
            'x': 17.5, 'y': 0.9, 'w': 2.5, 'h': 3.5,
            'text_center': (18.75, 2.65),
            'door': (17.8, 0.9, 0.8, 'N_IN_RIGHT')
        },

        # --- MIDDLE SECTION SOUTH (THÂN GIỮA NAM - Y: -4.4 to -0.9) ---
        {
            'id': 'P2_18', 'name': 'Phòng',
            'x': 5.0, 'y': -4.4, 'w': 2.5, 'h': 3.5,
            'text_center': (6.25, -2.65),
            'door': (5.3, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P2_19', 'name': 'Phòng',
            'x': 7.5, 'y': -4.4, 'w': 5.0, 'h': 3.5,
            'text_center': (10.0, -2.65),
            'door': (8.3, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P2_20', 'name': 'Phòng',
            'x': 12.5, 'y': -4.4, 'w': 5.0, 'h': 3.5,
            'text_center': (15.0, -2.65),
            'door': (13.3, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P2_21', 'name': 'Phòng',
            'x': 17.5, 'y': -4.4, 'w': 2.5, 'h': 3.5,
            'text_center': (18.75, -2.65),
            'door': (17.8, -0.9, 0.8, 'S_IN_RIGHT')
        },

        # --- RIGHT WING (CÁNH PHẢI - X: 20.0 to 25.0) ---
        {
            'id': 'P2_22_N', 'name': 'Phòng',
            'x': 20.0, 'y': 0.9, 'w': 5.0, 'h': 5.3,
            'text_center': (22.5, 3.55),
            'door': (22.0, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P2_22_S', 'name': 'Phòng',
            'x': 20.0, 'y': -6.2, 'w': 5.0, 'h': 5.3,
            'text_center': (22.5, -3.55),
            'door': (22.0, -0.9, 0.8, 'S_IN_RIGHT')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES (FLOOR 2: WHITE BACKGROUND `#ffffff`)
    # ---------------------------------------------------------
    # Central Main Staircase (North Passage: X: 11.2 to 13.8, Y: 1.4 to 4.2)
    stair_x, stair_y, stair_w, stair_h = 11.2, 1.4, 2.6, 2.8
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Full vertical dividing line for Floor 2 staircase
    mid_x = stair_x + stair_w / 2.0
    ax.plot([mid_x, mid_x], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.0, ha='center', va='top', zorder=5)

    # Corridor Label
    ax.text(5.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(20.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (ENCLOSED FLOOR 2 FAÇADE)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Wall (ENCLOSED AT CORRIDOR END WITH WINDOW!)
    draw_wall(-W, -6.2 - W, W, 12.4 + 2*W)

    # Rightmost Vertical Exterior Wall (ENCLOSED AT CORRIDOR END WITH WINDOW!)
    draw_wall(25.0, -6.2 - W, W, 12.4 + 2*W)

    # North Exterior Walls
    draw_wall(-W, 6.2, 5.0 + W, W)                             # Left Wing top wall
    draw_wall(5.0 - P/2, 4.4, P, 1.8 + W)                     # Left Wing inner North vertical wall
    draw_wall(5.0, 4.4, 5.0 + P/2, W)                         # Mid-left North wall
    draw_wall(10.0 - P/2, 4.4, P, 0.5 + W)                    # Passage North-West vertical wall
    draw_wall(10.0, 4.4 + 0.5, 5.0, W)                        # Passage North top wall
    draw_wall(15.0 - P/2, 4.4, P, 0.5 + W)                    # Passage North-East vertical wall
    draw_wall(15.0, 4.4, 5.0 + P/2, W)                        # Mid-right North wall
    draw_wall(20.0 - P/2, 4.4, P, 1.8 + W)                    # Right Wing inner North vertical wall
    draw_wall(20.0, 6.2, 5.0 + W, W)                            # Right Wing top wall

    # South Exterior Walls (ENCLOSED AT Y = -4.4 FOR MID SECTION)
    draw_wall(-W, -6.2 - W, 5.0 + W, W)                        # Left Wing bottom wall
    draw_wall(5.0 - P/2, -6.2 - W, P, 1.8 + W)                 # Left Wing inner South vertical wall
    draw_wall(5.0, -4.4 - W, 15.0 + P, W)                      # Mid-section continuous South wall
    draw_wall(20.0 - P/2, -6.2 - W, P, 1.8 + W)                # Right Wing inner South vertical wall
    draw_wall(20.0, -6.2 - W, 5.0 + W, W)                      # Right Wing bottom wall

    # ---------------------------------------------------------
    # CORRIDOR HORIZONTAL PARTITION WALLS & EXACT DOOR CUTOUTS
    # ---------------------------------------------------------
    # North Corridor Wall Line (Y = 0.9)
    draw_wall(0.0, 0.9 - P/2, 2.0, P)
    draw_wall(2.8, 0.9 - P/2, 2.2, P)
    draw_wall(5.0, 0.9 - P/2, 0.3, P)
    draw_wall(6.1, 0.9 - P/2, 1.7, P)
    draw_wall(8.6, 0.9 - P/2, 1.4, P)
    draw_wall(10.0, 0.9 - P/2, 1.2, P)
    draw_wall(13.8, 0.9 - P/2, 1.2, P)
    draw_wall(15.0, 0.9 - P/2, 0.3, P)
    draw_wall(16.1, 0.9 - P/2, 1.7, P)
    draw_wall(18.6, 0.9 - P/2, 1.4, P)
    draw_wall(20.0, 0.9 - P/2, 2.0, P)
    draw_wall(22.8, 0.9 - P/2, 2.2, P)

    # South Corridor Wall Line (Y = -0.9)
    draw_wall(0.0, -0.9 - P/2, 2.0, P)
    draw_wall(2.8, -0.9 - P/2, 2.2, P)
    draw_wall(5.0, -0.9 - P/2, 0.3, P)
    draw_wall(6.1, -0.9 - P/2, 2.2, P)
    draw_wall(9.1, -0.9 - P/2, 0.9, P)
    draw_wall(10.0, -0.9 - P/2, 3.3, P)
    draw_wall(14.1, -0.9 - P/2, 0.9, P)
    draw_wall(15.0, -0.9 - P/2, 2.8, P)
    draw_wall(18.6, -0.9 - P/2, 1.4, P)
    draw_wall(20.0, -0.9 - P/2, 2.0, P)
    draw_wall(22.8, -0.9 - P/2, 2.2, P)

    # Internal Vertical Partition Walls
    draw_wall(5.0 - P/2, -4.4, P, 3.5)   # Mid-left South Wing edge
    draw_wall(5.0 - P/2, 0.9, P, 3.5)    # Mid-left North Wing edge
    draw_wall(7.5 - P/2, 0.9, P, 3.5)    # P2_14 / P2_15
    draw_wall(7.5 - P/2, -4.4, P, 3.5)   # P2_18 / P2_19
    draw_wall(10.0 - P/2, 0.9, P, 3.5)   # P2_15 / Passage
    draw_wall(12.5 - P/2, -4.4, P, 3.5)  # P2_19 / P2_20
    draw_wall(15.0 - P/2, 0.9, P, 3.5)   # Passage / P2_16
    draw_wall(17.5 - P/2, 0.9, P, 3.5)   # P2_16 / P2_17
    draw_wall(17.5 - P/2, -4.4, P, 3.5)  # P2_20 / P2_21
    draw_wall(20.0 - P/2, 0.9, P, 3.5)   # Mid-right North Wing edge
    draw_wall(20.0 - P/2, -6.2, P, 5.3)  # Mid-right South Wing edge

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

    # Windows on North Facade
    draw_window(1.5, 6.2, 2.0, W, is_horizontal=True)    # P2_12 top window
    draw_window(5.7, 4.4, 1.2, W, is_horizontal=True)    # P2_14 top window
    draw_window(8.2, 4.4, 1.2, W, is_horizontal=True)    # P2_15 top window
    draw_window(11.5, 4.9, 2.0, W, is_horizontal=True)   # Staircase North window
    draw_window(15.7, 4.4, 1.2, W, is_horizontal=True)   # P2_16 top window
    draw_window(18.2, 4.4, 1.2, W, is_horizontal=True)   # P2_17 top window
    draw_window(21.5, 6.2, 2.0, W, is_horizontal=True)   # P2_22_N top window

    # Windows on South Facade
    draw_window(1.5, -6.2 - W, 2.0, W, is_horizontal=True) # P2_13 bottom window
    draw_window(5.7, -4.4 - W, 1.2, W, is_horizontal=True) # P2_18 bottom window
    draw_window(9.0, -4.4 - W, 2.0, W, is_horizontal=True) # P2_19 bottom window
    draw_window(13.5, -4.4 - W, 2.0, W, is_horizontal=True)# P2_20 bottom window
    draw_window(18.2, -4.4 - W, 1.2, W, is_horizontal=True)# P2_21 bottom window
    draw_window(21.5, -6.2 - W, 2.0, W, is_horizontal=True)# P2_22_S bottom window

    # Windows on East & West Outer Corridor Ends (Floor 2 Enclosed End Windows!)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)     # West Corridor End Window
    draw_window(25.0, -0.6, W, 1.2, is_horizontal=False)    # East Corridor End Window

    # Windows on East & West Outer Wing Walls
    draw_window(-W, 3.0, W, 1.5, is_horizontal=False)      # Left Wing North West window
    draw_window(-W, -4.5, W, 1.5, is_horizontal=False)     # Left Wing South West window
    draw_window(25.0, 3.0, W, 1.5, is_horizontal=False)    # Right Wing North East window
    draw_window(25.0, -4.5, W, 1.5, is_horizontal=False)   # Right Wing South East window

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
    # 9. DRAW ROOM LABELS (ALL LABELED "Phòng")
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.5, 27.5)
    ax.set_ylim(-9.5, 9.0)

    # Save output PNG in target directory
    out_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\AnGiang\AnGiang15\Tang2"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mat_bang_tang_2.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 2 floorplan PNG for AnGiang15 at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang2()
