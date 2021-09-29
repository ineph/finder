import os
import shutil
from finder_src import vars
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS

# migrar essa porra toda pra outro arquivo
def finder():
    exif = {}
    imagens_extensoes = ['.jpg', '.png', '.jpeg']
    pasta_destino = vars.get("OUTPUT_PATH")

    for arquivo in os.listdir('../..'):
        a = pasta_destino
        arquivo_nome, arquivo_extensao = os.path.splitext(arquivo)

        if arquivo_extensao in imagens_extensoes:
            imagem = Image.open(f"../{arquivo}")
            exif_arquivo = imagem._getexif()
            if exif_arquivo:
                caminho = Path(os.getcwd()).absolute()
                pasta_pai = caminho

                for tag, value in exif_arquivo.items():
                    if tag in TAGS:
                        exif[TAGS[tag]] = value

                if exif["Model"] == 'GT-M2520':

                    shutil.copy2(f"{caminho.parents[0]}/{arquivo}", f"{pasta_destino}/{arquivo}-GT-M2520")


                    print(exif)



    # image1 = Image.open('/media/ineps/BC2/HDMaxtor/samples/0016880.jpg')
    # image1.show()


if __name__ == '__main__':
    finder()


