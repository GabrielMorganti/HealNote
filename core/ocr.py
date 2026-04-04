from PIL import Image

try:
    import pytesseract
except ImportError:  # pragma: no cover - fallback for missing dependency
    pytesseract = None


def processar_receita(caminho_imagem):
    if pytesseract is None:
        return "OCR indisponivel: instale pytesseract e o Tesseract OCR no sistema."

    imagem = Image.open(caminho_imagem)
    texto = pytesseract.image_to_string(imagem)
    return texto.strip()
