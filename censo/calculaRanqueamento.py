import pandas as pd
import seaborn as sns

# DECLARAÇÃO E LEITURA DO ARQUIVO DE NOTAS #
caminho_arquivo = 'avaliacoes/notas.txt'
data = pd.read_csv(caminho_arquivo, sep='\t', header=None)

nome_avaliados = {
    0: 'Dedé',
    1: 'Rodrigo',
    2: 'Diego',
    3: 'Coutinho',
    4: 'Gusta',
    5: 'Meuga',
    6: 'Cardoso',
    7: 'Pizza',
    8: 'Embrithil',
    9: 'Roulland',
    10: 'Falsete',
    11: 'Rafael',
    12: 'Rd',
    13: 'Rocha',
    14: 'Tiago',
    15: 'Hulk',
    16: 'PeterJack'
}
nome_posicoes = {
    0: 'Top',
    1: 'Jungle',
    2: 'Mid',
    3: 'Sup',
    4: 'Adc'
}

# FUNÇÕES #
def calcular_media_por_posicao(data):
    medias = {}
    for posicao in range(5):
        nome_posicao = nome_posicoes[posicao]
        medias_posicao = []
        for jogador in range(17):
            notas_jogador = data.iloc[:, jogador * 5 + posicao]
            notas_jogador_sem_zeros = notas_jogador.replace(0, pd.NA)  # Substituir os zeros por NaN
            media_jogador = notas_jogador_sem_zeros.mean()
            medias_posicao.append(media_jogador)
        medias[nome_posicao] = medias_posicao
    return medias

def criar_tabela(medias_por_posicao):
    df_medias = pd.DataFrame(medias_por_posicao, index=nome_avaliados.values())
    df_medias.index.name = 'Posição'
    df_medias.columns.name = 'Jogador'
    df_medias = df_medias.round(2)
    return df_medias

def encontrar_melhor_jogador_todas_posicoes(medias_por_posicao):
    melhores_jogadores = {}
    for posicao in nome_posicoes.values():
        medias = medias_por_posicao[posicao]
        indice_melhor_jogador = medias.index(max(medias))
        melhores_jogadores[posicao] = (list(nome_avaliados.values())[indice_melhor_jogador], round(medias[indice_melhor_jogador], 2))
    df_melhores_jogadores = pd.DataFrame(melhores_jogadores.values(), index=melhores_jogadores.keys(), columns=['Melhor Jogador', 'Média'])
    df_melhores_jogadores.index.name = 'Posição'
    
    return df_melhores_jogadores

def encontrar_pior_jogador_todas_posicoes(medias_por_posicao):
    piores_jogadores = {}
    for posicao in nome_posicoes.values():
        medias = medias_por_posicao[posicao]
        indice_pior_jogador = medias.index(min(medias))
        piores_jogadores[posicao] = (list(nome_avaliados.values())[indice_pior_jogador], round(medias[indice_pior_jogador], 2))
    df_piores_jogadores = pd.DataFrame(piores_jogadores.values(), index=piores_jogadores.keys(), columns=['Pior Jogador', 'Média'])
    df_piores_jogadores.index.name = 'Posição'
    
    return df_piores_jogadores

def encontrar_melhores_tres_geral_media(tabela_bonita):
    media_geral = tabela_bonita.mean(axis=1)
    media_geral = media_geral.round(2)
    melhores_tres_geral_media = media_geral.nlargest(3)
    
    return melhores_tres_geral_media

def encontrar_piores_tres_geral_media(tabela_bonita):
    media_geral = tabela_bonita.mean(axis=1)
    media_geral = media_geral.round(2)
    piores_tres_geral_media = media_geral.nsmallest(3)
    
    return piores_tres_geral_media

def criar_ranking_geral(tabela_bonita):
    media_geral = tabela_bonita.mean(axis=1)
    media_geral = media_geral.round(2)
    media_geral = media_geral.fillna(0)
    ranking_geral = media_geral.sort_values(ascending=False)
    
    return ranking_geral

# ASSOCIAÇÕES #
medias_por_posicao = calcular_media_por_posicao(data)
tabela_bonita = criar_tabela(medias_por_posicao)
df_melhores_jogadores = encontrar_melhor_jogador_todas_posicoes(medias_por_posicao)
df_piores_jogadores = encontrar_pior_jogador_todas_posicoes(medias_por_posicao)
melhores_tres_geral_media = encontrar_melhores_tres_geral_media(tabela_bonita)
piores_tres_geral_media = encontrar_piores_tres_geral_media(tabela_bonita)
ranking_geral = criar_ranking_geral(tabela_bonita)

# EXPORT #
print("Tabela bonitinha")
print(tabela_bonita)

print("Melhores jogadores por posição:")
print(df_melhores_jogadores)

print("\nPiores jogadores por posição:")
print(df_piores_jogadores)

print("Três melhores jogadores no geral com base na média geral das notas:")
print(melhores_tres_geral_media)

print("\nTrês piores jogadores no geral com base na média geral das notas:")
print(piores_tres_geral_media)

print("Ranking geral de todos os jogadores:")
print(ranking_geral)