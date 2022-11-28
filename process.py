import cv2
from tensorflow import keras
import numpy as np

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
model = keras.models.load_model('content/mask_recog_ver2.h5')

def face_mask_detector(frame):
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = faceCascade.detectMultiScale(gray,
                                        scaleFactor = 1.1,
                                        minNeighbors = 5,
                                        minSize = (60, 60),
                                        flags = cv2.CASCADE_SCALE_IMAGE)
  faces_list = []
  preds = []

  for (x, y, w, h) in faces:
      face_frame = frame[y:y + h, x:x + w]
      face_frame = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)
      face_frame = cv2.resize(face_frame, (224, 224))
      face_frame = keras.preprocessing.image.img_to_array(face_frame)
      face_frame = np.expand_dims(face_frame, axis = 0)
      face_frame = keras.applications.mobilenet_v2.preprocess_input(face_frame)
      faces_list.append(face_frame)

      if len(faces_list) > 0:
          preds = model.predict(faces_list)

      for pred in preds:
          (mask, withoutMask) = pred

      label = "Mask" if mask > withoutMask else "No Mask"
      color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
      label = "{}: {}%".format(label, int(max(mask, withoutMask) * 100))
      cv2.putText(frame, label, (x, y - 10),
                  cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
      cv2.rectangle(frame, (x, y), (x + w, y + h),color, 3)
  return frame


def worker():
    input_image = cv2.imread('C:/Users/laisbel/PycharmProjects/facemaskrecog/content/image.jpg')
    output = face_mask_detector(input_image)
    # path = 'C:/Users/laisbel/PycharmProjects/facemaskrecog/content/test.jpg'
    cv2.imwrite('C:/Users/laisbel/PycharmProjects/facemaskrecog/content/test.jpg', output)
