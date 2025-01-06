from abc import ABC, abstractmethod
import time

class Observer(ABC):
    @abstractmethod
    def update(self, state: str):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class Timer(Subject):
    def __init__(self):
        self.observers = []
        self.state = None
        self.tempo_limite = 0
        self.tempo_inicio = None

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.state)

    def configurar_tempo(self, tempo_limite: int):
        """Configura o tempo limite (em segundos) para o Timer."""
        self.tempo_limite = tempo_limite

    def iniciar(self):
        self.state = "iniciado"
        self.tempo_inicio = time.time()
        print("Timer iniciado.")
        self.notify()
        self._verificar_tempo()

    def _verificar_tempo(self):
        """Verifica se o tempo limite foi atingido e atualiza o estado."""
        while True:
            elapsed = time.time() - self.tempo_inicio
            if elapsed >= self.tempo_limite:
                self.state = "finalizado"
                print("Tempo limite atingido. Timer finalizado.")
                self.notify()
                break
            time.sleep(1) # pode ser interessante usar thread para não bloquear I/O

    def pausar(self):
        self.state = "pausado"
        print("Timer pausado.")
        self.notify()

    def resetar(self):
        self.state = "resetado"
        self.tempo_inicio = None
        print("Timer resetado.")
        self.notify()

class Simulado(Observer):
    def __init__(self, id_simulado: int):
        self.id_simulado = id_simulado
        self.status = "inativo"

    def update(self, state: str):
        self.status = state
        print(f"Simulado {self.id_simulado} atualizado. Novo estado: {self.status}")

        if state == "finalizado":
            self.finalizar_simulado()

    def finalizar_simulado(self):
        """Executa ações específicas ao finalizar o simulado."""
        print(f"Simulado {self.id_simulado} foi finalizado automaticamente.")

if __name__ == "__main__":
    timer = Timer()

    simulado1 = Simulado(1)
    simulado2 = Simulado(2)

    timer.attach(simulado1)
    timer.attach(simulado2)

    timer.configurar_tempo(5)

    timer.iniciar()