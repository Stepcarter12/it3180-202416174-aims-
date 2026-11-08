# Changelog

Mọi thay đổi đáng chú ý của dự án AIMS-mini được ghi nhận tại tệp này.
Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
và dự án tuân thủ [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-11-08
### Added
- `Cart.print_cart()` hiển thị chi tiết giỏ hàng và xử lý giỏ hàng trống.
- `search_by_title()` tìm kiếm đĩa DVD theo tiêu đề trong `aims/search.py`.
- `Cart.total_cost_with_discount()` tính tổng tiền sau chiết khấu kèm kiểm tra phần trăm hợp lệ.
- Bộ kiểm thử đơn vị `unittest` cho `Cart` và `search` trong thư mục `tests/`.
- Biểu đồ Use Case (`docs/use-case.md`) và mẫu Pull Request (`.github/pull_request_template.md`).

### Fixed
- Sửa lỗi giới hạn giỏ hàng nhận đĩa thứ 21 vượt quá `MAX_NUMBERS_ORDERED = 20` (#6).
- Sửa công thức tính tiền sau giảm giá và kiểm tra biên `0 <= percent <= 100`.
