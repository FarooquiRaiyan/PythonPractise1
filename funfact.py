import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio import start_server

def get_fun_fact(btn_val=None):
    clear()
    
    put_html(
        '<p align="left">'
        '<h2><img src="" width="7%"> Fun Fact</h2>'
        '</p>'
    
    )
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    response = requests.get(url)
    print(response)
    data = json.loads(response.text)
    fact = data['text']
    style(put_text(fact), 'color:red; font-size: 40px')
    print(data)
    
    put_buttons(
        [dict(label='Click me', value='facts', color='primary')],
        onclick=get_fun_fact
    )
    hold()
    
get_fun_fact(btn_val=None)

