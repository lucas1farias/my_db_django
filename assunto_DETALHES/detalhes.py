

def detalhes():
    """
    * Quando se usa tags <select> + <option value=""> o que é passado via "request.POST.get(value)" é uma string
    * O objeto {{ object }} é muito útil e só se torna disponível sob algumas condições

        Precisa de uma "UpdateView"
        template_name = ''
        model = Model
        fields = ('',)
        Precisa de uma url dinâmica (exemplo abaixo)
        Normalmente está inserido num contexto onde um modelo esteje sendo iterado num template
        Normalmente está inserido num contexto onde seja preciso gerar links dinâmicos dos objetos p/ fazer algum crud
        No template dinâmico, cada link terá seu próprio {{ object }}, com permissão p/ usar atributos de modelo
        No exemplo abaixo, se "transactions" é um modelo usado num template, então {{ object.atrib_do_modelo }}

        path('detalhe-transacao/<int:pk>', TransactionCalculus.as_view(), name='detalhe-transacao')
        {% for transaction in transactions %}
            <a class="btn btn-info" href="{% url 'detalhe-transacao' transaction.pk %}">detalhes</a>
        {% endfor %}
    """
