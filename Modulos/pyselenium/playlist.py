from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.caminho_driver = r'Pyselenium/chromedriver.exe'
        self.opcoes = webdriver.ChromeOptions()
        self.opcoes.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.caminho_driver,
            options=self.opcoes
        )
    
    def acessa(self, site):
        self.chrome.get(site)

    def reproduzir_som(self):
        try:
            btn_tocar = self.chrome.find_element_by_css_selector(
                '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button')
            btn_tocar.click()
        except Exception as e:
            print("Erro ao reproduzir música:", e)

    def sair(self):
        self.chrome.quit()

if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://www.youtube.com/watch?v=7QU1nvuxaMA&list=RD7QU1nvuxaMA&start_radio=1')
    chrome.reproduzir_som()


    