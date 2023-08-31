

def descricao():
    """
    . A função "path" auxilia na configuração das urls vinculadas a suas respectivas views
    . Normalmente serve 3 parâmetros
    
    . path(
        "nome de apresentação do link", 
        referência da view, 
        "apelido da url"
    )
    
    . É comum usar os mesmos nomes em ambos parâmetros 1 e 3
    """

def exemplo():
    """
    from django.urls import path

    urlpatterns = [
        path('novo-cliente', AddClientView.as_view(), name='novo-cliente')
    ]
    """