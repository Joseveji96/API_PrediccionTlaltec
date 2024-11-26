import cv2
import numpy as np
from flask import Flask, jsonify, request
from ultralytics import YOLO
import base64

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 

# Cargar el modelo YOLO
model = YOLO("./models/TlalTec2.pt")

# Lista de las plagas que detecta el modelo
etiquetas_plagas = ["sano", "quemado", "rona", "trips", "anillamiento"]

@app.route('/detect_plagas', methods=['POST'])
def detect_plagas():
    try:
        # Leer la imagen en formato base64 desde la solicitud
        data = request.json
        base64_image = data.get('image')
        if not base64_image:
            return jsonify({'error': 'No se proporcionó ninguna imagen'}), 400
        
        image_bytes = base64.b64decode(base64_image)
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)

        # Decodificar el array en una imagen OpenCV
        frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        if frame is None:
            return jsonify({'error': 'No se pudo decodificar la imagen'}), 400

        # Redimensionar la imagen a 640x640
        frame = cv2.resize(frame, (640, 640))

        # Realizar la detección
        results = model.predict(frame, conf=0.3)

        # Verificar si se detectaron objetos
        results_with_confidence = []
        if results:
            for result in results:
                detections = []
                if hasattr(result, 'boxes') and len(result.boxes) > 0:
                    for box in result.boxes.numpy():
                        # Obtener la clase detectada y la confianza
                        clase_detectada = etiquetas_plagas[int(box.cls[0])]
                        confianza = float(box.conf[0])
                        detections.append({
                            "plaga": clase_detectada,
                            "confianza": confianza
                        })
                    results_with_confidence.append(detections)
        
        if results_with_confidence:
            # Anotar la imagen con las detecciones
            annotated_frame = results[0].plot()
            _, img_encoded = cv2.imencode('.jpg', annotated_frame)
            response = img_encoded.tobytes()

            # Devolver la imagen detectada y los resultados como respuesta
            return jsonify({
                'plagas_detectadas': results_with_confidence,
                'imagen': base64.b64encode(response).decode('utf-8')
            }), 200
        else:
            return jsonify({'message': 'No se detectaron plagas en la imagen'}), 200

    except Exception as e:
        print('Error en el servidor:', e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
