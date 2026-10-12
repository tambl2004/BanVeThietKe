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

def create_floorplan_tang3(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_3.png')

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
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
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
    fig.text(0.04, 0.945, 'MẶT BẰNG TẦNG 3  —  TÒA ÁN NHÂN DÂN KHU VỰC 3 - CAO BẰNG', 
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
    # 3. CORRIDOR & OPEN LOBBY / FOYER BACKGROUND FILL
    # ---------------------------------------------------------
    # Full floor background fill in soft pastel grey-cyan (#eef4f7)
    # The enclosed offices and stair box will be drawn on top with pure white (#ffffff)
    ax.add_patch(patches.Rectangle((0.0, -4.9), 20.0, 10.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (PHÒNG THƯ KÝ TẠI CÁNH TÂY BẮC, PHÓ CHÁNH ÁN TẠI CÁNH ĐÔNG BẮC, CÙNG KÍCH THƯỚC 7.5x4.5m)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # 1. Phòng Thư ký (Vị trí Sảnh đệm cũ: Dãy Bắc Cánh Tây, X: 0.0 to 7.5m, Y: 0.9 to 5.4m)
        {
            'id': 'P3_THUKY', 'name': 'Phòng Thư ký',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'door': (5.8, 0.9, 0.8, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        # 2. Phòng Phó Chánh án (Vị trí Sảnh đa năng cũ: Dãy Bắc Cánh Đông, X: 12.5 to 20.0m, Y: 0.9 to 5.4m)
        # Kích thước bằng nhau: 7.5m x 4.5m
        {
            'id': 'P3_PHOCHANHAN', 'name': 'Phòng Phó Chánh án',
            'x': 12.5, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (16.25, 3.15),
            'door': (13.4, 0.9, 0.8, 'N_IN_RIGHT'),
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
    # Central Staircase inside North Hall (Pure White background per Floor 3 Spec)
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

    # Labels for Open Corridor & Lobby Spaces ("còn lại ghi chữ hành lang sảnh thôi")
    ax.text(3.75, 0.0, 'HÀNH LANG SẢNH', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG SẢNH', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(10.0, -2.5, 'HÀNH LANG SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (CLOSED EXTERIOR ENCLOSURE & FUNCTIONAL PARTITIONS)
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

    # Stair Hall Side Walls (North Hall: X: 7.5 to 12.5, Y: 0.9 to 5.4)
    draw_wall(7.5 - P/2, 0.9, P, 4.5)
    draw_wall(12.5 - P/2, 0.9, P, 4.5)

    # North Corridor Wall Line (Y = 0.9m) with Doors into the 2 North Offices
    # Along Phòng Thư ký (X: 0.0 to 7.5m) - Door at X = 5.8 to 6.6m
    draw_wall(0.0, 0.9 - P/2, 5.8, P)
    draw_wall(6.6, 0.9 - P/2, 0.9, P)

    # Along Phòng Phó Chánh án (X: 12.5 to 20.0m) - Door at X = 13.4 to 14.2m
    draw_wall(12.5, 0.9 - P/2, 0.9, P)
    draw_wall(14.2, 0.9 - P/2, 5.8, P)

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
    draw_window(1.2, 5.4, 2.0, W, is_horizontal=True)    # Phòng Thư ký (NW)
    draw_window(4.3, 5.4, 2.0, W, is_horizontal=True)    # Phòng Thư ký (NW)
    draw_window(8.75, 5.4, 2.5, W, is_horizontal=True)   # Cửa sổ sau sảnh thang bộ
    draw_window(13.7, 5.4, 2.0, W, is_horizontal=True)   # Phòng Phó Chánh án (NE)
    draw_window(16.8, 5.4, 2.0, W, is_horizontal=True)   # Phòng Phó Chánh án (NE)

    # Bottom Windows (South Facade: Y = -4.9 - W)
    draw_window(1.2, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(4.3, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(8.75, -4.9 - W, 2.5, W, is_horizontal=True)
    draw_window(13.7, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(16.8, -4.9 - W, 2.0, W, is_horizontal=True)

    # Corridor End Windows (West & East Facades on Floor 3)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)        # Đầu hồi Tây
    draw_window(20.0, -0.6, W, 1.2, is_horizontal=False)      # Đầu hồi Đông

    # Side Windows
    draw_window(-W, 2.2, W, 1.8, is_horizontal=False)         # Phòng Thư ký (NW)
    draw_window(-W, -3.8, W, 1.8, is_horizontal=False)        # Sảnh phía Tây Nam
    draw_window(20.0, 2.2, W, 1.8, is_horizontal=False)       # Phòng Phó Chánh án (NE)
    draw_window(20.0, -3.8, W, 1.8, is_horizontal=False)      # Sảnh phía Đông Nam

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode == 'N_IN_RIGHT':
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
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
    print(f"SUCCESS: Generated Floor 3 floorplan PNG at {out_img_path}")
    plt.close(fig)

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaoBang\CaoBang3\Tang3"
    create_floorplan_tang3(target_dir)
