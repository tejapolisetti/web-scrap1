from selenium import webdriver
driver=webdriver.Chrome('')
driver.get("https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&ref_=adv_prv")
ans=[]
for i in range(10):
    temps=driver.find_elements_by_class_name('lister-item-content')
    for temp in temps:
        title=temp.find_element_by_class_name("lister-item-header")
        title=temp.find_element_by_tag_name("a")
        title=title.text
        print(title)

        rate=temp.find_element_by_class_name("ratings-imdb-rating")
        rate=rate.text
        print(rate)

        casts=[]
        cast=temp.find_elements_by_tag_name("p")
        cast=cast[2]
        cast=cast.find_elements_by_tag_name("a")
        for j in cast:
            casts.append(j.text)
        print(casts)
    
        print()
    
    if(i==0):
        break

    btn=driver.find_element_by_class_name('next-page')
    btn.click()







