# Computer Vision AI

Projeto experimental em Python voltado ao estudo de **visão computacional**, com foco em reconhecimento facial e reconhecimento de gestos em tempo real utilizando webcam.

O objetivo do projeto é praticar conceitos de inteligência artificial aplicada, processamento de imagem e identificação de padrões visuais por meio de bibliotecas como **OpenCV**, **MediaPipe** e **face_recognition**.

---

## Visão geral

Este repositório reúne protótipos simples de visão computacional desenvolvidos para fins de estudo e prática.

Atualmente, o projeto possui dois módulos principais:

- Reconhecimento facial em tempo real;
- Reconhecimento de gestos manuais em tempo real.

Ambos utilizam a webcam do computador para capturar imagens, processar os frames e exibir o resultado visualmente na tela.

---

## Funcionalidades

### Reconhecimento facial

O script de reconhecimento facial realiza as seguintes etapas:

- Carrega imagens de rostos conhecidos a partir de uma pasta local;
- Gera codificações faciais para cada pessoa cadastrada;
- Captura vídeo em tempo real pela webcam;
- Detecta rostos no frame;
- Compara os rostos detectados com a base local;
- Exibe o nome da pessoa reconhecida na tela;
- Marca o rosto identificado com um retângulo visual.

### Reconhecimento de gestos

O script de reconhecimento de gestos realiza as seguintes etapas:

- Captura vídeo em tempo real pela webcam;
- Detecta a mão utilizando MediaPipe Hands;
- Identifica os pontos de referência da mão;
- Verifica quais dedos estão levantados;
- Classifica gestos simples, como:
  - Punho fechado;
  - Mão aberta;
  - Joinha;
  - Hang loose;
  - Quantidade de dedos levantados.

---

## Tecnologias utilizadas

- Python
- OpenCV
- MediaPipe
- face_recognition
- Webcam / captura de vídeo em tempo real

---

## Estrutura do projeto

```txt
computer-vision-AI/
  reconhecimento_faces.py
  reconhecimentos_gestos.py
  .gitignore
  README.md
