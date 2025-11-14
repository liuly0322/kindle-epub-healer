# 📘 kindle-epub-healer

[中文版](README_zh.md)

Automatically fix EPUB files that fail in Amazon Send-to-Kindle conversion.  
This repository uses **GitHub Copilot Task Agent** to automatically analyze and fix EPUB files, making them compatible with Kindle's `kindlegen` conversion tool.

![amazing-amazon](https://github.com/user-attachments/assets/bf4a6279-5d74-4231-9c7c-9a158e98bfbe)

> You're right, but this is our Amazon Send-to-Kindle success rate!

> Manually fixing epub files is quite similar to SWE-bench, so we directly use copilot swe agent to complete this task.

---

## 🚀 Usage Workflow

1. **Create a new branch**  
   Create a new branch for each EPUB file you want to fix.

2. **Upload the EPUB file to be fixed**  
   Upload the problematic `.epub` file directly to the new branch (in the root directory).

3. **Create a Copilot task**  
   Use [Copilot Agent](https://github.com/copilot/agents) to create a task. Make sure to select the correct branch and apply the built-in kindle-epub-healer agent from this repository.
   Copilot will automatically create a **Pull Request** with fix suggestions.

4. **Review and merge the PR**  
   Check the changes and logs in the PR.  
   If the fixed EPUB can be successfully converted by `kindlegen`, merge it.

You can check [#6](https://github.com/liuly0322/kindle-epub-healer/pull/6) for an example PR.

> Note that all these steps can be completed on the GitHub web interface.

> Maybe there are corresponding APIs...?
