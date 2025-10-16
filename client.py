import asyncio
import websockets

async def chat():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("✅ Kết nối thành công!")
        
        async def receive():
            while True:
                msg = await websocket.recv()
                print(f"\n👤 Người khác: {msg}")

        asyncio.create_task(receive())

        while True:
            msg = input("Bạn: ")
            if msg.lower() == "exit":
                break
            await websocket.send(msg)

asyncio.run(chat())
