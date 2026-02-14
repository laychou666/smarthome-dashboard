from fastapi import HTTPException
class SensorNotFound(HTTPException):
    def __init__(self, sensor_id: int):
        super().__init__(status_code=404, detail=f"Sensor {sensor_id} not found")
