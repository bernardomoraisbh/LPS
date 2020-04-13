from django.db import models

class TipoUsuario(models.Model):
    nome = models.CharField(max_length=50)

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)

    disciplinas = models.ManyToManyField(Disciplina)

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    tema_tcc = models.CharField(max_length=50)

    disciplina_tcc = models.ForeignKey(Disciplina,on_delete=models.CASCADE)

class Horario(models.Model):
    horario = models.DateTimeField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    
