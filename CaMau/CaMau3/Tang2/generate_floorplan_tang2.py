import os
from typing import TypedDict, Tuple, List, Optional
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
    fig = plt.figure(figsize=(24, 22), dpi=300)
    ax = fig.add_axes([0.03, 0.04, 0.94, 0.90])
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

    WALL_THICKNESS = 0.22           # 220mm exterior wall
    PART_THICKNESS = 0.12           # 120mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.04, 0.965, 'MẶT BẰNG TẦNG 2  —  TÒA ÁN NHÂN DÂN KHU VỰC 3 CÀ MAU', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.04, 0.96], [0.948, 0.948], transform=fig.transFigure, color='#e2e8f0', linewidth=1.2)
    fig.lines.append(header_line)

    # Legend Box at Bottom Center
    lg_x, lg_y = 5.0, -8.6
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.38, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.06, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 7.5, lg_y + 0.11), 1.2, 0.16, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 9.0, lg_y + 0.06, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 14.5, lg_x + 15.7], [lg_y + 0.24, lg_y + 0.24], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 14.5, lg_x + 15.7], [lg_y + 0.09, lg_y + 0.09], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 16.0, lg_y + 0.06, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 21.0, lg_x + 21.0], [lg_y + 0.02, lg_y + 0.34], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=1)
    arc_lg = patches.Arc((lg_x + 21.0, lg_y + 0.02), 0.64, 0.64, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 22.3, lg_y + 0.06, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 5: Roof (Mái che)
    ax.add_patch(patches.Rectangle((lg_x + 28.5, lg_y + 0.06), 1.2, 0.28, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.0, zorder=1))
    ax.text(lg_x + 30.0, lg_y + 0.06, 'Mái che', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (PASTEL BLUE-GREY)
    # ---------------------------------------------------------
    # Main horizontal corridor of Tòa 1 (X: 0.0 to 36.0, Y: -1.0 to 1.0)
    ax.add_patch(patches.Rectangle((0.0, -1.0), 36.0, 2.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Central Staircase Lobby (X: 15.0 to 21.0, Y: 1.0 to 4.5)
    ax.add_patch(patches.Rectangle((15.0, 1.0), 6.0, 3.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # South transition lobbies flanking Chief Judge room
    ax.add_patch(patches.Rectangle((9.0, -4.5), 5.0, 3.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.add_patch(patches.Rectangle((22.0, -4.5), 6.5, 3.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOF AREA (MÁI CHE TÒA 2 - KHỐI 1 TẦNG PHÍA SAU)
    # ---------------------------------------------------------
    # Poly shape of Tòa 2 roof footprint (X: 3.0 to 34.0, Y: 4.5 to 30.0)
    # Neck: X: 15.0 to 21.0, Y: 4.5 to 6.5
    # Main rear body: X: 3.0 to 34.0, Y: 6.5 to 30.0
    roof_poly_coords = [
        (15.0, 4.5),
        (15.0, 6.5),
        (3.0, 6.5),
        (3.0, 30.0),
        (34.0, 30.0),
        (34.0, 6.5),
        (21.0, 6.5),
        (21.0, 4.5),
    ]
    roof_patch = patches.Polygon(roof_poly_coords, closed=True, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.5, zorder=2)
    ax.add_patch(roof_patch)

    # Big MÁI CHE text label in center of roof
    ax.text(18.5, 18.0, 'MÁI CHE', color=COLOR_TEXT_MUTED, fontsize=16.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 5. ROOM DEFINITIONS (TÒA 1: 6 PHÒNG TẦNG 2 CHUẨN PROMPT)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- Dãy phía Bắc Tòa 1 (Y: 1.0 to 4.5m) ---
        {
            'id': 'T1_201', 'name': 'Phòng Chánh toà toà dân sự', 'sub': '(KT: 5x3.5 | 3 ng)',
            'x': 0.0, 'y': 1.0, 'w': 7.5, 'h': 3.5,
            'text_center': (3.75, 2.75),
            'font_size': 8.5
        },
        {
            'id': 'T1_202', 'name': 'Phòng Chánh toà toà hình sự', 'sub': '(KT: 5x3.5 | 2 ng)',
            'x': 7.5, 'y': 1.0, 'w': 7.5, 'h': 3.5,
            'text_center': (11.25, 2.75),
            'font_size': 8.5
        },
        {
            'id': 'T1_203', 'name': 'Phòng Thẩm phán', 'sub': '(KT: 5x3 | 2 ng)',
            'x': 21.0, 'y': 1.0, 'w': 7.5, 'h': 3.5,
            'text_center': (24.75, 2.75),
            'font_size': 8.5
        },
        {
            'id': 'T1_204', 'name': 'Phòng phó chánh toà dân sự', 'sub': '(KT: 5x3 | 2 ng)',
            'x': 28.5, 'y': 1.0, 'w': 7.5, 'h': 3.5,
            'text_center': (32.25, 2.75),
            'font_size': 8.5
        },

        # --- Dãy phía Nam Tòa 1 (Y: -4.5 to -1.0m) ---
        {
            'id': 'T1_205', 'name': 'Phòng thẩm phán', 'sub': '(KT: 5x3.5)',
            'x': 0.0, 'y': -4.5, 'w': 9.0, 'h': 3.5,
            'text_center': (4.5, -2.75),
            'font_size': 9.0
        },
        {
            'id': 'T1_206', 'name': 'Phòng Chánh án', 'sub': '(KT: 5x4.5 | 1 ng)',
            'x': 14.0, 'y': -4.5, 'w': 8.0, 'h': 3.5,
            'text_center': (18.0, -2.75),
            'font_size': 9.5
        },
        {
            'id': 'T1_207', 'name': 'Khu vệ sinh', 'sub': '(WC Nam - Nữ)',
            'x': 28.5, 'y': -4.5, 'w': 7.5, 'h': 3.5,
            'text_center': (32.25, -2.75),
            'font_size': 8.0
        },
    ]

    # Draw pure white room interior fills
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 6. STAIRCASE (TẦNG 2: NỀN TRẮNG, HƯỚNG ĐI XUỐNG TẦNG 1)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 16.5, 1.2, 3.0, 3.1
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 10
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)
    # Down arrow on staircase
    ax.annotate('', xy=(mid_x - 0.7, stair_y + 0.5), xytext=(mid_x - 0.7, stair_y + 2.5),
                arrowprops=dict(arrowstyle="->", color=COLOR_WALL, lw=1.2), zorder=6)
    ax.text(mid_x - 0.7, stair_y + 2.7, 'XUỐNG', color=COLOR_TEXT_MUTED, fontsize=7.5, ha='center', va='bottom', zorder=6)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.25, 'Cầu thang bộ (Xuống tầng 1)', 
            color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', ha='center', va='top', zorder=5)

    # Corridor labels
    ax.text(6.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(30.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(18.0, 0.0, 'SẢNH TẦNG 2', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(11.5, -2.75, 'SẢNH ĐỆM', color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, -2.75, 'SẢNH ĐỆM', color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 7. DRAW SOLID STRUCTURAL WALLS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # === TÒA 1 EXTERIOR WALLS (ENCLOSED HEADS ON LEVEL 2) ===
    # West outer wall (X = -W, Y: -4.5 to 4.5 enclosed)
    draw_wall(-W, -4.5 - W, W, 9.0 + 2*W)
    # East outer wall (X = 36.0, Y: -4.5 to 4.5 enclosed)
    draw_wall(36.0, -4.5 - W, W, 9.0 + 2*W)

    # North exterior wall of Tòa 1 (Solid along entire 36m, separating from roof)
    draw_wall(-W, 4.5, 36.0 + 2*W, W)

    # South exterior wall of Tòa 1
    draw_wall(-W, -4.5 - W, 36.0 + 2*W, W)

    # === TÒA 1 CORRIDOR WALLS (Y = 1.0 & Y = -1.0) ===
    # North Corridor Wall Y = 1.0 with door cutouts:
    # Gap 1: 5.6 to 6.5 (Room 201)
    # Gap 2: 8.5 to 9.4 (Room 202)
    # Open: 15.0 to 21.0 (Stair hall)
    # Gap 3: 22.0 to 22.9 (Room 203)
    # Gap 4: 29.5 to 30.4 (Room 204)
    draw_wall(0, 1.0 - P/2, 5.6, P)
    draw_wall(6.5, 1.0 - P/2, 2.0, P)
    draw_wall(9.4, 1.0 - P/2, 5.6, P)

    draw_wall(21.0, 1.0 - P/2, 1.0, P)
    draw_wall(22.9, 1.0 - P/2, 6.6, P)
    draw_wall(30.4, 1.0 - P/2, 5.6, P)

    # South Corridor Wall Y = -1.0 with door cutouts:
    # Gap 1: 7.2 to 8.1 (Room 205)
    # Open: 9.0 to 14.0 (South West lobby)
    # Gap 2: 17.1 to 18.9 (Room 206 - Phòng Chánh án double doors)
    # Open: 22.0 to 28.5 (South East lobby)
    # Gap 3: 29.5 to 30.4 (Room 207 - WC)
    draw_wall(0, -1.0 - P/2, 7.2, P)
    draw_wall(8.1, -1.0 - P/2, 0.9, P)

    draw_wall(14.0, -1.0 - P/2, 3.1, P)
    draw_wall(18.9, -1.0 - P/2, 3.1, P)

    draw_wall(28.5, -1.0 - P/2, 1.0, P)
    draw_wall(30.4, -1.0 - P/2, 5.6, P)

    # === VERTICAL INTERNAL PARTITIONS ===
    # North row vertical partitions
    draw_wall(7.5 - P/2, 1.0, P, 3.5)
    draw_wall(15.0 - P/2, 1.0, P, 3.5)
    draw_wall(21.0 - P/2, 1.0, P, 3.5)
    draw_wall(28.5 - P/2, 1.0, P, 3.5)

    # South row vertical partitions
    draw_wall(9.0 - P/2, -4.5, P, 3.5)
    draw_wall(14.0 - P/2, -4.5, P, 3.5)
    draw_wall(22.0 - P/2, -4.5, P, 3.5)
    draw_wall(28.5 - P/2, -4.5, P, 3.5)

    # ---------------------------------------------------------
    # 8. DRAW WINDOWS
    # ---------------------------------------------------------
    def draw_window(x, y, w, h, is_horizontal=True):
        if is_horizontal:
            ax.add_patch(patches.Rectangle((x, y - 0.02), w, h + 0.04, facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x, x + w], [y + 0.04, y + 0.04], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x, x + w], [y + h - 0.04, y + h - 0.04], color=COLOR_WALL, linewidth=1.2, zorder=12)
        else:
            ax.add_patch(patches.Rectangle((x - 0.02, y), w + 0.04, h, facecolor='#ffffff', edgecolor='none', zorder=11))
            ax.plot([x + 0.04, x + 0.04], [y, y + h], color=COLOR_WALL, linewidth=1.2, zorder=12)
            ax.plot([x + w - 0.04, x + w - 0.04], [y, y + h], color=COLOR_WALL, linewidth=1.2, zorder=12)

    # South Exterior Windows (Y = -4.5 - W)
    draw_window(2.5, -4.5 - W, 3.5, W, is_horizontal=True)    # Room 205
    draw_window(10.2, -4.5 - W, 2.0, W, is_horizontal=True)   # South West lobby
    draw_window(15.5, -4.5 - W, 5.0, W, is_horizontal=True)   # Room 206 (Chánh án)
    draw_window(24.5, -4.5 - W, 2.5, W, is_horizontal=True)   # South East lobby
    draw_window(30.5, -4.5 - W, 2.5, W, is_horizontal=True)   # Room 207 (WC)

    # North Exterior Windows looking out to Mái che (Y = 4.5)
    draw_window(2.5, 4.5, 3.5, W, is_horizontal=True)         # Room 201
    draw_window(9.5, 4.5, 3.5, W, is_horizontal=True)         # Room 202
    draw_window(16.5, 4.5, 3.0, W, is_horizontal=True)        # Stair hall overlooking roof
    draw_window(23.5, 4.5, 3.5, W, is_horizontal=True)        # Room 203
    draw_window(30.5, 4.5, 3.5, W, is_horizontal=True)        # Room 204

    # Enclosed West & East Ends Corridor Windows (Level 2 Feature)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)        # West corridor end window
    draw_window(-W, 2.0, W, 1.8, is_horizontal=False)         # West Room 201 window
    draw_window(-W, -3.5, W, 1.8, is_horizontal=False)        # West Room 205 window

    draw_window(36.0, -0.6, W, 1.2, is_horizontal=False)      # East corridor end window
    draw_window(36.0, 2.0, W, 1.8, is_horizontal=False)       # East Room 204 window
    draw_window(36.0, -3.5, W, 1.8, is_horizontal=False)      # East Room 207 window

    # ---------------------------------------------------------
    # 9. DRAW DOORS & SWINGS (PRECISE WALL GAPS)
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

    # North Corridor Wall Y = 1.0 (Into North rooms)
    draw_door_h(5.6, 6.5, 1.0, into='north', hinge='left')    # Room 201
    draw_door_h(8.5, 9.4, 1.0, into='north', hinge='right')   # Room 202
    draw_door_h(22.0, 22.9, 1.0, into='north', hinge='left')  # Room 203
    draw_door_h(29.5, 30.4, 1.0, into='north', hinge='left')  # Room 204

    # South Corridor Wall Y = -1.0 (Into South rooms)
    draw_door_h(7.2, 8.1, -1.0, into='south', hinge='right')  # Room 205
    # Room 206: Double doors for Chief Judge
    draw_door_h(17.1, 18.0, -1.0, into='south', hinge='left')
    draw_door_h(18.0, 18.9, -1.0, into='south', hinge='right')
    draw_door_h(29.5, 30.4, -1.0, into='south', hinge='left') # Room 207 (WC)

    # ---------------------------------------------------------
    # 10. ROOM LABELS & METADATA
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 8.5)
        # Main room name (bold)
        ax.text(cx, cy + 0.22, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)
        # Secondary info
        if r['sub']:
            ax.text(cx, cy - 0.28, r['sub'], color=COLOR_TEXT_MUTED, fontsize=font_sz * 0.85, ha='center', va='center', zorder=15)

    # ---------------------------------------------------------
    # 11. AXIS LIMITS & EXPORT
    # ---------------------------------------------------------
    ax.set_xlim(-3.0, 39.0)
    ax.set_ylim(-9.5, 32.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {out_img_path}")

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau3\Tang2"
    create_floorplan_tang2(target_dir)
