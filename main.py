import cv2
cap = cv2.VideoCapture('./la_cabra.mp4')

i = 0
faces = []
while(cap.isOpened()):
    ret, frame = cap.read()
    classificador = cv2.CascadeClassifier('./haarcascade_frontalcatface.xml')


   
    if ret == False:
        break



    img = frame
    faces = classificador.detectMultiScale(img, scaleFactor = 1.1, minNeighbors=3)
    img_saida = img.copy()
    for face in faces:
        pos_x, pos_y, largura, altura = face
        frame_aux = cv2.rectangle(img_saida, (pos_x,pos_y), (pos_x+largura, pos_y+altura), color=(200,0,158), thickness=3)
        
        # Save Frame by Frame into disk using imwrite method
        cv2.imwrite('Frame'+str(i)+'.jpeg', frame_aux)
      
        height, width, layers = frame_aux.shape

        fps = 30  # Aumenta o FPS para 30 para aumentar a velocidade do vídeo
        video = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        for image in frame_aux:
            video.write(image)

    i += 1


video.release()
cap.release()
cv2.destroyAllWindows()