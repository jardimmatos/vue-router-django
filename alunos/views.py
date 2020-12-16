from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from alunos.models import Nacionalidade
from alunos.serializers import NacionalidadeSerializer


class IndexView(TemplateView):
    template_name = 'base.html'


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return # To not perform the csrf check previously happening

class NacionalidadeLC(generics.ListCreateAPIView):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]
    model = Nacionalidade
    queryset = model.objects.all()
    serializer_class = NacionalidadeSerializer

    def perform_create(self, serializer):
        """
        Necessário quando se quer alterar o comportamente ao criar
        """
        serializer.save()


class NacionalidadeRUD(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]
    model = Nacionalidade
    queryset = model.objects.all()
    serializer_class = NacionalidadeSerializer

    def perform_update(self, serializer):
        # serializer.save(created_by=self.request.user.username, updated_by=self.request.user.username)
        serializer.save()

    def __init__(self, *args, **kwargs):
        super(NacionalidadeRUD, self).__init__(*args, **kwargs)

