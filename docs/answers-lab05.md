# Câu hỏi thảo luận – Lab 05

## 1. Ưu, nhược điểm của "Upstream First" (sửa trên `master` trước rồi cherry-pick về `release/*`) so với "Release First" (sửa trên `release/*` trước rồi cherry-pick về `master`)?
- **Release First (như trong học phần – tạo `hotfix/*` từ `release/lab04`)**:
  - **Ưu điểm**: Bản vá được viết và kiểm thử trực tiếp trên đúng môi trường/mã nguồn của phiên bản đang gặp lỗi (`v1.0.0`), đảm bảo không vô tình phụ thuộc vào hàm hoặc cấu trúc mới chỉ có trên `master` (`v1.1.0`), giúp phát hành bản vá khẩn cấp (`v1.0.1`) nhanh và an toàn nhất.
  - **Nhược điểm**: Nếu quên cherry-pick về `master`, lỗi sẽ tái xuất hiện (regression) ở các bản phát hành tương lai.
- **Upstream First (như Microsoft Release Flow – sửa trên `master` trước rồi cherry-pick về `release/*`)**:
  - **Ưu điểm**: Đảm bảo `master` luôn có bản sửa lỗi đầu tiên, không bao giờ xảy ra tình trạng lỗi đã sửa ở bản cũ nhưng lại tái phát ở bản mới.
  - **Nhược điểm**: Khi `master` đã thay đổi nhiều so với nhánh `release/*` cũ, việc cherry-pick ngược từ `master` về `release/*` dễ gặp xung đột hoặc kéo theo các phụ thuộc mới không tồn tại ở bản cũ.

## 2. Vì sao ở Phần A khi tạo `release/lab05` lại chưa gắn tag `v1.1.0` ngay?
- Tag phát hành (`v1.1.0`) là bất biến (immutable) – một khi đã gắn và đẩy lên remote thì không được xóa hay di chuyển.
- Nhánh `release/lab05` vừa tách ra đang ở giai đoạn đóng băng/kiểm thử trước phát hành (release candidate). Khi phát hiện lỗi `search_by_title` ảnh hưởng cả `release/lab05`, ta có thể cherry-pick bản vá vào `release/lab05` rồi mới gắn tag `v1.1.0`. Nếu đã gắn tag `v1.1.0` từ trước thì không thể sửa lại `v1.1.0` mà buộc phải phát hành thêm bản vá `v1.1.1`.

## 3. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện ra?
- Có thể phát hiện ngay bằng các lệnh kiểm toán cấu hình (Configuration Audit) ở Phần F:
  1. `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`: Sẽ chỉ thấy **1** bản cherry-pick (trên `master`) thay vì **2** bản (`master` và `release/lab05`).
  2. `git cherry -v origin/release/lab05 origin/release/lab04`: Commit `fix: make search_by_title case-insensitive` sẽ mang dấu **`+`** (chưa có bản tương đương trong `release/lab05`) thay vì dấu **`-`**.
  3. Vòng lặp kiểm tra hành vi thực tế (`for ref in v1.0.1 v1.1.0 master; do ...`): Tại `v1.1.0` (hoặc `release/lab05`) sẽ in ra **`0`** thay vì **`1`**.
