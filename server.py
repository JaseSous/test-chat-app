import asyncio
import websockets
import os

clients = set()

async def handler(websocket):
    clients.add(websocket)
    print(f"✅ Client mới kết nối ({len(clients)} người online)")
    try:
        async for message in websocket:
            print(f"📩 Nhận: {message}")
            for client in clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("❌ Client ngắt kết nối")
    finally:
        clients.remove(websocket)

async def main():
    port = int(os.environ.get("PORT", 10000))  # ✅ dùng PORT từ Render
    async with websockets.serve(handler, "0.0.0.0", port):
        print(f"🚀 Server WebSocket chạy trên cổng {port}")
        await asyncio.Future()

asyncio.run(main())
