import datetime
from .models import *

def criar_bancas():

    #admite apenas uma grade
    grade = Grade.objects.filter(professor_set = None)[0]

    #para cada aluno, encaixa seu tema em um horario e dia da grade
    for a in Aluno.objects.all():
        #insere no proximo horario vago
        h = grade.horarios.filter(preenchido=False)[0]
        #Cria uma banca para esse horario
        Banca.objects.create(horario=h,aluno=a,disciplina=a.disciplina_tcc,professor=None) 
        #marca o horario como preenchido
        h.preenchido=True
        h.save()

    #para cada banca, associa um professor que estiver disponivel
    for b in Banca.objects.all():
        #encontra o professor disponivel
        prof = None
        for p in Professor.objects.all():
            #professor esta disponivel se possui horario vago no horario da banca
            if b.horario in p.grade.horarios.filter(preenchido=False):
                prof=p
                #marca o horario como preenchido
                horario = p.grade.horarios.filter(horario=b.horario.horario)[0]
                horario.preenchido = True
                horario.save()
                break
        else: #do for mesmo
            raise Exception
            
        b.professor=prof
        b.save()
