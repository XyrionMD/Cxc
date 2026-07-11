import os, requests
from config import CVT
from colors import C

API_KEY = f"{CVT.API}"
MODEL_AI = f"{CVT.MODEL}"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_AI}:generateContent?key={API_KEY}"

history = []

def show_help():
    print("""
AI ChatBot V21.0
<==> <==> <==> <==> <==> <==> <==> <==>
- help           | menampilkan menu ini
- quit           | untuk keluar
<==> <==> <==> <==> <==> <==> <==> <==>
          """)

def askAI():
    os.system("clear")
    os.system("figlet 'AI Chat' | lolcat")
    while True:
        try:
            askcvt = input(f"{C.RED}You >>>{C.RESET} ").strip()
            if askcvt.lower() == "quit":
                break
            elif askcvt.lower() == "help":
                show_help()
                continue
            if not askcvt.strip():
                continue

            history.append({
                "role": "user",
                "parts": [{"text": askcvt}]
            })

            SYS_PROMPT = f"{CVT.AI_PROMPT}"

            payload = {
                    "system_instruction": {
                        "parts": [{"text": SYS_PROMPT}]
                    },
                    "contents": history
            }

            headers = {
                    "Content-Type": "application/json"
            }

            response = requests.post(URL, json=payload, headers=headers)
            response.raise_for_status()

            data = response.json()
            ai_response = data['candidates'][0]['content']['parts'][0]['text']
            print(f"{C.BLUE}{CVT.NAME_OF_AI} >>>{C.RESET} {ai_response}")

            history.append({
                "role": "model",
                "parts": [{"text": ai_response}]
            })
        except requests.exceptions.RequestException as e:
            print(f"Connection Error {e}")
            history.pop()


