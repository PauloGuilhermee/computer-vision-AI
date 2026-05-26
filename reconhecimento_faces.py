import face_recognition
import cv2
import os

# Caminho absoluto da pasta onde estão os rostos
CAMINHO_BASE = r"C:\Users\paulo\OneDrive\Área de Trabalho\ia reconhecimento de gesto\rostos_conhecidos"

rostos_conhecidos = []
nomes_conhecidos = []

# Percorrer todas as subpastas
for pessoa in os.listdir(CAMINHO_BASE):
    caminho_pessoa = os.path.join(CAMINHO_BASE, pessoa)

    if os.path.isdir(caminho_pessoa):
        for arquivo in os.listdir(caminho_pessoa):
            if arquivo.lower().endswith((".jpg", ".png", ".jpeg")):
                caminho_imagem = os.path.join(caminho_pessoa, arquivo)
                imagem = face_recognition.load_image_file(caminho_imagem)
                codificacoes = face_recognition.face_encodings(imagem)

                if codificacoes:
                    rosto = codificacoes[0]
                    rostos_conhecidos.append(rosto)
                    nomes_conhecidos.append(pessoa)
                    print(f"[✔] Rosto carregado: {pessoa} ({arquivo})")
                else:
                    print(f"[⚠] Nenhum rosto detectado em: {arquivo}")

# Captura da webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    pequeno = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(pequeno, cv2.COLOR_BGR2RGB)

    locais_rostos = face_recognition.face_locations(rgb)
    codigos_rostos = face_recognition.face_encodings(rgb, locais_rostos)

    for rosto, local in zip(codigos_rostos, locais_rostos):
        comparacoes = face_recognition.compare_faces(rostos_conhecidos, rosto)
        nome = "Desconhecido"

        if True in comparacoes:
            indice = comparacoes.index(True)
            nome = nomes_conhecidos[indice]

        top, right, bottom, left = [v * 4 for v in local]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Reconhecimento Facial", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
