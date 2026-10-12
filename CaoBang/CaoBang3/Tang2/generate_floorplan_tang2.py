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
    # 1. SETUP CANVAS & STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(19, 12), dpi=300)
    ax = fig.add_axes([0.03, 0.08, 0.94, 0.82])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/stair hall
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#ffffff'    # Pure white background for upper floor stairs

    WALL_THICKNESS = 0.20           # 200mm exterior wall
    PART_THICKNESS = 0.10           # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line per Spec)
    fig.text(0.04, 0.945, 'MẶT BẰNG TẦNG 2  —  TÒA ÁN NHÂN DÂN KHU VỰC 3 - CAO BẰNG', 
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.04, 0.96], [0.92, 0.92], transform=fig.transFigure, color='#e2e8f0', linewidth=1.1)
    fig.lines.append(header_line)

    # Legend Box Centered at Bottom
    lg_x, lg_y = 1.0, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.9, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.2, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 5.5, lg_y + 0.10), 0.9, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 6.7, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 10.5, lg_x + 11.7], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 10.5, lg_x + 11.7], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 12.0, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 14.8, lg_x + 14.8], [lg_y + 0.02, lg_y + 0.32], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 14.8, lg_y + 0.02), 0.60, 0.60, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 16.0, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & STAIR HALL BACKGROUND FILL
    # ---------------------------------------------------------
    # Central Horizontal Corridor (X: 0 to 20, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # North Rear Stair Hall (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (ALL 6 ROOMS STRICTLY FROM SURVEY)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- DÃY BẮC (NORTH WING: Y: 0.9 to 5.4m) ---
        # 1. Phòng Thẩm phán (Cánh Tây Bắc: X: 0.0 to 7.5m)
        {
            'id': 'P2_THAMPHAN_NW', 'name': 'Phòng Thẩm phán',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'door': (5.8, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        # 2. Phòng Thẩm phán (Cánh Đông Bắc: X: 12.5 to 20.0m)
        {
            'id': 'P2_THAMPHAN_NE', 'name': 'Phòng Thẩm phán',
            'x': 12.5, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (16.25, 3.15),
            'door': (13.4, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 10.5
        },

        # --- DÃY NAM (SOUTH WING: Y: -4.9 to -0.9m) ---
        # 3. Phòng Thẩm phán (Cánh Tây Nam ngoài: X: 0.0 to 3.75m)
        {
            'id': 'P2_THAMPHAN_SW1', 'name': 'Phòng Thẩm phán',
            'x': 0.0, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (1.875, -2.9),
            'door': (2.4, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        # 4. Phòng Phó Chánh án (Cánh Tây Nam trong: X: 3.75 to 7.5m)
        {
            'id': 'P2_PHOCHANHAN', 'name': 'Phòng Phó Chánh án',
            'x': 3.75, 'y': -4.9, 'w': 3.75, 'h': 4.0,
            'text_center': (5.625, -2.9),
            'door': (4.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        # 5. Phòng Chánh án (Trung tâm phía Nam, thay thế Sảnh Tầng 1: X: 7.5 to 12.5m)
        {
            'id': 'P2_CHANHAN', 'name': 'Phòng Chánh án',
            'x': 7.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (10.0, -2.9),
            'door': (11.0, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        # 6. Phòng thẩm phán (Cánh Đông Nam: X: 12.5 to 20.0m)
        {
            'id': 'P2_THAMPHAN_SE', 'name': 'Phòng thẩm phán',
            'x': 12.5, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (16.25, -2.9),
            'door': (13.5, -0.9, 0.8, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], 
                                 facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE GRAPHIC (UPPER FLOOR - PURE WHITE BACKGROUND, NO EXTERIOR STEPS)
    # ---------------------------------------------------------
    # Central Staircase inside North Hall (Pure White background per Floor 2 Spec)
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, 
                                 facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    # Two flights with central well
    gap = 0.35
    flight_w = (stair_w - gap) / 2.0
    left_x1, left_x2 = stair_x, stair_x + flight_w
    right_x1, right_x2 = stair_x + flight_w + gap, stair_x + stair_w

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([left_x1, left_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
        ax.plot([right_x1, right_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Vertical dividing line down center of left & right flight
    mid_left = left_x1 + flight_w / 2.0
    mid_right = right_x1 + flight_w / 2.0
    ax.plot([mid_left, mid_left], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([mid_right, mid_right], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Staircase label
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.25, 'Cầu thang', 
            color=COLOR_TEXT_MAIN, fontsize=9.5, ha='center', va='top', zorder=5)

    # Labels for Corridor
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (CLOSED EXTERIOR ENCLOSURE FOR UPPER FLOORS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Wall (Continuous enclosing corridor West end)
    draw_wall(-W, -4.9 - W, W, 10.3 + 2 * W)

    # Rightmost Vertical Exterior Wall (Continuous enclosing corridor East end)
    draw_wall(20.0, -4.9 - W, W, 10.3 + 2 * W)

    # North Top Wall (Continuous across entire North facade)
    draw_wall(-W, 5.4, 20.0 + 2 * W, W)

    # South Bottom Wall (Continuous across entire South facade)
    draw_wall(-W, -4.9 - W, 20.0 + 2 * W, W)

    # North Corridor Wall Line (Y = 0.9) - with door openings & stair hall entrance
    draw_wall(0.0, 0.9 - P/2, 5.8, P)
    draw_wall(6.6, 0.9 - P/2, 0.9, P)
    draw_wall(12.5, 0.9 - P/2, 0.9, P)
    draw_wall(14.2, 0.9 - P/2, 5.8, P)

    # South Corridor Wall Line (Y = -0.9) - with door openings
    draw_wall(0.0, -0.9 - P/2, 2.4, P)
    draw_wall(3.2, -0.9 - P/2, 0.55, P)
    draw_wall(3.75, -0.9 - P/2, 0.75, P)
    draw_wall(5.3, -0.9 - P/2, 2.2, P)
    draw_wall(7.5, -0.9 - P/2, 3.5, P)
    draw_wall(11.8, -0.9 - P/2, 0.7, P)
    draw_wall(12.5, -0.9 - P/2, 1.0, P)
    draw_wall(14.3, -0.9 - P/2, 5.7, P)

    # Internal Vertical Partitions
    draw_wall(7.5 - P/2, 0.9, P, 4.5)     # North West Room & Stair Hall
    draw_wall(12.5 - P/2, 0.9, P, 4.5)    # North Stair Hall & East Room

    draw_wall(3.75 - P/2, -4.9, P, 4.0)   # South Room 3 & Room 4
    draw_wall(7.5 - P/2, -4.9, P, 4.0)    # South Room 4 & Phòng Chánh án
    draw_wall(12.5 - P/2, -4.9, P, 4.0)   # South Phòng Chánh án & Room 6

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

    # Top Windows (North Facade: Y = 5.4)
    draw_window(1.2, 5.4, 2.0, W, is_horizontal=True)    # Phòng Thẩm phán (NW)
    draw_window(4.3, 5.4, 2.0, W, is_horizontal=True)    # Phòng Thẩm phán (NW)
    draw_window(8.75, 5.4, 2.5, W, is_horizontal=True)   # Cửa sổ sảnh thang bộ
    draw_window(13.7, 5.4, 2.0, W, is_horizontal=True)   # Phòng Thẩm phán (NE)
    draw_window(16.8, 5.4, 2.0, W, is_horizontal=True)   # Phòng Thẩm phán (NE)

    # Bottom Windows (South Facade: Y = -4.9 - W)
    draw_window(1.0, -4.9 - W, 1.6, W, is_horizontal=True)    # Phòng Thẩm phán (SW ngoài)
    draw_window(4.8, -4.9 - W, 1.6, W, is_horizontal=True)    # Phòng Phó Chánh án
    draw_window(8.75, -4.9 - W, 2.5, W, is_horizontal=True)   # Phòng Chánh án (Trung tâm)
    draw_window(13.7, -4.9 - W, 2.0, W, is_horizontal=True)   # Phòng thẩm phán (SE)
    draw_window(16.8, -4.9 - W, 2.0, W, is_horizontal=True)   # Phòng thẩm phán (SE)

    # Corridor End Windows (West & East Facades on Floor 2)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)        # Đầu hồi Tây
    draw_window(20.0, -0.6, W, 1.2, is_horizontal=False)      # Đầu hồi Đông

    # Side Room Windows
    draw_window(-W, 2.2, W, 1.8, is_horizontal=False)         # Phòng Thẩm phán (NW)
    draw_window(-W, -3.8, W, 1.8, is_horizontal=False)        # Phòng Thẩm phán (SW)
    draw_window(20.0, 2.2, W, 1.8, is_horizontal=False)       # Phòng Thẩm phán (NE)
    draw_window(20.0, -3.8, W, 1.8, is_horizontal=False)      # Phòng thẩm phán (SE)

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
        if r['door']:
            dx, dy, dsize, dmode = r['door']
            draw_door(dx, dy, dsize, dmode)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS (FULL ROOM NAME FROM SURVEY)
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, 
                fontsize=r['font_size'], fontweight='bold', ha='center', va='center', zorder=15)

    # Limits & Bounds
    ax.set_xlim(-2.0, 22.0)
    ax.set_ylim(-8.5, 7.8)

    # Save output PNG
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Generated Floor 2 floorplan PNG at {out_img_path}")
    plt.close(fig)

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaoBang\CaoBang3\Tang2"
    create_floorplan_tang2(target_dir)
