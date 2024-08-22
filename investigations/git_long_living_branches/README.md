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

![bg right:40%](./images/code-tree.png)

### August 2024

---

## Why?"

-

![bg left:20% 100%](https://evaluationcanada.ca/client_assets/images/people_hold_arrow.png)

---

## What? - Long Living Feature Branches (Git-flow)

- **Goal - Simplify release management and isolating feature development.**

- Feature based development ([Git-Flow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow))

- Developers create separate, long lived branches for individual features.

- Depending on complexity, feature branches can be active for days, weeks or months.

- Once the feature is complete and thoroughly tested, it can be merged back into the main branch.

![w:230 h:100 - gitlogo](./images/git-logo.png)

---

## Gitflow Diagram

![w:10000 center - Git-flow img](./images/git-flow.png)

---

## Benefits of Git-flow

- Isolation of work:
  - Features are developed independently, reducing the risk of conflicts.

- Controlled Integration:
  - Code is reviewed and tested before merging.

- Supports Complex Projects:
  - Easier to manage large, multi-feature projects.

- Flexibility:
  -  Different branching strategies can be adapted to team needs.

---

## Disadvantages of Git-flow

- Complexity
  - Managing multiple branches can become complicated.

- Long Living Branches
  - Feature branches can diverge significantly, leading to merge conflicts.

- More Overhead.
  - Time consuming to review PR's and testing.

---

## What is Trunk Based Development?

- **Goal** - perform small incremental updates to minimize merge conflicts, and streamline the dev pipeline.

- Developers collaborate frequently on a single shared branch: "**trunk**" or "**main**".

- Frequent commits to the trunk, often multiple times a day.

- Short-lived branches are allowed, but are merged back to the **main** branch quickly.

![w:230 h:100 - gitlogo](./images/git-logo.png)

---

## Trunk Based Development Diagram

![w:1000 center - Trunk Based Development img](./images/trunk-based-dev.png)

---

## Benefits of Trunk Based Development

- Continuous Integration (CI)
  - Easier to integrate changes continuously.
  - Promotes frequent and smaller releases.
- Reduced marge conflicts
  - Less branching means fewer conflicts to resolve and less code to review.
- Faster feedback loops.
  - Immediate feedback on changes.
- Avoids clashes with other features in development.

---

## Disadvantages of Trunk Based Development

- Requires Discipline
  - Developers must commit to working code frequently.

- Risk of Breaking Changes
  - Changes committed to the trunk can affect all devs.

- Not ideal for Large Teams
  - Scaling can be challenging in large and distributed teams.

---

<h2>
  <img src="./images/splink-logo.png" alt="Splink Logo" style="width: 200px; vertical-align: middle; margin-right: 10px;">
  CASE Study
</h2>


#### **Background**

In Autumn of 2023, we decided to undertake a **major refactor of Splink**. This refactor was a necessary step to help us improve the performance and maintainability of the library.

However, for the first few months of this process, we had ongoing development in both versions 3 and 4. **This was due to**:

- Team members were actively developing data linking pipeline features, all required in version 3.
- There were ongoing features in version 3 that needed finalisation.

---

<h2>
  <img src="./images/splink-logo.png" alt="Splink Logo" style="width: 200px; vertical-align: middle; margin-right: 10px;">
  The problem
</h2>

Initially, we were infrequently merging changes from the main branch into our development branch. This led to regular divergences between the two versions and we were constantly resolving relatively large **merge conflicts**.

#### **This raised a question around version synchronisation:**
- What's the best strategy for keeping the new version updated with changes from the main branch?

---

<h2>
  <img src="./images/splink-logo.png" alt="Splink Logo" style="width: 200px; vertical-align: middle; margin-right: 10px;">
  A solution?
</h2>


- **GitHub Action creating merge branch on push to main**
  - Automatically create a new merge branch (`main` -> `splink_4_dev`) on push to the main branch
  - If no merge conflicts are detected, we could then create and merge the PR
  - If conflicts were present, we then had earlier sight of them


<br>

This ensured `splink_4_dev` was consistently updated with changed from the main branch, with regular merge PRs replacing ad-hoc updates.

---

<h2>
  <img src="./images/splink-logo.png" alt="Splink Logo" style="width: 200px; vertical-align: middle; margin-right: 10px;">
  Findings from experiment - Pros
</h2>

### **Pros**

- **Reduced manual intervention**: Eliminated the need for reminders or scheduling, ensuring continuous integration without extra effort.
- **Reduced size of conflicts**: Reduced the potential for large merge conflicts. Particularly troublesome to resolve as multiple developers were working on the same codebase.

---

<h2>
  <img src="./images/splink-logo.png" alt="Splink Logo" style="width: 200px; vertical-align: middle; margin-right: 10px;">
  Findings from experiment - Cons
</h2>

### **Cons**

- **Didn't solve all of our problems**: While it helped with synchronisation, it didn't fundamentally fix our issues with a divering codebase and stale code.
    - Required the structure of each branch remain consistent, which was only feasible in early development.
- **Overkill for our needs**: A simpler notification system might have been more appropriate and less faff to set up.

---

<h2>
  <img src="./images/splink-logo.png" alt="Splink Logo" style="width: 200px; vertical-align: middle; margin-right: 10px;">
  Case Study Summary
</h2>

Overall, this solution worked __acceptably__. The main benefit was in allowing us to quickly review if/where merge conflicts were occurring. We could then identify and resolve issues early on.

However, it didn't fundamentally resolve a lot of the issues we were encountering with the branches steadily diverging. Later in development we decided to stop actively working on version 3, and focus on version 4.

---


## create-a-pipeline - Linting

- [PR - #350](https://github.com/moj-analytical-services/airflow-create-a-pipeline/pull/350)

- Refactor all of our linting tools.

- Everyone was on different components, and it was a major change on how we approached linting in the codebase.

- Used long living branches to manage each componential change.

---

## 


![bg w:800 h:650](./images/linting-main-pr.png)

---

##  Linting

![bg 90%](./images/linting-prs.png)

---

## Best Practices

- TBD
  - Commit often with small incremental changes
  - Use feature toggles to manage incomplete features

- Feature-Based
  - Keep branches short-lived to minimize divergence.
  - Ensure thorough code reviews and testing before merging.
  - Regularly rebase feature branches on the main branch to reduce conflicts.

---

## Other Best Practices

- Pair experienced developers with those new to a codebase.
- Communication, Communication, Communication


---

## Strategies from the wild:

-


-

---


## Questions?

- What have people done before which has been successful?
- What should be considered a long living branch? (*a few days, weeks? etc.*)
  How long is too long? (*Month? Year?*)
- Other strategies for managing long living branches.

---

## The End

Thanks!

---

## References
        
- [Git Branching Strategies vs Trunk Based Development - Launch Darkly BLOG](https://launchdarkly.com/blog/git-branching-strategies-vs-trunk-based-development/)
    
- [Git Branching Strategies - Medium](https://medium.com/@sreekanth.thummala/choosing-the-right-git-branching-strategy-a-comparative-analysis-f5e635443423)

- [Git Workflow - Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

- [Trunk-Based Development - Atlassian](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development)