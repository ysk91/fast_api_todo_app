from typing import Optional

from pydantic import BaseModel, Field


# スキーマの共通部分を TaskBase として定義
# 継承元のBaseModelはPydanticの基底クラスで、FastAPIのスキーマモデルであることを表す
class TaskBase(BaseModel):
    # カラム名: 型ヒント  Field(デフォルト値, その他) という形式で記述
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")


# GET /tasks で返すレスポンスのスキーマ
# TaskBaseを継承して、idとdoneを追加
class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True


# POST /tasks で受け取るリクエストのスキーマ
class TaskCreate(TaskBase):
    pass


# POST /tasksした後のレスポンスのスキーマ
class TaskCreateResponse(TaskCreate):
    id: int


    class Config:
        orm_mode = True
