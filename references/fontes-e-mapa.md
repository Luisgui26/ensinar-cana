# Fontes e roteiro

## Materiais incorporados
- `assets/AULA1.pdf`: 52 páginas físicas. Seleção p.1–26; bubble p.27–52. Versões recursivas e iterativas, simulações e árvores de T(n)=T(n-1)+n.
- `assets/AULA2.pdf`: 80 páginas físicas. Inserção p.1–27; merge p.28–50; quick p.51–80. Partição Lomuto p.53, exemplo p.55–59, 90/10 p.71–74, pilha p.76–79.
- `assets/AULA3.pdf`: 23 páginas físicas. Limite de comparação p.1; counting p.2–17; radix/bucket p.18; tabelas p.19–21; revisão AV2 p.22.
- `assets/lista-unidade-2.pdf`: 5 páginas, 50 questões. Q1–15 conceitos/simulações; Q16–30 análise; Q31–45 demonstrações/variantes; Q46–50 escolhas/implementação. Referência textual: `lista-original.txt`.
- `assets/av1.pdf`: 3 páginas, na ordem física terceira/segunda/primeira da prova. Estrutura e solução comentadas em `prova-analisada.md`.

Os PDFs de aula estão com os slides lateralizados em parte da página. Para consultar visualmente, renderizar, girar 90 graus no sentido horário e recortar as margens brancas; isto foi feito para produzir o OCR textual. Textos `AULA*.txt` conservam a numeração física dos PDFs, não a numeração global do rodapé do curso.

## Escopo demonstrado
AULA3 p.22 orienta explicitamente para AV2: simular algoritmos; escrever pseudocódigo recursivo/iterativo; montar/resolver recorrências; justificar casos; comparar tempo, espaço e estabilidade; argumentar limite Ω(n log n) e exceção do counting. Também menciona laboratório de 30%, informação do material, não confirmação de regra atual de avaliação.
Heapsort e buscas estão na lista e nas tabelas finais, mas estes anexos não trazem uma aula detalhada própria deles. Ensinar a partir dos fundamentos e identificar essa complementação.
Não há provas AV2 anexadas. Usar AV1 para o estilo e a lista/revisão para assuntos de Unidade II.

## Roteiro sugerido
1. n, operação, melhor/médio/pior, O/Ω/Θ e laços.
2. Busca linear/binária, contagem e redução n-1 versus n/2.
3. Seleção, bubble e inserção: simulação → pseudocódigo → somatório/recorrência → espaço/estabilidade.
4. Merge: intercalação → árvore e Mestre.
5. Quick: partição → melhor/pior/médio, repetidos e memória.
6. Heap: propriedade → índices → heapify → construção e ordenação.
7. Counting: frequências → prefixos → saída estável → n+k.
8. Comparações, escolhas práticas e limite inferior.
9. Revisão da lista, simulado sem respostas e correção pelos erros.

Em revisão urgente, priorizar itens explicitamente mencionados no slide de revisão e a obrigação de justificar. Não inferir probabilidade numérica de cobrança nem excluir questões avançadas por conveniência.

## Pontos para conferir, sem reproduzir inconsistências
- AULA1 p.3 tem laço externo ini..fim-1 e interno i+1..fim: n(n-1)/2 comparações, embora p.22–25 simplifiquem com n(n+1)/2. Essa diferença não muda Θ(n²), mas muda conta exata.
- Com índices inclusivos e caso base ini≥fim, tamanho do trecho é fim-ini+1 e parada ocorre em n=1, não n=0. Algumas lâminas de altura usam n-h=0; para esse código usar n-h=1, h=n-1. O custo assintótico continua linear em altura.
- AULA2 p.31 tem ≤ na escolha da esquerda no empate, confirmado visualmente: o merge é estável. OCR pode reduzir ≤ a <.
- AULA2 p.67 descreve dois lados n/2 mais pivô como simplificação: os tamanhos reais somam n-1. Usar floor((n-1)/2) e ceil((n-1)/2) para fórmula literal; 2T(n/2)+Θ(n) para análise assintótica balanceada.
- Árvores com altura h têm h+1 níveis contando raiz e folhas. Em merge, h níveis internos lineares e folhas de custo total Θ(n).
- AULA2 p.71/75 usa generalizações práticas fortes para quick; contextualizar como expectativa sob distribuição/estratégia de pivô. Mediana de três determinística não garante tempo Θ(n log n).
- AULA2 p.79 dá O(log n) de pilha sem caso na tabela; qualificar média/equilíbrio ou versão otimizada. A versão simples pode ter Θ(n) de pilha.
- AULA3 p.15 menciona heap na forma aT(n/b)+f(n): distinguir heapify local, construção bottom-up e extrações; heapsort completo não se resume ao Mestre como mergesort.
- AULA3 p.18/21 generaliza bucket como sem comparações e pior O(n log n). Bucket pode usar ordenação por comparação dentro dos baldes; seu pior depende dessa rotina (inserção: Θ(n²), merge/heap: O(n log n)). Não ensinar como propriedade universal.
- Na tabela de AULA3, bubble linear no melhor caso exige bandeira, ausente no código simples de AULA1.
- Em Shellsort, não decorar expoentes sem indicar sequência de gaps. É complemento, não uma das sete ordenações nucleares da lista.

## Atualização do escopo — 20/10/2026
O aluno informou nova orientação do professor: as duas questões de cálculo cobram ordenação; a primeira questão pode tratar dos algoritmos estudados, excluindo busca linear e binária. Aplicar essa orientação aos simulados atuais. AV1 permanece referência histórica de estilo. Pesos, duração e extra são convenções herdadas, sem confirmação nova. Não excluir algoritmos de ordenação do treino por preferência e não impor recorrência a versões iterativas. Os materiais sobre buscas permanecem para consulta geral, fora do simulado atual.

A orientação complementar recebida em 20/10 esclarece que os algoritmos da prova não precisam constar nos PDFs: podem ser novos, desde que semelhantes em estrutura e nível aos estudados. Em particular, a Q1 pode incluir outra busca, mas não busca linear/binária; Q2 e Q3 continuam voltadas ao custo de ordenações.
