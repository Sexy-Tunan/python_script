# 版本说明

而都需要安装openpyxl 第三方库，输出结果为.xlsx格式

> pip install openpyxl





## v2版本

增加了重复文件数量显示

## v3版本

在v2版本基础上增加了图片预览图输出

特别的还需要安装 pillow第三方库

# 使用示例

两个版本都一样

`python xxxx.py target-dir output-dir`

其中结果的输出路径不一定需要指定

- 如果有，如果有则在此路径下创建名为 "'same_file_in_' + 指定目录名"的csv/xlsx文件并输出结果；_
- 如果没有则在与指定目录相同层级的位置创建 名为 "'same_file_in_' + 指定目录名"的csv/xlsx文件并输出结果