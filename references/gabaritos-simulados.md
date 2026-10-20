# Gabaritos dos simulados atualizados — soluções próprias

## Modelo A
Q1: V,F,V,V,V,F,V,F,V,V. Justificativas, respectivamente: seleção percorre todo resto; bubble sem bandeira continua quadrático; inserção não atravessa iguais; merge percorre duas sequências uma vez; partições extremas encadeiam; partição só separa; construção por alturas é linear; custo depende de k; definição de estabilidade; com blocos de tamanho √n, jump search faz até cerca de √n saltos e depois até √n inspeções lineares, então O(√n).

Q2a: Definir S=n(n-1)/2, L=n-1 e U atualizações da variável menor. Tratar `troque` como operação constante mesmo se índices iguais. Tabela:
- inicialização externa:1;
- teste externo:n;
- incremento externo:L;
- menor=i:L;
- inicialização interna:L;
- teste interno:S+L;
- incremento interno:S;
- comparação de chaves:S;
- menor=j:U;
- troca:L.
S=Σ(i=0..n-2)(n-1-i)=(n-1)+(n-2)+...+1=n(n-1)/2.
Com custos c0..c9 positivos fixos, T(n)=c0+c1n+c2L+c3L+c4L+c5(S+L)+c6S+c7S+c8U+c9L. Retorno implícito pode adicionar constante. Inicialização/incremento são cobrados como operações inteiras do pseudocódigo; não exigir o mesmo coeficiente de outro modelo.
Q2b: 0≤U≤S e comparações sempre S, logo Θ(n²) nos três casos. Passagens [6,2,5,1] → [1,2,5,6] → [1,2,5,6] → [1,2,5,6]. Contagem de comparações:3+2+1=6. Código executa3 trocas, das quais2 são autotrocas.

Q3a: mergesort. T(1)=β constante; T(n)=2T(n/2)+cn+d, n>1. Custo local linear do merge e controle constante.
Q3b: nível i possui2^i nós, cada um tamanho n/2^i, custo local principal cn/2^i, total cn. Altura h de n/2^h=1: log₂n. Níveis internos0..h-1, folhas n com custo β. T(n)=cn log₂n+d(n-1)+βn=Θ(n log n). Buffer pico Θ(n), pilha Θ(log n), total Θ(n), não produto n log n. Extra A. III é falso porque heap usual é instável. IV inverte empates: para [(2,A),(2,C)], A fica na última vaga e C na anterior.

## Modelo B
Q1: V,F,V,V,V,F,F,F,V,V. Inserção ordenada tem testes lineares sem deslocamentos; seleção pode inverter registros iguais numa troca; bandeira detecta ordenação; heap é completo com pai≥filhos; índices usuais de0; merge requer buffer linear; aleatório dá expectativa, mantém pior possível; counting usa índices e frequências; pivô máximo particiona n-1 e0; jump search faz cerca de √n saltos e examina no máximo um bloco de tamanho √n, então O(√n) no pior caso.

Q2a: zerar C custa Θ(k+1); contar Θ(n); prefixar Θ(k); preparar B Θ(n) no modelo declarado; construir saída Θ(n); copiar Θ(n). Uma função por fases é T(n,k)=a(k+1)+bn+ck+dn+en+fn+g, constantes positivas a..f e g constante de controle, absorvendo custos afins de testes/retornos. Isso dá Θ(n+k) para n≥1,k≥0, porque n+k≥1; não omitir todas as fases de tamanho n. Não é contagem exata independente de modelo: coeficientes dependem das operações cobradas. Espaço Θ(n+k+1), equivalente a Θ(n+k) sob n≥1.
Q2b: k=2. Frequências C=[1,1,2]; prefixos[1,2,4]. Processar de trás: (1,D) posição1; (2,C) posição3; (0,B) posição0; (2,A) posição2. Saída[(0,B),(1,D),(2,A),(2,C)]. Contagens finais[0,1,2]. Empates preservam A antes de C, porque o último registro original recebe última vaga da sua chave. Buffer n e contador k+1 explicam espaço.

Q3a: pivô é máximo e fica no fim; esquerda tamanho n-1, direita0. Comparações de chaves por partição n-1. T(0)=T(1)=Θ(1). T(n)=T(n-1)+T(0)+an+b, n≥2, ou T(n)=T(n-1)+an+b' após absorver chamada vazia. `i` avança em todas as n-1 comparações e as trocas internas são autotrocas; elas têm custo constante na rotina apresentada.
Q3b: custos locais de tamanhos n,n-1,...,2. Altura do ramo maior n-1 arestas até tamanho1; há também chamadas vazias, que somam apenas Θ(n). Com T(1)=β e termo local an+b': T(n)=β+a[Σ(m=2..n)m]+b'(n-1)=β+a[n(n+1)/2-1]+b'(n-1)=Θ(n²). Comparações de chaves, separadamente: (n-1)+(n-2)+...+1=n(n-1)/2. Pilha máxima Θ(n), mesmo sendo partição in place. Mestre padrão não se aplica a n-1. Extra C: I,II,III verdadeiros; IV falso.

## Correção
Pesos são proposta de treino, herdada da AV1. Valorizar desenvolvimento conforme enunciado: Q1 0,1 marcação/0,1 justificativa; Q2 1 ponto por item; Q3 1 e2 pontos. Não atribuir gabarito oficial. Aceitar modelos de custo consistentes que produzam contagens coerentes e justificativas corretas. Quando pedido número exato de comparações de chaves, não substituir pela contagem total de instruções.
