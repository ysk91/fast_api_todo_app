from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task as task_model
import api.schemas.task as task_schema


async def get_tasks_with_done(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await(
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).outerjoin(task_model.Done)
        )
    )

    return result.all()


async def create_task(
    # スキーマを受け取る
    db: AsyncSession, task_create: task_schema.TaskCreate
    # スキーマをモデルに変換する
) -> task_model.Task:
    # インスタンスの作成
    task = task_model.Task(**task_create.dict())
    # DBに保存
    db.add(task)
    await db.commit()
    await db.refresh(task)
    # 作成したインスタンスを返す
    return task
