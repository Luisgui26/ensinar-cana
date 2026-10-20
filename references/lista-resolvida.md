# Guia das 50 questões

## Índice
Q1–15: conceitos; Q16–30: análise; Q31–45: aprofundamento; Q46–50: cenários. As respostas abaixo são soluções próprias, não gabarito oficial. Expandir cada conta e exemplo conforme `SKILL.md`; consultar enunciados integrais em `lista-original.txt`. Implementações de referência para os cenários em `implementacoes.md`.

## Q1–15
1. Linear testa em sequência até encontrar chave ou acabar. Não exige ordenação.
2. Binária exige ordenação compatível com comparador; descartar metade sem essa propriedade pode eliminar a chave existente. Ex.: [3,1,2], procurar 3: meio1, descarta lado esquerdo onde estava3.
3. Estável preserva ordem de chaves empatadas. Inserção com > é estável; seleção usual não: [(2,A),(2,B),(1,C)] → [(1,C),(2,B),(2,A)].
4. In place: auxiliar O(1) no critério estrito. Seleção/bubble/inserção iterativos e heap com sift-down iterativo; merge usual e counting não. Quick particiona in place mas usa pilha; declarar convenção. Versões recursivas simples podem alterar a classificação.
5. Procurar mínimo e colocá-lo no início do resto. Até n-1 trocas efetivas; n-1 chamadas se inclui autotroca no laço usual. Versão recursiva que processa singleton pode fazer chamada extra de autotroca; conferir código.
6. Vizinhos trocam e maior “borbulha” ao fim na varredura esquerda→direita. Não significa que todo vetor ficou ordenado na primeira passagem.
7. Cartas: prefixo já ordenado, pegar próxima e deslocar maiores para inseri-la.
8. Divisão e intercalação. Merge une sequências já ordenadas em tempo linear.
9. Pivô é referência de partição. Lomuto põe menores à esquerda e demais à direita, posicionando pivô; não ordena internamente os dois lados.
10. Max-heap: árvore completa e pai≥filhos. Filhos 2i+1,2i+2 dentro do tamanho; pai floor((i-1)/2), i>0.
11. Conta ocorrências e calcula posições por índices de chaves inteiras de faixa finita razoável; pode deslocar negativos por mínimo. Não funciona diretamente com qualquer objeto comparável.
12. [7,3,9,1] → [1,3,9,7] → [1,3,9,7] → [1,3,7,9].
13. [4,2,8,1] → [2,4,8,1] → [2,4,8,1] → [1,2,4,8].
14. Até 11 inspeções de meio para n=1024 na binária usual; até1024 na linear. Se “comparações” conta igualdade e ordem separadas, a constante muda. Explicar diferença entre 10 divisões e até11 inspeções, não só responder log₂1024=10.
15. Sete ordenações: seis por comparação (seleção/bubble/inserção/merge/heap/quick), counting por distribuição. Os nove algoritmos incluem duas buscas, que não são ordenações.

