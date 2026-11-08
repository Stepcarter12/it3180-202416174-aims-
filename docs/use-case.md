# Biểu đồ Use Case – AIMS-mini

```mermaid
flowchart LR
    Customer(["Khách hàng (Customer)"])
    UC1(["Xem giỏ hàng (print_cart)"])
    UC2(["Thêm DVD vào giỏ (add_dvd)"])
    UC3(["Xóa DVD khỏi giỏ (remove_dvd)"])
    UC4(["Tìm kiếm DVD theo tiêu đề (search_by_title)"])
    UC5(["Tính tổng tiền (total_cost)"])

    Customer --> UC1
    Customer --> UC2
    Customer --> UC3
    Customer --> UC4
    Customer --> UC5
```
