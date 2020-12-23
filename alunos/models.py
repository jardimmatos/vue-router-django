from django.db import models
from django.urls import reverse


class Nacionalidade(models.Model):
	nome = models.CharField(max_length=100, null=True, blank=False, verbose_name="Nacionalidade")
	pais = models.CharField(max_length=100, null=True, blank=False, verbose_name='País')
	sigla = models.CharField(max_length=2, null=True, blank=False)

	def get_rud_url(self):
		return reverse('alunos:nacionalidades_rud',args=(self.pk,))

	def __str__(self):
		return self.nome

	class Meta:
		unique_together = ('nome','pais','sigla')


class Aluno(models.Model):
	matricula = models.CharField(max_length=10, null=True, blank=False, unique=True, verbose_name='Nome')
	nome = models.CharField(max_length=150, null=True, blank=False, verbose_name='Nome')
	nacionalidade = models.ForeignKey(Nacionalidade, on_delete=models.PROTECT, null=True, blank=False, related_name="alunos")

	def get_rud_url(self):
		return reverse('alunos:alunos_rud',args=(self.pk,))

	def __str__(self):
		return self.nome


class Disciplina(models.Model):
	descricao = models.CharField(max_length=150, null=True, unique=True, blank=False, verbose_name='Disciplina')
	alunos = models.ManyToManyField(Aluno, related_name="disciplinas")

	def __str__(self):
		return self.descricao

	def get_rud_url(self):
		return reverse('alunos:disciplinas_rud',args=(self.pk,))

	def get_alunos(self):
		return self.alunos.values('nome','matricula','nacionalidade__nome')


class Turma(models.Model):
	descricao = models.CharField(max_length=20, null=True, blank=False, unique=True, verbose_name='Turma')
	disciplinas = models.ManyToManyField(Disciplina, related_name="turmas")

	def __str__(self):
		return self.descricao


