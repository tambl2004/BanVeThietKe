import os
from typing import TypedDict, Tuple, List
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class RoomDict(TypedDict):
    id: str
    name: str
    sub: str
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
    COLOR_STAIR_FILL = '#ffffff'    # Pure white stair fill for Floor 2 per Spec

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.955, 'MẶT BẰNG TẦNG 2  —  TÒA ÁN NHÂN DÂN KHU VỰC 5 - CÀ MAU', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.938, 0.938], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = -0.5, -15.2
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 6.5, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 7.6, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 13.0, lg_x + 13.8], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 13.0, lg_x + 13.8], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 14.1, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 18.5, lg_x + 18.5], [lg_y + 0.02, lg_y + 0.28], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 18.5, lg_y + 0.02), 0.52, 0.52, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 19.6, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 5: Roof (Mái che)
    ax.add_patch(patches.Rectangle((lg_x + 25.0, lg_y + 0.05), 0.8, 0.25, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.0, zorder=1))
    ax.text(lg_x + 26.1, lg_y + 0.05, 'Mái che', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (TÒA 1)
    # ---------------------------------------------------------
    # Tòa 1 Horizontal Corridor (X: 0.0 to 20.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Center South Lobby (X: 7.5 to 12.5, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((7.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Tòa 1 Rear Stair Hall (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOF AREA (MÁI CHE TÒA 2)
    # ---------------------------------------------------------
    # Tòa 2 footprint on Floor 1: X: 20.8 to 28.8, Y: -12.5 to 5.4
    roof_w = 8.0
    roof_h = 17.9
    roof_rect = patches.Rectangle((20.8, -12.5), roof_w, roof_h, 
                                  facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.5, zorder=2)
    ax.add_patch(roof_rect)

    # Prominent MÁI CHE text label in center of Tòa 2
    ax.text(20.8 + roof_w / 2.0, -12.5 + roof_h / 2.0, 'MÁI CHE', 
            color=COLOR_TEXT_MUTED, fontsize=16.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 5. ROOM DEFINITIONS (TÒA 1: 4 PHÒNG CHUẨN PROMPT)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- North Wing Tòa 1 (Y: 0.9 to 5.4m, H = 4.5m) ---
        {
            'id': 'T1_P10', 'name': 'Phòng số 10', 'sub': '(KT: 6x3 | 2 ng)',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'font_size': 10.5
        },
        {
            'id': 'T1_P7', 'name': 'Phòng số 7', 'sub': '(KT: 5x3 | 1 ng)',
            'x': 12.5, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (16.25, 3.15),
            'font_size': 10.5
        },

        # --- South Wing Tòa 1 (Y: -4.9 to -0.9m, H = 4.0m) ---
        {
            'id': 'T1_P8', 'name': 'Phòng số 8', 'sub': '(KT: 3x3 | 1 ng)',
            'x': 0.0, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (3.75, -2.9),
            'font_size': 10.5
        },
        {
            'id': 'T1_P9', 'name': 'Phòng số 9', 'sub': '(KT: 3x3 | 1 ng)',
            'x': 12.5, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (16.25, -2.9),
            'font_size': 10.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 6. STAIRCASE (TẦNG 2: NỀN TRẮNG, HƯỚNG ĐI XUỐNG TẦNG 1)
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

    # Labels for Corridor and Center Lobby
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(10.0, 0.0, 'SẢNH TẦNG 2', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(10.0, -2.9, 'SẢNH TẦNG 2', color=COLOR_TEXT_MAIN, fontsize=11.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 7. DRAW STRUCTURAL WALLS (TÒA 1 ENCLOSED ON FLOOR 2)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior Perimeter Walls of Tòa 1
    # North Wall (Continuous from -W to 20.0+W at Y = 5.4)
    draw_wall(-W, 5.4, 20.0 + 2*W, W)

    # South Wall (Continuous from -W to 20.0+W at Y = -4.9-W)
    draw_wall(-W, -4.9 - W, 20.0 + 2*W, W)

    # West Exterior Wall (Enclosed from -4.9-W to 5.4+W)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)

    # East Exterior Wall (Enclosed from -4.9-W to 5.4+W, facing expansion joint)
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2*W)

    # Internal Vertical Partitions
    # North Wing
    draw_wall(7.5 - P/2, 0.9, P, 4.5)   # Room 10 & Stair hall
    draw_wall(12.5 - P/2, 0.9, P, 4.5)  # Stair hall & Room 7

    # South Wing
    draw_wall(7.5 - P/2, -4.9, P, 4.0)  # Room 8 & Center Lobby
    draw_wall(12.5 - P/2, -4.9, P, 4.0) # Center Lobby & Room 9

    # North Corridor Wall Line (Y = 0.9) with Door Openings
    # Room 10: door 6.0 to 6.9
    draw_wall(0.0, 0.9 - P/2, 6.0, P)
    draw_wall(6.9, 0.9 - P/2, 0.6, P)
    # Stair Hall (X: 7.5 to 12.5) is open
    # Room 7: door 13.1 to 14.0
    draw_wall(12.5, 0.9 - P/2, 0.6, P)
    draw_wall(14.0, 0.9 - P/2, 6.0, P)

    # South Corridor Wall Line (Y = -0.9) with Door Openings
    # Room 8: door 6.0 to 6.9
    draw_wall(0.0, -0.9 - P/2, 6.0, P)
    draw_wall(6.9, -0.9 - P/2, 0.6, P)
    # Center South Lobby (X: 7.5 to 12.5) is completely open to corridor
    # Room 9: door 13.1 to 14.0
    draw_wall(12.5, -0.9 - P/2, 0.6, P)
    draw_wall(14.0, -0.9 - P/2, 6.0, P)

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

    # North Windows
    draw_window(1.5, 5.4, 2.0, W, is_horizontal=True)    # Room 10 w1
    draw_window(4.5, 5.4, 2.0, W, is_horizontal=True)    # Room 10 w2
    draw_window(9.0, 5.4, 2.0, W, is_horizontal=True)    # Stair Hall North Window
    draw_window(14.0, 5.4, 2.0, W, is_horizontal=True)   # Room 7 w1
    draw_window(17.0, 5.4, 2.0, W, is_horizontal=True)   # Room 7 w2

    # South Windows
    draw_window(1.5, -4.9 - W, 2.0, W, is_horizontal=True)  # Room 8 w1
    draw_window(4.5, -4.9 - W, 2.0, W, is_horizontal=True)  # Room 8 w2
    draw_window(8.75, -4.9 - W, 2.5, W, is_horizontal=True) # Center South Window
    draw_window(14.0, -4.9 - W, 2.0, W, is_horizontal=True) # Room 9 w1
    draw_window(17.0, -4.9 - W, 2.0, W, is_horizontal=True) # Room 9 w2

    # West Gable Windows (Enclosed Corridor End Window included)
    draw_window(-W, 2.0, W, 2.0, is_horizontal=False)   # Room 10 West
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)  # West Corridor End Window
    draw_window(-W, -3.8, W, 2.0, is_horizontal=False)  # Room 8 West

    # East Gable Windows (Enclosed Corridor End Window included)
    draw_window(20.0, 2.0, W, 2.0, is_horizontal=False)   # Room 7 East
    draw_window(20.0, -0.6, W, 1.2, is_horizontal=False)  # East Corridor End Window
    draw_window(20.0, -3.8, W, 2.0, is_horizontal=False)  # Room 9 East

    # ---------------------------------------------------------
    # 9. DRAW DOORS & SWINGS
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

    # Doors for rooms
    draw_door_h(6.0, 6.9, 0.9, into='north', hinge='left')    # Room 10
    draw_door_h(13.1, 14.0, 0.9, into='north', hinge='right') # Room 7
    draw_door_h(6.0, 6.9, -0.9, into='south', hinge='left')   # Room 8
    draw_door_h(13.1, 14.0, -0.9, into='south', hinge='right')# Room 9

    # ---------------------------------------------------------
    # 10. ROOM LABELS & METADATA
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 10.0)
        ax.text(cx, cy + 0.22, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)
        if r['sub']:
            ax.text(cx, cy - 0.28, r['sub'], color=COLOR_TEXT_MUTED, fontsize=font_sz * 0.85, ha='center', va='center', zorder=15)

    # ---------------------------------------------------------
    # 11. AXIS LIMITS & EXPORT
    # ---------------------------------------------------------
    ax.set_xlim(-2.5, 31.5)
    ax.set_ylim(-16.0, 8.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {out_img_path}")

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau5\Tang2"
    create_floorplan_tang2(target_dir)
