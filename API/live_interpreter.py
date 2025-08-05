import cv2
import numpy as np
import tensorflow as tf
from collections import deque
from flask import Flask, Response

# Load base (non-streaming) TFLite model
models_path = "../Models/model_3_b30.tflite"
interpreter = tf.lite.Interpreter(model_path=models_path)
interpreter.allocate_tensors()
runner = interpreter.get_signature_runner()

# Input shape info
input_details = runner.get_input_details()
input_shape = input_details['image']['shape']  # [1, 13, height, width, 3]
input_height = input_shape[2]
input_width = input_shape[3]
clip_len = int(input_shape[1])

# Class labels
class_names = [
    'Dog everything', 'Emergency Stop', 'Extend boom', 'Hoist', 'Lower',
    'Lower boom', 'Lower boom and hoist loads', 'Move slowly', 'Raise boom',
    'Raise boom and lower loads', 'Retract boom', 'Travel',
    'Travel Both tracks', 'Travel only left track', 'Travel only right track',
    'Use Auxiliary Hoist', 'Use Main Hoist', 'stop', 'swing boom left',
    'swing boom right'
]

# Get top-k predictions
def get_top_k(probs, k=5):
    top_predictions = tf.argsort(probs, direction='DESCENDING')[:k]
    top_labels = [class_names[i] for i in top_predictions.numpy()]
    top_probs = probs.numpy()[top_predictions]
    return list(zip(top_labels, top_probs))

# Flask app
app = Flask(__name__)

@app.route('/video_feed')
def video_feed():
    cap = cv2.VideoCapture(0)
    frame_buffer = deque(maxlen=clip_len)

    def gen():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Preprocess frame
            resized = cv2.resize(frame, (input_width, input_height))
            normalized = resized.astype(np.float32) / 255.0
            frame_buffer.append(normalized)

            if len(frame_buffer) < clip_len:
                continue

            # Create clip and run model
            clip = np.expand_dims(np.array(frame_buffer), axis=0).astype(np.float32)  # (1, 13, H, W, 3)
            outputs = runner(image=clip)
            logits = outputs['classifier_head_1'][0]

            # Decode and draw predictions
            probs = tf.nn.softmax(logits)
            top_k = get_top_k(probs)

            for i, (label, prob) in enumerate(top_k):
                text = f"{label}: {prob:.2f}"
                y = 30 + i * 30
                cv2.putText(frame, text, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Encode to JPEG and stream
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        cap.release()

    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return '''
    <html>
      <head><title>Live Crane Interpreter</title></head>
      <body>
        <h1>🕵️ Live Crane Interpreter</h1>
        <img src="/video_feed" width="640" height="480" />
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
