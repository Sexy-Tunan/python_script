#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
时间戳生成工具：将日期时间字符串转换为Unix时间戳
使用示例：
    python timestamp_utils.py 2021/1/2-00:00:00
"""

import sys
from datetime import datetime
import time


def parse_datetime(datetime_str):
    """
    解析日期时间字符串并返回Unix时间戳

    支持的格式：
    - 2021/1/2-00:00:00
    - 2021/1/2 00:00:00
    - 2021-1-2-00:00:00
    - 2021-1-2 00:00:00
    - 2021/01/02-00:00:00
    等
    """
    # 支持多种分隔符
    datetime_str = datetime_str.strip()

    # 尝试不同的日期时间格式
    formats = [
        "%Y/%m/%d-%H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%Y-%m-%d-%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y.%m.%d-%H:%M:%S",
        "%Y.%m.%d %H:%M:%S",
        "%Y/%m/%d",  # 只有日期，默认00:00:00
        "%Y-%m-%d",
        "%Y.%m.%d",
    ]

    # 处理双冒号的情况 (例如 00:00::00)
    datetime_str = datetime_str.replace("::", ":")

    for fmt in formats:
        try:
            dt = datetime.strptime(datetime_str, fmt)
            timestamp = int(dt.timestamp())
            return timestamp, dt
        except ValueError:
            continue

    return None, None


def main():
    if len(sys.argv) != 2:
        print("用法: python timestamp_gen.py <datetime>")
        print("\n支持的日期时间格式示例:")
        print("  python timestamp_gen.py 2021/1/2-00:00:00")
        print("  python timestamp_gen.py \"2021/1/2 00:00:00\"")
        print("  python timestamp_gen.py 2021-1-2-00:00:00")
        print("  python timestamp_gen.py \"2021-1-2 00:00:00\"")
        print("  python timestamp_gen.py 2021/1/2")
        print("\n输出: Unix时间戳（秒）")
        sys.exit(1)

    datetime_str = sys.argv[1]

    timestamp, dt = parse_datetime(datetime_str)

    if timestamp is None:
        print(f"错误：无法解析日期时间格式 '{datetime_str}'")
        print("\n请使用以下格式之一:")
        print("  - 2021/1/2-00:00:00")
        print("  - 2021/1/2 00:00:00")
        print("  - 2021-1-2-00:00:00")
        print("  - 2021-1-2 00:00:00")
        sys.exit(1)

    print(f"日期时间: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"时间戳: {timestamp}")


if __name__ == "__main__":
    main()