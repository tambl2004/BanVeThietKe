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

COURT_NAME = "Tòa án nhân dân khu vực 10 - Đồng Nai"

def create_floorplan_tang2(court_name: str = COURT_NAME):
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
    COLOR_STAIR_FILL = '#ffffff'    # Pure white stair fill for upper floors per Spec

    WALL_THICKNESS = 0.22  # 220mm thick exterior walls
    PART_THICKNESS = 0.08  # 80mm thin interior walls/partitions
    W = WALL_THICKNESS
    P = PART_THICKNESS
    X_MAX = 35.0           # Single Building Total Length = 35.0m
    X_LOBBY_L = 15.0       # Center Left X = 15.0m
    X_LOBBY_R = 20.0       # Center Right X = 20.0m

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, f'MẶT BẰNG TẦNG 2  —  {court_name}', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.03, 0.97], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Left
    lg_x, lg_y = 1.0, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

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
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (ENCLOSED EXITS)
    # ---------------------------------------------------------
    # Main Horizontal Corridor (X: 0 to 35.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Central Stair Hall Space (X: 15.0 to 20.0, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((X_LOBBY_L, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 2 - 5 PHÒNG)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # === DÃY PHÍA BẮC (North Wing: Y > 0.9m) ===
        # Cánh Tây Bắc (X: 0.0 to 15.0m)
        {
            'id': 'T2_CA', 'name': 'Phòng Chánh án',
            'x': 0.0, 'y': 0.9, 'w': 15.0, 'h': 4.5,
            'text_center': (7.5, 3.15),
            'door': (13.5, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 11.0
        },
        # Cánh Đông Bắc (X: 20.0 to 35.0m)
        {
            'id': 'T2_TP', 'name': 'Phòng thẩm phán',
            'x': 20.0, 'y': 0.9, 'w': 15.0, 'h': 4.5,
            'text_center': (27.5, 3.15),
            'door': (21.5, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 11.0
        },

        # === DÃY PHÍA NAM (South Wing: Y < -0.9m) ===
        # Cánh Tây Nam (X: 0.0 to 15.0m)
        {
            'id': 'T2_TK1', 'name': 'Phòng thư ký',
            'x': 0.0, 'y': -4.9, 'w': 15.0, 'h': 4.0,
            'text_center': (7.5, -2.9),
            'door': (13.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
        # Trung tâm phía Nam (X: 15.0 to 20.0m)
        {
            'id': 'T2_TK2', 'name': 'Phòng thư ký',
            'x': 15.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (17.5, -2.9),
            'door': (16.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 9.5
        },
        # Cánh Đông Nam (X: 20.0 to 35.0m)
        {
            'id': 'T2_TK3', 'name': 'Phòng thư ký',
            'x': 20.0, 'y': -4.9, 'w': 15.0, 'h': 4.0,
            'text_center': (27.5, -2.9),
            'door': (21.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE (TẦNG 2: PURE WHITE STAIRCASE FILL)
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

    # Labels for Corridor
    ax.text(7.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(27.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (PRECISION STRUCTURAL WALLS & PARTITIONS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Exterior West Wall (Continuous, fully enclosed at X = -W)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2*W)

    # Exterior East Wall (Continuous, fully enclosed at X = X_MAX)
    draw_wall(X_MAX, -4.9 - W, W, 10.3 + 2*W)

    # Exterior North Wall (Continuous, fully enclosed at Y = 5.4m)
    draw_wall(-W, 5.4, X_MAX + 2*W, W)

    # Exterior South Wall (Continuous, fully enclosed at Y = -4.9m)
    draw_wall(-W, -4.9 - W, X_MAX + 2*W, W)

    # --- THIN INTERIOR WALLS (P = 0.08m) ---
    # Corridor North Wall Y = 0.9 (Doors at X: 13.5 to 14.35, X: 21.5 to 22.35)
    draw_wall(0.0, 0.9 - P/2, 13.5, P)
    draw_wall(14.35, 0.9 - P/2, 0.65, P)
    # Stair Hall open at X: 15.0 to 20.0
    draw_wall(20.0, 0.9 - P/2, 1.5, P)
    draw_wall(22.35, 0.9 - P/2, 12.65, P)

    # Corridor South Wall Y = -0.9 (Doors at X: 13.5 to 14.35, X: 16.2 to 17.05, X: 21.2 to 22.05)
    draw_wall(0.0, -0.9 - P/2, 13.5, P)
    draw_wall(14.35, -0.9 - P/2, 1.85, P)
    draw_wall(17.05, -0.9 - P/2, 4.15, P)
    draw_wall(22.05, -0.9 - P/2, 12.95, P)

    # Internal Partitions North Wing (Thin P = 0.08m)
    draw_wall(15.0 - P, 0.9 - P/2, P, 4.5 + P/2)    # Left of stair hall (flush at 15.0)
    draw_wall(20.0, 0.9 - P/2, P, 4.5 + P/2)        # Right of stair hall (flush at 20.0)

    # Internal Partitions South Wing (Thin P = 0.08m)
    draw_wall(15.0 - P, -4.9, P, 4.0 + P/2)         # West of center room (flush at 15.0)
    draw_wall(20.0, -4.9, P, 4.0 + P/2)             # East of center room (flush at 20.0)

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
    draw_window(2.5, 5.4, 3.5, W, is_horizontal=True)     # Phòng Chánh án W1
    draw_window(8.5, 5.4, 3.5, W, is_horizontal=True)     # Phòng Chánh án W2
    draw_window(16.0, 5.4, 3.0, W, is_horizontal=True)    # Sảnh cầu thang
    draw_window(22.5, 5.4, 3.5, W, is_horizontal=True)    # Phòng thẩm phán E1
    draw_window(28.5, 5.4, 3.5, W, is_horizontal=True)    # Phòng thẩm phán E2

    # South Windows (Y = -4.9 - W)
    draw_window(2.5, -4.9 - W, 3.2, W, is_horizontal=True)    # Phòng thư ký SW1
    draw_window(8.5, -4.9 - W, 3.2, W, is_horizontal=True)    # Phòng thư ký SW2
    draw_window(16.2, -4.9 - W, 2.6, W, is_horizontal=True)   # Phòng thư ký S Center
    draw_window(22.5, -4.9 - W, 3.2, W, is_horizontal=True)   # Phòng thư ký SE1
    draw_window(28.5, -4.9 - W, 3.2, W, is_horizontal=True)   # Phòng thư ký SE2

    # West & East Side Windows (Including Corridor End Windows)
    draw_window(-W, 0.0 - 0.5, W, 1.0, is_horizontal=False)   # West corridor end window
    draw_window(X_MAX, 0.0 - 0.5, W, 1.0, is_horizontal=False) # East corridor end window
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
    out_png = os.path.join(out_dir, 'mat_bang_tang_2.png')
    plt.savefig(out_png, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Bản vẽ Tầng 2 đã được xuất thành công: {out_png}")

if __name__ == '__main__':
    create_floorplan_tang2()