## Q16–30
16. Usar tabela de `algoritmos.md`, especificando variantes, parâmetros e pilha.
17. Seleção sempre busca mínimo no resto: n(n-1)/2 comparações. Inserção já ordenada não desloca e testa n-1 inserções. Adaptatividade depende do algoritmo, não só de ver dois laços no código.
18. Inversa: i deslocamentos na inserção do índice i, soma n(n-1)/2. Ordenada: zero deslocamentos e Θ(n) de testes. Para iguais com > não há deslocamentos.
19. Zerar flag a cada passagem, ativá-la se trocar, parar se permaneceu falsa. Vetor ordenado faz uma passagem com n-1 comparações: Θ(n).
20. T(n)=2T(n/2)+Θ(n), T(1)=Θ(1). a=2,b=2,d=1. a=b^d, caso2: Θ(n log n).
21. T(n)=T(n/2)+Θ(1). a=1 porque só uma metade é pesquisada; b=2,d=0; a=b^d=1, Θ(log n).
22. Pivô extremo repetidamente, partições 0 e n-1: soma quadrática. Aleatório controla expectativa para cada entrada; mediana de três evita algumas entradas ruins mas tem adversários.
23. Equilibrado: 2T(n/2)+cn, níveis custam cn, log n níveis → Θ(n log n). Pior: T(n-1)+cn → c Σj → Θ(n²). Não aplicar Mestre ao segundo.
24. Heapify desce altura O(log n), podendo descer toda ela: pior Θ(log n), não todos os casos. Construção: Σ quantidade de nós de altura h · O(h) ≤ O(n Σh/2^h)=O(n); laço de construção tem Θ(n) passos, logo Θ(n).
25. Counting ganha em ordem se k=o(n log n), empata se k=Θ(n log n), perde em ordem se k=ω(n log n); memória e constantes também importam. k=O(n) é condição suficiente, não necessária. n=1000,k=10^9 exige percorrer faixa bilionária; merge tem escala aproximada n log₂n≈9966, sem comparar constantes como tempos exatos.
26. Merge: buffers Θ(n), pilha Θ(log n), total Θ(n). Quick simples: partição O(1), pilha esperada Θ(log n) e pior Θ(n). Heap com sift-down iterativo: O(1).
27. Prefixo indica fim do bloco; último empate deve ocupar a última vaga: direita→esquerda e decremento preservam ordem. Frente→trás com esse mesmo decremento inverte iguais. Outra variante com inícios e incremento pode ser estável.
28. Lista encadeada não acessa meio por índice O(1). Localizar meios custa travessias; com estratégia adequada, soma n+n/2+...=Θ(n) de acessos. Não há garantia logarítmica de tempo; implementação ingênua que reinicia pode ser pior. Vetor/índice auxiliar muda a estrutura e os custos.
29. Posição uniforme entre1..n: E[C]=Σ(i·1/n)=(1/n)n(n+1)/2=(n+1)/2=Θ(n). Informar sucesso e uniformidade; ausência e probabilidades desiguais dão outra conta.
30. 1≤k≤n, folhas de tamanho Θ(k), em pior caso: n/k blocos · Θ(k²)=Θ(nk); intercalações têm log₂(n/k) níveis, Θ(n) cada: Θ(n log(n/k)+nk). Para k constante: Θ(n log n), com menor overhead prático. Para entradas especiais o custo das inserções pode ser menor. O corte k precisa ser limitado e ajustado empiricamente.

