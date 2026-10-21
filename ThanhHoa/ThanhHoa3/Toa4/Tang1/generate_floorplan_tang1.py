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

def create_floorplan_tang1(output_dir: str = None):
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, "mat_bang_tang_1.png")

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(18, 11), dpi=300)
    ax = fig.add_axes([0.03, 0.08, 0.94, 0.82])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Architectural Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 stair fill matches lobby color per Spec

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single line, font 20 bold, NO subtitle line)
    fig.text(0.04, 0.94, 'MẶT BẰNG TẦNG 1  —  Tòa nhà 4  —  Tòa án nhân dân khu vực 3 - Thanh Hóa', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
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

    # Legend Item 4: Door
    ax.plot([lg_x + 15.0, lg_x + 15.0], [lg_y + 0.02, lg_y + 0.32], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 15.0, lg_y + 0.02), 0.60, 0.60, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 16.3, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. LOBBY & CIRCULATION BACKGROUND FILL
    # ---------------------------------------------------------
    # Entrance Lobby & Stair Hall (East Wing: X: 15.0 to 20.0, Y: -4.9 to 5.4)
    ax.add_patch(patches.Rectangle((15.0, -4.9), 5.0, 10.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (PHÒNG XÉT XỬ HÌNH SỰ - KT: 15x7)
    # ---------------------------------------------------------
    # West Wing: Grand Criminal Trial Courtroom (X: 0.0 to 15.0, Y: -4.9 to 5.4)
    trial_room = {
        'id': 'T4_XXHS', 'name': 'Phòng xét xử hình sự',
        'x': 0.0, 'y': -4.9, 'w': 15.0, 'h': 10.3,
        'text_center': (7.5, 0.25),
        'font_size': 14.0
    }

    # Draw Room Background (Pure white `#ffffff`)
    rect = patches.Rectangle((trial_room['x'], trial_room['y']), trial_room['w'], trial_room['h'], 
                             facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
    ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS (FLOOR 1 SPECIFIC)
    # ---------------------------------------------------------
    # Staircase inside East Hall (X: 16.2 to 18.8, Y: 1.4 to 4.0)
    stair_x, stair_y, stair_w, stair_h = 16.2, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, 
                                 edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    # Horizontal tread lines across staircase
    num_treads = 9
    for i in range(1, num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Vertical divider line (Floor 1 Spec: runs from tread 2 down to bottom)
    top_tread_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    mid_x = stair_x + stair_w / 2.0
    ax.plot([mid_x, mid_x], [stair_y, top_tread_y], color=COLOR_WALL, linewidth=1.0, zorder=5)

    # Staircase label underneath box
    ax.text(mid_x, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # Entrance Lobby Label
    ax.text(17.5, -2.0, 'SẢNH ĐÓN', color=COLOR_TEXT_MAIN, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # --- OUTDOOR STEPS & CHEEK WALLS ---
    # South Front Entrance Steps (Y: -4.9 down to -5.70, X: 15.0 to 20.0)
    south_steps_y = [-5.06, -5.22, -5.38, -5.54, -5.70]
    for sy in south_steps_y:
        ax.plot([15.0, 20.0], [sy, sy], color=COLOR_WALL, linewidth=1.2, zorder=6)

    # North Rear Exit Steps (Y: 5.4 up to 6.20, X: 15.0 to 20.0)
    north_steps_y = [5.56, 5.72, 5.88, 6.04, 6.20]
    for sy in north_steps_y:
        ax.plot([15.0, 20.0], [sy, sy], color=COLOR_WALL, linewidth=1.2, zorder=6)

    # ---------------------------------------------------------
    # 6. DRAW WALLS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Wall (West facade continuous)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2 * W)

    # Rightmost Vertical Exterior Wall (East facade continuous)
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2 * W)

    # North Top Wall (continuous over trial room, opening at X: 15.0 to 20.0)
    draw_wall(-W, 5.4, 15.0 + W + P/2, W)

    # South Bottom Wall (continuous over trial room, opening at X: 15.0 to 20.0)
    draw_wall(-W, -4.9 - W, 15.0 + W + P/2, W)

    # Structural Wall Cheeks & Hooks (Floor 1 Spec)
    # South Front Entrance Side Wall Cheeks
    draw_wall(15.0 - P/2, -5.7, P, 0.8)
    draw_wall(20.0 - P/2, -5.7, P, 0.8)

    # North Rear Exit Side Wall Cheeks & Hooks
    draw_wall(15.0 - P/2, 5.4, P, 0.8)
    draw_wall(20.0 - P/2, 5.4, P, 0.8)
    draw_wall(15.0 - P/2, 6.2 - P, 0.5, P)
    draw_wall(20.0 + P/2 - 0.5, 6.2 - P, 0.5, P)

    # Partition Wall at X = 15.0 separating Trial Room from Lobby/Stairs
    # Door 1: Double door at Y = -1.5 (opening from Y: -2.2 to -0.8, size = 1.4m)
    # Door 2: Single door at Y = 2.5 (opening from Y: 2.075 to 2.925, size = 0.85m)
    draw_wall(15.0 - P/2, -4.9, P, 2.7)                # Segment from -4.9 to -2.2
    draw_wall(15.0 - P/2, -0.8, P, 2.875)              # Segment from -0.8 to 2.075
    draw_wall(15.0 - P/2, 2.925, P, 5.4 - 2.925)      # Segment from 2.925 to 5.4

    # ---------------------------------------------------------
    # 7. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    # Double door opening from Lobby into Trial Room at X = 15.0, Y = -1.5
    d_x, d_y = 15.0, -1.5
    half_d = 0.7
    # Door leaf panels
    ax.plot([d_x - half_d, d_x], [d_y - half_d, d_y - half_d], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
    ax.plot([d_x - half_d, d_x], [d_y + half_d, d_y + half_d], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=15)
    # Door swing arcs
    arc1 = patches.Arc((d_x, d_y - half_d), half_d * 2, half_d * 2, angle=0, theta1=90, theta2=180, 
                       color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
    arc2 = patches.Arc((d_x, d_y + half_d), half_d * 2, half_d * 2, angle=0, theta1=180, theta2=270, 
                       color=COLOR_DOOR_SWING, linewidth=1.1, zorder=14)
    ax.add_patch(arc1)
    ax.add_patch(arc2)

    # Secondary single door opening from Stair Hall into Trial Room at X = 15.0, Y = 2.075
    sd_x, sd_y, sd_sz = 15.0, 2.075, 0.85
    ax.plot([sd_x - sd_sz, sd_x], [sd_y, sd_y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
    arc_sd = patches.Arc((sd_x, sd_y), sd_sz * 2, sd_sz * 2, angle=0, theta1=90, theta2=180, 
                         color=COLOR_DOOR_SWING, linewidth=1.0, zorder=14)
    ax.add_patch(arc_sd)

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

    # Top Windows (North Facade: Y = 5.4)
    draw_window(1.8, 5.4, 2.5, W, is_horizontal=True)      # Trial Room window 1
    draw_window(5.8, 5.4, 2.5, W, is_horizontal=True)      # Trial Room window 2
    draw_window(9.8, 5.4, 2.5, W, is_horizontal=True)      # Trial Room window 3

    # Bottom Windows (South Front Facade: Y = -4.9 - W)
    draw_window(1.8, -4.9 - W, 2.5, W, is_horizontal=True)  # Trial Room window 1
    draw_window(5.8, -4.9 - W, 2.5, W, is_horizontal=True)  # Trial Room window 2
    draw_window(9.8, -4.9 - W, 2.5, W, is_horizontal=True)  # Trial Room window 3

    # Side Windows
    # West Facade (X = -W)
    draw_window(-W, 2.2, W, 2.0, is_horizontal=False)       # Trial Room West window North
    draw_window(-W, -1.0, W, 2.0, is_horizontal=False)      # Trial Room West window Center
    draw_window(-W, -4.2, W, 2.0, is_horizontal=False)      # Trial Room West window South

    # East Facade (X = 20.0)
    draw_window(20.0, 2.2, W, 2.0, is_horizontal=False)     # Stair hall window
    draw_window(20.0, -3.8, W, 2.0, is_horizontal=False)    # Sảnh đón window

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS
    # ---------------------------------------------------------
    cx, cy = trial_room['text_center']
    ax.text(cx, cy, trial_room['name'], color=COLOR_TEXT_MAIN, 
            fontsize=trial_room['font_size'], fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 22.0)
    ax.set_ylim(-8.5, 8.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Toa 4 Floor 1 floorplan PNG at {out_img_path}")
    plt.close(fig)

if __name__ == '__main__':
    create_floorplan_tang1()
