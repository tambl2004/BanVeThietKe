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
    fig.text(0.03, 0.955, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 7 - An Giang', color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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
    # Tòa 1 Horizontal Corridor (X: 0 to 20.0, Y: -0.9 to 0.9)
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
    # 4. ROOM DEFINITIONS (AN GIANG 7 SURVEY DATA - 11 ROOMS TOTAL)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- TÒA 1 (TÒA CHÍNH - 5 ROOMS) ---
        # 1. Phòng làm việc (11.5 x 6) - North-West Wing
        {
            'id': 'P1_1', 'name': 'Phòng làm việc',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'door': (6.0, 0.9, 0.8, 'N_IN_RIGHT')
        },
        # 2. Phòng họp (15 x 6.5) - North-East Wing
        {
            'id': 'P1_2', 'name': 'Phòng họp',
            'x': 12.5, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (16.25, 3.15),
            'door': (13.2, 0.9, 0.8, 'N_IN_RIGHT')
        },
        # 3. Phòng làm việc (5.7 x 3.7) - South-West Wing Left
        {
            'id': 'P1_3', 'name': 'Phòng làm việc',
            'x': 0.0, 'y': -4.9, 'w': 4.2, 'h': 4.0,
            'text_center': (2.1, -2.9),
            'door': (2.8, -0.9, 0.8, 'S_IN_RIGHT')
        },
        # 4. Phòng làm việc (4.5 x 3.5) - South-West Wing Right
        {
            'id': 'P1_4', 'name': 'Phòng làm việc',
            'x': 4.2, 'y': -4.9, 'w': 3.3, 'h': 4.0,
            'text_center': (5.85, -2.9),
            'door': (4.8, -0.9, 0.8, 'S_IN_RIGHT')
        },
        # 5. Phòng xử án (11.5 x 6) - South-East Wing
        {
            'id': 'P1_5', 'name': 'Phòng xử án',
            'x': 12.5, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (16.25, -2.9),
            'door': (13.2, -0.9, 0.9, 'S_IN_RIGHT')
        },

        # --- TÒA 2 (TÒA PHỤ - 6 ROOMS) ---
        # 6. Phòng làm việc 1 - North Room of Tòa 2
        {
            'id': 'P2_1', 'name': 'Phòng làm việc',
            'x': 20.8, 'y': 0.9, 'w': 8.0, 'h': 4.5,
            'text_center': (24.8, 3.15),
            'door': (23.8, 0.9, 0.8, 'N_IN_RIGHT')
        },
        # 7. Phòng làm việc 2 - Left Wing Upper
        {
            'id': 'P2_2', 'name': 'Phòng làm việc',
            'x': 20.8, 'y': -4.7, 'w': 3.1, 'h': 3.8,
            'text_center': (22.35, -2.8),
            'door': (23.9, -2.0, 0.8, 'E_IN_UP')
        },
        # 8. Phòng làm việc 3 - Left Wing Middle
        {
            'id': 'P2_3', 'name': 'Phòng làm việc',
            'x': 20.8, 'y': -8.6, 'w': 3.1, 'h': 3.9,
            'text_center': (22.35, -6.65),
            'door': (23.9, -5.8, 0.8, 'E_IN_UP')
        },
        # 9. Phòng làm việc 4 - Left Wing Lower
        {
            'id': 'P2_4', 'name': 'Phòng làm việc',
            'x': 20.8, 'y': -12.5, 'w': 3.1, 'h': 3.9,
            'text_center': (22.35, -10.55),
            'door': (23.9, -9.8, 0.8, 'E_IN_UP')
        },
        # 10. Phòng làm việc 5 - Right Wing Middle
        {
            'id': 'P2_5', 'name': 'Phòng làm việc',
            'x': 25.7, 'y': -7.2, 'w': 3.1, 'h': 5.4,
            'text_center': (27.25, -4.5),
            'door': (25.7, -3.5, 0.8, 'W_IN_UP')
        },
        # 11. Phòng làm việc 6 - Right Wing Lower
        {
            'id': 'P2_6', 'name': 'Phòng làm việc',
            'x': 25.7, 'y': -12.5, 'w': 3.1, 'h': 5.3,
            'text_center': (27.25, -9.8),
            'door': (25.7, -8.8, 0.8, 'W_IN_UP')
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS
    # ---------------------------------------------------------
    # --- 5.1 Central Staircase inside Tòa 1 North Hall ---
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Vertical divider line down center starting from step 2
    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Staircase label underneath box
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # --- 5.2 Tòa 2 Upper Right Staircase (X: 25.7 to 28.8, Y: -1.8 to 0.9) ---
    stair2_x, stair2_y, stair2_w, stair2_h = 25.7, -1.8, 3.1, 2.7
    stair2_bg = patches.Rectangle((stair2_x, stair2_y), stair2_w, stair2_h, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=3)
    ax.add_patch(stair2_bg)

    # Draw North, East, South outline of Tòa 2 Staircase box (West X=25.7 open to corridor)
    ax.plot([stair2_x, stair2_x + stair2_w], [stair2_y + stair2_h, stair2_y + stair2_h], color=COLOR_WALL, linewidth=1.1, zorder=4) # North wall
    ax.plot([stair2_x + stair2_w, stair2_x + stair2_w], [stair2_y, stair2_y + stair2_h], color=COLOR_WALL, linewidth=1.1, zorder=4) # East outer wall
    ax.plot([stair2_x, stair2_x + stair2_w], [stair2_y, stair2_y], color=COLOR_WALL, linewidth=1.1, zorder=4) # South partition wall

    for i in range(num_treads + 1):
        sy = stair2_y + i * (stair2_h / num_treads)
        ax.plot([stair2_x, stair2_x + stair2_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid2_x = stair2_x + stair2_w / 2.0
    ax.plot([mid2_x, mid2_x], [stair2_y, stair2_y + stair2_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair2_x + stair2_w / 2.0, stair2_y + stair2_h / 2.0, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=5)

    # 1. Tòa 1 Front Main Entrance Steps at Bottom (South: Y = -4.9 to -5.7)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([7.5, 7.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([12.5, 12.5], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # 2. Tòa 1 Rear Exit Steps at Top (North: Y = 5.4 to 6.2)
    for sy in [5.4, 5.56, 5.72, 5.88, 6.04, 6.20]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([7.5, 7.5], [5.4, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([12.5, 12.5], [5.4, 6.20], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([7.5, 8.0], [6.20, 6.20], color=COLOR_WALL, linewidth=1.4, zorder=4)
    ax.plot([12.0, 12.5], [6.20, 6.20], color=COLOR_WALL, linewidth=1.4, zorder=4)

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
    ax.text(24.8, -2.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='center', rotation=-90, zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (CLEAN WALL OPENINGS AT ALL DOORS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # =========================================================
    # --- TÒA 1 (TÒA CHÍNH EXTERIOR WALLS) ---
    # =========================================================
    draw_wall(-W, -4.9 - W, W, 4.0 + W)                  # West outer wall (bottom segment)
    draw_wall(-W, 0.9, W, 4.5 + W)                       # West outer wall (top segment)

    draw_wall(20.0, -4.9 - W, W, 4.0 + W)                # East outer wall (bottom segment Y: -4.9-W to -0.9)
    draw_wall(20.0, 0.9, W, 4.5 + W)                     # East outer wall (top segment Y: 0.9 to 5.4+W)

    draw_wall(-W, 5.4, 7.5 + W + PART_THICKNESS/2, W)     # North outer wall (left segment)
    draw_wall(12.5 - PART_THICKNESS/2, 5.4, 7.5 + W + PART_THICKNESS/2, W) # North outer wall (right segment)

    draw_wall(-W, -4.9 - W, 7.5 + W + PART_THICKNESS/2, W)# South outer wall (left segment)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9 - W, 7.5 + W + PART_THICKNESS/2, W) # South outer wall (right segment)

    # Tòa 1 Entrance / Exit Cheek Walls & Hooks
    draw_wall(7.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8) # South cheek left
    draw_wall(12.5 - PART_THICKNESS/2, -5.7, PART_THICKNESS, 0.8)# South cheek right

    draw_wall(7.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8)  # North cheek left
    draw_wall(12.5 - PART_THICKNESS/2, 5.4, PART_THICKNESS, 0.8) # North cheek right
    draw_wall(7.5 - PART_THICKNESS/2, 6.2 - PART_THICKNESS, 0.5, PART_THICKNESS) # Hook left
    draw_wall(12.5 + PART_THICKNESS/2 - 0.5, 6.2 - PART_THICKNESS, 0.5, PART_THICKNESS) # Hook right

    # Tòa 1 Corridor Wall Lines with CLEAN DOOR CUTOUTS (Y = 0.9 & Y = -0.9)
    # North Corridor Wall (Y = 0.9)
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 6.0, PART_THICKNESS)   # P1_1 before door
    draw_wall(6.8, 0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)   # P1_1 after door to stair hall
    draw_wall(12.5, 0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS)  # Stair hall to P1_2 door
    draw_wall(14.0, 0.9 - PART_THICKNESS/2, 6.0, PART_THICKNESS)  # P1_2 after door

    # South Corridor Wall (Y = -0.9)
    draw_wall(0.0, -0.9 - PART_THICKNESS/2, 2.8, PART_THICKNESS)  # P1_3 before door
    draw_wall(3.6, -0.9 - PART_THICKNESS/2, 1.2, PART_THICKNESS)  # Between P1_3 & P1_4 door
    draw_wall(5.6, -0.9 - PART_THICKNESS/2, 1.9, PART_THICKNESS)  # P1_4 after door
    draw_wall(12.5, -0.9 - PART_THICKNESS/2, 0.7, PART_THICKNESS) # Lobby to P1_5 door
    draw_wall(14.1, -0.9 - PART_THICKNESS/2, 5.9, PART_THICKNESS) # P1_5 after door

    # Tòa 1 Internal Vertical Partitions
    draw_wall(7.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(12.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    draw_wall(4.2 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(7.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)
    draw_wall(12.5 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

    # =========================================================
    # --- CONNECTING DOORWAY PASSAGE WALLS (BETWEEN TÒA 1 & TÒA 2) ---
    # =========================================================
    draw_wall(20.0, 0.9 - PART_THICKNESS/2, 0.8, PART_THICKNESS)
    draw_wall(20.0, -0.9 - PART_THICKNESS/2, 0.8, PART_THICKNESS)

    # =========================================================
    # --- TÒA 2 (TÒA PHỤ EXTERIOR WALLS & PARTITIONS) ---
    # =========================================================
    # West outer wall of Tòa 2 (X = 20.8 - W, split at Y: -0.9 to 0.9 for connecting doorway, NO WINDOWS)
    draw_wall(20.8 - W, -12.5 - W, W, 11.6 + W)              # Bottom segment Y: -12.5-W to -0.9
    draw_wall(20.8 - W, 0.9, W, 4.5 + W)                       # Top segment Y: 0.9 to 5.4+W

    draw_wall(28.8, -12.5 - W, W, 17.9 + 2*W)                  # East outer wall of Tòa 2

    draw_wall(20.8 - W, 5.4, 8.0 + 2*W, W)                     # North top wall of Tòa 2 (Flush top line with Tòa 1)

    draw_wall(20.8 - W, -12.5 - W, 3.1 + W + PART_THICKNESS/2, W) # South bottom wall (left segment)
    draw_wall(25.7 - PART_THICKNESS/2, -12.5 - W, 3.1 + W + PART_THICKNESS/2, W) # South bottom wall (right segment)

    # Tòa 2 South Entrance Cheek Walls (Y = -12.5 down to -13.3)
    draw_wall(23.9 - PART_THICKNESS/2, -13.3, PART_THICKNESS, 0.8)
    draw_wall(25.7 - PART_THICKNESS/2, -13.3, PART_THICKNESS, 0.8)

    # Tòa 2 North Room South Partition (Y = 0.9) with CLEAN DOOR CUTOUT for P2_1
    draw_wall(20.8, 0.9 - PART_THICKNESS/2, 3.0, PART_THICKNESS)  # X: 20.8 to 23.8
    draw_wall(24.6, 0.9 - PART_THICKNESS/2, 4.2, PART_THICKNESS)  # X: 24.6 to 28.8

    # Tòa 2 Left Vertical Corridor Wall (X = 23.9) with CLEAN DOOR CUTOUTS
    draw_wall(23.9 - PART_THICKNESS/2, -1.2, PART_THICKNESS, 0.3) # Y: -0.9 to -1.2
    draw_wall(23.9 - PART_THICKNESS/2, -5.0, PART_THICKNESS, 3.0) # Y: -5.0 to -2.0
    draw_wall(23.9 - PART_THICKNESS/2, -9.0, PART_THICKNESS, 3.2) # Y: -9.0 to -5.8
    draw_wall(23.9 - PART_THICKNESS/2, -12.5, PART_THICKNESS, 2.7)# Y: -12.5 to -9.8

    # Tòa 2 Right Vertical Corridor Wall (X = 25.7) - OPEN AT STAIRCASE (Y: -1.8 to 0.9)
    draw_wall(25.7 - PART_THICKNESS/2, -2.7, PART_THICKNESS, 0.9) # Y: -2.7 to -1.8 (Below staircase open entry)
    draw_wall(25.7 - PART_THICKNESS/2, -8.0, PART_THICKNESS, 4.5) # Y: -8.0 to -3.5
    draw_wall(25.7 - PART_THICKNESS/2, -12.5, PART_THICKNESS, 3.7)# Y: -12.5 to -8.8

    # Tòa 2 Horizontal Room Partitions
    draw_wall(20.8, -0.9 - PART_THICKNESS/2, 3.1, PART_THICKNESS) # Y: -0.9 (Top wall of P2_2)
    draw_wall(20.8, -4.7 - PART_THICKNESS/2, 3.1, PART_THICKNESS)
    draw_wall(20.8, -8.6 - PART_THICKNESS/2, 3.1, PART_THICKNESS)
    draw_wall(25.7, -1.8 - PART_THICKNESS/2, 3.1 + W, PART_THICKNESS) # Staircase South Wall | P2_5
    draw_wall(25.7, -7.2 - PART_THICKNESS/2, 3.1 + W, PART_THICKNESS) # P2_5 | P2_6

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
    draw_window(2.5, 5.4, 2.5, W, is_horizontal=True)    # P1_1
    draw_window(15.0, 5.4, 2.5, W, is_horizontal=True)   # P1_2

    # Tòa 1 South Windows
    draw_window(1.2, -4.9 - W, 1.8, W, is_horizontal=True) # P1_3
    draw_window(4.8, -4.9 - W, 1.8, W, is_horizontal=True) # P1_4
    draw_window(15.0, -4.9 - W, 2.5, W, is_horizontal=True)# P1_5

    # Tòa 2 North Windows
    draw_window(22.8, 5.4, 4.0, W, is_horizontal=True)   # P2_1

    # Tòa 2 East Outer Windows
    draw_window(28.8, -3.5, W, 1.5, is_horizontal=False) # P2_5
    draw_window(28.8, -9.5, W, 1.5, is_horizontal=False) # P2_6

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
        font_sz = 8.5 if r['w'] < 4.0 else 9.5
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.5, 31.5)
    ax.set_ylim(-16.0, 8.5)

    # Save target output in AnGiang/AnGiang7/Tang1
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\AnGiang\AnGiang7\Tang1"
    os.makedirs(target_dir, exist_ok=True)
    out_path = os.path.join(target_dir, "mat_bang_tang_1.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated AnGiang7 Floor 1 (Clean Doors & Wall Cutouts) floorplan PNG at {out_path}")

    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang1()
