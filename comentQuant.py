import pandas as pd 

path =[
   '/home/anderson/workspace/scraping/quantidade/clube_do_valor_com_data.csv',
   '/home/anderson/workspace/scraping/quantidade/EconoMirna_com_data.csv',
   '/home/anderson/workspace/scraping/quantidade/Economista_sincero_com_data.csv',
   '/home/anderson/workspace/scraping/quantidade/Finanças_com_a_Nath_com_data.csv',
   '/home/anderson/workspace/scraping/quantidade/Gustavo_Cerbasi_com_data.csv',
   '/home/anderson/workspace/scraping/quantidade/Me_poupe_com_data.csv',
   '/home/anderson/workspace/scraping/quantidade/Patricia_lages_com_data.csv'
]
nome = 'Patricia_lages_com_data'
if __name__=="__main__":
    
    #print(df.head())
    
    frame = []
    for p  in path:
        df =pd.read_csv(p)
        frame.append(df)

    result = pd.concat(frame)
    print(result['comentario'].sum())

    #df_ano.to_csv('quantidade/{}.csv'.format(nome))