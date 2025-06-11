# Reconhecimento de Dígitos Manuscritos em Tempo Real

**Autor:** Roan Ferreira de Sá

## Resumo do Projeto

Este projeto utiliza técnicas de Machine Learning e Visão Computacional para reconhecer dígitos manuscritos desenhados em uma interface gráfica, em tempo real. O modelo é treinado com o dataset MNIST e utiliza uma Rede Neural Convolucional (CNN) para classificar os dígitos desenhados pelo usuário.

## Tecnologias e Bibliotecas Utilizadas

- **Python 3.10+**: Linguagem principal do projeto
- **TensorFlow/Keras**: Criação, treinamento e inferência do modelo de rede neural
- **OpenCV (cv2)**: Processamento e pré-processamento de imagens
- **NumPy**: Manipulação de arrays e operações matemáticas
- **Pillow (PIL)**: Manipulação e captura de imagens
- **Pygame**: Interface gráfica para o usuário desenhar os dígitos
- **Matplotlib**: Visualização de dados e gráficos (opcional)

## Recursos do Projeto
- Treinamento de um modelo CNN com o dataset MNIST
- Interface gráfica para desenhar dígitos
- Pré-processamento avançado das imagens desenhadas
- Predição em tempo real do dígito desenhado
- Técnicas de data augmentation e callbacks para melhorar o treinamento
- Normalização dos dados para melhor desempenho do modelo

## Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd <nome-da-pasta-do-projeto>
```

### 2. Crie e ative um ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o programa principal
```bash
python3 main.py
```

- Na primeira execução, o modelo será treinado automaticamente (pode demorar alguns minutos).
- Após o treinamento, uma janela será aberta para você desenhar o dígito.
- Pressione **ENTER** para reconhecer o dígito desenhado.
- Pressione **C** para limpar a tela.
- Pressione **ESC** para sair.

## Estrutura do Projeto
```
reconhecimento_digitos/
├── requirements.txt
├── README.md
├── main.py
├── src/
│   ├── model/
│   │   ├── model.py
│   │   └── train_model.py
│   ├── utils/
│   │   └── image_processing.py
│   └── interface/
│       └── drawing_window.py
└── data/
    └── models/
```

## Explicação das Principais Tecnologias e Recursos

### TensorFlow/Keras
- Utilizado para criar e treinar a Rede Neural Convolucional (CNN) responsável pelo reconhecimento dos dígitos.
- O modelo possui camadas Conv2D, BatchNormalization, MaxPooling2D, Dropout e Dense.

### OpenCV
- Usado para pré-processar as imagens desenhadas, convertendo para escala de cinza, aplicando threshold e recortando o dígito.

### NumPy
- Manipulação eficiente de arrays e dados de imagem.

### Pillow (PIL)
- Utilizado para captura e manipulação de imagens, especialmente na função de captura de tela.

### Pygame
- Responsável pela interface gráfica onde o usuário pode desenhar os dígitos com o mouse.

### Matplotlib
- Opcional, pode ser usada para visualização de gráficos de desempenho do modelo.

## Observações
- O modelo é salvo em `data/models/mnist_model.h5` após o treinamento.
- O projeto pode ser facilmente expandido para reconhecer outros tipos de caracteres ou símbolos.
- O código segue boas práticas de organização e modularização.

---

Projeto desenvolvido por **Roan Ferreira de Sá**. # ML_Reconhecimento_de_Digitos
