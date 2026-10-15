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

COURT_NAME = "Tòa án nhân dân khu vực 8 - Đồng Nai"

def create_floorplan_tang1(court_name: str = COURT_NAME):
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 14), dpi=300)
    ax = fig.add_axes([0.02, 0.06, 0.96, 0.86])
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
    X_MAX = 32.0            # Main building length = 32.0m
    Y_TOA2_TOP = 14.5       # Extended rear building height (top Y = 14.5m)

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, f'MẶT BẰNG TẦNG 1  —  {court_name}', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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

    # Legend Item 4: Door
    ax.plot([lg_x + 21.0, lg_x + 21.0], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 21.0, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 22.0, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Main Building Horizontal Corridor (X: 0 to 32.0, Y: -0.9 to 0.9) running continuously
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Front Main Lobby Space (X: 13.5 to 18.5, Y: -5.7 to -0.9)
    ax.add_patch(patches.Rectangle((13.5, -5.7), 5.0, 4.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Connecting Lobby Passage leading to Tòa 2 (X: 13.5 to 18.5, Y: 0.9 to 14.5)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, Y_TOA2_TOP - 0.9, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TÒA ÁN KHU VỰC 8 - ĐỒNG NAI: TẦNG 1)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA 1 (CHÍNH PHÍA NAM - 4 PHÒNG HÀNH CHÍNH) ===
        # --- North-West Wing (Y: 0.9 to 5.4m) ---
        {
            'id': 'P1_VP', 'name': 'Văn phòng',
            'x': 0.0, 'y': 0.9, 'w': 13.5, 'h': 4.5,
            'text_center': (6.75, 3.15),
            'door': (12.0, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },

        # --- South-West Wing (Y: -4.9 to -0.9m) ---
        {
            'id': 'P1_CVP', 'name': 'Phòng Chánh văn phòng',
            'x': 0.0, 'y': -4.9, 'w': 13.5, 'h': 4.0,
            'text_center': (6.75, -2.9),
            'door': (12.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },

        # --- North-East Wing (Y: 0.9 to 5.4m) ---
        {
            'id': 'P1_P6', 'name': 'Phòng số 6',
            'x': 18.5, 'y': 0.9, 'w': 13.5, 'h': 4.5,
            'text_center': (25.25, 3.15),
            'door': (20.0, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },

        # --- South-East Wing (Y: -4.9 to -0.9m) ---
        {
            'id': 'P1_P5', 'name': 'Phòng số 5',
            'x': 18.5, 'y': -4.9, 'w': 13.5, 'h': 4.0,
            'text_center': (25.25, -2.9),
            'door': (20.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },

        # === TÒA 2 (KHỐI XÉT XỬ PHÍA BẮC - 2 HỘI TRƯỜNG XÉT XỬ A & B) ===
        # --- West Wing Tòa 2 (Courtroom Hall A: X: 3.5 to 13.5m, Y: 6.2 to 14.5m) ---
        {
            'id': 'P2_XXA', 'name': 'Hội trường xét xử A',
            'x': 3.5, 'y': 6.2, 'w': 10.0, 'h': Y_TOA2_TOP - 6.2,
            'text_center': (8.5, 10.35),
            'door': (13.5, 9.8, 0.9, 'W_IN_UP'),
            'font_size': 10.5
        },

        # --- East Wing Tòa 2 (Courtroom Hall B: X: 18.5 to 28.5m, Y: 6.2 to 14.5m) ---
        {
            'id': 'P2_XXB', 'name': 'Hội trường xét xử B',
            'x': 18.5, 'y': 6.2, 'w': 10.0, 'h': Y_TOA2_TOP - 6.2,
            'text_center': (23.5, 10.35),
            'door': (18.5, 9.8, 0.9, 'E_IN_UP'),
            'font_size': 10.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 14.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # Front Main Entrance Steps at Bottom (South: Y = -4.9 to -5.7)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([13.5, 18.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([13.5, 13.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([18.5, 18.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # Outdoor Side Steps at West & East Corridor Exits of Tòa 1 (Open Exits at both ends)
    for i in range(5):
        dx = -0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    for i in range(5):
        dx = X_MAX + 0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([X_MAX, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([X_MAX, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Labels for Lobby and Corridor
    ax.text(16.0, -2.9, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (PRECISION ALIGNED WITH DOOR OPENINGS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Tòa 1 Outer West Wall (Open at Corridor Y: -0.9 to 0.9)
    draw_wall(-W, -4.9 - W, W, 4.0 + W)
    draw_wall(-W, 0.9, W, 4.5 + W)

    # Tòa 1 Outer East Wall (Open at Corridor Y: -0.9 to 0.9)
    draw_wall(X_MAX, -4.9 - W, W, 4.0 + W)
    draw_wall(X_MAX, 0.9, W, 4.5 + W)

    # Tòa 1 North Top Wall (Y = 5.4m, open for rear passage at X: 13.5 to 18.5)
    draw_wall(-W, 5.4, 13.5 + W + PART_THICKNESS/2, W)
    draw_wall(18.5 - PART_THICKNESS/2, 5.4, (X_MAX - 18.5) + W + PART_THICKNESS/2, W)

    # Tòa 1 South Bottom Wall (Y = -4.9m, open for Main Entrance at X: 13.5 to 18.5)
    draw_wall(-W, -4.9 - W, 13.5 + W + PART_THICKNESS/2, W)
    draw_wall(18.5 - PART_THICKNESS/2, -4.9 - W, (X_MAX - 18.5) + W + PART_THICKNESS/2, W)

    # South Front Entrance Side Wall Cheeks
    draw_wall(13.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)
    draw_wall(18.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)

    # TÒA 2 CONNECTING PASSAGE WALLS & EXTERIOR WALLS
    # Left Wall at X = 13.5m (Door entry for Courtroom A at Y: 9.8 to 10.7)
    draw_wall(13.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 4.4)    # Y: 5.4 to 9.8
    draw_wall(13.5 - PART_THICKNESS/2, 10.7, PART_THICKNESS, 3.8)   # Y: 10.7 to 14.5

    # Right Wall at X = 18.5m (Door entry for Courtroom B at Y: 9.8 to 10.7)
    draw_wall(18.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 4.4)    # Y: 5.4 to 9.8
    draw_wall(18.5 - PART_THICKNESS/2, 10.7, PART_THICKNESS, 3.8)   # Y: 10.7 to 14.5

    # Tòa 2 Exterior Walls
    draw_wall(3.5 - W, 6.2 - W, W, (Y_TOA2_TOP - 6.2) + 2*W)       # West outer wall
    draw_wall(28.5, 6.2 - W, W, (Y_TOA2_TOP - 6.2) + 2*W)          # East outer wall
    draw_wall(3.5 - W, Y_TOA2_TOP, 25.0 + 2*W, W)                 # North outer wall
    draw_wall(3.5 - W, 6.2 - W, 10.0 + W, W)                     # South outer wall West wing (Courtroom A)
    draw_wall(18.5, 6.2 - W, 10.0 + W, W)                        # South outer wall East wing (Courtroom B)

    # Tòa 1 Corridor Wall Lines (Y = 0.9 & Y = -0.9)
    # North Corridor Line Y = 0.9
    draw_wall(0, 0.9 - PART_THICKNESS/2, 12.0, PART_THICKNESS)
    draw_wall(12.9, 0.9 - PART_THICKNESS/2, 0.6, PART_THICKNESS)
    draw_wall(18.5, 0.9 - PART_THICKNESS/2, 1.5, PART_THICKNESS)
    draw_wall(20.9, 0.9 - PART_THICKNESS/2, 11.1, PART_THICKNESS)

    # South Corridor Line Y = -0.9
    draw_wall(0, -0.9 - PART_THICKNESS/2, 12.0, PART_THICKNESS)
    draw_wall(12.9, -0.9 - PART_THICKNESS/2, 0.6, PART_THICKNESS)
    draw_wall(18.5, -0.9 - PART_THICKNESS/2, 1.5, PART_THICKNESS)
    draw_wall(20.9, -0.9 - PART_THICKNESS/2, 11.1, PART_THICKNESS)

    # Tòa 1 Internal Vertical Partitions
    # West dividing wall at X = 13.5m
    draw_wall(13.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(13.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

    # East dividing wall at X = 18.5m
    draw_wall(18.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(18.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

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

    # Tòa 1 North Windows (Y = 5.4m)
    draw_window(4.5, 5.4, 4.5, W, is_horizontal=True)      # Văn phòng
    draw_window(23.0, 5.4, 4.5, W, is_horizontal=True)     # Phòng số 6

    # Tòa 1 South Windows (Y = -4.9 - W)
    draw_window(4.5, -4.9 - W, 4.5, W, is_horizontal=True) # Phòng Chánh văn phòng
    draw_window(23.0, -4.9 - W, 4.5, W, is_horizontal=True)# Phòng số 5

    # Tòa 1 Side Windows
    draw_window(-W, 2.25, W, 1.8, is_horizontal=False)     # Văn phòng West
    draw_window(-W, -3.5, W, 1.8, is_horizontal=False)     # Phòng Chánh văn phòng West
    draw_window(X_MAX, 2.25, W, 1.8, is_horizontal=False)  # Phòng số 6 East
    draw_window(X_MAX, -3.5, W, 1.8, is_horizontal=False)  # Phòng số 5 East

    # Tòa 2 North Windows (Y = 14.5m)
    draw_window(7.0, Y_TOA2_TOP, 3.0, W, is_horizontal=True)   # Hội trường xét xử A
    draw_window(15.0, Y_TOA2_TOP, 2.0, W, is_horizontal=True)  # Central Hall Window
    draw_window(22.0, Y_TOA2_TOP, 3.0, W, is_horizontal=True)  # Hội trường xét xử B

    # Tòa 2 South Windows (Y = 6.2 - W)
    draw_window(7.0, 6.2 - W, 3.0, W, is_horizontal=True)    # Hội trường xét xử A
    draw_window(22.0, 6.2 - W, 3.0, W, is_horizontal=True)   # Hội trường xét xử B

    # Tòa 2 Side Windows
    draw_window(3.5 - W, 12.0, W, 1.8, is_horizontal=False)  # Hội trường xét xử A West
    draw_window(3.5 - W, 7.5, W, 1.8, is_horizontal=False)   # Hội trường xét xử A West
    draw_window(28.5, 12.0, W, 1.8, is_horizontal=False)     # Hội trường xét xử B East
    draw_window(28.5, 7.5, W, 1.8, is_horizontal=False)      # Hội trường xét xử B East

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
        elif mode == 'E_IN_UP':
            # Pivot at (x, y), door swings into room to the east (x > pivot)
            ax.plot([x, x + size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'W_IN_UP':
            # Pivot at (x, y), door swings into room to the west (x < pivot)
            ax.plot([x, x - size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)

    for r in rooms:
        dx, dy, dsize, dmode = r['door']
        draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS (SINGLE-LINE LABELS, NO WRAPPING)
    # ---------------------------------------------------------
    for r in rooms:
        if r['name']:
            cx, cy = r['text_center']
            font_sz = r.get('font_size', 9.5)
            ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 34.0)
    ax.set_ylim(-8.0, 16.5)

    # Output directory
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "mat_bang_tang_1.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang1()
