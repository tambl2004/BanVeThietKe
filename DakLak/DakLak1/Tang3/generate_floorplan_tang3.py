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
    P = PART_THICKNESS
    X_MAX = 32.0            # Main building length = 32.0m

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 3  —  Tòa án nhân dân khu vực 1 - Đắk Lắk', 
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

    # Legend Item 4: Roof
    ax.add_patch(patches.Rectangle((lg_x + 22.0, lg_y), 0.8, 0.3, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.0, zorder=1))
    ax.text(lg_x + 23.1, lg_y + 0.05, 'Mái che', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. LOBBY & STAIR BACKGROUND FILL
    # ---------------------------------------------------------
    # Central Lobby & Stair Hall (X: 13.5 to 18.5, Y: -4.9 to 5.4)
    ax.add_patch(patches.Rectangle((13.5, -4.9), 5.0, 10.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. TÒA 2 ROOF BLOCK (PLAIN WHITE BACKGROUND, NO HATCH LINES)
    # ---------------------------------------------------------
    roof_rect = patches.Rectangle((3.5 - W, 6.2 - W), 25.0 + 2*W, 8.3 + 2*W, 
                                  facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.5, zorder=2)
    ax.add_patch(roof_rect)
    
    # Roof Label in Center of Tòa 2 Roof Block
    ax.text(16.0, 10.35, 'MÁI CHE', color=COLOR_TEXT_MAIN, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 5. ROOM DEFINITIONS (TÒA 1 - EXACTLY 2 ROOMS AS SPECIFIED)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === PHÒNG 1: Phòng hòa giải đối thoại (Toàn bộ Cánh Tây: X: 0.0 -> 13.5m, Y: -4.9 -> 5.4m) ===
        {
            'id': 'T3_HOAGIAI', 'name': 'Phòng hòa giải đối thoại',
            'x': 0.0, 'y': -4.9, 'w': 13.5, 'h': 10.3,
            'text_center': (6.75, 0.25),
            'door': (13.5, 0.5, 1.0, 'W_IN_ROOM'),
            'font_size': 11.5
        },
        # === PHÒNG 2: Phòng nghị án (Toàn bộ Cánh Đông: X: 18.5 -> 32.0m, Y: -4.9 -> 5.4m) ===
        {
            'id': 'T3_NGHIAN', 'name': 'Phòng nghị án',
            'x': 18.5, 'y': -4.9, 'w': 13.5, 'h': 10.3,
            'text_center': (25.25, 0.25),
            'door': (18.5, 0.5, 1.0, 'E_IN_ROOM'),
            'font_size': 11.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
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

    # Label for Central Lobby
    ax.text(16.0, -1.8, 'SẢNH TẦNG 3', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 7. DRAW WALLS (EXACT ALIGNED SEGMENTS, NO GAPS OR OVERLAPS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Main Building Exterior Side Walls (Enclosed at ends X=0 and X=32 for Floor 3)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)
    draw_wall(X_MAX, -4.9 - W, W, 10.3 + 2*W)

    # Main Building North Top Wall (Continuous across whole top Y = 5.4m on Floor 3)
    draw_wall(-W, 5.4, X_MAX + 2*W, W)

    # Main Building South Bottom Wall (Continuous wall across whole front for Floor 3)
    draw_wall(-W, -4.9 - W, X_MAX + 2*W, W)

    # Tòa 1 Internal Vertical Partitions dividing Central Lobby from Rooms:
    # 1. West Partition at X = 13.5m (Door opening from Y = -0.5 to 0.5m)
    draw_wall(13.5 - P/2, -4.9, P, 4.4)   # From Y = -4.9 to -0.5m
    draw_wall(13.5 - P/2, 0.5, P, 4.9)    # From Y = 0.5 to 5.4m

    # 2. East Partition at X = 18.5m (Door opening from Y = -0.5 to 0.5m)
    draw_wall(18.5 - P/2, -4.9, P, 4.4)   # From Y = -4.9 to -0.5m
    draw_wall(18.5 - P/2, 0.5, P, 4.9)    # From Y = 0.5 to 5.4m

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

    # Tòa 1 North Exterior Windows (Y = 5.4)
    draw_window(2.5, 5.4, 3.5, W, is_horizontal=True)     # Hòa giải North
    draw_window(8.0, 5.4, 3.5, W, is_horizontal=True)     # Hòa giải North
    draw_window(14.5, 5.4, 3.0, W, is_horizontal=True)    # Central Stair Hall window looking out to Tòa 2 roof
    draw_window(20.5, 5.4, 3.5, W, is_horizontal=True)    # Nghị án North
    draw_window(26.0, 5.4, 3.5, W, is_horizontal=True)    # Nghị án North

    # Tòa 1 South Exterior Windows (Y = -4.9 - W)
    draw_window(2.5, -4.9 - W, 3.5, W, is_horizontal=True)  # Hòa giải South
    draw_window(8.0, -4.9 - W, 3.5, W, is_horizontal=True)  # Hòa giải South
    draw_window(14.5, -4.9 - W, 3.0, W, is_horizontal=True) # Sảnh Tầng 3 South window
    draw_window(20.5, -4.9 - W, 3.5, W, is_horizontal=True) # Nghị án South
    draw_window(26.0, -4.9 - W, 3.5, W, is_horizontal=True) # Nghị án South

    # Tòa 1 Side Windows
    draw_window(-W, 2.0, W, 2.0, is_horizontal=False)       # Hòa giải West upper
    draw_window(-W, -3.5, W, 2.0, is_horizontal=False)      # Hòa giải West lower
    draw_window(X_MAX, 2.0, W, 2.0, is_horizontal=False)    # Nghị án East upper
    draw_window(X_MAX, -3.5, W, 2.0, is_horizontal=False)   # Nghị án East lower

    # ---------------------------------------------------------
    # 9. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode == 'W_IN_ROOM':
            # Door at X = 13.5 opening into West Room (swinging left into Room)
            # Pivot at (x, y - size) = (13.5, -0.5), door swings inwards to (12.5, -0.5)
            pivot_y = y - size
            ax.plot([x, x - size], [pivot_y, pivot_y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, pivot_y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
            ax.add_patch(arc)
        elif mode == 'E_IN_ROOM':
            # Door at X = 18.5 opening into East Room (swinging right into Room)
            # Pivot at (x, y - size) = (18.5, -0.5), door swings inwards to (19.5, -0.5)
            pivot_y = y - size
            ax.plot([x, x + size], [pivot_y, pivot_y], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, pivot_y), size*2, size*2, angle=0, theta1=0, theta2=90,
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
        font_sz = r.get('font_size', 11.5)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 34.0)
    ax.set_ylim(-8.0, 16.5)

    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "mat_bang_tang_3.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {output_path}")

if __name__ == "__main__":
    create_floorplan_tang3()
