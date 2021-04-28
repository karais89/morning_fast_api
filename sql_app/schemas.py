from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass

# 이제 API에서 데이터를 반환 할 때 데이터를 읽을 때 사용할 Pydantic 모델(스키마)을 만듭니다.
# 예를 들어 item을 만들기 전에 할당 된 ID가 무엇인지 알 수 없지만 item을 읽을 때 (API에서 반환 할 때) 이미 해당 ID를 알고 있습니다.
# 
class Item(ItemBase):
    id: int
    owner_id: int

    # 이제 읽기를위한 Pydantic 모델에서 내부 Config 클래스를 추가합니다. 
    # 이 Config 클래스는 Pydantic에 구성을 제공하는 데 사용됩니다. 
    # Config 클래스에서 orm_mode = True 속성을 설정합니다.
    # Pydantic의 orm_mode는 Pydantic 모델이 딕셔너리가 아니라 ORM 모델 (또는 속성이있는 다른 임의의 개체)이더라도 데이터를 읽도록 지시합니다.
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str

# 위와 같은 방식으로 사용자를 읽을 때 이제 item에 이 사용자에게 속한 items 포함되도록 선언 할 수 있습니다.
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
