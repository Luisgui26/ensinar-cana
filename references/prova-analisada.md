# AV1: estrutura, resolução e cuidados

**Referência histórica:** a orientação atual do professor, relatada em 20/10/2026, exige ordenações nas duas questões de cálculo e exclui buscas da primeira questão. Não transportar a busca linear da Q2 desta AV1 para os simulados da próxima prova.

## Ordem das páginas
O arquivo tem 3 páginas fora da ordem impressa. Página física 3 = primeira página impressa; física 2 = segunda; física 1 = terceira. Não usar a sequência física como sequência das questões. As marcas manuscritas são do exemplar do aluno e não são gabarito oficial.

## Estrutura observada
100 minutos; 7 pontos mais 0,5 extra. Três questões principais. Desenvolvimento obrigatório: a prova informa que só o resultado não basta.
- Q1: 10 itens V/F com justificativa breve. 2 pontos; cada item vale 0,1 pela marcação e 0,1 pela justificativa.
- Q2: busca linear em carrinho de compras, primeiro item indisponível ou -1. 2 pontos: função de tempo (1) e simplificação com Θ justificada (1).
- Q3: duas chamadas de tamanho n/2 e um laço linear. 3 pontos: separar parte iterativa e recursiva e escrever recorrência (1); resolver por árvore, mostrando níveis e soma e justificar notação (2).
- Extra: reconhecer quicksort e avaliar memória, estabilidade, comparações médias e escolha do pivô. 0,5.

Isto demonstra formato e exigência da AV1. Não demonstra o conteúdo ou peso de uma futura AV2. Para a Unidade II, usar a lista como evidência de escopo.

## Q1: solução própria, com precisão
(a) V: O(n²) é limite superior e permite uma função que também seja O(n). Ex.: 3n+2 pertence a O(n²).
(b) Ambígua na redação: Ω(n) é limite inferior assintótico por uma constante positiva, e não necessariamente tempo literal ≥ n. Além disso, uma cota para o pior caso não implica cota para todas as entradas. Sob leitura informal de limite linear válido para todas as entradas, é a ideia de V; sob leitura literal ou sem função de caso, há imprecisão. Não impor V ou F sem explicar o problema.
(c) V: Θ(n log n) exige limites superior e inferior da mesma ordem, com constantes positivas. A marcação F no exemplar não é fundamento matemático.
(d) V: trechos sequenciais O(n) e O(n²) têm soma O(n²); isso não permite concluir Θ(n²) se só sabemos limites superiores.
(e) F: esgotar pilha é falha de execução, não caso base nem resultado válido; garantir término exige condição atingível e progresso.
(f) F: código iterativo pode alocar vetor auxiliar de n posições, consumindo Θ(n).
(g) F: recursão não implica assintoticamente mais tempo. Busca binária iterativa e recursiva têm pior tempo Θ(log n).
(h) F: no caso 1 do Mestre, se f(n) é polinomialmente menor que n^(log_b a), o resultado é Θ(n^(log_b a)).
(i) V sob as hipóteses completas: caso 3 requer diferença polinomial e regularidade a f(n/b) ≤ c f(n), com c<1, para n grande. Apenas “crescer mais rápido” não basta em geral.
(j) Cuidado: a intenção aparente é F, pois n repetições externas vezes constante interna dão Θ(n). Mas o texto usa O(n²): uma função Θ(n) também pertence a O(n²). Sob leitura formal, O(n²) é uma cota válida, embora frouxa. Ensinar essa diferença; ao gerar simulados, usar Θ para perguntar a ordem exata.

## Q2: contagem da busca linear
Pseudocódigo: para i=0 até n-1, testar disponibilidade; retornar i se indisponível; após o laço retornar -1. Assumir consulta à disponibilidade O(1), pois o enunciado não fornece uma operação remota de custo variável.

Definir modelo: cobrar c1 por teste do laço, c2 pelo teste de disponibilidade, c3 pelo retorno i e c4 pelo retorno -1; inicialização e incremento podem ser incluídos em c1 apenas como aproximação afim ou contados separadamente. Para expressão exata, preferir:
- inicialização: 1;
- teste do laço: n+1 se nenhum indisponível, n se retorno ocorre no último elemento;
- incremento: n se nenhum indisponível, n-1 se retorna no último;
- disponibilidade: n nos dois;
- retorno i: 0 ou 1;
- retorno -1: 1 ou 0.

Com custos c_init,c_test,c_inc,c_disp,c_ret_i,c_ret_fim:
T_ausente(n)=c_init+(n+1)c_test+n c_inc+n c_disp+c_ret_fim.
T_ultimo(n)=c_init+n c_test+(n-1)c_inc+n c_disp+c_ret_i.
Ambas são an+b, logo Θ(n) para custos constantes positivos e n≥1. Não executar mentalmente os dois retornos no mesmo caminho. Melhor caso: primeiro item indisponível, Θ(1).

## Q3: resolução em passos
Código: se n≤1 retornar 1; contador=0; repetir contador++ n vezes; retornar analise(A,n/2)+analise(A,n/2)+contador.

Mesmo subproblema repetido é computado duas vezes pelo código; não há memoização. Valor devolvido não é a função de tempo.
T(1)=d>0; T(n)=2T(n/2)+cn+d0, n>1, usando n potência de 2 para simplificar.
Para derivar soma simples, substituir parte não recursiva por cn, conservando a ordem.
No nível i: 2^i nós; tamanho n/2^i; custo por nó cn/2^i; custo total cn.
Profundidade h: n/2^h=1 → 2^h=n → h=log₂n.
Há h níveis internos, de 0 a h-1, e um nível de folhas. Folhas: 2^h=n, custo dn.
T(n)=cn log₂n+dn=Θ(n log n). Com d0 por nó interno, somar d0(n-1), sem alterar Θ.
Resposta de prova: “A parte local é linear. Há duas chamadas de metade do tamanho, portanto T(n)=2T(n/2)+Θ(n). Cada nível interno custa Θ(n), existem log₂n níveis internos e as folhas somam Θ(n). Logo T(n)=Θ(n log n).” Expandir os passos da árvore quando solicitado na prova.

## Extra
O algoritmo é quicksort com pivô no fim, partição semelhante à de Lomuto e comparador estrito.
A: O(n) de pilha é limite de pior caso da versão recursiva simples; média/partições equilibradas usam Θ(log n). Sem qualificar caso, a afirmação é vaga, mas a cota superior O(n) é válida.
B: F. Recursivo, porém não estável em geral.
C: V sob o modelo usual de permutações aleatórias de chaves distintas ou pivô aleatório, com Θ(n log n) comparações esperadas. Não prometer essa média sem hipótese probabilística.
D: F. Primeiro pivô não é universalmente melhor que último; depende dos dados.
Combinação pretendida e matematicamente defensável sob as hipóteses acima: A e C. A opção manuscrita A,B,C não é gabarito confiável.
O limite j até hi com teste A[j]<pivô não move o pivô durante a passagem; na forma usual usa-se hi-1. Não mudar silenciosamente o código original ao transcrevê-lo.
