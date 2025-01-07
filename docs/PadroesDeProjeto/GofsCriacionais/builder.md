# **GoF Criacional**

## **1. Introdução**

A crescente complexidade dos sistemas de software e a necessidade de criar soluções flexíveis e sustentáveis motivam o uso de padrões de projeto (patterns). Dentro do grupo de padrões criacionais descritos por Gamma, Helm, Johnson e Vlissides (1995), o Builder se destaca por separar a construção de objetos complexos de sua representação final, possibilitando a criação de diferentes versões de um mesmo objeto sem duplicar código. Segundo Fowler (2002), a adoção de padrões que promovem baixo acoplamento e alta coesão — como é o caso do Builder — contribui para aumentar a manutenibilidade e a evolução contínua das aplicações.

No contexto atual, em que projetos de software precisam atender rapidamente a mudanças de requisitos, o padrão Builder cumpre um papel fundamental. Ele permite encapsular etapas de criação de forma modular, reduzindo a proliferação de código repetitivo no cliente e, ao mesmo tempo, tornando o sistema mais adaptável a alterações. De acordo com Martin (2017), a clareza do código e a facilidade de expansão são características essenciais em arquiteturas limpas, características essas que são reforçadas pela aplicação de padrões criacionais, como o Builder. Além disso, referências como Refactoring.Guru (2025) destacam a versatilidade do padrão, pois ele permite isolar regras de construção em classes distintas, favorecendo o reuso de componentes e aumentando a robustez da solução final.

## **2. Metodologia**

