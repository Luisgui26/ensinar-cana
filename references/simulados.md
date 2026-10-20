# Simulados da próxima prova — escopo atualizado em 20/10/2026

## Índice
- Regras atuais
- Modelo A: seleção e mergesort
- Modelo B: counting e quicksort
- Variações para novas provas

## Regras atuais
Segundo informação do aluno sobre orientação do professor, atualizada com esclarecimento posterior: Q1 pode abordar algoritmos estudados ou novos, inclusive algoritmo de busca diferente de linear/binária, desde que o nível seja parecido. Busca linear e binária são excluídas da Q1. Q2 e Q3 cobram custo de ordenações, que podem ser estudadas ou novas de nível/estrutura semelhante. Os modelos abaixo ilustram esses limites, mas não preveem quais algoritmos específicos serão escolhidos. Cada Q1 pode incluir uma busca diferente de linear/binária, como jump search, para treinar leitura de algoritmo novo.
Usar 100 minutos, 7 pontos +0,5 extra como convenção de treino herdada da AV1, não como confirmação da próxima prova. Q1 vale2; Q2 vale2; Q3 vale3. Exigir desenvolvimento. Gabaritos em `gabaritos-simulados.md`, sem revelar em modo prova.

## Modelo A — seleção e mergesort

### Questão 1 — 2 pontos
Marcar V/F e justificar cada item. 0,1 por marcação +0,1 pela justificativa.
a) Seleção iterativa usual realiza Θ(n²) comparações de chaves mesmo com vetor ordenado.
b) Bubble sem bandeira de parada tem melhor tempo Θ(n).
c) Inserção com deslocamento apenas de chaves estritamente maiores é estável.
d) Merge pode intercalar duas sequências ordenadas em tempo linear no total de elementos.
e) Quicksort com pivô sempre extremo pode levar a Θ(n²).
f) A partição do quicksort ordena completamente os dois lados do pivô.
g) Construção bottom-up do heap custa Θ(n), apesar de uma descida individual ter pior Θ(log n).
h) Counting com n registros e faixa de k chaves custa Θ(n), para qualquer k.
i) Uma ordenação estável preserva a ordem original dos registros com a mesma chave.
j) Jump search em vetor ordenado, com blocos de tamanho aproximado √n, pode localizar uma chave em O(√n) comparações no pior caso.

### Questão 2 — 2 pontos
Um sistema ordena pedidos por valor com a rotina abaixo. n≥2, vetor indexado de0 a n-1.
```
selecao(v,n):
  para i=0 até n-2:
    menor=i
    para j=i+1 até n-1:
      se v[j]<v[menor]:
        menor=j
    troque v[i],v[menor]
```
a) (1 ponto) Monte tabela custo×vezes. Separe inicializações, testes e incrementos dos laços, comparação de chaves, atualização de menor e troca (que aqui é executada mesmo se for autotroca). Represente o número total de atualizações de menor por U, escreva T(n) com custos constantes positivos e derive a quantidade exata de comparações de chaves por somatório.
b) (1 ponto) Simplifique para Θ, justifique melhor/médio/pior e simule as passagens em [6,2,5,1]. Não confunda comparação de chaves com custo total.

### Questão 3 — 3 pontos
Um relatório é ordenado pelo código abaixo. Considere n potência de2, índices inclusivos e `intercalar` com tempo Θ(m) e buffer Θ(m) para trecho de m elementos.
```
ordenar(v,ini,fim):
  se ini>=fim: retorne
  meio=piso((ini+fim)/2)
  ordenar(v,ini,meio)
  ordenar(v,meio+1,fim)
  intercalar(v,ini,meio,fim)
```
a) (1 ponto) Identifique a ordenação, separe custo local/chamadas e escreva recorrência com base.
b) (2 pontos) Resolva por árvore: nós no nível i, tamanho/custo por nó, custo do nível, profundidade, folhas, soma e Θ. Informe espaço auxiliar incluindo pilha.

### Extra — 0,5 ponto
Notas inteiras0..100 de alunos já alfabeticamente ordenados; manter empates na ordem original. I counting estável é adequado; II custo Θ(n+101); III heap usual garante estabilidade; IV preencher posições finais acumuladas da esquerda para direita, decrementando contagens, garante estabilidade. Opções: A) I e II; B) I e III; C) II e IV; D) III e IV; E) todas.

