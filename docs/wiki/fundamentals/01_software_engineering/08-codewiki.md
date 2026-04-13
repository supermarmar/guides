# CodeWiki

<https://fsoft-ai4code.github.io/CodeWiki/>

Most projects begin clean. A few months (or years) later, you find yourself looking at files that reference other files, which interact with modules, and those modules connect to things nobody remembers writing. And documentation? Usually outdated, incomplete, or absent altogether.

That’s the problem CodeWiki aims to address. In short: it scans an entire repo and automatically creates proper documentation and architecture diagrams.

Large codebases are messy. Even skilled engineers find them messy. Teams change, features evolve, and manually documenting everything becomes a full-time job that nobody wants. CodeWiki solves this by combining three ideas:

## 1. Hierarchical Decomposition

Instead of reading your code file-by-file, CodeWiki divides the repository into meaningful modules. Think of it like this:

```code
project/
  ├── api/
  ├── core/
  ├── utils/
  └── services/
```

But dynamic. It clusters things based on structure, not just folder names. This method works even for large repositories — they tested it on projects ranging from 86K to 1.4 million lines of code.

## 2. A Recursive Multi-Agent System

Imagine a group of AI workers:

- One reads the repo
- Another breaks it into clusters
- Another writes documentation
- Another corrects diagrams
- And they talk to each other

That’s CodeWiki’s “agentic” system. Each agent manages a section of the repo and passes tasks when it becomes complex. In plain words: it scales without losing quality.

## 3. Multi-Modal Synthesis (text + diagrams)

CodeWiki doesn’t just generate [[02-markdown|Markdown]]. It provides diagrams like:

- Architecture overview
- Data flow
- Per-module dependency graphs
- Sequence diagrams

All created with [[07-mermaid|Mermaid]], so you can edit them later.

## Installation

You’ll need:

- Python 3.12+
- Node.js (for diagram validation)
- An LLM API key ([[CLAUDE|Claude]], OpenAI, etc.)

`pip install git+https://github.com/FSoft-AI4Code/CodeWiki.git`

```code
codewiki config set \
  --api-key YOUR_API_KEY \
  --base-url https://api.anthropic.com \
  --main-model claude-sonnet-4 \
  --cluster-model claude-sonnet-4
```

`cd /path/to/your/project`
`codewiki generate --create-branch --github-pages --verbose`
