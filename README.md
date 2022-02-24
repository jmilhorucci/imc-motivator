# Atividade-ProjetoFinal-MashupPG5
Atividade final da matéria de Programação V, lecionada pelo Omar.

## Equipe:
> - *Juliano Victor Nune Milhorucci*
> - *Kainan Gomes*
> - *Matheus Pimentel*
> - *Sandro Luiz Mazzolla Junior*
> - *Victor Hugo Freitas Savoldi*
> - *Vinicius Herculano*

## Nome do Projeto:

*IMC Motivator*

## API’s Utilizadas

- Body Mass Index (BMI) Calculator - Calculador de IMC -  https://rapidapi.com/principalapis/api/body-mass-index-bmi-calculator/
- Bodybuilding Quotes - Citações de figuras referências no mundo do fisiculturismo (Retorna os dados em em Inglês) - https://rapidapi.com/DenchCity/api/bodybuilding-quotes1/
- Google Translate - https://rapidapi.com/googlecloud/api/google-translate1/

## Definição

- O Mashup tem como objetivo manter as pessoas motivadas na busca em atingir a faixa de IMC ideal.
- O Mashup tem como objetivo manter as pessoas motivadas na busca em atingir a faixa de IMC ideal.
- A segunda API trás frases motivacionais dos principais fisiculturistas da história, porém, em inglês, que serão traduzidas pela última API da nossa lista, Google Translate, de acordo com a língua que o usuário quer receber a mensagem(Definida no momento do seu cadastro).

## Regras

1. O usuário deverá criar seu cadastro.
2. O usuário será obrigado a informar seu primeiro registro de peso após realizar o cadastro.
3. O registro subsequente do peso ocorrerá de 1 em 1 semana a partir da última data de cadastro. Se o IMC do usuário variar de 18 a 30 (peso ideal), irá aparecer frases somente do autor Arnold Schwarzenegger, caso contrário será exibido frases de autores aleatórias.
4. O sistema irá comparar o IMC atual com o anterior logo após registrar o peso, e notificar avanço ou retrocesso na obtenção do IMC ideal, junto disso irá perguntar se a pessoa está se sentindo bem com o resultado. Caso diga não, será apresentado uma frase motivacional randômica vindo da API, do contrário apenas registra o resultado.
5. Terá uma sessão no menu chamada “Dose de motivação” onde exibirá frases motivacionais de acordo com o filtro do usuário.

## Exemplos de utilização das API’s

###### >>> Body Mass Index (BMI) Calculator - https://rapidapi.com/principalapis/api/body-mass-index-bmi-calculator/ <<<

**Endpoint:** Metric
**Parâmetros:**
- Peso : Quilogramas
- Altura : Metros
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
