from pydantic import BaseModel
from datetime import datetime
class SensorReading(BaseModel):
    sensor_id: int
    value: float
    timestamp: datetime
class Sensor(BaseModel):
    id: int
    name: str
    type: str
    location: str
