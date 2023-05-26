import os
import shutil
from finder_src import config as env
from PIL import Image, ExifTags


# TODO: organizar essa merda
imagens_extensoes = ['.jpg', '.png', '.jpeg']
resolucoes = [
    (800, 600),
    (600, 800),
    (1024,768)
]
modelos = [
    'GT-M2520',
    'DSC-P200',
    'DSC-W110',
    'C261'
]


def mergulhador(caminho):
    for raiz, pastas, arquivos in os.walk(caminho):
        if pastas:
            for pasta in pastas:
                mergulhador(os.path.join(caminho, pasta))
        else:
            for arquivo in arquivos:
                arquivo_nome, arquivo_extensao = os.path.splitext(arquivo)
                if arquivo_extensao in imagens_extensoes:
                    arquivo_minuciado = exif_extrator(os.path.join(caminho, arquivo))
                    arquivo_validador(arquivo_minuciado)


def arquivo_validador(arquivo):
    # TODO: passar parametros de arquivo, e imagem como classe
    if arquivo[0] in resolucoes or arquivo[1].get('Model') in modelos:
        with open('output_arquivos.txt', 'a') as f:
            print(f'{arquivo[2]}', file=f)
        # TODO: previnir erros de exif quando imagem coletada por dimensões
        arquivo_criador(
            env.OUTPUT_PATH,
            os.path.split(arquivo[2])[0],
            arquivo[1].get('Model'), os.path.split(arquivo[2])[1]
        )


def finder():
    # TODO: limpar lixos
    exif = {}
    # TODO: adicionar mais extensões (imagens, videos, musicas, texto simples)
    imagens_extensoes = ['.jpg', '.png', '.jpeg']
    textos = ['.xml']
    videos = ['.rm', '.mpg', '.mpeg', '.mp3']
    input_pasta = env.INPUT_PATH
    output_pasta = env.OUTPUT_PATH

    mergulhador(input_pasta)


def arquivo_criador(pasta_output, pasta_input, pasta_nome, nm_arquivo):
    if not os.path.exists(os.path.join(pasta_output, pasta_nome)):
        os.makedirs(os.path.join(pasta_output, pasta_nome))
    shutil.copy2(os.path.join(pasta_input, nm_arquivo), os.path.join(pasta_output, pasta_nome, nm_arquivo))


def exif_extrator(caminho_arquivo):
    exif = {}
    imagem = Image.open(f"{caminho_arquivo}")
    exif_arquivo = imagem._getexif()
    imagem_tamanho = imagem._size

    if exif_arquivo:
        for tag, valor in exif_arquivo.items():
            if tag in ExifTags.TAGS:
                nm_tag = ExifTags.TAGS[tag]
                exif[nm_tag] = valor

    return imagem_tamanho, exif, caminho_arquivo


if __name__ == '__main__':
    finder()


