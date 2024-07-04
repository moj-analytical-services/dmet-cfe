---
marp: true
theme: default
paginate: true
_paginate: skip
---
<style scoped>
section {
  background-color: #1c619d;
  color: #ffffff;
}
a,h2 {
  color: #ffffff;
}
</style>

<img src="https://www.childrenslegalcentre.com/wp-content/uploads/2018/08/MoJ-logo.jpg" width="150px">

# [Monitoring Athena and Data Access](https://github.com/moj-analytical-services/dmet-cfe)

## Centre for Excellence

## July 2024 

---
<style scoped>
section {
  justify-content: flex-start;
  text-align: center;
}
</style>


## Why monitor Athena?

![bg 80%](./images/athena_costs.png)

---

![athena monitoring mindmap](./images/athena_monitoring_mindmap.excalidraw.png)

---

## Overview

0. ### Why monitor Athena?
2. ### Out-of-Scope
3. ### Amazon CloudWatch
4. ### AWS CloudTrail
5. ### Amazon Managed Grafana
6. ### (Proposed) Solution Architecture
7. ### Next Steps

---

## Out of Scope (for now)

- ### Incident response :arrow_right: Application Monitoring

- ### Data Quality Metrics :arrow_right: Data Catalogue 

- ### `create-a-derived-table` model metrics

- ### `create-a-pipeline` non-athena metrics

- ### `airflow` non-athena metrics :arrow_right: Analytical Platform

- ### NLP of Athena queries :arrow_right: :question:

---
<style scoped>
section {
  justify-content: flex-end;
}
</style>

## [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html)

#### What is happening on AWS?

![bg 70%](https://docs.aws.amazon.com/images/AmazonCloudWatch/latest/monitoring/images/CW-Overview.png)

---
<style scoped>
section {
  background-color: #1c619d;
  color: #ffffff;
}
h1 {
  color: #ffffff;
}
</style>

# CloudWatch Demo

Athena Workgroup Metrics

---
## AWS CloudTrail

#### Who did what on AWS?

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ejnlSrZ4eT1_BZPzT0WycA.png)

---
<style scoped>
section {
  background-color: #1c619d;
  color: #ffffff;
}
h1 {
  color: #ffffff;
}
</style>

# CloudTrail Demo

Query AWS Glue APIs

---

## Amazon Managed Grafana

- [Grafana](https://grafana.com/) is an open-source analytics platform that helps you query, visualize, alert on, and understand your metrics wherever they are stored.
- [Amazon Managed Grafana](https://aws.amazon.com/grafana/) is a fully managed service for Grafana.
- You can use it with CloudWatch by adding it as a data source.

- This [table](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/amg-dashboarding-visualization.html) compares Amazon Managed Grafana vs CloudWatch for dashboarding: 
  - Amazon Managed Grafana integrates with AWS Organizations to enable you to read data from AWS sources such as CloudWatch across all your accounts.
  - Grafana provides a larger collection of visualizations.

---
<style scoped>
section {
  background-color: #1c619d;
  color: #ffffff;
}
h1 {
  color: #ffffff;
}
</style>

# Grafana Demo

---

![](./images/athena_monitoring_solution_architecture.excalidraw.png)

---

<style scoped>
section{
  padding: 50px;
} 
li {
  font-size: 25px;
  margin-left: -30px;
}
</style>

## Next Steps

<div class="columns">
<div>

### July:

1. [Use workgroups for Airflow](#14)
1. Add `GetQueryExecution` to CloudWatch
1. Investigate `BatchGetTable`
1. Collaborate with OP discovery
1. OP to add Data and Analytics Engineers to data account
1. OP to add Ireland CloudWatch metrics

</div>

<div>

### August:

1. Set up DMET monitoring working group?
1. [Update dashboards](#15)
1. OP to implement dashboard-as-code?
1. Advertise dashboard with users?
1. AP to terraform Lamdba and `GetQueryExecution` resources?

</div>

<div>

### September:

1. Hand-over Athena monitoring to AP?
1. Convert dashboards to code?
1. Start create-a-derived-table monitoring workstream
1. Refactor DMET applications to use [custom cloudwatch logs](#16)?

</div>

</div>

---
<style scoped>
section {
  background-color: #1c619d;
  color: #ffffff;
}
h1, a {
  color: #ffffff;
}
</style>

# Appendix

---
<style scoped>
section {
    justify-content: flex-start;
}
</style>

## Using Athena workgroups in Airflow 

1. Create `airflow-{folder}` workgroup using [`athena_workgroups.tf`](https://github.com/ministryofjustice/analytical-platform/blob/main/terraform/aws/analytical-platform-data-production/athena/athena-workgroups.tf)

2. Add `mojap-athena-query-dump/{folder}` to Airflow role Athena `dump_bucket`

3. Add `"WR_WORKGROUP": "airflow-dev-workgroup"` to the env_vars dictionary that is passed to the Airflow task

4. That's it!

---

![bg 70%](./images/workgroup_monitoring.excalidraw.png)

---
## Custom CloudWatch Logs

[watchtower](https://github.com/kislyuk/watchtower)  is a lightweight adapter between Python [logging](https://docs.python.org/3/library/logging.html) and CloudWatch Logs

```
import watchtower, logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(watchtower.CloudWatchLogHandler(log_group_name="soumaya_test"))
logger.info(dict(table="apple", details={}))
logger.info(dict(table="banana", details={}))
logger.info(dict(table="orange", details={}))
logger.info(dict(table="apple", details={}))

# Log Insights query:
# stats count(@timestamp) by table
# orange 1
# apple 2
# banana 1
```

---
## [Marp](https://marp.app/) for Slides

- This slide deck was created using [Marp](https://marp.app/) (Markdown Presentation Ecosystem).
- Marp's format is based on [CommonMark](https://commonmark.org/), a consistent Markdown specification.
- For those familiar with [LaTex](https://www.latex-project.org/), it's a way of separating formatting from text, and means you can save documents as code.
- Marp comes with various in-built [themes](https://github.com/marp-team/marp-core/blob/main/themes/README.md).

- I use the default theme, tweaking the color palette to match the [GOV.UK color palette](https://design-system.service.gov.uk/styles/colour/).
- I've put some guidance on the [GitHub as a one-stop-shop](https://ministryofjustice.github.io/data-and-analytics-engineering/blog/posts/github-as-a-one-stop-shop/#slides) blog post (but hoping to run a workshop at some point if there's interest)


<style>
a, h1, h2 {
  color: #1c619d;
}
h1 {
  font-size: 70px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}
</style>