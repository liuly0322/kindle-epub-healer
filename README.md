# 📘 kindle-epub-healer

自动修复在 Amazon Send-to-Kindle 转换中失败的 EPUB 文件。  
本仓库利用 **GitHub Copilot Task Agent**，自动分析并修补 EPUB 文件，使其兼容 Kindle 的 `kindlegen` 转换工具。

![amazing-amazon](https://private-user-images.githubusercontent.com/77669094/513103789-f477f5aa-185b-4d10-9f55-0e3ff4970122.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjI5MjI1MDQsIm5iZiI6MTc2MjkyMjIwNCwicGF0aCI6Ii83NzY2OTA5NC81MTMxMDM3ODktZjQ3N2Y1YWEtMTg1Yi00ZDEwLTlmNTUtMGUzZmY0OTcwMTIyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTExMTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMTEyVDA0MzY0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWJlNjViOGY4NmNhMGZlYmMwOTQ1OWRlZWM2MTEzODM2Njg4YzQxNmQyM2NkNjZlY2I2NDg5MDc2YjA4YWNkYjcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.IpsYo8kmkOIlUPcqLzKOY5EcTCRhUWv-4uxsgCsTfNA)

> 你说得对，但这就是我们 Amazon Send-to-Kindle 的成功率！

> 手动修复 epub 和 SWE-bench 简直太像了，所以我们直接使用 copilot swe agent 来完成这项工作。

---

## 🚀 使用流程

1. **创建新分支**  
   每次修复一个 EPUB，都应新建一个分支。

2. **上传待修复的 EPUB 文件**  
   将有问题的 `.epub` 文件直接上传到新分支（根目录即可）。

3. **创建 Copilot 任务**  
   使用下面提供的任务提示词（prompt）创建一个 Task。  
   Copilot 会自动创建一个 **Pull Request**，提交修复建议。

4. **审查并合并 PR**  
   检查 PR 内的修改及日志。  
   若修复后的 EPUB 能被 `kindlegen` 成功转换，即可合并。

你可以在 [#1](https://github.com/liuly0322/kindle-epub-healer/pull/1) 查看一个示例 PR。

> 注意到这几步都可以在 GitHub 网页版上完成。

> 或许也有对应的 API……？

---

## 🧠 任务提示词（Task Prompt）

> **Prompt:**  
> 请修复上传的 EPUB 文件，使其能够通过 Amazon Kindle 的 `kindlegen` 转换工具成功转换。  
> 在执行转换前，请先在仓库根目录解压二进制包：  
>  
> ``tar -xzf kindlegen_linux_2.6_i386_v2_9.tar.gz``  
>  
> 然后找到解压后的 kindlegen 可执行文件，再使用以下命令测试转换是否成功：  
>  
> ``./kindlegen <filename>.epub``  
> 
> 如果修复成功，那么会在与 epub 相同目录下生成一个 mobi 文件。 
> 请确保修复后的 EPUB 保留原书的元数据和内容结构。  
> 若问题来自无效的 XHTML、缺少 manifest 条目或 spine 顺序错误，请自动修正。  
> 输出修复后的文件名为 ``fixed_<原文件名>.epub``。
>
> 除了新的 epub 文件，请创建一个 `fix_log.txt`，记录所有修复步骤，无需记录详细细节。
> 除此之外，你不需要创建任何其他文件。过程中使用的脚本可以创建在临时目录中，任务完成后删除即可。
