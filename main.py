from bs4 import BeautifulSoup
from urllib import request

url = "https://petittube.com/"
page=request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
result=soup.find('iframe')
result=result["src"]
code=result[30:41]
urlfinal="https://www.youtube.com/watch?v=" + code
print(urlfinal)