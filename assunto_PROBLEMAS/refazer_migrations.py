

"""
Quando fazer || em modo desenvolvimento
Contexto     || quando há modelos relacionados (OneToOneField, ForeignKey, OneToManyField)
Contexto     || quando for preciso corrigir algo feito errado

========== PROCEDIMENTOS ==========
* Comentar todo o conteúdo nos arquivos: (admin.py, models.py, views.py)
* Comentar os índices da lista em: (urls.py)
* python manage.py makemigrations
* python manage.py mmigrate
* Descomentar o conteúdo nos arquivos: (admin.py, models.py)
* python manage.py makemigrations
* python manage.py mmigrate
* Descomentar os conteúdos nos arquivos: (urls.py, views.py)
"""
