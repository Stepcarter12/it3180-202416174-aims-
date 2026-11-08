# Câu hỏi thảo luận – Lab 01

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **`--global`**: Được lưu tại tệp `~/.gitconfig` (hoặc `~/.config/git/config`, trên Windows là `C:\Users\<User>\.gitconfig`). Cấu hình này áp dụng mặc định cho **mọi kho chứa (repository)** của người dùng hiện tại trên máy tính.
- **`--local`**: Được lưu tại tệp `.git/config` bên trong thư mục của từng repository cụ thể. Cấu hình `--local` chỉ áp dụng cho kho chứa đó và có **độ ưu tiên cao hơn** `--global` (ghi đè giá trị `--global` nếu trùng khóa cấu hình).

## 2. Vì sao dùng `git mv` thay vì xóa tệp cũ và tạo tệp mới?
- `git mv <nguồn> <đích>` thực hiện đồng thời việc di chuyển/đổi tên tệp trênWorking Directory và cập nhật ngay trạng thái `renamed` trong Staging Area (Index).
- Nhờ đó, Git nhận diện rõ đây là thao tác đổi tên/di chuyển một Configuration Item (tương đồng 100% nội dung) thay vì xóa tệp cũ + thêm tệp mới rời rạc, giúp bảo toàn mạch lịch sử khi truy vết bằng `git log --follow -- aims/cart.py` và giúp người review PR thấy rõ `renamed` trong tab *Files changed*.

## 3. Nhánh `release/lab01` có phải là một baseline không?
- **Có.** Trong quản lý cấu hình phần mềm (SCM), `release/lab01` đóng vai trò là một **Baseline** (cơ sở cấu hình đã được nghiệm thu/chốt tại thời điểm kết thúc Lab 01 để giao nộp).
- Mọi thay đổi tiếp theo ở các bài thực hành sau diễn ra trên các nhánh mới tách từ `master`, không làm xáo trộn trạng thái đã chốt trên `release/lab01`.

## 4. Vì sao không commit thẳng lên `master` dù chỉ làm một mình?
- Tuân thủ nguyên tắc **Kiểm soát thay đổi (Change Control)** và **Release Flow**: `master` luôn đại diện cho nhánh tích hợp ổn định.
- Làm việc trên nhánh riêng (`refactor/*`, `feature/*`, `bugfix/*`) và đưa vào `master` qua Pull Request giúp:
  1. Cô lập các thay đổi đang phát triển dở dang khỏi nhánh chính.
  2. Có bước tự kiểm tra (self-review) hoặc đồng đội review, chạy CI test trước khi tích hợp.
  3. Dễ dàng truy vết mục đích của cụm thay đổi và hoàn tác (revert) cả PR nếu phát sinh lỗi.
