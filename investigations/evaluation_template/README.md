---
marp: true
theme: moj
paginate: true
_paginate: skip
_class: title
footer: ![image w:40](https://raw.githubusercontent.com/ministryofjustice/marp-moj-theme/main/images/moj.png)
_footer: ''
---

<!-- _header: ![w:100](https://raw.githubusercontent.com/ministryofjustice/marp-moj-theme/main/images/moj.png) -->

# Evaluation Template

## Centre for Excellence

##### Data and Analytics Engineeing

##### July 2024 

---

##  Why follow a Template? 

- Ensures all stakeholders are identified and informed

- Future-proof the solution

- Work around domain barriers

- Minimise duplication

- Speed up development

- Due diligence

![bg left 90%](https://evaluationcanada.ca/client_assets/images/people_hold_arrow.png)

---

## Does ![dltHub](https://cdn.sanity.io/images/nsq559ov/production/7f85e56e715b847c5519848b7198db73f793448d-82x25.svg?w=1800&auto=format) / API Data Extraction need an Evaluation?

- Cross-cutting need for extracting data from APIs (as opposed to niche use case)

- APIs are evolving ([REST vs GraphQL](https://aws.amazon.com/compare/the-difference-between-graphql-and-rest/))

- Multiple stakeholders involved (allow analysts to extract data from APIs?)

- Need to integrate with existing data and and analytics engineering tech stack

- Alternatives are available e.g. [Meltano](https://meltano.com/)

- dltHub can be used for more than extracting data from APIs so there is a risk of expansion and duplication

---

<style scoped>
.columns {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
p, li {
  font-size: 25px;
}
</style>

## Proposed Approach

Modified from 2023 [Iceberg Evaluation](https://miro.com/app/board/uXjVMNUs7Pg=/) and [RFCs](https://leaddev.com/process/thorough-team-guide-rfcs)

<div class="columns">

<div>


#### Investigation

1. Set up a (cross-domain) working group
1. Understand capabilities / use-cases
1. Complete [whether to RFC](./images/whether_to_rfc.excalidraw.png)
1. Present at Community Forum / Tech Review

</div>

<div>

####  Evaluation

1. Complete [RFC Template](./rfc_template.md)
1. Optional:
    1. Identify [Personas / Users](./images/persona.excalidraw.png)
    1. Identify & Prioritise [Evaluation Criteria](./images/evaluation_criteria.excalidraw.png)
    1. Create customised [User Story Map](./images/data_engineering_story_map.excalidraw.png)
1. Complete Evaluation
1. Present at Community Forum / Tech Review

</div>

</div>

---

## Whether to RFC

![whether to RFC](./images/whether_to_rfc.excalidraw.png)

---

## Personas / Users

![persona](./images/persona.excalidraw.png)

---

## Evaluation Criteria

![evaluation criteria](./images/evaluation_criteria.excalidraw.png)

---

## Data Engineer Story Mapping

![data engineer story mapping](./images/data_engineering_story_map.excalidraw.png)

