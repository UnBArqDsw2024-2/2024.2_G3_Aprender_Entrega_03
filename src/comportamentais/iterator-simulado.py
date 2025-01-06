from abc import ABC, abstractmethod
from typing import List

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def has_previous(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def previous(self):
        pass

class Questao:
    def __init__(self, id_questao: int, texto: str):
        self.id_questao = id_questao
        self.texto = texto

    def get_texto(self) -> str:
        return self.texto

    def __str__(self):
        return f"Questao {self.id_questao}: {self.texto}"

class SimuladoIterator(Iterator):
    def __init__(self, questoes: List[Questao]):
        self.questoes = questoes
        self.current_index = -1

    def has_next(self) -> bool:
        return self.current_index < len(self.questoes) - 1

    def has_previous(self) -> bool:
        return self.current_index > 0

    def next(self) -> Questao:
        if self.has_next():
            self.current_index += 1
            return self.questoes[self.current_index]
        raise StopIteration("Não há próxima questão.")

    def previous(self) -> Questao:
        if self.has_previous():
            self.current_index -= 1
            return self.questoes[self.current_index]
        raise StopIteration("Não há questão anterior.")

class Simulado:
    def __init__(self, id_simulado: int):
        self.id_simulado = id_simulado
        self.questoes = []

    def adicionar_questao(self, questao: Questao):
        self.questoes.append(questao)

    def get_iterator(self) -> SimuladoIterator:
        return SimuladoIterator(self.questoes)

if __name__ == "__main__":
    simulado = Simulado(1)

    simulado.adicionar_questao(Questao(1, "O que é POO?"))
    simulado.adicionar_questao(Questao(2, "O que é Herança?"))
    simulado.adicionar_questao(Questao(3, "O que é Polimorfismo?"))

    iterator = simulado.get_iterator()

    print("Navegando para frente:")
    while iterator.has_next():
        questao = iterator.next()
        print(questao)

    print("\nNavegando para trás:")
    while iterator.has_previous():
        questao = iterator.previous()
        print(questao)