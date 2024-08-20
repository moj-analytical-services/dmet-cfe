---
marp: true
title: Git - Long Living Branches
theme: moj
paginate: true
_paginate: skip
_class: title
footer: ![image w:40](https://raw.githubusercontent.com/ministryofjustice/marp-moj-theme/main/images/moj.png)
_footer: ''
---

<!-- _header: ![w:100](https://raw.githubusercontent.com/ministryofjustice/marp-moj-theme/main/images/moj.png) -->

## Gitflow vs Trunk Based Development

## Parminder & Tom H

### August 2024 

---

## Why?"

- 

![bg left 50%](https://evaluationcanada.ca/client_assets/images/people_hold_arrow.png)

---

## What? - Long Living Feature Branches

- Goal - 

- Feature based development ([GitFlow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow))

- Developers create seperate, long lived branches for individual features or tasks.

- Depending on complexity, feature branches can be active for days, weeks or months.

- Once the feature is complete and throroughly tested, it can be merged back into the main branch.

![bg 20%](./images/git-logo.png)

---

## Gitflow Diagram

![w:800 center - Gitflow img](./images/)



---

## What is Trunk Based Development?

- **Goal** - perform small incremental updates to minimise merge conflicts, and streamline the dev pipeline.

- Developers collaborate frequently on a single shared branch: "**trunk**" or "**main**".

- Frequent commits to the trunk, often multiple times a day.

- Short-lived branches are allowed, but are merged back to the **main** branch quickly.

![w:230 h:100 - gitlogo](./images/git-logo.png)

---

## Trunk Based Development Diagram

![w:800 center - Trunk Based Development img](./images/trunk-based-dev.png)

---

## Benefits of Trunk Based Development

- Continuous Integration (CI)
  - Easier to integrate changes continiously.
  - Promotes frequent and smaller releases.

- Reduced marge conflicts
  - Less branching means fewer conflicts to resolve.

- Faster feedback loops.
  - Immediate feedback on changes.

- Simplified Workflow:
  - No need to manage complex branching structures.

---
## Slide 5

Some interesting text

---
## Slide 6

Some interesting text

---

## Splink - CASE Study

Some interesting text

---

## Splink - CASE Study

Some interesting text

---

## Splink - CASE Study

Some interesting text

---

## Questions?

Some interesting text

---

## The End

Thanks!