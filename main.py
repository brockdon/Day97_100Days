import os,json,requests,openai
from bs4 import BeautifulSoup

openai.api_key = os.environ["openaiAPIkey"]
openai.organization = os.environ["organisationID"]
openai.Model.list()

url = "https://en.wikipedia.org/wiki/Hair_loss"

response =requests.get(url)
html = response.text

soup =BeautifulSoup(html,"html.parser")

references = soup.find_all("cite",{"class":"citation journal cs1"})
text = soup.find_all("p")
promptText = []

for t in text:
  promptText.append(t.text)
  
prompt = f"Summarize the text of this HTML page in no more than 3 paragraphs {promptText}"
openaiResponse = openai.Completion.create(model ="text-davinci-002",prompt=prompt,temperature =0,max_tokens =200)
queryresult = (openaiResponse['choices'][0]['text'].strip())
print (queryresult)
count =0
print("References:")
for reference in references:
  count +=1
  print(f"{count} {reference.text}")
  if count >=3:
    break
  else:
    pass