from fastapi import APIRouter
router = APIRouter(prefix="/api/sensors")

@router.get("/")
def list_sensors():
    return []

@router.get("/{sensor_id}/data")
def get_sensor_data(sensor_id: int):
    return []
