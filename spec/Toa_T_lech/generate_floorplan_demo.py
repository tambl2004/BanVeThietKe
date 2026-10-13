import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_demo_floorplan():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    out_img_path = os.path.join(output_dir, "mat_bang_phac_thao_demo.png")

    fig = plt.figure(figsize=(22, 16), dpi=300)
    ax = fig.add_axes([0.03, 0.05, 0.94, 0.88])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    COLOR_WALL = '#1e293b'
    COLOR_FILL_CORRIDOR = '#eef4f7'
    COLOR_ROOM_FILL = '#ffffff'
    COLOR_DOOR_SWING = '#334155'
    COLOR_TEXT_MAIN = '#0f172a'
    COLOR_TEXT_MUTED = '#64748b'
    COLOR_STAIR_FILL = '#eef4f7'

    W = 0.20  # Exterior wall thickness
    P = 0.10  # Interior partition thickness

    # Header Title
    fig.text(0.04, 0.95, 'MẶT BẰNG TẦNG 1  —  Tòa án nhân dân huyện Nậm Pồ (1 Tòa duy nhất)', 
             color='#0f172a', fontsize=20, fontweight='bold', family='sans-serif')
    header_line = plt.Line2D([0.04, 0.96], [0.93, 0.93], transform=fig.transFigure, color='#e2e8f0', linewidth=1.2)
    fig.lines.append(header_line)

    # -------------------------------------------------------------
    # 1. NỀN HÀNH LANG & SẢNH (Z-order = 1)
    # -------------------------------------------------------------
    # Khối trước (Khối A): Hành lang ngang
    ax.add_patch(patches.Rectangle((0.0, -0.9), 32.0, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    
    # Sảnh đón chính phía Nam
    ax.add_patch(patches.Rectangle((13.5, -4.9), 5.0, 4.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Sảnh cầu thang trung tâm Khối A
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Sảnh nối liên khối trung gian
    ax.add_patch(patches.Rectangle((13.5, 5.4), 5.0, 2.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Khối sau (Khối B): Sảnh trung tâm khối xét xử
    ax.add_patch(patches.Rectangle((13.5, 8.0), 5.0, 10.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # -------------------------------------------------------------
    # 2. CÁC PHÒNG CHỨC NĂNG (Nền trắng, Z-order = 2)
    # -------------------------------------------------------------
    rooms = [
        # Khối A - Dãy Nam Cánh Tây
        {"name": "Phòng Tiếp công dân", "x": 0.0, "y": -4.9, "w": 7.0, "h": 4.0, "door": (3.5, -0.9, 0.9, 'S_in')},
        {"name": "Phòng Tổ Hành chính tư pháp", "x": 7.0, "y": -4.9, "w": 6.5, "h": 4.0, "door": (10.0, -0.9, 0.9, 'S_in')},
        # Khối A - Dãy Nam Cánh Đông
        {"name": "Phòng Văn thư & Lưu trữ", "x": 18.5, "y": -4.9, "w": 6.5, "h": 4.0, "door": (21.5, -0.9, 0.9, 'S_in')},
        {"name": "Phòng Chánh văn phòng", "x": 25.0, "y": -4.9, "w": 7.0, "h": 4.0, "door": (28.5, -0.9, 0.9, 'S_in')},

        # Khối A - Dãy Bắc Cánh Tây (Nhìn ra sân trong Tây)
        {"name": "Phòng Thư ký viên", "x": 0.0, "y": 0.9, "w": 6.5, "h": 4.5, "door": (3.2, 0.9, 0.9, 'N_in')},
        {"name": "Phòng Phó Chánh văn phòng", "x": 6.5, "y": 0.9, "w": 7.0, "h": 4.5, "door": (10.0, 0.9, 0.9, 'N_in')},

        # Khối A - Dãy Bắc Cánh Đông (Nhìn ra sân trong Đông)
        {"name": "Phòng Thư ký viên", "x": 18.5, "y": 0.9, "w": 6.5, "h": 4.5, "door": (21.5, 0.9, 0.9, 'N_in')},
        {"name": "Phòng Kế toán", "x": 25.0, "y": 0.9, "w": 7.0, "h": 4.5, "door": (28.5, 0.9, 0.9, 'N_in')},

        # Khối B (Tòa sau nhỏ hơn: X từ 4.5m đến 27.5m, Y từ 8.0m đến 18.0m)
        # Cánh Tây Khối B: Phòng Xét xử Dân sự
        {"name": "Phòng Xét xử Dân sự\n(Hội trường 1)", "x": 4.5, "y": 8.0, "w": 9.0, "h": 10.0, "door": (13.5, 12.0, 1.4, 'Double_W')},

        # Cánh Đông Khối B: Phòng Xét xử Hình sự
        {"name": "Phòng Xét xử Hình sự\n(Hội trường 2)", "x": 18.5, "y": 8.0, "w": 9.0, "h": 10.0, "door": (18.5, 12.0, 1.4, 'Double_E')},
    ]

    for r in rooms:
        ax.add_patch(patches.Rectangle((r['x'], r['y']), r['w'], r['h'], 
                                       facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2))
        ax.text(r['x'] + r['w']/2, r['y'] + r['h']/2, r['name'], 
                color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)

    # -------------------------------------------------------------
    # 3. NHÃN HÀNH LANG & SẢNH
    # -------------------------------------------------------------
    ax.text(6.5, 0.0, "HÀNH LANG", color=COLOR_TEXT_MUTED, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(25.0, 0.0, "HÀNH LANG", color=COLOR_TEXT_MUTED, fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(16.0, -2.9, "SẢNH ĐÓN CHÍNH", color=COLOR_TEXT_MUTED, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(16.0, 6.7, "SẢNH NỐI LIỀN KHỐI", color=COLOR_TEXT_MUTED, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(16.0, 12.0, "SẢNH TRUNG TÂM\nKHỐI XÉT XỬ", color=COLOR_TEXT_MUTED, fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=4)

    # Ghi chú 2 khoảng sân trong lấy sáng đối xứng
    ax.text(9.0, 6.7, "SÂN TRONG TÂY\n(LẤY SÁNG)", 
            color='#94a3b8', fontsize=8.5, ha='center', va='center', style='italic', zorder=3)
    ax.text(23.0, 6.7, "SÂN TRONG ĐÔNG\n(LẤY SÁNG)", 
            color='#94a3b8', fontsize=8.5, ha='center', va='center', style='italic', zorder=3)

    # -------------------------------------------------------------
    # 4. CẦU THANG BỘ TRUNG TÂM TẦNG 1
    # -------------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 14.5, 1.2, 3.0, 3.0
    ax.add_patch(patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.0, zorder=3))
    num_steps = 9
    for i in range(1, num_steps):
        step_y = stair_y + i * (stair_h / num_steps)
        ax.plot([stair_x, stair_x + stair_w], [step_y, step_y], color='#94a3b8', linewidth=0.8, zorder=4)
    ax.plot([stair_x + stair_w/2, stair_x + stair_w/2], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=1.2, zorder=4)
    ax.text(stair_x + stair_w/2, stair_y - 0.4, "CẦU THANG", color=COLOR_TEXT_MAIN, fontsize=8.5, fontweight='bold', ha='center', va='top', zorder=5)

    # -------------------------------------------------------------
    # 5. TƯỜNG BAO & VÁCH NGĂN (Z-order = 6)
    # -------------------------------------------------------------
    walls = []
    # Khối A: Tường ngoại thất Nam
    walls.append((0.0, -4.9, 13.5, -4.9, W))
    walls.append((18.5, -4.9, 32.0, -4.9, W))
    # Khối A: Hai đầu hồi Đông - Tây (Lớn hơn: X = 0.0m đến 32.0m)
    walls.append((0.0, -4.9, 0.0, -0.9, W))
    walls.append((0.0, 0.9, 0.0, 5.4, W))
    walls.append((32.0, -4.9, 32.0, -0.9, W))
    walls.append((32.0, 0.9, 32.0, 5.4, W))
    # Khối A: Tường Bắc
    walls.append((0.0, 5.4, 13.5, 5.4, W))
    walls.append((18.5, 5.4, 32.0, 5.4, W))
    # Khối A: Tường sảnh chính Nam
    walls.append((13.5, -4.9, 13.5, -0.9, W))
    walls.append((18.5, -4.9, 18.5, -0.9, W))

    # Sảnh nối trung gian (Y: 5.4m -> 8.0m)
    walls.append((13.5, 5.4, 13.5, 8.0, W))
    walls.append((18.5, 5.4, 18.5, 8.0, W))

    # Khối B (Tòa sau nhỏ hơn: X: 4.5m -> 27.5m, Y: 8.0m -> 18.0m)
    # Tường Nam Khối B giáp sân trong
    walls.append((4.5, 8.0, 13.5, 8.0, W))
    walls.append((18.5, 8.0, 27.5, 8.0, W))
    # Tường hai đầu hồi Đông - Tây Khối B (Thụt vào 4.5m ở cả 2 bên)
    walls.append((4.5, 8.0, 4.5, 18.0, W))
    walls.append((27.5, 8.0, 27.5, 18.0, W))
    # Tường Bắc Khối B
    walls.append((4.5, 18.0, 13.5, 18.0, W))
    walls.append((18.5, 18.0, 27.5, 18.0, W))

    # Vách ngăn hành lang Khối A
    walls.append((0.0, -0.9, 13.5, -0.9, P))
    walls.append((18.5, -0.9, 32.0, -0.9, P))
    walls.append((0.0, 0.9, 13.5, 0.9, P))
    walls.append((18.5, 0.9, 32.0, 0.9, P))
    # Vách ngăn các phòng Khối A
    walls.append((7.0, -4.9, 7.0, -0.9, P))
    walls.append((25.0, -4.9, 25.0, -0.9, P))
    walls.append((6.5, 0.9, 6.5, 5.4, P))
    walls.append((25.0, 0.9, 25.0, 5.4, P))

    # Vách ngăn Khối B (Ngăn sảnh với phòng xét xử: X=13.5m và X=18.5m)
    walls.append((13.5, 8.0, 13.5, 11.0, P))
    walls.append((13.5, 13.0, 13.5, 18.0, P))
    walls.append((18.5, 8.0, 18.5, 11.0, P))
    walls.append((18.5, 13.0, 18.5, 18.0, P))

    for x1, y1, x2, y2, th in walls:
        ax.plot([x1, x2], [y1, y2], color=COLOR_WALL, linewidth=th * 18, solid_capstyle='butt', zorder=6)

    # -------------------------------------------------------------
    # 6. BẬC TAM CẤP NGOẠI THẤT (Z-order = 3)
    # -------------------------------------------------------------
    # Sảnh chính Nam
    for i, dy in enumerate([0.2, 0.4, 0.6, 0.8]):
        ax.plot([13.5 - i*0.1, 18.5 + i*0.1], [-4.9 - dy, -4.9 - dy], color='#64748b', linewidth=1.0, zorder=3)
    # Tường má sảnh Nam
    ax.plot([13.5, 13.5], [-4.9, -5.7], color=COLOR_WALL, linewidth=W * 18, solid_capstyle='butt', zorder=6)
    ax.plot([18.5, 18.5], [-4.9, -5.7], color=COLOR_WALL, linewidth=W * 18, solid_capstyle='butt', zorder=6)

    # Sảnh thoát hiểm phía sau (Bắc Khối B)
    for i, dy in enumerate([0.2, 0.4, 0.6]):
        ax.plot([13.5, 18.5], [18.0 + dy, 18.0 + dy], color='#64748b', linewidth=1.0, zorder=3)
    # Tường móc sảnh sau
    ax.plot([13.5, 13.5], [18.0, 18.6], color=COLOR_WALL, linewidth=W * 18, solid_capstyle='butt', zorder=6)
    ax.plot([18.5, 18.5], [18.0, 18.6], color=COLOR_WALL, linewidth=W * 18, solid_capstyle='butt', zorder=6)
    ax.plot([13.5, 14.0], [18.6, 18.6], color=COLOR_WALL, linewidth=W * 18, solid_capstyle='butt', zorder=6)
    ax.plot([18.5, 18.0], [18.6, 18.6], color=COLOR_WALL, linewidth=W * 18, solid_capstyle='butt', zorder=6)

    # Bậc thoát hiểm hai đầu hồi Đông & Tây Khối A
    for dx in [0.25, 0.50, 0.75]:
        ax.plot([-dx, -dx], [-0.9, 0.9], color='#64748b', linewidth=0.9, zorder=3)
        ax.plot([32.0 + dx, 32.0 + dx], [-0.9, 0.9], color='#64748b', linewidth=0.9, zorder=3)

    # -------------------------------------------------------------
    # 7. CỬA ĐI & CỬA SỔ
    # -------------------------------------------------------------
    def draw_door(dx, dy, dw, d_type):
        ax.plot([dx, dx + dw], [dy, dy], color=COLOR_FILL_CORRIDOR if 'S' in d_type else COLOR_ROOM_FILL, linewidth=P*22, zorder=7)
        if 'S_in' in d_type:
            ax.plot([dx, dx], [dy, dy - dw], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=8)
            arc = patches.Arc((dx, dy), 2*dw, 2*dw, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=8)
            ax.add_patch(arc)
        elif 'N_in' in d_type:
            ax.plot([dx, dx], [dy, dy + dw], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=8)
            arc = patches.Arc((dx, dy), 2*dw, 2*dw, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=8)
            ax.add_patch(arc)

    for r in rooms:
        d = r['door']
        if d[3] in ['S_in', 'N_in']:
            draw_door(d[0], d[1], d[2], d[3])
        elif d[3] == 'Double_W':
            # Cửa đôi vào phòng xét xử Tây
            ax.plot([d[0], d[0]], [d[1] - 0.7, d[1] + 0.7], color=COLOR_ROOM_FILL, linewidth=P*24, zorder=7)
            ax.plot([d[0] - 0.7, d[0]], [d[1] - 0.7, d[1] - 0.7], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=8)
            ax.plot([d[0] - 0.7, d[0]], [d[1] + 0.7, d[1] + 0.7], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=8)
            arc1 = patches.Arc((d[0], d[1] - 0.7), 1.4, 1.4, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=8)
            arc2 = patches.Arc((d[0], d[1] + 0.7), 1.4, 1.4, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=8)
            ax.add_patch(arc1)
            ax.add_patch(arc2)
        elif d[3] == 'Double_E':
            # Cửa đôi vào phòng xét xử Đông
            ax.plot([d[0], d[0]], [d[1] - 0.7, d[1] + 0.7], color=COLOR_ROOM_FILL, linewidth=P*24, zorder=7)
            ax.plot([d[0] + 0.7, d[0]], [d[1] - 0.7, d[1] - 0.7], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=8)
            ax.plot([d[0] + 0.7, d[0]], [d[1] + 0.7, d[1] + 0.7], color=COLOR_DOOR_SWING, linewidth=1.5, zorder=8)
            arc1 = patches.Arc((d[0], d[1] - 0.7), 1.4, 1.4, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=8)
            arc2 = patches.Arc((d[0], d[1] + 0.7), 1.4, 1.4, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=8)
            ax.add_patch(arc1)
            ax.add_patch(arc2)

    # Cửa sổ trên tường bao
    def draw_window(wx1, wy1, wx2, wy2):
        ax.plot([wx1, wx2], [wy1, wy2], color='#38bdf8', linewidth=2.0, zorder=9)

    # Windows on South Facade Khối A
    for wx in [1.5, 4.5, 8.5, 11.5, 20.0, 23.0, 27.0, 30.0]:
        draw_window(wx, -4.9, wx + 1.2, -4.9)
    # Windows on North Rear Facade Khối B
    for wx in [6.0, 9.5, 20.0, 23.5]:
        draw_window(wx, 18.0, wx + 2.0, 18.0)
    # Windows on West & East Facade Khối B
    for wy in [10.0, 14.0]:
        draw_window(4.5, wy, 4.5, wy + 2.0)
        draw_window(27.5, wy, 27.5, wy + 2.0)

    # Chú thích góc dưới
    lg_x, lg_y = 1.0, -8.0
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.4, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.1, 'Hành lang / Sảnh kết nối', color=COLOR_TEXT_MUTED, fontsize=9.0, va='bottom')
    ax.add_patch(patches.Rectangle((lg_x + 7.5, lg_y + 0.15), 1.2, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 9.0, lg_y + 0.1, 'Tường kết cấu chịu lực', color=COLOR_TEXT_MUTED, fontsize=9.0, va='bottom')

    # Giới hạn trục tọa độ
    ax.set_xlim(-3.0, 35.0)
    ax.set_ylim(-9.5, 20.5)

    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Generated floorplan successfully: {out_img_path}")

if __name__ == '__main__':
    generate_demo_floorplan()
