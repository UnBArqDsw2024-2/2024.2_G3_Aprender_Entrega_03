from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, usuario_id: int, experiencia: int):
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

class Usuario(Subject):
    def __init__(self, id_usuario: int, nome: str):
        self.id_usuario = id_usuario
        self.nome = nome
        self.experiencia = 0
        self.nivel = 1
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.id_usuario, self.experiencia)

    def calcular_experiencia(self, pontos: int):
        self.experiencia += pontos
        print(f"Usuário {self.nome} ganhou {pontos} pontos de experiência. Experiência total: {self.experiencia}")

        self.notify()

class Emblema(Observer):
    def __init__(self, id_emblema: int, nome: str, requisito_experiencia: int):
        self.id_emblema = id_emblema
        self.nome = nome
        self.requisito_experiencia = requisito_experiencia
        self.usuarios_conquistaram = []

    def update(self, usuario_id: int, experiencia: int):
        if experiencia >= self.requisito_experiencia and usuario_id not in self.usuarios_conquistaram:
            self.conquistar(usuario_id)

    def conquistar(self, usuario_id: int):
        self.usuarios_conquistaram.append(usuario_id)
        print(f"Usuário {usuario_id} conquistou o emblema '{self.nome}'!")

if __name__ == "__main__":
    usuario = Usuario(1, "João")

    emblema1 = Emblema(1, "Iniciante", 10)
    emblema2 = Emblema(2, "Veterano", 50)

    usuario.attach(emblema1)
    usuario.attach(emblema2)

    usuario.calcular_experiencia(5) 
    usuario.calcular_experiencia(10)
    usuario.calcular_experiencia(40)