Para a elaboração deste documento, adotou-se uma abordagem que combinou **revisão bibliográfica** e aplicação prática do padrão de projeto Builder. Em um primeiro momento, realizou-se uma pesquisa em fontes reconhecidas na área de Engenharia de Software, a fim de embasar teoricamente o tema e identificar boas práticas de implementação. Posteriormente, foi desenvolvida uma [modelagem UML](https://unbarqdsw2024-2.github.io/2024.2_G3_Aprender_Entrega_02/#/Modelagem/2.1.2.DiagramaClasses) que evidenciou as entidades envolvidas e seus relacionamentos, garantindo clareza no entendimento da lógica de construção.

Com base no material coletado, procedeu-se à implementação de um protótipo de código, estruturado para isolar as etapas de criação de objetos complexos, evitando acoplamento excessivo e favorecendo a manutenibilidade. Por fim, foi realizada uma análise crítica dos resultados obtidos, com foco em verificar a adequação do padrão às necessidades do projeto, bem como a clareza, escalabilidade e legibilidade do sistema resultante.

## **3. Modelagem e Contextualização do Builder no Sistema**

No contexto do nosso projeto, o uso do padrão de projeto Builder foi fundamental para simplificar a criação de objetos complexos compostos por diversas partes ou que exigem configurações específicas. Ao adotar o Builder, conseguimos reduzir a complexidade de construção, encapsulando a lógica em uma estrutura dedicada e evitando acoplamento excessivo no código principal, o que manteve a clareza em cada etapa da criação. Esse padrão também promoveu a reutilização e flexibilidade, permitindo que diferentes configurações do mesmo tipo de objeto fossem criadas de maneira eficiente, sem redundância. Além disso, facilitou a manutenção e expansão do sistema, pois a adição de novos atributos ou configurações ao objeto exigiu modificações apenas no Builder, sem afetar o código do cliente. A estrutura fluente do Builder também melhorou a legibilidade do código, tornando o processo de criação mais sequencial, intuitivo e alinhado com os objetivos do projeto. Dessa forma, o uso do padrão Builder não só lidou com a complexidade de maneira eficaz, mas também preparou o sistema para futuras mudanças, garantindo qualidade e escalabilidade à solução.

<center>
<div style="max-width:800px;">
<figure markdown>
<font size="3"><p style="text-align: center"><b>GoF Criacional Builder - </b>Imagem 1</p></font>

![Exemplo Model](../../assets/gof-criacional-builder.png)

<font size="3"><p style="text-align: center">Fonte: [Ana Carolina](https://github.com/CarolCoCe), [Felipe de Oliveira](https://github.com/M0tt1nh4), [Giovanni Giampauli](https://github.com/giovanniacg) e [João Artur](https://github.com/joao-artl)</p>
</font>
</figure>
</div>
</center>

## **4. Demonstração de Código e Exemplificação**

Abaixo está detalhado o código da implementação do padrão GoF Criacional **Builder**

[Veja o código na íntegra](https://github.com/UnBArqDsw2024-2/2024.2_G3_Aprender_Entrega_03/blob/main/src/criacionais/builder-simulado.py)

<center>
<div style="max-width:600px;">
<figure markdown>
<font size="3"><p style="text-align: center"><b>GoF Criacional -</b> Builder</p></font>

![Exemplo Model](../../assets/gof-criacional-builder-codigo.png)

<font size="3"><p style="text-align: center">Fonte: [Arthur Alves](https://github.com/Arthrok), [Diego Sousa](https://github.com/DiegoSousaLeite), [Julio Cesar](https://github.com/julio-dourado) e [Paulo Henrique](https://github.com/paulomh)</p>
</font>
</figure>
</div>
</center>

**Classe Simulado**

A classe Simulado representa o modelo principal do simulador, contendo os atributos e comportamentos necessários para gerenciar um simulado.

Atributos:

- idSimulado: Identificador único do simulado.
- usuario: Usuário que realizará o simulado.
- dataInicio: Data e hora de início do simulado.
- dataTermino: Data e hora de término do simulado.
- perguntas: Lista de perguntas incluídas no simulado.
- tempoLimite: Tempo máximo permitido para a realização do simulado.
- pontuacao: Pontuação total do simulado.
- status: Status atual do simulado (ex.: "Em andamento", "Concluído").
- dificuldadeMedia: Média de dificuldade das perguntas.
- percentualConclusao: Percentual de progresso no simulado com base nas perguntas respondidas.

Métodos:

- calcularPontuacao(): Soma os valores de pontuação das perguntas para calcular a pontuação total do simulado.
- calcularDificuldadeMedia(): Calcula a dificuldade média com base nos valores atribuídos a cada pergunta.
- atualizarProgresso(perguntasRespondidas): Atualiza o percentual de conclusão com base no número de perguntas respondidas.
- finalizar(): Altera o status do simulado para "Concluído".

Essa classe encapsula toda a lógica relacionada ao gerenciamento de um simulado.

**Classe BuilderSimulado**

A classe BuilderSimulado implementa o padrão Builder para facilitar a criação de objetos do tipo Simulado. Com ela, é possível configurar o simulado passo a passo e garantir que ele seja construído corretamente.
Atributos:

- simulado: Instância da classe Simulado que será configurada e retornada.

Métodos:

- setUsuario(usuario): Define o usuário que realizará o simulado.
-setDataInicio(dataInicio): Define a data e hora de início.
- setPerguntas(perguntas): Adiciona uma lista de perguntas ao simulado.
- setTempoLimite(tempoLimite): Define o tempo limite para o simulado.
- setConfig(config): Configurações adicionais (ex.: idSimulado e status).
- criarSimulado(): Finaliza a configuração e retorna o objeto Simulado.

Essa classe promove um fluxo fluente (métodos encadeáveis), facilitando a leitura e a construção de objetos complexos.


**Saída**

<center>
<div style="max-width:600px;">
<figure markdown>
<font size="3"><p style="text-align: center"><b>GoF Criacional -</b> Builder</p></font>

![Saída](../../assets/gof-criacional-builder-exemplo.png)

<font size="3"><p style="text-align: center">Fonte: [Danilo Naves](https://github.com/DaniloNavesS)</p>
</font>
</figure>
</div>
</center>

## **5. Análise e Conclusão**

O uso do padrão de projeto Builder no BuilderSimulador provou ser uma decisão estratégica e altamente eficaz para lidar com a complexidade inerente ao sistema. Durante o desenvolvimento, nos deparamos com a necessidade de criar objetos compostos por várias partes interdependentes e que poderiam variar conforme diferentes cenários de simulação. O padrão Builder permitiu que abordássemos esses desafios de forma organizada, flexível e extensível.

## **Referências Bibliográficas**

- REFACTORING.GURU. Builder design pattern. Disponível em: https://refactoring.guru/design-patterns/builder. Acesso em: 5 jan. 2025.
- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1995). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
- Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley.
- Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.
- Código Builder, Squad 1. Disponível em: [Código](https://github.com/UnBArqDsw2024-2/2024.2_G3_Aprender_Entrega_03/blob/main/src/criacionais/builder-simulado.py)

## **Histórico de Versão**

| Versão | Data       | Data de Revisão | Descrição do Documento                         | Autor(es)                                                | Revisor(es)                                       | Detalhes da revisão                                                                                         |
|-------|------------|-----------------|-------------------------------------------------|----------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `1.0`   | 04/01/2025 | 05/01/2025      | Criação do diagrama UML.                        | [Ana Carolina](https://github.com/CarolCoCe), [Felipe de Oliveira](https://github.com/M0tt1nh4), [Giovanni Giampauli](https://github.com/giovanniacg), [João Artur](https://github.com/joao-artl) | [Danilo Naves](https://github.com/DaniloNavesS) | [#7](https://github.com/UnBArqDsw2024-2/2024.2_G3_Aprender_Entrega_03/pull/7)|
| `1.1`   | 04/01/2025 | 05/01/2025      | Implementação do código de demonstração.           | [Arthur Alves](https://github.com/Arthrok), [Diego Sousa](https://github.com/DiegoSousaLeite), [Julio Cesar](https://github.com/julio-dourado), [Paulo Henrique](https://github.com/paulomh) | [Danilo Naves](https://github.com/DaniloNavesS)  | [#7](https://github.com/UnBArqDsw2024-2/2024.2_G3_Aprender_Entrega_03/pull/7)|
| `1.2`   | 05/01/2025 | 05/01/2025      | Documentação do padrão Builder.                | [Danilo Naves](https://github.com/DaniloNavesS)              |[Gustavo Melo](https://github.com/gusrberto) | [#7](https://github.com/UnBArqDsw2024-2/2024.2_G3_Aprender_Entrega_03/pull/7)|
| `1.3`   | 05/01/2025 | - | Refinamento da introdução e metodologia | [Giovanni Giampauli](https://github.com/giovanniacg) | - | - |