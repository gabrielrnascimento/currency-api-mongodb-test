from pydantic import BaseModel
from datetime import datetime


class Currency(BaseModel):
    currency_code: str
    rate: float
    backed_by: str = "USD"
    currency_type: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
