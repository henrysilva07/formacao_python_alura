from datetime import datetime


class DatasBr:

    def __init__(self):
        self._momento_cadastro = datetime.today()

    def mes_cadastro(self):

        lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril"
                 "Maio" , "Junho" , "Julho" "Agosto" ,
                 "Setembro" , "Outubro" , "Novembro", "Dezembro"]

        mes_cadastro = self._momento_cadastro.month - 1

        return lista_meses[mes_cadastro]


    def dia_semana(self):

        lista_semana = ["Segunda" , "Terça", "Quarta",
                        "Quinta", "Sexta", "Sábado", "Domingo"]

        dia_semana = self._momento_cadastro.weekday()

        return lista_semana[dia_semana]

    def _format_data(self):

        data_formatada = self._momento_cadastro.strftime("%d-%m-%Y %H:%m")

        return data_formatada

    def __str__(self):

        return self._format_data()

    def tempo_cadastro(self):

        return datetime.today() - self._momento_cadastro

