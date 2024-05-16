import requests

BASE = "https://ideal-fiesta-v6wrr7r967v26wwj-5000.app.github.dev/"

response = requests.get(BASE + "helloworld/sroshsafa/14")
data = response.text
print(data)
print(data.json())