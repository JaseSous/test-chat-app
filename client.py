# client.py
import websocket
import threading
import time

URL = "wss://test-chat-server-j9ik.onrender.com"

def receive_messages(ws):
    """Luồng nhận tin nhắn từ server"""
    while True:
        try:
            msg = ws.recv()
            if msg:
                print(f"\n💬 Tin nhắn: {msg}\n> ", end="")
        except:
            break

def main():
    ws = websocket.WebSocket()
    ws.connect(URL)
    print(f"✅ Đã kết nối đến {URL}")
    print("Gõ tin nhắn và nhấn Enter để gửi")

    # Tạo luồng nhận tin nhắn
    threading.Thread(target=receive_messages, args=(ws,), daemon=True).start()

    # Gửi tin nhắn từ terminal
    while True:
        try:
            msg = input("> ")
            if msg.strip().lower() == "exit":
                break
            ws.send(msg)
        except KeyboardInterrupt:
            break

    ws.close()
    print("🔌 Đã ngắt kết nối")

if __name__ == "__main__":
    main()
