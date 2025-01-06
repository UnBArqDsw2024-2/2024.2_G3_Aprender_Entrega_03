from abc import ABC, abstractmethod
from datetime import datetime

class Questao:
    def __init__(self, id_questao: int, texto: str):
        self.id_questao = id_questao
        self.texto = texto

    def get_texto(self) -> str:
        return self.texto

class SimuladoStrategy(ABC):
    @abstractmethod
    def configurar_simulado(self, config: dict):
        pass

    @abstractmethod
    def finalizar(self):
        pass

class SimuladoPadraoStrategy(SimuladoStrategy):
    def configurar_simulado(self, config: dict):
        print("Configurando simulado padrão com as configurações:", config)

    def finalizar(self):
        print("Finalizando simulado padrão.")

class SimuladoPersonalizadoStrategy(SimuladoStrategy):
    def configurar_simulado(self, config: dict):
        print("Configurando simulado personalizado com as configurações:", config)

    def pausar(self):
        print("Simulado personalizado pausado.")

    def retomar(self):
        print("Simulado personalizado retomado.")

    def finalizar(self):
        print("Finalizando simulado personalizado.")

class Simulado:
    def __init__(self, id_simulado: int, questoes: list[Questao], strategy: SimuladoStrategy):
        self.id_simulado = id_simulado
        self.questoes = questoes
        self.data_inicio = None
        self.data_termino = None
        self.strategy = strategy

    def iniciar(self):
        self.data_inicio = datetime.now()
        print(f"Simulado {self.id_simulado} iniciado em {self.data_inicio}.")

    def configurar_simulado(self, config: dict):
        self.strategy.configurar_simulado(config)

    def finalizar(self):
        self.data_termino = datetime.now()
        self.strategy.finalizar()
        print(f"Simulado {self.id_simulado} finalizado em {self.data_termino}.")

if __name__ == "__main__":
    questao1 = Questao(1, "Qual é a capital do Brasil?")
    questao2 = Questao(2, "Qual é a fórmula da água?")
    questoes = [questao1, questao2]

    simulado_padrao = Simulado(101, questoes, SimuladoPadraoStrategy())
    simulado_padrao.iniciar()
    simulado_padrao.configurar_simulado({"duracao": "60 minutos", "nivel": "intermediário"})
    simulado_padrao.finalizar()

    print("\n")

    simulado_personalizado = Simulado(102, questoes, SimuladoPersonalizadoStrategy())
    simulado_personalizado.iniciar()
    simulado_personalizado.configurar_simulado({"duracao": "120 minutos", "nivel": "avançado"})
    simulado_personalizado.strategy.pausar()
    simulado_personalizado.strategy.retomar()
    simulado_personalizado.finalizar()