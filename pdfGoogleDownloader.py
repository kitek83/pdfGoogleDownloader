#Program, uses google search to find query. If the file is in pdf, then is downloaded.
try:
    from googlesearch import search
except ImportError:
    print('Sth was wrong.')
import requests

query = 'Norway pdf'
count = 0
for j in search(query,num=8,stop=8,pause=3):
    count += 1
    if j.endswith('.pdf'):
        print(f'{count}.{j}')

        #downloading the file pdf
        page = requests.get(j)
        file = open(f'Norway{count}.pdf','wb')
        for chunk in page.iter_content(100000):
            file.write(chunk)