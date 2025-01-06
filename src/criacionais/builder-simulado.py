from datetime import datetime, timedelta

class Simulado:
    def __init__(self):
        self.idSimulado = None
        self.usuario = None
        self.dataInicio = None
        self.dataTermino = None
        self.perguntas = []
        self.tempoLimite = None
        self.pontuacao = 0
        self.status = None
        self.dificuldadeMedia = 0.0
        self.percentualConclusao = 0.0

    def calcularPontuacao(self):
        self.pontuacao = sum([questao['pontuacao'] for questao in self.perguntas])
        return self.pontuacao

    def calcularDificuldadeMedia(self):
        if self.perguntas:
            self.dificuldadeMedia = sum([questao['dificuldade'] for questao in self.perguntas]) / len(self.perguntas)
        return self.dificuldadeMedia

    def atualizarProgresso(self, perguntasRespondidas):
        if self.perguntas:
            self.percentualConclusao = (perguntasRespondidas / len(self.perguntas)) * 100
        return self.percentualConclusao

    def finalizar(self):
        self.status = "Concluído"
        return self

class BuilderSimulado:
    def __init__(self):
        self.simulado = Simulado()

    def setUsuario(self, usuario):
        self.simulado.usuario = usuario
        return self

    def setDataInicio(self, dataInicio):
        self.simulado.dataInicio = dataInicio
        return self

    def setPerguntas(self, perguntas):
        self.simulado.perguntas = perguntas
        return self

    def setTempoLimite(self, tempoLimite):
        self.simulado.tempoLimite = tempoLimite
        return self

    def setConfig(self, config):
        self.simulado.idSimulado = config.get("idSimulado", None)
        self.simulado.status = config.get("status", "Não iniciado")
        return self

    def criarSimulado(self):
        self.simulado.dataTermino = self.simulado.dataInicio + self.simulado.tempoLimite
        return self.simulado

if __name__ == "__main__":

    perguntas = [
        {"id": 1, "texto": "Pergunta 1", "dificuldade": 3, "pontuacao": 5},
        {"id": 2, "texto": "Pergunta 2", "dificuldade": 5, "pontuacao": 10},
        {"id": 3, "texto": "Pergunta 3", "dificuldade": 2, "pontuacao": 3},
    ]

    config = {
        "idSimulado": 101,
        "status": "Em andamento"
    }

    builder = BuilderSimulado()
    simulado = (
        builder.setUsuario("João Silva")
        .setDataInicio(datetime.now())
        .setPerguntas(perguntas)
        .setTempoLimite(timedelta(hours=1))
        .setConfig(config)
        .criarSimulado()
    )

    print(f"Simulado ID: {simulado.idSimulado}")
    print(f"Usuário: {simulado.usuario}")
    print(f"Data de Início: {simulado.dataInicio}")
    print(f"Data de Término: {simulado.dataTermino}")
    print(f"Perguntas: {len(simulado.perguntas)}")
    print(f"Status: {simulado.status}")
    print(f"Pontuação Total: {simulado.calcularPontuacao()}")
    print(f"Dificuldade Média: {simulado.calcularDificuldadeMedia()}")
    print(f"Progresso: {simulado.atualizarProgresso(2)}%")
    simulado.finalizar()
    print(f"Status Final: {simulado.status}")