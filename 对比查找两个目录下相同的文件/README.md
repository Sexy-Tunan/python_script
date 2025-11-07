# 游戏资源文件对比工具

这是一个用于对比两个文件夹中内容相同但名称不同的文件的Python工具。通过计算文件的MD5值来匹配国内版本和国外版本的美术资源文件。

## 功能特点

- 🔍 深度遍历文件夹（包括所有子文件夹）
- 🔐 通过MD5值精确匹配文件内容
- 📊 输出格式化的Excel对比报告
- ⚡ 大文件友好（分块读取，不占用过多内存）
- 📝 显示相对路径，方便查看
- 🎨 Excel表格带样式，易于阅读

## 安装依赖

```bash
pip install openpyxl
```

## 使用方法

### 基本用法

```bash
python compare_resources.py <目录1路径> <目录2路径> <输出Excel路径>
```

### 示例

```bash
# 示例1: 对比CN和EN文件夹
python compare_resources.py D:/assets/cn D:/assets/en D:/output/contrast.xlsx

# 示例2: 带空格的路径需要用引号包裹
python compare_resources.py "C:/Game/Resources/CN" "C:/Game/Resources/EN" "C:/output/result.xlsx"

# 示例3: 相对路径
python compare_resources.py ./resources_cn ./resources_en ./contrast.xlsx
```

### 参数说明

- **第一个参数**: 第一个文件夹路径（例如：国内版本资源文件夹）
- **第二个参数**: 第二个文件夹路径（例如：国外版本资源文件夹）
- **第三个参数**: 输出的Excel文件路径（会自动添加.xlsx扩展名如果没有的话）

## 输出说明

生成的Excel文件包含以下列：

| 列名 | 说明 |
|------|------|
| 序号 | 匹配组的序号 |
| MD5值 | 文件内容的MD5哈希值 |
| 文件路径1 | 第一个文件夹中的文件相对路径 |
| 文件路径2 | 第二个文件夹中的文件相对路径 |
| 文件大小 | 文件大小（字节） |





## 常见问题

### Q: 运行时提示找不到openpyxl模块？
**A:** 请先安装依赖：`pip install openpyxl`

### Q: 可以对比非图片文件吗？
**A:** 可以，脚本支持任何类型的文件对比

### Q: 处理大量文件需要多久？
**A:** 处理速度取决于文件数量和大小，脚本会显示进度（每100个文件显示一次）

### Q: 如果某个文件夹中有文件另一个没有怎么办？
**A:** 只有MD5值匹配的文件会出现在结果中，独有的文件不会显示

# v2版本相较于v1版本的区别

v2版本增加了图片预览效果

需额外下载第三方库

> pip install Pillow