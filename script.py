import os
import json
import requests

# GitHub Secrets से आपका टोकन यहाँ अपने आप आ जाएगा
token = os.getenv("API_TOKEN")

# यहाँ उस रिपॉजिटरी का यूजरनेम और नाम डालें जिसका डेटा आपको चाहिए
OWNER = "manish62377" 
REPO = "open-source-app-directory"
PATH = "" # अगर किसी खास फ़ोल्डर का डेटा चाहिए तो उसका नाम लिखें, वरना खाली छोड़ दें

url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}"
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # निकाले गए डेटा को data.json नाम की फाइल में सेव करना
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("डेटा सफलतापूर्वक सेव हो गया है!")
else:
    print(f"एरर आया है: {response.status_code} - {response.text}")
