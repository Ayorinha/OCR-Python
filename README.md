Descrição do Projeto:
OCR com Tesseract e Python para Extração de Texto de Imagens (PNG/JPG)

Este projeto utiliza o Tesseract OCR e a biblioteca OpenCV para realizar a extração de texto de imagens. A aplicação é projetada para converter uma imagem (ex: JPG) em texto, realizando pré-processamento da imagem para melhorar a precisão do OCR, e salvando o texto extraído em um documento do tipo .docx.

Principais Funcionalidades:
Carregamento de imagem local para extração de texto.

Pré-processamento da imagem (escala de cinza, redimensionamento, suavização e limiarização).

Configuração personalizada para o Tesseract OCR para melhorar a acuracidade.

Geração de arquivo Word (.docx) com o texto extraído.

Exibição do texto extraído no console.

Armazenamento de uma imagem de debug com a imagem pré-processada.

Tecnologias Utilizadas:
Python: Linguagem de programação para manipulação de imagem e execução do OCR.

Tesseract OCR: Ferramenta para extração de texto a partir de imagens.

OpenCV: Biblioteca para manipulação e pré-processamento de imagens.

python-docx: Para salvar o resultado em um arquivo Word.

Como Funciona:
O código carrega a imagem do caminho especificado.

A imagem é convertida para escala de cinza, redimensionada e suavizada.

É aplicada a limiarização de Otsu para melhorar a definição do texto.

O Tesseract OCR é executado para extrair o texto da imagem.

O texto extraído é salvo em um arquivo .docx com a data e hora no nome do arquivo.

O texto extraído também é exibido no console.

Pré-requisitos:
Python 3.x

Tesseract OCR instalado e configurado corretamente.

Bibliotecas necessárias: cv2, pytesseract, os, docx, datetime.

Para instalar as dependências, use:

bash
Copiar
Editar
pip install opencv-python pytesseract python-docx
Instruções de Uso:
Certifique-se de que o Tesseract OCR esteja instalado corretamente no seu sistema.

Ajuste o caminho da imagem no código conforme necessário.

Execute o script Python e o texto extraído será salvo automaticamente em um arquivo .docx na área de trabalho.

Objetivo:
Este código pode ser utilizado para sistemas de automação de digitalização de documentos, especialmente útil em ambientes administrativos, jurídicos e em processos que necessitam de extração de texto a partir de imagens escaneadas ou fotografadas.

