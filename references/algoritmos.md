# Buscas e ordenações

## Busca
Linear: testar uma posição por vez; não exige ordenação. Melhor Θ(1), pior Θ(n); sucesso uniforme dá (1+...+n)/n=(n+1)/2, Θ(n). Ausência: n testes.
Binária em vetor ordenado: comparar com meio e descartar metade. Invariante: se chave existe, está no intervalo ainda considerado. Melhor Θ(1), pior Θ(log n); iterativa Θ(1) auxiliar, recursiva Θ(log n). Usar meio=esq+(dir-esq)//2.
Contar “comparações” definindo unidade: uma inspeção do meio pode envolver teste de igualdade e outro de ordem. Pior número de inspeções com implementação usual e n≥1: floor(log₂n)+1. Em n=1024, até 11, não necessariamente 10; 10 é o número de divisões para chegar de 1024 a 1. Para n=8 buscando extremo adequado, meios podem ter tamanhos 8,4,2,1.

## Tabela das versões usuais
|Algoritmo|Melhor|Médio|Pior|Auxiliar|Estável?|
|---|---|---|---|---|---|
|Seleção|Θ(n²)|Θ(n²)|Θ(n²)|Θ(1) iterativo; Θ(n) recursivo simples|Não|
|Bubble com bandeira|Θ(n)|Θ(n²)|Θ(n²)|Θ(1) iterativo; até Θ(n) recursivo|Sim, troca só se >|
|Inserção|Θ(n)|Θ(n²)|Θ(n²)|Θ(1) iterativo; Θ(n) recursivo|Sim, desloca só se >|
|Merge em vetor|Θ(n log n)|Θ(n log n)|Θ(n log n)|Θ(n), pilha Θ(log n) absorvida|Sim, escolher esquerda no empate|
|Heap iterativo|Depende de repetição/implementação|Θ(n log n) usual|Θ(n log n)|Θ(1)|Não|
|Quick, partição usual|Θ(n log n)|Θ(n log n) esperado sob hipóteses|Θ(n²)|Pilha Θ(log n) equilibrada/esperada; Θ(n) pior|Não|
|Counting estável|Θ(n+k)|Θ(n+k)|Θ(n+k)|Θ(n+k)|Sim na construção estável|

Para heapsort em chaves distintas, a tabela didática usual dá Θ(n log n) nos três casos. Com todas as chaves iguais e sift-down que para imediatamente quando pai≥filhos, pode ocorrer Θ(n). Especificar a variante e as hipóteses; não universalizar tabela. Counting: k é tamanho da faixa de chaves, max-min+1; algumas fontes usam máximo de chaves não negativas e vetor k+1.

## Execução e justificativas
Seleção: achar mínimo do trecho restante e trocar com começo. [7,3,9,1] → [1,3,9,7] → [1,3,9,7] → [1,3,7,9]. Comparações (n-1)+...+1=n(n-1)/2 independentemente da ordem. Implementação que troca sempre faz n-1 chamadas de troca; sem autotroca, até n-1 trocas efetivas, não necessariamente n-1.
Bubble crescente: comparar vizinhos, trocar se esquerdo>direito. Passagem esquerda→direita leva maior ao fim; direita→esquerda leva menor ao início. Nunca afirmar qual sem conferir sentido. Bandeira permite terminar após passagem sem trocas.
Inserção: como organizar cartas na mão. Manter prefixo ordenado, guardar chave e deslocar maiores. [4,2,8,1] → [2,4,8,1] → [2,4,8,1] → [1,2,4,8]. Inversões explicam deslocamentos: Θ(n+I).
Merge: dividir até unidades, ordenar metades, intercalar duas sequências ordenadas com dois índices. Merge é Θ(n); T=2T(n/2)+Θ(n). Padrão aloca buffer de n. Inserir à esquerda antes da direita no empate preserva estabilidade.
Heap: árvore binária completa com pai≥filhos no max-heap; vetor indexado de 0, filhos 2i+1,2i+2, pai floor((i-1)/2) para i>0. Construir bottom-up dos índices floor(n/2)-1 até 0; trocar raiz com último ativo e recompor heap reduzido. Sift-down (heapify local) pior Θ(log n), melhor Θ(1). Construir não custa Θ(n log n): maioria dos nós está perto das folhas. Limite n Σ(h/2^(h+1))=O(n); percorrer Θ(n) posições dá Θ(n).
Quick: escolher pivô, particionar, ordenar lados. Lomuto: pivô=último, i=início, j de início até fim-1, se v[j]<pivô trocar v[i],v[j] e i++; ao fim trocar v[i],v[fim]; pivô termina em i. [4,1,5,2], pivô2 → [1,2,5,4]. Recorrência T(n)=T(q)+T(n-q-1)+Θ(n). Equilíbrio dá Θ(n log n); q=0 ou n-1 repetido dá Θ(n²). Aleatorização produz esperança, não elimina pior caso. Todos iguais degeneram em Lomuto simples; partição em três vias resolve em Θ(n) nesse caso. Hoare pode se comportar diferente.
Counting estável: contar frequências, prefixar somas, alocar saída, percorrer entrada do fim para começo, escrever em C[chave]-1 e decrementar C. Ex.: [(2,A),(1,B),(2,C)] deve virar [(1,B),(2,A),(2,C)]. Percurso para frente usando posições finais e decremento inverteria empates; percurso para frente pode ser estável com posições iniciais e incremento. Não dizer que qualquer counting exige direita→esquerda.

## Propriedades e escolhas
Estabilidade preserva ordem relativa de registros de mesma chave; não é apenas ordenar valores iguais. In place normalmente permite O(1) auxiliar; quicksort é frequentemente chamado in place para a partição, mas sua pilha deve ser informada. Versões recursivas de seleção/bubble/inserção podem usar Θ(n) de pilha.
Por comparação: seleção, bubble, inserção, merge, heap, quick. Por distribuição: counting; radix se ampliar o assunto. Buscas linear/binária não são ordenações: a lista fala em nove algoritmos contando duas buscas e sete ordenações, portanto não classificar as buscas como ordenação.
Escolhas: n pequeno/quase ordenado e poucas inversões → inserção; faixa inteira pequena + estabilidade → counting; pior caso garantido e espaço mínimo → heap; registros em arquivo maior que RAM → merge externo; uso geral com memória disponível e estabilidade → merge.
