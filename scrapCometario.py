import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd  
import numpy as np

from lib.Tempo import obterDataPostagem

data=[]#Vetor do Texto

tmp = []#Vetor do Tempo
canal ="https://www.youtube.com/watch?v=4jaWDfTbytA&t=9s"
video_cometario = "Patricia_lages"

sair =1

with Chrome(executable_path=r'lib/chromedriver') as driver:
    wait = WebDriverWait(driver,20)
    driver.get(canal)
    driver.maximize_window()
    time.sleep(5)
    driver.execute_script("window.scrollBy(0 ,450);")

    for item in range(10): 
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)  
    
    for tempo in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#header-author > yt-formatted-string.published-time-text  > a"))):
        tmp.append(obterDataPostagem(tempo.text))

    # >
    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#content > yt-formatted-string#content-text"))):
        data.append(comment.text)
print("{} {}".format(len(data),len(tmp)))
if len(data) == len(tmp):  
    dados = {
        'comentario':data,
        'Postagem':tmp
    }
    df = pd.DataFrame(dados,index=range(0,len(tmp)), columns=['comentario','Postagem'])
    df = df.sort_values(by='Postagem')
    print(df.head(n=20))
    video_cometario = video_cometario.replace(" ",'_')
    df.to_excel('comentariosYoutube/{}_com_data.xlsx'.format(video_cometario), index = False,encoding="utf-8")