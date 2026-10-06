# Báo cáo Lab: Self evolving Agentic

## 1. Thông tin nhóm và cấu hình

| Họ tên | Mã sinh viên | Phần đóng góp |
|---|---|---|
| Nguyễn Huy Cường | 2A202602842 | Hoàn thiện agent harness, subagents, runner và curator |

- Cấu hình mô hình: chưa chạy thí nghiệm online trong môi trường này; không commit khóa API.
- Kiểm thử ngoại tuyến: Python hiện hành trên Windows, Deep Agents theo `pyproject.toml`.
- Kết quả kiểm thử: `32 passed`.

## 2. Giả thuyết

- H1: `subagents` có thể đạt điểm cao hơn `baseline` trên các tác vụ cần phân tích nhiều bước, nhưng sẽ tốn thêm token.
- H2: `skills-auto` chỉ cải thiện khi skill tổng quát và đúng; skill tự sinh có thể không chuyển giao tốt sang tập đánh giá.
- H3: tác vụ học có thể đạt điểm cao hơn tác vụ đánh giá do tác vụ đánh giá có dữ liệu và quy ước mới.

## 3. Làm quen Deep Agents

1. Backend tách sandbox khỏi workspace gốc và cung cấp file tools cùng shell tools.
2. `subagents` được mô tả bằng tên, hướng dẫn giao việc và system prompt riêng.
3. Skill được nạp theo yêu cầu, còn runner ghi trace, token, tool calls và điểm kiểm tra.

## 4-7. Thí nghiệm

Các lần chạy mô hình thật chưa được thực hiện vì repository không kèm API key. Do đó không ghi số liệu giả; bảng hiện tại chỉ xác nhận không có kết quả online để tổng hợp.

## 8. Phân tích

Phần phân tích định lượng cần được hoàn thiện sau khi chạy `baseline`, `subagents` và `skills-auto` trên cả tập học và tập đánh giá theo hướng dẫn trong `GUIDE.md`.

## 9. Hạn chế và tính hợp lệ

1. Chưa có provider/model và API key trong môi trường thực thi, nên chưa thể đo token, thời gian và điểm của tác vụ thật.
2. Các test hiện có là test ngoại tuyến với scripted model, không đại diện cho chất lượng của một LLM cụ thể.
3. Kết quả thực nghiệm phụ thuộc model, temperature và số lần chạy; cần chạy lại với cùng cấu hình để so sánh công bằng.

## 10. Kết luận

Bốn module TODO đã được cài đặt theo pseudo-code và toàn bộ test ngoại tuyến đạt `32/32`. Backend cũng tương thích các lệnh POSIX của lab trên Windows thông qua Git Bash mà không kế thừa biến môi trường nhạy cảm. Bước tiếp theo là cấu hình model có tool calling và chạy quy trình thực nghiệm đầy đủ.

## Phụ lục

- `python -m pip install -e .`
- `python -m pytest -q`
- `python scripts/check_breakdown.py`
