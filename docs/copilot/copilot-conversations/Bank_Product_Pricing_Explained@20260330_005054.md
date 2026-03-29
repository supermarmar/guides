---
epoch: 1774824654335
modelKey: "claude-sonnet-4-6|anthropic"
topic: "Bank Product Pricing Explained"



tags:
  - copilot-conversation
---

**user**: I would like to understand more about how banks price their products
[Timestamp: 2026/03/30 00:50:54]

**ai**: 
<think>The user wants to understand how banks price their products. I'll provide a comprehensive explanation of bank product pricing.</think># How Banks Price Their Products

Banks use several frameworks and factors to determine pricing across their product lines. Here's an overview:

---

## Core Pricing Principles

### 1. **Cost-Plus Pricing**
Banks calculate the total cost of delivering a product and add a profit margin:
$$\text{Price} = \text{Cost of Funds} + \text{Operating Costs} + \text{Risk Premium} + \text{Profit Margin}$$

### 2. **Risk-Based Pricing**
The higher the risk of a borrower or product, the higher the price charged. This is common in:
- Personal loans
- Credit cards
- Mortgages

---

## Key Components of Bank Pricing

| Component | Description |
| --- | --- |
| **Cost of Funds** | What it costs the bank to source money (e.g., deposit rates, interbank rates) |
| **Credit Risk** | Probability of default by the borrower |
| **Liquidity Risk** | Risk of not being able to meet obligations |
| **Operational Costs** | Staff, technology, compliance costs |
| **Capital Charge** | Cost of holding regulatory capital |
| **Profit Margin** | Target return for shareholders |

---

## Pricing by Product Type

### 🏦 Loans & Mortgages
- Benchmarked against a **reference rate** (e.g., SOFR, Prime Rate)
- Formula: $$\text{Loan Rate} = \text{Base Rate} + \text{Credit Spread}$$
- Credit spread reflects the borrower's creditworthiness

### 💳 Credit Cards
- Higher rates due to **unsecured nature** and revolving credit
- Influenced by customer credit scores and behavioral data

### 💰 Deposits & Savings Accounts
- Rates set based on:
  - Central bank policy rates
  - Competition for deposits
  - Bank's liquidity needs

### 📈 Investment Products
- Fee-based (management fees, advisory fees)
- Sometimes performance-linked

---

## External Factors That Influence Pricing

- **Central Bank Policy Rates** – e.g., Fed Funds Rate, ECB rate
- **Market Competition** – Banks monitor competitor pricing
- **Regulatory Requirements** – Capital adequacy rules (Basel III/IV)
- **Macroeconomic Conditions** – Inflation, credit cycles
- **Customer Relationship** – Loyalty discounts or bundled pricing

---

## Transfer Pricing (Internal)

Banks also use **Funds Transfer Pricing (FTP)** internally to allocate the cost of funds between business units, ensuring each product is profitable on a standalone basis.

$$\text{Net Interest Margin} = \text{Lending Rate} - \text{FTP Rate}$$

---

Would you like to dive deeper into any specific product or concept, such as **mortgage pricing**, **credit card pricing**, or **FTP**?
[Timestamp: 2026/03/30 00:51:09]

**user**: How do I use the spaced repition plugin to read this file
[Context: Notes: F107_Flashcards.md]
[Timestamp: 2026/03/30 01:05:58]

**ai**: 
<think>The user is asking about how to use the spaced repetition plugin in Obsidian to read their flashcard file (F107_Flashcards.md). I can see the note uses the `?` separator format which is compatible with the **Obsidian Spaced Repetition** plugin by Stephen Mwangi (also known as "sr" plugin). Let me provide guidance on how to use it.</think># Using the Spaced Repetition Plugin with [[F107_Flashcards]]

Your note is already formatted correctly for the **Obsidian Spaced Repetition** plugin (by Stephen Mwangi). Here's how to get started:

---

## 1. Install the Plugin
- Go to **Settings → Community Plugins → Browse**
- Search for **"Spaced Repetition"**
- Install and **Enable** it

---

## 2. Tag Your Note
Your note already has the tag `#flashcards/F107` at the top — this is exactly what the plugin needs to detect flashcard decks. ✅

---

