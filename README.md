# OCR-Python

> OCR de imagens com Python, Tesseract e OpenCV, com pré-processamento e exportação do texto extraído para `.docx`.

## Visão geral

Projeto de engenharia de OCR para transformar imagens PNG/JPG em texto pesquisável. O fluxo aplica pré-processamento da imagem antes da leitura pelo Tesseract e gera um documento Word com o resultado.

## Funcionalidades

- Carregamento de imagens locais (PNG/JPG).
- Conversão para escala de cinza.
- Redimensionamento e suavização.
- Limiarização de Otsu para realce do texto.
- Extração de texto com Tesseract OCR.
- Exibição do resultado no console.
- Exportação para `.docx`.
- Geração opcional de imagem pré-processada para inspeção/debug.

## Arquitetura do fluxo

```text
Imagem
  ↓
OpenCV / Pré-processamento
  ↓
Tesseract OCR
  ↓
Texto extraído
  ├── Console
  └── Documento .docx
```

## Stack

- Python 3.x
- OpenCV
- Tesseract OCR
- pytesseract
- python-docx

## Instalação

Crie um ambiente virtual e instale as dependências:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

O executável do Tesseract também precisa estar instalado no sistema. Em instalações Windows, configure o caminho do executável no código/configuração do projeto quando necessário.

## Uso

O código original deste repositório foi desenvolvido para receber o caminho de uma imagem, executar o pipeline de OCR e gerar um `.docx`. Antes de executar, utilize uma imagem de exemplo e ajuste a entrada conforme a implementação local.

## Dados e privacidade

Não inclua documentos reais, documentos pessoais, credenciais, chaves de API ou dados institucionais neste repositório. Para demonstrações públicas, utilize somente arquivos sintéticos ou autorizados.

## Evolução recomendada

- Separar o pipeline em módulos de entrada, pré-processamento, OCR e exportação.
- Tornar parâmetros de OCR configuráveis.
- Adicionar testes automatizados.
- Adicionar métricas de qualidade, como CER/WER, usando conjuntos de teste sintéticos.
- Adicionar processamento em lote.
- Evoluir para Document Intelligence com extração estruturada e validação de campos.

## Autor

**Anderson Leon Ayora**  
Data Scientist | AI Engineer | Data Architect

Foco: Applied AI, Document Intelligence, OCR, Intelligent Automation e Data Engineering.
