# AI CODE REVIEWER

[English](README.md)/中文

## 前言

本项目旨在介绍AI自动评审代码的重要性。代码评审作为日常开发工作中不可或缺的一环，利用AI技术赋能自动评审代码可以提升开发效率。AI可帮助检测代码潜在错误，评估代码整体质量，并提供具体的改进建议。

## 使用准备

本项目适用于GitLab平台，使用前需要准备以下材料：OPENAI密钥、GitLab链接和GitLab令牌。

### 步骤一：安装项目依赖

运行以下命令安装项目依赖：

```bash
pip install -r requirements.txt
```

### 步骤二：配置基础设置

将OPENAI密钥、GitLab链接和令牌配置到环境变量中：

```bash
export OPENAI_API_KEY=your_openai_api_key
export GITLAB_URL=your_gitlab_url
export GITLAB_PRIVATE_TOKEN=your_gitlab_private_token
```

### 步骤三：可选设置代理

如果GitLab位于内网环境中，需额外添加代理设置到环境变量中：

```bash
export GITLAB_PROXY=http://your_proxy_server:port
```

### 步骤四：执行AI代码审查

执行以下命令进行AI代码审查：

```bash
python review_script.py <project_id> <merge_request_id>
```

## 效果演示

让我们通过以下Python代码片段演示代码审查：

```python
a = 1/0
```

### 审查结果

代码中存在一个明显的错误，即尝试进行除以零的操作（`a = 1/0`），这会导致运行时错误（ZeroDivisionError）。为避免此类错误，建议加入适当的异常处理，例如使用 try-except 语句来捕获和处理这种错误。由于缺乏其他上下文信息（如函数签名、全局数据结构等），无法评估其他方面（如性能优化、安全实践、错误处理机制完整性、代码质量和错误检测）。

建议的修改是加入异常处理：

```python
try:
    a = 1/0
except ZeroDivisionError:
    print("不能除以零！")
    # 在此处可以添加其他适当的错误处理逻辑
```

综上所述，由于存在未处理的运行时错误（除以零操作），该代码不符合安全和稳定的编程实践。建议加入适当的错误处理机制以优化代码质量和健壮性。

## 使用场景

通过在GitLab项目中设置Webhook，实现对合并请求（Merge Request）进行代码的AI自动评审。

## 反馈

如在使用过程中遇到任何问题或有任何建议，请随时与我们交流。
