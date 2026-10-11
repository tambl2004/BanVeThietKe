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
    font_size: float

def create_floorplan_tang2(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_2.png')

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
    COLOR_STAIR_FILL = '#ffffff'    # Stair fill is pure white for Floor 2 per Spec

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.04, 0.94, 'MẶT BẰNG TẦNG 2  —  TÒA ÁN NHÂN DÂN KHU VỰC 4 - CÀ MAU', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.04, 0.96], [0.915, 0.915], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = 0.5, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 5.5, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 6.6, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 10.5, lg_x + 11.3], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 10.5, lg_x + 11.3], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 11.6, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 15.5, lg_x + 15.5], [lg_y + 0.02, lg_y + 0.28], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 15.5, lg_y + 0.02), 0.52, 0.52, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 16.6, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (ENCLOSED ON FLOOR 2)
    # ---------------------------------------------------------
    # Horizontal Corridor (X: 0.0 to 20.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Stair Hall on North (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (ALL 9 ROOMS STRICTLY MATCHING PROMPT)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- North Wing (Y: 0.9 to 5.4m, H = 4.5m) ---
        # West North (3 rooms, width 2.5m each)
        {
            'id': 'P2_NW1', 'name': 'Phòng Phó Chánh\nVăn - Phòng',
            'x': 0.0, 'y': 0.9, 'w': 2.5, 'h': 4.5,
            'text_center': (1.25, 3.15),
            'font_size': 7.6
        },
        {
            'id': 'P2_NW2', 'name': 'Phòng\nThẩm phán',
            'x': 2.5, 'y': 0.9, 'w': 2.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'font_size': 7.8
        },
        {
            'id': 'P2_NW3', 'name': 'Phòng Phó\nChánh án',
            'x': 5.0, 'y': 0.9, 'w': 2.5, 'h': 4.5,
            'text_center': (6.25, 3.15),
            'font_size': 7.8
        },

        # East North (3 rooms, width 2.5m each)
        {
            'id': 'P2_NE1', 'name': 'Phòng Thẩm phán -\nChánh toà dân sự',
            'x': 12.5, 'y': 0.9, 'w': 2.5, 'h': 4.5,
            'text_center': (13.75, 3.15),
            'font_size': 7.5
        },
        {
            'id': 'P2_NE2', 'name': 'Phòng\nThẩm phán',
            'x': 15.0, 'y': 0.9, 'w': 2.5, 'h': 4.5,
            'text_center': (16.25, 3.15),
            'font_size': 7.8
        },
        {
            'id': 'P2_NE3', 'name': 'Phòng Thẩm phán\nsơ cấp',
            'x': 17.5, 'y': 0.9, 'w': 2.5, 'h': 4.5,
            'text_center': (18.75, 3.15),
            'font_size': 7.6
        },

        # --- South Wing (Y: -4.9 to -0.9m, H = 4.0m) ---
        # West South
        {
            'id': 'P2_SW', 'name': 'Phòng Chánh án',
            'x': 0.0, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (3.75, -2.9),
            'font_size': 11.0
        },
        # Center South (Replaces floor 1 lobby per upper floor spec)
        {
            'id': 'P2_SC', 'name': 'Phòng Thẩm phán',
            'x': 7.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (10.0, -2.9),
            'font_size': 10.5
        },
        # East South
        {
            'id': 'P2_SE', 'name': 'Phòng Phó Chánh án',
            'x': 12.5, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (16.25, -2.9),
            'font_size': 11.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE (TẦNG 2: NỀN TRẮNG, HƯỚNG ĐI XUỐNG TẦNG 1)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.8
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 10
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Down arrow on staircase
    ax.annotate('', xy=(mid_x - 0.6, stair_y + 0.4), xytext=(mid_x - 0.6, stair_y + 2.2),
                arrowprops=dict(arrowstyle="->", color=COLOR_WALL, lw=1.2), zorder=6)
    ax.text(mid_x - 0.6, stair_y + 2.4, 'XUỐNG', color=COLOR_TEXT_MUTED, fontsize=7.5, ha='center', va='bottom', zorder=6)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.25, 'Cầu thang bộ (Xuống tầng 1)', 
            color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', ha='center', va='top', zorder=5)

    # Corridor labels
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(10.0, 0.0, 'SẢNH TẦNG 2', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW STRUCTURAL WALLS (ENCLOSED PERIMETER ON FLOOR 2)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior Perimeter Walls (Enclosed on all 4 sides on Floor 2)
    # North Exterior Wall (Continuous from -W to 20.0+W)
    draw_wall(-W, 5.4, 20.0 + 2*W, W)

    # South Exterior Wall (Continuous from -W to 20.0+W)
    draw_wall(-W, -4.9 - W, 20.0 + 2*W, W)

    # West Exterior Wall (Continuous from -4.9-W to 5.4+W)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)

    # East Exterior Wall (Continuous from -4.9-W to 5.4+W)
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2*W)

    # Internal Vertical Partitions
    # North Wing Partitions (Y: 0.9 to 5.4)
    draw_wall(2.5 - P/2, 0.9, P, 4.5)   # P2_NW1 & P2_NW2
    draw_wall(5.0 - P/2, 0.9, P, 4.5)   # P2_NW2 & P2_NW3
    draw_wall(7.5 - P/2, 0.9, P, 4.5)   # P2_NW3 & Stair Hall
    draw_wall(12.5 - P/2, 0.9, P, 4.5)  # Stair Hall & P2_NE1
    draw_wall(15.0 - P/2, 0.9, P, 4.5)  # P2_NE1 & P2_NE2
    draw_wall(17.5 - P/2, 0.9, P, 4.5)  # P2_NE2 & P2_NE3

    # South Wing Partitions (Y: -4.9 to -0.9)
    draw_wall(7.5 - P/2, -4.9, P, 4.0)  # P2_SW & P2_SC
    draw_wall(12.5 - P/2, -4.9, P, 4.0) # P2_SC & P2_SE

    # North Corridor Partition Wall (Y = 0.9) with Door Openings
    # P2_NW1: door 1.5 to 2.3
    draw_wall(0.0, 0.9 - P/2, 1.5, P)
    # P2_NW2: door 3.8 to 4.6
    draw_wall(2.3, 0.9 - P/2, 1.5, P)
    # P2_NW3: door 6.3 to 7.1
    draw_wall(4.6, 0.9 - P/2, 1.7, P)
    draw_wall(7.1, 0.9 - P/2, 0.4, P)
    # Stair Hall opening: X: 7.5 to 12.5 (completely open to corridor)
    # P2_NE1: door 12.9 to 13.7
    draw_wall(12.5, 0.9 - P/2, 0.4, P)
    # P2_NE2: door 15.4 to 16.2
    draw_wall(13.7, 0.9 - P/2, 1.7, P)
    # P2_NE3: door 17.9 to 18.7
    draw_wall(16.2, 0.9 - P/2, 1.7, P)
    draw_wall(18.7, 0.9 - P/2, 1.3, P)

    # South Corridor Partition Wall (Y = -0.9) with Door Openings
    # P2_SW: door 5.9 to 6.8
    draw_wall(0.0, -0.9 - P/2, 5.9, P)
    draw_wall(6.8, -0.9 - P/2, 0.7, P)
    # P2_SC: door 9.5 to 10.4
    draw_wall(7.5, -0.9 - P/2, 2.0, P)
    draw_wall(10.4, -0.9 - P/2, 2.1, P)
    # P2_SE: door 13.2 to 14.1
    draw_wall(12.5, -0.9 - P/2, 0.7, P)
    draw_wall(14.1, -0.9 - P/2, 5.9, P)

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

    # North Windows (Facade Bắc)
    draw_window(0.5, 5.4, 1.5, W, is_horizontal=True)    # P2_NW1
    draw_window(3.0, 5.4, 1.5, W, is_horizontal=True)    # P2_NW2
    draw_window(5.5, 5.4, 1.5, W, is_horizontal=True)    # P2_NW3
    draw_window(9.0, 5.4, 2.0, W, is_horizontal=True)    # Stair Hall North Window
    draw_window(13.0, 5.4, 1.5, W, is_horizontal=True)   # P2_NE1
    draw_window(15.5, 5.4, 1.5, W, is_horizontal=True)   # P2_NE2
    draw_window(18.0, 5.4, 1.5, W, is_horizontal=True)   # P2_NE3

    # South Windows (Facade Nam)
    draw_window(1.5, -4.9 - W, 2.0, W, is_horizontal=True)  # P2_SW window 1
    draw_window(4.5, -4.9 - W, 2.0, W, is_horizontal=True)  # P2_SW window 2
    draw_window(8.75, -4.9 - W, 2.5, W, is_horizontal=True) # P2_SC window
    draw_window(13.5, -4.9 - W, 2.0, W, is_horizontal=True) # P2_SE window 1
    draw_window(16.5, -4.9 - W, 2.0, W, is_horizontal=True) # P2_SE window 2

    # West Gable Windows (Facade Tây)
    draw_window(-W, 2.2, W, 2.0, is_horizontal=False)   # P2_NW1 West window
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)  # West Corridor End Window
    draw_window(-W, -3.8, W, 2.0, is_horizontal=False)  # P2_SW West window

    # East Gable Windows (Facade Đông)
    draw_window(20.0, 2.2, W, 2.0, is_horizontal=False)  # P2_NE3 East window
    draw_window(20.0, -0.6, W, 1.2, is_horizontal=False) # East Corridor End Window
    draw_window(20.0, -3.8, W, 2.0, is_horizontal=False) # P2_SE East window

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door_h(x1, x2, y, into='north', hinge='left'):
        size = x2 - x1
        if into == 'north':
            if hinge == 'left':
                ax.plot([x1, x1], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x1, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
            else: # hinge == 'right'
                ax.plot([x2, x2], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x2, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
        elif into == 'south':
            if hinge == 'left':
                ax.plot([x1, x1], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x1, y), size*2, size*2, angle=0, theta1=270, theta2=360,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)
            else: # hinge == 'right'
                ax.plot([x2, x2], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
                arc = patches.Arc((x2, y), size*2, size*2, angle=0, theta1=180, theta2=270,
                                  color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
                ax.add_patch(arc)

    # North Corridor Doors (into North rooms)
    draw_door_h(1.5, 2.3, 0.9, into='north', hinge='left')   # P2_NW1
    draw_door_h(3.8, 4.6, 0.9, into='north', hinge='left')   # P2_NW2
    draw_door_h(6.3, 7.1, 0.9, into='north', hinge='left')   # P2_NW3

    draw_door_h(12.9, 13.7, 0.9, into='north', hinge='right') # P2_NE1
    draw_door_h(15.4, 16.2, 0.9, into='north', hinge='right') # P2_NE2
    draw_door_h(17.9, 18.7, 0.9, into='north', hinge='right') # P2_NE3

    # South Corridor Doors (into South rooms)
    draw_door_h(5.9, 6.8, -0.9, into='south', hinge='right') # P2_SW
    draw_door_h(9.5, 10.4, -0.9, into='south', hinge='left') # P2_SC
    draw_door_h(13.2, 14.1, -0.9, into='south', hinge='left')# P2_SE

    # ---------------------------------------------------------
    # 9. ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 8.5)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # ---------------------------------------------------------
    # 10. AXIS LIMITS & EXPORT
    # ---------------------------------------------------------
    ax.set_xlim(-2.5, 22.5)
    ax.set_ylim(-8.5, 8.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {out_img_path}")

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau4\Tang2"
    create_floorplan_tang2(target_dir)
