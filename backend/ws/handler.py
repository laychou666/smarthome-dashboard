from fastapi import WebSocket
async def sensor_ws(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_json({"type": "sensor_update", "data": data})
