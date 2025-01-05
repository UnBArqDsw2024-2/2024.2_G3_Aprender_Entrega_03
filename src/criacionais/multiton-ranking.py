class Usuario:
    def __init__(self, id_usuario: int, nome: str):
        self.id_usuario = id_usuario
        self.nome = nome

    def __repr__(self):
        return f"Usuario(id={self.id_usuario}, nome='{self.nome}')"


class Ranking:
    _instances = {}

    def __new__(cls, idRanking: int, *args, **kwargs):
        if idRanking not in cls._instances:
            instance = super(Ranking, cls).__new__(cls)
            instance.idRanking = idRanking
            instance.usuariosRanqueados = []
            cls._instances[idRanking] = instance
        return cls._instances[idRanking]

    @classmethod
    def getRankingInstance(cls, idRanking: int):
        return cls._instances.get(idRanking)

    def incluirUsuarioNoRanking(self, usuario: Usuario):
        if usuario not in self.usuariosRanqueados:
            self.usuariosRanqueados.append(usuario)
            print(f"Usuário {usuario.nome} adicionado ao ranking {self.idRanking}.")
        else:
            print(f"Usuário {usuario.nome} já está no ranking {self.idRanking}.")

    def excluirUsuarioDoRanking(self, usuario: Usuario):
        if usuario in self.usuariosRanqueados:
            self.usuariosRanqueados.remove(usuario)
            print(f"Usuário {usuario.nome} removido do ranking {self.idRanking}.")
        else:
            print(f"Usuário {usuario.nome} não está no ranking {self.idRanking}.")

    def obterPosicao(self, usuario: Usuario):
        if usuario in self.usuariosRanqueados:
            posicao = self.usuariosRanqueados.index(usuario) + 1
            print(f"Usuário {usuario.nome} está na posição {posicao} no ranking {self.idRanking}.")
            return posicao
        else:
            print(f"Usuário {usuario.nome} não está no ranking {self.idRanking}.")
            return None

    def exibirRanking(self):
        print(f"Ranking {self.idRanking}:")
        for i, usuario in enumerate(self.usuariosRanqueados, start=1):
            print(f"{i}. {usuario.nome}")


if __name__ == "__main__":
    usuario1 = Usuario(1, "Alice")
    usuario2 = Usuario(2, "Bob")
    usuario3 = Usuario(3, "Carol")
    usuario4 = Usuario(4, "David")

    ranking1 = Ranking(101)
    ranking2 = Ranking(102)

    ranking1.incluirUsuarioNoRanking(usuario1)
    ranking1.incluirUsuarioNoRanking(usuario2)
    ranking2.incluirUsuarioNoRanking(usuario3)
    ranking2.incluirUsuarioNoRanking(usuario4)

    ranking1.exibirRanking()
    ranking2.exibirRanking()

    ranking1.obterPosicao(usuario1)
    ranking2.obterPosicao(usuario4)

    same_ranking1 = Ranking.getRankingInstance(101)
    print("Same instance for ranking 101:", ranking1 is same_ranking1)

    ranking1.excluirUsuarioDoRanking(usuario2)
    ranking1.exibirRanking()
