# Câu hỏi thảo luận – Lab 02

## 1. Vì sao phải đồng bộ `master` vào nhánh tính năng trước khi gửi/hoàn tất PR?
- Khi phát triển song song, nhánh `master` có thể đã tiến thêm các commit mới từ các PR khác (ví dụ PR `feature/cart-print` đã được merge trước).
- Việc đồng bộ `origin/master` vào nhánh tính năng (`feature/search-by-title`) trước khi merge PR giúp:
  1. Phát hiện và giải quyết xung đột (nếu có) ngay trên nhánh tính năng thay vì làm hỏng `master`.
  2. Kiểm thử tích hợp (`python main.py` / chạy bộ test) trên mã nguồn kết hợp mới nhất để đảm bảo tính năng mới hoạt động đúng cùng các thay đổi vừa có trên `master`.

## 2. Khi nào không được dùng `git rebase`?
- **Quy tắc vàng của Rebase**: Không bao giờ `rebase` các commit đã được chia sẻ công khai mà người khác đang dựa vào để làm việc (đặc biệt là các nhánh dùng chung như `master`, `release/*`, hoặc nhánh tính năng có nhiều người cùng commit).
- Lý do: `rebase` viết lại lịch sử bằng cách tạo các commit mới với mã băm (SHA) mới. Nếu nhánh đã chia sẻ bị rebase, lịch sử của các thành viên khác sẽ bị lệch (diverged), gây trùng lặp commit hoặc mất thay đổi khi đồng bộ.

## 3. Nhánh `feature/*` khác nhánh `topic/*` ra sao?
- **`feature/*`**: Dùng cho việc phát triển **tính năng nghiệp vụ mới** của sản phẩm có tác động trực tiếp đến hành vi phần mềm/người dùng (ví dụ: `feature/cart-print`, `feature/search-by-title`).
- **`topic/*`**: Dùng cho các công việc **phi chức năng hoặc hỗ trợ kỹ thuật/tài liệu/quy trình** như bổ sung tài liệu, biểu đồ thiết kế, cấu hình PR template, cấu hình CI/CD, hoặc chuẩn bị thông tin phát hành (ví dụ: `topic/pr-template`, `topic/use-case-diagram`, `topic/prepare-release-1.0.0`, `topic/ci-unit-tests`).