## Modelo B — counting e quicksort

### Questão 1 — 2 pontos
Marcar V/F com justificativas, 0,2 cada.
a) Insertion em vetor ordenado faz zero deslocamentos de elementos anteriores e tem tempo Θ(n).
b) Seleção usual é estável porque sempre posiciona o menor valor restante.
c) Bubble com bandeira encerra após uma passagem sem trocas.
d) Max-heap exige que todo nó seja maior ou igual aos descendentes imediatos, além de representar uma árvore binária completa.
e) No heap indexado de0, filhos de i têm índices2i+1 e2i+2, quando existentes.
f) Mergesort usual em vetor usa apenas Θ(log n) de espaço auxiliar total, incluindo buffers.
g) Escolher pivô aleatório remove a possibilidade de pior caso quadrático do quicksort.
h) Counting sempre compara os registros dois a dois para determinar a ordenação.
i) Com partição Lomuto e pivô último, vetor ordenado com chaves distintas pode gerar partições0 e n-1 repetidamente.
j) Uma ordenação por comparação precisa de Ω(n log n) comparações no pior caso para ordenar n chaves distintas arbitrárias.

### Questão 2 — 2 pontos
Ordenação estável de n≥1 registros com chave inteira entre0 e k, k≥0:
```
counting(v,n,k):
  C=vetor de k+1 posições, todo zerado
  para i=0 até n-1: C[v[i].chave]++
  para j=1 até k: C[j]=C[j]+C[j-1]
  B=vetor de n posições
  para i=n-1 até0, decrescendo:
    x=v[i].chave
    B[C[x]-1]=v[i]
    C[x]--
  copie B para v
```
a) (1 ponto) Conte o custo das fases, incluindo inicialização de C e alocação/inicialização de B sob o modelo usual de custo por posição. Escreva a função de custo com constantes positivas e conclua Θ em função de n,k. Não crie recorrência para este código iterativo.
b) (1 ponto) Simule frequências, prefixos e vetor final para [(2,A),(0,B),(2,C),(1,D)]. Explique estabilidade e espaço auxiliar.

### Questão 3 — 3 pontos
Um sistema ordena códigos com quicksort, particionamento Lomuto:
```
particionar(v,ini,fim):
  pivo=v[fim]
  i=ini
  para j=ini até fim-1:
    se v[j]<pivo:
      troque v[i],v[j]
      i++
  troque v[i],v[fim]
  retorne i

quick(v,ini,fim):
  se ini<fim:
    p=particionar(v,ini,fim)
    quick(v,ini,p-1)
    quick(v,p+1,fim)
```
Considere chaves distintas inicialmente em ordem crescente e pivô sempre no fim.
a) (1 ponto) Determine tamanhos das partições, comparações de chaves de uma partição de tamanho n e recorrência completa do tempo com caso base.
b) (2 pontos) Resolva a recorrência por expansão ou árvore, mostrando custos sucessivos, profundidade, soma, Θ de tempo e espaço máximo da pilha. Informe também o número total de comparações de chaves. Não aplicar Mestre padrão à redução por1.

### Extra — 0,5 ponto
Em quicksort com partições balanceadas e chaves distintas: I a profundidade é Θ(log n); II trabalho total por nível interno é O(n); III tempo é Θ(n log n); IV a rotina usual é estável. Corretas: A) I e IV; B) II e IV; C) I,II,III; D) apenas III; E) todas.

## Variações para novas provas
Alternar entre seleção, bubble, inserção, merge, quick, heap e counting. Q2/Q3 sempre calculam custo de ordenação real, podendo ser ambas iterativas ou recursivas se apropriado. Rotacionar pares para não ensinar que só seleção+merge cairão. Incluir casos, memória, estabilidade e simulações. Não incluir busca linear/binária na Q1; pode incluir busca nova de dificuldade comparável, como jump search. Q2/Q3 não são buscas: calcular o custo de algoritmos de ordenação, que podem ser novos mas de nível semelhante. Radix/bucket são complementos dos slides: aprofundar apenas conforme matéria e pedido. Nas recursivas, exigir recorrência/base/árvore quando adequado; no counting, somar fases; em heap, distinguir construção, descida e extrações. Não copiar algoritmo recursivo genérico da AV1 fingindo que ordena. Corrigir sem entregar resposta em modo prova.
