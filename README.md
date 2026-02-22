# ProjectLaunch 🚀

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PyPI](https://img.shields.io/pypi/v/projectlaunch)
![Downloads](https://img.shields.io/pypi/dm/projectlaunch)

**Simple GitHub Push Tool for Students & Developers**

Push your projects to GitHub with a single command. No complex git commands needed!

---

## 🎯 What Does It Do?

ProjectLaunch simplifies pushing your code to GitHub:
- ✅ Automatically initializes git repository
- ✅ Adds all your files
- ✅ Creates a commit with your message
- ✅ Pushes to your GitHub repository
- ✅ All in one command!

---

## 📦 Installation

```bash
pip install projectlaunch
```

**Requirements:**
- Python 3.8 or higher
- Git installed on your system ([Download Git](https://git-scm.com))

---

## 🚀 Quick Start

### Basic Usage (Interactive)

Navigate to your project folder and run:

```bash
pl push
```

The tool will ask you:
1. **GitHub repository URL** - Example: `https://github.com/username/my-project`
2. **Commit message** - Example: `Initial commit` or `Added new features`

That's it! Your code is now on GitHub! 🎉

---

## 💡 Usage Examples

### Example 1: Interactive Mode (Recommended for Beginners)

```bash
cd my-project
pl push
```

**Output:**
```
ProjectLaunch - GitHub Push Tool

Enter your GitHub repository URL:
Repository URL: https://github.com/username/my-project

Enter commit message:
Commit message [Initial commit]: Added homepage

Pushing to GitHub...
✓ Initializing git...
✓ Adding files...
✓ Committing: Added homepage
✓ Setting remote...
✓ Pushing...

Successfully pushed!
Repository: https://github.com/username/my-project
```

---

### Example 2: With Command-Line Options (Faster)

```bash
pl push --repo https://github.com/username/my-project --message "Initial commit"
```

**Short version:**
```bash
pl push -r https://github.com/username/my-project -m "Initial commit"
```

---

### Example 3: Push from Different Directory

```bash
pl push --path /path/to/your/project --repo https://github.com/username/repo
```

---

## 📖 Command Reference

### Main Command

```bash
pl push [OPTIONS]
```

### Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--repo` | `-r` | GitHub repository URL | `--repo https://github.com/user/repo` |
| `--message` | `-m` | Commit message | `--message "Fixed bugs"` |
| `--path` | `-p` | Project directory path | `--path ./my-project` |
| `--help` | `-h` | Show help message | `--help` |

### Other Commands

```bash
pl --version          # Show version
pl --help            # Show all commands
projectlaunch push   # Full command name (same as 'pl push')
```

---

## 🎓 Step-by-Step Tutorial

### First Time Setup

**Step 1: Create a GitHub Repository**

1. Go to [GitHub](https://github.com)
2. Click the **+** icon → **New repository**
3. Enter repository name (e.g., `my-awesome-project`)
4. Click **Create repository**
5. Copy the repository URL (e.g., `https://github.com/username/my-awesome-project`)

**Step 2: Install ProjectLaunch**

```bash
pip install projectlaunch
```

**Step 3: Navigate to Your Project**

```bash
cd path/to/your/project
```

**Step 4: Push to GitHub**

```bash
pl push
```

Enter the repository URL you copied in Step 1, and you're done! 🎉

---

## 🔧 Common Scenarios

### Scenario 1: First Time Pushing a New Project

```bash
cd my-new-project
pl push
# Enter: https://github.com/username/my-new-project
# Enter: Initial commit
```

---

### Scenario 2: Updating an Existing Project

```bash
cd my-existing-project
pl push -r https://github.com/username/my-existing-project -m "Updated features"
```

---

### Scenario 3: Quick Push with Default Message

```bash
pl push -r https://github.com/username/repo
# Uses default message: "Initial commit"
```

---

## ❓ FAQ

### Q: Do I need to create a GitHub repository first?
**A:** Yes! Create an empty repository on GitHub first, then use ProjectLaunch to push your code.

### Q: What if I already have a git repository?
**A:** No problem! ProjectLaunch will detect it and just push your changes.

### Q: Can I use this for private repositories?
**A:** Yes! Just make sure you're logged into GitHub on your system.

### Q: What if the push fails?
**A:** ProjectLaunch will automatically try force push. Make sure:
- Git is installed
- You have internet connection
- The repository URL is correct
- You have permission to push to the repository

### Q: Does it work on Windows/Mac/Linux?
**A:** Yes! Works on all platforms where Python and Git are installed.

---

## 🛠️ Troubleshooting

### Error: "Git not installed"

**Solution:** Install Git from [git-scm.com](https://git-scm.com)

---

### Error: "Permission denied"

**Solution:** Make sure you're logged into GitHub:
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

### Error: "Repository not found"

**Solution:** 
1. Check the repository URL is correct
2. Make sure the repository exists on GitHub
3. Verify you have access to the repository

---

## 🎯 Real-World Examples

### Example 1: Student Project

```bash
# You just finished your college project
cd final-year-project
pl push -r https://github.com/student123/final-year-project -m "Completed project"
```

---

### Example 2: Quick Prototype

```bash
# You built a quick prototype and want to share it
cd prototype-app
pl push
# Enter repo URL and message when prompted
```

---

### Example 3: Daily Updates

```bash
# End of day, pushing your work
cd work-project
pl push -r https://github.com/company/work-project -m "Day 5: Implemented login feature"
```

---

## 📝 Tips & Best Practices

1. **Use descriptive commit messages**
   - ❌ Bad: `"update"`
   - ✅ Good: `"Added user authentication feature"`

2. **Push regularly**
   - Don't wait until the end of the project
   - Push after completing each feature

3. **Check your files**
   - Make sure you're not pushing sensitive data (passwords, API keys)
   - Use `.gitignore` to exclude unnecessary files

4. **Create a .gitignore file**
   ```
   # Common files to ignore
   __pycache__/
   *.pyc
   .env
   node_modules/
   .DS_Store
   ```

---

## 🆘 Need Help?

- **GitHub:** [madhan112007/test-project_launch](https://github.com/madhan112007/test-project_launch)
- **Issues:** [Report bugs](https://github.com/madhan112007/test-project_launch/issues)
- **Email:** codethetrend@gmail.com
- **PyPI:** [projectlaunch](https://pypi.org/project/projectlaunch/)

---

## 📄 License

MIT License - Free to use for everyone!

---

## 🙏 Credits

Built for students and developers who want a simpler way to push code to GitHub.

---

**Made with ❤️ by Madhan**

---

## Quick Reference Card

```bash
# Install
pip install projectlaunch

# Basic usage
pl push

# With options
pl push -r https://github.com/user/repo -m "Commit message"

# Get help
pl --help

# Check version
pl --version
```

---

**Happy Coding! 🚀**
