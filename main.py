import selenium
import re
import operator
from operator import itemgetter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import yaml
class Pars:
    def __init__(self):
        options = Options()
        self.data= {}
        self.browser = webdriver.Edge(executable_path='msedgedriver.exe',options=options)
        self.url = f"https://dobro.ru/analytics"
        self.browser.get(self.url)
        self.main(self)
    #options.add_argument("headless")
    def PrintInfo(self):
        region= self.browser.find_element(By.XPATH,'/html/body/main/section[1]/div/div[3]/div[2]/div/span/h3')
        print('\n',region.text,"\n")
        table = self.browser.find_element(By.TAG_NAME,"table")
        rows = table.find_elements(By.TAG_NAME,"tr")
        rowData=[]
        for i in rows:
            name=i.find_element(By.TAG_NAME,"p").text
            info = i.find_element(By.TAG_NAME,"span").text
            rowData.append({name:info})
            print(name,"   ",info,"\n")
        self.data={region.text:rowData}
        self.writeFile(self)


        
        return self.data
    def writeFile(self):
        with open("data.yaml","a",encoding='utf-8') as f:
            yaml.dump(self.data,f,allow_unicode=True,encoding='utf-8')
    def main(self):
        
        
        time.sleep(1)
        form = self.browser.find_element(By.TAG_NAME,"form")
        buttons = form.find_elements(By.TAG_NAME,"button")
        buttons[1].click()
        time.sleep(3)
        for i in range(1,90):
            xpath=f'//*[@id="bs-select-2-'+i.__str__()+'"]' 
            dropdown=self.browser.find_element(By.XPATH,xpath)
            #Block =  i.find_element(By.TAG_NAME,"a")
            #Block =  dropdown.find_element(By.TAG_NAME,"a")
            #print(Block.text,"\n")
            dropdown.click()
            time.sleep(7)
            self.PrintInfo(self)
            
            buttons[1].click()
            time.sleep(1)
            #time.sleep(1)

test= Pars.__init__(Pars)
           