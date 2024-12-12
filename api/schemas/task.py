from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    # カラム名: 型ヒント  Field(デフォルト値, その他) という形式で記述
    id: int
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")
