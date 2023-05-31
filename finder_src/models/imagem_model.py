import os
from PIL import Image, ExifTags

from finder_src.models.arquivo_model import ArquivoModel


class ImagemModel(ArquivoModel):

    def __init__(self, caminho, nome, extensao, exif, dimensoes: tuple):
        super().__init__(caminho, nome, extensao)
        self.exif = exif
        self.dimensoes = dimensoes

    def exif_extrator(self, exif, caminho):
        imagem = Image.open(f"{caminho}")
        exif_arquivo = imagem._getexif()
        imagem_tamanho = imagem._size
        if exif:
            for tag, valor in exif.items():
                if tag in ExifTags.TAGS:
                    nm_tag = ExifTags.TAGS[tag]
                    exif[nm_tag] = valor

        return imagem_tamanho, exif, caminho


imagem = ImagemModel
