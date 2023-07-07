from Helper.Helper import Helper
from tqdm import tqdm

class StatusInvestPage:
    def __init__(self):
        self.driver = Helper()
        
    def navigate_to_status_invest(self):
        self.driver.get_url('https://statusinvest.com.br/')
        
    def wait_page_status_invest_loading(self):
        self.driver.wait_until(10, "xpath", "//div[h3[text()='BAIXAS']]//strong")
        
    def click_in_symbols(self, status: str):
        self.driver.send_click('xpath', "//div[h3[text()='"+status+"']]//strong")
        
    def wait_loading_page_high_and_low_stocks(self):
        self.driver.wait_until(10, 'xpath', "//input[@aria-label='Filtro por índice']")
        
    def expand_all_stocks(self, down_symbol: bool):
        down_or_up = ""
        if down_symbol:
            down_or_up = "asDown"
        else:
            down_or_up = "asUp"
        self.driver.send_click('xpath', f"//*[@id='{down_or_up}']//div[@class='select-wrapper']")
        self.driver.send_click('xpath', f"//*[@id='{down_or_up}']//span[text()='TODOS']")
    
    def click_page_home(self):
        # self.driver.send_click('xpath', "//a[@title='Página inicial']")
        # self.driver.wait_until(10, 'xpath', "//h2[a[@class='text-main']]/small[text()='BOVESPA e BM&F']")
        self.driver.back_page()

    def close_status_invest(self):
        self.driver.close()
        
    def print_list_stocks(self, down_symbol: bool):
        rows = 1
        downOrUp = ""
        if down_symbol:
            downOrUp = "asDown"
        else:
            downOrUp = "asUp"
        while True:
            try:
                print("nome=" + self.driver.get_text_element('xpath',"//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//small[@title='Nome da empresa/FII']") + ";" +
                    "ativo=" + self.driver.get_text_element('xpath',"//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//span[@title='ticker/código do ativo']") + ";" + 
                    "valor_abertura=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//div[@title='Valor de abertura']/span/span") + ";" +  
                    "min=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//div[@title='Mínima do dia']/span/span") + ";" + 
                    "max=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//div[@title='Máxima do dia']/span/span") + ";" + 
                    "valor_fechamento=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//div[@title='Valor de fechamento']/span/span") + ";" + 
                    "volume_financeiro=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//div[@title='Volume financeiro']/span/span") + ";" + 
                    "variação=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//span[@title='Variação atual no preço do ativo']").strip(" ").split('downward')[1])
                rows += 1
            except:
                break
 
    def writter_file(self, path_file: str, down_symbol: bool):
        rows = 1
        downOrUp = ""
        arrow = ""
        if down_symbol:
            downOrUp = "asDown"
            arrow = "downward"
        else:
            downOrUp = "asUp"
            arrow = "upward"
        with open(path_file, 'w', newline='') as arquivo:
            while True:
                try:
                    arquivo.write("nome=" + self.driver.get_text_element('xpath',"//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//small[@title='Nome da empresa/FII']") + ";")
                    arquivo.write("ativo=" + self.driver.get_text_element('xpath',"//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//span[@title='ticker/código do ativo']") + ";")
                    arquivo.write("valor_abertura=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//div[@title='Valor de abertura']/span/span") + ";")
                    arquivo.write("min=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//div[@title='Mínima do dia']/span/span") + ";")
                    arquivo.write("max=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//div[@title='Máxima do dia']/span/span") + ";")
                    arquivo.write("valor_fechamento=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//div[@title='Valor de fechamento']/span/span") + ";")
                    arquivo.write("volume_financeiro=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//div[@title='Volume financeiro']/span/span") + ";")
                    arquivo.write("variação=" + self.driver.get_text_element('xpath', "//div[@id='"+downOrUp+"']//div[@class='list']//a["+str(rows)+"]//span[@title='Variação atual no preço do ativo']").strip(" ").split(arrow)[1] + "\n")
                    rows += 1
                except:
                    break  