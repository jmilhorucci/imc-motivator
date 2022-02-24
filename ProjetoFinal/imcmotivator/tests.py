#from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Create your tests here.

# -- Linha abaixo instalar o webdriver dinamicamente, porém fechar o browser --
#driver = webdriver.Chrome(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# -- Linha abaixo procura o webdriver no local exato, no caso (Sandro) no Downloads, mas não fecha o browser --
driver = webdriver.Chrome(
    chrome_options=options, executable_path=r'C:\Users\jmazz\Downloads\chromedriver.exe')

driver.get("http://127.0.0.1:8000/imcmotivator/login/")

# Efetuar Cadastro

element = driver.find_element_by_link_text("Cadastre-se").click()

nome = driver.find_element_by_id("first_name")
nome.send_keys("Developer")

sobrenome = driver.find_element_by_id("last_name")
sobrenome.send_keys("Dev")

email = driver.find_element_by_id("email")
email.send_keys("dev@dev.com")

username = driver.find_element_by_id("username")
# Alterar aqui para testes, caso já exista o username
username.send_keys("Developer@Teste123")

password = driver.find_element_by_id("password")
password.send_keys("@Dev123456")

telefone = driver.find_element_by_id("telefone")
telefone.send_keys("1000001111")

altura = driver.find_element_by_id("altura")
altura.send_keys("1.90")

autor = driver.find_element_by_id("autor")
autor.click()
select_autor = Select(autor)
select_autor.select_by_value("Arnold Schwarzenegger")
autor.click()

idioma = driver.find_element_by_id("idioma")
idioma.click()
select_idioma = Select(idioma)
select_idioma.select_by_value("pt")
idioma.click()

time.sleep(5)
cadastrar = driver.find_element_by_xpath(
    "/html/body/div/div[1]/div/div/div[2]/form/div[10]/a[2]/button").click()

# Efetuar Login

driver.get("http://127.0.0.1:8000/imcmotivator/login/")

username = driver.find_element_by_id("username")
# Alterar aqui para fazer o login com o username cadastrado acima
username.send_keys("Developer@Teste123")

password = driver.find_element_by_id("password")
password.send_keys("@Dev123456")

time.sleep(5)
login = driver.find_element_by_css_selector(
    "body > form > div > div > div > div > div > div > a > button").click()

# Efetuar Cadastro de Peso

pesos = driver.find_element_by_css_selector(
    "body > nav > div > div.navbar-content.ps > ul > li:nth-child(4) > a > span.pc-mtext").click()

cadastrarPesos = driver.find_element_by_xpath(
    "/html/body/nav/div/div[2]/ul/li[4]/ul[1]/li/a").click()

cadastrarPesosKg = driver.find_element_by_id("peso")
cadastrarPesosKg.send_keys("110")

time.sleep(2)
enviarPeso = driver.find_element_by_class_name("btn-primary").click()

time.sleep(2)
clicarSim = driver.find_element_by_link_text("Sim").click()

# Receber motivação aleatória

doseMotivacao = driver.find_element_by_partial_link_text("Dos").click()

time.sleep(2)
fraseRandomica = driver.find_element_by_partial_link_text("Frase Ale").click()
