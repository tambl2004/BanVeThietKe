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

def create_floorplan_tang3():
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
    COLOR_STAIR_FILL = '#ffffff'    # Pure white for staircase fill on Floor 3
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    X_MAX = 32.0            # Main building length = 32.0m

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 3  —  Tòa án nhân dân tỉnh Đồng Nai', 
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
    ax.plot([lg_x + 22.0, lg_x + 22.0], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 22.0, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 23.0, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Main Building Horizontal Corridor (X: 0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Central Passage leading to Tòa 2 (X: 13.5 to 18.5, Y: 0.9 to 14.5)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 13.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 3 — ĐỒNG NAI)
    # Tòa 1: 18 phòng, Tòa 2: 2 phòng (tổng 20 phòng)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA 1 — NORTH WING (Y: 0.9 to 5.4m) ===
        # West Wing: 301 HC, 302 HC, 303 HC, 304 HC
        {
            'id': 'P3_301HC', 'name': 'Phòng 301 HC',
            'x': 0.0, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (1.6875, 3.15),
            'door': (2.2, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P3_302HC', 'name': 'Phòng 302 HC',
            'x': 3.375, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (5.0625, 3.15),
            'door': (5.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P3_303HC', 'name': 'Phòng 303 HC',
            'x': 6.75, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (8.4375, 3.15),
            'door': (8.8, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P3_304HC', 'name': 'Phòng 304 HC',
            'x': 10.125, 'y': 0.9, 'w': 3.375, 'h': 4.5,
            'text_center': (11.8125, 3.15),
            'door': (12.2, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        # East Wing: 308, 309, 310, 311, 312, 313
        {
            'id': 'P3_308', 'name': 'Phòng 308',
            'x': 18.5, 'y': 0.9, 'w': 2.0, 'h': 4.5,
            'text_center': (19.5, 3.15),
            'door': (19.4, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P3_309', 'name': 'Phòng 309',
            'x': 20.5, 'y': 0.9, 'w': 2.0, 'h': 4.5,
            'text_center': (21.5, 3.15),
            'door': (21.4, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P3_310', 'name': 'Phòng 310',
            'x': 22.5, 'y': 0.9, 'w': 2.0, 'h': 4.5,
            'text_center': (23.5, 3.15),
            'door': (23.4, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P3_311', 'name': 'Phòng 311',
            'x': 24.5, 'y': 0.9, 'w': 2.0, 'h': 4.5,
            'text_center': (25.5, 3.15),
            'door': (25.4, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P3_312', 'name': 'Phòng 312',
            'x': 26.5, 'y': 0.9, 'w': 3.5, 'h': 4.5,
            'text_center': (28.25, 3.15),
            'door': (27.5, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P3_313', 'name': 'Phòng 313',
            'x': 30.0, 'y': 0.9, 'w': 2.0, 'h': 4.5,
            'text_center': (31.0, 3.15),
            'door': (30.8, 0.9, 0.75, 'N_IN_RIGHT'),
            'font_size': 7.5
        },

        # === TÒA 1 — SOUTH WING (Y: -4.9 to -0.9m) ===
        # West Wing: 301, 302, 303, 304
        {
            'id': 'P3_301', 'name': 'Phòng 301',
            'x': 0.0, 'y': -4.9, 'w': 2.25, 'h': 4.0,
            'text_center': (1.125, -2.9),
            'door': (1.2, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P3_302', 'name': 'Phòng 302',
            'x': 2.25, 'y': -4.9, 'w': 2.25, 'h': 4.0,
            'text_center': (3.375, -2.9),
            'door': (3.5, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P3_303', 'name': 'Phòng 303',
            'x': 4.5, 'y': -4.9, 'w': 2.25, 'h': 4.0,
            'text_center': (5.625, -2.9),
            'door': (5.7, -0.9, 0.75, 'S_IN_RIGHT'),
            'font_size': 7.5
        },
        {
            'id': 'P3_304', 'name': 'Phòng 304',
            'x': 6.75, 'y': -4.9, 'w': 6.75, 'h': 4.0,
            'text_center': (10.125, -2.9),
            'door': (12.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        # Center South: 305
        {
            'id': 'P3_305', 'name': 'Phòng 305',
            'x': 13.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (16.0, -2.9),
            'door': (14.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        # East Wing: 306, 307, 307
        {
            'id': 'P3_306', 'name': 'Phòng 306',
            'x': 18.5, 'y': -4.9, 'w': 6.5, 'h': 4.0,
            'text_center': (21.75, -2.9),
            'door': (19.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 8.5
        },
        {
            'id': 'P3_307A', 'name': 'Phòng 307',
            'x': 25.0, 'y': -4.9, 'w': 3.5, 'h': 4.0,
            'text_center': (26.75, -2.9),
            'door': (26.0, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.0
        },
        {
            'id': 'P3_307B', 'name': 'Phòng 307',
            'x': 28.5, 'y': -4.9, 'w': 3.5, 'h': 4.0,
            'text_center': (30.25, -2.9),
            'door': (29.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 8.0
        },

        # === TÒA 2 — REAR BLOCK (Y: 6.2 to 14.5m) ===
        # West Wing Large Courtroom: Phòng XX 5
        {
            'id': 'P3_XX5', 'name': 'Phòng XX 5',
            'x': 3.5, 'y': 6.2, 'w': 10.0, 'h': 8.3,
            'text_center': (8.5, 10.35),
            'door': (13.5, 10.25, 0.9, 'W_IN_DOWN'),
            'font_size': 10.5
        },
        # East Wing Large Meeting Room: Phòng họp 2
        {
            'id': 'P3_H2', 'name': 'Phòng họp 2',
            'x': 18.5, 'y': 6.2, 'w': 10.0, 'h': 8.3,
            'text_center': (23.5, 10.35),
            'door': (18.5, 10.25, 0.9, 'E_IN_DOWN'),
            'font_size': 10.5
        },
    ]

    # Draw Room Background Fills
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE (UPPER FLOOR SPEC: PURE WHITE BACKGROUND)
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

    # Labels for Corridor
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.0, 10.25, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Main Building Exterior Side Walls (Enclosed at X=0 and X=32)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)
    draw_wall(X_MAX, -4.9 - W, W, 10.3 + 2*W)

    # Main Building North Top Wall (Y = 5.4)
    draw_wall(-W, 5.4, 13.5 + W + PART_THICKNESS/2, W)
    draw_wall(18.5 - PART_THICKNESS/2, 5.4, (X_MAX - 18.5) + W + PART_THICKNESS/2, W)

    # Main Building South Bottom Wall
    draw_wall(-W, -4.9 - W, X_MAX + 2*W, W)

    # Tòa 2 Connecting Passage Side Walls (X = 13.5m and X = 18.5m, with doors to XX 5 and Phòng họp 2)
    # Left Wall at X = 13.5m: door at Y = 10.25 to 11.15
    draw_wall(13.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 4.85)   # From Y=5.4 to 10.25m
    draw_wall(13.5 - PART_THICKNESS/2, 11.15, PART_THICKNESS, 3.35) # From Y=11.15 to 14.5m
    
    # Right Wall at X = 18.5m: door at Y = 10.25 to 11.15
    draw_wall(18.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 4.85)   # From Y=5.4 to 10.25m
    draw_wall(18.5 - PART_THICKNESS/2, 11.15, PART_THICKNESS, 3.35) # From Y=11.15 to 14.5m

    # Tòa 2 Exterior Walls
    draw_wall(3.5 - W, 14.5, 25.0 + 2*W, W)                      # North outer wall
    draw_wall(3.5 - W, 6.2 - W, 10.0 + W, W)                     # South outer wall West wing
    draw_wall(18.5, 6.2 - W, 10.0 + W, W)                        # South outer wall East wing
    draw_wall(3.5 - W, 6.2 - W, W, 8.3 + 2*W)                    # West outer wall
    draw_wall(28.5, 6.2 - W, W, 8.3 + 2*W)                      # East outer wall

    # Tòa 1 Corridor Wall Lines (Y = 0.9 & Y = -0.9) with door cutouts
    # North Corridor Line Y = 0.9 (Doors at: 2.2, 5.5, 8.8, 12.2 | 19.4, 21.4, 23.4, 25.4, 27.5, 30.8)
    # West Wing:
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 2.2, PART_THICKNESS)
    draw_wall(3.0, 0.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)
    draw_wall(6.3, 0.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)
    draw_wall(9.6, 0.9 - PART_THICKNESS/2, 2.6, PART_THICKNESS)
    draw_wall(13.0, 0.9 - PART_THICKNESS/2, 0.5, PART_THICKNESS)
    # East Wing:
    draw_wall(18.5, 0.9 - PART_THICKNESS/2, 0.9, PART_THICKNESS)
    draw_wall(20.15, 0.9 - PART_THICKNESS/2, 1.25, PART_THICKNESS)
    draw_wall(22.15, 0.9 - PART_THICKNESS/2, 1.25, PART_THICKNESS)
    draw_wall(24.15, 0.9 - PART_THICKNESS/2, 1.25, PART_THICKNESS)
    draw_wall(26.15, 0.9 - PART_THICKNESS/2, 1.35, PART_THICKNESS)
    draw_wall(28.3, 0.9 - PART_THICKNESS/2, 2.5, PART_THICKNESS)
    draw_wall(31.55, 0.9 - PART_THICKNESS/2, 0.45, PART_THICKNESS)

    # South Corridor Line Y = -0.9 (Doors at: 1.2, 3.5, 5.7, 12.2 | 14.5 | 19.5, 26.0, 29.5)
    # West Wing:
    draw_wall(0.0, -0.9 - PART_THICKNESS/2, 1.2, PART_THICKNESS)
    draw_wall(1.95, -0.9 - PART_THICKNESS/2, 1.55, PART_THICKNESS)
    draw_wall(4.25, -0.9 - PART_THICKNESS/2, 1.45, PART_THICKNESS)
    draw_wall(6.45, -0.9 - PART_THICKNESS/2, 5.75, PART_THICKNESS)
    draw_wall(13.05, -0.9 - PART_THICKNESS/2, 0.45, PART_THICKNESS)
    # Center:
    draw_wall(13.5, -0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(15.35, -0.9 - PART_THICKNESS/2, 3.15, PART_THICKNESS)
    # East Wing:
    draw_wall(18.5, -0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(20.35, -0.9 - PART_THICKNESS/2, 5.65, PART_THICKNESS)
    draw_wall(26.8, -0.9 - PART_THICKNESS/2, 2.7, PART_THICKNESS)
    draw_wall(30.3, -0.9 - PART_THICKNESS/2, 1.7, PART_THICKNESS)

    # Tòa 1 Internal Vertical Partitions
    # North Wing:
    draw_wall(3.375 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(6.75 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(10.125 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(13.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(18.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(20.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(22.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(24.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(26.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(30.0 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    # South Wing:
    draw_wall(2.25 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(4.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(6.75 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(13.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(18.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(25.0 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(28.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

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

    # Tòa 1 North Windows (Y = 5.4)
    draw_window(1.0, 5.4, 1.4, W, is_horizontal=True)    # 301 HC
    draw_window(4.4, 5.4, 1.4, W, is_horizontal=True)    # 302 HC
    draw_window(7.7, 5.4, 1.4, W, is_horizontal=True)    # 303 HC
    draw_window(11.1, 5.4, 1.4, W, is_horizontal=True)   # 304 HC
    draw_window(19.0, 5.4, 1.0, W, is_horizontal=True)   # 308
    draw_window(21.0, 5.4, 1.0, W, is_horizontal=True)   # 309
    draw_window(23.0, 5.4, 1.0, W, is_horizontal=True)   # 310
    draw_window(25.0, 5.4, 1.0, W, is_horizontal=True)   # 311
    draw_window(27.5, 5.4, 1.5, W, is_horizontal=True)   # 312
    draw_window(30.5, 5.4, 1.0, W, is_horizontal=True)   # 313

    # Tòa 1 South Windows (Y = -4.9 - W)
    draw_window(0.5, -4.9 - W, 1.2, W, is_horizontal=True)   # 301
    draw_window(2.8, -4.9 - W, 1.2, W, is_horizontal=True)   # 302
    draw_window(5.0, -4.9 - W, 1.2, W, is_horizontal=True)   # 303
    draw_window(9.0, -4.9 - W, 2.5, W, is_horizontal=True)   # 304
    draw_window(14.75, -4.9 - W, 2.5, W, is_horizontal=True) # 305
    draw_window(20.5, -4.9 - W, 2.5, W, is_horizontal=True)  # 306
    draw_window(25.8, -4.9 - W, 1.8, W, is_horizontal=True)  # 307
    draw_window(29.3, -4.9 - W, 1.8, W, is_horizontal=True)  # 307

    # Tòa 1 Corridor End Windows (Floor 3 enclosed ends)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)

    # Tòa 2 Windows (Phòng XX 5 & Phòng họp 2)
    draw_window(6.5, 14.5, 4.0, W, is_horizontal=True)       # XX 5 North
    draw_window(21.5, 14.5, 4.0, W, is_horizontal=True)      # H2 North
    draw_window(15.0, 14.5, 2.0, W, is_horizontal=True)      # Corridor North top window
    draw_window(6.5, 6.2 - W, 4.0, W, is_horizontal=True)    # XX 5 South
    draw_window(21.5, 6.2 - W, 4.0, W, is_horizontal=True)   # H2 South

    draw_window(3.5 - W, 9.5, W, 2.5, is_horizontal=False)   # XX 5 West
    draw_window(28.5, 9.5, W, 2.5, is_horizontal=False)     # H2 East

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
        elif mode == 'W_IN_DOWN':
            # Door on east wall of room (X = 13.5), opens inward West and Down
            ax.plot([x, x - size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=180, theta2=270,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'E_IN_DOWN':
            # Door on west wall of room (X = 18.5), opens inward East and Down
            ax.plot([x, x + size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
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
        if r['name']:
            cx, cy = r['text_center']
            font_sz = r.get('font_size', 8.0)
            ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                    fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 34.0)
    ax.set_ylim(-8.0, 16.5)

    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "mat_bang_tang_3.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 3 đã xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang3()
