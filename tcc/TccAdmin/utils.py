import datetime
from .models import *

def criar_bancas():

    #Cria uma grade para cada dia da semana
    grade = []
    for i in range(7):
        ano = datetime.date.today.year
        mes = datetime.date.today.month
        dia = datetime.date.today.day

        delta = datetime.timedelta(i)

        g = Grade(
            h1=Horario(datetime.datetime(ano,mes,dia+delta).replace(hour=7,minute=0))
            h2=Horario(datetime.datetime(ano,mes,dia+delta).replace(hour=8,minute=50))
            h3=Horario(datetime.datetime(ano,mes,dia+delta).replace(hour=10,minute=30))
            h4=Horario(datetime.datetime(ano,mes,dia+delta).replace(hour=13,minute=30))
            h5=Horario(datetime.datetime(ano,mes,dia+delta).replace(hour=15,minute=20))
            h6=Horario(datetime.datetime(ano,mes,dia+delta).replace(hour=17,minute=0))
            )
        grade.add(g)

    for a in Aluno.objects.all():
        inserido=False
        horario = None
        while not inserido:
            for g in grade:
                if g.h1.preenchido:
                    if g.h2.preenchido:
                        if g.h3.preenchido:
                            if g.h4.preenchido:
                                if g.h5.preenchido:
                                    if g.h6.preenchido:
                                        pass
                                    else:
                                        horario=g.h6
                                        g.h6.preenchido=True
                                        inserido=True
                                else:
                                    horario=g.h5
                                    g.h5.preenchido=True
                                    inserido=True
                            else:
                                horario=g.h4
                                g.h4.preenchido=True
                                inserido=True
                        else:
                            horario=g.h3
                            g.h3.preenchido=True
                            inserido=True
                    else:
                        horario=g.h2
                        g.h2.preenchido=True
                        inserido=True
                else:
                    horario=g.h1
                    g.h1.preenchido=True
                    inserido=True
                g.save()
                if inserido:
                    break
            else: #else do for. Se passou por todas as grades e nao inseriu, informa o problema e sai
                inserido=True
                print("Sem horarios disponiveis pra banca essa semana")
                criar=False
        #end while
        if criar:
            prof = None
            #TODO Selecionar professor
            for p in Professor.objects.all():
                prof=p

            Banca.objects.create(horario=horario,aluno=a,disciplina=a.disciplina_tcc,professor=prof) 




        


