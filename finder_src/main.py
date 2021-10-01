import os
import shutil
from finder_src import config as env
from PIL import Image
from PIL.ExifTags import TAGS


# migrar essa porra toda pra outro arquivo(/)
def finder():
    exif = {}
    imagens_extensoes = ['.jpg', '.png', '.jpeg']
    pasta_alvo = env.INPUT_PATH
    pasta_destino = env.OUTPUT_PATH

    for arquivo in os.listdir(pasta_alvo):
        arquivo_nome, arquivo_extensao = os.path.splitext(arquivo)

        if arquivo_extensao in imagens_extensoes:
            imagem = Image.open(f"{pasta_alvo}/{arquivo}")
            exif_arquivo = imagem._getexif()
            if exif_arquivo:

                for tag, value in exif_arquivo.items():
                    if tag in TAGS:
                        exif[TAGS[tag]] = value

                if exif["Model"] == 'GT-M2520':
                    shutil.copy2(f"{pasta_alvo}/{arquivo}", f"{pasta_destino}/{arquivo}-GT-M2520")

                elif exif["Model"] == 'DSC-P200':
                    shutil.copy2(f"{pasta_alvo}/{arquivo}", f"{pasta_destino}/{arquivo}-DSC-P200")

if __name__ == '__main__':
    finder()


