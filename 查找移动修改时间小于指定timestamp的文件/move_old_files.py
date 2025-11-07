#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件移动脚本：根据时间戳将旧文件移动到新目录
使用示例：
    # 基本用法（自动生成目标目录）
    python move_old_files.py <timestamp> <folder_path>

    # 指定目标目录
    python move_old_files.py <timestamp> <folder_path> <target_dir>

    # 示例：移动2023年11月7日之前的文件（自动生成res2、res3等目录）
    python move_old_files.py 1699344000 ./res

    # 示例：移动到指定目录
    python move_old_files.py 1699344000 ./res ./backup_res
"""

import os
import sys
import shutil
from pathlib import Path


def find_available_target_dir(source_dir):
    """
    查找可用的目标目录名称（原名+数字，从2开始递增）
    
    Args:
        source_dir: 源目录路径（Path对象）
    
    Returns:
        可用的目标目录路径（Path对象）
    """
    counter = 2
    while True:
        target_dir = source_dir.parent / (source_dir.name + str(counter))
        if not target_dir.exists():
            return target_dir
        counter += 1


def move_old_files(timestamp, folder_path, target_dir_path=None):
    """
    将修改时间小于指定时间戳的文件移动到新目录

    Args:
        timestamp: Unix时间戳（秒）
        folder_path: 要扫描的文件夹路径
        target_dir_path: 目标目录路径（可选，如果不指定则自动生成）
    """
    # 转换为绝对路径
    source_dir = Path(folder_path).resolve()

    if not source_dir.exists():
        print(f"错误：目录不存在 - {source_dir}")
        return

    if not source_dir.is_dir():
        print(f"错误：路径不是一个目录 - {source_dir}")
        return

    # 确定目标目录
    if target_dir_path:
        # 用户指定了目标目录
        target_dir = Path(target_dir_path).resolve()
        if target_dir.exists():
            print(f"错误：目标目录已存在 - {target_dir}")
            print(f"请指定一个不存在的目录，或者不指定目标目录以自动生成")
            return
    else:
        # 自动生成目标目录（原名+数字，从2开始递增）
        target_dir = find_available_target_dir(source_dir)

    # 收集需要移动的文件
    files_to_move = []

    print(f"正在扫描目录: {source_dir}")
    print(f"目标目录: {target_dir}")
    print(f"时间戳阈值: {timestamp}")

    # 遍历所有文件
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = Path(root) / file
            try:
                # 获取文件的修改时间
                file_mtime = os.path.getmtime(file_path)

                # 如果修改时间小于指定的timestamp
                if file_mtime < float(timestamp):
                    files_to_move.append(file_path)

            except Exception as e:
                print(f"警告：无法读取文件 {file_path} 的修改时间: {e}")

    # 如果没有找到需要移动的文件
    if not files_to_move:
        print(f"没有找到修改时间小于 {timestamp} 的文件")
        return

    print(f"\n找到 {len(files_to_move)} 个文件需要移动")

    # 移动文件
    moved_count = 0
    for file_path in files_to_move:
        try:
            # 计算相对路径
            relative_path = file_path.relative_to(source_dir)

            # 目标文件路径
            target_path = target_dir / relative_path

            # 创建目标目录（如果不存在）
            target_path.parent.mkdir(parents=True, exist_ok=True)

            # 移动文件
            shutil.move(str(file_path), str(target_path))
            print(f"已移动: {relative_path}")
            moved_count += 1

        except Exception as e:
            print(f"错误：移动文件 {file_path} 失败: {e}")

    print(f"\n完成！成功移动 {moved_count} 个文件到 {target_dir}")


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("用法: python move_old_files.py <timestamp> <folder_path> [target_dir]")
        print("\n示例:")
        print("  # 自动生成目标目录（res2, res3等）")
        print("  python move_old_files.py 1699344000 ./res")
        print("\n  # 指定目标目录")
        print("  python move_old_files.py 1699344000 ./res ./backup_res")
        print("\n说明:")
        print("  timestamp   - Unix时间戳（秒），文件修改时间小于此值将被移动")
        print("  folder_path - 要扫描的文件夹路径")
        print("  target_dir  - 目标目录路径（可选）")
        print("                如果不指定，将自动生成'原目录名+数字'的目录")
        print("                数字从2开始递增，直到找到不存在的目录名")
        sys.exit(1)

    timestamp = sys.argv[1]
    folder_path = sys.argv[2]
    target_dir = sys.argv[3] if len(sys.argv) == 4 else None

    try:
        # 验证timestamp是否为有效数字
        float(timestamp)
    except ValueError:
        print(f"错误：timestamp必须是一个数字，当前值: {timestamp}")
        sys.exit(1)

    move_old_files(timestamp, folder_path, target_dir)


if __name__ == "__main__":
    main()