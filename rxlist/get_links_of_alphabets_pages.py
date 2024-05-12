import requests

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
              'n','o','p','q','r','s','t','u','v','w','x','y','z']


def get_alphabets_pages():
    # url_example = "https://www.rxlist.com/drugs/alpha_a.htm"
    
    for character in characters:
        t = requests.get("https://www.rxlist.com/drugs/alpha_"+character+".htm").text
        lt = t.split("\n")
        lt = [item for item in lt if item.startswith('<li><a href="https://www.rxlist.com/')]
        with open('rxlist/'+character+'.txt', 'w',encoding='utf-8') as file:
            for item in lt:
                print(item)
                temp = item[len('<li><a href="'):-len('</a></li>')-1]+'\n'
                temps = temp.split('">')
                file.write(temps[0]+'\n'+temps[1])
                
                
get_alphabets_pages()