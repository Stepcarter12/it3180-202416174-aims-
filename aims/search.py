def search_by_category(items, category):
    """Tìm danh sách đĩa DVD theo thể loại (không phân biệt hoa thường)."""
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]


def search_by_title(items, keyword):
    """Tìm danh sách đĩa DVD theo tiêu đề."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