## 3. Configure the Plugin (Optional)
- Go to **Settings → Spaced Repetition**
- Under **Flashcard Decks**, ensure it is set to recognise the `#flashcards` tag
- You can also configure the **card separator** — your note uses `?` which is the default ✅

---

## 4. Start a Review Session
- Click the **ribbon icon** (stack of cards) on the left sidebar, **OR**
- Open the **Command Palette** (`Ctrl/Cmd + P`) and search:
  - `Spaced Repetition: Open a new flashcard review session`
- Select the deck **F107** from the list

---

## 5. During Review
For each card, you'll see the **question** first, then reveal the answer. You then rate yourself:

| Button | Meaning |
| --- | --- |
| **Hard** | Struggled — show again soon |
| **Good** | Got it — standard interval |
| **Easy** | Knew it well — longer interval |

The plugin will **schedule cards** based on your ratings using the SM-2 algorithm.

---

## 6. Track Progress
- The plugin adds scheduling metadata to your note automatically
- You can see due card counts in the ribbon icon

---

> 💡 **Tip**: Since your cards are organised into Easy/Medium/Hard tiers, you may want to review them in order the first time before letting the algorithm take over.
[Timestamp: 2026/03/30 01:06:13]

**user**: How do I use tags with this folder structure to further enhance my learning experience
[Context: Notes: application/banking/02_external_environment/01-regulatory_environment.md]
[Timestamp: 2026/03/30 01:15:46]

**ai**: 
<think>The user is asking about how to use tags with their folder structure to enhance their learning experience in Obsidian. They have an active note open - the regulatory environment note - and previously we were discussing the spaced repetition plugin with flashcards. Let me think about how tags work in Obsidian and how they can be used with this specific vault structure.

Looking at the note, I can see it's in the path: `application/banking/02_external_environment/01-regulatory_environment.md`

And from the flashcard note, I can see it uses `#flashcards/F107` as a tag.
 
Now I'm considering how to structure tags that align with their folder hierarchy and complement the spaced repetition workflow - things like using hierarchical tags to mirror their domain structure, tagging notes by difficulty level or review status, and leveraging tags to create filtered views that work alongside their flashcard system.</think># Using Tags with Your Vault Structure

Based on your active note [[01-regulatory_environment]] and your flashcard note [[F107_Flashcards]], here's how you can build a powerful tagging system:

---

## Your Current Folder Structure
```
application/
└── banking/
    └── 02_external_environment/
        └── 01-regulatory_environment.md
```

Tags complement folders by adding **cross-cutting dimensions** that folders alone can't capture.

---

## Suggested Tagging Strategy

### 1. **Topic/Subject Tags**
Mirror your folder structure in tags for quick filtering:
```
#banking/regulatory
#banking/capital
#banking/credit-risk
```

### 2. **Jurisdiction Tags**
Your note covers SA, UK, and EU regulation — tag accordingly:
```
#jurisdiction/south-africa
#jurisdiction/uk
#jurisdiction/eu
```

### 3. **Regulatory Body Tags**
```
#regulator/sarb
#regulator/fca
#regulator/bcbs
#regulator/fsb
```

### 4. **Spaced Repetition Integration**
Following the pattern already in [[F107_Flashcards]], use nested flashcard tags per topic:
```
#flashcards/F107/regulatory-environment
#flashcards/F107/consumer-protection
#flashcards/F107/twin-peaks
```
This lets you **drill specific sub-topics** in isolation.

### 5. **Study Status Tags**
Track your learning progress:
```
#status/new
#status/reviewing
#status/mastered
```

### 6. **Difficulty Tags** (aligned with your flashcard tiers)
```
#difficulty/easy
#difficulty/medium
#difficulty/hard
```

---

## Example Front Matter for [[01-regulatory_environment]]

Add this to the top of your note:

```yaml
---
tags:
  - banking/regulatory
  - jurisdiction/south-africa
  - jurisdiction/uk
  - jurisdiction/eu
  - regulator/sarb
  - regulator/bcbs
  - regulator/fsb
  - flashcards/F107/regulatory-environment
  - status/reviewing
---
```

---

## How This Enhances Learning

