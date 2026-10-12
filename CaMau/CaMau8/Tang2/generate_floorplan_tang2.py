import os
from typing import TypedDict, Tuple, List, Optional
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
    door: Optional[Tuple[float, float, float, str]]
    font_size: float

def create_floorplan_tang2(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_2.png')

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(26, 8.5), dpi=300)
    ax = fig.add_axes([0.02, 0.08, 0.96, 0.82])
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
    COLOR_STAIR_FILL = '#ffffff'    # Floor 2 stair fill is pure white per Spec

    WALL_THICKNESS = 0.20           # 200mm exterior wall
    PART_THICKNESS = 0.10           # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    X_MIN = -24.5
    X_MAX = 44.5

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line per Spec)
    fig.text(0.03, 0.952, 'MẶT BẰNG TẦNG 2  —  TÒA ÁN NHÂN DÂN KHU VỰC 8 - CÀ MAU', 
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.932, 0.932], transform=fig.transFigure, color='#e2e8f0', linewidth=1.1)
    fig.lines.append(header_line)

    # Legend Box Centered at Bottom
    lg_x, lg_y = 0.0, -8.2
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x - 12.0, lg_y), 1.2, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x - 10.4, lg_y + 0.05, 'Hành lang', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x - 3.0, lg_y + 0.10), 1.2, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x - 1.4, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 6.0, lg_x + 7.2], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 6.0, lg_x + 7.2], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 7.6, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 13.5, lg_x + 13.5], [lg_y + 0.02, lg_y + 0.32], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 13.5, lg_y + 0.02), 0.60, 0.60, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 14.8, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR BACKGROUND FILL (FULLY ENCLOSED ON FLOOR 2)
    # ---------------------------------------------------------
    # Horizontal Central Corridor (X: -24.5 to 44.5, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((X_MIN, -0.9), X_MAX - X_MIN, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Stair Hall on North (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (ALL 11 ROOMS STRICTLY MATCHING PROMPT SURVEY)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # ==========================================
        # === CÁNH TÂY (WEST WING: 5 PHÒNG) ===
        # ==========================================
        # --- Dãy Bắc Cánh Tây (3 Phòng: Phòng 15, 16, 17) ---
        {
            'id': 'P15', 'name': 'Phòng 15',
            'x': -24.5, 'y': 0.9, 'w': 11.0, 'h': 4.5,
            'text_center': (-19.0, 3.15),
            'door': (-14.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P16', 'name': 'Phòng 16',
            'x': -13.5, 'y': 0.9, 'w': 10.5, 'h': 4.5,
            'text_center': (-8.25, 3.15),
            'door': (-4.0, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P17', 'name': 'Phòng 17',
            'x': -3.0, 'y': 0.9, 'w': 10.5, 'h': 4.5,
            'text_center': (2.25, 3.15),
            'door': (6.2, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },

        # --- Dãy Nam Cánh Tây (2 Phòng: Phòng 18, 19) ---
        {
            'id': 'P18', 'name': 'Phòng 18',
            'x': -24.5, 'y': -4.9, 'w': 16.0, 'h': 4.0,
            'text_center': (-16.5, -2.9),
            'door': (-10.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
        {
            'id': 'P19', 'name': 'Phòng 19',
            'x': -8.5, 'y': -4.9, 'w': 16.0, 'h': 4.0,
            'text_center': (-0.5, -2.9),
            'door': (6.2, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 11.0
        },

        # ==========================================
        # === KHU TRUNG TÂM PHÍA NAM (1 PHÒNG: PHÒNG 20) ===
        # (Chuyển đổi vị trí sảnh đón tầng 1 thành phòng chức năng độc lập theo Spec)
        # ==========================================
        {
            'id': 'P20', 'name': 'Phòng 20',
            'x': 7.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (10.0, -2.9),
            'door': (8.5, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.5
        },

        # ==========================================
        # === CÁNH ĐÔNG (EAST WING: 5 PHÒNG) ===
        # ==========================================
        # --- Dãy Bắc Cánh Đông (3 Phòng: Phòng 21, 22, 23) ---
        {
            'id': 'P21', 'name': 'Phòng 21',
            'x': 12.5, 'y': 0.9, 'w': 10.5, 'h': 4.5,
            'text_center': (17.75, 3.15),
            'door': (13.8, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P22', 'name': 'Phòng 22',
            'x': 23.0, 'y': 0.9, 'w': 10.5, 'h': 4.5,
            'text_center': (28.25, 3.15),
            'door': (24.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P23', 'name': 'Phòng 23',
            'x': 33.5, 'y': 0.9, 'w': 11.0, 'h': 4.5,
            'text_center': (39.0, 3.15),
            'door': (35.0, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },

        # --- Dãy Nam Cánh Đông (2 Phòng: Phòng 24, 25) ---
        {
            'id': 'P24', 'name': 'Phòng 24',
            'x': 12.5, 'y': -4.9, 'w': 16.0, 'h': 4.0,
            'text_center': (20.5, -2.9),
            'door': (13.8, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
        {
            'id': 'P25', 'name': 'Phòng 25',
            'x': 28.5, 'y': -4.9, 'w': 16.0, 'h': 4.0,
            'text_center': (36.5, -2.9),
            'door': (30.0, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE (TẦNG 2: NỀN TRẮNG, CÓ HƯỚNG ĐI XUỐNG TẦNG 1)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.8, 2.6, 2.7
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 10
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Vertical dividing line down center
    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Down arrow on staircase
    ax.annotate('', xy=(mid_x - 0.65, stair_y + 0.35), xytext=(mid_x - 0.65, stair_y + 2.05),
                arrowprops=dict(arrowstyle="->", color=COLOR_WALL, lw=1.2), zorder=6)
    ax.text(mid_x - 0.65, stair_y + 2.2, 'XUỐNG', color=COLOR_TEXT_MUTED, fontsize=7.0, 
            ha='center', va='bottom', zorder=6,
            bbox=dict(boxstyle='square,pad=0.1', facecolor='#ffffff', edgecolor='none'))

    # Staircase label underneath box
    ax.text(stair_x + stair_w / 2.0, 1.35, 'Cầu thang bộ\n(Xuống tầng 1)', 
            color=COLOR_TEXT_MAIN, fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=5)

    # Labels for Corridor and Hall
    ax.text(-8.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(28.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(10.0, 0.0, 'SẢNH TẦNG 2', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW STRUCTURAL WALLS (ENCLOSED PERIMETER ON FLOOR 2)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior Perimeter Walls (Enclosed on all 4 sides on Floor 2, NO outdoor openings/steps)
    # North Exterior Wall (Continuous from X_MIN-W to X_MAX+W at Y = 5.4m)
    draw_wall(X_MIN - W, 5.4, (X_MAX - X_MIN) + 2*W, W)

    # South Exterior Wall (Continuous from X_MIN-W to X_MAX+W at Y = -4.9m - W)
    draw_wall(X_MIN - W, -4.9 - W, (X_MAX - X_MIN) + 2*W, W)

    # West Exterior Wall (Enclosed from Y = -4.9-W to 5.4+W)
    draw_wall(X_MIN - W, -4.9 - W, W, 10.3 + 2*W)

    # East Exterior Wall (Enclosed from Y = -4.9-W to 5.4+W)
    draw_wall(X_MAX, -4.9 - W, W, 10.3 + 2*W)

    # Vertical Internal Partitions (North Wing Y: 0.9 to 5.4m)
    north_part_x = [-13.5, -3.0, 7.5, 12.5, 23.0, 33.5]
    for px in north_part_x:
        draw_wall(px - P/2, 0.9, P, 4.5)

    # Vertical Internal Partitions (South Wing Y: -4.9 to -0.9m)
    south_part_x = [-8.5, 7.5, 12.5, 28.5]
    for px in south_part_x:
        draw_wall(px - P/2, -4.9, P, 4.0)

    # North Corridor Wall Line (Y = 0.9m) - Broken cleanly at door openings
    # P15: door at -14.5 to -13.6
    draw_wall(X_MIN, 0.9 - P/2, (-14.5 - X_MIN), P)
    draw_wall(-13.6, 0.9 - P/2, 0.1, P)
    # P16: door at -4.0 to -3.1
    draw_wall(-13.5, 0.9 - P/2, 9.5, P)
    draw_wall(-3.1, 0.9 - P/2, 0.1, P)
    # P17: door at 6.2 to 7.1
    draw_wall(-3.0, 0.9 - P/2, 9.2, P)
    draw_wall(7.1, 0.9 - P/2, 0.4, P)
    # (X: 7.5 to 12.5 is Stair Hall Open Entrance)
    # P21: door at 13.8 to 14.7
    draw_wall(12.5, 0.9 - P/2, 1.3, P)
    draw_wall(14.7, 0.9 - P/2, 8.3, P)
    # P22: door at 24.5 to 25.4
    draw_wall(23.0, 0.9 - P/2, 1.5, P)
    draw_wall(25.4, 0.9 - P/2, 8.1, P)
    # P23: door at 35.0 to 35.9
    draw_wall(33.5, 0.9 - P/2, 1.5, P)
    draw_wall(35.9, 0.9 - P/2, (X_MAX - 35.9), P)

    # South Corridor Wall Line (Y = -0.9m) - Broken cleanly at door openings
    # P18: door at -10.0 to -9.1
    draw_wall(X_MIN, -0.9 - P/2, (-10.0 - X_MIN), P)
    draw_wall(-9.1, -0.9 - P/2, 0.6, P)
    # P19: door at 6.2 to 7.1
    draw_wall(-8.5, -0.9 - P/2, 14.7, P)
    draw_wall(7.1, -0.9 - P/2, 0.4, P)
    # P20: door at 8.5 to 9.4 (Center South Room)
    draw_wall(7.5, -0.9 - P/2, 1.0, P)
    draw_wall(9.4, -0.9 - P/2, 3.1, P)
    # P24: door at 13.8 to 14.7
    draw_wall(12.5, -0.9 - P/2, 1.3, P)
    draw_wall(14.7, -0.9 - P/2, 13.8, P)
    # P25: door at 30.0 to 30.9
    draw_wall(28.5, -0.9 - P/2, 1.5, P)
    draw_wall(30.9, -0.9 - P/2, (X_MAX - 30.9), P)

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

    # Windows on North Exterior Wall (Y = 5.4m)
    # West North rooms:
    draw_window(-21.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(-16.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(-10.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(-6.0, 5.4, 2.0, W, is_horizontal=True)
    draw_window(0.0, 5.4, 2.0, W, is_horizontal=True)
    draw_window(4.5, 5.4, 2.0, W, is_horizontal=True)
    # Stair Hall North Window:
    draw_window(9.0, 5.4, 2.0, W, is_horizontal=True)
    # East North rooms:
    draw_window(15.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(20.0, 5.4, 2.0, W, is_horizontal=True)
    draw_window(26.0, 5.4, 2.0, W, is_horizontal=True)
    draw_window(30.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(36.5, 5.4, 2.0, W, is_horizontal=True)
    draw_window(41.0, 5.4, 2.0, W, is_horizontal=True)

    # Windows on South Exterior Wall (Y = -4.9m - W)
    # West South rooms:
    draw_window(-21.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(-17.0, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(-12.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(-5.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(-1.0, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(3.5, -4.9 - W, 2.0, W, is_horizontal=True)
    # Center South Room (Phòng 20) Front Windows:
    draw_window(9.0, -4.9 - W, 2.0, W, is_horizontal=True)
    # East South rooms:
    draw_window(15.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(20.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(25.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(31.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(36.5, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(41.5, -4.9 - W, 2.0, W, is_horizontal=True)

    # Windows on West & East End Walls (including corridor daylighting windows)
    draw_window(X_MIN - W, 2.0, W, 1.8, is_horizontal=False)
    draw_window(X_MIN - W, -0.6, W, 1.2, is_horizontal=False)  # West corridor window
    draw_window(X_MIN - W, -3.8, W, 1.8, is_horizontal=False)

    draw_window(X_MAX, 2.0, W, 1.8, is_horizontal=False)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)      # East corridor window
    draw_window(X_MAX, -3.8, W, 1.8, is_horizontal=False)

    # ---------------------------------------------------------
    # 8. DRAW DOORS (INWARD SWINGING PER SPEC)
    # ---------------------------------------------------------
    def draw_door(hx, hy, dw, dtype):
        if dtype == 'N_IN_RIGHT':
            ax.plot([hx, hx], [hy, hy + dw], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((hx, hy), dw * 2, dw * 2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc)
        elif dtype == 'S_IN_RIGHT':
            ax.plot([hx, hx], [hy, hy - dw], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((hx, hy), dw * 2, dw * 2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc)

    for r in rooms:
        if r['door']:
            dx, dy, dw, dtype = r['door']
            draw_door(dx, dy, dw, dtype)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS (FULL ROOM NAMES FROM SURVEY PROMPT)
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'], 
                fontweight='bold', ha='center', va='center', zorder=20)

    # Save high-resolution PNG
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Floorplan Tầng 2 successfully generated at: {out_img_path}")

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau8\Tang2"
    create_floorplan_tang2(target_dir)
