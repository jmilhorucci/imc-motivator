from typing import cast
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.defaultfilters import last, time
from requests.api import request
from imcmotivator.models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
import requests
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.hashers import make_password
import random
import http.client
# Create your views here.

global apiKey

apiKey = "999fcbe93cmsh9511529eac0763fp1f244cjsna4772317414f"


def index(request):
    return render(request, "imcmotivator/dashboard.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "imcmotivator/login.html", {
                "message": "Usuário ou senha incorreto!"
            })
    else:
        return render(request, "imcmotivator/login.html")


def logout_view(request):
    logout(request)
    return render(request, "imcmotivator/login.html", {
        "message": "Logged out."
    })


def paginaCadastro(request):
    return render(request, "imcmotivator/signup.html")


def salvarCadastro(request):
    username = request.POST["username"]
    password = request.POST["password"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    telefone = request.POST["telefone"]
    altura = request.POST["altura"]
    autor = request.POST["autor"]
    idioma = request.POST["idioma"]

    user = User(username=username,
                password=make_password(password),
                first_name=first_name,
                last_name=last_name,
                email=email)
    user.save()

    pessoa = Pessoa(user=user,
                    telefone=telefone,
                    altura=altura,
                    autor=autor,
                    idioma=idioma)
    pessoa.save()

    return render(request, "imcmotivator/login.html")


def editarCadastro(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    context = {"pessoa": Pessoa.objects.get(user=usuario)}
    print(context)
    return render(request, "imcmotivator/editar-cadastro.html", context)


def editarCad(request,  usuario_id):

    usuario = User.objects.get(pk=usuario_id)

    if request.method == "POST":
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        telefone = request.POST["telefone"]
        altura = request.POST["altura"]
        autor = request.POST["autor"]
        idioma = request.POST["idioma"]

        usuario.password = make_password(password)
        usuario.first_name = first_name
        usuario.last_name = last_name
        usuario.email = email
        usuario.save()

        pessoa = Pessoa.objects.get(user=usuario)
        pessoa.telefone = telefone
        pessoa.altura = altura
        pessoa.autor = autor
        pessoa.idioma = idioma
        pessoa.save()

        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "imcmotivator/home.html")


def cadastroPeso(request):
    # context = {"pessoa": Pessoa.objects.get(pk=pessoa_id)}
    return render(request, "imcmotivator/cadastro_peso.html")


def salvarPeso(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    pessoa = Pessoa.objects.get(user__exact=usuario)

    # Trecho que valida se faz 1 semana da data de cadastro do último peso
    try:
        ultimoPeso = Peso.objects.filter(
            pessoa__exact=pessoa).order_by('-dataCadastro')[0:1].get()
        fazUmaSemana = ultimoPeso.dataCadastro + timedelta(days=7)
        if(fazUmaSemana >= timezone.now()):
            return render(request, "imcmotivator/cadastro_peso.html", {
                "message": "Ainda não faz uma semana desde o último peso cadastrado."
            })
    except Peso.DoesNotExist:
        ultimoPeso = None

    # Caso faça menos de 1 semana, segue a rotina abaixo e efetua o cadastro já calculando o imc.
    valor_peso = request.POST["peso"]

    url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/metric"
    querystring = {"weight": valor_peso, "height": pessoa.altura}
    headers = {
        'x-rapidapi-host': "body-mass-index-bmi-calculator.p.rapidapi.com",
        'x-rapidapi-key': apiKey
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    result = response.json()

    novoPeso = Peso(
        pessoa=pessoa,
        peso=valor_peso,
        imc=((result["bmi"]))
    )

    novoPeso.save()
    context = {"peso": Peso.objects.filter(
        pessoa__exact=pessoa).order_by('-dataCadastro')[0:1].get()}
    return render(request, "imcmotivator/pergunta.html", context)


def listarPeso(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    pessoaBD = Pessoa.objects.get(user__exact=usuario)
    context = {"pesos": Peso.objects.filter(pessoa__exact=pessoaBD)}
    return render(request, "imcmotivator/listagemPesos.html", context)


def deletarCadastro(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)
    pessoa.delete()
    return render(request, "imcmotivator/login.html")


def fraseRandomica(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    pessoaBD = Pessoa.objects.get(user__exact=usuario)
    idioma = pessoaBD.idioma

    class Frase:
        def __init__(self, frase, autor, imgAutor):
            self.frase = frase
            self.autor = autor
            self.imgAutor = imgAutor

    # Busca uma frase randomica na api
    url = "https://bodybuilding-quotes1.p.rapidapi.com/random-quote"
    headers = {
        'x-rapidapi-host': "bodybuilding-quotes1.p.rapidapi.com",
        'x-rapidapi-key': apiKey
    }
    response = requests.request("GET", url, headers=headers)
    result = response.json()
    frase = ((result["quote"]))
    autor = ((result["author"]))

    # Pesquisa imagem do Autor
    requisitos = {"keyword": autor, "max": "1"}

    urlImagem = "https://google-image-search1.p.rapidapi.com/"

    headersImagem = {
        'x-rapidapi-host': "google-image-search1.p.rapidapi.com",
        'x-rapidapi-key': apiKey
    }

    responseImagem = requests.request(
        "GET", urlImagem, headers=headersImagem, params=requisitos)
    resultImagem = responseImagem.json()

    posImagemLista = random.choice(resultImagem)

    linkImagem = posImagemLista["image"]["url"]

    # traduz a frase se o idioma da pessoa nao for ingles
    if(idioma != "en"):
        urlTradutor = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        conteudo = "q="+frase+"&target="+idioma+"&source=en"
        headersTradutor = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com",
            'x-rapidapi-key': apiKey
        }

        responseTradutor = requests.request(
            "POST", urlTradutor, data=conteudo, headers=headersTradutor)

        resultTradutoor = responseTradutor.json()
        fraseTraduzida = (
            (resultTradutoor["data"]["translations"][0]["translatedText"]))
        print(fraseTraduzida)

        objFrase = Frase(fraseTraduzida, autor, linkImagem)
        print(objFrase.autor)

        return render(request, "imcmotivator/fraseRandomica.html", {"randomFrase": objFrase})
    else:
        objFrase = Frase(frase, autor, linkImagem)

        return render(request, "imcmotivator/fraseRandomica.html", {"randomFrase": objFrase})


def fraseAutorPessoa(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    pessoaBD = Pessoa.objects.get(user__exact=usuario)
    autor = {"author": pessoaBD.autor}
    idioma = pessoaBD.idioma

    class Frase:
        def __init__(self, frase, autor, imgAutor):
            self.frase = frase
            self.autor = autor
            self.imgAutor = imgAutor

    # Busca as frases do Autor da Pessoa
    url = "https://bodybuilding-quotes1.p.rapidapi.com/author-quotes"
    headers = {
        'x-rapidapi-host': "bodybuilding-quotes1.p.rapidapi.com",
        'x-rapidapi-key': apiKey
    }
    response = requests.request("GET", url, headers=headers, params=autor)
    result = response.json()

    posAleatoriaLista = random.choice(result)

    frase = posAleatoriaLista["quote"]

    # Pesquisa imagem do Autor
    requisitos = {"keyword": pessoaBD.autor, "max": "1"}

    urlImagem = "https://google-image-search1.p.rapidapi.com/"

    headersImagem = {
        'x-rapidapi-host': "google-image-search1.p.rapidapi.com",
        'x-rapidapi-key': apiKey
    }

    responseImagem = requests.request(
        "GET", urlImagem, headers=headersImagem, params=requisitos)
    resultImagem = responseImagem.json()

    posImagemLista = random.choice(resultImagem)

    linkImagem = posImagemLista["image"]["url"]

   # traduz a frase se o idioma da pessoa nao for ingles
    if(idioma != "en"):
        urlTradutor = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        conteudo = "q="+frase+"&target="+idioma+"&source=en"
        headersTradutor = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com",
            'x-rapidapi-key': apiKey
        }

        responseTradutor = requests.request(
            "POST", urlTradutor, data=conteudo, headers=headersTradutor)

        resultTradutoor = responseTradutor.json()
        fraseTraduzida = (
            (resultTradutoor["data"]["translations"][0]["translatedText"]))

        objFrase = Frase(fraseTraduzida, pessoaBD.autor, linkImagem)

        return render(request, "imcmotivator/fraseAutorPessoa.html", {"autorPessoaFrase": objFrase})
    else:
        objFrase = Frase(frase, pessoaBD.autor, linkImagem)

        return render(request, "imcmotivator/fraseAutorPessoa.html", {"autorPessoaFrase": objFrase})


def frasePalavra(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    return render(request, "imcmotivator/frasepalavra.html")


def frasePalavrachave(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    pessoaBD = Pessoa.objects.get(user__exact=usuario)
    idioma = pessoaBD.idioma
    palavra = request.POST["palavra"]

    class Frase:
        def __init__(self, frase, autor, palavra, imgAutor):
            self.frase = frase
            self.autor = autor
            self.palavra = palavra
            self.imgAutor = imgAutor
    # ---------------------------------------------------------------------------------------|

    if(idioma != "en"):
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        payload = "q="+palavra+"&target=en&source="+idioma
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com",
            'x-rapidapi-key': apiKey
        }

        responseTradutor = requests.request(
            "POST", url, data=payload, headers=headers)

        resultTradutoor = responseTradutor.json()
        palavraTraduzida = (
            (resultTradutoor["data"]["translations"][0]["translatedText"]))
    else:
        palavraTraduzida = palavra
    # ---------------------------------------------------------------------------------------|

    url = "https://bodybuilding-quotes1.p.rapidapi.com/quote-search"

    querystring = {"search": palavraTraduzida}

    headers = {
        'x-api-key': "{{api-key}}",
        'x-rapidapi-host': "bodybuilding-quotes1.p.rapidapi.com",
        'x-rapidapi-key': apiKey
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    resultfrase = response.json()

    if (resultfrase != None):

        fraseAl = random.choice(resultfrase)
        frase = fraseAl["quote"]
        autor = fraseAl["author"]
    else:
        frase = "There is no sentence for your word, sorry"
        autor = "Unknown"

    if(idioma != 'en'):
        urlTradutor = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        conteudo = "q="+frase+"&target="+idioma+"&source=en"
        headersTradutor = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com",
            'x-rapidapi-key': apiKey
        }

        responseTradutor = requests.request(
            "POST", urlTradutor, data=conteudo, headers=headersTradutor)

        resultTradutoor = responseTradutor.json()
        fraseTraduzida = (
            (resultTradutoor["data"]["translations"][0]["translatedText"]))
    else:
        fraseTraduzida = frase
    # ---------------------------------------------------------------------------------------|

    # Pesquisa imagem do Autor
    requisitos = {"keyword": autor, "max": "1"}

    urlImgPalavra = "https://google-image-search1.p.rapidapi.com/"

    headersImgPalavra = {
        'x-rapidapi-host': "google-image-search1.p.rapidapi.com",
        'x-rapidapi-key': apiKey
    }

    responseImagem = requests.request(
        "GET", urlImgPalavra, headers=headersImgPalavra, params=requisitos)
    resultImagem = responseImagem.json()

    posImgPlLista = random.choice(resultImagem)

    linkImgPalavra = posImgPlLista["image"]["url"]

    objFrase = Frase(fraseTraduzida, autor, palavra, linkImgPalavra)

    return render(request, "imcmotivator/frasepalavra.html", {"returnFrase": objFrase})


# def pergunta(request, usuario_id):
    usuario = User.objects.get(pk=usuario_id)
    pessoa = Pessoa.objects.get(user__exact=usuario)

    context = {"peso": Peso.objects.filter(
        pessoa__exact=pessoa).order_by('-dataCadastro')[0:1].get()}
    return render(request, "imcmotivator/pergunta.html", context)
