from PIL import Image
import os

# Configurações globais
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

# Garantir que a pasta de saída exista
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def criar_imagem_cor_solida(largura, altura, cor, nome_arquivo):
    img = Image.new("RGB", (largura, altura), color=cor)
    img.save(os.path.join(OUTPUT_FOLDER, nome_arquivo))
    print(f"Imagem {nome_arquivo} salva com sucesso.")
    return img

def criar_padrao_triangular(tamanho):
    img = Image.new("RGB", (tamanho, tamanho), "white")
    pixels = img.load()  # Carrega os dados para acesso rápido

    for x in range(tamanho):
        for y in range(tamanho):
            if y > x:
                pixels[x, y] = (0, 0, 0)
    
    return img

if __name__ == "__main__":
    solido = criar_imagem_cor_solida(400, 400, "red", "fundo_vermelho.png")
    soli.save(os.path.join(OUTPUT_FOLDER, "fundo_vermelho.png"))
    solido.show()
    
    tri = criar_padrao_triangular(500)
    tri.save(os.path.join(OUTPUT_FOLDER, "triangulo.png"))
    tri.show()