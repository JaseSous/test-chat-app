import asyncio
import websockets

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
    port = 10000  # Render sẽ dùng cổng này từ biến môi trường
    async with websockets.serve(handler, "0.0.0.0", port):
        print(f"🚀 Server WebSocket chạy trên cổng {port}")
        await asyncio.Future()

asyncio.run(main())
