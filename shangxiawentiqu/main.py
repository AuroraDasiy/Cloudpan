import json
from datetime import datetime
import re


def format_timestamp(timestamp):
    if timestamp:
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return '未知时间'


def process_content(content):
    # 保留 Markdown 格式
    # 处理 LaTeX 公式
    content = re.sub(r'\$\$(.*?)\$\$', r'\\[\1\\]', content)  # 处理行间公式
    content = re.sub(r'\$(.*?)\$', r'\\(\1\\)', content)  # 处理行内公式
    return content


def format_chat(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    formatted_chat = []

    messages = data.get('messages', [])

    for message in messages:
        author = message.get('author', {})
        role = author.get('role')
        content = message.get('content', {}).get('parts', [''])[0]
        timestamp = message.get('create_time')

        processed_content = process_content(content)

        if role == 'user':
            formatted_message = f"用户 ({format_timestamp(timestamp)}):\n\n{processed_content}\n"
        elif role == 'assistant':
            formatted_message = f"GPT ({format_timestamp(timestamp)}):\n\n{processed_content}\n"
        elif role == 'tool':
            tool_name = author.get('name', '未知工具')
            formatted_message = f"{tool_name} ({format_timestamp(timestamp)}):\n\n{processed_content}\n"
        else:
            continue  # 跳过系统消息或其他不相关的消息

        formatted_chat.append(formatted_message)

    return "\n".join(formatted_chat)


# 使用示例
if __name__ == "__main__":
    json_file = "对话1.json"
    formatted_conversation = format_chat(json_file)
    print(formatted_conversation)