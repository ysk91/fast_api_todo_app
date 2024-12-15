from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Tuple, Optional

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


# 受け取ったtask_idに対応するタスクを1つ取得する
# PUTやDELETEの対象taskを取得するために使用
async def get_task(db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
    result: Result = await db.execute(
        # SELECT * FROM tasks WHERE id = task_id
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task: Optional[task_model.Task] = result.first()
    # Resultはタプル型で返すため、[0]でインスタンスを取り出す
    return task[0] if task else None


async def update_task(
        db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
) -> task_model.Task:
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()
