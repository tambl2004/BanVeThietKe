import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def draw_floorplan_tang2():
    fig, ax = plt.subplots(figsize=(24, 14), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')

    # Color Palette for Floor 2
    COLOR_WALL = '#1e293b'              # Dark slate wall color
    COLOR_FILL_CORRIDOR = '#eef4f7'      # Pastel blue-grey for corridor
    COLOR_ROOM_FILL = '#ffffff'          # White for active rooms on Floor 2
    COLOR_STAIR_FILL = '#ffffff'         # White for Staircase on Floor 2
    COLOR_ROOF_FILL = '#f1f5f9'          # Light grey fill for 1-story courtroom roof coverage
    COLOR_ROOF_BORDER = '#94a3b8'        # Muted slate border for roof outlines
    COLOR_DOOR_SWING = '#334155'         # Slate blue for door arc
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

    # ==================== GEOMETRY DEFINITION (FLOOR 2) ====================
    # 1. CORRIDOR FILLS
    draw_corridor_fill(0, 4, 48, 3.0)      # Main Corridor Floor 2

    # 2. ROOM FILLS (10 Rooms Total: 9 'Phòng' + 1 'Phòng họp')
    # South Rooms Row (Y: 0..4) - 5 rooms total
    draw_room_fill(0, 0, 10, 4)            # Phòng 1
    draw_room_fill(10, 0, 10, 4)           # Phòng 2
    draw_room_fill(20, 0, 8, 4)            # Phòng 3
    draw_room_fill(28, 0, 10, 4)           # Phòng 4
    draw_room_fill(38, 0, 10, 4)           # Phòng 5

    # Middle Rooms Row (Y: 7..11) - 4 rooms + 1 Phòng họp + Staircase
    draw_room_fill(0, 7, 6.66, 4)        # Phòng 6
    draw_room_fill(6.66, 7, 6.67, 4)     # Phòng 7
    draw_room_fill(13.33, 7, 6.67, 4)    # Phòng 8
    draw_room_fill(28, 7, 6.66, 4)       # Phòng 9
    draw_room_fill(34.66, 7, 13.34, 4)   # Phòng họp

    # 3. UNIFIED 1-STORY COURTROOM ROOF POLYGON (NO INTERIOR PARTITIONS, SINGLE 'MÁI CHE' LABEL)
    roof_poly_coords = [
        [0, 11], [48, 11], [48, 21], [34, 21], 
        [34, 24], [14, 24], [14, 21], [0, 21]
    ]
    roof_poly = patches.Polygon(roof_poly_coords, linewidth=1.2, edgecolor=COLOR_ROOF_BORDER, 
                                facecolor=COLOR_ROOF_FILL, linestyle='--', zorder=1)
    ax.add_patch(roof_poly)

    # 4. WALL SEGMENTS (FLOOR 2 MAIN BUILDING ENVELOPE)
    # South Facade Walls (Y=0)
    draw_wall_rect(0 - WALL_THICKNESS, 0, 3.5 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(6.5, 0, 7.0, WALL_THICKNESS)
    draw_wall_rect(16.5, 0, 6.0, WALL_THICKNESS)
    draw_wall_rect(25.5, 0, 6.0, WALL_THICKNESS)
    draw_wall_rect(34.5, 0, 7.0, WALL_THICKNESS)
    draw_wall_rect(44.5, 0, 3.5 + WALL_THICKNESS, WALL_THICKNESS)

    # West Outer Wall (X=0, Y=0..11)
    draw_wall_rect(0 - WALL_THICKNESS, 0, WALL_THICKNESS, 4.0 + WALL_THICKNESS)
    draw_wall_rect(0 - WALL_THICKNESS, 4.0, WALL_THICKNESS, 3.0)
    draw_wall_rect(0 - WALL_THICKNESS, 7.0, WALL_THICKNESS, 4.0 + WALL_THICKNESS)

    # East Outer Wall (X=48, Y=0..11)
    draw_wall_rect(48, 0, WALL_THICKNESS, 4.0 + WALL_THICKNESS)
    draw_wall_rect(48, 4.0, WALL_THICKNESS, 3.0)
    draw_wall_rect(48, 7.0, WALL_THICKNESS, 4.0 + WALL_THICKNESS)

    # North Outer Wall of Floor 2 Main Block (Y=11.0)
    draw_wall_rect(0 - WALL_THICKNESS, 11, 48 + 2*WALL_THICKNESS, WALL_THICKNESS)

    # Partition Walls Y=4.0
    draw_wall_rect(0 - WALL_THICKNESS, 4, 1.5 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(2.7, 4, 7.3, WALL_THICKNESS)
    draw_wall_rect(10, 4, 1.5, WALL_THICKNESS)
    draw_wall_rect(12.7, 4, 8.8, WALL_THICKNESS)
    draw_wall_rect(22.7, 4, 12.6, WALL_THICKNESS)
    draw_wall_rect(36.5, 4, 1.5, WALL_THICKNESS)
    draw_wall_rect(38, 4, 7.3, WALL_THICKNESS)
    draw_wall_rect(46.5, 4, 1.5 + WALL_THICKNESS, WALL_THICKNESS)

    # Vertical Partitions South Row
    draw_wall_rect(10, 0, WALL_THICKNESS, 4.0)
    draw_wall_rect(20 - WALL_THICKNESS, 0, WALL_THICKNESS, 4.0)
    draw_wall_rect(28, 0, WALL_THICKNESS, 4.0)
    draw_wall_rect(38, 0, WALL_THICKNESS, 4.0)

    # Partition Walls Y=7.0
    draw_wall_rect(0 - WALL_THICKNESS, 7, 1.5 + WALL_THICKNESS, WALL_THICKNESS)
    draw_wall_rect(2.7, 7, 3.96, WALL_THICKNESS)
    draw_wall_rect(6.66, 7, 1.34, WALL_THICKNESS)
    draw_wall_rect(9.2, 7, 4.13, WALL_THICKNESS)
    draw_wall_rect(13.33, 7, 1.17, WALL_THICKNESS)
    draw_wall_rect(15.7, 7, 4.3, WALL_THICKNESS)
    draw_wall_rect(28, 7, 4.3, WALL_THICKNESS)
    draw_wall_rect(33.5, 7, 2.5, WALL_THICKNESS)
    draw_wall_rect(37.4, 7, 10.6 + WALL_THICKNESS, WALL_THICKNESS)

    # Vertical Partitions Middle Row
    draw_wall_rect(6.66, 7, WALL_THICKNESS, 4.0)
    draw_wall_rect(13.33, 7, WALL_THICKNESS, 4.0)
    draw_wall_rect(20 - WALL_THICKNESS, 7, WALL_THICKNESS, 4.0)
    draw_wall_rect(28, 7, WALL_THICKNESS, 4.0)
    draw_wall_rect(34.66, 7, WALL_THICKNESS, 4.0)

    # 5. DOORS PLACEMENT
    DOOR_W = 1.2
    draw_door(1.5, 4, DOOR_W, style='swing_down_right')
    draw_door(11.5, 4, DOOR_W, style='swing_down_right')
    draw_door(21.5, 4, DOOR_W, style='swing_down_right')
    draw_door(35.3, 4, DOOR_W, style='swing_down_left')
    draw_door(45.3, 4, DOOR_W, style='swing_down_left')

    draw_door(1.5, 7, DOOR_W, style='swing_in_right')
    draw_door(8.0, 7, DOOR_W, style='swing_in_right')
    draw_door(14.5, 7, DOOR_W, style='swing_in_right')
    draw_door(32.3, 7, DOOR_W, style='swing_in_left')
    draw_door(36.0, 7, 1.4, style='swing_in_left')

    # 6. WINDOWS DRAWING
    draw_window(3.5, 0, 3.0, 'horizontal')
    draw_window(13.5, 0, 3.0, 'horizontal')
    draw_window(22.5, 0, 3.0, 'horizontal')
    draw_window(31.5, 0, 3.0, 'horizontal')
    draw_window(41.5, 0, 3.0, 'horizontal')

    draw_window(0 - WALL_THICKNESS, 4.75, 1.5, 'vertical')
    draw_window(48, 4.75, 1.5, 'vertical')

    draw_window(2.0, 11, 3.0, 'horizontal')
    draw_window(8.5, 11, 3.0, 'horizontal')
    draw_window(15.0, 11, 3.0, 'horizontal')
    draw_window(30.0, 11, 3.0, 'horizontal')
    draw_window(39.0, 11, 6.0, 'horizontal')

    # 7. STAIRCASE GRAPHIC
    stair_x1, stair_x2 = 21.5, 26.5
    stair_y1, stair_y2 = 7.5, 10.5
    stair_w = stair_x2 - stair_x1
    stair_h = stair_y2 - stair_y1

    rect_stair = patches.Rectangle((stair_x1, stair_y1), stair_w, stair_h, lw=1.2, edgecolor='#334155', facecolor=COLOR_STAIR_FILL, zorder=3)
    ax.add_patch(rect_stair)

    steps = 10
    step_dy = stair_h / steps
    for i in range(1, steps):
        sy = stair_y1 + i * step_dy
        ax.plot([stair_x1, stair_x2], [sy, sy], color='#334155', lw=0.9, zorder=4)
    ax.plot([stair_x1 + stair_w/2, stair_x1 + stair_w/2], [stair_y1, stair_y1 + (steps-1)*step_dy], color='#334155', lw=1.0, zorder=4)

    # 8. TEXT LABELS
    ax.text(5, 2.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(15, 2.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(24, 2.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(33, 2.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(43, 2.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)

    ax.text(3.33, 9.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(10.0, 9.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(16.66, 9.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(31.33, 9.0, 'Phòng', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)
    ax.text(41.33, 9.0, 'Phòng họp', ha='center', va='center', fontsize=12, fontweight='bold', color=COLOR_TEXT_MAIN, zorder=10)

    ax.text(24, 5.5, 'HÀNH LANG CHÍNH TẦNG 2', ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT_MUTED, zorder=10)
    ax.text(24, 7.2, 'Cầu thang', ha='center', va='center', fontsize=8, color=COLOR_TEXT_MUTED, zorder=10)

    # SINGLE UNIFIED 'MÁI CHE' LABEL IN CENTER OF ROOF POLYGON (PER EXACT USER DIRECTIVE)
    ax.text(24, 17.5, 'MÁI CHE', ha='center', va='center', fontsize=14, fontweight='bold', color=COLOR_TEXT_MUTED, zorder=10)

    # 9. HEADER TITLE
    ax.text(-0.25, 27.5, 'MẶT BẰNG TẦNG 2  —  Tòa án nhân dân khu vực 13 - An Giang', 
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

    ax.add_patch(patches.Rectangle((30, legend_y), 1.8, 0.4, facecolor=COLOR_ROOF_FILL, edgecolor=COLOR_ROOF_BORDER, linestyle='--', zorder=10))
    ax.text(32.2, legend_y + 0.2, 'Mái che khối 1 tầng', fontsize=9, color=COLOR_TEXT_MUTED, va='center', zorder=10)

    # Limits & Margins
    ax.set_xlim(-3, 51)
    ax.set_ylim(-8, 29)

    # Output path
    output_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\AnGiang\AnGiang13\Tang2"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "mat_bang_tang_2.png")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"SUCCESS: Generated Floor 2 floorplan PNG at {output_path}")

if __name__ == "__main__":
    draw_floorplan_tang2()
