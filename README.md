# IMC Motivator
Atividade final da matéria de Programação V, lecionada pelo Omar no curso de Sistemas de Informação.

## Equipe
> - *Juliano Victor Nune Milhorucci*
> - *Kainan Gomes*
> - *Matheus Pimentel*
> - *Sandro Luiz Mazzolla Junior*
> - *Victor Hugo Freitas Savoldi*
> - *Vinicius Herculano*

## Nome do Projeto

*IMC Motivator*

## Definição

- O Mashup tem como objetivo manter as pessoas motivadas na busca em atingir a faixa de IMC ideal.
- Utilizaremos uma API para calcular o IMC  através do último peso informado e a altura no cadastro do usuário.
- A segunda API trás frases motivacionais dos principais fisiculturistas da história, porém, em inglês, que serão traduzidas pela última API da nossa lista, Google Translate, de acordo com a língua que o usuário quer receber a mensagem(Definida no momento do seu cadastro).

## Capturas de Telas

**Tela de Login**

![image](https://user-images.githubusercontent.com/44588590/155437895-4af79fc5-0bd7-4e0f-8852-5d10252341ef.png)

**Tela de Cadastro de Usuário**

![image](https://user-images.githubusercontent.com/44588590/155438550-7e3268b4-63bb-400c-a0e3-fa7e4a5ee002.png)

**Tela de Dashboard**

![image](https://user-images.githubusercontent.com/44588590/155439035-69f90e94-7e0b-4345-a5d1-4c71d75693d2.png)

**Tela de Listagem de Peso**

![image](https://user-images.githubusercontent.com/44588590/155440112-83f8e26d-2b63-4aee-810b-45676e7d4d02.png)

**Tela de Resultado IMC**

![image](https://user-images.githubusercontent.com/44588590/155439192-bc910471-1f87-43f0-bb8e-a28443cb093f.png)

**Tela de Dose de Motivação > Frase Aleatória**

![image](https://user-images.githubusercontent.com/44588590/155439117-7f89f077-046f-4d2d-9038-5604ab693f51.png)


## API’s Utilizadas

- Body Mass Index (BMI) Calculator - Calculador de IMC -  https://rapidapi.com/principalapis/api/body-mass-index-bmi-calculator/
- Bodybuilding Quotes - Citações de figuras referências no mundo do fisiculturismo (Retorna os dados em em Inglês) - https://rapidapi.com/DenchCity/api/bodybuilding-quotes1/
- Google Translate - https://rapidapi.com/googlecloud/api/google-translate1/

## Regras

1. O usuário deverá criar seu cadastro.
2. O usuário será obrigado a informar seu primeiro registro de peso após realizar o cadastro.
3. O registro subsequente do peso ocorrerá de 1 em 1 semana a partir da última data de cadastro. Se o IMC do usuário variar de 18 a 30 (peso ideal), irá aparecer frases somente do autor Arnold Schwarzenegger, caso contrário será exibido frases de autores aleatórias.
4. O sistema irá comparar o IMC atual com o anterior logo após registrar o peso, e notificar avanço ou retrocesso na obtenção do IMC ideal, junto disso irá perguntar se a pessoa está se sentindo bem com o resultado. Caso diga não, será apresentado uma frase motivacional randômica vindo da API, do contrário apenas registra o resultado.
5. Terá uma sessão no menu chamada “Dose de motivação” onde exibirá frases motivacionais de acordo com o filtro do usuário.
6. Ao realizar o cadastro de um Novo Peso, o usuário será redirecionado a página de pergunta, onde será questionado “você está satisfeito(a) com os seus resultados?”. Se o usuário optar em “Sim”, será redirecionado para a página de Frase por Autor, onde exibirá uma frase do atleta favorito (escolhido no ato do cadastro), caso contrário, ao optar em “Não”, será redirecionado para a página de Frase Aleatória, onde exibirá uma frase aleatória de qualquer atleta listado na regra “Top 10”.
7. O sistema usará a API de Pesquisa de Imagens do Google, para reconhecimento do nome do autor (vinculado a API de Frases), que será exibido abaixo da frase (Aleatória ou Por Autor).


## Exemplos de utilização das API’s

###### >>> Body Mass Index (BMI) Calculator - https://rapidapi.com/principalapis/api/body-mass-index-bmi-calculator/ <<<

**Endpoint:** Metric
**Parâmetros:**
- Peso: Quilogramas
- Altura: Metros
**Retorno:** Cálculo do IMC

###### >>> Bodybuilding Quotes - https://rapidapi.com/DenchCity/api/bodybuilding-quotes1/ <<<

**Endpoint:** RandomQuote (Citação Aleatória)<br />
**Parâmetros:** Nenhum<br />
**Retorno:** Uma citação aleatória<br />

**Endpoint:** AuthorQuotes (Citação do Autor)<br />
**Parâmetros:** 
- Nome do autor
Retorno: Lista de citações do Autor informado<br />

**Endpoint:** SearchQuotes (Buscar citações)<br />
**Parâmetros:** 
- Uma ou mais palavras
**Retorno:** Lista de citações que contêm a(s) palavra(s) informada(s) como parâmetro<br />

###### >>> Google Translate - https://rapidapi.com/googlecloud/api/google-translate1/ <<<

**Endpoint:** Translate (Traduzir)<br />
**Parâmetros**:<br />
  - **_Obrigatórios_**:<br />
	  q – Texto a ser traduzido<br />
	  target – Idioma para qual vai ser traduzido<br />

  - **_Opcionais_**:<br />
	  format – Formato que o texto vai ser enviado(HTML/Texto Simples)<br />
	  source – A Linguagem de origem do texto a ser traduzido (Caso não informado a   própria API tenta identificar).<br />
          model – Modelo de tradução a ser utilizado<br />
	
**Retorno**: Texto traduzido<br />

## Execução do Projeto

**Certifique-se que o Python está instalado executando o seguinte comando:** 
> - *$ python --version*

###### >>> Instalação do Python - https://www.python.org/downloads/ <<<

**Certifique-se que o Django está instalado executando o seguinte comando:** 
> - *$ python -m django --version*

###### >>> Instalação do Django - https://docs.djangoproject.com/pt-br/4.0/topics/install/#installing-official-release <<<

**Instale Resquests executando o comando:** 
> - *python -m pip install requests*

**Se necessário, realize o upgrade do PIP com previlégio de Administrador executando o seguinte comando:** 
> - *python -m pip install --upgrade pip*

**Aplique o Migrate para sincronizar o banco executando o seguinte comando:** 
> - *python manage.py migrate*

**Execute o projeto executando o seguinte comando:** 
> - *python manage.py runserver*

## Procedimentos Realizados

> - *Avaliação de Usabilidade com Think Aloud*
> - *Criação do Diagrama de Classe da aplicação*
> - *TDD da aplicação utilizando o Selenium*
