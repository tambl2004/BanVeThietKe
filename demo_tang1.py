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

def create_floorplan_tang1():
    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 15), dpi=300)
    ax = fig.add_axes([0.02, 0.05, 0.96, 0.88])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    fig.text(0.03, 0.95, "MẶT BẰNG TẦNG 1 — Tòa án nhân dân khu vực 7- Bắc Ninh", 
             fontsize=20, fontweight='bold', color=COLOR_TEXT_MAIN, ha='left', va='top')

    ax.add_patch(patches.Rectangle((2, -6.5), 1.2, 0.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none'))
    ax.text(3.4, -6.3, "Hành lang / sảnh", fontsize=9, color=COLOR_TEXT_MUTED, va='center')

    ax.add_patch(patches.Rectangle((10, -6.4), 1.2, 0.2, facecolor=COLOR_WALL, edgecolor='none'))
    ax.text(11.4, -6.3, "Tường / vách", fontsize=9, color=COLOR_TEXT_MUTED, va='center')

    ax.plot([18, 19.2], [-6.3, -6.3], color=COLOR_WALL, linewidth=3)
    ax.plot([18, 19.2], [-6.15, -6.15], color=COLOR_WALL, linewidth=1)
    ax.plot([18, 19.2], [-6.45, -6.45], color=COLOR_WALL, linewidth=1)
    ax.text(19.4, -6.3, "Cửa sổ", fontsize=9, color=COLOR_TEXT_MUTED, va='center')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY FILL
    # ---------------------------------------------------------
    ax.add_patch(patches.Rectangle((0, -0.8), 32.0, 1.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.add_patch(patches.Rectangle((13.5, -4.5), 5.0, 3.7, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.add_patch(patches.Rectangle((13.5, 0.8), 5.0, 11.7, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.add_patch(patches.Rectangle((3.5, 7.8), 25.0, 1.2, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    bbox_style = dict(boxstyle='round,pad=0.2', facecolor=COLOR_FILL_CORRIDOR, edgecolor='none')
    ax.text(6.75, 0.0, "HÀNH LANG", fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6, bbox=bbox_style)
    ax.text(25.25, 0.0, "HÀNH LANG", fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6, bbox=bbox_style)
    ax.text(8.5, 8.4, "HÀNH LANG", fontsize=9, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6, bbox=bbox_style)
    ax.text(23.5, 8.4, "HÀNH LANG", fontsize=9, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=6, bbox=bbox_style)

    ax.text(16.0, -2.65, "SẢNH CHÍNH", fontsize=11, fontweight='bold', color=COLOR_TEXT_MAIN, ha='center', va='center', zorder=5)

    for i in range(5):
        dy = -4.5 - 0.2 * (i + 1)
        dx_min = 13.5 - i * 0.15
        dx_max = 18.5 + i * 0.15
        ax.plot([dx_min, dx_max], [dy, dy], color=COLOR_WALL, linewidth=1.0, zorder=4)
        ax.plot([dx_min, dx_min], [-4.5, dy], color=COLOR_WALL, linewidth=1.0, zorder=4)
        ax.plot([dx_max, dx_max], [-4.5, dy], color=COLOR_WALL, linewidth=1.0, zorder=4)

    for i in range(5):
        sx = 0.0 - (i + 1) * 0.16
        ax.plot([sx, sx], [-0.8, 0.8], color=COLOR_WALL, linewidth=1.0, zorder=4)
    for i in range(5):
        sx = 32.0 + (i + 1) * 0.16
        ax.plot([sx, sx], [-0.8, 0.8], color=COLOR_WALL, linewidth=1.0, zorder=4)

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS & INWARD DOORS
    # ---------------------------------------------------------
    rooms: List[RoomDict] = []

    rooms.append({
        'id': 'T1_HALL_MAIN', 'name': "Phòng Hội trường\nxét xử",
        'x': 0.0, 'y': -4.5, 'w': 13.5, 'h': 3.7,
        'text_center': (6.75, -2.65), 'door': (6.75, -0.8, 1.0, 'IN_SOUTH')
    })
    rooms.append({
        'id': 'T1_ACC', 'name': "Phòng Kế toán",
        'x': 0.0, 'y': 0.8, 'w': 6.75, 'h': 3.7,
        'text_center': (3.375, 2.65), 'door': (3.375, 0.8, 0.9, 'IN_NORTH')
    })
    rooms.append({
        'id': 'T1_VICE_ADMIN', 'name': "Phòng Phó Chánh văn - Phòng",
        'x': 6.75, 'y': 0.8, 'w': 6.75, 'h': 3.7,
        'text_center': (10.125, 2.65), 'door': (10.125, 0.8, 0.9, 'IN_NORTH')
    })
    rooms.append({
        'id': 'T1_TRIAL_ROOM', 'name': "Phòng xét xử",
        'x': 18.5, 'y': -4.5, 'w': 13.5, 'h': 3.7,
        'text_center': (25.25, -2.65), 'door': (25.25, -0.8, 1.0, 'IN_SOUTH')
    })
    rooms.append({
        'id': 'T1_HEAD_ADMIN', 'name': "Phòng Chánh văn - Phòng",
        'x': 18.5, 'y': 0.8, 'w': 6.75, 'h': 3.7,
        'text_center': (21.875, 2.65), 'door': (21.875, 0.8, 0.9, 'IN_NORTH')
    })
    rooms.append({
        'id': 'T1_HALL_SMALL', 'name': "Phòng Hội trường\nxét xử",
        'x': 25.25, 'y': 0.8, 'w': 6.75, 'h': 3.7,
        'text_center': (28.625, 2.65), 'door': (28.625, 0.8, 0.9, 'IN_NORTH')
    })

    rooms.append({
        'id': 'T2_JUDGE_1', 'name': "Phòng Thẩm phán",
        'x': 3.5, 'y': 4.5, 'w': 10.0, 'h': 3.3,
        'text_center': (8.5, 6.15), 'door': (8.5, 7.8, 0.9, 'IN_SOUTH')
    })
    rooms.append({
        'id': 'T2_SEC_1', 'name': "Phòng Thư ký",
        'x': 18.5, 'y': 4.5, 'w': 10.0, 'h': 3.3,
        'text_center': (23.5, 6.15), 'door': (23.5, 7.8, 0.9, 'IN_SOUTH')
    })
    rooms.append({
        'id': 'T2_JUDGE_2', 'name': "Phòng Thẩm phán",
        'x': 3.5, 'y': 9.0, 'w': 7.5, 'h': 3.5,
        'text_center': (7.25, 10.75), 'door': (7.25, 9.0, 0.9, 'IN_NORTH')
    })
    rooms.append({
        'id': 'T2_JUDGE_3', 'name': "Phòng Thẩm phán",
        'x': 11.0, 'y': 9.0, 'w': 10.0, 'h': 3.5,
        'text_center': (16.0, 10.75), 'door': (16.0, 9.0, 0.9, 'IN_NORTH')
    })
    rooms.append({
        'id': 'T2_SEC_2', 'name': "Phòng Thư ký",
        'x': 21.0, 'y': 9.0, 'w': 7.5, 'h': 3.5,
        'text_center': (24.75, 10.75), 'door': (24.75, 9.0, 0.9, 'IN_NORTH')
    })

    for r in rooms:
        ax.add_patch(patches.Rectangle((r['x'], r['y']), r['w'], r['h'], 
                                       facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))
        ax.text(r['text_center'][0], r['text_center'][1], r['name'], 
                fontsize=9.5, fontweight='bold', color=COLOR_TEXT_MAIN, 
                ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 5. STAIRCASE (MOVED HIGHER UP)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 14.7, 1.0, 2.6, 2.6
    ax.add_patch(patches.Rectangle((stair_x, stair_y), stair_w, stair_h, 
                                   facecolor='#ffffff', edgecolor=COLOR_WALL, linewidth=1.2, zorder=3))
    ax.plot([stair_x + stair_w/2, stair_x + stair_w/2], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=1.0, zorder=4)
    num_treads = 9
    for i in range(1, num_treads):
        ty = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [ty, ty], color=COLOR_WALL, linewidth=0.8, zorder=4)
    ax.text(stair_x + stair_w/2, stair_y - 0.35, "Cầu thang", fontsize=8, color=COLOR_TEXT_MUTED, ha='center', va='top', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS & CUTOUTS
    # ---------------------------------------------------------
    def draw_wall_segment(p1: Tuple[float, float], p2: Tuple[float, float], 
                          cutouts: List[Tuple[float, float]] = None, thickness=0.10):
        cutouts = cutouts or []
        x1, y1 = p1
        x2, y2 = p2
        if abs(x1 - x2) < 0.001:  # Vertical wall
            y_min, y_max = min(y1, y2), max(y1, y2)
            current_y = y_min
            sorted_cutouts = sorted(cutouts, key=lambda c: c[0])
            for cy_start, cy_end in sorted_cutouts:
                if cy_start > current_y + 0.01:
                    ax.plot([x1, x1], [current_y, cy_start], color=COLOR_WALL, linewidth=thickness*15, zorder=4, solid_capstyle='butt')
                current_y = max(current_y, cy_end)
            if current_y < y_max - 0.01:
                ax.plot([x1, x1], [current_y, y_max], color=COLOR_WALL, linewidth=thickness*15, zorder=4, solid_capstyle='butt')
        else:  # Horizontal wall
            x_min, x_max = min(x1, x2), max(x1, x2)
            current_x = x_min
            sorted_cutouts = sorted(cutouts, key=lambda c: c[0])
            for cx_start, cx_end in sorted_cutouts:
                if cx_start > current_x + 0.01:
                    ax.plot([current_x, cx_start], [y1, y1], color=COLOR_WALL, linewidth=thickness*15, zorder=4, solid_capstyle='butt')
                current_x = max(current_x, cx_end)
            if current_x < x_max - 0.01:
                ax.plot([current_x, x_max], [y1, y1], color=COLOR_WALL, linewidth=thickness*15, zorder=4, solid_capstyle='butt')

    # FIX 1: WINDOW DRAWING WITH CLEAN FULL-COVERAGE MASKING
    def draw_window(x: float, y: float, w: float, orientation: str):
        if orientation == 'H':
            ax.add_patch(patches.Rectangle((x - w/2 - 0.05, y - 0.25), w + 0.10, 0.50, facecolor='#ffffff', edgecolor='none', zorder=6))
            ax.plot([x - w/2, x + w/2], [y, y], color=COLOR_WALL, linewidth=3, zorder=7)
            ax.plot([x - w/2, x + w/2], [y + 0.08, y + 0.08], color=COLOR_WALL, linewidth=1, zorder=7)
            ax.plot([x - w/2, x + w/2], [y - 0.08, y - 0.08], color=COLOR_WALL, linewidth=1, zorder=7)
        else:
            ax.add_patch(patches.Rectangle((x - 0.25, y - w/2 - 0.05), 0.50, w + 0.10, facecolor='#ffffff', edgecolor='none', zorder=6))
            ax.plot([x, x], [y - w/2, y + w/2], color=COLOR_WALL, linewidth=3, zorder=7)
            ax.plot([x + 0.08, x + 0.08], [y - w/2, y + w/2], color=COLOR_WALL, linewidth=1, zorder=7)
            ax.plot([x - 0.08, x - 0.08], [y - w/2, y + w/2], color=COLOR_WALL, linewidth=1, zorder=7)

    # FIX 2: DOOR GAP MASK FILLED WITH CORRIDOR COLOR
    def draw_door(x: float, y: float, width: float, direction: str):
        if direction in ['IN_NORTH', 'IN_SOUTH']:
            ax.add_patch(patches.Rectangle((x - width/2, y - 0.12), width, 0.24, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=6))
            door_x = x - width/2
            if direction == 'IN_NORTH':
                ax.plot([door_x, door_x], [y, y + width], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=7)
                arc = patches.Arc((door_x, y), width*2, width*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.2, linestyle='--', zorder=7)
                ax.add_patch(arc)
            elif direction == 'IN_SOUTH':
                ax.plot([door_x, door_x], [y, y - width], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=7)
                arc = patches.Arc((door_x, y), width*2, width*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.2, linestyle='--', zorder=7)
                ax.add_patch(arc)

    y_south_corridor_cutouts = []
    y_north_corridor_cutouts = []
    for r in rooms:
        dx, dy, dw, ddir = r['door']
        if ddir == 'IN_SOUTH' and dy == -0.8:
            y_south_corridor_cutouts.append((dx - dw/2, dx + dw/2))
        elif ddir == 'IN_NORTH' and dy == 0.8:
            y_north_corridor_cutouts.append((dx - dw/2, dx + dw/2))

    # TÒA 1 EXTERIOR WALLS
    draw_wall_segment((0, -4.5), (13.5, -4.5), cutouts=[(2.6, 4.4), (9.1, 10.9)], thickness=WALL_THICKNESS)
    draw_wall_segment((18.5, -4.5), (32.0, -4.5), cutouts=[(21.1, 22.9), (27.6, 29.4)], thickness=WALL_THICKNESS)

    draw_wall_segment((0.0, -4.5), (0.0, 4.5), cutouts=[(-0.8, 0.8)], thickness=WALL_THICKNESS)
    draw_wall_segment((32.0, -4.5), (32.0, 4.5), cutouts=[(-0.8, 0.8)], thickness=WALL_THICKNESS)

    draw_wall_segment((0.0, 4.5), (3.5, 4.5), cutouts=[(2.625, 4.125)], thickness=WALL_THICKNESS)
    draw_wall_segment((28.5, 4.5), (32.0, 4.5), cutouts=[(27.875, 29.375)], thickness=WALL_THICKNESS)

    # TÒA 1 CORRIDOR INTERNAL WALLS
    draw_wall_segment((0.0, -0.8), (13.5, -0.8), cutouts=y_south_corridor_cutouts, thickness=PART_THICKNESS)
    draw_wall_segment((18.5, -0.8), (32.0, -0.8), cutouts=y_south_corridor_cutouts, thickness=PART_THICKNESS)

    draw_wall_segment((0.0, 0.8), (13.5, 0.8), cutouts=y_north_corridor_cutouts, thickness=PART_THICKNESS)
    draw_wall_segment((18.5, 0.8), (32.0, 0.8), cutouts=y_north_corridor_cutouts, thickness=PART_THICKNESS)

    # TÒA 1 INTERIOR ROOM DIVIDERS
    draw_wall_segment((6.75, 0.8), (6.75, 4.5), thickness=PART_THICKNESS)
    draw_wall_segment((25.25, 0.8), (25.25, 4.5), thickness=PART_THICKNESS)

    # SẢNH CHÍNH VERTICAL SIDE WALLS
    draw_wall_segment((13.5, -4.5), (13.5, -0.8), thickness=PART_THICKNESS)
    draw_wall_segment((18.5, -4.5), (18.5, -0.8), thickness=PART_THICKNESS)

    # FIX 3: REMOVED LOBBY WALL BLOCKAGE
    draw_wall_segment((13.5, 4.5), (13.5, 7.8), thickness=PART_THICKNESS)
    draw_wall_segment((18.5, 4.5), (18.5, 7.8), thickness=PART_THICKNESS)

    draw_wall_segment((3.5, 4.5), (13.5, 4.5), cutouts=[(9.375, 10.875)], thickness=PART_THICKNESS)
    draw_wall_segment((18.5, 4.5), (28.5, 4.5), cutouts=[(21.125, 22.625)], thickness=PART_THICKNESS)

    # TÒA 2 EXTERIOR WALLS
    draw_wall_segment((3.5, 4.5), (3.5, 12.5), cutouts=[(5.4, 6.9), (10.0, 11.5)], thickness=WALL_THICKNESS)
    draw_wall_segment((28.5, 4.5), (28.5, 12.5), cutouts=[(5.4, 6.9), (10.0, 11.5)], thickness=WALL_THICKNESS)
    draw_wall_segment((3.5, 12.5), (28.5, 12.5), cutouts=[(6.5, 8.0), (15.0, 17.0), (24.0, 25.5)], thickness=WALL_THICKNESS)

    # TÒA 2 CORRIDOR WALLS
    draw_wall_segment((3.5, 7.8), (13.5, 7.8), cutouts=[(8.05, 8.95)], thickness=PART_THICKNESS)
    draw_wall_segment((18.5, 7.8), (28.5, 7.8), cutouts=[(23.05, 23.95)], thickness=PART_THICKNESS)

    draw_wall_segment((3.5, 9.0), (28.5, 9.0), cutouts=[(6.8, 7.7), (15.55, 16.45), (24.3, 25.2)], thickness=PART_THICKNESS)

    # TÒA 2 NORTH ROW PARTITION WALLS
    draw_wall_segment((11.0, 9.0), (11.0, 12.5), thickness=PART_THICKNESS)
    draw_wall_segment((21.0, 9.0), (21.0, 12.5), thickness=PART_THICKNESS)

    # DRAW ALL DOORS
    for r in rooms:
        dx, dy, dw, ddir = r['door']
        draw_door(dx, dy, dw, ddir)

    # ---------------------------------------------------------
    # 7. WINDOWS
    # ---------------------------------------------------------
    draw_window(3.5, -4.5, 1.8, 'H')
    draw_window(10.0, -4.5, 1.8, 'H')
    draw_window(22.0, -4.5, 1.8, 'H')
    draw_window(28.5, -4.5, 1.8, 'H')

    draw_window(3.375, 4.5, 1.5, 'H')
    draw_window(10.125, 4.5, 1.5, 'H')
    draw_window(21.875, 4.5, 1.5, 'H')
    draw_window(28.625, 4.5, 1.5, 'H')

    draw_window(3.5, 6.15, 1.5, 'V')
    draw_window(28.5, 6.15, 1.5, 'V')

    draw_window(7.25, 12.5, 1.5, 'H')
    draw_window(16.0, 12.5, 2.0, 'H')
    draw_window(24.75, 12.5, 1.5, 'H')
    draw_window(3.5, 10.75, 1.5, 'V')
    draw_window(28.5, 10.75, 1.5, 'V')

    ax.set_xlim(-2.5, 34.5)
    ax.set_ylim(-7.5, 14.5)

    output_dir = r"c:\Users\Tam\Desktop\BanVeThietKe"
    output_path = os.path.join(output_dir, "mat_bang_tang_1.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"SUCCESS: Generated demo floorplan PNG at {output_path}")

if __name__ == "__main__":
    create_floorplan_tang1()
