# 1I-PSI-M3-14687-EXPA01
<h1>Descrição do Código - Jogo de Adivinhação</h1>
    <p>Este código implementa um simples jogo de adivinhação em Python, onde o jogador deve tentar adivinhar um número aleatório gerado pelo computador entre 1 e 20. O jogador tem um total de 6 tentativas para acertar o número.</p>
<h2>Como Funciona</h2>
    <ol>
        <li>O programa importa a biblioteca <code>random</code> para gerar números aleatórios.</li>
        <li>Uma função chamada <code>scoreboard</code> é definida para exibir a pontuação, mas contém um erro na lógica de incremento.</li>
        <li>A função <code>main</code> é onde a lógica principal do jogo acontece:</li>
        <ul>
            <li>Um número aleatório é gerado entre 1 e 20.</li>
            <li>O jogador é solicitado a escolher um número e tem 6 tentativas para adivinhar corretamente.</li>
            <li>Após cada tentativa, o programa informa se o número escolhido é maior ou menor que o número aleatório.</li>
            <li>Se o jogador acertar, uma mensagem de sucesso é exibida e a função <code>scoreboard</code> é chamada.</li>
            <li>Se as tentativas se esgotarem, o programa informa o número correto e termina.</li>
        </ul>
