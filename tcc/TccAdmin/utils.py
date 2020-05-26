import datetime
from .models import *

def criar_bancas():

    #Cria uma grade para cada dia da semana

    a = None
    #para cada aluno, encaixa seu tema em um horario e dia da grade
    for a in Aluno.objects.all():
        pass
        #inserir na grade onde couber
        Banca.objects.create(horario=horario,aluno=a,disciplina=a.disciplina_tcc,professor=None) 


    prof = None
    #para cada banca, associa um professor que estiver disponivel
    for b in Banca.objects.all():
        #encontra o professor disponivel
        for p in Professor.objects.all():
            pass
        b.professor=prof
        b.save()
        





        


