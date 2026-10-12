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

def create_floorplan_tang3(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    out_img_path = os.path.join(output_dir, 'mat_bang_tang_3.png')

    # ---------------------------------------------------------
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(26, 15), dpi=300)
    ax = fig.add_axes([0.03, 0.06, 0.94, 0.88])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Bảng màu kiến trúc chuẩn mực theo Spec Tầng 3
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#ffffff'    # Floor 3 staircase fill is pure white per Spec

    WALL_THICKNESS = 0.22           # 220mm exterior wall
    PART_THICKNESS = 0.12           # 120mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    X_MAX = 35.0                    # Tổng chiều dài tòa nhà mở rộng = 35.0m
    LOBBY_W = 6.0                   # Trục trung tâm rộng 6.0m (X: 14.5 to 20.5)

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Tiêu đề bản vẽ (Chuẩn font 20 bold, KHÔNG có dòng phụ)
    fig.text(0.04, 0.962, 'MẶT BẰNG TẦNG 3  —  TÒA ÁN NHÂN DÂN KHU VỰC 1 - CAO BẰNG', 
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
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (TẦNG 3 KHÉP KÍN HAI ĐẦU)
    # ---------------------------------------------------------
    # Hành lang trung tâm (X: 0.0 to 35.0, Y: -1.0 to 1.0, rộng 2.0m)
    ax.add_patch(patches.Rectangle((0.0, -1.0), X_MAX, 2.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Sảnh cầu thang bộ phía Bắc (X: 14.5 to 20.5, Y: 1.0 to 6.5, kích thước 6.0m x 5.5m)
    ax.add_patch(patches.Rectangle((14.5, 1.0), LOBBY_W, 5.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (TẤT CẢ 10 PHÒNG THEO KHẢO SÁT PROMPT)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # =========================================================
        # === DÃY NAM: 6 PHÒNG HÀNH CHÍNH & LÀM VIỆC CHUYÊN MÔN ===
        # =========================================================
        # 1. Phòng Thẩm phán 1 (Cánh Tây Nam: 7.25m x 6.0m)
        {
            'id': 'T3_TP1', 'name': 'Phòng Thẩm phán',
            'x': 0.0, 'y': -7.0, 'w': 7.25, 'h': 6.0,
            'text_center': (3.625, -4.0),
            'door': (5.8, -1.0, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        # 2. Phòng Phó Chánh án 2 (Cánh Tây Nam: 7.25m x 6.0m)
        {
            'id': 'T3_PHO_CA2', 'name': 'Phòng Phó Chánh án',
            'x': 7.25, 'y': -7.0, 'w': 7.25, 'h': 6.0,
            'text_center': (10.875, -4.0),
            'door': (13.0, -1.0, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        # 3. Phòng Phó Chánh án 1 (Nam Trung tâm: 6.0m x 6.0m)
        {
            'id': 'T3_PHO_CA1', 'name': 'Phòng Phó Chánh án',
            'x': 14.5, 'y': -7.0, 'w': 6.0, 'h': 6.0,
            'text_center': (17.5, -4.0),
            'door': (15.5, -1.0, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        # 4. Phòng Kế toán (Cánh Đông Nam: 4.83m x 6.0m)
        {
            'id': 'T3_KETOAN', 'name': 'Phòng Kế toán',
            'x': 20.5, 'y': -7.0, 'w': 4.83, 'h': 6.0,
            'text_center': (22.915, -4.0),
            'door': (21.8, -1.0, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        # 5. Phòng Thư ký 1 (Cánh Đông Nam: 4.84m x 6.0m, 3 người)
        {
            'id': 'T3_TK1', 'name': 'Phòng Thư ký',
            'x': 25.33, 'y': -7.0, 'w': 4.84, 'h': 6.0,
            'text_center': (27.75, -4.0),
            'door': (26.6, -1.0, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        # 6. Phòng Thư ký 2 (Cánh Đông Nam: 4.83m x 6.0m, KT survey 6.4x4.8m, 3 người)
        {
            'id': 'T3_TK2', 'name': 'Phòng Thư ký',
            'x': 30.17, 'y': -7.0, 'w': 4.83, 'h': 6.0,
            'text_center': (32.585, -4.0),
            'door': (31.4, -1.0, 0.9, 'S_IN_RIGHT'),
            'font_size': 10.0
        },

        # =========================================================
        # === DÃY BẮC: 4 PHÒNG THẨM PHÁN (SÂU 5.5m) ===
        # =========================================================
        # --- CÁNH TÂY (2 PHÒNG THẨM PHÁN) ---
        # 7. Phòng Thẩm phán 2 (Cánh Tây Bắc 1: 7.25m x 5.5m)
        {
            'id': 'T3_TP2', 'name': 'Phòng Thẩm phán',
            'x': 0.0, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (3.625, 3.75),
            'door': (5.8, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        # 8. Phòng Thẩm phán 3 (Cánh Tây Bắc 2: 7.25m x 5.5m)
        {
            'id': 'T3_TP3', 'name': 'Phòng Thẩm phán',
            'x': 7.25, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (10.875, 3.75),
            'door': (8.5, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },

        # --- CÁNH ĐÔNG (2 PHÒNG THẨM PHÁN) ---
        # 9. Phòng Thẩm phán 4 (Cánh Đông Bắc 1: 7.25m x 5.5m)
        {
            'id': 'T3_TP4', 'name': 'Phòng Thẩm phán',
            'x': 20.5, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (24.125, 3.75),
            'door': (21.8, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        },
        # 10. Phòng Thẩm phán 5 (Cánh Đông Bắc 2: 7.25m x 5.5m)
        {
            'id': 'T3_TP5', 'name': 'Phòng Thẩm phán',
            'x': 27.75, 'y': 1.0, 'w': 7.25, 'h': 5.5,
            'text_center': (31.375, 3.75),
            'door': (29.0, 1.0, 0.9, 'N_IN_RIGHT'),
            'font_size': 10.5
        }
    ]

    # Tô màu nền trắng thuần cho tất cả các phòng chức năng
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES (TẦNG 3: NỀN TRẮNG THUẦN THEO SPEC)
    # ---------------------------------------------------------
    stair_x, stair_y, stair_w, stair_h = 16.1, 1.8, 2.8, 3.2
    stair_bg = patches.Rectangle((stair_x, stair_y), stair_w, stair_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair_bg)

    num_treads = 10
    for i in range(num_treads + 1):
        sy = stair_y + i * (stair_h / num_treads)
        ax.plot([stair_x, stair_x + stair_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid_x = stair_x + stair_w / 2.0
    top_step_y = stair_y + (num_treads - 1) * (stair_h / num_treads)
    ax.plot([mid_x, mid_x], [stair_y, top_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(mid_x, stair_y - 0.25, 'Cầu thang bộ', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='top', zorder=5)

    # Nhãn Hành lang
    ax.text(7.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(27.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=10.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW STRUCTURAL WALLS & PARTITIONS (KHÉP KÍN TOÀN BỘ)
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # ==========================
    # === TƯỜNG BAO NGOẠI THẤT (TẦNG 3 KHÉP KÍN LIÊN TỤC) ===
    # ==========================
    # Vách ngoài biên Tây (X = -W) - KHÉP KÍN TOÀN BỘ CHIỀU SÂU
    draw_wall(-W, -7.0 - W, W, 13.5 + 2 * W)

    # Vách ngoài biên Đông (X = 35.0) - KHÉP KÍN TOÀN BỘ CHIỀU SÂU
    draw_wall(X_MAX, -7.0 - W, W, 13.5 + 2 * W)

    # Tường bao Nam (Y = -7.0 - W) - CHẠY KÍN LIÊN TỤC TOÀN BỘ MẶT TIỀN
    draw_wall(-W, -7.0 - W, X_MAX + 2 * W, W)

    # Tường bao Bắc (Y = 6.5m) - CHẠY KÍN LIÊN TỤC TOÀN BỘ MẶT SAU
    draw_wall(-W, 6.5, X_MAX + 2 * W, W)

    # ==========================
    # === VÁCH NGĂN HÀNH LANG ===
    # ==========================
    # Vách ngăn hành lang Bắc (Y = 1.0m) có chừa cửa cho 4 phòng
    # Cánh Tây: TP2 (5.8m), TP3 (8.5m)
    draw_wall(0.0, 1.0 - P/2, 5.8, P)
    draw_wall(6.7, 1.0 - P/2, 1.8, P)
    draw_wall(9.4, 1.0 - P/2, 5.1, P)
    # X: 14.5 to 20.5 thông sảnh thang
    # Cánh Đông: TP4 (21.8m), TP5 (29.0m)
    draw_wall(20.5, 1.0 - P/2, 1.3, P)
    draw_wall(22.7, 1.0 - P/2, 6.3, P)
    draw_wall(29.9, 1.0 - P/2, 5.1, P)

    # Vách ngăn hành lang Nam (Y = -1.0m) có chừa cửa cho 6 phòng
    # TP1 (5.8m), Phó CA 2 (13.0m), Phó CA 1 (15.5m), Kế toán (21.8m), TK1 (26.6m), TK2 (31.4m)
    draw_wall(0.0, -1.0 - P/2, 5.8, P)
    draw_wall(6.7, -1.0 - P/2, 6.3, P)
    draw_wall(13.9, -1.0 - P/2, 1.6, P)
    draw_wall(16.4, -1.0 - P/2, 5.4, P)
    draw_wall(22.7, -1.0 - P/2, 3.9, P)
    draw_wall(27.5, -1.0 - P/2, 3.9, P)
    draw_wall(32.3, -1.0 - P/2, 2.7, P)

    # ==========================
    # === VÁCH NGĂN PHÒNG NỘI BỘ ===
    # ==========================
    # Dãy Bắc:
    draw_wall(7.25 - P/2, 1.0, P, 5.5)     # TP2 & TP3
    draw_wall(14.5 - P/2, 1.0, P, 5.5)     # TP3 & Sảnh thang
    draw_wall(20.5 - P/2, 1.0, P, 5.5)     # Sảnh thang & TP4
    draw_wall(27.75 - P/2, 1.0, P, 5.5)    # TP4 & TP5

    # Dãy Nam:
    draw_wall(7.25 - P/2, -7.0, P, 6.0)    # TP1 & Phó CA 2
    draw_wall(14.5 - P/2, -7.0, P, 6.0)    # Phó CA 2 & Phó CA 1
    draw_wall(20.5 - P/2, -7.0, P, 6.0)    # Phó CA 1 & Kế toán
    draw_wall(25.33 - P/2, -7.0, P, 6.0)   # Kế toán & TK1
    draw_wall(30.17 - P/2, -7.0, P, 6.0)   # TK1 & TK2

    # ---------------------------------------------------------
    # 7. DRAW WINDOWS (VỪA PHẢI, THOÁNG ĐÃNG, KHÔNG LỖI CHÈN ÉP)
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

    # Cửa sổ mặt tiền Nam (Y = -7.0 - W):
    # TP1:
    draw_window(1.8, -7.0 - W, 1.8, W, is_horizontal=True)
    draw_window(4.6, -7.0 - W, 1.8, W, is_horizontal=True)
    # Phó CA 2:
    draw_window(9.0, -7.0 - W, 1.8, W, is_horizontal=True)
    draw_window(11.8, -7.0 - W, 1.8, W, is_horizontal=True)
    # Phó CA 1: 2 cửa sổ sang trọng đối xứng
    draw_window(15.4, -7.0 - W, 1.8, W, is_horizontal=True)
    draw_window(17.8, -7.0 - W, 1.8, W, is_horizontal=True)
    # Kế toán: 1 cửa sổ lớn
    draw_window(22.0, -7.0 - W, 1.8, W, is_horizontal=True)
    # TK1: 1 cửa sổ lớn
    draw_window(26.8, -7.0 - W, 1.8, W, is_horizontal=True)
    # TK2: 1 cửa sổ lớn
    draw_window(31.7, -7.0 - W, 1.8, W, is_horizontal=True)

    # Cửa sổ mặt sau Bắc (Y = 6.5m):
    # TP2:
    draw_window(1.8, 6.5, 1.8, W, is_horizontal=True)
    draw_window(4.6, 6.5, 1.8, W, is_horizontal=True)
    # TP3:
    draw_window(9.0, 6.5, 1.8, W, is_horizontal=True)
    draw_window(11.8, 6.5, 1.8, W, is_horizontal=True)
    # Sảnh cầu thang bộ trung tâm:
    draw_window(16.5, 6.5, 2.0, W, is_horizontal=True)
    # TP4:
    draw_window(22.2, 6.5, 1.8, W, is_horizontal=True)
    draw_window(25.0, 6.5, 1.8, W, is_horizontal=True)
    # TP5:
    draw_window(29.4, 6.5, 1.8, W, is_horizontal=True)
    draw_window(32.2, 6.5, 1.8, W, is_horizontal=True)

    # Cửa sổ đầu hồi Tây (X = -W) - Mỗi phòng 1 cửa sổ tâm vách + 1 cửa sổ đầu hành lang
    draw_window(-W, -4.9, W, 1.8, is_horizontal=False)   # Phòng Thẩm phán 1 (Y: -4.9 to -3.1)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)   # Cửa sổ lấy sáng đầu hành lang Tây
    draw_window(-W, 2.85, W, 1.8, is_horizontal=False)   # Phòng Thẩm phán 2 (Y: 2.85 to 4.65)

    # Cửa sổ đầu hồi Đông (X = 35.0) - Mỗi phòng 1 cửa sổ tâm vách + 1 cửa sổ đầu hành lang
    draw_window(X_MAX, -4.9, W, 1.8, is_horizontal=False)  # Phòng Thư ký 2 (Y: -4.9 to -3.1)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)  # Cửa sổ lấy sáng đầu hành lang Đông
    draw_window(X_MAX, 2.85, W, 1.8, is_horizontal=False)  # Phòng Thẩm phán 5 (Y: 2.85 to 4.65)

    # ---------------------------------------------------------
    # 8. DRAW DOORS (INWARD SWINGING PER SPEC)
    # ---------------------------------------------------------
    def draw_door(hx, hy, dw, dtype):
        if dtype == 'N_IN_RIGHT':
            ax.plot([hx, hx], [hy, hy + dw], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((hx, hy), dw * 2, dw * 2, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc)
        elif dtype == 'S_IN_RIGHT':
            ax.plot([hx, hx], [hy, hy - dw], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc = patches.Arc((hx, hy), dw * 2, dw * 2, angle=0, theta1=270, theta2=360, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc)

    for r in rooms:
        if r['door'] is not None:
            hx, hy, dw, dtype = r['door']
            draw_door(hx, hy, dw, dtype)

    # ---------------------------------------------------------
    # 9. ROOM TEXT LABELS
    # ---------------------------------------------------------
    for r in rooms:
        tx, ty = r['text_center']
        ax.text(tx, ty, r['name'], color=COLOR_TEXT_MAIN, fontsize=r['font_size'], 
                fontweight='bold', ha='center', va='center', zorder=20)

    # ---------------------------------------------------------
    # 10. EXPORT HIGH-RESOLUTION IMAGE (300 DPI)
    # ---------------------------------------------------------
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Floorplan Cao Bang 1 Tầng 3 successfully generated at: {out_img_path}")

    # Copy ảnh và file code sang thư mục cha CaoBang1 nếu cần
    parent_dir = os.path.dirname(output_dir)
    if os.path.basename(parent_dir) == 'CaoBang1':
        parent_img = os.path.join(parent_dir, 'mat_bang_tang_3.png')
        shutil.copyfile(out_img_path, parent_img)
        print(f"Copied floorplan to parent directory: {parent_img}")

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    create_floorplan_tang3(script_dir)
