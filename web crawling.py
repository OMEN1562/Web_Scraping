import requests
import json
import pandas as pd
file = "ID.csv"
file_pd = pd.read_csv(file).values
reshaped = file_pd.reshape(-1,)


url = "http://api.icndb.com/jokes/json?"
parameter = {"value" : ""}
response = requests.get(url, params=parameter)
content = response.content
json_content = json.loads(content)
value = json_content["value"]
a = []
for i in range(len(value)):
    if value[i]["id"] in reshaped:
        a.append(value[i]["joke"])
dp = pd.DataFrame({'ID': reshaped, 'Joke' : a})
dp.to_csv("new.csv",index = False)