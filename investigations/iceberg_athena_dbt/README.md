---
marp: true
lang: en-US
title: Codebase Collaborator
description: LLMs for source code analysis and augmentation
theme: moj
transition: fade
paginate: true
_paginate: skip
_class: title
footer: ![image w:40](https://raw.githubusercontent.com/ministryofjustice/marp-moj-theme/main/images/moj.png)
_footer: ''
---

<!-- _header: ![w:100](https://raw.githubusercontent.com/ministryofjustice/marp-moj-theme/main/images/moj.png) -->

## Building a transaction data lake  using<br/> [Amazon Athena, Apache Iceberg and dbt](https://moj-analytical-services.github.io/dmet-cfe/iceberg_athena_dbt)

<br/>

### Dr Soumaya Mauthoor

September 2024

---
<style scoped>
section {
  justify-content: flex-end;
}
</style>

![bg 70%](https://assets.publishing.service.gov.uk/media/6241e4dae90e075f06b37247/digi-strategy-2025.jpg)

Published in 2022 under the Johnson Conservative government

<!-- 
https://intranet.justice.gov.uk/blog/becoming-a-truly-data-led-justice-system/

Our data strategy:

We will improve justice outcomes through data driven insight and innovation.
We will ensure data meets user needs.
We will build a data culture to value data as a strategic asset.
-->

---
## MoJ Analytical Platform

</br>

![w:800](https://user-guidance.analytical-platform.service.justice.gov.uk/images/overview/analytical-platform.excalidraw.png)

![bg right:40% w:90%](./images/cjs_dashboard.png)

--- 

<style scoped>
p { text-align: center; }
</style>

## Previous ELT Architecture

![](./images/previous_etl_architecture.excalidraw.png)

---

<style scoped>
p, h5 { 
  text-align: center; 
}
</style>

## Modern Table Formats

<!-- Provide a table-like abstraction on top of native file formats like Parquet by storing additional metadata. -->

![w:1200](https://miro.medium.com/v2/resize:fit:720/format:webp/1*H_goBvOV52AUid4egopzGw.png)

##### **Iceberg** was the obvious choice for our usecase because of enhanced Athena support


---

<style scoped>
li { 
  font-size: 25px; 
}
</style>


## Glue PySpark vs Athena Curation Benchmarking

![bg left w:600](./images/athena_vs_glue.excalidraw.png)

**Criteria**
1. Cost
2. Complexity
3. Run Time

**Dataset**

TPCDS stores_sales

- scale: 100 (~10GB)
- scale: 3000 (~400GB)

---
## Bulk Insert

<br/>

```
CREATE TABLE target_table
AS SELECT * FROM source_table
```
<br/>

- Athena is cheaper <=3TB scale
- Glue PySpark is faster at the 3TB scale

![bg left w:550](./images/bulk_insert.png)

---
## SCD2 Merge

Update 0.1% rows 

```
MERGE INTO target_table
USING source_query
ON search_condition
WHEN MATCHED THEN UPDATE []
WHEN NOT MATCHED THEN INSERT []
```
<br/>

- Athena is cheaper and faster
- Glue PySpark runs out of memory at the 3TB scale

![bg left w:550](./images/scd2_merge.png)

---

<style scoped>
p { 
  text-align: center; 
}
</style>

## Full Load Blue-Green Deployment

![w:750](./images/wap.excalidraw.png)

---

<style scoped>
p { 
  text-align: center; 
}
</style>

## Incremental Blue-Green Deployment

![w:750](./images/wap_incremental.excalidraw.png)

---

## Outcomes

![bg left w:600](./images/glue_vs_athena_costs.png)

- Reduced query costs by 99%

- Reduced query time by 50-75%
- Enabled daily refresh cycle
- Stabilised data pipeline
- Ensured data quality
- Streamlined technology stack
- Facilitated phased development

---

<!-- _class: title -->
<style scoped>
p { 
  font-size: 20px; 
}
</style>

# Questions?

<br/>
<br/>
<br/>
<br/>

These slides were created using <img style="width:100px" src="https://github.com/marp-team/marp/raw/main/marp-dark.png">

