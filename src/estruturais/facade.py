from datetime import datetime, timedelta
from typing import List


class ConfigSimulado:
    def __init__(self, tempo_limite: int, dificuldade: int):
        self.tempo_limite = tempo_limite
        self.dificuldade = dificuldade


class Questao:
    def __init__(self, idQuestao: int, texto: str):
        self.idQuestao = idQuestao
        self.texto = texto
        self.alternativas: List[str] = []
        self.respostaCorreta: str = ""
        self.resolucao: str = ""
        self.tags: List[str] = []
        self.dificuldade: int = 0
        self.taxaAcertos: float = 0.0

    def validarResposta(self, resposta: str) -> bool:
        if resposta == self.respostaCorreta:
            return True
        else:
            return False

    def exibirResolucao(self):
        return f"Resolução: {self.resolucao}" if self.resolucao else "Nenhuma resolução disponível."

    def adicionarComentario(self, comentario: str):
        self.tags.append(comentario)
        return f"Comentário adicionado: {comentario}"


class Simulado:
    def __init__(self, idSimulado: int, idUsuario: int):
        self.idSimulado = idSimulado
        self.idUsuario = idUsuario
        self.dataInicio: datetime = None
        self.dataTermino: datetime = None
        self.perguntas: List[Questao] = []
        self.pontuacao: int = 0
        self.tempoLimite: timedelta = timedelta()
        self.status: str = "Não iniciado"

    def configurarSimulado(self, config: ConfigSimulado):
        self.tempoLimite = timedelta(minutes=config.tempo_limite)
        self.status = "Configurado"

    def iniciar(self):
        if not self.perguntas:
            raise ValueError(
                "Não é possível iniciar um simulado sem perguntas.")
        self.dataInicio = datetime.now()
        self.status = "Em andamento"

    def finalizar(self):
        self.dataTermino = datetime.now()
        self.status = "Finalizado"

    def calcularPontuacao(self, respostas: List[str]):
        self.pontuacao = 0
        for pergunta, resposta in zip(self.perguntas, respostas):
            if pergunta.validarResposta(resposta):
                self.pontuacao += 1
        print(f"Pontuação do simulado {self.idSimulado}: {self.pontuacao}")
        return self.pontuacao


    def exibirResolucoes(self):
        return [questao.exibirResolucao() for questao in self.perguntas]


class Usuario:
    def __init__(self, idUsuario: int, nome: str, email: str, senha: str):
        self.idUsuario = idUsuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfilPublico: bool = False
        self.fotoPerfil: str = ""
        self.bio: str = ""
        self.experiencia: int = 0
        self.nivel: int = 1

    def registrarAcesso(self):
        return f"Acesso do usuário {self.nome} registrado em {datetime.now()}."

    def calcularExperiencia(self, pontos: int):
        self.experiencia += pontos
        if self.experiencia >= 100:
            self.nivel += self.experiencia // 100
            self.experiencia = self.experiencia % 100
        return f"Nível: {self.nivel}, Experiência: {self.experiencia}"

class SistemaEducacionalFacade:
    def __init__(self, usuario: Usuario, simulado: Simulado):
        self.usuario = usuario
        self.simulado = simulado

    def exibirInfoUsuario(self, idUsuario: int):
        if idUsuario == self.usuario.idUsuario:
            return f'''
Nome: {self.usuario.nome},
Email: {self.usuario.email}
Nível: {self.usuario.nivel}, Experiência: {self.usuario.experiencia}
'''

    def iniciarSimulado(self):
        # Iniciando e finalizando o simulado
        self.simulado.iniciar()
        respostas_usuario = ["Brasília", "4", "Verde"]  # Uma resposta incorreta
        self.simulado.calcularPontuacao(respostas_usuario)
        self.simulado.finalizar()


# Criando questões
questao1 = Questao(1, "Qual a capital do Brasil?")
questao1.respostaCorreta = "Brasília"

questao2 = Questao(2, "Quanto é 2 + 2?")
questao2.respostaCorreta = "4"

questao3 = Questao(3, "Qual a cor do céu durante o dia?")
questao3.respostaCorreta = "Azul"

# Criando simulado e configurando
simulado = Simulado(1, 123)
simulado.perguntas.extend([questao1, questao2, questao3])
simulado.configurarSimulado(ConfigSimulado(30, 2))

# Criando usuário
usuario = Usuario(1, "Alice", "alice@example.com", "senha123")
print(usuario.registrarAcesso())
print(usuario.calcularExperiencia(120))

sistema = SistemaEducacionalFacade(usuario, simulado)
print(sistema.exibirInfoUsuario(1))
sistema.iniciarSimulado()

print(usuario.calcularExperiencia(80))