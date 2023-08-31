

def terminal():
    """
    pip install django-bootstrap4
    pip freeze > libs.txt
    """


def settings():
    """
    INSTALLED_APPS = ['bootstrap4']
    """


def templates():
    """
    * Abaixo temos as "tags mandatórias" e onde elas devem ser anexadas no template
    * {% load bootstrap4 %}                    || antes / depois da tag <DOCTYPE>
    * {% bootstrap_css %}                      || no escopo da tag <head>
    * {% bootstrap_javascript jquery='full' %} || no escopo da tag <body>
    * {% bootstrap_messages %}                 || no escopo da tag <body> (no topo ou logo acima de uma tag estratégica)
    * OBS || {% bootstrap_css %} deve ser anexada ANTES de qualquer tag <link> p/ css que customize o template
    * OBS || {% bootstrap_messages %} precisa de bibliotecas Django p/ aplicação no template, antes usadas nas views

    <!DOCTYPE html>
    {% load bootstrap4 %}

    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        {% bootstrap_css %}
        {% block title %} {% endblock %}
        {% block link %} {% endblock %}
        {% block style %} {% endblock %}
    </head>
    <body>
      {% bootstrap_messages %}
      {% block body %}

      {% endblock %}
      {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """


def views():
    """
    * Como a biblioteca é usada nas views
    * Normalmente, são usadas em funções que usam algum tipo de formulário
    * No template, se aplica a sintaxe {% bootstrap_messages %}

    from django.contrib import messages
    (def post)         messages.error(request, 'Mensagem de erro')
    (def post)         messages.success(request, 'Mensagem de sucesso')
    (def form_valid)   messages.error(self.request, 'Mensagem de erro')
    (def form_invalid) messages.success(self.request, 'Mensagem de sucesso')
    """