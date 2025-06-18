#!/usr/bin/env python3
"""
字体精简工具 v1.0
用法: 
  python font_minifier.py [输入字体] [字库文件] [输出字体]
示例:
  python font_minifier.py SourceHanSans.ttf my_chars.txt slim_font.otf
"""

import sys
from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter, Options

def extract_characters(char_file):
    """从字库文件中提取所有唯一字符"""
    with open(char_file, 'r', encoding='utf-8') as f:
        content = f.read()
    return set(content)

def create_font_subset(input_font, char_set, output_font):
    """创建字体子集并保存"""
    font = TTFont(input_font)
    
    # 配置子集化选项
    options = Options()
    options.drop_tables = []  # 保留所有必要表
    options.name_IDs = ['*']  # 保留所有字体名称信息
    options.name_legacy = True
    options.glyph_names = True
    
    # 执行子集化
    subsetter = Subsetter(options=options)
    subsetter.populate(text=''.join(char_set))  # 设置要保留的字符
    subsetter.subset(font)
    
    # 保存精简后的字体
    font.save(output_font)
    print(f"精简字体已保存至: {output_font}")
    print(f"原始大小: {round(len(font.reader.file.getvalue())/1024)} KB")
    
    # 清理临时文件
    font.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("参数错误！正确格式:")
        print("python font_minifier.py <输入字体> <字库文件> <输出字体>")
        sys.exit(1)
    
    input_font = sys.argv[1]
    char_file = sys.argv[2]
    output_font = sys.argv[3]
    
    try:
        char_set = extract_characters(char_file)
        print(f"成功读取字库: {len(char_set)} 个字符")
        create_font_subset(input_font, char_set, output_font)
    except Exception as e:
        print(f"处理失败: {str(e)}")
        sys.exit(1)