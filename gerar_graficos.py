import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Configurar diretório de saída
OUTPUT_DIR = "graficos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Configurações globais de estilo para artigos científicos (IEEE)
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

print("=" * 60)
print("  GERADOR DE GRÁFICOS - TRABALHO 07 (SPN / JUPITER)")
print("=" * 60)



def gerar_grafico_e1():
    csv_file = "experimento_E1_demanda.csv"
    if not os.path.exists(csv_file):
        print(f"[AVISO] Arquivo {csv_file} não encontrado. Pulando E1.")
        return

    df = pd.read_csv(csv_file, sep=";")
    plt.figure(figsize=(7, 4.5))

    plt.plot(df['ATRASO_CHEGADA_E'], df['MQT_E'], marker='o', color='#e74c3c', linewidth=2, label='Espontâneos (MQT_E)')
    plt.plot(df['ATRASO_CHEGADA_E'], df['MQT_A'], marker='s', color='#2980b9', linewidth=2, label='Agendados (MQT_A)')
    plt.plot(df['ATRASO_CHEGADA_E'], df['MQT'], marker='^', color='#27ae60', linewidth=2, linestyle='--', label='Geral (MQT)')

    plt.title('Experimento E1: Tempo Médio de Espera na Fila vs. Demanda', fontsize=11, fontweight='bold', pad=10)
    plt.xlabel('Intervalo Médio entre Chegadas de Espontâneos (s)\n[Demanda Decrescente ->]', fontsize=10)
    plt.ylabel('Tempo Médio na Fila (s)', fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(fontsize=9, loc='upper right')
    plt.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "grafico_E1_demanda_espera.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Gráfico E1 gerado: {out_path}")


def gerar_grafico_e2():
    csv_file = "experimento_E2_recursos_N.csv"
    if not os.path.exists(csv_file):
        print(f"[AVISO] Arquivo {csv_file} não encontrado. Pulando E2.")
        return

    df = pd.read_csv(csv_file, sep=";")
    fig, ax1 = plt.subplots(figsize=(7, 4.5))

    color_bar = '#e67e22'
    ax1.set_xlabel('Número de Atendentes (N)', fontsize=10)
    ax1.set_ylabel('Tempo Médio de Espera na Fila MQT (s)', color=color_bar, fontsize=10)
    bars = ax1.bar(df['N'].astype(str), df['MQT'], color=color_bar, alpha=0.6, width=0.35, label='Fila MQT (s)')
    ax1.tick_params(axis='y', labelcolor=color_bar)
    ax1.set_ylim(0, max(df['MQT']) * 1.18)

    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + max(df['MQT']) * 0.02, f'{yval:.1f}s', ha='center', va='bottom', color=color_bar, fontweight='bold', fontsize=9)

    ax2 = ax1.twinx()
    color_line = '#27ae60'
    ax2.set_ylabel('Taxa de Utilização dos Atendentes U (%)', color=color_line, fontsize=10)
    ax2.plot(df['N'].astype(str), df['U'], color=color_line, marker='s', linewidth=2.5, label='Utilização U (%)')
    ax2.tick_params(axis='y', labelcolor=color_line)
    ax2.set_ylim(0, 110)

    for i, txt in enumerate(df['U']):
        ax2.annotate(f'{txt:.1f}%', (str(df['N'].iloc[i]), txt + 1.5), color=color_line, fontweight='bold', ha='center', fontsize=9)

    plt.title('Experimento E2: Impacto da Equipe de Atendimento (N) na Fila e Utilização', fontsize=11, fontweight='bold', pad=10)
    fig.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "grafico_E2_recursos_atendentes.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Gráfico E2 gerado: {out_path}")



def gerar_grafico_e3():
    csv_file = "experimento_E3_capacidade_K.csv"
    if not os.path.exists(csv_file):
        print(f"[AVISO] Arquivo {csv_file} não encontrado. Pulando E3.")
        return

    df = pd.read_csv(csv_file, sep=";")
    fig, ax1 = plt.subplots(figsize=(7, 4.5))

    color_bar = '#c0392b'
    ax1.set_xlabel('Capacidade Total do Sistema (Vagas K)', fontsize=10)
    ax1.set_ylabel('Probabilidade de Descarte DP (%)', color=color_bar, fontsize=10)
    bars = ax1.bar(df['K'].astype(str), df['DP'], color=color_bar, alpha=0.6, width=0.35, label='Descarte DP (%)')
    ax1.tick_params(axis='y', labelcolor=color_bar)
    ax1.set_ylim(0, max(df['DP']) * 1.25)

    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + max(df['DP']) * 0.025, f'{yval:.3f}%', ha='center', va='bottom', color=color_bar, fontweight='bold', fontsize=9)

    ax2 = ax1.twinx()
    color_line = '#2980b9'
    ax2.set_ylabel('Tempo Médio na Fila MQT (s)', color=color_line, fontsize=10)
    ax2.plot(df['K'].astype(str), df['MQT'], color=color_line, marker='o', linewidth=2.5, label='Fila MQT (s)')
    ax2.tick_params(axis='y', labelcolor=color_line)
    ax2.set_ylim(0, max(df['MQT']) * 1.25)

    for i, txt in enumerate(df['MQT']):
        ax2.annotate(f'{txt:.1f}s', (str(df['K'].iloc[i]), txt + max(df['MQT']) * 0.04), color=color_line, fontweight='bold', ha='center', fontsize=9)

    plt.title('Experimento E3: Impacto da Capacidade de Vagas (K) no Descarte e Espera', fontsize=11, fontweight='bold', pad=10)
    fig.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "grafico_E3_capacidade_buffer.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Gráfico E3 gerado: {out_path}")



def gerar_grafico_e4():
    csv_file = "scenarios-U-1795054431473.csv"
    if not os.path.exists(csv_file):
        print(f"[AVISO] Arquivo {csv_file} não encontrado. Pulando E4.")
        return

    df = pd.read_csv(csv_file, sep=";")
    plt.figure(figsize=(7, 4.5))

    plt.plot(df['ATRASO_CHEGADA_E'], df['N=4'], marker='o', color='#e74c3c', linewidth=2, label='N = 4 Atendentes (Equipe Reduzida)')
    plt.plot(df['ATRASO_CHEGADA_E'], df['N=6'], marker='s', color='#27ae60', linewidth=2, label='N = 6 Atendentes (Baseline Recomendado)')
    plt.plot(df['ATRASO_CHEGADA_E'], df['N=8'], marker='^', color='#2980b9', linewidth=2, label='N = 8 Atendentes (Equipe Reforçada)')

    plt.title('Experimento E4: Utilização dos Recursos vs. Demanda e Dimensionamento', fontsize=11, fontweight='bold', pad=10)
    plt.xlabel('Intervalo Médio entre Chegadas de Espontâneos (s)\n[Demanda Decrescente ->]', fontsize=10)
    plt.ylabel('Taxa de Utilização dos Atendentes U (%)', fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(fontsize=9, loc='upper right')
    plt.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "grafico_E4_utilizacao_combinada.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Gráfico E4 gerado: {out_path}")


if __name__ == "__main__":
    gerar_grafico_e1()
    gerar_grafico_e2()
    gerar_grafico_e3()
    gerar_grafico_e4()
    print("=" * 60)
    print("Todos os gráficos foram gerados com sucesso na pasta /graficos!")
    print("=" * 60)
