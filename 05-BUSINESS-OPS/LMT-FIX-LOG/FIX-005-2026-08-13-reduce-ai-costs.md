# FIX-005 — Reduce AI Coding Costs
Date: 2026-08-13
Status: IN PROGRESS

---

## Problem
Anthropic API charges running ~$73/mo. Most of the cost is Claude Code sessions, not the Barb app.

## Fix Part 1 — Barb App (DONE)
Switched Ask Barb from claude-sonnet-4-6 to claude-haiku-4-5-20251001.
Estimated savings: ~10x reduction in per-message cost.
Repo: securestep-ai / app.py

## Fix Part 2 — Claude Code Alternatives (TODO)

Evaluate and test one of the following as a replacement or supplement to Claude Code:

| Tool | Cost | Notes |
|---|---|---|
| **Cursor** | $20/mo | Full IDE replacement, best overall |
| **GitHub Copilot** | $10/mo | Lighter weight, code completion focused |
| **Aider** | Free + API key | Terminal-based like Claude Code, use Haiku to keep costs near $0 |
| **Continue.dev** | Free + API key | VS Code plugin, same model flexibility |
| **Windsurf** | $15/mo | Similar to Cursor |

**Recommended next step:** Test Aider — free tool, uses your existing Anthropic key, can be pointed at Haiku. Near-zero cost per session.

## Action Items
- [ ] Get Barb app Streamlit secret updated to ANTHROPIC_API_KEY (Haiku)
- [ ] Test Barb on Haiku — confirm it works
- [ ] Research Aider setup on Windows
- [ ] Compare Cursor vs Aider for Brian's workflow
- [ ] Decision: replace or supplement Claude Code
