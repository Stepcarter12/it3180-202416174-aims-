# Câu hỏi thảo luận – Lab 03

## 1. Merge base là gì? Vai trò của nó trong 3-way merge?
- **Merge base** là tổ tiên chung gần nhất (nearest common ancestor) của hai nhánh cần hợp nhất.
- Trong thuật toán **3-way merge**, Git so sánh 3 phiên bản:
  1. `BASE` (merge base – tổ tiên chung),
  2. `OURS` / `HEAD` (nhánh đích hiện tại),
  3. `THEIRS` (nhánh nguồn cần hợp nhất).
- Nếu một dòng chỉ thay đổi ở một phía so với `BASE`, Git tự động chọn phía có thay đổi. Nếu cả hai phía cùng sửa một vùng khác nhau so với `BASE`, Git báo **Merge conflict** để lập trình viên quyết định.

## 2. Vì sao trên nhánh `master` và `release/*` phải dùng `git revert` thay vì `git reset`?
- **`git reset`** dời con trỏ nhánh lùi về commit cũ, tức là **viết lại lịch sử (rewrite history)**. Trên các nhánh dùng chung (`master`, `release/*`), việc viết lại lịch sử bị chặn bởi Branch Protection (`force push` bị cấm) và sẽ làm hỏng lịch sử của các thành viên khác đã pull trước đó.
- **`git revert`** tạo ra một **commit mới** có nội dung đảo ngược chính xác các thay đổi của commit/merge cần hủy. Lịch sử tiến về phía trước một cách minh bạch, đi qua quy trình Pull Request + Review + CI đầy đủ và hoàn toàn an toàn cho các nhánh chia sẻ.
