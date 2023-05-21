# WEB SCRAPPING

import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

product_name = input("Search for products : ")
flipkart_url = "https://www.flipkart.com/search?q="+product_name
print(flipkart_url)
urlclient = urlopen(flipkart_url)
flipkart_page = urlclient.read()
flipkart_html = bs(flipkart_page,'html.parser')

# products
product = flipkart_html.find_all('div',{"class":"_1AtVbE col-12-12"})
del product[0:2]
print("Total Product : ",len(product))

# details :
for i in range(len(product)):
    try:
        
        p_name = product[i].find_all("div",{"class":"_4rR01T"})[0].text
        p_rating = product[i].div.find_all("div",{"class":"_3LWZlK"})[0].text
        p_price = product[i].div.find_all("div",{"class":"_30jeq3 _1_WHN1"})[0].text
        print("Product",i+1,":",end="\n")
        print("NAME : ",p_name,end="\n")
        print("Ratings : ",p_rating,end="\n")
        print("Price : ",p_price,end="\n")
        print(end="\n")
    except:
        continue

# To show the entered product
n = int(input("Which product u want to see ? please, Enter the product number : "))
if n > 0 and n<=len(product):
    n = n-1
    print(end="\n")
    p_specification = (product[n].div.find_all("ul",{"class":"_1xgFaf"})[0].text)
    print("Specification : ",end="\n")
    print(p_specification,end="\n")
    print(end="\n")
    print("Here is the LINK of your product : ")
    product_link = "https://www.flipkart.com"+product[n].div.div.div.a['href']
    print(product_link)
    product_page = requests.get(product_link)
    product_html = bs(product_page.text,'html.parser')
    comment = product_html.find_all("div",{"class":"_16PBlm"})
    print(end="\n")
    print("Reviews : ",end="\n")
    print(end="\n")
    for i in comment:
        try:
            clientComment = i.find_all("div",{"class":"t-ZTKy"})[0].text
            comment_star = i.div.div.div.find_all("div",{"class":"_3LWZlK _1BLPMq"})[0].text
            clientname_comment = i.div.div.find_all("p",{"class":"_2sc7ZR _2V5EHH"})[0].text   
            clientComment = clientComment.rstrip('READ MORE')
            print("NAME :",clientname_comment,end="\n")
            print("Rating :",comment_star,end="\n")
            print("Comment :",clientComment,end="\n")
            print(end="\n")
        except:
            continue
    print(end="\n")
else:
    print("Invalid Product id")