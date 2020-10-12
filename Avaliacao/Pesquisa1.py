import json
from io import StringIO
class Pesquisa1 :

    def convesao (self,data):
        io = StringIO(data)
        conv = json.load(io)
        sex_category = ''
        age_category = ''
        address_category = ''
        famsize_category = ''
        Pstatus_category = ''
        Medu_category = ''
        Fedu_category = ''
        Mjob_category = ''
        Fjob_category = ''
        reason_category = ''
        guardian_category = ''
        traveltime_category = ''
        studytime_category = ''
        failures_category = ''
        schoolsup_category = ''
        famsup_category = ''
        activities_category = ''
        nursery_category = ''
        higher_category = ''
        internet_category = ''
        romantic_category = ''
        famrel_category = ''
        freetime_category = ''
        goout_category = ''
        dalc_category = ''
        walc_category = ''
        health_category = ''
        absences_category = ''


        if (conv[0] == 'Feminino') or (conv[0] == 'Masculino'):
            if conv[0] == 'Feminino':
                sex_category = 0
            else:
                sex_category = 1

        try:
            if 15 <= int(conv[1]) <= 22:
                age_category = int(conv[1])
        except:
            return  None

        if (conv[2] == 'Urbano') or (conv[2] == 'Rural'):
            if conv[2] == 'Urbano':
                address_category = 0
            else:
                address_category = 1

        if (conv[3] == 'Menor ou igual a 3 pessoas') or (conv[3] == 'Mais de 3 pessoas'):
            if conv[3] == 'Menos de 3 pessoas':
                famsize_category = 0
            else:
                famsize_category = 1

        if (conv[4] == 'Juntos') or (conv[4] == 'Separados'):
            if conv[4] == 'Juntos':
                Pstatus_category = 0
            else:
                Pstatus_category = 1

        if conv[5] == 'Nenhuma':
                Medu_category = 0
        elif conv[5] == 'Educação primária até o 4 ano':
                Medu_category = 1
        elif conv[5] == 'Do 5 ao 9 ano':
                Medu_category = 2
        elif conv[5] == 'Educação secundária':
                Medu_category = 3
        elif conv[5] == 'Educação Superior':
                Medu_category = 4


        if conv[6] == 'Nenhuma':
                Fedu_category = 0
        elif conv[6] == 'Educação primária até o 4 ano':
                Fedu_category= 1
        elif conv[6] == 'Do 5 ao 9 ano':
                Fedu_category = 2
        elif conv[6] == 'Educação secundária':
                Fedu_category = 3
        elif conv[6] == 'Educação Superior':
                Fedu_category = 4

        if conv[7] == 'Professora':
                Mjob_category = 0
        elif conv[7] == 'Saúde':
                Mjob_category = 1
        elif conv[7] == 'Serviços':
                Mjob_category = 2
        elif conv[7] == 'Em casa':
                Mjob_category = 3
        elif conv[7] == 'Outro':
                Mjob_category = 4

        if conv[8] == 'Professor':
            Fjob_category = 0
        elif conv[8] == 'Saúde':
            Fjob_category = 1
        elif conv[8] == 'Serviços':
            Fjob_category = 2
        elif conv[8] == 'Em casa':
            Fjob_category = 3
        elif conv[8] == 'Outro':
            Fjob_category = 4


        if conv[9] == 'Perto de casa':
            reason_category = 0
        elif conv[9] == 'Reputação':
            reason_category = 1
        elif conv[9] == 'Cursos':
            reason_category = 2
        elif conv[9] == 'Outro':
            reason_category = 3


        if conv[10] == 'Mãe':
            guardian_category = 0
        elif conv[10] == 'Pai':
            guardian_category = 1
        elif conv[10] == 'Outro':
            guardian_category = 2

        if conv[11] == 'Menos que 15 minutos':
            traveltime_category  = 1
        elif conv[11] == 'Entre 15 e 30 minutos':
            traveltime_category = 2
        elif conv[11] == 'Entre 30 minutos e 1 hora':
            traveltime_category  = 3
        elif conv[11] == 'Mais que 1 hora':
            traveltime_category  = 4

        if conv[12] == 'Menos que 2 horas':
            studytime_category = 1
        elif conv[12] == 'Entre 2 e 5 horas':
            studytime_category = 2
        elif conv[12] == 'Entre 5 e 10 horas':
            studytime_category = 3
        elif conv[12] == 'Mais que 10 horas':
            studytime_category = 4

        if conv[13].isnumeric():
            if 0 <= int(conv[13]) <= 3:
                failures_category = int(conv[13])
            else:
                failures_category = 4

        if conv[14] == 'Sim' :
            schoolsup_category = 1
        elif conv[14] == 'Não':
            schoolsup_category = 0

        if conv[15] == 'Sim':
            famsup_category = 1
        elif conv[15] == 'Não':
            famsup_category = 0

        if conv[16] == 'Sim':
            activities_category = 1
        elif conv[16] == 'Não':
            activities_category = 0

        if conv[17] == 'Sim':
            nursery_category = 1
        elif conv[17] == 'Não':
            nursery_category = 0

        if conv[18] == 'Sim':
            higher_category = 1
        elif conv[18] == 'Não':
            higher_category = 0

        if conv[19] == 'Sim':
            internet_category = 1
        elif conv[19] == 'Não':
            internet_category = 0

        if conv[20] == 'Sim':
            romantic_category = 1
        elif conv[20] == 'Não':
            romantic_category = 0

        try:
            if 1 <= int(conv[21]) <= 5:
                famrel_category = int(conv[21])
        except:
            return None

        try:
            if 1 <= int(conv[22]) <= 5:
                freetime_category = int(conv[22])
        except:
            return None

        try:
            if 1 <= int(conv[23]) <= 5:
                goout_category = int(conv[23])
        except:
            return None

        try:
            if 1 <= int(conv[24]) <= 5:
                dalc_category = int(conv[24])
        except:
            return None

        try:
            if 1 <= int(conv[25]) <= 5:
                walc_category = int(conv[25])
        except:
            return None

        try:
            if 1 <= int(conv[26]) <= 5:
                health_category = int(conv[26])
        except:
            return None

        try:
            if 0 <= int(conv[27]) <= 93:
                absences_category = int(conv[27])
        except:
            return None


        return (sex_category ,
        age_category ,
        address_category ,
        famsize_category ,
        Pstatus_category ,
        Medu_category ,
        Fedu_category ,
        Mjob_category ,
        Fjob_category ,
        reason_category ,
        guardian_category ,
        traveltime_category ,
        studytime_category ,
        failures_category ,
        schoolsup_category ,
        famsup_category ,
        activities_category ,
        nursery_category ,
        higher_category ,
        internet_category ,
        romantic_category ,
        famrel_category,
        freetime_category ,
        goout_category ,
        dalc_category ,
        walc_category ,
        health_category,
        absences_category)





