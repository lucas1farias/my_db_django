

def instalacao():
    """
    * Escolher uma aplicação onde os filtros serão usados
    * Após escolher, criar um diretório "templatetags", criar um módulo "__init__.py" e um módulo "my_filters.py"
    * O nome do módulo é opcional
    * No módulo criar as funções pertinentes, que serão aplicadas em conteúdos nos templates
    """


def exemplos_de_funcao():
    """
    * Antes de qualquer função, a importação e a instanciação da variável são necessárias
    * Após isso, as funções são configuradas usando a variável que é um decorador "@register.filter(name=str)"
    * O nome passado ao parâmetro "name" é recomendado que seja o mesmo nome da função
    * O parâmetro "name" é como a função será chamada no template

    from django import template
    register = template.Library()

    @register.filter(name='get_type')
    def get_type(value):
        return type(value).__name__


    @register.filter(name='turn_into_string')
    def turn_into_string(content):
        return str(content)


    @register.filter(name='calculate_purchase_value')
    def calculate_purchase_value(amount, unit_price):
        amount_ = float(amount)
        unit_price_ = float(unit_price)
        return f'{amount_ * unit_price_:.2f}'
    """


def exemplos():
    """
    * Para que seja possível carregar as funções no template, é preciso uma importação {% load %}
    * No template, em tags com algum conteúdo, você as usa como parâmetro para as funções criadas
    * Em funções com 1 parâmetro, a sua chamada vêm ao final, a partir do separador |nome da função
    * Em funções com + de 1 parâmetro, seguir e outro exemplo deixado abaixo

    {% load nome_módulo_dos_filtros.py %}

    <tag>{{ conteúdo|get_type }}</tag>

    {{ object.stock_shares|calculate_purchase_value:object.share_unit_price }}
    {{ parâmetro|nome_da_função:parâmetro }}
    """