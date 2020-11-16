from socialblade import YouTubeChannel
import csv
from datetime import datetime
import locale
import numpy as np
import pandas as pd
locale.setlocale(locale.LC_ALL, '')

data=[]

def create_more_readable_ints(integer):
    valor = locale.currency(integer, symbol=False, grouping=True).replace('.00', '').replace(',', "'")
    return valor


pewdiepie_channel = YouTubeChannel('UC8mDF5mWNGE-Kpfcvnn0bUg')
nomeCanal ="Me poupe!"

for video in pewdiepie_channel.get_most_viewed_videos():
    try:
        vdeo = [
                video.title,
                str(video.created_at),
                create_more_readable_ints(video.views_num),
                create_more_readable_ints(video.comments_num)
            ]
        data.append(vdeo)
    except Exception as e:
         print(str(e))

dta_np = np.array(data)

df = pd.DataFrame(dta_np,index=range(0,len(data)),columns=['Titulo', 'Postado', 'Visualizacao', 'comentarios'])
df.sort_values(by=['Visualizacao','Postado'], inplace=True,ascending=[False,False])
nomeCanal = nomeCanal.replace(' ','_')
df.to_csv('dadosCanal/{}.csv'.format(nomeCanal))
print(df.head())