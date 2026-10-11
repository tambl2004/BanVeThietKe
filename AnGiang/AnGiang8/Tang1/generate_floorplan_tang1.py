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
    fig = plt.figure(figsize=(24, 16), dpi=300)
    ax = fig.add_axes([0.02, 0.05, 0.96, 0.88])
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
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Including Building Name, NO Subtitle line)
    fig.text(0.03, 0.955, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 8 - An Giang', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.938, 0.938], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = -0.5, -15.2
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

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (SEAMLESS CONNECTING DOORWAY)
    # ---------------------------------------------------------
    # Tòa 1 Horizontal Corridor (X: 0.0 to 20.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Front Main Lobby Space (X: 7.5 to 12.5, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((7.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Rear Stair & Passage Hall (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # CONNECTING DOORWAY PASSAGE BETWEEN TÒA 1 & TÒA 2 (X: 20.0 to 23.9, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((20.0, -0.9), 3.9, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 2 Vertical Corridor (X: 23.9 to 25.7, Y: -12.5 to 0.9)
    ax.add_patch(patches.Rectangle((23.9, -12.5), 1.8, 13.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (AN GIANG 8 SURVEY DATA - 15 ROOMS TOTAL)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- TÒA 1 (TÒA CHÍNH - 10 ROOMS) ---
        # 1. North Wing (4 rooms)
        {
            'id': 'P1_10', 'name': 'Phòng số 10',
            'x': 0.0, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (1.875, 3.15),
            'door': (2.4, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_11', 'name': 'Phòng số 11',
            'x': 3.75, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (5.625, 3.15),
            'door': (6.0, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_12', 'name': 'Phòng số 12',
            'x': 12.5, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (14.375, 3.15),
            'door': (13.2, 0.9, 0.8, 'N_IN_RIGHT')
        },
        {
            'id': 'P1_13', 'name': 'Phòng số 13',
            'x': 16.25, 'y': 0.9, 'w': 3.75, 'h': 4.5,
            'text_center': (18.125, 3.15),
            'door': (17.0, 0.9, 0.8, 'N_IN_RIGHT')
        },

        # 2. South Wing (6 rooms including 2 courtrooms)
        {
            'id': 'P1_14', 'name': 'Phòng số 14',
            'x': 0.0, 'y': -4.9, 'w': 1.875, 'h': 4.0,
            'text_center': (0.9375, -2.9),
            'door': (0.8, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_15', 'name': 'Phòng số 15',
            'x': 1.875, 'y': -4.9, 'w': 1.875, 'h': 4.0,
            'text_center': (2.8125, -2.9),
            'door': (2.7, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_16', 'name': 'Phòng số 16',
            'x': 3.75, 'y': -4.9, 'w': 1.875, 'h': 4.0,
            'text_center': (4.6875, -2.9),
            'door': (4.5, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_17', 'name': 'Phòng số 17',
            'x': 5.625, 'y': -4.9, 'w': 1.875, 'h': 4.0,
            'text_center': (6.5625, -2.9),
            'door': (6.3, -0.9, 0.8, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_XX2', 'name': 'Phòng xét xử số 2',
            'x': 12.5, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (14.375, -2.9),
            'door': (13.2, -0.9, 0.9, 'S_IN_RIGHT')
        },
        {
            'id': 'P1_XX3', 'name': 'Phòng xét xử số 3',
            'x': 16.25, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (18.125, -2.9),
            'door': (17.0, -0.9, 0.9, 'S_IN_RIGHT')
        },

        # --- TÒA 2 (TÒA PHỤ - 5 ROOMS + 1 CẦU THANG) ---
        # 1. North Top Room
        {
            'id': 'P2_XX1', 'name': 'Phòng xét xử số 1',
            'x': 20.8, 'y': 0.9, 'w': 8.0, 'h': 4.5,
            'text_center': (24.8, 3.15),
            'door': (23.8, 0.9, 0.8, 'N_IN_RIGHT')
        },
        # 2. Left Wing Upper
        {
            'id': 'P2_2', 'name': 'Phòng số 2',
            'x': 20.8, 'y': -4.7, 'w': 3.1, 'h': 3.8,
            'text_center': (22.35, -2.8),
            'door': (23.9, -2.0, 0.8, 'E_IN_UP')
        },
        # 3. Left Wing Middle
        {
            'id': 'P2_3', 'name': 'Phòng số 3',
            'x': 20.8, 'y': -8.6, 'w': 3.1, 'h': 3.9,
            'text_center': (22.35, -6.65),
            'door': (23.9, -5.8, 0.8, 'E_IN_UP')
        },
        # 4. Left Wing Lower
        {
            'id': 'P2_4', 'name': 'Phòng số 4',
            'x': 20.8, 'y': -12.5, 'w': 3.1, 'h': 3.9,
            'text_center': (22.35, -10.55),
            'door': (23.9, -9.8, 0.8, 'E_IN_UP')
        },
        # 5. Right Wing (Phòng tiếp dân - Full height)
        {
            'id': 'P2_TD', 'name': 'Phòng tiếp dân',
            'x': 25.7, 'y': -12.5, 'w': 3.1, 'h': 13.4,
            'text_center': (27.25, -5.8),
            'door': (25.7, -5.5, 0.9, 'W_IN_UP')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHICS (TÒA 1 STAIRS ONLY)
    # ---------------------------------------------------------
    # --- 5.1 Central Staircase inside Tòa 1 North Hall ---
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
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

    # --- 5.2 Entrance Steps ---
    # Tòa 1 Front Main Entrance Steps at Bottom (South: Y = -4.9 to -5.7)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([7.5, 7.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([12.5, 12.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # Tòa 1 Rear Exit Steps at Top (North: Y = 5.4 to 6.2)
    for sy in [5.4, 5.56, 5.72, 5.88, 6.04, 6.20]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([7.5, 7.5], [5.4, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([12.5, 12.5], [5.4, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # Outdoor Side Steps at Tòa 1 West Exit (X = 0.0)
    for i in range(5):
        dx = -0.25 * (i + 1)
        dy = 0.9 + i * 0.1
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Outdoor Entrance Steps at Tòa 2 South Exit (Y = -12.5 to -13.3)
    for sy in [-12.5, -12.66, -12.82, -12.98, -13.14, -13.30]:
        ax.plot([23.9, 25.7], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([23.9, 23.9], [-12.5, -13.30], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([25.7, 25.7], [-12.5, -13.30], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # Labels for Lobby and Corridors
    ax.text(10.0, -2.9, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(24.8, -5.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', rotation=-90, zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (CLEAN WALL OPENINGS AT ALL DOORS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # =========================================================
    # --- TÒA 1 (TÒA CHÍNH EXTERIOR WALLS & PARTITIONS) ---
    # =========================================================
    draw_wall(-W, -4.9 - W, W, 4.0 + W)                  # West outer wall (bottom segment)
    draw_wall(-W, 0.9, W, 4.5 + W)                       # West outer wall (top segment)
    draw_wall(20.0, -4.9 - W, W, 4.0 + W)                # East outer wall (bottom segment)
    draw_wall(20.0, 0.9, W, 4.5 + W)                     # East outer wall (top segment)

    draw_wall(-W, 5.4, 7.5 + W + PART_THICKNESS/2, W)     # North outer wall (left segment)
    draw_wall(12.5 - PART_THICKNESS/2, 5.4, 7.5 + W + PART_THICKNESS/2, W) # North outer wall (right segment)
    draw_wall(-W, -4.9 - W, 7.5 + W + PART_THICKNESS/2, W)# South outer wall (left segment)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9 - W, 7.5 + W + PART_THICKNESS/2, W) # South outer wall (right segment)

    # Tòa 1 Entrance / Exit Cheek Walls
    draw_wall(7.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8) # South cheek left
    draw_wall(12.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)# South cheek right
    draw_wall(7.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)  # North cheek left
    draw_wall(12.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8) # North cheek right

    # Tòa 1 Corridor Wall Lines (Y = 0.9 & Y = -0.9)
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 2.4, PART_THICKNESS)
    draw_wall(3.2, 0.9 - PART_THICKNESS/2, 2.8, PART_THICKNESS)
    draw_wall(6.8, 0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)
    draw_wall(12.5, 0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)
    draw_wall(14.0, 0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)
    draw_wall(17.8, 0.9 - PART_THICKNESS/2, 2.2, PART_THICKNESS)

    draw_wall(0.0, -0.9 - PART_THICKNESS/2, 0.8, PART_THICKNESS)
    draw_wall(1.6, -0.9 - PART_THICKNESS/2, 1.1, PART_THICKNESS)
    draw_wall(3.5, -0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(5.3, -0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(7.1, -0.9 - PART_THICKNESS/2, 0.4, PART_THICKNESS)
    draw_wall(12.5, -0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)
    draw_wall(14.1, -0.9 - PART_THICKNESS/2, 2.9, PART_THICKNESS)
    draw_wall(17.9, -0.9 - PART_THICKNESS/2, 2.1, PART_THICKNESS)

    # Tòa 1 Internal Vertical Partitions
    draw_wall(3.75 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(7.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(12.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(16.25 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    draw_wall(1.875 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(3.75 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(5.625 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(7.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(16.25 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

    # =========================================================
    # --- CONNECTING DOORWAY PASSAGE WALLS (BETWEEN TÒA 1 & TÒA 2) ---
    # =========================================================
    draw_wall(20.0, 0.9 - PART_THICKNESS/2, 0.8, PART_THICKNESS)
    draw_wall(20.0, -0.9 - PART_THICKNESS/2, 0.8, PART_THICKNESS)

    # =========================================================
    # --- TÒA 2 (TÒA PHỤ EXTERIOR WALLS & PARTITIONS) ---
    # =========================================================
    draw_wall(20.8 - W, -12.5 - W, W, 11.6 + W)              # West outer wall (bottom segment)
    draw_wall(20.8 - W, 0.9, W, 4.5 + W)                       # West outer wall (top segment)
    draw_wall(28.8, -12.5 - W, W, 17.9 + 2*W)                  # East outer wall of Tòa 2
    draw_wall(20.8 - W, 5.4, 8.0 + 2*W, W)                     # North top wall of Tòa 2
    draw_wall(20.8 - W, -12.5 - W, 3.1 + W + PART_THICKNESS/2, W) # South bottom wall (left segment)
    draw_wall(25.7 - PART_THICKNESS/2, -12.5 - W, 3.1 + W + PART_THICKNESS/2, W) # South bottom wall (right segment)

    # Tòa 2 South Entrance Cheek Walls
    draw_wall(23.9 - PART_THICKNESS/2, -13.3, PART_THICKNESS, 0.8)
    draw_wall(25.7 - PART_THICKNESS/2, -13.3, PART_THICKNESS, 0.8)

    # Tòa 2 North Room South Partition (Y = 0.9) - SEAMLESS OVERLAP
    draw_wall(20.8 - W, 0.9 - PART_THICKNESS/2, 3.0 + W + PART_THICKNESS/2, PART_THICKNESS)  # X: 20.8-W to 23.8+
    draw_wall(24.6 - PART_THICKNESS/2, 0.9 - PART_THICKNESS/2, 4.2 + W + PART_THICKNESS/2, PART_THICKNESS)  # X: 24.6- to 28.8+W

    # Tòa 2 Left Vertical Corridor Wall (X = 23.9)
    draw_wall(23.9 - PART_THICKNESS/2, -1.2, PART_THICKNESS, 0.3 + PART_THICKNESS/2) # Y: -1.2 to -0.9
    draw_wall(23.9 - PART_THICKNESS/2, -5.0, PART_THICKNESS, 3.0) # Y: -5.0 to -2.0
    draw_wall(23.9 - PART_THICKNESS/2, -9.0, PART_THICKNESS, 3.2) # Y: -9.0 to -5.8
    draw_wall(23.9 - PART_THICKNESS/2, -12.5, PART_THICKNESS, 2.7)# Y: -12.5 to -9.8

    # Tòa 2 Right Vertical Corridor Wall (X = 25.7)
    draw_wall(25.7 - PART_THICKNESS/2, -4.6, PART_THICKNESS, 5.5 + PART_THICKNESS/2) # Y: -4.6 to 0.9+
    draw_wall(25.7 - PART_THICKNESS/2, -12.5, PART_THICKNESS, 7.0)# Y: -12.5 to -5.5

    # Tòa 2 Horizontal Room Partitions
    draw_wall(20.8, -0.9 - PART_THICKNESS/2, 3.1, PART_THICKNESS)
    draw_wall(20.8, -4.7 - PART_THICKNESS/2, 3.1, PART_THICKNESS)
    draw_wall(20.8, -8.6 - PART_THICKNESS/2, 3.1, PART_THICKNESS)

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

    # Tòa 1 North Windows
    draw_window(1.0, 5.4, 1.8, W, is_horizontal=True)    # P1_10
    draw_window(4.8, 5.4, 1.8, W, is_horizontal=True)    # P1_11
    draw_window(13.5, 5.4, 1.8, W, is_horizontal=True)   # P1_12
    draw_window(17.2, 5.4, 1.8, W, is_horizontal=True)   # P1_13

    # Tòa 1 South Windows
    draw_window(0.5, -4.9 - W, 1.0, W, is_horizontal=True) # P1_14
    draw_window(2.3, -4.9 - W, 1.0, W, is_horizontal=True) # P1_15
    draw_window(4.2, -4.9 - W, 1.0, W, is_horizontal=True) # P1_16
    draw_window(6.0, -4.9 - W, 1.0, W, is_horizontal=True) # P1_17
    draw_window(13.5, -4.9 - W, 1.8, W, is_horizontal=True)# P1_XX2
    draw_window(17.2, -4.9 - W, 1.8, W, is_horizontal=True)# P1_XX3

    # Tòa 2 North Windows
    draw_window(22.8, 5.4, 4.0, W, is_horizontal=True)   # P2_XX1

    # Tòa 2 East Outer Windows
    draw_window(28.8, -3.0, W, 2.5, is_horizontal=False) # P2_TD Upper Window
    draw_window(28.8, -9.0, W, 2.5, is_horizontal=False) # P2_TD Lower Window

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
            ax.plot([x, x - size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'W_IN_UP':
            ax.plot([x, x + size], [y, y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
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
        font_sz = 7.5 if r['w'] < 2.2 else 9.0
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.5, 31.5)
    ax.set_ylim(-16.0, 8.5)

    # Save target output in AnGiang/AnGiang8/Tang1
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\AnGiang\AnGiang8\Tang1"
    os.makedirs(target_dir, exist_ok=True)
    out_path = os.path.join(target_dir, "mat_bang_tang_1.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated AnGiang8 Floor 1 floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang1()
