import os
import shutil
from finder_src import config as env
from PIL import Image
from PIL.ExifTags import TAGS


def finder():
    exif = {}
    # TODO: adicionar mais extensões (imagens, videos, musicas, texto simples)
    imagens_extensoes = ['.jpg', '.png', '.jpeg']
    textos = ['.xml']
    videos = ['.rm', '.mpg', '.mpeg', '.mp3']
    pasta_input = env.INPUT_PATH
    pasta_output = env.OUTPUT_PATH

    for pasta, subpastas, arquivos in os.walk(pasta_input):

        for subpasta in subpastas:
            joim = os.path.join(pasta_input, subpasta)

            if not os.path.isfile(joim):
                for arquivo in os.listdir(joim):

                    pasta_atual = os.path.join(pasta_input, pasta, subpasta)
                    arquivo_nome, arquivo_extensao = os.path.splitext(arquivo)

                    if arquivo_extensao in imagens_extensoes:
                        arquivo_exif = exif_construtor(os.path.join(pasta_atual, arquivo))

                        if arquivo_exif[1]:
                            if arquivo_exif[1]["Model"] == 'GT-M2520':
                                arquivo_criador(pasta_output, pasta_atual, 'GT-M2520(cel_samsung)', arquivo)

                            if arquivo_exif[1]["Model"] == 'DSC-P200':
                                arquivo_criador(pasta_output, pasta_atual, 'DSC-P200(flavio)', arquivo)

                            if arquivo_exif[1]["Model"] == 'DSC-W110':
                                arquivo_criador(pasta_output, pasta_atual, 'DSC-W110(camera_quebrada)', arquivo)

                            if arquivo_exif[1]["Model"] == 'C261':
                                arquivo_criador(pasta_output, pasta_atual, 'C261(cel_motorola)', arquivo)
                        else:
                            if arquivo_exif[0][0] == 800 and arquivo_exif[0][1] == 600:
                                arquivo_criador(pasta_output, pasta_atual, '800x600', arquivo)

                            if arquivo_exif[0][1] == 800 and arquivo_exif[0][0] == 600:
                                arquivo_criador(pasta_output, pasta_atual, '600x800', arquivo)

                            if arquivo_exif[0][0] == 1024 and arquivo_exif[0][1] == 768:
                                arquivo_criador(pasta_output, pasta_atual, '1024x768', arquivo)


def arquivo_criador(pasta_output, pasta_input, pasta_nome, arquivo):
    if not os.path.exists(os.path.join(pasta_output, pasta_nome)):
        os.makedirs(os.path.join(pasta_output, pasta_nome))
    shutil.copy2(os.path.join(pasta_input, arquivo), os.path.join(pasta_output, pasta_nome, arquivo))


def exif_construtor(caminho_arquivo):
    exif = {}
    imagem = Image.open(f"{caminho_arquivo}")
    exif_arquivo = imagem._getexif()
    imagem_tamanho = imagem._size

    if exif_arquivo:
        for tag, value in exif_arquivo.items():
            if tag in TAGS:
                exif[TAGS[tag]] = value

    return imagem_tamanho, exif


if __name__ == '__main__':
    finder()


