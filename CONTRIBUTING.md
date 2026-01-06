# Contributing Guidelines

Thanks for your interest in contributing! This repository follows simple, practical standards to keep the codebase clean, readable, and production-oriented.

---

## 📌 What This Repo Is For

This project is focused on:
- Cloud / CloudOps simulations
- Troubleshooting and automation workflows
- Infrastructure concepts demonstrated through code and runbooks

Contributions should improve **clarity, reliability, or realism** of cloud operations.

---

## 🛠 Ways to Contribute

You can help by:
- Fixing bugs or broken scripts
- Improving documentation or runbooks
- Adding tests or validation steps
- Refactoring code for clarity or reliability
- Adding realistic failure scenarios or troubleshooting steps

Low-effort or cosmetic-only changes may be declined.

---

## 🧪 Testing Expectations

Before submitting a pull request:
- Scripts should run without errors
- Any new functionality should be tested manually or with automated tests (if applicable)
- Clearly describe **how you tested your change**

If tests exist, they **must pass** before submission.

---

## 📂 Project Structure (General)

- `scripts/` – automation or helper scripts  
- `runbooks/` – troubleshooting and operational guides  
- `tests/` – validation and test files  
- `screenshots/` – evidence of execution or results  
- `README.md` – project overview and usage  

Follow existing structure unless there’s a strong reason to change it.

---

## 🧾 Commit Message Guidelines

Use clear, descriptive commit messages:

**Good**
Fix EC2 permission error in startup script
Add runbook for S3 access denied troubleshooting

markdown
Copy code

**Bad**
updates
fix
stuff

yaml
Copy code

---

## 🔀 Pull Request Process

1. Fork the repository
2. Create a feature or fix branch  
feature/add-cloudwatch-runbook
fix/iam-policy-bug

yaml
Copy code
3. Make your changes
4. Submit a pull request with:
- What changed
- Why it matters
- How it was tested

Incomplete PRs may be closed without review.

---

## 🚫 What Not to Submit

- Generated files or secrets
- Hard-coded credentials
- Plagiarized content
- AI-generated content without verification or testing

---

## 📄 Code of Conduct

Be respectful and professional. This project values clear thinking, accountability, and real-world engineering practices.

---

## ❓ Questions

If something is unclear, open an issue with:
- The problem
- What you tried
- Expected vs actual behavior

Clear questions get faster answers.







