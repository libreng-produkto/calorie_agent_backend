import requests

BASE_URL = "https://calorieagentbackend-production.up.railway.app"

def test_health():
    resp = requests.get(f"{BASE_URL}/health")
    print(f"Health: {resp.json()}")

def test_chat(message: str, image_path: str = None):
    data = {"message": message}
    files = None
    if image_path:
        files = {"file": open(image_path, "rb")}
    
    resp = requests.post(f"{BASE_URL}/chat", data=data, files=files)
    print(f"Response: {resp.json()}")

def test_chat_with_image(message: str, image_path: str):
    with open(image_path, "rb") as f:
        files = {"file": f}
        data = {"message": message}
        resp = requests.post(f"{BASE_URL}/chat", files=files, data=data)

if __name__ == "__main__":
    print("=== Health Check ===")
    test_health()
    
    print("\n=== Chat Test ===")
    test_chat("I had chicken and rice for lunch")
    
    print("\n=== Image Test ===")
    test_chat("I ate this for breakfast", "/home/hz/CalorieAssistant/image.png")