---
marp: true
lang: en-US
title: Codebase Collaborator
description: LLMs for source code analysis and augmentation
theme: uncover
transition: fade
paginate: true
_paginate: false
---

<style scoped>
section {
  background-color: #8ecae6;
}
</style>

# <img src="https://sqlmesh.readthedocs.io/en/stable/sqlmesh.png"> SQLMesh Evaluation

## May 2024

---

# Demo

- Jupyter Notebook for SQL Mesh

- [Elementary with create-a-derived-table](https://github.com/moj-analytical-services/create-a-derived-table/pull/1404)

---

# Must Haves

Tool | Athena Adapter| Unit Testing | Model Generation | 
-| - | - | -| 
DBT| :white_check_mark:| :star: | :wrench: | 
SQLMesh| :hourglass_flowing_sand: | :star::star:| :wrench: |

<!-- 
Athena Adapter: SQLMesh has trino adapter, and we could potentially build it ourselves

Model Generation: Neither has in-built support for model generation so we would need to build a custom solution, but SQLMesh has the concept of a load class where you could dynamically generate N models and have them be recognized by SQLMesh as if they were defined in your file system.
See https://tobiko-data.slack.com/archives/C044BRE5W4S/p1714598530943139 for more details.

Unit Testing: Both (>=dbt.1.8) have support for unit testing of models. SQLMesh uses python-based macros so you can use pytest for unit testing macros.
-->

---

# Should Haves

Tool |  Airflow Integration | Incremental Models | Monitoring
-| - | - | - | 
DBT| :wrench: | :star: | :white_check_mark: | 
SQLMesh| SQL  | :star::star: | :dollar: |

<!-- 
Airflow Integration: It's possible to kick-off a dbt build from Airflow, whereas with SQLMesh you can create a DAG per model. Wouldn't work with python models which run where SQLMesh is installed, instead of K* cluster

Monitoring: You can integrate dbt with elementary and track model-level metrics. SQLMesh enterprise has native support for monitoring, otherwise you use Airflow UI to monitor individual models.

Incremental Models: Both have support for incremental models but SQLMesh uses a more powerful interval-based approach see https://tobikodata.com/data_load_patterns_101.html for more details. 
-->

---

# Nice to Haves

Tool | Column Lineage | Python Models | Preview | 
-| - | - | -| 
DBT| :x: | :star: | :x: | 
SQLMesh| :white_check_mark: | :star::star:| :white_check_mark: |

<!-- 

Column Lineage: SQLMesh is able to track column lineage for SQL models but not python models

Python Models: dbt-athena supports Athena Spark python models, whilst SQLMesh supports both spark and local python models.

Preview: SQLMesh is able to preview changes before deploying them.
-->

---

## Conclusion

- Liaise with AP team and ? domain team [elementary](https://www.elementary-data.com/) on deploying elementary

- Work with observability platform to visualise the stats

- Work with HMCTS team to agree naming approach

- Pause on SQLMesh for now

- Pause on implementing incremental models for curation


<style>
section {
  color: 	#003078;
}
</style>
