

def requisitos():
    """
    . View
    . Rota da view
    . Template
    """

def contexto():
    """
    Criar objetos de um modelo de forma automática
    É usado uma entrada e um formulário, onde a entrada passa seu atrib "name" para o método "post" na view
    """

def ex_formulario():
    """
    . Definir como tipo "post"
    . Dar um nome (name="") à entrada para que seu valor seja enviável (aqui, para a view)

    <form method="post">
        {% csrf_token %}
        <input type="text" name="client-amount" placeholder="Quantidade de hospedes">
        <input type="submit" value="criar hospedes">
    </form>
    """

def view():
    """
    . O método "post" é nativo do Django, e por causa do formulário na view, eu uso este método "post"
    . A variável "new_client_amount" armazena o valor enviado pelo formulário
    . Com o formulário enviado, essa variável deixa de ser "None" e pode ser manipulada
    . A manipulação aqui é usar o valor passado no formulário como parâmetro para um loop
    . O loop indica a qtd. de vezes que objetos de hospedes serão criados (via função "create_person_object")
    . Houve problemas com a função "render" (não sei o motivo), portanto foi optado usar "redirect"
    . redirect("nome da url da view alvo")

    from django.shortcuts import redirect
    
    def post(self, request):
        new_client_amount = request.POST.get("client-amount")

        if new_client_amount is not None:
            for i in range(int(new_client_amount)):
                create_person_object()
        
        return redirect("index")
    """
