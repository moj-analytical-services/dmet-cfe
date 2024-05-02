import typing as t
from datetime import datetime

import pandas as pd
from sqlmesh import ExecutionContext, model

@model(
    "sqlmesh_example.from_python",
    columns={
        "id": "int",
        "item_id": "int",
        "event_date": "date",
    },
)
def execute(
    context: ExecutionContext,
    start: datetime,
    end: datetime,
    execution_time: datetime,
    **kwargs: t.Any,
) -> pd.DataFrame:
    # get the upstream model's name and register it as a dependency
    table = context.table("sqlmesh_example.from_sql")

    # fetch data from the model as a pandas DataFrame
    # if the engine is spark, this returns a spark DataFrame
    df = context.fetchdf(f"SELECT * FROM {table}")
    df.to_csv('from_python.csv')
    # do some pandas stuff
    # df[id] += 1
    return df