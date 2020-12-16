from rest_framework import serializers
from .models import Nacionalidade, Aluno, Disciplina, Turma

class NacionalidadeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Nacionalidade
		fields = '__all__'


class AlunoSerializer(serializers.ModelSerializer):
	nacionalidade = NacionalidadeSerializer(many=False, read_only=True)

	class Meta:
		model = Aluno
		fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Disciplina
		fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
	disciplinas = DisciplinaSerializer(many=True, read_only=True)

	class Meta:
		model = Turma
		fields = '__all__'