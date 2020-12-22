from rest_framework import serializers
from .models import Nacionalidade, Aluno, Disciplina, Turma

class NacionalidadeSerializer(serializers.ModelSerializer):
	rud_url = serializers.SerializerMethodField()

	def get_rud_url(self, obj):
		return obj.get_rud_url()

	class Meta:
		model = Nacionalidade
		fields = '__all__'


class AlunoSerializer(serializers.ModelSerializer):
	#nacionalidade = NacionalidadeSerializer(many=False, read_only=False)
	rud_url = serializers.SerializerMethodField()
	get_nacionalidade = serializers.SerializerMethodField()

	def get_rud_url(self, obj):
		return obj.get_rud_url()

	def get_get_nacionalidade(self, obj):
		try:
			return obj.nacionalidade.nome
		except:
		 	return ''


	class Meta:
		model = Aluno
		fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):
	#alunos = AlunoSerializer(many=True, read_only=False)
	rud_url = serializers.SerializerMethodField()
	get_alunos = serializers.SerializerMethodField()

	def get_get_alunos(self, obj):
		return obj.get_alunos()

	def get_rud_url(self, obj):
		return obj.get_rud_url()


	class Meta:
		model = Disciplina
		fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
	disciplinas = DisciplinaSerializer(many=True, read_only=True)

	class Meta:
		model = Turma
		fields = '__all__'