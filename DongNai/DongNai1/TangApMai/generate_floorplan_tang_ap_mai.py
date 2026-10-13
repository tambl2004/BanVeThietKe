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

def create_floorplan_tang_ap_mai():
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(26, 12), dpi=300)
    ax = fig.add_axes([0.02, 0.06, 0.96, 0.86])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_STAIR_FILL = '#ffffff'    # Pure white for staircase on Floor 2+
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # Building Dimensions (Scaled I-Shape)
    X_MAX = 50.0
    X_WING_L = 8.0
    X_LOBBY_L = 22.0
    X_LOBBY_R = 28.0
    X_WING_R = 42.0

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG ÁP MÁI  —  Tòa án nhân dân khu vực 1 - Đồng Nai', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    header_line = plt.Line2D([0.03, 0.97], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    lg_x, lg_y = 0.0, -8.6
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.0, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.3, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.add_patch(patches.Rectangle((lg_x + 8.0, lg_y + 0.1), 1.0, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 9.3, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 16.0, lg_x + 17.2], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 16.0, lg_x + 17.2], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 17.5, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    ax.plot([lg_x + 24.0, lg_x + 24.0], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 24.0, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 25.0, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (I-SHAPE)
    # ---------------------------------------------------------
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.add_patch(patches.Rectangle((X_LOBBY_L, 0.9), 6.0, 3.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG ÁP MÁI — ĐỒNG NAI 1)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === NORTH ROW (Y > 0.9) ===
        # West North: Kho lưu trữ (X: 0.0 to 22.0)
        {
            'id': 'PAM_KLT', 'name': 'Kho lưu trữ',
            'x': 0.0, 'y': 0.9, 'w': 22.0, 'h': 3.5,
            'text_center': (11.0, 2.65),
            'door': (11.0, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.0
        },
        # East North: Kho lưu trữ 2 (X: 28.0 to 50.0)
        {
            'id': 'PAM_KLT2', 'name': 'Kho lưu trữ 2',
            'x': 28.0, 'y': 0.9, 'w': 22.0, 'h': 3.5,
            'text_center': (39.0, 2.65),
            'door': (39.0, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.0
        },

        # === SOUTH ROW (Y < -0.9) ===
        # West South: Kho lưu trữ 1 (X: 0.0 to 22.0)
        {
            'id': 'PAM_KLT1', 'name': 'Kho lưu trữ 1',
            'x': 0.0, 'y': -4.4, 'w': 22.0, 'h': 3.5,
            'text_center': (11.0, -2.65),
            'door': (11.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
        # Central South: Sảnh đệm kỹ thuật (X: 22.0 to 28.0)
        {
            'id': 'PAM_SDKT', 'name': 'Sảnh đệm kỹ thuật',
            'x': 22.0, 'y': -4.4, 'w': 6.0, 'h': 3.5,
            'text_center': (25.0, -2.65),
            'door': (24.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
        # East South: Kho thiết bị (X: 28.0 to 50.0)
        {
            'id': 'PAM_KTB', 'name': 'Kho thiết bị',
            'x': 28.0, 'y': -4.4, 'w': 22.0, 'h': 3.5,
            'text_center': (39.0, -2.65),
            'door': (39.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
    ]

    # Draw Room Background Fills
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)
    # Extra wing areas for I-shape footprint
    ax.add_patch(patches.Rectangle((0.0, 4.4), 8.0, 1.8, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))
    ax.add_patch(patches.Rectangle((0.0, -6.2), 8.0, 1.8, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))
    ax.add_patch(patches.Rectangle((42.0, 4.4), 8.0, 1.8, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))
    ax.add_patch(patches.Rectangle((42.0, -6.2), 8.0, 1.8, facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))

    # ---------------------------------------------------------
    # 5. STAIRCASES (FLOOR ÁP MÁI: PURE WHITE BACKGROUND)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 23.5, 1.2, 3.0, 2.8
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.0, ha='center', va='top', zorder=5)

    # Labels
    ax.text(11.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(35.0, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior West & East Wing Outer Walls
    draw_wall(-W, -6.2 - W, W, 12.4 + 2*W)
    draw_wall(X_MAX, -6.2 - W, W, 12.4 + 2*W)

    # North Exterior Walls
    draw_wall(-W, 6.2, X_WING_L + W, W)                         # West Wing top wall
    draw_wall(X_WING_L - P/2, 4.4, P, 1.8 + W)                  # West Wing inner vertical wall
    draw_wall(X_WING_L, 4.4, (X_WING_R - X_WING_L) + P/2, W)   # Continuous Mid North wall
    draw_wall(X_WING_R - P/2, 4.4, P, 1.8 + W)                  # East Wing inner vertical wall
    draw_wall(X_WING_R, 6.2, (X_MAX - X_WING_R) + W, W)        # East Wing top wall

    # South Exterior Walls
    draw_wall(-W, -6.2 - W, X_WING_L + W, W)                    # West Wing bottom wall
    draw_wall(X_WING_L - P/2, -6.2 - W, P, 1.8 + W)             # West Wing inner vertical wall
    draw_wall(X_WING_L, -4.4 - W, (X_WING_R - X_WING_L) + P/2, W) # Continuous Mid South wall
    draw_wall(X_WING_R - P/2, -6.2 - W, P, 1.8 + W)             # East Wing inner vertical wall
    draw_wall(X_WING_R, -6.2 - W, (X_MAX - X_WING_R) + W, W)   # East Wing bottom wall

    # Corridor Horizontal Partition Walls (Y = 0.9 & Y = -0.9) with door cutouts
    # North Line (Y = 0.9): Doors at 11.0 (Kho lưu trữ) | 39.0 (Kho lưu trữ 2)
    draw_wall(0.0, 0.9 - P/2, 11.0, P)
    draw_wall(11.9, 0.9 - P/2, 10.1, P)

    draw_wall(28.0, 0.9 - P/2, 11.0, P)
    draw_wall(39.9, 0.9 - P/2, 10.1, P)

    # South Line (Y = -0.9): Doors at 11.0 (Kho lưu trữ 1) | 24.0 (Sảnh đệm) | 39.0 (Kho thiết bị)
    draw_wall(0.0, -0.9 - P/2, 11.0, P)
    draw_wall(11.9, -0.9 - P/2, 10.1, P)

    draw_wall(22.0, -0.9 - P/2, 2.0, P)
    draw_wall(24.85, -0.9 - P/2, 3.15, P)

    draw_wall(28.0, -0.9 - P/2, 11.0, P)
    draw_wall(39.9, -0.9 - P/2, 10.1, P)

    # Internal Vertical Partitions
    # North:
    draw_wall(22.0 - P/2, 0.9, P, 3.5)  # Wall between Kho lưu trữ and Stair hall
    draw_wall(28.0 - P/2, 0.9, P, 3.5)  # Wall between Stair hall and Kho lưu trữ 2

    # South:
    draw_wall(22.0 - P/2, -4.4, P, 3.5) # Wall between Kho lưu trữ 1 and Sảnh đệm
    draw_wall(28.0 - P/2, -4.4, P, 3.5) # Wall between Sảnh đệm and Kho thiết bị

    # ---------------------------------------------------------
    # 7. DRAW WINDOWS
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
    draw_window(2.5, 6.2, 3.5, W, is_horizontal=True)        # Kho lưu trữ
    draw_window(12.0, 4.4, 2.5, W, is_horizontal=True)       # Kho lưu trữ
    draw_window(24.5, 4.4, 2.0, W, is_horizontal=True)       # Stair hall
    draw_window(34.0, 4.4, 2.5, W, is_horizontal=True)       # Kho lưu trữ 2
    draw_window(44.0, 6.2, 3.5, W, is_horizontal=True)       # Kho lưu trữ 2

    # South Windows
    draw_window(2.5, -6.2 - W, 3.5, W, is_horizontal=True)   # Kho lưu trữ 1
    draw_window(12.0, -4.4 - W, 2.5, W, is_horizontal=True)  # Kho lưu trữ 1
    draw_window(24.5, -4.4 - W, 2.0, W, is_horizontal=True)  # Sảnh đệm
    draw_window(34.0, -4.4 - W, 2.5, W, is_horizontal=True)  # Kho thiết bị
    draw_window(44.0, -6.2 - W, 3.5, W, is_horizontal=True)  # Kho thiết bị

    # Corridor End Windows
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)

    # Outer West & East Windows
    draw_window(-W, 3.5, W, 2.0, is_horizontal=False)
    draw_window(-W, -4.5, W, 2.0, is_horizontal=False)
    draw_window(X_MAX, 3.5, W, 2.0, is_horizontal=False)
    draw_window(X_MAX, -4.5, W, 2.0, is_horizontal=False)

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

    for r in rooms:
        dx, dy, dsize, dmode = r['door']
        draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 8.5)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                fontweight='bold', ha='center', va='center', zorder=15)

    ax.set_xlim(-3.0, 53.0)
    ax.set_ylim(-9.0, 8.5)

    out_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\DongNai\DongNai1\TangApMai"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mat_bang_tang_ap_mai.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng Áp Mái đã xuất thành công tại: {out_path}")

if __name__ == "__main__":
    create_floorplan_tang_ap_mai()
