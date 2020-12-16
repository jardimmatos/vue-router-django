from django.urls import path, include

from alunos.views import IndexView

urlpatterns = [
    path('', IndexView.as_view())
]
