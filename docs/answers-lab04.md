# Câu hỏi thảo luận – Lab 04

## 1. Vì sao chuẩn bị phát hành (cập nhật `__version__`, `CHANGELOG.md`) trên `master` trước, không sửa trực tiếp trên nhánh `release/*`?
- Trong **Release Flow**, nhánh `release/*` chỉ được tách ra từ `master` để đóng băng baseline và **không bao giờ merge ngược lại vào `master`**.
- Nếu cập nhật `__version__ = "1.0.0"` và `CHANGELOG.md` trên nhánh `release/lab04`, nhánh `master` sẽ thiếu thông tin lịch sử phát hành `1.0.0` và phải cherry-pick ngược lại. Chuẩn bị trên `master` (qua PR `topic/prepare-release-1.0.0`) giúp cả `master` lẫn nhánh `release/lab04` mới tạo đều có chung lịch sử chuẩn xác.

## 2. Vì sao `release/*` không merge ngược vào `master`? So sánh với GitFlow.
- **Trong Release Flow**:
  - `master` luôn là nơi tích hợp mọi thay đổi trước hoặc thông qua cherry-pick từ hotfix.
  - `release/*` là dòng bảo trì (maintenance line) của một phiên bản cụ thể (ví dụ dòng `1.0.x`). Trên `release/lab04` sẽ có những commit riêng của dòng `1.0.x` (như `chore: bump version to 1.0.1`), trong khi `master` đã tiến lên `1.1.0`. Nếu merge cả nhánh `release/*` vào `master` sẽ gây xung đột số phiên bản và kéo theo các thay đổi đặc thù của bản cũ.
- **So sánh với GitFlow**:
  - **GitFlow** có 2 nhánh sống dài (`main` và `develop`), nhánh `release/*` tách từ `develop`, khi hoàn tất phải merge vào cả `main` (để gắn tag) lẫn `develop`. Quy trình này phức tạp hơn và dễ phát sinh xung đột khi duy trì song song nhiều phiên bản.
  - **Release Flow** chỉ có một nhánh tích hợp chính (`master`), các nhánh `release/*` tách ra một chiều từ `master` để đóng băng từng bản phát hành và bảo trì độc lập từng phiên bản song song.

## 3. Vì sao nâng phiên bản lên `1.0.0` mà không phải `0.4.0`?
- Theo quy ước **Semantic Versioning (SemVer)**:
  - Dải phiên bản `0.y.z` (`v0.1.0`, `v0.2.0`, `v0.3.0` ở Lab 01–03) dùng cho giai đoạn phát triển ban đầu (initial development), khi API và cấu trúc gói chưa ổn định.
  - Khi phần mềm đã hoàn thiện các chức năng cốt lõi (tạo giỏ hàng, thêm/xóa đĩa, in giỏ hàng, tìm kiếm, tính chiết khấu, có bộ kiểm thử đơn vị và tài liệu đầy đủ) và sẵn sàng công bố bản phát hành chính thức (baseline ổn định đầu tiên cho người dùng), phiên bản được nâng lên **`1.0.0`**.