| Use Case | How Tags Help |
| --- | --- |
| **Spaced Repetition** | Review only `#flashcards/F107/regulatory-environment` cards |
| **Jurisdiction Focus** | Filter all `#jurisdiction/south-africa` notes before an SA-specific exam |
| **Progress Tracking** | Query `#status/new` to find notes not yet studied |
| **Cross-topic Links** | Find all notes tagged `#regulator/bcbs` across folders |
| **Difficulty Drilling** | Isolate `#difficulty/hard` cards for focused revision |

---

## Querying Tags with Dataview

If you have the **Dataview** plugin, you can create dynamic study lists:

````
```dataview
TABLE status, tags
FROM #flashcards/F107
WHERE contains(tags, "status/reviewing")
SORT file.name ASC
```
````

---

> 💡 **Tip**: The nested tag format (e.g., `#flashcards/F107/regulatory-environment`) is particularly powerful because searching for `#flashcards/F107` will automatically include **all sub-tags**, giving you flexible filtering.
[Timestamp: 2026/03/30 01:16:05]

**user**: How do I use the Dataview plugin
[Context: Notes: study_trakcer.md]
[Timestamp: 2026/03/30 01:25:46]

**ai**: 
<think>The user has an active note called "study_trakcer.md" which contains a Dataview query. They want to know how to use the Dataview plugin. Let me provide a comprehensive guide on using the Dataview plugin in Obsidian, with specific reference to their current note and vault structure.</think># Using the Dataview Plugin

I can see your [[study_tracker]] note already has a query started! Here's how to get everything working:

---

## 1. Install the Plugin
- Go to **Settings → Community Plugins → Browse**
- Search for **"Dataview"**
- Install and **Enable** it
- In Dataview settings, enable **"Enable Inline Queries"** and **"Enable JavaScript Queries"**

---

## 2. Fix Your Current Query
Your note's query needs a small adjustment — wrap it in a dataview code block:

````
```dataview
TABLE status, tags
FROM #flashcards/F107
SORT file.name ASC
```
````

> ⚠️ Your note currently wraps it in ` ```text ` instead of ` ```dataview ` — this is why it won't render correctly.

---

## 3. Query Syntax Basics

### Core Structure
```
SELECT  →  TABLE / LIST / TASK / CALENDAR
FROM    →  Source (tag, folder, file)
WHERE   →  Filter condition
SORT    →  Ordering
```

### FROM Sources

| Source Type | Example |
| --- | --- |
| **Tag** | `FROM #flashcards/F107` |
| **Folder** | `FROM "application/banking"` |
| **Specific File** | `FROM "F107_Flashcards"` |
| **Combined** | `FROM #flashcards AND "application"` |

---

## 4. Useful Queries for Your Vault

### 📋 View All Flashcard Notes with Status
````
```dataview
TABLE status, tags
FROM #flashcards/F107
SORT file.name ASC
```
````

### 🔴 Show Only Notes Still Being Reviewed
````
```dataview
TABLE file.name, status
FROM #flashcards/F107
WHERE contains(tags, "status/reviewing")
SORT file.name ASC
```
````

### 📁 All Notes in Banking Folder
````
```dataview
LIST
FROM "application/banking"
SORT file.name ASC
```
````

### 📅 Recently Modified Notes
````
```dataview
TABLE file.mtime AS "Last Modified", status
FROM #flashcards/F107
SORT file.mtime DESC
```
````

### 🌍 Notes by Jurisdiction
````
```dataview
TABLE tags
FROM "application/banking"
WHERE contains(tags, "jurisdiction/south-africa")
```
````

---

## 5. Reading Query Results

Once the code block uses ` ```dataview `, Obsidian will render it as a **live dynamic table** that:
- **Auto-updates** when notes change
- **Links** file names so you can click through
- **Reflects** tag and property changes in real time

---

## 6. Dataview Property Types

For best results, use **YAML front matter** in your notes (as suggested previously):

```yaml
---
tags:
  - flashcards/F107
  - status/reviewing
  - difficulty/hard
date: 2026-03-29
---
```

You can then query any of these fields directly in Dataview.

---

> 💡 **Tip**: Rename your note from `study_trakcer` to `study_tracker` to fix the typo — you can right-click the note in the file explorer to rename it!
[Timestamp: 2026/03/30 01:26:04]