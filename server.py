# server.py (phiên bản websockets >=10)
import asyncio
import websockets

clients = set()

async def handler(websocket):  # chỉ 1 argument
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
    # websockets.serve giờ chỉ cần 2 arguments: handler, host, port
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("🚀 Server đang chạy trên ws://0.0.0.0:8765")
        await asyncio.Future()

asyncio.run(main())
