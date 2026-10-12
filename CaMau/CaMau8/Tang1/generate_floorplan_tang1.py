import os
from typing import TypedDict, Tuple, List, Optional
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
    door: Optional[Tuple[float, float, float, str]]
    font_size: float

def create_floorplan_tang1(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_1.png')

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(26, 8.5), dpi=300)
    ax = fig.add_axes([0.02, 0.08, 0.96, 0.82])
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
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 stair fill matching lobby background

    WALL_THICKNESS = 0.20           # 200mm exterior wall
    PART_THICKNESS = 0.10           # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    X_MIN = -24.5
    X_MAX = 44.5

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line per Spec)
    fig.text(0.03, 0.952, 'MẶT BẰNG TẦNG 1  —  TÒA ÁN NHÂN DÂN KHU VỰC 8 - CÀ MAU', 
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.932, 0.932], transform=fig.transFigure, color='#e2e8f0', linewidth=1.1)
    fig.lines.append(header_line)

    # Legend Box Centered at Bottom
    lg_x, lg_y = 0.0, -8.2
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x - 12.0, lg_y), 1.2, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x - 10.4, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x - 3.0, lg_y + 0.10), 1.2, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x - 1.4, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 6.0, lg_x + 7.2], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 6.0, lg_x + 7.2], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 7.6, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 13.5, lg_x + 13.5], [lg_y + 0.02, lg_y + 0.32], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 13.5, lg_y + 0.02), 0.60, 0.60, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 14.8, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (OPEN EXITS AT EAST & WEST)
    # ---------------------------------------------------------
    # Horizontal Central Corridor (X: -24.5 to 44.5, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((X_MIN, -0.9), X_MAX - X_MIN, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # South Front Main Lobby Space (X: 7.5 to 12.5, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((7.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # North Rear Stair & Passage Hall Space (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (ALL 16 ROOMS STRICTLY MATCHING PROMPT SURVEY)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # ==========================================
        # === CÁNH TÂY (WEST WING: 8 PHÒNG) ===
        # ==========================================
        # --- Dãy Bắc Cánh Tây (4 Phòng: Phòng 27, 1, 2, 3) ---
        {
            'id': 'P27', 'name': 'Phòng 27',
            'x': -24.5, 'y': 0.9, 'w': 14.0, 'h': 4.5,
            'text_center': (-17.5, 3.15),
            'door': (-12.0, 0.9, 1.2, 'DOUBLE_N'),
            'font_size': 11.5
        },
        {
            'id': 'P1', 'name': 'Phòng 1',
            'x': -10.5, 'y': 0.9, 'w': 6.0, 'h': 4.5,
            'text_center': (-7.5, 3.15),
            'door': (-5.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P2', 'name': 'Phòng 2',
            'x': -4.5, 'y': 0.9, 'w': 6.0, 'h': 4.5,
            'text_center': (-1.5, 3.15),
            'door': (0.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P3', 'name': 'Phòng 3',
            'x': 1.5, 'y': 0.9, 'w': 6.0, 'h': 4.5,
            'text_center': (4.5, 3.15),
            'door': (6.2, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },

        # --- Dãy Nam Cánh Tây (4 Phòng: Phòng 4, 5, 6, 7) ---
        {
            'id': 'P4', 'name': 'Phòng 4',
            'x': -24.5, 'y': -4.9, 'w': 8.0, 'h': 4.0,
            'text_center': (-20.5, -2.9),
            'door': (-18.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P5', 'name': 'Phòng 5',
            'x': -16.5, 'y': -4.9, 'w': 8.0, 'h': 4.0,
            'text_center': (-12.5, -2.9),
            'door': (-10.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P6', 'name': 'Phòng 6',
            'x': -8.5, 'y': -4.9, 'w': 8.0, 'h': 4.0,
            'text_center': (-4.5, -2.9),
            'door': (-2.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P7', 'name': 'Phòng 7',
            'x': -0.5, 'y': -4.9, 'w': 8.0, 'h': 4.0,
            'text_center': (3.5, -2.9),
            'door': (6.2, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },

        # ==========================================
        # === CÁNH ĐÔNG (EAST WING: 8 PHÒNG) ===
        # ==========================================
        # --- Dãy Bắc Cánh Đông (4 Phòng: Phòng 8, 9, 10, 26) ---
        {
            'id': 'P8', 'name': 'Phòng 8',
            'x': 12.5, 'y': 0.9, 'w': 6.0, 'h': 4.5,
            'text_center': (15.5, 3.15),
            'door': (13.8, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P9', 'name': 'Phòng 9',
            'x': 18.5, 'y': 0.9, 'w': 6.0, 'h': 4.5,
            'text_center': (21.5, 3.15),
            'door': (19.8, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P10', 'name': 'Phòng 10',
            'x': 24.5, 'y': 0.9, 'w': 6.0, 'h': 4.5,
            'text_center': (27.5, 3.15),
            'door': (25.8, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P26', 'name': 'Phòng 26',
            'x': 30.5, 'y': 0.9, 'w': 14.0, 'h': 4.5,
            'text_center': (37.5, 3.15),
            'door': (32.5, 0.9, 1.2, 'DOUBLE_N'),
            'font_size': 11.5
        },

        # --- Dãy Nam Cánh Đông (4 Phòng: Phòng 11, 12, 13, 14) ---
        {
            'id': 'P11', 'name': 'Phòng 11',
            'x': 12.5, 'y': -4.9, 'w': 7.0, 'h': 4.0,
            'text_center': (16.0, -2.9),
            'door': (13.8, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P12', 'name': 'Phòng 12',
            'x': 19.5, 'y': -4.9, 'w': 7.0, 'h': 4.0,
            'text_center': (23.0, -2.9),
            'door': (20.8, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P13', 'name': 'Phòng 13',
            'x': 26.5, 'y': -4.9, 'w': 7.0, 'h': 4.0,
            'text_center': (30.0, -2.9),
            'door': (27.8, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'P14', 'name': 'Phòng 14',
            'x': 33.5, 'y': -4.9, 'w': 11.0, 'h': 4.0,
            'text_center': (39.0, -2.9),
            'door': (35.0, -0.9, 1.0, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS (FLOOR 1 SPECIFIC)
    # ---------------------------------------------------------
    # Central Staircase inside North Hall (Background matches sảnh fill COLOR_STAIR_FILL per Tang 1 Spec)
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
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
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.25, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='top', zorder=5)

    # 1. Front Main Entrance Steps at South (Y = -4.9 to -5.7m, X = 7.5 to 12.5m)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # 2. Rear Exit Steps at North (Y = 5.4 to 6.2m, X = 7.5 to 12.5m)
    for sy in [5.4, 5.56, 5.72, 5.88, 6.04, 6.20]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Outdoor Side Steps at Corridor Ends (East & West Exits)
    for i in range(5):
        dx = X_MIN - 0.22 * (i + 1)
        dy = 0.9 + i * 0.08
        ax.plot([dx, X_MIN], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, X_MIN], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    for i in range(5):
        dx = X_MAX + 0.22 * (i + 1)
        dy = 0.9 + i * 0.08
        ax.plot([X_MAX, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([X_MAX, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Labels for Lobby and Corridor
    ax.text(10.0, -2.9, 'SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(-8.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(28.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (UNBLOCKED CORRIDOR EXITS & ENTRANCE CHEEK WALLS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Walls (SPLIT TO LEAVE CORRIDOR Y: -0.9 TO 0.9 UNBLOCKED!)
    draw_wall(X_MIN - W, -4.9 - W, W, 4.0 + W)  # Bottom-left segment (Y: -4.9-W to -0.9)
    draw_wall(X_MIN - W, 0.9, W, 4.5 + W)       # Top-left segment (Y: 0.9 to 5.4+W)

    # Rightmost Vertical Exterior Walls (SPLIT TO LEAVE CORRIDOR Y: -0.9 TO 0.9 UNBLOCKED!)
    draw_wall(X_MAX, -4.9 - W, W, 4.0 + W)      # Bottom-right segment (Y: -4.9-W to -0.9)
    draw_wall(X_MAX, 0.9, W, 4.5 + W)           # Top-right segment (Y: 0.9 to 5.4+W)

    # North Top Exterior Wall (with opening for rear exit at X: 7.5 to 12.5)
    draw_wall(X_MIN - W, 5.4, (7.5 - X_MIN) + W + P/2, W)
    draw_wall(12.5 - P/2, 5.4, (X_MAX - 12.5) + W + P/2, W)

    # South Bottom Exterior Wall (with opening for main front entrance at X: 7.5 to 12.5)
    draw_wall(X_MIN - W, -4.9 - W, (7.5 - X_MIN) + W + P/2, W)
    draw_wall(12.5 - P/2, -4.9 - W, (X_MAX - 12.5) + W + P/2, W)

    # STRUCTURAL WALL CHEEKS & HOOKS
    # South Front Entrance Side Wall Cheeks (Y: -4.9 down to -5.7m)
    draw_wall(7.5 - P/2, -5.7, P, 0.8)
    draw_wall(12.5 - P/2, -5.7, P, 0.8)

    # North Rear Exit Side Wall Cheeks (Y: 5.4 up to 6.2m) & Top Inward Hooks
    draw_wall(7.5 - P/2, 5.4, P, 0.8)
    draw_wall(12.5 - P/2, 5.4, P, 0.8)
    # Top Inward Hooks at Y = 6.2m (0.5m inward)
    draw_wall(7.5 - P/2, 6.2 - P, 0.5, P)
    draw_wall(12.5 + P/2 - 0.5, 6.2 - P, 0.5, P)

    # Vertical Internal Partitions (North Wing Y: 0.9 to 5.4m)
    north_part_x = [-10.5, -4.5, 1.5, 7.5, 12.5, 18.5, 24.5, 30.5]
    for px in north_part_x:
        draw_wall(px - P/2, 0.9, P, 4.5)

    # Vertical Internal Partitions (South Wing Y: -4.9 to -0.9m)
    south_part_x = [-16.5, -8.5, -0.5, 7.5, 12.5, 19.5, 26.5, 33.5]
    for px in south_part_x:
        draw_wall(px - P/2, -4.9, P, 4.0)

    # North Corridor Wall Line (Y = 0.9m) - Broken cleanly at door openings
    # West North segments:
    # P27: X = -24.5 to -10.5, door at -12.0 to -10.8 (width 1.2)
    draw_wall(X_MIN, 0.9 - P/2, (-12.0 - X_MIN), P)
    draw_wall(-10.8, 0.9 - P/2, 0.3, P)
    # P1: door at -5.5 to -4.6
    draw_wall(-10.5, 0.9 - P/2, 5.0, P)
    draw_wall(-4.6, 0.9 - P/2, 0.1, P)
    # P2: door at 0.5 to 1.4
    draw_wall(-4.5, 0.9 - P/2, 5.0, P)
    draw_wall(1.4, 0.9 - P/2, 0.1, P)
    # P3: door at 6.2 to 7.1
    draw_wall(1.5, 0.9 - P/2, 4.7, P)
    draw_wall(7.1, 0.9 - P/2, 0.4, P)
    # (X: 7.5 to 12.5 is Stair Hall Open Entrance)
    # P8: door at 13.8 to 14.7
    draw_wall(12.5, 0.9 - P/2, 1.3, P)
    draw_wall(14.7, 0.9 - P/2, 3.8, P)
    # P9: door at 19.8 to 20.7
    draw_wall(18.5, 0.9 - P/2, 1.3, P)
    draw_wall(20.7, 0.9 - P/2, 3.8, P)
    # P10: door at 25.8 to 26.7
    draw_wall(24.5, 0.9 - P/2, 1.3, P)
    draw_wall(26.7, 0.9 - P/2, 3.8, P)
    # P26: door at 32.5 to 33.7 (width 1.2)
    draw_wall(30.5, 0.9 - P/2, 2.0, P)
    draw_wall(33.7, 0.9 - P/2, (X_MAX - 33.7), P)

    # South Corridor Wall Line (Y = -0.9m) - Broken cleanly at door openings
    # P4: door at -18.0 to -17.1
    draw_wall(X_MIN, -0.9 - P/2, (-18.0 - X_MIN), P)
    draw_wall(-17.1, -0.9 - P/2, 0.6, P)
    # P5: door at -10.0 to -9.1
    draw_wall(-16.5, -0.9 - P/2, 6.5, P)
    draw_wall(-9.1, -0.9 - P/2, 0.6, P)
    # P6: door at -2.0 to -1.1
    draw_wall(-8.5, -0.9 - P/2, 6.5, P)
    draw_wall(-1.1, -0.9 - P/2, 0.6, P)
    # P7: door at 6.2 to 7.1
    draw_wall(-0.5, -0.9 - P/2, 6.7, P)
    draw_wall(7.1, -0.9 - P/2, 0.4, P)
    # (X: 7.5 to 12.5 is Front Lobby Open Connection)
    # P11: door at 13.8 to 14.7
    draw_wall(12.5, -0.9 - P/2, 1.3, P)
    draw_wall(14.7, -0.9 - P/2, 4.8, P)
    # P12: door at 20.8 to 21.7
    draw_wall(19.5, -0.9 - P/2, 1.3, P)
    draw_wall(21.7, -0.9 - P/2, 4.8, P)
    # P13: door at 27.8 to 28.7
    draw_wall(26.5, -0.9 - P/2, 1.3, P)
    draw_wall(28.7, -0.9 - P/2, 4.8, P)
    # P14: door at 35.0 to 36.0
    draw_wall(33.5, -0.9 - P/2, 1.5, P)
    draw_wall(36.0, -0.9 - P/2, (X_MAX - 36.0), P)

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

    # Windows on North Exterior Wall (Y = 5.4m)
    # West North rooms:
    draw_window(-22.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(-18.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(-14.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(-8.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(-2.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(3.5, 5.4, 2.0, W, is_horizontal=True)
    # East North rooms:
    draw_window(14.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(20.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(26.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(32.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(36.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(40.5, 5.4, 2.0, W, is_horizontal=True)

    # Windows on South Exterior Wall (Y = -4.9m - W)
    # West South rooms:
    draw_window(-22.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(-18.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(-14.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(-10.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(-6.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(-2.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(1.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(4.5, -4.9 - W, 2.0, W, is_horizontal=True)
    # East South rooms:
    draw_window(14.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(17.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(21.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(24.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(28.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(31.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(35.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(39.5, -4.9 - W, 2.0, W, is_horizontal=True)

    # Windows on West & East End Walls
    draw_window(X_MIN - W, 2.0, W, 1.8, is_horizontal=False)
    draw_window(X_MIN - W, -3.8, W, 1.8, is_horizontal=False)
    draw_window(X_MAX, 2.0, W, 1.8, is_horizontal=False)
    draw_window(X_MAX, -3.8, W, 1.8, is_horizontal=False)

    # ---------------------------------------------------------
    # 8. DRAW DOORS (INWARD SWINGING PER SPEC)
    # ---------------------------------------------------------
    def draw_door(hx, hy, dw, dtype):
        if dtype == 'N_IN_RIGHT':
            ax.plot([hx, hx], [hy, hy + dw], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((hx, hy), dw * 2, dw * 2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc)
        elif dtype == 'S_IN_RIGHT':
            ax.plot([hx, hx], [hy, hy - dw], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((hx, hy), dw * 2, dw * 2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc)
        elif dtype == 'DOUBLE_N':
            # Double door at hx with width dw
            leaf = dw / 2.0
            # Left leaf
            ax.plot([hx, hx], [hy, hy + leaf], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_l = patches.Arc((hx, hy), leaf * 2, leaf * 2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc_l)
            # Right leaf
            ax.plot([hx + dw, hx + dw], [hy, hy + leaf], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_r = patches.Arc((hx + dw, hy), leaf * 2, leaf * 2, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc_r)

    for r in rooms:
        if r['door']:
            dx, dy, dw, dtype = r['door']
            draw_door(dx, dy, dw, dtype)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS (FULL ROOM NAMES FROM SURVEY PROMPT)
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'], 
                fontweight='bold', ha='center', va='center', zorder=20)

    # Save high-resolution PNG
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Floorplan successfully generated at: {out_img_path}")

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau8\Tang1"
    create_floorplan_tang1(target_dir)
