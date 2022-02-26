import requests
class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):

        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def __str__(self):

        return self.format_cep()

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        re = requests.get(url)
        dados = re.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
