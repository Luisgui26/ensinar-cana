# Implementações dos cenários

Exemplos Java simples. Explicar cada função ao usá-la. Não entregar todos os métodos quando só um for solicitado. Os registros são objetos para que estabilidade tenha significado observável.

```java
import java.util.Arrays;

class Cenarios {
    static class Aluno {
        String nome;
        int nota;
        Aluno(String nome, int nota) { this.nome = nome; this.nota = nota; }
    }

    // Q46: entrada já está em ordem alfabética; notas entre 0 e 100.
    static Aluno[] ordenarNotas(Aluno[] alunos) {
        int[] c = new int[101];
        for (Aluno a : alunos) c[a.nota]++;
        // c[x] passa a indicar quantos alunos têm nota <= x.
        for (int x = 1; x < c.length; x++) c[x] += c[x - 1];
        Aluno[] saida = new Aluno[alunos.length];
        for (int i = alunos.length - 1; i >= 0; i--) {
            Aluno a = alunos[i];
            saida[--c[a.nota]] = a; // Última vaga livre dessa nota.
        }
        return saida;
    }

    // Q47: timestamps; para registros, deslocar o objeto inteiro.
    static void insercao(long[] v) {
        for (int i = 1; i < v.length; i++) {
            long chave = v[i];
            int j = i - 1;
            while (j >= 0 && v[j] > chave) {
                v[j + 1] = v[j];
                j--;
            }
            v[j + 1] = chave;
        }
    }

    // Q48: restaurar max-heap em v[0..tamanho-1], sem recursão.
    static void descer(long[] v, int tamanho, int pai) {
        while (pai < tamanho / 2) { // Só nós com filho esquerdo.
            int filho = 2 * pai + 1;
            if (filho + 1 < tamanho && v[filho + 1] > v[filho]) filho++;
            if (v[pai] >= v[filho]) return;
            long aux = v[pai]; v[pai] = v[filho]; v[filho] = aux;
            pai = filho;
        }
    }
    static void heapSort(long[] v) {
        for (int i = v.length / 2 - 1; i >= 0; i--) descer(v, v.length, i);
        for (int fim = v.length - 1; fim > 0; fim--) {
            long aux = v[0]; v[0] = v[fim]; v[fim] = aux;
            descer(v, fim, 0);
        }
    }

    // Q50: ordenar uma única vez; consultas não modificam a base.
    static boolean existe(long[] baseOrdenada, long chave) {
        int esq = 0, dir = baseOrdenada.length - 1;
        while (esq <= dir) {
            int meio = esq + (dir - esq) / 2;
            if (baseOrdenada[meio] == chave) return true;
            if (baseOrdenada[meio] < chave) esq = meio + 1;
            else dir = meio - 1;
        }
        return false;
    }
    static boolean[] consultar(long[] base, long[] chaves) {
        heapSort(base); // Preparação única Θ(n log n) no pior caso, O(1) extra.
        boolean[] respostas = new boolean[chaves.length];
        for (int i = 0; i < chaves.length; i++) respostas[i] = existe(base, chaves[i]);
        return respostas; // Saída de m booleanos: Θ(m), informar separadamente.
    }
}
```

Q49 — pseudocódigo de merge externo:
1. Reservar parte da RAM para um bloco de registros e parte para buffers/estrutura de intercalação.
2. Enquanto houver entrada: ler bloco; ordenar em RAM; gravar arquivo temporário de run ordenado.
3. Escolher fan-in f que caiba na RAM e no limite de arquivos abertos.
4. Para cada grupo de até f runs, abrir buffer por run e buffer de saída. Colocar no min-heap a primeira chave de cada run.
5. Retirar mínimo, gravar no buffer de saída e repor próximo registro do mesmo run. Recarregar/esvaziar buffers sequencialmente.
6. Repetir passagens até restar um run final; verificar término e integridade antes de apagar temporários.
Há Θ(N/B) transferências por passagem e aproximadamente ceil(log_f R) passagens de intercalação, para N registros, buffers de B registros e R runs. Explicar que unidades bytes/registros precisam ser compatíveis. Não chamar esta rotina de O(1) em espaço em disco.
