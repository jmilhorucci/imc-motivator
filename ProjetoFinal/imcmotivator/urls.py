from django.urls import path

from .import views

urlpatterns = [

    path("", views.login_view),
    path('home/', views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('signup/', views.paginaCadastro),
    path('salvarCadastro/', views.salvarCadastro),
    path('editarCadastro/<int:usuario_id>/', views.editarCadastro),
    path('editarCad/<int:usuario_id>/', views.editarCad),
    path('deletarCadastro/<int:pessoa_id>/', views.deletarCadastro),
    path('salvarPeso/<int:usuario_id>/', views.salvarPeso),
    path('cadastroPeso/', views.cadastroPeso),
    path('listarPeso/<int:usuario_id>/', views.listarPeso),
    path('fraseRandomica/<int:usuario_id>/', views.fraseRandomica),
    path('fraseAutorPessoa/<int:usuario_id>/', views.fraseAutorPessoa),
    path('frasePalavra/<int:usuario_id>/', views.frasePalavra),
    path('PesquisafrasePalavrachave/<int:usuario_id>/', views.frasePalavrachave),
    # path('pergunta/<int:usuario_id>/', views.pergunta)

]
