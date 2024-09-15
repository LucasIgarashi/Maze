class Pessoa: 
    nome = "João"
    idade = 567
    nome_mae = "Alberta"

    def __init__(self,nome:str,idade:int) -> None:
        self.nome = nome
        self.idade = idade
    
    def getNome(self) -> None:
        return self.nome
    
    def getIdade(self):
        return self.idade
    
    def setNome(self,new_name):
        self.nome=new_name

    def setIdade(self,new_idade):
        self.idade=new_idade

    
Camila = Pessoa("Camila",22)
Rodolfa = Pessoa("Rodolfa",19)

Rodolfa.setNome("Isabela")

print(f"Camila\nidade = {Camila.idade}\nnome = {Camila.getNome()}")

print(Rodolfa.getNome(),Rodolfa.nome_mae)


class No:
    pai:int = 0
    filhos:list = []

a:float=6.4

print(a)
