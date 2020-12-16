from django.contrib import admin

from alunos.models import Aluno, Nacionalidade, Disciplina, Turma


@admin.register(Nacionalidade)
class NacionalidadeAdmin(admin.ModelAdmin):
    pass

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    pass

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    pass

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    pass