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

def create_floorplan_tang1():
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
    COLOR_STAIR_FILL = '#eef4f7'    # Stair fill matches lobby fill for Tang 1

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Exact format per spec)
    fig.text(0.04, 0.94, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 10 - An Giang', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (OPEN EXITS)
    # ---------------------------------------------------------
    # Horizontal Corridor (X: 0 to 20, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Front Main Lobby Space (X: 7.5 to 12.5, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((7.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Stair & Passage Hall Space (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (12 ROOMS ACCORDING TO SURVEY)
    # ---------------------------------------------------------
    # North West Wing (X: 0.0 -> 7.5, Y: 0.9 -> 5.4, H = 4.5)
    # Sum of widths (6+5+5=16): P1=2.8125, P2=2.34375, P3=2.34375
    # North East Wing (X: 12.5 -> 20.0, Y: 0.9 -> 5.4, H = 4.5)
    # Sum of widths (5+5+6=16): P4=2.34375, P5=2.34375, P6=2.8125
    # South West Wing (X: 0.0 -> 7.5, Y: -4.9 -> -0.9, H = 4.0)
    # Sum of widths (6+6+5=17): P7=2.647, P8=2.647, P9=2.206
    # South East Wing (X: 12.5 -> 20.0, Y: -4.9 -> -0.9, H = 4.0)
    # Sum of widths (5+5+5=15): P10=2.5, P11=2.5, P12=2.5

    nw_w1, nw_w2, nw_w3 = 2.8125, 2.34375, 2.34375
    ne_w4, ne_w5, ne_w6 = 2.34375, 2.34375, 2.8125
    sw_w7, sw_w8, sw_w9 = 2.647, 2.647, 2.206
    se_w10, se_w11, se_w12 = 2.5, 2.5, 2.5

    rooms: List[RoomDict] = [
        # North Wing (Y > 0.9)
        {
            'id': 'P1', 'name': 'Phòng 1',
            'x': 0.0, 'y': 0.9, 'w': nw_w1, 'h': 4.5,
            'text_center': (nw_w1 / 2.0, 3.15),
            'door': (0.3, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P2', 'name': 'Phòng 2',
            'x': nw_w1, 'y': 0.9, 'w': nw_w2, 'h': 4.5,
            'text_center': (nw_w1 + nw_w2 / 2.0, 3.15),
            'door': (nw_w1 + 0.3, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P3', 'name': 'Phòng 3',
            'x': nw_w1 + nw_w2, 'y': 0.9, 'w': nw_w3, 'h': 4.5,
            'text_center': (nw_w1 + nw_w2 + nw_w3 / 2.0, 3.15),
            'door': (nw_w1 + nw_w2 + 0.3, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P4', 'name': 'Phòng 4',
            'x': 12.5, 'y': 0.9, 'w': ne_w4, 'h': 4.5,
            'text_center': (12.5 + ne_w4 / 2.0, 3.15),
            'door': (12.8, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P5', 'name': 'Phòng 5',
            'x': 12.5 + ne_w4, 'y': 0.9, 'w': ne_w5, 'h': 4.5,
            'text_center': (12.5 + ne_w4 + ne_w5 / 2.0, 3.15),
            'door': (12.5 + ne_w4 + 0.3, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P6', 'name': 'Phòng 6',
            'x': 12.5 + ne_w4 + ne_w5, 'y': 0.9, 'w': ne_w6, 'h': 4.5,
            'text_center': (12.5 + ne_w4 + ne_w5 + ne_w6 / 2.0, 3.15),
            'door': (12.5 + ne_w4 + ne_w5 + 0.3, 0.9, 0.8, 'N_IN_RIGHT')
        },
        # South Wing (Y < -0.9)
        {
            'id': 'P7', 'name': 'Phòng 7',
            'x': 0.0, 'y': -4.9, 'w': sw_w7, 'h': 4.0,
            'text_center': (sw_w7 / 2.0, -2.9),
            'door': (0.3, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P8', 'name': 'Phòng 8',
            'x': sw_w7, 'y': -4.9, 'w': sw_w8, 'h': 4.0,
            'text_center': (sw_w7 + sw_w8 / 2.0, -2.9),
            'door': (sw_w7 + 0.3, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P9', 'name': 'Phòng 9',
            'x': sw_w7 + sw_w8, 'y': -4.9, 'w': sw_w9, 'h': 4.0,
            'text_center': (sw_w7 + sw_w8 + sw_w9 / 2.0, -2.9),
            'door': (sw_w7 + sw_w8 + 0.3, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P10', 'name': 'Phòng 10',
            'x': 12.5, 'y': -4.9, 'w': se_w10, 'h': 4.0,
            'text_center': (12.5 + se_w10 / 2.0, -2.9),
            'door': (12.8, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P11', 'name': 'Phòng 11',
            'x': 12.5 + se_w10, 'y': -4.9, 'w': se_w11, 'h': 4.0,
            'text_center': (12.5 + se_w10 + se_w11 / 2.0, -2.9),
            'door': (12.5 + se_w10 + 0.3, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P12', 'name': 'Phòng 12',
            'x': 12.5 + se_w10 + se_w11, 'y': -4.9, 'w': se_w12, 'h': 4.0,
            'text_center': (12.5 + se_w10 + se_w11 + se_w12 / 2.0, -2.9),
            'door': (12.5 + se_w10 + se_w11 + 0.3, -0.9, 0.8, 'S_IN_RIGHT')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS (FLOOR 1 SPECIFIC)
    # ---------------------------------------------------------
    # Central Staircase inside North Hall (Background matches sảnh fill COLOR_FILL_CORRIDOR)
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Vertical line down center starting from step 2 down to bottom
    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Staircase label underneath box
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # 1. Front Main Entrance Steps at Bottom (South: Y = -4.9 to -5.7)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # 2. Rear Exit Steps at Top (North: Y = 5.4 to 6.2)
    for sy in [5.4, 5.56, 5.72, 5.88, 6.04, 6.20]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Outdoor Side Steps at Corridor Ends (East & West Exits)
    for i in range(5):
        dx = -0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    for i in range(5):
        dx = 20.0 + 0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([20.0, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([20.0, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Labels for Lobby and Corridor
    ax.text(10.0, -2.9, 'SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (EXTERIOR & INTERIOR PARTITIONS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Walls (SPLIT TO LEAVE CORRIDOR Y: -0.9 TO 0.9 UNBLOCKED!)
    draw_wall(-W, -4.9 - W, W, 4.0 + W)  # Bottom-left segment (Y: -4.9-W to -0.9)
    draw_wall(-W, 0.9, W, 4.5 + W)       # Top-left segment (Y: 0.9 to 5.4+W)

    # Rightmost Vertical Exterior Walls (SPLIT TO LEAVE CORRIDOR Y: -0.9 TO 0.9 UNBLOCKED!)
    draw_wall(20.0, -4.9 - W, W, 4.0 + W) # Bottom-right segment (Y: -4.9-W to -0.9)
    draw_wall(20.0, 0.9, W, 4.5 + W)      # Top-right segment (Y: 0.9 to 5.4+W)

    # North Top Wall (with opening for rear exit to trial building at X: 7.5 to 12.5)
    draw_wall(-W, 5.4, 7.5 + W + PART_THICKNESS/2, W)
    draw_wall(12.5 - PART_THICKNESS/2, 5.4, 7.5 + W + PART_THICKNESS/2, W)

    # South Bottom Wall (with opening for main front entrance at X: 7.5 to 12.5)
    draw_wall(-W, -4.9 - W, 7.5 + W + PART_THICKNESS/2, W)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9 - W, 7.5 + W + PART_THICKNESS/2, W)

    # STRUCTURAL WALL CHEEKS & HOOKS (PER TẦNG 1 SPEC)
    # South Front Entrance Side Wall Cheeks (Y: -4.9 down to -5.7)
    draw_wall(7.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)
    draw_wall(12.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)

    # North Rear Exit Side Wall Cheeks (Y: 5.4 up to 6.2) & Top Inward Hooks
    draw_wall(7.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)
    draw_wall(12.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)
    # Top Inward Hooks at Y = 6.2
    draw_wall(7.5 - PART_THICKNESS/2, 6.2 - PART_THICKNESS, 0.5, PART_THICKNESS)
    draw_wall(12.5 + PART_THICKNESS/2 - 0.5, 6.2 - PART_THICKNESS, 0.5, PART_THICKNESS)

    # Draw Corridor Walls with Door Openings
    # North Corridor Wall Line (Y = 0.9)
    # Left segment: 0.0 to 7.5 (Doors at: 0.3-1.1, nw_w1+0.3 to nw_w1+1.1, nw_w1+nw_w2+0.3 to nw_w1+nw_w2+1.1)
    def draw_h_wall_with_doors(y_center, x_start, x_end, door_spans):
        # door_spans is list of (d_start, d_end)
        cur_x = x_start
        for ds, de in sorted(door_spans):
            if ds > cur_x:
                draw_wall(cur_x, y_center - PART_THICKNESS/2, ds - cur_x, PART_THICKNESS)
            cur_x = max(cur_x, de)
        if cur_x < x_end:
            draw_wall(cur_x, y_center - PART_THICKNESS/2, x_end - cur_x, PART_THICKNESS)

    # North corridor wall segments with doors:
    n_doors_left = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == 0.9 and r['x'] < 7.5]
    draw_h_wall_with_doors(0.9, 0.0, 7.5, n_doors_left)

    n_doors_right = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == 0.9 and r['x'] >= 12.5]
    draw_h_wall_with_doors(0.9, 12.5, 20.0, n_doors_right)

    # South corridor wall segments with doors:
    s_doors_left = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == -4.9 and r['x'] < 7.5]
    draw_h_wall_with_doors(-0.9, 0.0, 7.5, s_doors_left)

    s_doors_right = [(r['door'][0], r['door'][0] + r['door'][2]) for r in rooms if r['y'] == -4.9 and r['x'] >= 12.5]
    draw_h_wall_with_doors(-0.9, 12.5, 20.0, s_doors_right)

    # Internal Vertical Partitions
    # Stair Hall & Lobby side partitions
    draw_wall(7.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)   # NW & Stair hall
    draw_wall(12.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)  # Stair hall & NE
    draw_wall(7.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)  # SW & Front Lobby
    draw_wall(12.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0) # Front Lobby & SE

    # North West room partitions
    draw_wall(nw_w1 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(nw_w1 + nw_w2 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    # North East room partitions
    draw_wall(12.5 + ne_w4 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(12.5 + ne_w4 + ne_w5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    # South West room partitions
    draw_wall(sw_w7 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(sw_w7 + sw_w8 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

    # South East room partitions
    draw_wall(12.5 + se_w10 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(12.5 + se_w10 + se_w11 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

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

    # Draw a window for each room on exterior wall
    for r in rooms:
        if r['y'] == 0.9: # North room -> window on North exterior wall (Y = 5.4)
            win_w = min(1.4, r['w'] * 0.5)
            win_x = r['x'] + (r['w'] - win_w) / 2.0
            draw_window(win_x, 5.4, win_w, W, is_horizontal=True)
        elif r['y'] == -4.9: # South room -> window on South exterior wall (Y = -4.9 - W)
            win_w = min(1.4, r['w'] * 0.5)
            win_x = r['x'] + (r['w'] - win_w) / 2.0
            draw_window(win_x, -4.9 - W, win_w, W, is_horizontal=True)

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
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 22.0)
    ax.set_ylim(-8.5, 8.5)

    # Output directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(script_dir, "mat_bang_tang_1.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 1 floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang1()
