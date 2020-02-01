from bs4 import BeautifulSoup
from  urllib.request import urlopen
from urllib.request import urlretrieve
import requests
import os

p = -1
page = 1

for i in range(int(page)):
    p += 1
    html = urlopen("https://mm131.pro/e/action/ListInfo/index.php?page=" + str(p) + "&classid=1").read()
    soup = BeautifulSoup(html,features="lxml")
    dl_soup = soup.find_all("dl",{"class":"list-left public-box"})
    for ssp in dl_soup:
        dd_soup = ssp.find_all("dd")[:-1]
        for ddp in dd_soup:
            dd_href = ddp.find_all("a")
            for a_href in dd_href:
                all_href = "https://mm131.pro" + a_href["href"]
                all_title = a_href.find_all("img")
                for dir_name in all_title:
                    dir_img = dir_name["alt"]
                    all_dir = "mm131/" + dir_img
                    os.makedirs(all_dir,exist_ok=True)
                all_html = urlopen(all_href).read()
                all_soup = BeautifulSoup(all_html,"lxml")
                page_url = all_soup.find_all("div",{"class":"content-pic"})
                for all_page in page_url:
                    page_href = all_page.find_all("a")
                    pageone_img = all_page.find_all("img")
                    for one_alt in pageone_img:
                        oneall_alt = one_alt["alt"]
                        oneimg_url = one_alt["src"]
                        rurl = requests.get(oneimg_url)
                        one_name = str(all_dir) + "/"+ str(oneall_alt) + ".jpg"
                        with open(one_name,"wb") as sf:
                            sf.write(rurl.content)
                        print(one_name)
                    page_size = all_soup.find("span",{"class":"page-ch"})
                    size = int(page_size.get_text()[1:-1])
                    for pageone in page_href:
                        pageone_url = pageone["href"]
                        ints = 1
                        for all_int in range(size-1):
                            ints += 1
                            allpage_url = "https://www.mm131.pro" + pageone_url[:-7] + "_" + str(ints) + ".html" 
                            size_url = urlopen(allpage_url).read()
                            size_html = BeautifulSoup(size_url,"lxml")
                            htmls = size_html.find_all("div",{"class":"content-pic"})
                            for size_h in htmls:
                                tag_img = size_h.find_all("img")
                                tag_alt = size_h.find_all("alt")
                                for all_src in tag_img:
                                    src = all_src["src"]
                                    alt = all_src["alt"]
                                    r = requests.get(src)
                                    save_name = str(all_dir) + "/" + str(alt) + ".jpg"
                                    with open(save_name,"wb") as f:
                                        f.write(r.content)
                                    print(save_name)



                        

                        
                        



                
                


