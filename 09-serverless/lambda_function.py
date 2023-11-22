import tflite_runtime.interpreter as tflite
import preprocessing


interpreter = tflite.Interpreter(model_path='bees-wasps-v2.tflite')
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


def predict(url):
    img = preprocessing.download_image(url)
    img = preprocessing.prepare_image(img, (150, 150))
    X = preprocessing.preprocess_input(img)
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    return preds


def lambda_handler(event, context):
    url = event['url']
    result = predict(url).tolist()
    return result