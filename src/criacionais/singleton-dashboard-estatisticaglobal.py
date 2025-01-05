from datetime import datetime

class EstatisticasGlobais:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EstatisticasGlobais, cls).__new__(cls, *args, **kwargs)
            cls._instance.totalUsuarios = 0
            cls._instance.totalQuestoesRespondidas = 0
            cls._instance.taxaAcertosMedia = 0.0
            cls._instance.totalSimuladosRealizados = 0
            cls._instance.totalCategoriasCadastradas = 0
            cls._instance.dataUltimaAtualizacao = datetime.now()
        return cls._instance

    def atualizarEstatisticas(self):
        self.dataUltimaAtualizacao = datetime.now()
        print("Estatísticas atualizadas. Data/hora:", self.dataUltimaAtualizacao)

    def calcularTaxaAcertosMedia(self):
        if self.totalQuestoesRespondidas > 0:
            self.taxaAcertosMedia = (self.taxaAcertosMedia / self.totalQuestoesRespondidas) * 100
        return self.taxaAcertosMedia

    def registrarNovoUsuario(self):
        self.totalUsuarios += 1
        print(f"Novo usuário registrado. Total de usuários: {self.totalUsuarios}")

    def registrarNovaQuestaoRespondida(self, acerto: bool):
        self.totalQuestoesRespondidas += 1
        if acerto:
            self.taxaAcertosMedia += 1
        print(f"Questão respondida. Total de questões: {self.totalQuestoesRespondidas}")

    def registrarSimuladoRealizado(self):
        self.totalSimuladosRealizados += 1
        print(f"Simulado realizado. Total de simulados: {self.totalSimuladosRealizados}")


class Dashboard:
    def __init__(self, idDashboard: int, idUsuario: int):
        self.idDashboard = idDashboard
        self.idUsuario = idUsuario
        self.dadosProgresso = {}
        self.dadosDesempenho = {}
        self.estatisticas = EstatisticasGlobais()

    def atualizarDados(self):
        print(f"Atualizando dados do usuário {self.idUsuario}...")
        self.estatisticas.atualizarEstatisticas()

    def exibirGraficos(self):
        print("Exibindo gráficos de progresso e desempenho...")

    def configurarMetas(self):
        print("Configurando metas para o usuário...")

    def exibirResumoDiario(self):
        print("Exibindo resumo diário do usuário...")

if __name__ == "__main__":
    estatisticas = EstatisticasGlobais()

    # Criando Dashboards
    dashboard1 = Dashboard(1, 101)
    dashboard2 = Dashboard(2, 102)

    estatisticas.registrarNovoUsuario()
    estatisticas.registrarNovaQuestaoRespondida(True)
    estatisticas.registrarNovaQuestaoRespondida(False)
    estatisticas.registrarSimuladoRealizado()

    dashboard1.atualizarDados()
    dashboard2.atualizarDados()

    print("Taxa de acertos média:", estatisticas.calcularTaxaAcertosMedia(), "%")
    print("Data da última atualização:", estatisticas.dataUltimaAtualizacao)
