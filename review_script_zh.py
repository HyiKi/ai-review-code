import review

PROMPT = """
以下是供审查的合并请求中的代码片段。 请根据以下标准评估代码：

语法和风格：检查是否有任何语法错误或与标准编码约定的偏差。 突出显示任何不符合该语言的可读性和可维护性最佳实践的代码行。
性能优化：确定代码中可以优化以获得更好性能的任何部分。 建议可以提高效率的具体更改，例如优化循环、降低计算复杂性或最小化内存使用量。
安全实践：扫描代码中常见的安全漏洞，例如 SQL 注入、跨站点脚本 (XSS) 或对用户输入的不当处理。 在适用的情况下推荐安全编码实践。
错误处理：评估代码是否有正确的错误处理机制。 指出任何可能破坏程序执行流程的潜在未处理异常或错误。
代码质量：评估代码的整体质量。 寻找代码异味、不必要的复杂性或可以简化或重构的冗余代码。
错误检测：分析代码是否存在可能导致错误行为的潜在错误或逻辑错误。 解释任何已发现的问题并提出修复建议。
我希望你能在 100 字之内简洁地总结一下差异。 如果适用，您的摘要应包含有关导出函数签名、全局数据结构和变量的更改以及可能影响代码的外部接口或行为的任何更改的注释。
确保您的反馈清晰、简洁且可操作，并尽可能提供具体的改进建议，改进建议使用中文回答。
顺便说一句，如果代码问题不是太大，你只需要回答“LGTM”。

代码：
"""

if __name__ == "__main__":
    review.main(PROMPT)
