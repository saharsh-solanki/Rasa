
import requests
from bs4 import BeautifulSoup

URL = "https://in.indeed.com/java-developer-jobs-in-Ujjain,-Madhya-Pradesh"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
result = soup.find_all('a')


for p in result:
	t=p.find("h2",class_="jobTitle jobTitle-color-purple")
	if t==None:
		pass
	else:
		print(t.get_text())