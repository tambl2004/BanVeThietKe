import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def draw_floorplan():
    fig, ax = plt.subplots(figsize=(24, 14), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')

    # Color Palette
    COLOR_WALL = '#1e293b'          # Dark slate wall color
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Pastel blue-grey for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'      # White for rooms
    COLOR_DOOR_SWING = '#334155'     # Slate blue for door arc
    COLOR_TEXT_MAIN = '#0f172a'
    COLOR_TEXT_MUTED = '#64748b'
    COLOR_WINDOW = '#64748b'

    WALL_THICKNESS = 0.25

    def draw_wall_rect(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, linewidth=0, facecolor=COLOR_WALL, zorder=5)
        ax.add_patch(rect)

    def draw_room_fill(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, linewidth=0, facecolor=COLOR_ROOM_FILL, zorder=1)
        ax.add_patch(rect)

    def draw_corridor_fill(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, linewidth=0, facecolor=COLOR_FILL_CORRIDOR, zorder=1)
        ax.add_patch(rect)

    def draw_door(x, y, width, style='swing_in_left'):
        door_line_width = 1.5
        if style == 'swing_in_left':
            ax.plot([x, x], [y, y + width], color=COLOR_DOOR_SWING, lw=door_line_width, zorder=6)
            arc = patches.Arc((x, y), width*2, width*2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, lw=door_line_width, ls='--', zorder=6)
            ax.add_patch(arc)
        elif style == 'swing_in_right':
            ax.plot([x + width, x + width], [y, y + width], color=COLOR_DOOR_SWING, lw=door_line_width, zorder=6)
            arc = patches.Arc((x + width, y), width*2, width*2, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, lw=door_line_width, ls='--', zorder=6)
            ax.add_patch(arc)
        elif style == 'swing_down_left':
            ax.plot([x, x], [y, y - width], color=COLOR_DOOR_SWING, lw=door_line_width, zorder=6)
            arc = patches.Arc((x, y), width*2, width*2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, lw=door_line_width, ls='--', zorder=6)
            ax.add_patch(arc)
        elif style == 'swing_down_right':
            ax.plot([x + width, x + width], [y, y - width], color=COLOR_DOOR_SWING, lw=door_line_width, zorder=6)
            arc = patches.Arc((x + width, y), width*2, width*2, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, lw=door_line_width, ls='--', zorder=6)
            ax.add_patch(arc)

    def draw_window(x, y, length, orientation='horizontal'):
        if orientation == 'horizontal':
            ax.plot([x, x + length], [y + WALL_THICKNESS/2, y + WALL_THICKNESS/2], color='#ffffff', lw=4, zorder=7)
            ax.plot([x, x + length], [y + WALL_THICKNESS/2 + 0.08, y + WALL_THICKNESS/2 + 0.08], color=COLOR_WINDOW, lw=1.2, zorder=8)
            ax.plot([x, x + length], [y + WALL_THICKNESS/2 - 0.08, y + WALL_THICKNESS/2 - 0.08], color=COLOR_WINDOW, lw=1.2, zorder=8)
        else:
            ax.plot([x + WALL_THICKNESS/2, x + WALL_THICKNESS/2], [y, y + length], color='#ffffff', lw=4, zorder=7)
            ax.plot([x + WALL_THICKNESS/2 + 0.08, x + WALL_THICKNESS/2 + 0.08], [y, y + length], color=COLOR_WINDOW, lw=1.2, zorder=8)
            ax.plot([x + WALL_THICKNESS/2 - 0.08, x + WALL_THICKNESS/2 - 0.08], [y, y + length], color=COLOR_WINDOW, lw=1.2, zorder=8)

    # ==================== GEOMETRY DEFINITION (PROPORTIONAL 3.0M CORRIDORS) ====================
    # South Rooms: Y=0..4
    # Main Corridor: Y=4..7 (3.0m wide)
    # Middle Rooms & Stair: Y=7..11
    # Rear Corridor: Y=11..14 (3.0m wide)
    # North Courtrooms: Y=14..24 (PX2, PX3: Y=14..21, PX1: Y=14..24)

    # 1. CORRIDOR & LOBBY FILLS
    draw_corridor_fill(20, -3.5, 8, 3.5)   # Sảnh đón
    draw_corridor_fill(20, 0, 8, 4)        # Sảnh trệt
    draw_corridor_fill(0, 4, 48, 3.0)      # Hành lang chính (3.0m wide)
    draw_corridor_fill(20, 7, 8, 4)        # Ô cầu thang & sảnh giữa
    draw_corridor_fill(0, 11, 48, 3.0)     # Hành lang nối xét xử (3.0m wide)

    # 2. ROOM FILLS
    # South Rooms Row (Y: 0..4)
    draw_room_fill(0, 0, 10, 4)
    draw_room_fill(10, 0, 10, 4)
    draw_room_fill(28, 0, 10, 4)
    draw_room_fill(38, 0, 10, 4)

    # Middle Rooms Row (Y: 7..11)
    draw_room_fill(0, 7, 6.66, 4)
    draw_room_fill(6.66, 7, 6.67, 4)
    draw_room_fill(13.33, 7, 6.67, 4)
    draw_room_fill(28, 7, 6.66, 4)
    draw_room_fill(34.66, 7, 6.67, 4)
    draw_room_fill(41.33, 7, 6.67, 4)

    # North Courtrooms Row (Y: 14..24)
    draw_room_fill(0, 14, 14, 7)           # PX2
    draw_room_fill(14, 14, 20, 10)         # PX1
    draw_room_fill(34, 14, 14, 7)          # PX3

    # 3. WALL SEGMENTS (CLEAN JOINTS, ZERO EXTRA STUBS, EXACT FIT CORNERS)

    # --- SOUTH FACADE WALLS (Y=0) ---
    draw_wall_rect(0 - WALL_THICKNESS, 0, 3.5 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(6.5, 0, 7.0, WALL_THICKNESS)
    draw_wall_rect(16.5, 0, 3.5, WALL_THICKNESS)
    draw_wall_rect(28, 0, 3.5, WALL_THICKNESS)
    draw_wall_rect(34.5, 0, 7.0, WALL_THICKNESS)
    draw_wall_rect(44.5, 0, 3.5 + WALL_THICKNESS, WALL_THICKNESS)

    # --- SẢNH ĐÓN PORCH WALLS (X=20, 28, Y=-3.5..0) ---
    draw_wall_rect(20 - WALL_THICKNESS, -3.5, WALL_THICKNESS, 3.5)
    draw_wall_rect(28, -3.5, WALL_THICKNESS, 3.5)

    # --- VERTICAL WALLS SEPARATING SOUTH ROOMS AND LOBBY (X=20 & X=28, Y=0..4) --- [NO PROTRUDING STUBS AT Y=0]
    draw_wall_rect(20 - WALL_THICKNESS, 0, WALL_THICKNESS, 4.0)
    draw_wall_rect(28, 0, WALL_THICKNESS, 4.0)

    # --- WEST OUTER WALL (X=0) --- Gaps for Corridor 1 (Y=4..7) and Corridor 2 (Y=11..14)
    draw_wall_rect(0 - WALL_THICKNESS, 0, WALL_THICKNESS, 4.0 + WALL_THICKNESS)          # Y=0..4.0
    draw_wall_rect(0 - WALL_THICKNESS, 7.0, WALL_THICKNESS, 4.0 + WALL_THICKNESS)        # Y=7.0..11.0
    draw_wall_rect(0 - WALL_THICKNESS, 14.0, WALL_THICKNESS, 7.0 + WALL_THICKNESS)       # Y=14.0..21.0

    # --- EAST OUTER WALL (X=48) --- Gaps for Corridor 1 (Y=4..7) and Corridor 2 (Y=11..14)
    draw_wall_rect(48, 0, WALL_THICKNESS, 4.0 + WALL_THICKNESS)                          # Y=0..4.0
    draw_wall_rect(48, 7.0, WALL_THICKNESS, 4.0 + WALL_THICKNESS)                        # Y=7.0..11.0
    draw_wall_rect(48, 14.0, WALL_THICKNESS, 7.0 + WALL_THICKNESS)                       # Y=14.0..21.0

    # --- COURTROOM BOUNDARY WALLS --- [PERFECT JOINTS WITHOUT EXTRA PROTRUDING STUBS]

    # Shared vertical wall PX2 / PX1 at X=14 (runs Y=14 to 24)
    draw_wall_rect(14 - WALL_THICKNESS, 14, WALL_THICKNESS, 10.0 + WALL_THICKNESS)

    # Shared vertical wall PX3 / PX1 at X=34 (runs Y=14 to 24)
    draw_wall_rect(34, 14, WALL_THICKNESS, 10.0 + WALL_THICKNESS)

    # North wall PX2 (Y=21, X=0..14) - Stops EXACTLY at X=14 [FIXED STUB ISSUE]
    draw_wall_rect(0 - WALL_THICKNESS, 21, 4.0 + WALL_THICKNESS, WALL_THICKNESS)          # Window at X=4..10
    draw_wall_rect(10, 21, 4.0, WALL_THICKNESS)                                          # Ends flush at X=14!

    # North wall PX3 (Y=21, X=34..48) - Starts EXACTLY at X=34 [FIXED STUB ISSUE]
    draw_wall_rect(34, 21, 4.0, WALL_THICKNESS)                                          # Starts flush at X=34!
    draw_wall_rect(44, 21, 4.0 + WALL_THICKNESS, WALL_THICKNESS)                          # Window at X=38..44

    # North wall PX1 (Y=24, X=14..34)
    draw_wall_rect(14 - WALL_THICKNESS, 24, 6.0 + WALL_THICKNESS, WALL_THICKNESS)        # Window at X=20..28
    draw_wall_rect(28, 24, 6.0 + WALL_THICKNESS, WALL_THICKNESS)

    # --- INTERIOR PARTITION WALLS ---

    # Horizontal Wall Y=4.0 (South Rooms / Corridor 1 boundary)
    draw_wall_rect(0 - WALL_THICKNESS, 4, 1.5 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(2.7, 4, 7.3, WALL_THICKNESS)
    draw_wall_rect(10, 4, 1.5, WALL_THICKNESS)
    draw_wall_rect(12.7, 4, 7.3, WALL_THICKNESS)
    draw_wall_rect(28, 4, 7.3, WALL_THICKNESS)
    draw_wall_rect(36.5, 4, 1.5, WALL_THICKNESS)
    draw_wall_rect(38, 4, 7.3, WALL_THICKNESS)
    draw_wall_rect(46.5, 4, 1.5 + WALL_THICKNESS, WALL_THICKNESS)

    # Vertical Partitions South Row (Y: 0..4)
    draw_wall_rect(10, 0, WALL_THICKNESS, 4.0)
    draw_wall_rect(38, 0, WALL_THICKNESS, 4.0)

    # Horizontal Wall Y=7.0 (Corridor 1 / Middle Rooms boundary)
    draw_wall_rect(0 - WALL_THICKNESS, 7, 1.5 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(2.7, 7, 3.96, WALL_THICKNESS)
    draw_wall_rect(6.66, 7, 1.34, WALL_THICKNESS)
    draw_wall_rect(9.2, 7, 4.13, WALL_THICKNESS)
    draw_wall_rect(13.33, 7, 1.17, WALL_THICKNESS)
    draw_wall_rect(15.7, 7, 4.3, WALL_THICKNESS)
    draw_wall_rect(28, 7, 4.3, WALL_THICKNESS)
    draw_wall_rect(33.5, 7, 1.16, WALL_THICKNESS)
    draw_wall_rect(34.66, 7, 4.34, WALL_THICKNESS)
    draw_wall_rect(40.2, 7, 1.13, WALL_THICKNESS)
    draw_wall_rect(41.33, 7, 4.17, WALL_THICKNESS)
    draw_wall_rect(46.7, 7, 1.3 + WALL_THICKNESS, WALL_THICKNESS)

    # Vertical Partitions Middle Row (Y: 7..11)
    draw_wall_rect(6.66, 7, WALL_THICKNESS, 4.0)
    draw_wall_rect(13.33, 7, WALL_THICKNESS, 4.0)
    draw_wall_rect(20 - WALL_THICKNESS, 7, WALL_THICKNESS, 4.0)
    draw_wall_rect(28, 7, WALL_THICKNESS, 4.0)
    draw_wall_rect(34.66, 7, WALL_THICKNESS, 4.0)
    draw_wall_rect(41.33, 7, WALL_THICKNESS, 4.0)

    # Horizontal Wall Y=11.0 (Middle Rooms / Corridor 2 boundary)
    draw_wall_rect(0 - WALL_THICKNESS, 11, 20.0 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(28, 11, 20.0 + WALL_THICKNESS, WALL_THICKNESS)

    # Horizontal Wall Y=14.0 (Corridor 2 / North Courtrooms boundary)
    draw_wall_rect(0 - WALL_THICKNESS, 14, 6.0 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(7.4, 14, 6.6, WALL_THICKNESS)
    draw_wall_rect(14 - WALL_THICKNESS, 14, 8.6 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(25.4, 14, 8.6 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(34 - WALL_THICKNESS, 14, 6.0 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(41.4, 14, 6.6 + WALL_THICKNESS, WALL_THICKNESS)

    # 4. DOORS PLACEMENT
    DOOR_W = 1.2
    # South Rooms Doors
    draw_door(1.5, 4, DOOR_W, style='swing_down_right')
    draw_door(11.5, 4, DOOR_W, style='swing_down_right')
    draw_door(35.3, 4, DOOR_W, style='swing_down_left')
    draw_door(45.3, 4, DOOR_W, style='swing_down_left')

    # Middle Rooms Doors
    draw_door(1.5, 7, DOOR_W, style='swing_in_right')
    draw_door(8.0, 7, DOOR_W, style='swing_in_right')
    draw_door(14.5, 7, DOOR_W, style='swing_in_right')
    draw_door(32.3, 7, DOOR_W, style='swing_in_left')
    draw_door(39.0, 7, DOOR_W, style='swing_in_left')
    draw_door(45.5, 7, DOOR_W, style='swing_in_left')

    # Courtrooms Doors
    draw_door(6.0, 14, 1.4, style='swing_in_right')
    # Double door for PX1
    draw_door(22.6, 14, 1.4, style='swing_in_left')
    draw_door(24.0, 14, 1.4, style='swing_in_right')
    draw_door(40.0, 14, 1.4, style='swing_in_left')

    # 5. WINDOWS DRAWING
    draw_window(3.5, 0, 3.0, 'horizontal')
    draw_window(13.5, 0, 3.0, 'horizontal')
    draw_window(31.5, 0, 3.0, 'horizontal')
    draw_window(41.5, 0, 3.0, 'horizontal')

    draw_window(4.0, 21, 6.0, 'horizontal')
    draw_window(20.0, 24, 8.0, 'horizontal')
    draw_window(38.0, 21, 6.0, 'horizontal')

    # 6. STAIRCASE GRAPHIC
    stair_x1, stair_x2 = 21.5, 26.5
    stair_y1, stair_y2 = 7.5, 10.5
    stair_w = stair_x2 - stair_x1
    stair_h = stair_y2 - stair_y1

    rect_stair = patches.Rectangle((stair_x1, stair_y1), stair_w, stair_h, lw=1.2, edgecolor='#334155', facecolor='#eef4f7', zorder=3)
    ax.add_patch(rect_stair)

    steps = 10
    step_dy = stair_h / steps
    for i in range(1, steps):
        sy = stair_y1 + i * step_dy
        ax.plot([stair_x1, stair_x2], [sy, sy], color='#334155', lw=0.9, zorder=4)
    ax.plot([stair_x1 + stair_w/2, stair_x1 + stair_w/2], [stair_y1, stair_y1 + (steps-1)*step_dy], color='#334155', lw=1.0, zorder=4)

    # 7. CORRIDOR EXIT STEPS (FLUSH WITH 3.0M CORRIDOR OPENINGS) [FIXED MISALIGNMENT ISSUE]

    # South Main Entrance Steps
    for i in range(5):
        sy = -3.5 - i * 0.25
        ax.plot([20, 28], [sy, sy], color='#334155', lw=0.9, zorder=4)

    # West Exit 1 (Corridor 1: Y=4.0 to 7.0)
    for i in range(4):
        sx = -WALL_THICKNESS - (i+1) * 0.25
        ax.plot([sx, sx], [4.0, 7.0], color='#334155', lw=0.9, zorder=4)
    ax.plot([-WALL_THICKNESS - 1.0, -WALL_THICKNESS], [4.0, 4.0], color='#334155', lw=0.9, zorder=4)
    ax.plot([-WALL_THICKNESS - 1.0, -WALL_THICKNESS], [7.0, 7.0], color='#334155', lw=0.9, zorder=4)

    # West Exit 2 (Corridor 2: Y=11.0 to 14.0)
    for i in range(4):
        sx = -WALL_THICKNESS - (i+1) * 0.25
        ax.plot([sx, sx], [11.0, 14.0], color='#334155', lw=0.9, zorder=4)
    ax.plot([-WALL_THICKNESS - 1.0, -WALL_THICKNESS], [11.0, 11.0], color='#334155', lw=0.9, zorder=4)
    ax.plot([-WALL_THICKNESS - 1.0, -WALL_THICKNESS], [14.0, 14.0], color='#334155', lw=0.9, zorder=4)

    # East Exit 1 (Corridor 1: Y=4.0 to 7.0)
    for i in range(4):
        sx = 48 + WALL_THICKNESS + (i+1) * 0.25
        ax.plot([sx, sx], [4.0, 7.0], color='#334155', lw=0.9, zorder=4)
    ax.plot([48 + WALL_THICKNESS, 48 + WALL_THICKNESS + 1.0], [4.0, 4.0], color='#334155', lw=0.9, zorder=4)
    ax.plot([48 + WALL_THICKNESS, 48 + WALL_THICKNESS + 1.0], [7.0, 7.0], color='#334155', lw=0.9, zorder=4)

    # East Exit 2 (Corridor 2: Y=11.0 to 14.0)
    for i in range(4):
        sx = 48 + WALL_THICKNESS + (i+1) * 0.25
        ax.plot([sx, sx], [11.0, 14.0], color='#334155', lw=0.9, zorder=4)
    ax.plot([48 + WALL_THICKNESS, 48 + WALL_THICKNESS + 1.0], [11.0, 11.0], color='#334155', lw=0.9, zorder=4)
    ax.plot([48 + WALL_THICKNESS, 48 + WALL_THICKNESS + 1.0], [14.0, 14.0], color='#334155', lw=0.9, zorder=4)


    # 8. TEXT LABELS
    # South Office Rooms
    ax.text(5, 2.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(15, 2.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(33, 2.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(43, 2.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)

    # Middle Office Rooms
    ax.text(3.33, 9.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(10.0, 9.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(16.66, 9.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(31.33, 9.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(38.0, 9.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(44.66, 9.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)

    # Courtrooms
    ax.text(7, 17.5, 'Phòng xử 2', ha='center', va='center', fontsize=12, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(24, 19.0, 'Phòng xử 1', ha='center', va='center', fontsize=14, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(41, 17.5, 'Phòng xử 3', ha='center', va='center', fontsize=12, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)

    # Public Areas
    ax.text(24, -1.8, 'SẢNH', ha='center', va='center', fontsize=11, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(24, 5.5, 'HÀNH LANG CHÍNH', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MUTED, zorder=10)
    ax.text(24, 12.5, 'HÀNH LANG NỐI XÉT XỬ', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MUTED, zorder=10)
    ax.text(24, 7.2, 'Cầu thang', ha='center', va='center', fontsize=8, color=COLOR_TEXT_MUTED, zorder=10)

    # 9. HEADER TITLE
    ax.text(-0.25, 27.5, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân khu vực 13 - An Giang', 
            fontsize=20, fontweight='bold', color=COLOR_TEXT_MAIN, ha='left', va='center', zorder=10)

    # 10. LEGEND AT BOTTOM
    legend_y = -6.5
    ax.add_patch(patches.Rectangle((0, legend_y), 1.8, 0.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=10))
    ax.text(2.2, legend_y + 0.2, 'Hành lang / sảnh', fontsize=9, color=COLOR_TEXT_MUTED, va='center', zorder=10)

    ax.add_patch(patches.Rectangle((10, legend_y + 0.15), 1.8, 0.1, facecolor=COLOR_WALL, edgecolor='none', zorder=10))
    ax.text(12.2, legend_y + 0.2, 'Tường / vách', fontsize=9, color=COLOR_TEXT_MUTED, va='center', zorder=10)

    ax.plot([20, 21.8], [legend_y + 0.2, legend_y + 0.2], color='#ffffff', lw=3, zorder=10)
    ax.plot([20, 21.8], [legend_y + 0.28, legend_y + 0.28], color=COLOR_WINDOW, lw=1.2, zorder=10)
    ax.plot([20, 21.8], [legend_y + 0.12, legend_y + 0.12], color=COLOR_WINDOW, lw=1.2, zorder=10)
    ax.text(22.2, legend_y + 0.2, 'Cửa sổ', fontsize=9, color=COLOR_TEXT_MUTED, va='center', zorder=10)

    # Limits & Margins
    ax.set_xlim(-3, 51)
    ax.set_ylim(-8, 29)

    # Output path
    output_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\AnGiang\AnGiang13\Tang1"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "mat_bang_tang_1.png")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"SUCCESS: Generated Floor 1 floorplan PNG at {output_path}")

if __name__ == "__main__":
    draw_floorplan()
