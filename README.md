# AIMS-mini

Ứng dụng mẫu cho chuỗi bài thực hành **Quản lý cấu hình phần mềm (SCM) với Git & GitHub** – Học phần **IT3180 (Nhập môn Công nghệ phần mềm)**.

## Thông tin sinh viên
- **Họ và tên**: Lê Đức Dương
- **MSSV**: 202416174
- **Email**: leducduong20gg@gmail.com

## Yêu cầu hệ thống
- **Python**: `>= 3.10` (chỉ sử dụng thư viện chuẩn của Python và `unittest`)
- **Git**: `>= 2.40`

## Cấu trúc dự án

```text
it3180-202416174-aims/
├── .github/
│   ├── pull_request_template.md   # Mẫu mô tả Pull Request chuẩn
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI tự động chạy unittest
├── aims/
│   ├── __init__.py                # Định nghĩa gói aims và __version__
│   ├── cart.py                    # Lớp Cart (thêm, xóa, in giỏ hàng, chiết khấu, sắp xếp)
│   ├── dvd.py                     # Lớp DigitalVideoDisc
│   └── search.py                  # Các hàm tìm kiếm search_by_title, search_by_category
├── docs/
│   ├── use-case.md                # Biểu đồ Use Case (Mermaid)
│   ├── answers-lab01.md           # Câu hỏi thảo luận Lab 01
│   ├── answers-lab02.md           # Câu hỏi thảo luận Lab 02
│   ├── answers-lab03.md           # Câu hỏi thảo luận Lab 03
│   ├── answers-lab04.md           # Câu hỏi thảo luận Lab 04
│   └── answers-lab05.md           # Câu hỏi thảo luận Lab 05
├── tests/
│   ├── __init__.py
│   ├── test_cart.py               # Unit tests cho lớp Cart
│   └── test_search.py             # Unit tests cho mô-đun search
├── CHANGELOG.md                   # Nhật ký thay đổi theo chuẩn Keep a Changelog
├── README.md                      # Tài liệu hướng dẫn dự án
└── main.py                        # Chương trình chạy thử nghiệm (Demo)
```

## Hướng dẫn chạy chương trình & kiểm thử

### 1. Chạy chương trình chính
```bash
python main.py
```
Kết quả đầu ra mẫu:
```text
AIMS-mini v1.1.0
Đã thêm đĩa vào giỏ hàng
Đã thêm đĩa vào giỏ hàng
Đã thêm đĩa vào giỏ hàng
***********************CART***********************
1. DVD - The Lion King - Animation - Roger Allers - 87: 19.95 $
2. DVD - Star Wars - Science Fiction - George Lucas - 87: 24.95 $
3. DVD - Aladdin - Animation -  - 0: 18.99 $
Total cost: 63.89 $
**************************************************
Total cost: 63.89 $
```

### 2. Chạy bộ kiểm thử đơn vị (Unit Tests)
```bash
python -m unittest discover -s tests -v
```

## Các nhánh phát hành (Release Branches) & Tags
| Bài thực hành | Nhánh nộp bài | Tag (Baseline) | Nội dung chính |
| :--- | :--- | :--- | :--- |
| **Lab 01** | `release/lab01` | `v0.1.0` | Thiết lập môi trường, `.gitignore`, Refactor flow (`git mv` vào gói `aims/`) |
| **Lab 02** | `release/lab02` | `v0.2.0` | Feature/Topic flow, PR template, 3 kiểu merge (Merge commit, Squash, Rebase) |
| **Lab 03** | `release/lab03` | `v0.3.0` | Bugfix flow (từ `master` & `feature/*`), giải quyết Merge Conflict, `git revert -m 1` |
| **Lab 04** | `release/lab04` | `v1.0.0`, `v1.0.1` | Semantic Versioning, `CHANGELOG.md`, đóng băng baseline & Hotfix `1.0.1` |
| **Lab 05** | `release/lab05` | `v1.1.0` | Hotfix flow, lan truyền bản vá đa phiên bản với `git cherry-pick -x`, CI workflow |
