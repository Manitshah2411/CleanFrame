# Contributing to CleanFrame

Thank you for your interest in contributing to **CleanFrame** 🎉  
This document explains how to set up the project locally, propose changes, and submit contributions following open-source best practices.

---

## Table of Contents

- Getting Started
- Development Setup
- Running Tests
- Branching Model
- Commit Message Guidelines
- Pull Request Process
- Reporting Issues
- Code of Conduct

---

## Getting Started

1. Fork the repository on GitHub.

2. Clone your fork locally:

```bash
git clone https://github.com/<your-username>/CleanFrame.git
cd CleanFrame
```

3. Add the upstream repository:

```bash
git remote add upstream https://github.com/Manitshah2411/CleanFrame.git
```

---

## Development Setup

CleanFrame uses a standard Python `src/` layout and is installed in editable mode during development.

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the project in editable mode:

```bash
pip install -e .
```

3. Install development dependencies:

```bash
pip install pytest
```

---

## Running Tests

All tests are written using **pytest**.

To run the test suite locally:

```bash
pytest
```

All tests **must pass** before opening a pull request.  
The CI pipeline will automatically run the same tests on every pull request.

---

## Branching Model

- `main` is the **stable branch**
- Never commit directly to `main`
- Always create a feature branch from `main`

Example:

```bash
git checkout main
git pull upstream main
git checkout -b feat/meaningful-change
```

---

## Commit Message Guidelines

We follow a simple, readable commit style inspired by Conventional Commits:

``` txt
<type>: short description
```

### Allowed types

- `feat` – new functionality
- `fix` – bug fixes
- `docs` – documentation changes
- `test` – adding or updating tests
- `ci` – CI/CD changes
- `chore` – maintenance or tooling

### Examples

``` txt
feat: normalize CSV headers
fix: handle empty header values
ci: add GitHub Actions test workflow
```

---

## Pull Request Process

1. Ensure your branch is up to date:

```bash
git fetch upstream
git rebase upstream/main
```

2. Push your branch to your fork:

```bash
git push origin feat/meaningful-change
```

3. Open a Pull Request on GitHub:

- Base branch: `main`
- Describe **what** changed and **why**
- Reference any related issues (e.g. `Closes #12`)

4. Address review feedback if requested.

---

## Reporting Issues

If you find a bug or want to request a feature:

1. Check existing issues first

2. Open a new issue with:

- Clear description
- Steps to reproduce (if a bug)
- Expected vs actual behavior

Well-written issues help maintainers respond faster.

---

## Code of Conduct

This project follows a simple rule:  
**Be respectful, constructive, and professional.**

Harassment, discrimination, or hostile behavior is not tolerated.

---

Thank you for contributing ❤️  
Every issue, pull request, and discussion helps improve CleanFrame.
