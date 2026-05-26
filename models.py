from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Promo(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)
    discount_percent = Column(Integer, nullable=False)
    valid_until_days = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    max_uses = Column(Integer, nullable=False)