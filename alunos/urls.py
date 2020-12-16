from django.urls import path, include

from alunos.views import IndexView, NacionalidadeLC, NacionalidadeRUD

app_name = 'alunos'

urlpatterns = [
    path('', IndexView.as_view()),
    path('nacionalidades/', NacionalidadeLC.as_view(), name="nacionalidades_lc"),
    path('nacionalidades/<pk>/', NacionalidadeRUD.as_view(), name="nacionalidades_rud"),
]
