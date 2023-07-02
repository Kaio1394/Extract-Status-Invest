import os
import time
from page.StatusInvestPage import StatusInvestPage
                

if __name__ == '__main__':

    path = "C:/RPA/CSV/"

    # Criando pasta que será salvo os arquivos CSV's
    if os.path.exists(path) and os.path.isdir(path):
        print("O diretório existe.")
    else:
        print("O diretório não existe: " + path + ". Criando a pasta...")
        os.makedirs(path)
        print("Diretório criado com sucesso.")
        
    # Extraindo dados de todos os ativos em baixa na bolsa de valores
    print('INICIANDO BOT DE EXTRAÇÃO DE DADOS')
    driver = StatusInvestPage()
    driver.navigate_to_status_invest()
    driver.wait_page_status_invest_loading()
    driver.click_in_symbols("BAIXAS")
    driver.wait_loading_page_high_and_low_stocks()
    driver.expand_all_stocks()
    time.sleep(5)
    driver.print_list_stocks()
    print("Imprimindo os dados no terminal...")
    driver.close_status_invest()
    print('BOT FINALIZADO')

