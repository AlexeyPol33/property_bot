from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re
import time

class parser():
    def __init__(self) -> None:

        print('создан объект "парсер"')
        self.url = 'https://www.avito.ru/moskva/kvartiry/prodam'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        pass

    def __del__ (self):
        self.driver.close()
        print('Объект "парсер" удален')
        pass

    def get_property(html):
        soup = BeautifulSoup(html,'html.parser')
        soup = soup.find_all('div',class_="iva-item-content-rejJg")
        for s in soup:
            name = BeautifulSoup(str(s),'html.parser')
            name = name.find_all('h3',class_="title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO")
            name = re.search(r'>(.+)<',str(name))
            if name:
                name = name[0][1:-1]
            print(name)
            print('\n')
        
        pass



if __name__ == '__main__':
    a = parser()
    del a
    


