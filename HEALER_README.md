# EPUB Healer 使用说明

## 功能说明

`epub_healer.py` 是一个自动修复 EPUB 文件的 Python 脚本，可以解决以下常见问题：

- **重复的 manifest 条目**：自动检测并删除 content.opf 中的重复项
- **保留元数据和内容结构**：修复过程不会改变书籍的内容、章节顺序或元数据
- **Kindle 兼容性**：确保修复后的 EPUB 能通过 Amazon Kindle 的 kindlegen 工具转换

## 使用方法

### 基本用法

```bash
python3 epub_healer.py <epub文件路径>
```

### 示例

```bash
# 修复单个 EPUB 文件
python3 epub_healer.py '[入间人间]六百六十元的实情.epub'

# 输出文件将自动命名为：fixed_[入间人间]六百六十元的实情.epub
```

### 验证修复结果

修复完成后，使用 kindlegen 验证转换是否成功：

```bash
# 1. 解压 kindlegen 工具（首次使用时）
tar -xzf kindlegen_linux_2.6_i386_v2_9.tar.gz

# 2. 测试转换
./kindlegen fixed_<原文件名>.epub
```

如果转换成功，会在相同目录下生成对应的 .mobi 文件。

## 技术细节

### 修复内容

脚本会自动检测并修复以下问题：

1. **重复的 manifest 项**
   - 扫描 content.opf 中的所有 `<item>` 元素
   - 检测具有相同 `id` 属性的重复项
   - 保留第一次出现的项，删除后续重复项

2. **EPUB 结构完整性**
   - 正确提取和重新打包 EPUB（ZIP 格式）
   - 确保 mimetype 文件位于 ZIP 包的首位（未压缩）
   - 保留所有命名空间和 XML 声明

### 工作流程

1. 提取 EPUB 文件到临时目录
2. 定位并解析 content.opf 文件
3. 识别并删除重复的 manifest 条目
4. 重新打包为符合 EPUB 规范的 ZIP 文件
5. 清理临时文件

## 常见问题

### Q: 修复后的文件在哪里？
A: 与原文件在同一目录下，文件名为 `fixed_<原文件名>.epub`

### Q: 原文件会被修改吗？
A: 不会，原文件保持不变，所有修改都保存到新文件中

### Q: 支持哪些类型的 EPUB 问题？
A: 目前主要修复 manifest 中的重复条目问题，这是导致 kindlegen 转换失败的最常见原因之一

### Q: 脚本需要什么依赖？
A: 只需要 Python 3 标准库，无需安装额外依赖包

## 许可证

本脚本为开源软件，遵循仓库的许可证条款。
