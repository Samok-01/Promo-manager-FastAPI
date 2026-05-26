from pydantic import BaseModel, Field, field_validator
from typing import Optional

# --- Создание промокода (входящие данные) ---
class PromoCreate(BaseModel):
    code: str
    discount_percent: int = Field(..., ge=1, le=90)
    valid_until_days: int
    is_active: bool = True
    max_uses: int

    @field_validator("code")
    @classmethod
    def uppercase_code(cls, v: str) -> str:
        return v.upper()

# --- Обновление промокода (все поля необязательные) ---
class PromoUpdate(BaseModel):
    is_active: Optional[bool] = None
    valid_until_days: Optional[int] = None

# --- Ответ клиенту (исходящие данные) ---
class PromoOut(BaseModel):
    id: int
    code: str
    discount_percent: int
    valid_until_days: int
    is_active: bool
    max_uses: int

    model_config = {"from_attributes": True}

# --- Применение промокода ---
class ApplyRequest(BaseModel):
    code: str
    initial_cart_sum: float

class ApplyResponse(BaseModel):
    final_sum: float
    saved: float