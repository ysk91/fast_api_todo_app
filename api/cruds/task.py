from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema


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
