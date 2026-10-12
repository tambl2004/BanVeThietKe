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
    # 1. SETUP CANVAS & CANVAS STYLING
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(24, 17), dpi=300)
    ax = fig.add_axes([0.03, 0.05, 0.94, 0.89])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    # Color Palette according to Architectural Spec
    COLOR_WALL = '#1e293b'          # Dark slate structural wall & partitions
    COLOR_FILL_CORRIDOR = '#eef4f7'  # Soft pastel grey-cyan fill for corridor/lobby
    COLOR_ROOM_FILL = '#ffffff'     # Pure white for room interior
    COLOR_DOOR_SWING = '#334155'    # Dark slate door panel and arc
    COLOR_TEXT_MAIN = '#0f172a'     # Deep navy text
    COLOR_TEXT_MUTED = '#64748b'    # Muted grey text
    COLOR_STAIR_FILL = '#ffffff'    # Floor 2 staircase fill is pure white per Spec

    WALL_THICKNESS = 0.20           # 200mm exterior wall
    PART_THICKNESS = 0.10           # 100mm interior wall
    W = WALL_THICKNESS
    P = PART_THICKNESS

    X_MAX = 32.0                    # Tòa 1 length = 32.0m

    # ---------------------------------------------------------
    # 2. HEADER & LEGEND
    # ---------------------------------------------------------
    # Header Title (Single-line, font 20 bold, NO subtitle line per Spec)
    fig.text(0.04, 0.962, 'MẶT BẰNG TẦNG 2  —  TÒA ÁN NHÂN DÂN KHU VỰC 9 - CÀ MAU', 
             color=COLOR_TEXT_MAIN, fontsize=20, fontweight='bold', family='sans-serif')
    
    # Header horizontal line
    header_line = plt.Line2D([0.04, 0.96], [0.945, 0.945], transform=fig.transFigure, color='#e2e8f0', linewidth=1.1)
    fig.lines.append(header_line)

    # Legend Box Centered at Bottom
    lg_x, lg_y = 4.0, -8.2
    # Legend Item 1: Corridor fill
    ax.add_patch(patches.Rectangle((lg_x, lg_y), 1.2, 0.35, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))
    ax.text(lg_x + 1.5, lg_y + 0.05, 'Hành lang / sảnh', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 2: Wall
    ax.add_patch(patches.Rectangle((lg_x + 7.0, lg_y + 0.10), 1.2, 0.15, facecolor=COLOR_WALL, edgecolor='none', zorder=1))
    ax.text(lg_x + 8.5, lg_y + 0.05, 'Tường / vách', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 3: Window
    ax.plot([lg_x + 14.0, lg_x + 15.2], [lg_y + 0.22, lg_y + 0.22], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.plot([lg_x + 14.0, lg_x + 15.2], [lg_y + 0.08, lg_y + 0.08], color=COLOR_WALL, linewidth=1.5, zorder=1)
    ax.text(lg_x + 15.5, lg_y + 0.05, 'Cửa sổ', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # Legend Item 4: Door
    ax.plot([lg_x + 20.5, lg_x + 20.5], [lg_y + 0.02, lg_y + 0.32], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=1)
    arc_lg = patches.Arc((lg_x + 20.5, lg_y + 0.02), 0.60, 0.60, angle=0, theta1=0, theta2=90, color=COLOR_DOOR_SWING, linewidth=1.0)
    ax.add_patch(arc_lg)
    ax.text(lg_x + 21.8, lg_y + 0.05, 'Cửa đi mở vào', color=COLOR_TEXT_MUTED, fontsize=9.5, va='bottom')

    # ---------------------------------------------------------
    # 3. CORRIDOR & LOBBY BACKGROUND FILL (SEAMLESS INTEGRATION)
    # ---------------------------------------------------------
    # === TÒA 1 CORRIDOR & STAIR HALL ===
    # Horizontal Central Corridor (X: 0.0 to 32.0, Y: -0.9 to 0.9)
    ax.add_patch(patches.Rectangle((0.0, -0.9), X_MAX, 1.8, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # North Central Hall / Staircase Space (X: 13.5 to 18.5, Y: 0.9 to 5.4)
    ax.add_patch(patches.Rectangle((13.5, 0.9), 5.0, 4.5, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === CONNECTING LOBBY PASSAGE TO TÒA 2 ===
    # Passage neck connecting Tòa 1 to Tòa 2 (X: 13.5 to 18.5, Y: 5.4 to 7.0)
    ax.add_patch(patches.Rectangle((13.5, 5.4), 5.0, 1.6, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # === TÒA 2: FOYER GIỮA & SẢNH CHỜ XÉT XỬ CÁNH ĐÔNG ===
    # Central Courtroom Lobby / Staircase Hall (X: 13.5 to 18.5, Y: 7.0 to 15.0)
    ax.add_patch(patches.Rectangle((13.5, 7.0), 5.0, 8.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # Cánh Đông Tòa 2: Sảnh chờ xét xử / Không gian mở liền mạch (X: 18.5 to 30.5, Y: 7.0 to 15.0)
    ax.add_patch(patches.Rectangle((18.5, 7.0), 12.0, 8.0, facecolor=COLOR_FILL_CORRIDOR, edgecolor='none', zorder=1))

    # ---------------------------------------------------------
    # 4. ROOM DEFINITIONS (ALL 13 ROOMS TÒA 1 + PHÒNG XÉT XỬ TÒA 2)
    # ---------------------------------------------------------
    rooms: List[RoomDict] = [
        # =========================================================
        # === TÒA 1: KHỐI NHÀ CHÍNH (13 PHÒNG) ===
        # =========================================================
        # --- DÃY BẮC CÁNH TÂY (3 PHÒNG) ---
        # 1. Tp Phương (KT survey: 4,8m x 3,5m - 2 người)
        {
            'id': 'T1_TP_PHUONG', 'name': 'Tp Phương',
            'x': 0.0, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (2.25, 3.15),
            'door': (3.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        # 2. Tp. Bình (KT survey: 4,8m x 4m - 1 người)
        {
            'id': 'T1_TP_BINH', 'name': 'Tp. Bình',
            'x': 4.5, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (6.75, 3.15),
            'door': (7.7, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        # 3. Tp Đào (KT survey: 4,8m x 3,5m - 2 người)
        {
            'id': 'T1_TP_DAO', 'name': 'Tp Đào',
            'x': 9.0, 'y': 0.9, 'w': 4.5, 'h': 4.5,
            'text_center': (11.25, 3.15),
            'door': (12.2, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },

        # --- DÃY BẮC CÁNH ĐÔNG (3 PHÒNG) ---
        # 4. Tp. Tồn (KT survey: 4,8m x 3,5m - 1 người)
        {
            'id': 'T1_TP_TON', 'name': 'Tp. Tồn',
            'x': 18.5, 'y': 0.9, 'w': 4.0, 'h': 4.5,
            'text_center': (20.5, 3.15),
            'door': (19.8, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        # 5. Kho lưu trữ (KT survey: 6m x 4,5m)
        {
            'id': 'T1_KHO_1', 'name': 'Kho lưu trữ',
            'x': 22.5, 'y': 0.9, 'w': 4.7, 'h': 4.5,
            'text_center': (24.85, 3.15),
            'door': (23.8, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },
        # 6. Kho lưu trữ (KT survey: 6m x 4,5m)
        {
            'id': 'T1_KHO_2', 'name': 'Kho lưu trữ',
            'x': 27.2, 'y': 0.9, 'w': 4.8, 'h': 4.5,
            'text_center': (29.6, 3.15),
            'door': (28.4, 0.9, 0.85, 'N_IN_RIGHT'),
            'font_size': 10.0
        },

        # --- DÃY NAM CÁNH TÂY (3 PHÒNG) ---
        # 8. Tp Thu (KT survey: 8m x 5m - 3 người)
        {
            'id': 'T1_TP_THU', 'name': 'Tp Thu',
            'x': 0.0, 'y': -4.9, 'w': 5.5, 'h': 4.0,
            'text_center': (2.75, -2.9),
            'door': (4.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },
        # 9. Tp Kiệt (KT survey: 5m x 3,5m - 1 người)
        {
            'id': 'T1_TP_KIET', 'name': 'Tp Kiệt',
            'x': 5.5, 'y': -4.9, 'w': 4.0, 'h': 4.0,
            'text_center': (7.5, -2.9),
            'door': (8.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        # 10. Tp Diễm (KT survey: 6m x 3,5m - 1 người)
        {
            'id': 'T1_TP_DIEM', 'name': 'Tp Diễm',
            'x': 9.5, 'y': -4.9, 'w': 4.0, 'h': 4.0,
            'text_center': (11.5, -2.9),
            'door': (12.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.0
        },

        # --- DÃY NAM TRUNG TÂM (1 PHÒNG - THAY THẾ SẢNH CHÍNH TẦNG 1 THEO SPEC) ---
        # 7. Tp. Quy (KT survey: 5m x 4m - 1 người)
        {
            'id': 'T1_TP_QUY', 'name': 'Tp. Quy',
            'x': 13.5, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (16.0, -2.9),
            'door': (14.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.5
        },

        # --- DÃY NAM CÁNH ĐÔNG (3 PHÒNG) ---
        # 11. Thư ký (KT survey: 4m x 3m - 1 người)
        {
            'id': 'T1_THUKY', 'name': 'Thư ký',
            'x': 18.5, 'y': -4.9, 'w': 4.0, 'h': 4.0,
            'text_center': (20.5, -2.9),
            'door': (19.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        # 12. Tp Tú Anh (KT survey: 5m x 4m - 1 người)
        {
            'id': 'T1_TP_TUANH', 'name': 'Tp Tú Anh',
            'x': 22.5, 'y': -4.9, 'w': 4.5, 'h': 4.0,
            'text_center': (24.75, -2.9),
            'door': (23.8, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.0
        },
        # 13. Tp Nhi (KT survey: 6m x 4m - 1 người)
        {
            'id': 'T1_TP_NHI', 'name': 'Tp Nhi',
            'x': 27.0, 'y': -4.9, 'w': 5.0, 'h': 4.0,
            'text_center': (29.5, -2.9),
            'door': (28.2, -0.9, 0.85, 'S_IN_RIGHT'),
            'font_size': 10.0
        },

        # =========================================================
        # === TÒA 2: KHỐI NHÀ XÉT XỬ PHÍA BẮC (CÁNH TÂY) ===
        # =========================================================
        # 14. Phòng xét xử (KT survey: 12m x 6m)
        {
            'id': 'T2_XETXU', 'name': 'Phòng xét xử',
            'x': 1.5, 'y': 7.0, 'w': 12.0, 'h': 8.0,
            'text_center': (7.5, 11.0),
            'door': (13.5, 11.0, 1.4, 'DOUBLE_W'),
            'font_size': 12.0
        }
    ]

    # Render Room Backgrounds
    for r in rooms:
        rect = patches.Rectangle((r['x'], r['y']), r['w'], r['h'], facecolor=COLOR_ROOM_FILL, edgecolor='none', zorder=2)
        ax.add_patch(rect)

    # ---------------------------------------------------------
    # 5. STAIRCASES (TẦNG 2: NỀN TRẮNG THUẦN THEO SPEC)
    # ---------------------------------------------------------
    # === CẦU THANG BỘ TÒA 1 (NORTH HALL TÒA 1) ===
    stair1_x, stair1_y, stair1_w, stair1_h = 14.7, 1.4, 2.6, 2.6
    stair1_bg = patches.Rectangle((stair1_x, stair1_y), stair1_w, stair1_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair1_bg)

    num_treads = 9
    for i in range(num_treads + 1):
        sy = stair1_y + i * (stair1_h / num_treads)
        ax.plot([stair1_x, stair1_x + stair1_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid1_x = stair1_x + stair1_w / 2.0
    top1_step_y = stair1_y + (num_treads - 1) * (stair1_h / num_treads)
    ax.plot([mid1_x, mid1_x], [stair1_y, top1_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(mid1_x, stair1_y - 0.25, 'Cầu thang bộ', color=COLOR_TEXT_MAIN, fontsize=9.0, fontweight='bold', ha='center', va='top', zorder=5)

    # === CẦU THANG BỘ TÒA 2 (KHỐI XÉT XỬ TẦNG 2) ===
    stair2_x, stair2_y, stair2_w, stair2_h = 14.7, 10.2, 2.6, 3.6
    stair2_bg = patches.Rectangle((stair2_x, stair2_y), stair2_w, stair2_h, facecolor=COLOR_STAIR_FILL, edgecolor=COLOR_WALL, linewidth=1.1, zorder=3)
    ax.add_patch(stair2_bg)

    num_treads_2 = 11
    for i in range(num_treads_2 + 1):
        sy = stair2_y + i * (stair2_h / num_treads_2)
        ax.plot([stair2_x, stair2_x + stair2_w], [sy, sy], color=COLOR_WALL, linewidth=0.8, zorder=4)

    mid2_x = stair2_x + stair2_w / 2.0
    top2_step_y = stair2_y + (num_treads_2 - 1) * (stair2_h / num_treads_2)
    ax.plot([mid2_x, mid2_x], [stair2_y, top2_step_y], color=COLOR_WALL, linewidth=0.9, zorder=4)
    ax.text(mid2_x, stair2_y - 0.35, 'Cầu thang khối xét xử', color=COLOR_TEXT_MAIN, 
            fontsize=8.5, fontweight='bold', ha='center', va='top', zorder=5)

    # Nhãn Hành lang & Sảnh
    ax.text(6.75, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(25.25, 0.0, 'HÀNH LANG', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    ax.text(16.0, 7.8, 'SẢNH XÉT XỬ', color=COLOR_TEXT_MAIN, fontsize=9.5, fontweight='bold', ha='center', va='center', zorder=5)
    
    # Nhãn Hành lang sảnh chờ cánh Đông Tòa 2
    ax.text(24.5, 11.0, 'SẢNH CHỜ XÉT XỬ', color=COLOR_TEXT_MAIN, fontsize=12.0, fontweight='bold', ha='center', va='center', zorder=5)

    # ---------------------------------------------------------
    # 6. DRAW STRUCTURAL WALLS & PARTITIONS
    # ---------------------------------------------------------
    def draw_wall(x, y, w, h):
        rect = patches.Rectangle((x, y), w, h, facecolor=COLOR_WALL, edgecolor='none', zorder=10)
        ax.add_patch(rect)

    # ==========================
    # === TƯỜNG BAO TÒA 1 (KÍN HOÀN TOÀN TRÊN TẦNG 2) ===
    # ==========================
    # Vách ngoài biên Tây (X = -W) - KHÉP KÍN TOÀN BỘ CHIỀU DÀI
    draw_wall(-W, -4.9 - W, W, 10.3 + 2 * W)

    # Vách ngoài biên Đông (X = 32.0) - KHÉP KÍN TOÀN BỘ CHIỀU DÀI
    draw_wall(X_MAX, -4.9 - W, W, 10.3 + 2 * W)

    # Tường bao Nam Tòa 1 (Y = -4.9 - W) - CHẠY KÍN LIÊN TỤC TOÀN BỘ MẶT TIỀN (KHÔNG CÒN SẢNH MỞ)
    draw_wall(-W, -4.9 - W, X_MAX + 2 * W, W)

    # Tường bao Bắc Tòa 1 (Y = 5.4m) - mở nối sang Tòa 2 tại X: 13.5 to 18.5
    draw_wall(-W, 5.4, 13.5 + W + P/2, W)
    draw_wall(18.5 - P/2, 5.4, (X_MAX - 18.5) + W + P/2, W)

    # Vách ngăn hành lang Bắc Tòa 1 (Y = 0.9m) có chừa cửa cho 6 phòng
    # Cánh Tây: Tp Phương (3.2), Tp. Bình (7.7), Tp Đào (12.2)
    draw_wall(0.0, 0.9 - P/2, 3.2, P)
    draw_wall(4.05, 0.9 - P/2, 3.65, P)
    draw_wall(8.55, 0.9 - P/2, 3.65, P)
    draw_wall(13.05, 0.9 - P/2, 0.45, P)
    # X: 13.5 to 18.5 thông sảnh thang
    # Cánh Đông: Tp. Tồn (19.8), Kho 1 (23.8), Kho 2 (28.4)
    draw_wall(18.5, 0.9 - P/2, 1.3, P)
    draw_wall(20.65, 0.9 - P/2, 3.15, P)
    draw_wall(24.65, 0.9 - P/2, 3.75, P)
    draw_wall(29.25, 0.9 - P/2, 2.75, P)

    # Vách ngăn hành lang Nam Tòa 1 (Y = -0.9m) có chừa cửa cho 7 phòng
    # Cánh Tây: Tp Thu (4.2), Tp Kiệt (8.2), Tp Diễm (12.2)
    draw_wall(0.0, -0.9 - P/2, 4.2, P)
    draw_wall(5.05, -0.9 - P/2, 3.15, P)
    draw_wall(9.05, -0.9 - P/2, 3.15, P)
    draw_wall(13.05, -0.9 - P/2, 0.45, P)
    # Trung tâm: Vách phòng Tp. Quy (13.5 to 18.5) chừa cửa tại X = 14.8
    draw_wall(13.5, -0.9 - P/2, 1.3, P)
    draw_wall(15.65, -0.9 - P/2, 2.85, P)
    # Cánh Đông: Thư ký (19.8), Tp Tú Anh (23.8), Tp Nhi (28.2)
    draw_wall(18.5, -0.9 - P/2, 1.3, P)
    draw_wall(20.65, -0.9 - P/2, 3.15, P)
    draw_wall(24.65, -0.9 - P/2, 3.55, P)
    draw_wall(29.05, -0.9 - P/2, 2.95, P)

    # Vách ngăn phòng nội bộ Tòa 1
    # Dãy Bắc:
    draw_wall(4.5 - P/2, 0.9, P, 4.5)      # Tp Phương & Tp. Bình
    draw_wall(9.0 - P/2, 0.9, P, 4.5)      # Tp. Bình & Tp Đào
    draw_wall(13.5 - P/2, 0.9, P, 4.5)     # Tp Đào & Sảnh thang
    draw_wall(18.5 - P/2, 0.9, P, 4.5)     # Sảnh thang & Tp. Tồn
    draw_wall(22.5 - P/2, 0.9, P, 4.5)     # Tp. Tồn & Kho 1
    draw_wall(27.2 - P/2, 0.9, P, 4.5)     # Kho 1 & Kho 2

    # Dãy Nam:
    draw_wall(5.5 - P/2, -4.9, P, 4.0)     # Tp Thu & Tp Kiệt
    draw_wall(9.5 - P/2, -4.9, P, 4.0)     # Tp Kiệt & Tp Diễm
    draw_wall(13.5 - P/2, -4.9, P, 4.0)    # Tp Diễm & Tp. Quy
    draw_wall(18.5 - P/2, -4.9, P, 4.0)    # Tp. Quy & Thư ký
    draw_wall(22.5 - P/2, -4.9, P, 4.0)    # Thư ký & Tp Tú Anh
    draw_wall(27.0 - P/2, -4.9, P, 4.0)    # Tp Tú Anh & Tp Nhi

    # ==========================
    # === SẢNH NỐI & TÒA 2 (CÂN ĐỐI 2 BÊN, KHÔNG CÓ TƯỜNG THỪA) ===
    # ==========================
    # Vách cổ nối Tây (X = 13.5m, Y: 5.4 to 7.0)
    draw_wall(13.5 - P/2, 5.4, P, 1.6)

    # Vách cổ nối Đông (X = 18.5m, Y: 5.4 to 7.0)
    draw_wall(18.5 - P/2, 5.4, P, 1.6)

    # Vách ngăn Sảnh giữa với Phòng Xét xử (X = 13.5m, Y: 7.0 to 15.0) - CẮT KHOẢNG MỞ CỬA TẠI Y: 10.3 TO 11.7
    draw_wall(13.5 - P/2, 7.0, P, 3.3)
    draw_wall(13.5 - P/2, 11.7, P, 3.3)

    # (Vị trí X = 18.5m giữa Sảnh giữa và Sảnh chờ Đông hoàn toàn thông suốt, không có tường thừa)

    # --- TƯỜNG NGOẠI THẤT CÁNH TÂY TÒA 2 (PHÒNG XÉT XỬ) ---
    # Tường Nam Tây Tòa 2 (Y = 7.0 - W, X: 1.5 - W to 13.5)
    draw_wall(1.5 - W, 7.0 - W, 12.0 + W + P/2, W)
    # Tường Tây Tòa 2 (X = 1.5 - W, Y: 7.0 - W to 15.0 + W)
    draw_wall(1.5 - W, 7.0 - W, W, 8.0 + 2*W)
    # Tường Bắc Tây Tòa 2 (Y = 15.0m, X: 1.5 - W to 13.5 + P/2)
    draw_wall(1.5 - W, 15.0, 12.0 + W + P/2, W)

    # --- TƯỜNG NGOẠI THẤT CÁNH ĐÔNG TÒA 2 (SẢNH CHỜ XÉT XỬ) ---
    # Tường Nam Đông Tòa 2 (Y = 7.0 - W, X: 18.5 to 30.5 + W)
    draw_wall(18.5 - P/2, 7.0 - W, 12.0 + W + P/2, W)
    # Tường Đông Tòa 2 (X = 30.5m, Y: 7.0 - W to 15.0 + W)
    draw_wall(30.5, 7.0 - W, W, 8.0 + 2*W)
    # Tường Bắc Đông Tòa 2 (Y = 15.0m, X: 18.5 - P/2 to 30.5 + W)
    draw_wall(18.5 - P/2, 15.0, 12.0 + W + P/2, W)

    # --- TƯỜNG BẮC SẢNH XÉT XỬ TẦNG 2 (KHÉP KÍN LIÊN TỤC VÌ LÀ TẦNG TRÊN, KHÔNG CÓ BẬC THANG NGOẠI THẤT) ---
    draw_wall(13.5 - P/2, 15.0, 5.0 + P, W)

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

    # Windows on Tòa 1 North Wall (Y = 5.4m)
    draw_window(1.3, 5.4, 1.8, W, is_horizontal=True)
    draw_window(5.8, 5.4, 1.8, W, is_horizontal=True)
    draw_window(10.3, 5.4, 1.8, W, is_horizontal=True)
    draw_window(19.6, 5.4, 1.8, W, is_horizontal=True)
    draw_window(23.9, 5.4, 1.8, W, is_horizontal=True)
    draw_window(28.6, 5.4, 1.8, W, is_horizontal=True)

    # Windows on Tòa 1 South Wall (Y = -4.9m - W)
    draw_window(1.8, -4.9 - W, 2.0, W, is_horizontal=True)
    draw_window(6.6, -4.9 - W, 1.8, W, is_horizontal=True)
    draw_window(10.6, -4.9 - W, 1.8, W, is_horizontal=True)
    draw_window(15.0, -4.9 - W, 2.0, W, is_horizontal=True)  # Window for Tp. Quy (center room)
    draw_window(19.6, -4.9 - W, 1.8, W, is_horizontal=True)
    draw_window(23.8, -4.9 - W, 1.8, W, is_horizontal=True)
    draw_window(28.5, -4.9 - W, 1.8, W, is_horizontal=True)

    # Windows on Tòa 1 East/West end walls (Bao gồm cửa sổ 2 đầu hành lang per Spec Tầng 2)
    # Tường Tây:
    draw_window(-W, 2.2, W, 1.8, is_horizontal=False)
    draw_window(-W, -0.6, W, 1.2, is_horizontal=False)  # Cửa sổ đầu hành lang Tây
    draw_window(-W, -3.8, W, 1.8, is_horizontal=False)
    # Tường Đông:
    draw_window(X_MAX, 2.2, W, 1.8, is_horizontal=False)
    draw_window(X_MAX, -0.6, W, 1.2, is_horizontal=False)  # Cửa sổ đầu hành lang Đông
    draw_window(X_MAX, -3.8, W, 1.8, is_horizontal=False)

    # Windows on Tòa 2 (Khối xét xử & Sảnh chờ)
    # Tường Tây Tòa 2 (X = 1.5 - W)
    draw_window(1.5 - W, 8.5, W, 1.8, is_horizontal=False)
    draw_window(1.5 - W, 11.5, W, 1.8, is_horizontal=False)
    # Tường Nam Cánh Tây Tòa 2 (Y = 7.0 - W)
    draw_window(3.5, 7.0 - W, 2.2, W, is_horizontal=True)
    draw_window(8.5, 7.0 - W, 2.2, W, is_horizontal=True)
    # Tường Bắc Cánh Tây Tòa 2 (Y = 15.0m)
    draw_window(3.5, 15.0, 2.2, W, is_horizontal=True)
    draw_window(8.5, 15.0, 2.2, W, is_horizontal=True)

    # Tường Bắc Sảnh xét xử ở giữa (Y = 15.0m)
    draw_window(15.0, 15.0, 2.0, W, is_horizontal=True)

    # Tường Đông Tòa 2 (X = 30.5m)
    draw_window(30.5, 8.5, W, 1.8, is_horizontal=False)
    draw_window(30.5, 11.5, W, 1.8, is_horizontal=False)
    # Tường Nam Cánh Đông Tòa 2 (Y = 7.0 - W)
    draw_window(20.5, 7.0 - W, 2.2, W, is_horizontal=True)
    draw_window(25.5, 7.0 - W, 2.2, W, is_horizontal=True)
    # Tường Bắc Cánh Đông Tòa 2 (Y = 15.0m)
    draw_window(20.5, 15.0, 2.2, W, is_horizontal=True)
    draw_window(25.5, 15.0, 2.2, W, is_horizontal=True)

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
        elif dtype == 'DOUBLE_W':
            # Double door at X=13.5 opening westward into Courtroom
            leaf = dw / 2.0
            # North leaf
            ax.plot([hx - leaf, hx], [hy + leaf, hy + leaf], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_n = patches.Arc((hx, hy + leaf), leaf * 2, leaf * 2, angle=0, theta1=90, theta2=180, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc_n)
            # South leaf
            ax.plot([hx - leaf, hx], [hy - leaf, hy - leaf], color=COLOR_DOOR_SWING, linewidth=1.4, zorder=15)
            arc_s = patches.Arc((hx, hy - leaf), leaf * 2, leaf * 2, angle=0, theta1=180, theta2=270, color=COLOR_DOOR_SWING, linewidth=1.0, zorder=15)
            ax.add_patch(arc_s)

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
    # 10. EXPORT HIGH-RESOLUTION IMAGE
    # ---------------------------------------------------------
    plt.savefig(out_img_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Floorplan CaMau 9 Tầng 2 successfully generated at: {out_img_path}")

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    create_floorplan_tang2(script_dir)
