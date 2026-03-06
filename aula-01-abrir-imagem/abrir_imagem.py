from PIL import Image # Importa a biblioteca PIL para manipulação de imagens


caminho_imagem = "imagem.png" # Substitua pelo caminho da sua imagem

image = Image.open(caminho_imagem) # Abre a imagem usando PIL

print(image.getpixel((100, 100))) # Exibe o valor do pixel na posição (100, 100)
# Indicando pelo padrão R - RED | G - GREEN | B - BLUE a cor do pixel, 
# onde cada valor varia de 0 a 255, sendo 0 a ausência da cor e 255 a intensidade máxima da cor.

image.show() # Exibe a imagem em uma janela separada
