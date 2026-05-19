import requests

BASE_URL = "http://localhost:8000"

def test_health():
    resp = requests.get(f"{BASE_URL}/health")
    print(f"Health: {resp.json()}")

def test_chat(message: str, images: list = None):
    payload = {"message": message}
    if images:
        payload["images"] = images
    
    resp = requests.post(f"{BASE_URL}/chat", json=payload)
    print(f"Response: {resp.json()}")

if __name__ == "__main__":
    print("=== Health Check ===")
    test_health()
    
    print("\n=== Chat Test ===")
    test_chat("I had chicken and rice for lunch")
    
    print("\n=== Image Test ===")
    test_chat(
        "I ate this for breakfast", 
        images=["/home/hz/CalorieAssistant/image.png"]
    )