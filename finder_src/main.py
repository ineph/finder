import os
import shutil
from finder_src import config as env

from finder_src.models.imagem_model import ImagemModel

# TODO: adicionar mais extensões (imagens, videos, musicas, texto simples)
# TODO: depois, adicionar extensões como parâmetros em console
imagens_extensoes = ['.jpg', '.png', '.jpeg']
resolucoes = [
    (800, 600),
    (600, 800),
    (1024, 768)
]
modelos = [
    'GT-M2520',
    'DSC-P200',
    'DSC-W110',
    'C261'
]
excecoes = ['f0019952.jpg', 'f0005568.jpg', 'f0020288.jpg']


def mergulhador(caminho):
    contador = 0
    for raiz, pastas, arquivos in os.walk(caminho):
        if pastas:
            for pasta in pastas:
                mergulhador(os.path.join(caminho, pasta))
        else:
            for arquivo in arquivos:
                arquivo_nome, arquivo_extensao = os.path.splitext(arquivo)
                if arquivo_extensao in imagens_extensoes:
                    # TODO: remover esse contador tosco depois de resolver o problema do último loop
                    contador += 1
                    if contador == 80:
                        print('s')
                    imagem = ImagemModel(os.path.join(caminho, arquivo), arquivo_nome, arquivo_extensao)
                    if imagem_validador(imagem):
                        print(contador)
    return True


def imagem_validador(arquivo: ImagemModel):
    if arquivo.dimensoes in resolucoes or arquivo.exif.get('Model') in modelos or arquivo.nome_completo in excecoes:
        with open('output_arquivos.txt', 'a') as f:
            print(arquivo.nome_completo, file=f)
        # TODO: previnir erros de exif quando imagem coletada por dimensões
        return arquivo_criador(
            env.OUTPUT_PATH,
            os.path.split(arquivo.caminho)[0],
            arquivo.exif.get('Model') if arquivo.exif.get('Model') else f'{arquivo.dimensoes[0]}x{arquivo.dimensoes[1]}',
            arquivo.nome_completo
        )


# TODO: migrar esta lógica para classe de arquivo
def arquivo_criador(pasta_output, pasta_input, pasta_nome, nm_arquivo):
    try:
        if not os.path.exists(os.path.join(pasta_output, pasta_nome)):
            os.makedirs(os.path.join(pasta_output, pasta_nome))

        shutil.copy2(os.path.join(pasta_input, nm_arquivo), os.path.join(pasta_output, pasta_nome, nm_arquivo))
        return True
    except Exception as e:
        print(e)


def finder():
    # TODO: adicionar mais extensões (imagens, videos, musicas, texto simples)
    input_pasta = env.INPUT_PATH

    mergulhador(input_pasta)


if __name__ == '__main__':
    finder()
