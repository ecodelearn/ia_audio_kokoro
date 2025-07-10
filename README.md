# Projeto de Conversão de Texto em Fala

Este projeto é uma aplicação Python que converte texto em fala utilizando a biblioteca Kokoro.

## Funcionalidades

- Conversão de texto em fala com diferentes vozes.
- Geração de arquivos de áudio a partir do texto fornecido.

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para usar a função de conversão de texto em fala, você pode chamar a função `text_to_speech`:

```python
from kokoro import KPipeline

text_to_speech("Seu texto aqui", "voz_desejada", "caminho/do/audio.wav")
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias e correções. Faça um fork do repositório e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License.