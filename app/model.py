from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional


class Currency(BaseModel):
    currency_code: str
    rate: float
    backed_by: str = "USD"
    currency_type: Optional[str]
    created_at: Optional[datetime] = datetime.utcnow()
    updated_at: Optional[datetime] = datetime.utcnow()
