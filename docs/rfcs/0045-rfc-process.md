- RFC PR: https://github.com/moj-analytical-services/dmet-cfe/pull/45
- Related:


## Summary

Use GitHub Discussions to document proposed design changes as lightweight [RFCs](https://leaddev.com/process/thorough-team-guide-rfcs), placing each one in the most relevant repository. Add the 'RFC' label to make them easy to search across multiple repositories.

## Example

This discussion!

## Motivation

Data and analytics engineering teams are already using GitHub discussions to propose design changes e.g. [dimensional and data marts](https://github.com/moj-analytical-services/create-a-derived-table/discussions/1873). These are stored in multiple repositories. This RFC proposes a consistent, light-weight documentation approach for such design changes that makes it easy for people to find.

## Detailed Design

1. Add Discussion template with the category "RFC", labels "RFC" "Draft" and following headings based on vuejs [RFC template](https://github.com/vuejs/rfcs/blob/master/0000-template.md):
  a. Summary
  b. Example (if applicable)
  c. Motivation
  d. Detailed design
  e. Drawbacks
  f. Alternatives
  g. Deployment strategy
  h. Unresolved questions
1. Once ready, set discussion label to "Discussion"
1. Once agreed, set discussion label to "Active" and lock conversation
1. Otherwise, close discussion as outdated
1. Use discussion title as RFC title (no need to add "RFC" prefix)
1. No need to generate RFC ID since you can use the GitHub-generated URL ID
1. To find relevant RFCs, search by label "RFC" e.g. [test](https://github.com/search?q=+test+label%3ARFC++++org%3Amoj-analytical-services+org%3Aministryofjustice+&type=discussions) instead of searching by category because doesn't work [when searching globally](https://github.com/orgs/community/discussions/136763)
1. Chase Github about adding [discussions to projects](https://github.com/orgs/community/discussions/11223) so that in the future we can set status and flag all RFCs in a shared GitHub project

## Drawbacks

- GitHub discussion search is less advanced that GitHub code search 
- GitHub discussions cannot be added to GitHub projects
- Harder to track changes to RFC within discussion summary

## Alternatives

### Store RFCs in Markdown and associate with PR

Based on [reactjs RFC Process](https://github.com/reactjs/rfcs?tab=readme-ov-file#what-the-process-is):
- Store RFCs in Markdown and associate with PR
- Make sure that RFC title and ID matches with PR title and ID
- Merge in RFC once Active
- Use PR status to reflect RFC status (but not superseded): Draft | Ready for review | Merged | Closed without merging
- Colleagues can provide feedback on PR through comments

Cons:
- More complicated than creating/updating GitHub discussion which can discourage people from writing RFCs
- Easy to end up with more than one PR per RFC which messes up workflow
- PR comments have less features than discussion comments
- RFC text cannot be searched until PR is merged

Pros:
- PRs can be added to a centralised GitHub project, unlike Discussions
- Easier to track changes to RFC using git
- RFC and comments about the RFC are more clearly separated and less likely to "bleed" into each other
- PR status provides intuitive mechanism for tracking RFC status
- During the commenting phase, comments can be explicitly linked to specific lines

### Store RFCs in Issues with label "RFC"

Similar to using GitHub discussions but using GitHub issues instead.

Cons:
- Counterintuitive to store RFCs as an issue
- Issue comments have less features than discussion comments

Pros:
- Issues can be added to a centralised GitHub project and assigned a status 
- GitHub has better support for searching Issues than discussions
- GitHub has better support for Issue API than discussion API

### Any Github-based strategy, as long as same headings and label "RFC"

Allow teams to choose how they document design proposals, as long as they use the same headings and the label "RFC". 

Cons:
- Could be confusing

Pros:
- Allows teams to choose the strategy that best meets their needs

## Adoption Strategy

- Ensure that new design changes us this approach
- Add 'RFC' label to historic github discussions that document design changes

## Unresolved questions

1. How to notify people when a GitHub discussion has been created that they might be interested in
2. What is the next step e.g. creating [ADR](https://adr.github.io/)
