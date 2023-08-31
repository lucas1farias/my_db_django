

def models():
    """
    * O modelo alvo é "Language", ele conversará com um modelo de formulário em "pa/forms.py" (é criado e configurado)
    * A comunicação se dá pelos atributos criados em "Language" que são passados igualmente p/ o "ModelForm"
    * Mais infos: ver parte 4

    from django.db import models

    class Language(models.Model):

        name = models.CharField('Nome', max_length=100)

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Linguagem'
            verbose_name_plural = 'Linguagens'
    """


def admin():
    """
    * O modelo + os atributos desejados a serem exibidos, são passados

    from django.contrib import admin
    from .models import *

    @admin.register(Child)
    class ChildAdmin(admin.ModelAdmin):
        list_display = ('name',)
    """


def terminal():
    """
    python manage.py makemigrations
    python manage.py migrate
    """


def forms():
    """
    * Criar na raiz da aplicação, um módulo "forms.py"
    * O modelo a conversar com o modelo formulário, deve ser importado em "forms.py"
    * Basicamente, temos uma "conversa" entre um "modelo" e um "formulário modelo"
    * No "formulário modelo" são clonados os campos do "modelo" manualmente
    * Ou seja, todos os campo de um "modelo" são recriados em um "modelo formulário"
    * A conexão entre os modelos se dá via "class Meta"

    * ========== IMPORTANTE ==========
    * Após esse "modelo formulário" se conectar a uma view, no template, ele ganha configurações IMPLÍCITAS
    * Para ver essas informações, é preciso ir ao template e INSPECIONAR
    * Por exemplo, o campo criado no "formulário modelo" é passado como os atrib.: id & name
    * EXEMPLO     || country = forms.CharField(max_length=100)
    * NO TEMPLATE || <input id="country" name="country">

    from django import forms
    from .models import *

    class LanguageModelForm(forms.ModelForm):
        class Meta:
            model = Language
            fields = ('name',)
            name = forms.CharField(max_length=100)
    """


def views():
    """
    * O "formulário modelo" após ser criado, é enviado a view e é identificao pela var. "form_class"
    * Juntamente de "forms.py", como o "modelo" está importado para lá, ele não precisa ser importado novamente
    * Por convenção, a view que renderizará os campos do "formulário modelo", deve ser do tipo "FormView"
    * Views do tipo "FormView", recebem implicitamente as funções: [form_valid, form_invalid]
    * Essas funções trazem tratamentos IMPLÍCITOS, como por exemplo, o atrib. <required>
    * ========== OPCIONAL ==========
    * Função "get_last_object_data"
    * Serve apenas p/ demonstrar que o "formulário modelo" funciona
    * Ela trabalha em conjunto com: "__init__" e "get_context_data"

    from .forms import *
    from django.views.generic import FormView
    from django.urls import reverse_lazy
    from django.contrib import messages

    class LanguageFormView(FormView):
        template_name = 'model_form.html'
        form_class = LanguageModelForm
        success_url = reverse_lazy('model_form')  # nome do url desta view

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.db = Language.objects.all()
            self.last_object = ''

            if len(self.db) == 0:
                mock_obj = Language(name='Python')
                mock_obj.save()
            else:
                self.last_object = self.get_last_object_data()

        def get_last_object_data(self) -> str:
            db_size = len(self.db) - 1
            last_object_from_db = None

            for pos, index in enumerate(self.db):
                # Se chegar no último índice do banco, pegar o atributo deste objeto neste índice
                if pos == db_size:
                    last_object_from_db = self.db[pos].name

            # Porque usar 'filter'? por lidar com objetos repetidos, enquanto 'get' só lida com um objeto
            # Enquanto 'get' só achar uma ocorrência, seu uso é melhor, mas quando houver objetos repetidos, ele gera erro
            last_input = Language.objects.filter(name=last_object_from_db)
            return last_input[0].name

        def form_valid(self, form):
            print(dir(form))
            print('--->', form.cleaned_data.get('name'))
            form.save()
            messages.success(self.request, 'Linguagem enviada')
            return super(LanguageFormView, self).form_valid(form)

        def form_invalid(self, form):
            messages.error(self.request, 'Erros nos campos')
            return super(LanguageFormView, self).form_invalid(form)

        def get_context_data(self, **kwargs):
            context = super(LanguageFormView, self).get_context_data(**kwargs)
            context['db'] = self.db
            context['input_value'] = self.last_object
            return context
    """


def urls():
    """
    path('model_form', LanguageFormView.as_view(), name='model_form')
    """


def html():
    """
    * A view configurada como "FormView" permite que o formulário seja chamado no template como {{ form }}
    * O atributo "action" remete a própria página. Se fosse p/ ir a outra lugar, se passa o url de outro template
    * O atributo "method" sempre é "post", o que indica que o formulário está a receber dados
    * O envio se dá por botão ou input, ambas formas funcionam

    <section>
        <div>
            <h2>Teste de formulário com model form Django</h2>
            <h5>Ordem: models.py, admin.py, forms.py, views.py, urls.py, template</h5>

            <form action="{% url 'model_form' %}" method="post">
                {% csrf_token %}
                {{ form }}

                <button type="submit">Enviar (via button)</button>
                <input type="submit" value="Enviar (via input)">
            </form>

            <div>Último dado enviado:<span class="btn btn-success">{{ input_value }}</span></div>
        </div>
    </section>
    """
