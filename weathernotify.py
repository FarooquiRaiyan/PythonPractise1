import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


n = ToastNotifier()


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

def getdata(url):
    r = requests.get(url, headers=headers)
    return r.text



res = getdata("you site url")




soup = BeautifulSoup(res, 'html.parser')
weather_blocks = soup.select('div.body-item')   #will be different for different sites 


for block in weather_blocks:
    # print(block)
    if block.p:
        head1  =block.p.text    
        head2 =  block.p.b.text
        print("Estimated Temperature: " ,block.p.b.text)
        n.show_toast(head1,head2,duration=5)
