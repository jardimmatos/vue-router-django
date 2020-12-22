from django.db.models import ProtectedError
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from alunos.models import Nacionalidade, Aluno, Disciplina
from alunos.serializers import NacionalidadeSerializer, AlunoSerializer, DisciplinaSerializer



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

    def perform_destroy(self, instance):
        print(instance)
        try:
            instance.delete()
            print('teste')
        except:
            print('teste 2')
            raise serializers.ValidationError('Não foi possível excluir Nacionalidade: ')



                       

class AlunoLC(generics.ListCreateAPIView):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]
    model = Aluno
    queryset = model.objects.all()
    serializer_class = AlunoSerializer

    def perform_create(self, serializer):
        """
        Necessário quando se quer alterar o comportamente ao criar
        """
        serializer.save()


class AlunoRUD(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]
    model = Aluno
    queryset = model.objects.all()
    serializer_class = AlunoSerializer

    def perform_update(self, serializer):
        # serializer.save(created_by=self.request.user.username, updated_by=self.request.user.username)
        serializer.save()

                        # Disciplina

class DisciplinaLC(generics.ListCreateAPIView):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]
    model = Disciplina
    queryset = model.objects.all()
    serializer_class = DisciplinaSerializer

    def perform_create(self, serializer):
        """
        Necessário quando se quer alterar o comportamente ao criar
        """
        serializer.save()


class DisciplinaRUD(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]
    model = Disciplina
    queryset = model.objects.all()
    serializer_class = DisciplinaSerializer

    def perform_update(self, serializer):
        # serializer.save(created_by=self.request.user.username, updated_by=self.request.user.username)
        serializer.save()




