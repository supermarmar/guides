# 🧾 Overview of the Contribution Workflow

Welcome! 👋 We’re glad you're here. This guide will walk you through how to contribute to the shared repository using Azure and VS Code.

Whether you're fixing a typo, building a model, or improving documentation — follow these steps to keep our codebase clean, traceable, and collaborative.

---

## 1️⃣ Tracking Work Using Azure Boards

We use **Azure Boards** to manage work and collaboration.

| Level   | Description                              |
|---------|------------------------------------------|
| **Epic**     | Large thematic areas (e.g. "IFRS9 Modelling")     |
| **Feature**  | Major work items or deliverables     |
| **Task**     | Smallest actionable units of work    |
| **Bug**      | Defects or things that need fixing   |

---

## 2️⃣ How to Get Started

- Ask a **Repo Maintainer** to give you access to Azure Boards
- Browse the project boards for active work
- Pick an open **Task** assigned to your **Feature**
- If none exist, contact the **Team Coordinator** to help define and assign one

Each task will contain:

- A clear description
- Acceptance criteria
- Links to related documentation or code

---

## 3️⃣ Pull the Latest `main` Locally

Once you’ve selected a task from Azure Boards open your terminal in VS Code:

```bash
git checkout main
git pull origin main
```

---

## 4️⃣ Create a New Branch

Use the naming convention: `yourname/short-description-YYYYMMDD`

```bash
git checkout -b joanna/improve-cleaning-20250529
```

---

## 5️⃣ Make Your Changes

Help reviewers and contributors remember key checks before pushing:

- Focus on one subtask or issue at a time.
- Run the code regularly to check for errors.
- Follow existing coding standards (see docs\markdown\modelling\coding_standards.md).
- Avoid committing large files or credentials
- Delete unused code and print statements

Before staging your changes run the following formating commands in the terminal:

- `nbqa black .`
- `nbqa isort .`
- `nbqa flake8 .`
- `black .`
- `isort .`
- `flake8 .`

---

## 6️⃣ Stage Your Changes

*Note: Before staging your changes, please execute the following codes to ensure you have the latest version of the main branch on your repository:*

```bash
git checkout main
git pull origin main
```

Add files you want to commit:

```bash
git add .
```

Or add specific files:

```bash
git add notebooks/001-data_cleaning-20250909.ipynb
```

---

## 7️⃣ Commit with a Message

Use clear, concise messages that explain what was done:

```bash
git commit -m "Add notebook to clean missing values in loan dataset"
```

💡 Tip: Use [conventional commit style](https://www.conventionalcommits.org/en/v1.0.0/) if possible.

---

## 8️⃣ Push to Azure

Push your branch to Azure:

```bash
git push origin joanna/improve-cleaning-20250529
```

If it’s the first push for this branch, Git will tell you to set upstream. You can follow its suggestion or use:

```bash
git push --set-upstream origin joanna/improve-cleaning-20250529
```

On subsequent pushes:

```bash
git push
```

---

## 9️⃣ Create a Pull Request (PR)

1. On Azure go to **Repos > Pull Requests**
2. Click “New Pull Request” and set:
   - Source branch = your feature branch
   - Target branch = main
3. See the Pull Request template section below for an example on how to set it up. You can also find it in this [template](pr_template.md).
4. Assign Reviewers from the repo team
5. Submit the PR

---

## 🔁 Review & Feedback

The reviewer will:

- Check if the code runs correctly
- Ensure naming, formatting, and logic are consistent
- Request changes if needed

Once approved, your PR will be merged into main ✅

---

## 🔟 Clean Up After Merge

Delete the branch on Azure if prompted. Locally, return to `main`:

```bash
git checkout main
git pull origin main
```

Delete your branch locally if you wish:

```bash
git branch -d joanna/improve-cleaning-20250529
```

## 🚦Summary Workflow Diagram

Tasks ➡ Branch ➡ Add ➡ Commit ➡ Push ➡ PR ➡ Review ➡ Merge ➡ Delete
