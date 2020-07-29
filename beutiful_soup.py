import bs4
import requests

#url to scrap
url="https://www.passiton.com/inspirational-quotes?page=2"

#get response 
response=requests.get(url)

#print(response.content)

#HTML parser
soup=bs4.BeautifulSoup(response.content,'html.parser')
#finding all div with id=all_quotes 
container = soup.find("div",{"id":"all_quotes"})
#finding all img tags from that div
article_element=container.findAll('img')

#print(container)

#for 1st image 
article=article_element[0]

print(article.attrs['src'])

#for only 1 article 
with open('inspiration.jpg','wb') as file:
    #find the image url from div
    img_url=article.attrs['src']
    #request the image url from internet
    response=requests.get(img_url)
    #write the response in file
    file.write(response.content)
    
    
#for all images in article_element 
for i,article in enumerate(article_element):
    with open('inspiration{}.jpg'.format(i),'wb') as file:
        img_url=article.attrs['src']
        #img_url+="https://"
        response=requests.get(img_url)
        
        file.write(response.content)
