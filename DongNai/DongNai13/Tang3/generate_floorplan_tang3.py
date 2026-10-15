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

COURT_NAME = "Tòa án nhân dân khu vực 13 - Đồng Nai"

def create_floorplan_tang3(court_name: str = COURT_NAME):
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
    COLOR_ROOF_FILL = '#ffffff'     # Pure white for roof area
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#ffffff'    # Floor 3 stair background is pure white

    WALL_THICKNESS = 0.22  # 220mm exterior structural wall (dày)
    PART_THICKNESS = 0.08  # 80mm interior partition & corridor wall (mỏng, thanh thoát)
    W = WALL_THICKNESS
    P = PART_THICKNESS
    X_MAX = 32.0            # Tòa 1 Main Building Length = 32.0m
    Y_TOA2_TOP = 14.5       # Tòa 2 Top Y = 14.5m

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, f'MẶT BẰNG TẦNG 3  —  {court_name}', 
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
    ax.plot([lg_x + 15.0, lg_x + 15.8], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.4, zorder=1)
    ax.plot([lg_x + 15.0, lg_x + 15.8], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.4, zorder=1)
    ax.text(lg_x + 16.1, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 21.0, lg_x + 21.0], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 21.0, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 22.0, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (TẦNG 3)
    # ---------------------------------------------------------
    # Main Building Horizontal Corridor (X: 0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Stair Hall at Center North (X: 13.5 to 18.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TÒA ÁN KHU VỰC 13 - ĐỒNG NAI: TẦNG 3)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === TÒA 1: DÃY PHÍA BẮC (North Wing: Y > 0.9m) ===
        # Cánh Tây Bắc (X: 0.0 to 13.5m)
        {
            'id': 'T3_PPCA1', 'name': 'Phòng Phó chánh án',
            'x': 0.0, 'y': 0.9, 'w': 13.5, 'h': 4.5,
            'text_center': (6.75, 3.15),
            'door': (12.0, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.5
        },

        # Cánh Đông Bắc (X: 18.5 to 32.0m) - Phòng Hoà giải, đối thoại lớn
        {
            'id': 'T3_PHG', 'name': 'Phòng Hoà giải, đối thoại',
            'x': 18.5, 'y': 0.9, 'w': 13.5, 'h': 4.5,
            'text_center': (25.25, 3.15),
            'door': (19.5, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.5
        },

        # === TÒA 1: DÃY PHÍA NAM (South Wing: Y < -0.9m) ===
        # Cánh Tây Nam (X: 0.0 to 13.5m)
        {
            'id': 'T3_PTP1', 'name': 'Phòng Thẩm phán',
            'x': 0.0, 'y': -4.9, 'w': 13.5, 'h': 4.0,
            'text_center': (6.75, -2.9),
            'door': (12.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },

        # Dãy Nam Trung tâm (X: 13.5 to 18.5m)
        {
            'id': 'T3_PPCA2', 'name': 'Phòng Phó chánh án',
            'x': 13.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (16.0, -2.9),
            'door': (14.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },

        # Cánh Đông Nam (X: 18.5 to 32.0m)
        {
            'id': 'T3_PTP2', 'name': 'Phòng Thẩm phán',
            'x': 18.5, 'y': -4.9, 'w': 13.5, 'h': 4.0,
            'text_center': (25.25, -2.9),
            'door': (19.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. TÒA 2: MÁI CHE (ROOF AREA - TẦNG 3)
    # ---------------------------------------------------------
    # Tòa 2 roof background (Pure white, enclosed border)
    roof_rect = patches.Rectangle((3.5, 6.2), 25.0, Y_TOA2_TOP - 6.2, facecolor=COLOR_ROOF_FILL, edgecolor='none', zorder=2)
    ax.add_patch(roof_rect)

    # Roof label (centered, bold, muted grey)
    ax.text(16.0, (6.2 + Y_TOA2_TOP) / 2.0, 'MÁI CHE', color=COLOR_TEXT_MUTED, fontsize=14.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. STAIRCASE GRAPHIC (FLOOR 3 - NỀN TRẮNG THUẦN)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 14.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    ax.plot([mid_x, mid_x], [stair_y, stair_y + stair_h * (num_treads - 1) / num_treads], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Stair label
    ax.text(mid_x, stair_y + stair_h / 2.0, 'CẦU THANG', color=COLOR_TEXT_MUTED, fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=5)

    # Labels for Corridor
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 7. DRAW WALLS (PRECISION ALIGNED WITH DOOR OPENINGS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # === TÒA 1: EXTERIOR ENVELOPE WALLS (WALL_THICKNESS = 0.22m) ===
    # Tòa 1 Outer West Wall (ENCLOSED AT CORRIDOR Y: -0.9 to 0.9)
    draw_wall(-W, -4.9 - W, W, (5.4 + 4.9) + 2*W)

    # Tòa 1 Outer East Wall (ENCLOSED AT CORRIDOR Y: -0.9 to 0.9)
    draw_wall(X_MAX, -4.9 - W, W, (5.4 + 4.9) + 2*W)

    # Tòa 1 North Top Wall (Y = 5.4m, ENCLOSED FULL LENGTH from X: -W to X_MAX + W)
    draw_wall(-W, 5.4, X_MAX + 2*W, W)

    # Tòa 1 South Bottom Wall (Y = -4.9m, ENCLOSED FULL LENGTH from X: -W to X_MAX + W)
    draw_wall(-W, -4.9 - W, X_MAX + 2*W, W)

    # === TÒA 2: MÁI CHE PERIMETER WALLS (WALL_THICKNESS = 0.22m) ===
    draw_wall(3.5 - W, 6.2 - W, W, (Y_TOA2_TOP - 6.2) + 2*W)       # West outer wall
    draw_wall(28.5, 6.2 - W, W, (Y_TOA2_TOP - 6.2) + 2*W)          # East outer wall
    draw_wall(3.5 - W, Y_TOA2_TOP, 25.0 + 2*W, W)                 # North outer wall
    draw_wall(3.5 - W, 6.2 - W, 25.0 + 2*W, W)                    # South perimeter wall

    # === TÒA 1: INTERIOR CORRIDOR & PARTITION WALLS (PART_THICKNESS = 0.08m) ===
    # 1. North Corridor Line Y = 0.9m
    # Cánh Tây Bắc (X: 0.0 to 13.5): Door at (12.0 to 12.85)
    draw_wall(0.0, 0.9 - P/2, 12.0, P)
    draw_wall(12.85, 0.9 - P/2, 13.5 - 12.85, P)

    # Cánh Đông Bắc (X: 18.5 to 32.0): Door at (19.5 to 20.35)
    draw_wall(18.5, 0.9 - P/2, 19.5 - 18.5, P)
    draw_wall(20.35, 0.9 - P/2, 32.0 - 20.35, P)

    # 2. South Corridor Line Y = -0.9m
    # Cánh Tây Nam & Center (X: 0.0 to 18.5): Doors at (12.0 to 12.85), (14.0 to 14.85)
    draw_wall(0.0, -0.9 - P/2, 12.0, P)
    draw_wall(12.85, -0.9 - P/2, 14.0 - 12.85, P)
    draw_wall(14.85, -0.9 - P/2, 18.5 - 14.85, P)

    # Cánh Đông Nam (X: 18.5 to 32.0): Door at (19.5 to 20.35)
    draw_wall(18.5, -0.9 - P/2, 19.5 - 18.5, P)
    draw_wall(20.35, -0.9 - P/2, 32.0 - 20.35, P)

    # 3. Tòa 1 Internal Vertical Partitions
    draw_wall(13.5 - P/2, 0.9, P, 4.5)        # Main lobby West wall (North)
    draw_wall(13.5 - P/2, -4.9, P, 4.0)       # Between Thẩm phán 1 & Phó chánh án 2
    draw_wall(18.5 - P/2, 0.9, P, 4.5)        # Main lobby East wall (North)
    draw_wall(18.5 - P/2, -4.9, P, 4.0)       # Between Phó chánh án 2 & Thẩm phán 2

    # ---------------------------------------------------------
    # 8. DRAW WINDOWS ON EXTERIOR WALLS
    # ---------------------------------------------------------
    def draw_window_horizontal(x0, x1, y):
        ax.plot([x0, x1], [y + 0.07, y + 0.07], color=COLOR_WALL, linewidth=1.3, zorder=12)
        ax.plot([x0, x1], [y - 0.07, y - 0.07], color=COLOR_WALL, linewidth=1.3, zorder=12)

    def draw_window_vertical(x, y0, y1):
        ax.plot([x + 0.07, x + 0.07], [y0, y1], color=COLOR_WALL, linewidth=1.3, zorder=12)
        ax.plot([x - 0.07, x - 0.07], [y0, y1], color=COLOR_WALL, linewidth=1.3, zorder=12)

    # Tòa 1 North Windows (Y = 5.4 + W/2)
    draw_window_horizontal(4.0, 8.0, 5.4 + W/2)       # Phó chánh án 1
    draw_window_horizontal(14.5, 17.5, 5.4 + W/2)     # Sảnh thang nhìn ra mái che
    draw_window_horizontal(23.0, 27.0, 5.4 + W/2)     # Phòng Hoà giải

    # Tòa 1 South Windows (Y = -4.9 - W/2)
    draw_window_horizontal(4.0, 8.0, -4.9 - W/2)      # Thẩm phán 1
    draw_window_horizontal(14.5, 17.5, -4.9 - W/2)    # Phó chánh án 2
    draw_window_horizontal(23.0, 27.0, -4.9 - W/2)    # Thẩm phán 2

    # Tòa 1 West End Windows (X = -W/2)
    draw_window_vertical(-W/2, -3.9, -1.9)
    draw_window_vertical(-W/2, -0.6, 0.6)             # Corridor West End Window
    draw_window_vertical(-W/2, 2.1, 4.1)

    # Tòa 1 East End Windows (X = X_MAX + W/2)
    draw_window_vertical(X_MAX + W/2, -3.9, -1.9)
    draw_window_vertical(X_MAX + W/2, -0.6, 0.6)      # Corridor East End Window
    draw_window_vertical(X_MAX + W/2, 2.1, 4.1)

    # ---------------------------------------------------------
    # 9. DOORS RENDERING (WITH SWING ARCS)
    # ---------------------------------------------------------
    def draw_door(dx, dy, dw, dtype):
        if dtype == 'N_IN_RIGHT':
            ax.plot([dx, dx], [dy, dy + dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((dx, dy), dw*2, dw*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)
        elif dtype == 'S_IN_RIGHT':
            ax.plot([dx, dx], [dy, dy - dw], color=COLOR_DOOR_SWING, linewidth=1.3, zorder=15)
            arc = patches.Arc((dx, dy), dw*2, dw*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=14)
            ax.add_patch(arc)

    for r in rooms:
        dx, dy, dw, dtype = r['door']
        draw_door(dx, dy, dw, dtype)

    # ---------------------------------------------------------
    # 10. ROOM LABELS & TEXT
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'], 
                fontweight='bold', ha='center', va='center', zorder=20)

    # ---------------------------------------------------------
    # 11. EXPORT & SAVE
    # ---------------------------------------------------------
    output_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\DongNai\DongNai13\Tang3"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "mat_bang_tang_3.png")

    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close(fig)
    print(f"Bản vẽ đã được xuất thành công tại: {output_path}")

if __name__ == '__main__':
    create_floorplan_tang3()
