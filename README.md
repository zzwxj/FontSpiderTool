# 利用python的fonttools库精简字体文件

1.安装依赖
pip install fonttools

（fonttools后续更新指令）python.exe -m pip install --upgrade pip

2.字库txt

3.运行命令
python font_minifier.py [输入字体] [字库文件] [输出字体]
例如：python font_minifier.py original.ttf my_chars.txt slim_font.otf

注意事项
1.字库文件必须使用UTF-8编码

2.支持TTF/OTF输入输出，输出格式自动匹配扩展名

3.保留所有字体元信息（名称、版权等）

4.处理超大字体时可能需要增加内存
