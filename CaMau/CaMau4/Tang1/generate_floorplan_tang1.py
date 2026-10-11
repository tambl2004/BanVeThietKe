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

def create_floorplan_tang1(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_1.png')

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(18, 11), dpi=300)
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
    COLOR_STAIR_FILL = '#eef4f7'    # Stair fill matching lobby color for floor 1

    WALL_THICKNESS = 0.20  # 200mm exterior wall
    PART_THICKNESS = 0.10  # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line)
    fig.text(0.04, 0.94, 'MẶT BẰNG TẦNG 1  —  TÒA ÁN NHÂN DÂN KHU VỰC 4 - CÀ MAU', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.04, 0.96], [0.915, 0.915], transform=fig.transFigure, color='#e2e8f0', linewidth=1.0)
    fig.lines.append(header_line)

    # Legend Box at Bottom Center / Left
    lg_x, lg_y = 0.5, -7.5
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 0.8, 0.3, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.1, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 5.5, lg_y + 0.1), 0.8, 0.12, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 6.6, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 10.5, lg_x + 11.3], [lg_y + 0.2, lg_y + 0.2], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 10.5, lg_x + 11.3], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 11.6, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 15.5, lg_x + 15.5], [lg_y + 0.02, lg_y + 0.28], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 15.5, lg_y + 0.02), 0.52, 0.52, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 16.6, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (OPEN EXITS)
    # ---------------------------------------------------------
    # Horizontal Corridor (X: 0.0 to 20.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), 20.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Front Main Lobby Space (X: 7.5 to 12.5, Y: -4.9 to -0.9)
    ax.add_patch(patches.Rectangle((7.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Rear Stair & Passage Hall Space (X: 7.5 to 12.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((7.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (ALL 4 ROOMS MATCHING PROMPT)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # --- North Wing (Y > 0.9m) ---
        {
            'id': 'P_HOP', 'name': 'Phòng họp',
            'x': 0.0, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (3.75, 3.15),
            'door': (6.1, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.0
        },
        {
            'id': 'P_THAMPHAN', 'name': 'Phòng Thẩm phán',
            'x': 12.5, 'y': 0.9, 'w': 7.5, 'h': 4.5,
            'text_center': (16.25, 3.15),
            'door': (13.5, 0.9, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.0
        },

        # --- South Wing (Y < -0.9m) ---
        {
            'id': 'P_TIEPDAN', 'name': 'Phòng tiếp công dân',
            'x': 0.0, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (3.75, -2.9),
            'door': (6.1, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
        {
            'id': 'P_KETOAN', 'name': 'Phòng kế Toán',
            'x': 12.5, 'y': -4.9, 'w': 7.5, 'h': 4.0,
            'text_center': (16.25, -2.9),
            'door': (13.5, -0.9, 0.9, 'S_IN_RIGHT'),
            'font_size': 11.0
        },
    ]

    # Draw Room Background Fills (Pure white `#ffffff`)
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASE & ENTRANCE/EXIT STEPS (FLOOR 1 SPECIFIC)
    # ---------------------------------------------------------
    # Central Staircase inside North Hall (Background matches sảnh fill COLOR_STAIR_FILL per Tang 1 Spec)
    stair_x, stair_y, stair_w, stair_h = 8.7, 1.4, 2.6, 2.6
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Vertical line down center starting from step 2 down to bottom
    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Staircase label underneath box
    ax.text(stair_x + stair_w / 2.0, stair_y - 0.25, 'Cầu thang', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='top', zorder=5)

    # 1. Front Main Entrance Steps at Bottom (South: Y = -4.9 to -5.7)
    for sy in [-4.9, -5.06, -5.22, -5.38, -5.54, -5.70]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # 2. Rear Exit Steps at Top (North: Y = 5.4 to 6.2)
    for sy in [5.4, 5.56, 5.72, 5.88, 6.04, 6.20]:
        ax.plot([7.5, 12.5], [sy, sy], color=COLOR_WALL, linewidth=0.9, zorder=4)

    # Outdoor Side Steps at Corridor Ends (East & West Exits)
    for i in range(5):
        dx = -0.22 * (i + 1)
        dy = 0.9 + i * 0.08
        ax.plot([dx, 0.0], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, 0.0], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    for i in range(5):
        dx = 20.0 + 0.22 * (i + 1)
        dy = 0.9 + i * 0.08
        ax.plot([20.0, dx], [dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([20.0, dx], [-dy, -dy], color=COLOR_WALL, linewidth=0.8, zorder=2)
        ax.plot([dx, dx], [-dy, dy], color=COLOR_WALL, linewidth=0.8, zorder=2)

    # Labels for Lobby and Corridor
    ax.text(10.0, -2.9, 'SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(3.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW WALLS (UNBLOCKED CORRIDOR EXITS & ENTRANCE CHEEK WALLS)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # Leftmost Vertical Exterior Walls (SPLIT TO LEAVE CORRIDOR Y: -0.9 TO 0.9 UNBLOCKED!)
    draw_wall(-W, -4.9 - W, W, 4.0 + W)  # Bottom-left segment (Y: -4.9-W to -0.9)
    draw_wall(-W, 0.9, W, 4.5 + W)       # Top-left segment (Y: 0.9 to 5.4+W)

    # Rightmost Vertical Exterior Walls (SPLIT TO LEAVE CORRIDOR Y: -0.9 TO 0.9 UNBLOCKED!)
    draw_wall(20.0, -4.9 - W, W, 4.0 + W) # Bottom-right segment (Y: -4.9-W to -0.9)
    draw_wall(20.0, 0.9, W, 4.5 + W)      # Top-right segment (Y: 0.9 to 5.4+W)

    # North Top Wall (with opening for rear exit at X: 7.5 to 12.5)
    draw_wall(-W, 5.4, 7.5 + W + P/2, W)
    draw_wall(12.5 - P/2, 5.4, 7.5 + W + P/2, W)

    # South Bottom Wall (with opening for main front entrance at X: 7.5 to 12.5)
    draw_wall(-W, -4.9 - W, 7.5 + W + P/2, W)
    draw_wall(12.5 - P/2, -4.9 - W, 7.5 + W + P/2, W)

    # STRUCTURAL WALL CHEEKS & HOOKS
    # South Front Entrance Side Wall Cheeks (Y: -4.9 down to -5.7)
    draw_wall(7.5 - P/2, -5.7, P, 0.8)
    draw_wall(12.5 - P/2, -5.7, P, 0.8)

    # North Rear Exit Side Wall Cheeks (Y: 5.4 up to 6.2) & Top Inward Hooks
    draw_wall(7.5 - P/2, 5.4, P, 0.8)
    draw_wall(12.5 - P/2, 5.4, P, 0.8)
    # Top Inward Hooks at Y = 6.2 (0.5m)
    draw_wall(7.5 - P/2, 6.2 - P, 0.5, P)
    draw_wall(12.5 + P/2 - 0.5, 6.2 - P, 0.5, P)

    # Internal Vertical Partitions
    draw_wall(7.5 - P/2, 0.9, P, 4.5)   # North West room & Stair hall
    draw_wall(12.5 - P/2, 0.9, P, 4.5)  # North Stair hall & East room

    draw_wall(7.5 - P/2, -4.9, P, 4.0)  # South West room & Front Lobby
    draw_wall(12.5 - P/2, -4.9, P, 4.0) # South Front Lobby & East room

    # North Corridor Wall Line (Y = 0.9)
    # Room Hop (door at 5.2 to 6.1)
    draw_wall(0.0, 0.9 - P/2, 5.2, P)
    draw_wall(6.1, 0.9 - P/2, 1.4, P)
    # Stair Hall (X: 7.5 to 12.5) is open
    # Room Tham Phan (door at 13.5 to 14.4)
    draw_wall(12.5, 0.9 - P/2, 1.0, P)
    draw_wall(14.4, 0.9 - P/2, 5.6, P)

    # South Corridor Wall Line (Y = -0.9)
    # Room Tiep Dan (door at 5.2 to 6.1)
    draw_wall(0.0, -0.9 - P/2, 5.2, P)
    draw_wall(6.1, -0.9 - P/2, 1.4, P)
    # Front Lobby (X: 7.5 to 12.5) is open
    # Room Ke Toan (door at 13.5 to 14.4)
    draw_wall(12.5, -0.9 - P/2, 1.0, P)
    draw_wall(14.4, -0.9 - P/2, 5.6, P)

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

    # North Windows (Facade Bắc)
    draw_window(1.5, 5.4, 2.0, W, is_horizontal=True)    # Phòng họp cửa 1
    draw_window(4.5, 5.4, 2.0, W, is_horizontal=True)    # Phòng họp cửa 2
    draw_window(13.5, 5.4, 2.0, W, is_horizontal=True)   # Phòng Thẩm phán cửa 1
    draw_window(16.5, 5.4, 2.0, W, is_horizontal=True)   # Phòng Thẩm phán cửa 2

    # South Windows (Facade Nam)
    draw_window(1.5, -4.9 - W, 2.0, W, is_horizontal=True)  # Phòng tiếp công dân cửa 1
    draw_window(4.5, -4.9 - W, 2.0, W, is_horizontal=True)  # Phòng tiếp công dân cửa 2
    draw_window(13.5, -4.9 - W, 2.0, W, is_horizontal=True) # Phòng kế Toán cửa 1
    draw_window(16.5, -4.9 - W, 2.0, W, is_horizontal=True) # Phòng kế Toán cửa 2

    # West Gable Windows (Facade Tây)
    draw_window(-W, 2.0, W, 2.0, is_horizontal=False)   # Phòng họp đầu hồi Tây
    draw_window(-W, -3.8, W, 2.0, is_horizontal=False)  # Phòng tiếp công dân đầu hồi Tây

    # East Gable Windows (Facade Đông)
    draw_window(20.0, 2.0, W, 2.0, is_horizontal=False)  # Phòng Thẩm phán đầu hồi Đông
    draw_window(20.0, -3.8, W, 2.0, is_horizontal=False) # Phòng kế Toán đầu hồi Đông

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door(x, y, size, mode):
        if mode == 'N_IN_RIGHT':
            # Hinge at x, opens upward into North room
            ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'N_IN_LEFT':
            ax.plot([x + size, x + size], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x + size, y), size*2, size*2, angle=0, theta1=90, theta2=180,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_RIGHT':
            # Hinge at x, opens downward into South room
            ax.plot([x, x], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=270, theta2=360,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
            ax.add_patch(arc)
        elif mode == 'S_IN_LEFT':
            ax.plot([x + size, x + size], [y, y - size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((x + size, y), size*2, size*2, angle=0, theta1=180, theta2=270,
                              color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.1, zorder=14)
            ax.add_patch(arc)

    # Doors for rooms
    draw_door(5.2, 0.9, 0.9, 'N_IN_RIGHT')   # Phòng họp
    draw_door(13.5, 0.9, 0.9, 'N_IN_RIGHT')  # Phòng Thẩm phán
    draw_door(5.2, -0.9, 0.9, 'S_IN_RIGHT')  # Phòng tiếp công dân
    draw_door(13.5, -0.9, 0.9, 'S_IN_RIGHT') # Phòng kế Toán

    # ---------------------------------------------------------
    # 9. ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        cx, cy = r['text_center']
        font_sz = r.get('font_size', 11.0)
        ax.text(cx, cy, r['name'], color=COLOR_TEXT_MAIN, fontsize=font_sz, fontweight='bold', ha='center', va='center', zorder=15)

    # ---------------------------------------------------------
    # 10. AXIS LIMITS & EXPORT
    # ---------------------------------------------------------
    ax.set_xlim(-2.5, 22.5)
    ax.set_ylim(-8.5, 8.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Bản vẽ đã được xuất thành công tại: {out_img_path}")

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaMau\CaMau4\Tang1"
    create_floorplan_tang1(target_dir)
