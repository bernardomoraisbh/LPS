from django.db import models

class Horario(models.Model):
    horario = models.DateTimeField()
    preenchido = models.BooleanField(default=False)

class TipoUsuario(models.Model):
    nome = models.CharField(max_length=50)

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)
    grade = models.ForeignKey('Grade',on_delete=models.SET_NULL,null=True)

    disciplinas = models.ManyToManyField(Disciplina)

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    tema_tcc = models.CharField(max_length=50)

    disciplina_tcc = models.ForeignKey(Disciplina,on_delete=models.CASCADE)

class Banca(models.Model):
    horario = Horario
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

class Grade(models.Model):
    h1 = models.ForeignKey(Horario,on_delete=models.CASCADE)
    h2 = models.ForeignKey(Horario,on_delete=models.CASCADE)
    h3 = models.ForeignKey(Horario,on_delete=models.CASCADE) 
    h4 = models.ForeignKey(Horario,on_delete=models.CASCADE)
    h5 = models.ForeignKey(Horario,on_delete=models.CASCADE)
    h6 = models.ForeignKey(Horario,on_delete=models.CASCADE)
