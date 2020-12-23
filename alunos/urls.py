from django.urls import path, include

from alunos.views import IndexView, NacionalidadeLC, NacionalidadeRUD, AlunoLC, AlunoRUD, DisciplinaLC, DisciplinaRUD

app_name = 'alunos'

urlpatterns = [
    path('', IndexView.as_view()),
    path('nacionalidades/', NacionalidadeLC.as_view(), name="nacionalidades_lc"),
    path('nacionalidades/<pk>/', NacionalidadeRUD.as_view(), name="nacionalidades_rud"),

    # Alunos
    path('alunos/', AlunoLC.as_view(), name="alunos_lc"),
    path('alunos/<pk>/', AlunoRUD.as_view(), name="alunos_rud"),

    # Disciplina
    path('disciplinas/', DisciplinaLC.as_view(), name="disciplinas_lc"),
    path('disciplinas/<pk>/', DisciplinaRUD.as_view(), name="disciplinas_rud"),

]
	