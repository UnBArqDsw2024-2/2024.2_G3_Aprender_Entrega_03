from abc import ABC, abstractmethod
from datetime import datetime

class ElementoCronograma(ABC):
  @abstractmethod
  def exibirDetalhes(self):
    pass
  
  @abstractmethod
  def obterDuracaoTotal(self): # int para simplificar o exemplo, utilizando a escala em dias
    pass
  
  @abstractmethod
  def obterPontuacaoTotal(self) -> int:
    pass

class Atividade(ElementoCronograma):
  def __init__(self, idAtividade: int, descricao: str, tema: str, duracao: int, idCronograma: int):
    self.idAtividade = idAtividade
    self.descricao = descricao
    self.tema = tema
    self.duracao = duracao
    self.completada = False
    self.idCronograma = idCronograma
    self.pontuacao = 0

  def exibirDetalhes(self):
    return f'''Descricao: {self.descricao},
Tema: {self.tema},
Duracao: {self.duracao} dias,
Pontuacao: {self.pontuacao}.
'''

  def obterDuracaoTotal(self) -> int:
    return self.duracao
  
  def obterPontuacaoTotal(self) -> int:
    return self.pontuacao
  
  def marcarComoCompletada(self):
    self.completada = True
  
  def atribuirPontuacao(self, pontos: int):
    self.pontuacao = pontos

class Cronograma(ElementoCronograma):
  def __init__(self, idCronograma: int, atividades: list):
    self.idCronograma = idCronograma
    self.atividades = atividades
    self.dataCriacao = datetime.now()

  def exibirDetalhes(self):
    atividades = ""
    if self.atividades:
      atividades = ""
      for i in self.atividades:
        atividades += f"{i.descricao}, "

    return f'''Atividades: {atividades or "Nenhuma atividade,"}
Data de Criacao: {self.dataCriacao},
Duracao Total: {self.obterDuracaoTotal()},
Pontuacao Total: {self.obterPontuacaoTotal()}.
'''

  def obterDuracaoTotal(self):
    total = 0
    for i in self.atividades:
      total += i.obterPontuacaoTotal()

    return total

  def obterPontuacaoTotal(self) -> int:
    total = 0
    for i in self.atividades:
      total += i.obterPontuacaoTotal()
    
    return total

  def adicionarAtividade(self, elemento: ElementoCronograma):
    self.atividades.append(elemento)
  
  def removerAtividade(self, elemento: ElementoCronograma):
    self.atividades.remove(elemento)
  
if __name__ == "__main__":
  cronograma = Cronograma(1, [])

  atividade1 = Atividade(1, "Estudar", "Matematica", 3, 1)
  print(atividade1.exibirDetalhes())
  atividade2 = Atividade(2, "Fazer exercícios", "Matematica", 6, 1)
  print(atividade2.exibirDetalhes())

  cronograma.adicionarAtividade(atividade1)
  cronograma.adicionarAtividade(atividade2)
  print(cronograma.exibirDetalhes())

  cronograma.removerAtividade(atividade1)
  cronograma.removerAtividade(atividade2)
  print(cronograma.exibirDetalhes())