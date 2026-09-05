# Cursor: Complete Guide to Getting Started

## Part 1: How to Use Cursor

### What is Cursor?
Cursor is an AI-powered code editor built on VS Code that integrates Claude, GPT-4, and other AI models directly into your coding workflow. It's designed to make coding faster and more intuitive.

### Installation & Setup

1. **Download Cursor**
   - Go to [cursor.com](https://cursor.com)
   - Download for your OS (Mac, Windows, Linux)
   - Install like any standard application

2. **Initial Configuration**
   - Open Cursor and sign up or sign in
   - Select your AI model preference (Claude, GPT-4, etc.)
   - Configure your API keys if using external models
   - Cursor comes with built-in Claude access for Pro users

### Core Features

#### 1. **Cmd/Ctrl + K (Code Generation)**
   - Fastest way to generate code
   - Highlight a section and press Cmd/Ctrl + K
   - Describe what you want: "Add error handling to this function"
   - AI edits code inline with your approval
   - You can edit the suggestion or ask it to retry

#### 2. **Cmd/Ctrl + Shift + L (Composer/Multi-file Editing)**
   - Edit multiple files at once
   - Great for larger refactoring tasks
   - See all changes before applying
   - Ask questions like "Refactor this entire module to use TypeScript"

#### 3. **Chat Sidebar (Cmd/Shift + I)**
   - Ask questions about your codebase
   - Get explanations without editing code
   - Reference files with @ symbol: "@filename.js explain this function"
   - Use this for understanding, learning, and debugging

#### 4. **Tab Autocomplete**
   - Smart code completion as you type
   - Understands context and patterns
   - Press Tab to accept suggestions
   - Press Escape to dismiss

#### 5. **Rules & Cursor Settings**
   - Create `.cursor/rules` file in your project
   - Define coding standards, style guides, architecture patterns
   - All AI operations follow these rules
   - Example: "Use TypeScript", "Follow Airbnb style guide", "Use async/await"

### Pro Tips for Effective Use

- **Context is Everything**: Include file references (@) so AI understands your codebase
- **Be Specific**: "Add validation" is vague; "Add email validation using zod" is clear
- **Review Changes**: Always review AI suggestions before accepting
- **Iterate**: If results aren't perfect, refine your request
- **Use Rules**: Create `.cursor/rules` for consistent quality across all AI operations

---

## Part 2: Printing & Creating PDFs from Cursor

### Method 1: Print to PDF (Built-in)

1. **Select the code** you want to print
2. **Cmd/Ctrl + P** → Search "Print"
3. Choose "Print to PDF" option
4. Configure:
   - Page size (A4, Letter)
   - Margins
   - Headers/footers with filename
5. Save to location of choice

**Limitation**: This includes UI elements; code may have formatting issues.

### Method 2: Export as HTML → PDF (Better for Code)

1. **Install Extension**: "Code to HTML" or "Better Comments"
2. **Select code block**
3. Right-click → "Export to HTML"
4. Open HTML file in browser
5. **Cmd/Ctrl + P** → Print → Save as PDF
6. **Benefits**: 
   - Syntax highlighting preserved
   - Clean formatting
   - Professional appearance

### Method 3: Use VS Code Extensions

**Recommended Extensions:**
- **Markdown PDF**: Converts markdown notes to PDF
- **Print Code**: Optimized for printing code
- **Markdown Preview Enhanced**: Great for documentation

**Steps:**
1. Install extension from Cursor's Extensions marketplace
2. Open file
3. Right-click → "Print to PDF" or equivalent command
4. Customize styling in extension settings

### Method 4: Command Line (Most Professional)

If you want high-quality PDF output:

```bash
# Using Pandoc (install first: brew install pandoc)
pandoc your_file.md -o output.pdf

# Using VS Code CLI
code --print-to-pdf="output.pdf" filename.js

# Using wkhtmltopdf for HTML
wkhtmltopdf input.html output.pdf
```

### Method 5: Generate Documentation PDF

For entire projects:

1. **Install**: "Markdown All in One" extension
2. **Create**: `README.md` or `DOCUMENTATION.md`
3. **Ask Claude**: "Generate comprehensive documentation for this project"
4. **Export**: Markdown file → PDF using Pandoc or VS Code

### Best Practices for Code PDFs

- **Syntax Highlighting**: Use dark or light theme consistently
- **Line Numbers**: Enable for reference
- **File Headers**: Include filename and date
- **Code Blocks**: Keep lines under 80 characters for readability
- **Font**: Use monospace (Courier, Monaco, Fira Code)

---

## Part 3: Git Integration in Cursor

### Built-in Git Features

Cursor includes full Git support (inherited from VS Code):

#### 1. **Source Control Panel (Cmd/Ctrl + Shift + G)**

Opens the Git panel where you can:
- See modified files
- Stage/unstage changes
- Write commit messages
- View file differences
- Resolve merge conflicts

**Workflow:**
1. Make changes to your files
2. Files appear in "Changes" section
3. Click + icon to stage files
4. Type commit message
5. Press Cmd/Enter or click commit button

#### 2. **Diff Viewer**

- **View changes**: Click on any file to see what changed
- **Side-by-side**: Left = original, Right = modified
- **Colors**: Red = removed, Green = added
- **Review before committing**

#### 3. **Git Commands via Command Palette**

Press Cmd/Ctrl + Shift + P and search:
- `Git: Clone` - Clone a repository
- `Git: Commit` - Create a commit
- `Git: Push` - Push to remote
- `Git: Pull` - Pull from remote
- `Git: Create Branch` - Create new branch
- `Git: Delete Branch` - Delete branch
- `Git: Merge Branch` - Merge branches
- `Git: Checkout to...` - Switch branches

#### 4. **Branch Management**

- **Current branch indicator**: Bottom-left of window
- **Click to switch branches**: Shows all local/remote branches
- **Create new branch**: Cmd/Ctrl + Shift + P → "Git: Create Branch"

### Advanced Git in Cursor

#### 1. **Gitignore Support**
- Cursor respects your `.gitignore`
- Files listed won't show in source control
- Edit `.gitignore` to change what Git tracks

#### 2. **Merge Conflict Resolution**
When conflicts occur:
- **Visual indicators**: Conflicted sections highlighted
- **Accept Current/Incoming/Both**: Buttons appear in conflict regions
- **Manual editing**: Edit conflicts directly if needed
- **Mark resolved**: File status updates automatically

#### 3. **Git History (with Extension)**

Install "Git Graph" extension:
1. Extensions → Search "Git Graph"
2. Install
3. Cmd/Ctrl + Shift + G → Click "Git Graph"
4. Visualize commit history
5. Right-click commits to:
   - Cherry-pick
   - Revert
   - Create branch
   - View details

#### 4. **GitHub/GitLab Integration**

1. **Authenticate**:
   - Cmd/Ctrl + Shift + P → "GitHub: Authorize"
   - Sign in with your GitHub account

2. **Features**:
   - Create pull requests from Cursor
   - View PRs and issues
   - Publish branches directly
   - Sync with remote easily

### Practical Git Workflow in Cursor

#### Scenario 1: Daily Development

```
1. Start: Cmd/Ctrl + Shift + G (open source control)
2. Make changes to your files
3. Stage files you want to commit (click + icon)
4. Write message: "feat: add user authentication"
5. Commit: Cmd/Enter
6. Push: Cmd/Ctrl + Shift + P → "Git: Push"
```

#### Scenario 2: Creating a Feature Branch

```
1. Cmd/Ctrl + Shift + P → "Git: Create Branch"
2. Name it: "feature/new-dashboard"
3. Make changes on this branch
4. Stage and commit
5. Cmd/Ctrl + Shift + P → "Git: Push" (publishes branch)
6. Create PR on GitHub/GitLab
```

#### Scenario 3: Pulling Latest Changes

```
1. Cmd/Ctrl + Shift + P → "Git: Pull"
2. Automatically downloads and merges latest changes
3. If conflicts: Resolve in Diff Viewer
4. Continue working
```

### Essential Git Commands Quick Reference

| Task | Command |
|------|---------|
| Open Source Control | Cmd/Ctrl + Shift + G |
| Stage all changes | Click checkbox next to "Changes" |
| Commit | Cmd/Enter (with message written) |
| Push to remote | Cmd/Ctrl + Shift + P → "Git: Push" |
| Pull latest | Cmd/Ctrl + Shift + P → "Git: Pull" |
| Switch branch | Click branch name (bottom-left) |
| Create branch | Cmd/Ctrl + Shift + P → "Git: Create Branch" |
| View history | Install "Git Graph" extension |

### Recommended Extensions for Git

1. **Git Graph** - Visual commit history
2. **GitLens** - Detailed blame/history
3. **GitHub Pull Requests** - Full PR management in editor
4. **Conventional Commits** - Helps write standard commit messages

### Common Git Issues & Solutions

**Problem: "Permission denied" when pushing**
- Solution: Check SSH keys setup or use HTTPS tokens
- Cmd/Ctrl + Shift + P → "GitHub: Authorize"

**Problem: Merge conflicts**
- Solution: Use Diff Viewer's conflict resolution tools
- Manual edit if needed

**Problem: Can't see remote branches**
- Solution: Cmd/Ctrl + Shift + P → "Git: Fetch" first

**Problem: Accidentally committed to wrong branch**
- Solution: Cmd/Ctrl + Shift + P → "Git: Cherry Pick"

---

## Summary: Your First 15 Minutes in Cursor

1. **Download & Install** Cursor from cursor.com
2. **Configure AI model** (Claude is recommended)
3. **Open a project folder**
4. **Try Cmd/Ctrl + K** on a function to see AI code editing
5. **Create `.cursor/rules`** with your coding standards
6. **Initialize Git**: Cmd/Ctrl + Shift + P → "Git: Initialize Repository"
7. **Make first commit**: Edit a file → Stage → Commit → Push
8. **Explore Chat** (Cmd/Shift + I) to ask questions about your code

---

## Learning Resources

- **Official Docs**: [docs.cursor.com](https://docs.cursor.com)
- **YouTube Channel**: "Cursor AI Editor" tutorials
- **Community**: Cursor Discord for tips and troubleshooting
- **VS Code Docs**: Since Cursor is VS Code-based, VS Code docs apply

---

## Pro Tips Recap

✅ Use `@filename` in chat to reference specific files  
✅ Create `.cursor/rules` for consistent AI behavior  
✅ Review all AI changes before accepting  
✅ Commit frequently with descriptive messages  
✅ Use branches for features, not main development  
✅ Always pull before pushing  
✅ Learn keyboard shortcuts for speed  
