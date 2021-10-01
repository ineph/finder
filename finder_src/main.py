import os
import shutil
from finder_src import config as env
from PIL import Image
from PIL.ExifTags import TAGS


def finder():
    exif = {}
    # TODO: adicionar mais extensões (imagens, videos, musicas, texto simples)
    imagens_extensoes = ['.jpg', '.png', '.jpeg']
    pasta_alvo = env.INPUT_PATH
    pasta_destino = env.OUTPUT_PATH

    for arquivo in os.listdir(pasta_alvo):
        arquivo_nome, arquivo_extensao = os.path.splitext(arquivo)

        # TODO: navegar para pastas filhas e procurar mais arquivos recursamente
        if arquivo_extensao in imagens_extensoes:
            imagem = Image.open(f"{pasta_alvo}/{arquivo}")
            exif_arquivo = imagem._getexif()
            imagem_tamanho = imagem._size

            if exif_arquivo:
                for tag, value in exif_arquivo.items():
                    if tag in TAGS:
                        exif[TAGS[tag]] = value
                # TODO: adicionar parâmetros dinâmicos (modelos de cameras e tamanhos)
                if exif["Model"] == 'GT-M2520':
                    arquivo_criador(pasta_destino, pasta_alvo, 'GT-M2520', arquivo)

                if exif["Model"] == 'DSC-P200':
                    arquivo_criador(pasta_destino, pasta_alvo, 'DSC-P200', arquivo)

            else:
                if imagem_tamanho[0] == 800 and imagem_tamanho[1] == 600:
                    arquivo_criador(pasta_destino, pasta_alvo, '800x600', arquivo)

                if imagem_tamanho[1] == 800 and imagem_tamanho[0] == 600:
                    arquivo_criador(pasta_destino, pasta_alvo, '600x800', arquivo)

                if imagem_tamanho[0] == 1024 and imagem_tamanho[1] == 768:
                    arquivo_criador(pasta_destino, pasta_alvo, '1024x768', arquivo)


def arquivo_criador(pasta_destino, pasta_alvo, pasta_nome, arquivo):
    if not os.path.exists(f"{pasta_destino}/{pasta_nome}"):
        os.makedirs(f"{pasta_destino}/{pasta_nome}")
    shutil.copy2(f"{pasta_alvo}/{arquivo}", f"{pasta_destino}/{pasta_nome}/{arquivo}")
# testando

if __name__ == '__main__':
    # TODO: organizar estrutura e separar em arquivos (sem overengineering, caralho)
    finder()


