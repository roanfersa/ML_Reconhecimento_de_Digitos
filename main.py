import tensorflow as tf
import numpy as np
import os
from src.model.model import create_model
from src.utils.image_processing import preprocess_image
from src.interface.drawing_window import DrawingWindow

def main():
    # Verifica se o modelo existe, se não, treina um novo
    if not os.path.exists('data/models/mnist_model.h5'):
        print("Modelo não encontrado. Treinando novo modelo...")
        from src.model.train_model import train_mnist_model
        train_mnist_model()
    
    # Carrega o modelo MNIST pré-treinado
    model = tf.keras.models.load_model('data/models/mnist_model.h5')
    
    # Inicializa a janela de desenho
    window = DrawingWindow()
    
    print("Instruções:")
    print("- Desenhe um dígito na janela")
    print("- Pressione ENTER para reconhecer o dígito")
    print("- Pressione C para limpar a tela")
    print("- Pressione ESC para sair")
    
    while True:
        # Captura o desenho do usuário
        image = window.draw()
        if image is None:
            break
            
        # Pré-processa a imagem
        processed_image = preprocess_image(image)
        
        # Faz a predição
        prediction = model.predict(processed_image)
        digit = np.argmax(prediction)
        confidence = prediction[0][digit] * 100
        
        print(f"Dígito reconhecido: {digit} (Confiança: {confidence:.2f}%)")

if __name__ == "__main__":
    main() 