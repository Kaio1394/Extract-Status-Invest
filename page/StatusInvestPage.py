from Helper.Helper import Helper


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
        
    def expand_all_stocks(self):
        self.driver.send_click('xpath', "(//div[@class='select-wrapper'])[3]")
        self.driver.send_click('xpath', "(//span[text()='TODOS'])[2]")
    
    def close_status_invest(self):
        self.driver.close()
        
    def print_list_stocks(self):
        rows = 1
        while True:
            try:
                print("nome=" + self.driver.get_text_element('xpath',"//div[@id='asDown']//div[@class='list']//a["+str(rows)+"]//small[@title='Nome da empresa/FII']") + ";" +
                    "ativo=" + self.driver.get_text_element('xpath',"//div[@id='asDown']//div[@class='list']//a["+str(rows)+"]//span[@title='ticker/código do ativo']") + ";" + 
                    "valor_abertura=" + self.driver.get_text_element('xpath', "//div[@id='asDown']//div[@class='list']//a["+str(rows)+"]//div[@title='Valor de abertura']/span/span") + ";" +  
                    "min=" + self.driver.get_text_element('xpath', "//div[@id='asDown']//div[@class='list']//a["+str(rows)+"]//div[@title='Mínima do dia']/span/span") + ";" + 
                    "max=" + self.driver.get_text_element('xpath', "//div[@id='asDown']//div[@class='list']//a["+str(rows)+"]//div[@title='Máxima do dia']/span/span") + ";" + 
                    "valor_fechamento=" + self.driver.get_text_element('xpath', "//div[@id='asDown']//div[@class='list']//a["+str(rows)+"]//div[@title='Valor de fechamento']/span/span") + ";" + 
                    "volume_financeiro=" + self.driver.get_text_element('xpath', "//div[@id='asDown']//div[@class='list']//a["+str(rows)+"]//div[@title='Volume financeiro']/span/span") + ";" + 
                    "variação=" + self.driver.get_text_element('xpath', "//div[@id='asDown']//div[@class='list']//a["+str(rows)+"]//span[@title='Variação atual no preço do ativo']").strip(" ").split('downward')[1])
                rows += 1
            except:
                break