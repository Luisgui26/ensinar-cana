# Fundamentos e modelos de explicação

## Tempo, tamanho e notação
n é o tamanho da entrada, não segundos. T(n) conta operações segundo um modelo. Máquina e linguagem afetam constantes; a análise assintótica estuda crescimento para n grande.
O(g): existe c>0 e n0 tais que 0≤T(n)≤c g(n) para n≥n0.
Ω(g): existe c>0 e n0 tais que T(n)≥c g(n)≥0 para n≥n0.
Θ(g): existem c1,c2>0 e n0 tais que c1 g(n)≤T(n)≤c2 g(n).
Ex.: T(n)=3n+2. Para n≥1, 3n≤3n+2≤5n; logo Θ(n). Também O(n²), mas não Θ(n²).
Melhor/pior/médio são funções diferentes de n; qualquer uma pode receber limites O, Ω e Θ. O não significa automaticamente pior caso e Ω não significa melhor caso.
Crescimento usual: 1 < log n < n < n log n < n² < n³ < 2^n < n! (para n suficientemente grande). Base constante >1 do log só altera fator constante.

## Contar laços
- Laço com n execuções e corpo constante: Θ(n). Sob teste convencional há n+1 testes e n incrementos. Se houver retorno antecipado, recalcular caminho.
- Sequência de dois laços: somar custos; n+n²=Θ(n²).
- Dois laços completos de n cada, aninhados: n·n=Θ(n²).
- Externo n e interno 5: 5n=Θ(n).
- Interno de 0 até i-1: 0+1+...+(n-1)=n(n-1)/2=Θ(n²). Mostrar com n=4: 0+1+2+3=6.
- Dobrar i começando em 1: 1,2,4,8,...,2^k; terminar quando 2^k≥n, então k≈log₂n. Não presumir log para qualquer while.
- Laço externo em n e interno por duplicação: Θ(n log n).
- Alocar/copiar vetor de tamanho n não é operação constante no modelo usual de custo por elemento.

## Somatórios úteis
1+...+n=n(n+1)/2; 1+2+...+2^h=2^(h+1)-1; soma de q^i, i=0..h-1, é (q^h-1)/(q-1), q≠1. Para q=1, soma=h.
Explicar pela quantidade de termos antes de usar fórmula. Diferenciar h de h+1 níveis.

## Recorrências
T(n)=aT(n/b)+f(n): a chamadas, cada uma com tamanho n/b, trabalho local f(n). Caso base T(1)=Θ(1). Para reduzir arredondamentos, assumir n potência de b e explicar que isso não muda a ordem nos exemplos usuais.
Árvore: nível i tem a^i nós, tamanho n/b^i, custo do nível a^i f(n/b^i), altura log_b n, a^(log_b n)=n^(log_b a) folhas.
Se f(n)=cn^d, custo do nível=cn^d(a/b^d)^i. Razão=1 → níveis custam o mesmo; <1 → raiz domina; >1 → fundo domina. Contar folhas antes de concluir.
Exemplos: 2T(n/2)+n → Θ(n log n); T(n/2)+1 → Θ(log n); 4T(n/2)+n → Θ(n²); 2T(n/2)+n² → Θ(n²).
T(n)=T(n-1)+n: n+(n-1)+...+2+T(1)=Θ(n²), fora da forma padrão do Mestre.
T(n)=T(n-1)+1=Θ(n).
T(n)=2T(n-1)+1=Θ(2^n).

## Mestre
Exigir a≥1 constante, b>1 constante, f assintoticamente não negativa. Seja p=log_b a.
1. f(n)=O(n^(p-ε)) para ε>0: Θ(n^p).
2. f(n)=Θ(n^p): Θ(n^p log n). Extensão: Θ(n^p log^k n), k≥0, resulta Θ(n^p log^(k+1)n).
3. f(n)=Ω(n^(p+ε)), ε>0, e a f(n/b)≤c f(n), c<1 para n grande: Θ(f(n)).
Na versão com f(n)=Θ(n^d), comparar d e p; equivalência: a versus b^d. Não confundir coeficiente d de expoente com constante aditiva de outra equação.
Ex.: 2T(n/2)+n: a=2,b=2,p=1,f=Θ(n); caso 2, Θ(n log n).

## Memória e correção
Memória auxiliar é espaço além da entrada; informar se inclui saída e pilha. Recursão consome profundidade máxima simultânea, não total de chamadas. n folhas não significam automaticamente pilha de n posições.
Correção por invariante: mostrar validade antes do laço; que uma iteração a mantém; e que ao terminar ela implica objetivo. Término exige progresso e limite, além da invariante.
