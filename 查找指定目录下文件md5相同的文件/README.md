# 版本说明

无需安装 openpyxl 第三方库，输出的结果文件格式为.csv格式
但缺点是无法在代码中设置列宽，通过excel打开之后需要手动设置列宽才能有一个好的观看体验



而普通版本需要安装openpyxl 第三方库，输出结果为.xlsx格式

> pip install openpyxl

优点，查看时无需手动设置列宽



# 使用示例

两个版本都一样

`python xxxx.py target-dir output-dir`

其中结果的输出路径不一定需要指定

- 如果有，如果有则在此路径下创建名为 "'same_file_in_' + 指定目录名"的csv/xlsx文件并输出结果；_
- 如果没有则在与指定目录相同层级的位置创建 名为 "'same_file_in_' + 指定目录名"的csv/xlsx文件并输出结果