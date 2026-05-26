import cv2
import mediapipe as mp

# Inicializa o MediaPipe Hands
mp_maos = mp.solutions.hands
maos = mp_maos.Hands(max_num_hands=1)
mp_desenho = mp.solutions.drawing_utils

# Nomes dos dedos
nomes_dedos = ["Polegar", "Indicador", "Medio", "Anelar", "Mindinho"]

# Função para verificar se o dedo está levantado
def dedo_levantado(pontos, id_dedo):
    ponta = pontos[id_dedo]
    base = pontos[id_dedo - 2]
    return ponta.y < base.y  # Quanto menor o y, mais "alto" na imagem

# Função especial para o polegar (posição horizontal, não vertical)
def polegar_levantado(pontos):
    return pontos[4].x < pontos[3].x if pontos[4].y < pontos[3].y else pontos[4].x > pontos[3].x

# Inicia a captura da webcam
cap = cv2.VideoCapture(0)

while True:
    sucesso, frame = cap.read()
    if not sucesso:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = maos.process(frame_rgb)
    texto = "Nenhum gesto"

    if resultado.multi_hand_landmarks:
        for mao in resultado.multi_hand_landmarks:
            mp_desenho.draw_landmarks(frame, mao, mp_maos.HAND_CONNECTIONS)
            pontos = mao.landmark

            # Verifica dedo por dedo
            dedos = []
            dedos.append(polegar_levantado(pontos))        # Polegar
            dedos.append(dedo_levantado(pontos, 8))        # Indicador
            dedos.append(dedo_levantado(pontos, 12))       # Médio
            dedos.append(dedo_levantado(pontos, 16))       # Anelar
            dedos.append(dedo_levantado(pontos, 20))       # Mindinho

            # Conta os dedos levantados
            total_levantados = dedos.count(True)

            # Verifica gestos específicos
            if total_levantados == 0:
                texto = "Punho fechado"
            elif total_levantados == 5:
                texto = "Mao aberta"
            elif dedos == [True, False, False, False, False]:
                texto = "Joinha"
            elif dedos == [True, False, False, False, True]:
                texto = "Hang loose"
            else:
                texto = f"{total_levantados} dedo(s): " + ", ".join(
                    nome for nome, levantado in zip(nomes_dedos, dedos) if levantado
                )

    # Mostra o gesto e o vídeo
    cv2.putText(frame, texto, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    cv2.imshow("Reconhecimento de Gestos", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC para sair
        break

cap.release()
cv2.destroyAllWindows()

