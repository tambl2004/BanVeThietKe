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

def create_floorplan_tang4():
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
    COLOR_STAIR_FILL = '#ffffff'    # Pure white for staircase fill on Floor 4
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
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 4  —  Tòa án nhân dân tỉnh Đồng Nai', 
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

    # Legend Item 5: Roof
    ax.add_patch(patches.Rectangle((lg_x + 29.0, lg_y), 0.8, 0.3, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.0, zorder=1))
    ax.text(lg_x + 30.1, lg_y + 0.05, 'Mái che', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Main Building Horizontal Corridor (X: 0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Central Vertical Stair Passage (X: 13.5 to 18.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. TÒA 2 ROOF BLOCK (PLAIN WHITE BACKGROUND, NO HATCH LINES)
    # ---------------------------------------------------------
    roof_rect = patches.Rectangle((3.5 - W, 6.2 - W), 25.0 + 2*W, 8.3 + 2*W, 
                                  facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.5, zorder=2)
    ax.add_patch(roof_rect)
    
    # Roof Label in Center of Tòa 2 Roof Block
    ax.text(16.0, 10.35, 'MÁI CHE', color=COLOR_TEXT_MAIN, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 5. ROOM DEFINITIONS (TẦNG 4 — ĐỒNG NAI)
    # 4 phòng chức năng tại Tòa 1: Phòng 401, 402, 403, 404
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- TÒA 1 — NORTH WING (Y: 0.9 to 5.4m) ---
        {
            'id': 'P4_401', 'name': 'Phòng 401',
            'x': 0.0, 'y': 0.9, 'w': 13.5, 'h': 4.5,
            'text_center': (6.75, 3.15),
            'door': (11.8, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P4_402', 'name': 'Phòng 402',
            'x': 18.5, 'y': 0.9, 'w': 13.5, 'h': 4.5,
            'text_center': (25.25, 3.15),
            'door': (19.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },

        # --- TÒA 1 — SOUTH WING (Y: -4.9 to -0.9m) ---
        {
            'id': 'P4_403', 'name': 'Phòng 403',
            'x': 0.0, 'y': -4.9, 'w': 16.0, 'h': 4.0,
            'text_center': (8.0, -2.9),
            'door': (12.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P4_404', 'name': 'Phòng 404',
            'x': 16.0, 'y': -4.9, 'w': 16.0, 'h': 4.0,
            'text_center': (24.0, -2.9),
            'door': (19.5, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
    ]

    # Draw Room Background Fills
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 6. STAIRCASE (UPPER FLOOR SPEC: PURE WHITE BACKGROUND)
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

    # ---------------------------------------------------------
    # 7. DRAW WALLS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Main Building Exterior Side Walls (Enclosed at X=0 and X=32)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)
    draw_wall(X_MAX, -4.9 - W, W, 10.3 + 2*W)

    # Main Building North Top Wall (Continuous across whole top Y = 5.4m on Floor 4)
    draw_wall(-W, 5.4, X_MAX + 2*W, W)

    # Main Building South Bottom Wall (Continuous wall across whole front for Floor 4)
    draw_wall(-W, -4.9 - W, X_MAX + 2*W, W)

    # Tòa 1 Corridor Wall Lines (Y = 0.9 & Y = -0.9) with door cutouts
    # North Corridor Line Y = 0.9 (Doors at 11.8, 19.5)
    draw_wall(0.0, 0.9 - PART_THICKNESS/2, 11.8, PART_THICKNESS)
    draw_wall(12.7, 0.9 - PART_THICKNESS/2, 0.8, PART_THICKNESS)

    draw_wall(18.5, 0.9 - PART_THICKNESS/2, 1.0, PART_THICKNESS)
    draw_wall(20.4, 0.9 - PART_THICKNESS/2, 11.6, PART_THICKNESS)

    # South Corridor Line Y = -0.9 (Doors at 12.0, 19.5)
    draw_wall(0.0, -0.9 - PART_THICKNESS/2, 12.0, PART_THICKNESS)
    draw_wall(12.9, -0.9 - PART_THICKNESS/2, 6.6, PART_THICKNESS)
    draw_wall(20.4, -0.9 - PART_THICKNESS/2, 11.6, PART_THICKNESS)

    # Tòa 1 Internal Vertical Partitions
    # North Wing:
    draw_wall(13.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)
    draw_wall(18.5 - PART_THICKNESS/2, 0.9, PART_THICKNESS, 4.5)

    # South Wing: partition separating 403 & 404 at X = 16.0m
    draw_wall(16.0 - PART_THICKNESS/2, -4.9, PART_THICKNESS, 4.0)

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

    # Tòa 1 Exterior Windows
    draw_window(4.5, 5.4, 2.5, W, is_horizontal=True)    # 401 North 1
    draw_window(8.5, 5.4, 2.5, W, is_horizontal=True)    # 401 North 2
    draw_window(15.0, 5.4, 2.0, W, is_horizontal=True)   # Stair hall window overlooking roof
    draw_window(21.0, 5.4, 2.5, W, is_horizontal=True)   # 402 North 1
    draw_window(26.0, 5.4, 2.5, W, is_horizontal=True)   # 402 North 2

    draw_window(4.5, -4.9 - W, 3.0, W, is_horizontal=True)   # 403 South 1
    draw_window(10.5, -4.9 - W, 3.0, W, is_horizontal=True)  # 403 South 2
    draw_window(19.0, -4.9 - W, 3.0, W, is_horizontal=True)  # 404 South 1
    draw_window(25.0, -4.9 - W, 3.0, W, is_horizontal=True)  # 404 South 2

    # Tòa 1 Corridor End Windows (East & West)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)

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
        font_sz = r.get('font_size', 10.5)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 34.0)
    ax.set_ylim(-8.0, 16.5)

    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "mat_bang_tang_4.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 4 đã xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang4()