## Q31–45
31. Chaves distintas: n! resultados possíveis, árvore de decisão binária de altura h tem ≤2^h folhas. Então 2^h≥n!, h≥log₂(n!). Como n!≥(n/2)^(n/2) para n≥2 (ajustar pisos), h≥(n/2)log₂(n/2)=Ω(n log n). Isso limita pior caso do modelo por comparações.
32. Counting usa informação das chaves como índices e restrição de faixa; não se limita ao modelo da árvore de comparações.
33. Seja C_n custo esperado e pivô uniforme, C_0=0, custo local cn. n C_n=2Σ(j=0..n-1)C_j+cn². Para n-1: (n-1)C_(n-1)=2Σ(j=0..n-2)C_j+c(n-1)². Subtrair: n C_n=(n+1)C_(n-1)+c(2n-1). Dividir por n(n+1): C_n/(n+1)=C_(n-1)/n+c(2n-1)/(n(n+1)). Telescopar: parcela somada é Θ(1/n), soma Θ(log n), logo C_n=Θ(n log n). Para comparações locais n-1, solução exata usual C_n=2(n+1)H_n-4n, H_n=Σ1/i; não trocar modelos no meio.
34. Nós de altura h: O(n/2^(h+1)); custo por nó O(h). Soma O(n) pois Σh/2^h converge (vale2 de h=1 ao infinito). Laço bottom-up visita Θ(n) nós e cada chamada tem custo mínimo constante: Ω(n); construção Θ(n). Não calcular n vezes custo máximo e chamar essa cota frouxa de ordem exata.
35. T(n)=T(0,9n)+T(0,1n)+cn com arredondamentos: caminho mais longo log_(10/9)n e custo por nível ≤cn dão O(n log n). Até aproximadamente log₁₀n níveis todas as partes ainda estão ativas e o trabalho total por nível é Θ(n), dando Ω(n log n); portanto Θ(n log n). Alternativa por Akra–Bazzi p=1: soma das proporções=1 e integral 1/u gera log. Não usar Mestre padrão de partes iguais.
36. Lomuto com < e todos iguais devolve pivô extremo, T(n)=T(n-1)+Θ(n). Partição ternária separa <,=,>; recursar só < e >, todos iguais resolve numa passagem Θ(n). A degeneração não vale para toda implementação tradicional, especialmente Hoare balanceado em iguais.
37. Decorar registros com índice original; comparar (chave,índice) lexicograficamente; retirar decoração. Distinguir chaves iguais agora por índices preserva ordem original. Θ(n) posições extras para decoração explícita e Θ(n) tempo para preparar/remover; comparação do par é Θ(1) no modelo usual. Não declarar manutenção automática de O(1) de memória.
38. Merge bottom-up: intercalar blocos tamanho1,2,4,8... com buffer reutilizável. Θ(n log n) tempo e Θ(n) auxiliar; dispensa pilha recursiva, não o buffer.
39. Ordenar tudo: Θ(n log n) usando merge/heap. Quickselect só recursa no lado do k-ésimo: esperado Θ(n) com pivô uniforme, pior Θ(n²). Recorrência esperada exata depende de k: para r uniforme em0..n-1, A(n,k)=cn+(1/n)[Σ(r=k..n-1) A(r,k)+Σ(r=0..k-2) A(n-r-1,k-r-1)], k indexado1..n; r=k-1 encerra. Explicação simples por contração: pelo menos metade dos pivôs está no intervalo central e reduz lado a ≤3n/4; custo esperado até uma boa redução é O(n); n+3n/4+(3/4)²n+...=O(n), partição inicial Ω(n). Não usar T(n)=T(n/2)+n como recorrência exata do caso médio.
40. Em cada passo uma metade é ordenada. Se v[esq]≤v[meio], testar se chave pertence ao intervalo dessa metade; caso contrário explorar a outra. Análogo para direita. Chaves distintas dão Θ(log n) no pior caso. Duplicatas podem tornar ambas indistinguíveis e forçar Θ(n); declarar essa hipótese ausente do enunciado.
41. d passagens estáveis de custo Θ(n+b): Θ(d(n+b)). Base maior reduz d≈ceil(log_b(U+1)) e aumenta buffer/inicialização. Não escolher b só para minimizar d, ignorando memória. LSD exige estabilidade em cada dígito.
42. Cada deslocamento remove exatamente uma inversão em relação à chave inserida; há I deslocamentos, mais Θ(n) de preparação/testes de encerramento. Total Θ(n+I); para reverso I=n(n-1)/2.
43. Merge externo: ler blocos que cabem em RAM, ordená-los e gravar runs; intercalar múltiplos runs em arquivos, com buffers de leitura/escrita e estrutura para o próximo menor. Acesso sequencial reduz I/O. Não carregar tudo nem manter um buffer de tamanho total na RAM.
44. [(2,A),(2,B),(1,C)] é max-heap válido se empates não trocam. Raiz troca com último → [(1,C),(2,B),(2,A)]. Heapify troca1 e2B; extração seguinte produz [(1,C),(2,B),(2,A)]. Os dois2 inverteram; instável.
45. Antes da iteração i, prefixo v[0..i-1] está ordenado e é permutação dos registros originais desse prefixo. Inicialização i=1: singleton ordenado. Manutenção: guardar chave, deslocar maiores, inserir na vaga conserva elementos e ordena prefixo até i. Término i=n: prefixo é vetor inteiro. i cresce e é limitado, garantindo término. Para prova de estabilidade usar deslocamento estrito >.

## Q46–50
46. Counting estável por nota, k=101, Θ(n+101) tempo e Θ(n+101) espaço. Preserva ordem alfabética prévia nos empates. Heap/quick usuais podem destruí-la; merge também serve mas tem Θ(n log n).
47. Inserção iterativa: Θ(n+I), O(1) extra. “Poucas dezenas fora de ordem” não determina I: uma leitura pode precisar atravessar quase todo vetor; q leituras deslocadas podem gerar O(qn) inversões. Justificar em termos de I ou q limitado, sem prometer Θ(n) para qualquer entrada chamada quase ordenada. Merge garante Θ(n log n) se desordem for grande.
48. Heap com sift-down iterativo: pior Θ(n log n), auxiliar O(1). Quick simples não garante pior n log n; merge exige buffer linear. Garantia assintótica sozinha não comprova prazo de tempo real: medir limite na máquina e limitar n.
49. Merge externo; RAM de8 GB exige reservar memória para sistema/buffers, não criar um bloco de8 GB integral. Arquivo200 GB gera vários runs; intercalar com buffers e heap de cabeças, possivelmente várias passagens.
50. Linear em m consultas: Θ(mn). Ordenar uma vez por merge e consultar: Θ(n log n+m log n). No modelo simplificado custos n por linear, n log₂n ordenar e log₂n consultar: m>n log₂n/(n-log₂n). Para n=10^7, log₂n≈23,2535, limiar≈23,25355 →24 consultas. É aproximação de operações e constantes unitárias, não limite universal de execução real. Busca linear com sucesso uniforme custa cerca de n/2 e muda limiar. Para m=100000 vantagem de reutilizar ordenação é ampla. Base precisa manter-se estática; não reordenar por consulta.
