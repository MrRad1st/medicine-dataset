import requests
from bs4 import BeautifulSoup

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
              'n','o','p','q','r','s','t','u','v','w','x','y','z']

for character in characters:
    with open("rxlist/links/"+character+".txt", "r") as file:
        file_contents = file.read()
        drugs = file_contents.split("***\n")[:-1]
        print(drugs[-1])
        for drug in drugs:
            data = drug.split("\n")
            name = data[0]
            link = data[1]
            explanations = BeautifulSoup(requests.get(link).text, features="html.parser")\
                    .find('body')\
                    .find('main')\
                    .find('section')\
                    .find('article')\
                    .find('div')\
                    .find_all('section')
            full_explanation = ""
            for paragraph in explanations:
                full_explanation += paragraph.text
            with open('rxlist/drugs/'+name.replace('/','_')+'.txt','w',encoding='utf-8') as file:
                file.write(name+'\n'+link+'\n\n')
                file.write(full_explanation)
                
            print(name)
            
        # exit()
 