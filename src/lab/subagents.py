"""GUIDE Phần 1 - Định nghĩa subagent (tác tử con).   >>> SINH VIÊN CÀI ĐẶT <<<

Pseudo-code: guides/pseudocode/02_subagents.md
Kiểm tra:    pytest tests/test_02_agent.py
"""


def get_subagents() -> list[dict]:
    """Trả về danh sách subagent (ít nhất 2, tên khác nhau).

    Mỗi phần tử là một dict có các khóa bắt buộc:
      "name":          tên duy nhất (chữ thường, có thể có dấu gạch ngang)
      "description":   khi nào tác tử chính nên giao việc cho subagent này (viết như một hướng dẫn hành động)
      "system_prompt": chỉ dẫn cho subagent
    Gợi ý vai trò: explorer (đọc và báo cáo), implementer (thực hiện), reviewer (kiểm tra độc lập).
    """
    return [
        {
            "name": "explorer",
            "description": "Delegate when you need an independent inventory of files, tests, or requirements before editing.",
            "system_prompt": (
                "Inspect the task carefully and report relevant files, constraints, and likely causes. "
                "Do not make changes unless explicitly asked."
            ),
        },
        {
            "name": "implementer",
            "description": "Delegate non-trivial implementation work after the relevant requirements and files are understood.",
            "system_prompt": (
                "Implement the requested change in the workspace. Run focused checks, keep changes minimal, "
                "and report exactly what changed and what was verified."
            ),
        },
        {
            "name": "reviewer",
            "description": "Delegate an independent review after editing to find missed requirements and run relevant tests.",
            "system_prompt": (
                "Review the current workspace against the task instructions and tests. "
                "Identify concrete defects and fix them when appropriate, then report verification."
            ),
        },
    ]
