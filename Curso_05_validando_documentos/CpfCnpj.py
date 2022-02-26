from validate_docbr import CPF, CNPJ

class documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)

        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de Dígitos incorreta")

class DocCpf:

    def __init__(self, documento):

        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")

    def valida(self, documento):
        valida = CPF()
        return valida.validate(documento)

    def __str__(self):
        return self.format()

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:

    def __init__(self, documento):
        documento = str(documento)
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!")

    def valida(self, documento):
        valida = CNPJ()
        return valida.validate(documento)

    def __str__(self):
        return self.format()

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)



