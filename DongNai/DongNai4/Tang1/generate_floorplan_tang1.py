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

def create_floorplan_tang1():
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
    COLOR_STAIR_FILL = '#eef4f7'    # Floor 1 stair background matches lobby

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.03, 0.95, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 4 - Đồng Nai', 
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
    # Horizontal Corridor (X: 0 to 35, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 35.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Front Main Lobby Space (X: 15.0 to 20.0, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((15.0, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Stair & Passage Hall Space (X: 15.0 to 20.0, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((15.0, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẦNG 1 - TÒA ÁN KHU VỰC 4 - ĐỒNG NAI)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # North Wing (Y > 0.9)
        {
            'id': 'P1_XXA', 'name': 'Phòng xét xử A',
            'x': 0.0, 'y': 0.9, 'w': 15.0, 'h': 4.5,
            'text_center': (7.5, 3.15),
            'door': (13.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.5
        },
        {
            'id': 'P1_XXB', 'name': 'Phòng xét xử B',
            'x': 20.0, 'y': 0.9, 'w': 15.0, 'h': 4.5,
            'text_center': (27.5, 3.15),
            'door': (21.0, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.5
        },
        # South Wing (Y < -0.9)
        {
            'id': 'P1_TD', 'name': 'Phòng tiếp dân',
            'x': 0.0, 'y': -4.9, 'w': 8.0, 'h': 4.0,
            'text_center': (4.0, -2.9),
            'door': (6.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P1_HG', 'name': 'Phòng hòa giải',
            'x': 8.0, 'y': -4.9, 'w': 7.0, 'h': 4.0,
            'text_center': (11.5, -2.9),
            'door': (9.0, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P1_KT', 'name': 'Phòng kế toán',
            'x': 20.0, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (23.75, -2.9),
            'door': (21.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        {
            'id': 'P1_TP', 'name': 'Phòng Thẩm phán',
            'x': 27.5, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (31.25, -2.9),
            'door': (28.5, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHIC (GROUND FLOOR)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 16.2, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    gap = 0.35
    flight_w = (stair_w - gap) / 2.0
    left_x1, left_x2 = stair_x, stair_x + flight_w
    right_x1, right_x2 = stair_x + flight_w + gap, stair_x + stair_w

    num_treads = 9
    landing_y = stair_y + stair_h
    ax.plot([stair_x, stair_x + stair_w], [landing_y, landing_y], color=COLOR_WALL, linewidth=1.0, zorder=4)

    for i in range(num_treads):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([left_x1, left_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
        ax.plot([right_x1, right_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_left = left_x1 + flight_w / 2.0
    mid_right = right_x1 + flight_w / 2.0
    ax.plot([mid_left, mid_left], [stair_y, stair_y + stair_h * (num_treads - 1) / num_treads], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([mid_right, mid_right], [stair_y, stair_y + stair_h * (num_treads - 1) / num_treads], color=COLOR_WALL, linewidth=0.9, zorder=4)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.3, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # Labels for Corridor & Lobby
    ax.text(7.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(27.5, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(17.5, -2.9, 'SẢNH CHÍNH', color=COLOR_TEXT_MAIN, fontsize=11.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. EXTERIOR STEPS (OUTDOOR STEPS)
    # ---------------------------------------------------------
    # Front South Entrance Steps (Y: -4.9 to -5.7, X: 15.0 to 20.0)
    for i in range(4):
        step_y = -4.9 - 0.2 * (i + 1)
        ax.plot([15.0, 20.0], [step_y, step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Rear North Exit Steps (Y: 5.4 to 6.2, X: 15.0 to 20.0)
    for i in range(4):
        step_y = 5.4 + 0.2 * (i + 1)
        ax.plot([15.0, 20.0], [step_y, step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # West Corridor Exit Steps (X: 0.0 to -0.8, Y: -0.9 to 0.9)
    for i in range(4):
        step_x = 0.0 - 0.2 * (i + 1)
        ax.plot([step_x, step_x], [-0.9, 0.9], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # East Corridor Exit Steps (X: 35.0 to 35.8, Y: -0.9 to 0.9)
    for i in range(4):
        step_x = 35.0 + 0.2 * (i + 1)
        ax.plot([step_x, step_x], [-0.9, 0.9], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # ---------------------------------------------------------
    # 7. DRAW WALLS (STRUCTURAL WALLS & PARTITIONS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Walls (Split around open corridor Y: -0.9 to 0.9)
    draw_wall(-W, 0.9, W, 4.5 + W)
    draw_wall(-W, -4.9 - W, W, 4.0 + W)

    # Rightmost Vertical Exterior Walls (Split around open corridor Y: -0.9 to 0.9)
    draw_wall(35.0, 0.9, W, 4.5 + W)
    draw_wall(35.0, -4.9 - W, W, 4.0 + W)

    # Topmost Horizontal Exterior Wall (North Facade, split around rear exit X: 15.0 to 20.0)
    draw_wall(-W, 5.4, 15.0 + W, W)
    draw_wall(20.0, 5.4, 15.0 + W, W)

    # Bottommost Horizontal Exterior Wall (South Facade, split around main lobby X: 15.0 to 20.0)
    draw_wall(-W, -4.9 - W, 15.0 + W, W)
    draw_wall(20.0, -4.9 - W, 15.0 + W, W)

    # Outdoor Extended Walls: Front Entrance (South)
    draw_wall(15.0 - W, -5.7, W, 0.8 + W)
    draw_wall(20.0, -5.7, W, 0.8 + W)

    # Outdoor Extended Walls: Rear Exit (North) with inward hooks
    draw_wall(15.0 - W, 5.4, W, 0.8 + W)
    draw_wall(20.0, 5.4, W, 0.8 + W)
    # Hooks turning inward 0.5m
    draw_wall(15.0, 6.2, 0.5, W)
    draw_wall(19.5, 6.2, 0.5, W)

    # Corridor North Horizontal Wall (Y = 0.9 - W, split for doors & passage)
    draw_wall(0.0, 0.9 - W, 13.5, W)
    draw_wall(14.4, 0.9 - W, 0.6, W)
    draw_wall(20.0, 0.9 - W, 1.0, W)
    draw_wall(21.9, 0.9 - W, 13.1, W)

    # Corridor South Horizontal Wall (Y = -0.9, split for doors & lobby)
    draw_wall(0.0, -0.9, 6.8, W)
    draw_wall(7.65, -0.9, 1.35, W)
    draw_wall(9.85, -0.9, 5.15, W)
    draw_wall(20.0, -0.9, 1.2, W)
    draw_wall(22.05, -0.9, 6.45, W)
    draw_wall(29.35, -0.9, 5.65, W)

    # Interior Partitions (North Wing)
    draw_wall(15.0 - PART_THICKNESS, 0.9, PART_THICKNESS, 4.5)
    draw_wall(20.0, 0.9, PART_THICKNESS, 4.5)

    # Interior Partitions (South Wing)
    draw_wall(8.0 - PART_THICKNESS/2.0, -4.9, PART_THICKNESS, 4.0)
    draw_wall(15.0 - PART_THICKNESS, -4.9, PART_THICKNESS, 4.0)
    draw_wall(20.0, -4.9, PART_THICKNESS, 4.0)
    draw_wall(27.5 - PART_THICKNESS/2.0, -4.9, PART_THICKNESS, 4.0)

    # ---------------------------------------------------------
    # 8. DRAW WINDOWS
    # ---------------------------------------------------------
    def draw_window(x, y, w, h):
        ax.add_patch(patches.Rectangle((x, y - 0.02), w, h + 0.04, facecolor='#ffffff', edgecolor='none', zorder=11))
        ax.plot([x, x + w], [y + 0.03, y + 0.03], color=COLOR_WALL, linewidth=1.2, zorder=12)
        ax.plot([x, x + w], [y + h - 0.03, y + h - 0.03], color=COLOR_WALL, linewidth=1.2, zorder=12)

    # North Facade Windows
    draw_window(3.0, 5.4, 3.0, W)    # P1_XXA
    draw_window(9.0, 5.4, 3.0, W)    # P1_XXA
    draw_window(23.0, 5.4, 3.0, W)   # P1_XXB
    draw_window(29.0, 5.4, 3.0, W)   # P1_XXB

    # South Facade Windows
    draw_window(2.5, -4.9 - W, 3.0, W)   # Phòng tiếp dân
    draw_window(10.0, -4.9 - W, 2.5, W)  # Phòng hòa giải
    draw_window(22.5, -4.9 - W, 2.5, W)  # Phòng kế toán
    draw_window(30.0, -4.9 - W, 2.5, W)  # Phòng Thẩm phán

    # ---------------------------------------------------------
    # 9. DRAW DOORS & SWINGS
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
    # 10. DRAW ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 10.5)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, 
                fontweight='bold', ha='center', va='center', zorder=15)

    ax.set_xlim(-3.0, 38.0)
    ax.set_ylim(-8.0, 8.5)

    out_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\DongNai\DongNai4\Tang1"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mat_bang_tang_1.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ Tầng 1 đã xuất thành công tại: {out_path}")

if __name__ == "__main__":
    create_floorplan_tang1()
