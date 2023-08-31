

"""
* Views do tipo "FormView" possuem funções: [form_valid, form_invalid]
* A variável interna usada nessas funções, se chama [form], que também é passada ao template via {{ form }}
* O uso dessa variável é somente p/ salvar novos objetos num modelo e EXIBIR ELES NO TERMINAL
* Essa variável não consegue mostrar os dados no template por "var. self" dentro da view
* Para conseguir, o único meio é salvando o objeto e o resgatando do modelo
* Sabendo disso, o exemplo abaixo não funcionaria

========== EXEMPLO QUE FUNCIONA ==========
* No terminal, é possível ver os dados passados no(s) input(s), e "form.save()" anexa um novo objeto em um modelo

def form_valid(self, form):
    print(dir(form))
    print('--->', form.cleaned_data.get('nome_do_valor_do_atrib_name_no_input_alvo'))
    form.save()
    messages.success(self.request, 'Mensagem de sucesso')
    return super(LanguageFormView, self).form_valid(form)

* ========== EXEMPLO QUE NÃO FUNCIONA ==========
* Todos os dados abaixo são funções que podem ser criadas numa view do tipo "FormView"
* O template não conseguirá exibir o valor passado p/ "self.data", pois não é assim que se resgata dados

__init__         || self.data = ''
form_valid       || self.data = form.cleaned_data.get('input_atrib_name')
get_context_data || context['data'] = self.data

"""
