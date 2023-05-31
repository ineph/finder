import os
from PIL import Image, ExifTags

from finder_src.models.arquivo_model import ArquivoModel


class ImagemModel(ArquivoModel):

    def __init__(self, caminho, nome, extensao):
        super().__init__(caminho, nome, extensao)
        imagem = Image.open(f"{caminho}")
        exif_cru = imagem._getexif()
        self.dimensoes = imagem._size
        self.caminho_completo = caminho
        self.nome = nome
        self.extensao = extensao
        self.nome_completo = f'{self.nome}{self.extensao}'
        self.exif = dict()
        if exif_cru:
            _exif = dict()
            for tag, valor in exif_cru.items():
                if tag in ExifTags.TAGS:
                    nm_tag = ExifTags.TAGS[tag]
                    _exif[nm_tag] = valor
            self.exif = _exif


imagem = ImagemModel
