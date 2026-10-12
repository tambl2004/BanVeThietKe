import os
import shutil
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
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(26, 15), dpi=300)
    ax = fig.add_axes([0.03, 0.06, 0.94, 0.88])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Spec Tầng 2
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#ffffff'    # Floor 2 staircase fill is pure white per Spec

    WALL_THICKNESS = 0.22           # 220mm exterior wall
    PART_THICKNESS = 0.12           # 120mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    X_MAX = 35.0                    # Tổng chiều dài tòa nhà = 35.0m
    LOBBY_W = 6.0                   # Trục trung tâm rộng 6.0m (X: 14.5 to 20.5)

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Tiêu đề bản vẽ (Chuẩn font 20 bold, KHÔNG có dòng phụ)
    fig.text(0.04, 0.962, 'MẶT BẰNG TẦNG 2  —  TÒA ÁN NHÂN DÂN KHU VỰC 5 - CAO BẰNG', 
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    # Đường phân cách tiêu đề
    header_line = plt.Line2D([0.04, 0.96], [0.945, 0.945], transform=fig.transFigure, color='#e2e8f0', linewidth=1.1)
    fig.lines.append(header_line)

    # Chú thích bản vẽ (Legend) đặt gọn gàng phía dưới
    lg_x, lg_y = 5.5, -9.8
    # Legend 1: Hành lang / sảnh
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend 2: Tường / vách
    ax.add_patch(patches.Rectangle((lg_x + 7.0, lg_y + 0.10), 1.2, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 8.5, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend 3: Cửa sổ
    ax.plot([lg_x + 14.0, lg_x + 15.2], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 14.0, lg_x + 15.2], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 15.5, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend 4: Cửa đi mở vào
    ax.plot([lg_x + 20.5, lg_x + 20.5], [lg_y + 0.02, lg_y + 0.32], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 20.5, lg_y + 0.02), 0.60, 0.60, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 21.8, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL
    # ---------------------------------------------------------
    # Toàn bộ mặt bằng lót màu pastel grey-cyan (#eef4f7)
    # Phía Nam hoàn toàn mở làm hành lang sảnh rộng rãi
    ax.add_patch(patches.Rectangle((0.0, -7.0), X_MAX, 13.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (4 PHÒNG CHIA ĐỀU CHO 2 CÁNH DÃY BẮC)
    # ---------------------------------------------------------
    # Cánh Tây Bắc (2 phòng): 2 Phòng Thẩm phán
    # Cánh Đông Bắc (2 phòng): Phòng Chánh án & Phòng Thư ký
    rooms: List[RoomDict] = [
        # === CÁNH TÂY BẮC (2 PHÒNG THẨM PHÁN) ===
        # 1. Phòng Thẩm phán 1 (X: 0.0 to 7.25m, Y: 1.0 to 6.5m)
        {
            'id': 'T2_TP1', 'name': 'Phòng Thẩm phán',
            'x': 0.0, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (3.625, 3.75),
            'door': (5.8, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.0
        },
        # 2. Phòng Thẩm phán 2 (X: 7.25 to 14.5m, Y: 1.0 to 6.5m)
        {
            'id': 'T2_TP2', 'name': 'Phòng Thẩm phán',
            'x': 7.25, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (10.875, 3.75),
            'door': (8.5, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.0
        },

        # === CÁNH ĐÔNG BẮC (PHÒNG CHÁNH ÁN & PHÒNG THƯ KÝ) ===
        # 3. Phòng Chánh án (X: 20.5 to 27.75m, Y: 1.0 to 6.5m, kề sảnh thang)
        {
            'id': 'T2_CA', 'name': 'Phòng Chánh án',
            'x': 20.5, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (24.125, 3.75),
            'door': (21.8, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.5
        },
        # 4. Phòng Thư ký (X: 27.75 to 35.0m, Y: 1.0 to 6.5m, kề Phòng Chánh án)
        {
            'id': 'T2_TK', 'name': 'Phòng Thư ký',
            'x': 27.75, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (31.375, 3.75),
            'door': (29.0, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 11.0
        },
    ]

    # Tô màu nền trắng thuần cho 4 phòng chức năng
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES (TẦNG 2: NỀN TRẮNG THUẦN THEO SPEC)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 16.1, 1.8, 2.8, 3.2
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, 
                                 facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    # Hai vế thang đối xứng
    gap = 0.35
    flight_w = (stair_w - gap) / 2.0
    left_x1, left_x2 = stair_x, stair_x + flight_w
    right_x1, right_x2 = stair_x + flight_w + gap, stair_x + stair_w

    num_treads = 10
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([left_x1, left_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)
        ax.plot([right_x1, right_x2], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    # Phân vế thang
    mid_left = left_x1 + flight_w / 2.0
    mid_right = right_x1 + flight_w / 2.0
    ax.plot([mid_left, mid_left], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.plot([mid_right, mid_right], [stair_y, stair_y + stair_h], color=COLOR_WALL, linewidth=0.9, zorder=4)

    ax.text(stair_x + stair_w / 2.0, stair_y - 0.25, 'Cầu thang', color=COLOR_TEXT_MAIN, 
            fontsize=9.0, fontweight='bold', ha='center', va='top', zorder=5)

    # Nhãn không gian Hành lang sảnh rộng mở phía Nam ("ở dưới trống trải làm hành lang cho rộng")
    ax.text(7.25, 0.0, 'HÀNH LANG SẢNH', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(27.75, 0.0, 'HÀNH LANG SẢNH', color=COLOR_TEXT_MAIN, fontsize=10.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(7.25, -4.0, 'HÀNH LANG SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(17.5, -4.0, 'HÀNH LANG SẢNH', color=COLOR_TEXT_MAIN, fontsize=12.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(27.75, -4.0, 'HÀNH LANG SẢNH', color=COLOR_TEXT_MAIN, fontsize=11.5, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW STRUCTURAL WALLS & PARTITIONS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # ==========================
    # === TƯỜNG BAO NGOẠI THẤT LIÊN TỤC KHÉP KÍN ===
    # ==========================
    # Tường bao Tây (X = -W) - Chạy kín từ Nam lên Bắc
    draw_wall(-W, -7.0 - W, W, 13.5 + 2 * W)

    # Tường bao Đông (X = 35.0) - Chạy kín từ Nam lên Bắc
    draw_wall(X_MAX, -7.0 - W, W, 13.5 + 2 * W)

    # Tường bao Nam (Y = -7.0 - W) - Chạy kín suốt toàn bộ mặt tiền
    draw_wall(-W, -7.0 - W, X_MAX + 2 * W, W)

    # Tường bao Bắc (Y = 6.5m) - Chạy kín suốt toàn bộ mặt sau
    draw_wall(-W, 6.5, X_MAX + 2 * W, W)

    # ==========================
    # === VÁCH NGĂN PHÒNG DÃY BẮC (NỘI BỘ) ===
    # ==========================
    # Vách ngăn giữa Thẩm phán 1 & Thẩm phán 2 (X = 7.25m)
    draw_wall(7.25 - P/2, 1.0, P, 5.5)

    # Vách ngăn Tây sảnh thang (X = 14.5m)
    draw_wall(14.5 - P/2, 1.0, P, 5.5)

    # Vách ngăn Đông sảnh thang (X = 20.5m)
    draw_wall(20.5 - P/2, 1.0, P, 5.5)

    # Vách ngăn giữa Chánh án & Thư ký (X = 27.75m)
    draw_wall(27.75 - P/2, 1.0, P, 5.5)

    # ==========================
    # === VÁCH NGĂN HÀNH LANG BẮC (Y = 1.0m) CÓ CỬA ĐI ===
    # ==========================
    # Cánh Tây Bắc: Thẩm phán 1 (cửa tại 5.8m), Thẩm phán 2 (cửa tại 8.5m)
    draw_wall(0.0, 1.0 - P/2, 5.8, P)
    draw_wall(6.7, 1.0 - P/2, 1.8, P)
    draw_wall(9.4, 1.0 - P/2, 5.1, P)

    # Khoảng giữa X: 14.5 to 20.5m mở thông hoàn toàn sảnh thang!

    # Cánh Đông Bắc: Chánh án (cửa tại 21.8m), Thư ký (cửa tại 29.0m)
    draw_wall(20.5, 1.0 - P/2, 1.3, P)
    draw_wall(22.7, 1.0 - P/2, 6.3, P)
    draw_wall(29.9, 1.0 - P/2, 5.1, P)

    # Toàn bộ Dãy Nam (Y < 1.0m) hoàn toàn dỡ bỏ vách ngăn, tạo không gian sảnh hành lang cực kỳ rộng rãi và thông thoáng!

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

    # Cửa sổ tường Bắc (Y = 6.5m)
    # Thẩm phán 1:
    draw_window(1.5, 6.5, 1.8, W, is_horizontal=True)
    draw_window(4.3, 6.5, 1.8, W, is_horizontal=True)
    # Thẩm phán 2:
    draw_window(8.75, 6.5, 1.8, W, is_horizontal=True)
    draw_window(11.55, 6.5, 1.8, W, is_horizontal=True)
    # Sau sảnh thang:
    draw_window(16.5, 6.5, 2.0, W, is_horizontal=True)
    # Phòng Chánh án:
    draw_window(22.0, 6.5, 1.8, W, is_horizontal=True)
    draw_window(24.8, 6.5, 1.8, W, is_horizontal=True)
    # Phòng Thư ký:
    draw_window(29.25, 6.5, 1.8, W, is_horizontal=True)
    draw_window(32.05, 6.5, 1.8, W, is_horizontal=True)

    # Cửa sổ mặt tiền Nam (Y = -7.0 - W) - Bố trí thoáng đãng, cân xứng
    draw_window(2.2, -7.0 - W, 2.0, W, is_horizontal=True)
    draw_window(6.0, -7.0 - W, 2.0, W, is_horizontal=True)
    draw_window(9.8, -7.0 - W, 2.0, W, is_horizontal=True)
    draw_window(15.4, -7.0 - W, 2.0, W, is_horizontal=True)
    draw_window(18.0, -7.0 - W, 2.0, W, is_horizontal=True)
    draw_window(23.2, -7.0 - W, 2.0, W, is_horizontal=True)
    draw_window(27.0, -7.0 - W, 2.0, W, is_horizontal=True)
    draw_window(30.8, -7.0 - W, 2.0, W, is_horizontal=True)

    # Cửa sổ đầu hồi Tây (X = -W) & Đông (X = 35.0)
    # Đầu hành lang lấy sáng
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)

    # Cửa sổ hông phòng:
    draw_window(-W, -4.8, W, 2.0, is_horizontal=False)     # Sảnh Nam Tây
    draw_window(-W, 2.8, W, 2.0, is_horizontal=False)      # Thẩm phán 1
    draw_window(X_MAX, -4.8, W, 2.0, is_horizontal=False)  # Sảnh Nam Đông
    draw_window(X_MAX, 2.8, W, 2.0, is_horizontal=False)   # Thư ký

    # ---------------------------------------------------------
    # 8. DRAW DOORS & SWINGS
    # ---------------------------------------------------------
    def draw_door_n_in(x, y, size):
        # Mở từ hành lang (Y = 1.0) vào phía Bắc (Y dương)
        ax.plot([x, x], [y, y + size], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
        arc = patches.Arc((x, y), size*2, size*2, angle=0, theta1=0, theta2=90,
                          color=COLOR_DOOR_SWING, linestyle='-', linewidth=1.0, zorder=14)
        ax.add_patch(arc)

    for r in rooms:
        if r['door']:
            dx, dy, dsize, dmode = r['door']
            draw_door_n_in(dx, dy, dsize)

    # ---------------------------------------------------------
    # 9. DRAW ROOM LABELS
    # ---------------------------------------------------------
    for r in rooms:
        tx, ty = r['text_center']
        ax.text(tx, ty, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'], 
                fontweight='bold', ha='center', va='center', zorder=15)

    # Canvas viewport limits
    ax.set_xlim(-3.0, 38.0)
    ax.set_ylim(-11.5, 9.5)

    # Xuất file ảnh PNG 300 DPI
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    print(f"SUCCESS: Đã tạo thành công mặt bằng Tầng 2 điều chỉnh tại {out_img_path}")
    plt.close(fig)

if __name__ == '__main__':
    target_dir = r"c:\Users\Tam\Desktop\BanVeThietKe\CaoBang\CaoBang5\Tang2"
    create_floorplan_tang2(target_dir)
