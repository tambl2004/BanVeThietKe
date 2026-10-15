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

COURT_NAME = "Tòa án nhân dân khu vực 9 - Đồng Nai"

def create_floorplan_tang1(court_name: str = COURT_NAME):
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(22, 11), dpi=300)
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
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 stair fill matches lobby background

    WALL_THICKNESS = 0.22  # 220mm exterior structural wall (dày)
    PART_THICKNESS = 0.08  # 80mm interior partition & corridor wall (mỏng, thanh thoát)
    W = WALL_THICKNESS
    P = PART_THICKNESS
    X_MAX = 35.0           # Single Building Total Length = 35.0m
    X_LOBBY_L = 15.0       # Lobby Left X = 15.0m
    X_LOBBY_R = 20.0       # Lobby Right X = 20.0m

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, f'MẶT BẰNG TẦNG 1  —  {court_name}', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = 1.0, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 6.0, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 7.1, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 11.5, lg_x + 12.5], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.4, zorder=1)
    ax.plot([lg_x + 11.5, lg_x + 12.5], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.4, zorder=1)
    ax.text(lg_x + 12.8, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 16.5, lg_x + 16.5], [lg_y + 0.05, lg_y + 0.35], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 16.5, lg_y + 0.05), 0.6, 0.6, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 17.5, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (OPEN EXITS)
    # ---------------------------------------------------------
    # Main Horizontal Corridor (X: 0 to 35.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Front Main Lobby Space (X: 15.0 to 20.0, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((X_LOBBY_L, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Stair & Passage Hall Space (X: 15.0 to 20.0, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((X_LOBBY_L, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TÒA ÁN KHU VỰC 9 - ĐỒNG NAI: TẦNG 1 - 8 PHÒNG)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === DÃY PHÍA BẮC (North Wing: Y > 0.9m) ===
        # Cánh Tây Bắc (X: 0.0 to 15.0m)
        {
            'id': 'T1_XXDS', 'name': 'Phòng xét xử Dân sự',
            'x': 0.0, 'y': 0.9, 'w': 8.5, 'h': 4.5,
            'text_center': (4.25, 3.15),
            'door': (7.2, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'T1_NA', 'name': 'Phòng nghị án',
            'x': 8.5, 'y': 0.9, 'w': 6.5, 'h': 4.5,
            'text_center': (11.75, 3.15),
            'door': (13.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        # Cánh Đông Bắc (X: 20.0 to 35.0m)
        {
            'id': 'T1_XXHS', 'name': 'Phòng XX hình sự',
            'x': 20.0, 'y': 0.9, 'w': 8.0, 'h': 4.5,
            'text_center': (24.0, 3.15),
            'door': (21.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'T1_HG', 'name': 'Phòng Hòa giải đối thoại',
            'x': 28.0, 'y': 0.9, 'w': 7.0, 'h': 4.5,
            'text_center': (31.5, 3.15),
            'door': (29.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.0
        },

        # === DÃY PHÍA NAM (South Wing: Y < -0.9m) ===
        # Cánh Tây Nam (X: 0.0 to 15.0m)
        {
            'id': 'T1_TDVP', 'name': 'Phòng tiếp dân, văn - Phòng',
            'x': 0.0, 'y': -4.9, 'w': 8.0, 'h': 4.0,
            'text_center': (4.0, -2.9),
            'door': (6.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        {
            'id': 'T1_TDS', 'name': 'Phòng làm việc tiếp đương sự',
            'x': 8.0, 'y': -4.9, 'w': 7.0, 'h': 4.0,
            'text_center': (11.5, -2.9),
            'door': (13.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.2
        },
        # Cánh Đông Nam (X: 20.0 to 35.0m)
        {
            'id': 'T1_KT', 'name': 'Phòng kế toán',
            'x': 20.0, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (23.75, -2.9),
            'door': (21.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        {
            'id': 'T1_LV_KHO', 'name': 'Phòng làm việc để trống làm kho',
            'x': 27.5, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (31.25, -2.9),
            'door': (29.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS (FLOOR 1 SPEC)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 16.2, 1.4, 2.6, 2.6
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

    # Front Main Entrance Steps (South: Y = -4.9 to -5.7m, X: 15.0 to 20.0m)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([X_LOBBY_L, X_LOBBY_R], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([X_LOBBY_L, X_LOBBY_L], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.plot([X_LOBBY_R, X_LOBBY_R], [-4.9, -5.70], color=COLOR_WALL, linewidth=1.2, zorder=4)

    # Rear North Exit Steps (North: Y = 5.4 to 6.2m, X: 15.0 to 20.0m)
    for i in range(4):
        step_y = 5.4 + 0.2 * (i + 1)
        ax.plot([X_LOBBY_L, X_LOBBY_R], [step_y, step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # West & East Corridor Exit Steps (Open Corridor Exits)
    for i in range(4):
        step_x = 0.0 - 0.2 * (i + 1)
        ax.plot([step_x, step_x], [-0.9, 0.9], color=COLOR_WALL, linewidth=0.9, zorder=4)

    for i in range(4):
        step_x = X_MAX + 0.2 * (i + 1)
        ax.plot([step_x, step_x], [-0.9, 0.9], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Labels for Lobby and Corridor
    ax.text(17.5, -2.9, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(7.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(27.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (THICK EXTERIOR WALLS & THIN INTERIOR PARTITIONS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior West Wall (Thick, open at Corridor Y: -0.9 to 0.9)
    draw_wall(-W, 0.9, W, 4.5 + W)
    draw_wall(-W, -4.9 - W, W, 4.0 + W)

    # Exterior East Wall (Thick, open at Corridor Y: -0.9 to 0.9)
    draw_wall(X_MAX, 0.9, W, 4.5 + W)
    draw_wall(X_MAX, -4.9 - W, W, 4.0 + W)

    # Exterior North Wall (Thick, Y = 5.4m, open for rear exit at X: 15.0 to 20.0m)
    draw_wall(-W, 5.4, X_LOBBY_L + W, W)
    draw_wall(X_LOBBY_R, 5.4, (X_MAX - X_LOBBY_R) + W, W)

    # Exterior South Wall (Thick, Y = -4.9m, open for main entrance at X: 15.0 to 20.0m)
    draw_wall(-W, -4.9 - W, X_LOBBY_L + W, W)
    draw_wall(X_LOBBY_R, -4.9 - W, (X_MAX - X_LOBBY_R) + W, W)

    # Front Entrance Side Cheeks (Thick, South: Y = -4.9 to -5.7m, exactly flush with building exterior)
    draw_wall(X_LOBBY_L - W, -5.7, W, 0.8)
    draw_wall(X_LOBBY_R, -5.7, W, 0.8)

    # Rear Exit Side Walls with inward hooks (Thick, North: Y = 5.4 to 6.2m, exactly flush with hooks at 6.2m)
    draw_wall(X_LOBBY_L - W, 5.4, W, 0.8)
    draw_wall(X_LOBBY_R, 5.4, W, 0.8)
    # Hooks turning inward 0.5m per Spec (Top flush at Y = 6.2m)
    draw_wall(X_LOBBY_L, 6.2 - W, 0.5, W)
    draw_wall(X_LOBBY_R - 0.5, 6.2 - W, 0.5, W)

    # --- THIN INTERIOR WALLS (P = 0.08m) ---
    # Corridor North Wall Y = 0.9 (Thin P=0.08m, centered at Y = 0.9)
    # Doors at X: 7.2 to 8.1, X: 13.5 to 14.4, X: 21.5 to 22.4, X: 29.5 to 30.4
    draw_wall(0.0, 0.9 - P/2, 7.2, P)
    draw_wall(8.1, 0.9 - P/2, 5.4, P)
    draw_wall(14.4, 0.9 - P/2, 0.6, P)
    # Sảnh thang / lối ra sau mở tại X: 15.0 to 20.0
    draw_wall(20.0, 0.9 - P/2, 1.5, P)
    draw_wall(22.4, 0.9 - P/2, 7.1, P)
    draw_wall(30.4, 0.9 - P/2, 4.6, P)

    # Corridor South Wall Y = -0.9 (Thin P=0.08m, centered at Y = -0.9)
    # Doors at X: 6.8 to 7.65, X: 13.5 to 14.35, X: 21.5 to 22.35, X: 29.0 to 29.85
    draw_wall(0.0, -0.9 - P/2, 6.8, P)
    draw_wall(7.65, -0.9 - P/2, 5.85, P)
    draw_wall(14.35, -0.9 - P/2, 0.65, P)
    # Sảnh chính mở tại X: 15.0 to 20.0
    draw_wall(20.0, -0.9 - P/2, 1.5, P)
    draw_wall(22.35, -0.9 - P/2, 6.65, P)
    draw_wall(29.85, -0.9 - P/2, 5.15, P)

    # Internal Vertical Partitions (Thin P=0.08m)
    # North Wing Partitions
    draw_wall(8.5 - P/2, 0.9 - P/2, P, 4.5 + P/2)      # Between XX Dân sự & Nghị án
    draw_wall(15.0 - P, 0.9 - P/2, P, 4.5 + P/2)       # West edge of rear hall (flush at X = 15.0)
    draw_wall(20.0, 0.9 - P/2, P, 4.5 + P/2)           # East edge of rear hall (flush at X = 20.0)
    draw_wall(28.0 - P/2, 0.9 - P/2, P, 4.5 + P/2)     # Between XX Hình sự & Hòa giải

    # South Wing Partitions
    draw_wall(8.0 - P/2, -4.9, P, 4.0 + P/2)           # Between Tiếp dân VP & Tiếp đương sự
    draw_wall(15.0 - P, -4.9, P, 4.0 + P/2)            # West edge of main lobby (flush at X = 15.0)
    draw_wall(20.0, -4.9, P, 4.0 + P/2)                # East edge of main lobby (flush at X = 20.0)
    draw_wall(27.5 - P/2, -4.9, P, 4.0 + P/2)          # Between Kế toán & Để trống làm kho

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

    # North Windows (Y = 5.4m)
    draw_window(2.5, 5.4, 3.5, W, is_horizontal=True)    # XX Dân sự
    draw_window(10.0, 5.4, 3.5, W, is_horizontal=True)   # Phòng nghị án
    draw_window(22.0, 5.4, 3.5, W, is_horizontal=True)   # XX Hình sự
    draw_window(29.5, 5.4, 3.5, W, is_horizontal=True)   # Hòa giải đối thoại

    # South Windows (Y = -4.9 - W)
    draw_window(2.5, -4.9 - W, 3.5, W, is_horizontal=True)   # Tiếp dân VP
    draw_window(9.5, -4.9 - W, 3.5, W, is_horizontal=True)   # Tiếp đương sự
    draw_window(22.0, -4.9 - W, 3.5, W, is_horizontal=True)  # Kế toán
    draw_window(29.5, -4.9 - W, 3.5, W, is_horizontal=True)  # Để trống làm kho

    # West & East Side Windows
    draw_window(-W, 2.25, W, 1.8, is_horizontal=False)
    draw_window(-W, -3.5, W, 1.8, is_horizontal=False)
    draw_window(X_MAX, 2.25, W, 1.8, is_horizontal=False)
    draw_window(X_MAX, -3.5, W, 1.8, is_horizontal=False)

    # ---------------------------------------------------------
    # 8. DRAW DOORS (SWINGS & LEAVES)
    # ---------------------------------------------------------
    def draw_door(x, y, w, dtype):
        if dtype == 'N_IN_RIGHT':
            ax.plot([x, x], [y, y + w], color=COLOR_DOOR_SWING, linewidth=1.2, zorder=15)
            arc = patches.Arc((x, y), 2*w, 2*w, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=15)
            ax.add_patch(arc)
        elif dtype == 'S_IN_RIGHT':
            ax.plot([x, x], [y, y - w], color=COLOR_DOOR_SWING, linewidth=1.2, zorder=15)
            arc = patches.Arc((x, y), 2*w, 2*w, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=0.9, zorder=15)
            ax.add_patch(arc)

    for r in rooms:
        dx, dy, dw, dtype = r['door']
        draw_door(dx, dy, dw, dtype)

    # ---------------------------------------------------------
    # 9. ROOM TEXT LABELS (EXACT NAMES FROM SURVEY, CENTERED)
    # ---------------------------------------------------------
    for r in rooms:
        tx, ty = r['text_center']
        ax.text(tx, ty, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'], 
                fontweight='bold', ha='center', va='center', zorder=20)

    # ---------------------------------------------------------
    # 10. SAVE FIGURE (PNG 300 DPI)
    # ---------------------------------------------------------
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_png = os.path.join(out_dir, 'mat_bang_tang_1.png')
    plt.savefig(out_png, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Bản vẽ Tầng 1 đã được xuất thành công: {out_png}")

if __name__ == '__main__':
    create_floorplan_tang1()
