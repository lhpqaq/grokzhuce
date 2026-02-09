#!/usr/bin/env python3
"""从 email:password:sso 格式文件中提取纯 SSO"""
import sys

def extract_sso(input_file, output_file):
    """读取完整格式文件，提取SSO并写入新文件"""
    count = 0
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            if not line:
                continue
            parts = line.split(':')
            if len(parts) >= 3:
                # 取最后一部分（可能包含多个冒号）
                sso = ':'.join(parts[2:])
                f_out.write(sso + '\n')
                count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python extract_sso.py <输入文件> [输出文件]")
        print("示例: python extract_sso.py grok_full.txt grok_sso.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.txt', '_sso.txt')
    
    try:
        count = extract_sso(input_file, output_file)
        print(f"[✓] 提取完成: {count} 个 SSO -> {output_file}")
    except Exception as e:
        print(f"[-] 错误: {e}")
        sys.exit(1)
