import requests

url = 'https://stb-beton.novacode.uz/api/client/company-branch-list/'
headers = {
    'Authorization': 'ajdiw08hh802h8f0430hf803hf39fh934hf39yfbrbfb39h4u34hfuADEDWEFDj',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Xatolik yuz berdi: {response.status_code}")

