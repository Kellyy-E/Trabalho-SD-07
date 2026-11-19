# Trabalho 07 — Modelagem e Avaliação de Desempenho com SPN

Modelo em **Redes de Petri Estocásticas (SPN)** desenvolvido na ferramenta **Jupiter** para a avaliação quantitativa de desempenho de uma recepção hospitalar com fluxos de pacientes **agendados** (prioritários via arco inibidor) e **espontâneos** (com etapa probabilística de cadastro prévio), capacidade limitada ($K$) e pool compartilhado de atendentes ($N$).

---

## Estrutura do Repositório

| Arquivo | Descrição |
| :--- | :--- |
| `spn_recepcao_agendado_espontaneo (1).json` | Modelo SPN completo para importação no **Jupiter**. |
| `spn_recepcao_agendado_espontaneo.png` | Representação gráfica do modelo SPN implementado. |
| `analysis-report-1795118559923.txt` | Relatório de simulação estacionária do **Cenário de Referência** ($N=6$, $K=20$, 250 replicações, 22,6 milhões de eventos). |
| `experimento_E1_demanda.csv` | **Experimento E1** — Taxa de chegada (5 níveis de demanda: intervalo de espontâneos de 80 s a 200 s). |
| `experimento_E2_recursos_N.csv` | **Experimento E2** — Capacidade de processamento ($N \in \{4, 6, 8\}$ atendentes). |
| `experimento_E3_capacidade_K.csv` | **Experimento E3** — Capacidade do sistema/buffer ($K \in \{10, 20, 30\}$ vagas). |
| `scenarios-U-1795054431473.csv` | **Experimento E4** — Demanda e recursos combinados (utilização $U$ para $N \in \{4, 6, 8\}$ nos 5 níveis de demanda). |
| `scenarios-U-1795119774879.pdf` | Gráfico 2D do Experimento E4 exportado diretamente do Jupiter. |
| `gerar_graficos.py` | Script Python para reproduzir automaticamente os 4 gráficos do artigo em alta resolução (300 DPI). |

---

## Como Reproduzir os Gráficos

Pré-requisitos: Python 3 com `pandas` e `matplotlib`.

```bash
pip install pandas matplotlib
python gerar_graficos.py
```

Os 4 gráficos em PNG (300 DPI) serão gerados automaticamente na pasta `graficos/`:
* `grafico_E1_demanda_espera.png`
* `grafico_E2_recursos_atendentes.png`
* `grafico_E3_capacidade_buffer.png`
* `grafico_E4_utilizacao_combinada.png`

---

## Como Abrir o Modelo no Jupiter

1. Acesse a ferramenta **Jupiter**.
2. Importe o arquivo `spn_recepcao_agendado_espontaneo (1).json`.
3. Execute em modo **Stationary Simulation** (horizonte de `2.000.000 s`, aquecimento de `10%`, 250 replicações, IC de 95%) ou utilize a aba **Scenarios** para replicar as varreduras E1 a E4.
