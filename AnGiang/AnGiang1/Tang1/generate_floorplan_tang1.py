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

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & FOOTER
    # ---------------------------------------------------------
    # Header Title (Including Building Name, NO Subtitle line)
    fig.text(0.04, 0.94, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 1 - An Giang', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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
    # 4. ROOM DEFINITIONS (ALL 10 ROOMS FILLED SEAMLESSLY)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- NORTH WING (Y > 0.9) ---
        {
            # Phòng Phó chánh án (7,8 × 3,6 m)
            'id': 'P1_1', 'name': 'Phòng\nPhó chánh án',
            'x': 0.0, 'y': 0.9, 'w': 4.1, 'h': 4.5,
            'text_center': (2.05, 3.15),
            'door': (3.1, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            # Phòng nhận đơn khởi kiện (6,0 × 3,6 m)
            'id': 'P1_2', 'name': 'Phòng nhận đơn\nkhởi kiện',
            'x': 4.1, 'y': 0.9, 'w': 3.4, 'h': 4.5,
            'text_center': (5.8, 3.15),
            'door': (4.8, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            # Phòng Hình sự (7,8 × 3,6 m)
            'id': 'P1_3', 'name': 'Phòng\nHình sự',
            'x': 12.5, 'y': 0.9, 'w': 3.5, 'h': 4.5,
            'text_center': (14.25, 3.15),
            'door': (13.2, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            # Phòng Hoà giải đối thoại (7,2 × 3,6 m)
            'id': 'P1_4', 'name': 'Phòng Hoà giải\nđối thoại',
            'x': 16.0, 'y': 0.9, 'w': 2.2, 'h': 4.5,
            'text_center': (17.1, 3.15),
            'door': (16.4, 0.9, 0.7, 'N_IN_RIGHT')
        },
        {
            # Phòng Thẩm phán (3,6 × 3,3 m)
            'id': 'P1_5', 'name': 'Phòng\nThẩm phán',
            'x': 18.2, 'y': 0.9, 'w': 1.8, 'h': 4.5,
            'text_center': (19.1, 3.15),
            'door': (18.4, 0.9, 0.7, 'N_IN_RIGHT')
        },

        # --- SOUTH WING (Y < -0.9) ---
        {
            # Phòng Phó chánh văn phòng (7,8 × 3,3 m)
            'id': 'P1_6', 'name': 'Phòng Phó chánh\nvăn phòng',
            'x': 0.0, 'y': -4.9, 'w': 3.9, 'h': 4.0,
            'text_center': (1.95, -2.9),
            'door': (2.8, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            # Phòng Thẩm phán (4,8 × 3,3 m)
            'id': 'P1_7', 'name': 'Phòng\nThẩm phán',
            'x': 3.9, 'y': -4.9, 'w': 3.6, 'h': 4.0,
            'text_center': (5.7, -2.9),
            'door': (4.6, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            # Phòng Thẩm phán (4,8 × 3,3 m)
            'id': 'P1_8', 'name': 'Phòng\nThẩm phán',
            'x': 12.5, 'y': -4.9, 'w': 2.8, 'h': 4.0,
            'text_center': (13.9, -2.9),
            'door': (13.2, -0.9, 0.7, 'S_IN_RIGHT')
        },
        {
            # Phòng Thẩm phán (3,6 × 3,3 m)
            'id': 'P1_9', 'name': 'Phòng\nThẩm phán',
            'x': 15.3, 'y': -4.9, 'w': 2.35, 'h': 4.0,
            'text_center': (16.475, -2.9),
            'door': (15.7, -0.9, 0.7, 'S_IN_RIGHT')
        },
        {
            # Phòng Văn thư lưu trữ (3,3 × 3,3 m)
            'id': 'P1_10', 'name': 'Phòng\nVăn thư lưu trữ',
            'x': 17.65, 'y': -4.9, 'w': 2.35, 'h': 4.0,
            'text_center': (18.825, -2.9),
            'door': (18.0, -0.9, 0.7, 'S_IN_RIGHT')
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
    # South entrance side cheek lines
    ax.plot([7.5, 7.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([12.5, 12.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # 2. Rear Exit Steps & Passage Walls at Top (North: Y = 5.4 to 6.2)
    for sy in [5.4, 5.56, 5.72, 5.88, 6.04, 6.20]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    # North exit side cheek lines extending upwards
    ax.plot([7.5, 7.5], [5.4, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([12.5, 12.5], [5.4, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)
    # North exit inward wall hooks at top end
    ax.plot([7.5, 8.0], [6.20, 6.20], color=COLOR_WALL, linewidth=1.4, zorder=4)
    ax.plot([12.0, 12.5], [6.20, 6.20], color=COLOR_WALL, linewidth=1.4, zorder=4)

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
    # 6. DRAW WALLS (FLUSH & UNBROKEN PARTITIONS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Walls (SPLIT TO LEAVE CORRIDOR Y: -0.9 TO 0.9 UNBLOCKED!)
    draw_wall(-W, -4.9 - W, W, 4.0 + W)
    draw_wall(-W, 0.9, W, 4.5 + W)

    # Rightmost Vertical Exterior Walls (SPLIT TO LEAVE CORRIDOR Y: -0.9 TO 0.9 UNBLOCKED!)
    draw_wall(20.0, -4.9 - W, W, 4.0 + W)
    draw_wall(20.0, 0.9, W, 4.5 + W)

    # North Top Wall (with opening for rear exit at X: 7.5 to 12.5)
    draw_wall(-W, 5.4, 7.5 + W + PART_THICKNESS/2, W)
    draw_wall(12.5 - PART_THICKNESS/2, 5.4, 7.5 + W + PART_THICKNESS/2, W)

    # South Bottom Wall (with opening for main front entrance at X: 7.5 to 12.5)
    draw_wall(-W, -4.9 - W, 7.5 + W + PART_THICKNESS/2, W)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9 - W, 7.5 + W + PART_THICKNESS/2, W)

    # STRUCTURAL WALL CHEEKS & HOOKS (PER SPEC)
    # South Front Entrance Side Wall Cheeks
    draw_wall(7.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)
    draw_wall(12.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)

    # North Rear Exit Side Wall Cheeks & Hooks
    draw_wall(7.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)
    draw_wall(12.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)
    draw_wall(7.5 - PART_THICKNESS/2, 6.2 - PART_THICKNESS, 0.5, PART_THICKNESS)
    draw_wall(12.5 + PART_THICKNESS/2 - 0.5, 6.2 - PART_THICKNESS, 0.5, PART_THICKNESS)

    # North Corridor Wall Line (Y = 0.9)
    draw_wall(0, 0.9 - PART_THICKNESS/2, 3.1, PART_THICKNESS)
    draw_wall(3.9, 0.9 - PART_THICKNESS/2, 0.9, PART_THICKNESS)
    draw_wall(5.6, 0.9 - PART_THICKNESS/2, 1.9, PART_THICKNESS)
    draw_wall(7.5 - PART_THICKNESS/2, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    draw_wall(12.5, 0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)
    draw_wall(14.0, 0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)
    draw_wall(17.1, 0.9 - PART_THICKNESS/2, 1.3, PART_THICKNESS)
    draw_wall(19.1, 0.9 - PART_THICKNESS/2, 0.9, PART_THICKNESS)

    # South Corridor Wall Line (Y = -0.9)
    draw_wall(0, -0.9 - PART_THICKNESS/2, 2.8, PART_THICKNESS)
    draw_wall(3.6, -0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(5.4, -0.9 - PART_THICKNESS/2, 2.1, PART_THICKNESS)
    draw_wall(12.5, -0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)
    draw_wall(13.9, -0.9 - PART_THICKNESS/2, 1.8, PART_THICKNESS)
    draw_wall(16.4, -0.9 - PART_THICKNESS/2, 1.6, PART_THICKNESS)
    draw_wall(18.7, -0.9 - PART_THICKNESS/2, 1.3, PART_THICKNESS)

    # Internal Vertical Partitions
    # North Wing Partitions
    draw_wall(4.1 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(7.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(12.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(16.0 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(18.2 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    # South Wing Partitions
    draw_wall(3.9 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(7.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(15.3 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(17.65 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

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
    draw_window(1.2, 5.4, 1.8, W, is_horizontal=True)    # P1_1
    draw_window(4.9, 5.4, 1.8, W, is_horizontal=True)    # P1_2
    draw_window(13.3, 5.4, 1.8, W, is_horizontal=True)   # P1_3
    draw_window(16.5, 5.4, 1.2, W, is_horizontal=True)   # P1_4
    draw_window(18.5, 5.4, 1.0, W, is_horizontal=True)   # P1_5

    # Bottom Windows (South Front Facade)
    draw_window(1.1, -4.9 - W, 1.7, W, is_horizontal=True) # P1_6
    draw_window(4.8, -4.9 - W, 1.7, W, is_horizontal=True) # P1_7
    draw_window(13.1, -4.9 - W, 1.6, W, is_horizontal=True)# P1_8
    draw_window(15.8, -4.9 - W, 1.2, W, is_horizontal=True)# P1_9
    draw_window(18.2, -4.9 - W, 1.2, W, is_horizontal=True)# P1_10

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
        font_sz = 7.8 if r['w'] < 2.2 else 8.5
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 22.0)
    ax.set_ylim(-8.5, 8.5)

    # Save output PNG in target folder
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\AnGiang\AnGiang1\Tang1"
    os.makedirs(target_dir, exist_ok=True)
    out_path = os.path.join(target_dir, "mat_bang_tang_1.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 1 floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang1()
