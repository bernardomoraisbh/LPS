from django.db import models

class Horario(models.Model):
    horario = models.DateTimeField()
    preenchido_banca = models.BooleanField(default=False)
    preenchido_prof = models.BooleanField(default=False)

    def __str__(self):
        return self.horario.strftime('%Y/%m/%d - %H:%M')

class TipoUsuario(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)
    aulas = models.ForeignKey('GradeAula',on_delete=models.SET_NULL,null=True)

    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    tema_tcc = models.CharField(max_length=50)

    disciplina_tcc = models.ForeignKey(Disciplina,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Banca(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, null=True, blank=True, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.aluno.__str__() + " " + self.professor.__str__()

class GradeAula(models.Model):
    nome = models.CharField(max_length=50)
    horarios = models.ManyToManyField(Horario)

    def __str__(self):
        return self.nome

class GradeTcc(models.Model):
    nome = models.CharField(max_length=50)
    horarios = models.ManyToManyField(Horario)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
