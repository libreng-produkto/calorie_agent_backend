import requests

BASE_URL = "https://calorieagentbackend-production.up.railway.app"

def test_health():
    resp = requests.get(f"{BASE_URL}/health")
    print(f"Health: {resp.json()}")

def test_chat(message: str, images: list = None):
    payload = {"message": message}
    if images:
        payload["images"] = images
    
    resp = requests.post(f"{BASE_URL}/chat", json=payload)
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
    test_chat_with_image(
        "I ate this for breakfast", 
        image_path=["/home/hz/CalorieAssistant/image.png"]
    )