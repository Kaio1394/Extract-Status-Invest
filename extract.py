import os
import time
from page.StatusInvestPage import StatusInvestPage
                

if __name__ == '__main__':

    path = "C:/RPA/CSV/"
    file_name = "dados_ativos_em_baixa.txt"
    # Criando pasta que será salvo os arquivos CSV's
    if os.path.exists(path) and os.path.isdir(path):
        print("\nO diretório existe.")
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
    driver.expand_all_stocks(True)
    time.sleep(5)
    print(f'INICIANDO EXPORTAÇÃO DOS DADOS PARA O ARQUIVO TXT {file_name}...')
    driver.writter_file(path + file_name, True)
    print('DADOS SALVO NO ARQUIVO: ' + path + file_name)
    driver.close_status_invest()
    print('RETORNANDO PARA A OÁGINA INICIAL...')
    driver.click_page_home()

    # Extraindo dados de todos os ativos em alta na bolsa de valores
    driver.click_in_symbols("ALTAS") 
    driver.wait_loading_page_high_and_low_stocks()
    driver.expand_all_stocks(False)
    time.sleep(5)
    file_name = "dados_ativos_em_alta.txt"
    print(f'INICIANDO EXPORTAÇÃO DOS DADOS PARA O ARQUIVO TXT {file_name}...')
    driver.writter_file(path + file_name, False)
    print('DADOS SALVO NO ARQUIVO: ' + path + file_name)

    print('BOT FINALIZADO... DADO EXTRAIDOS COM SUCESSO.')
    
