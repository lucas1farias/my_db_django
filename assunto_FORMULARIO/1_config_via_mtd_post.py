

def post():
    """
    * A função "post" pode ser criada no escopo de "class based views"
    * A função "post" é um método que consegue resgatar dados de inputs via seu parâmetro: "request"
    * RESGATE: [ request.POST['atrib_name_do_input'] ] ou [ request.POST.get('atrib_name_do_input') ]
    * VALIDAÇÃO: <input type="" name="" required> (uso do atrib. "required")
    * Para isso, essa view Django deve ter um método "post" que aponte p/ um template com um formulário (method="post")
    """

def views():
    """
    * "self.name" é apenas um "exemplo" de uma var. de classe que recebe os dados de um input de um template
    * Dentro da função "post" os dados resgatados são inseridos nela
    * Toda função "post" deve ter ao final, algum redirecionamento p/ alguma rota url
    * Por fim, no contexto do template, o objeto salvo na função "post" pode ser apresentado

    from django.shortcuts import redirect
    from django.views.generic import TemplateView
    from .models import *

    class IndexView(TemplateView):
        template_name = 'index.html'

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.name = ''

        def post(self, request):
            if str(request.method) == 'POST':
                self.name = request.POST['atrib_name_from_input']
                obj = Model(name=self.name)
                obj.save()
                return redirect('index')

        def get_context_data(self, **kwargs):
            context = super(IndexView, self).get_context_data(**kwargs)
            context['name_self'] = f'Var. self: {self.name}'
            return context
    """

def html():
    """
    * O envio de dados ao back-end se dá majoritariamente por 2 tags: <button type="submit"> ou <input type="submit">
    * É RECOMENDADO (não mandatório) que estes botões estejam internos ao escopo da tag <form>
    * Caso seja optado colocá-los fora, configurar da seguinte forma
    * <form id="nome"> ... <input type="submit" form="nome"> .. <button type="submit" form="nome"></button>

    * O atributo "name" é quem resgata o valor do input e o envia ao back-end
    * O atributo "name" deve ter o mesmo nome do campo Django no modelo que o criou
    * No back-end, dados são acessados numa função "post" via código (request.POST['campo']) (request.POST.get('campo'))
    * A sintaxe {% csrf_token %} é mandatória, caso contrário, Django gera erro "Forbidden"

    * ========== EXEMPLO ==========
    <section>
        <div class="generic-form">
            <form action="{% url '' %}" autocomplete="off" method="post">
                {% csrf_token %}
                <div><input type="text" max="100" min="2" name="first_name" placeholder="Seu nome" required></div>

                <button type="submit">Enviar dados ao back-end (botão)</button>
                <input type="submit" value="Enviar dados ao back-end (botão input)">
            </form>
        </div>
    </section>
    """
