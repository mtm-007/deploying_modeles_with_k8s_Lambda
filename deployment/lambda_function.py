import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

Interpreter = tflite.Interpreter(model_path="fashion_model.tflite")
Interpreter.allocate_tensors()

input_index = Interpreter.get_input_details()[0]['index']
output_index = Interpreter.get_output_details()[0]['index']

preprocessor = create_preprocessor('xception', target_size=(299,299))

#url = 'http://bit.ly/mlbookcamp-pants'
#X = preprocessor.from_url(url)

classes = [
    'dress',
     'hat',
     'longsleeve',
     'outwear',
     'pants',
     'shirt',
     'shoes',
     'shorts',
     'skirt',
     't-shirt',]

def predict(url):
    X = preprocessor.from_url(url)

    Interpreter.set_tensor(input_index, X)
    Interpreter.invoke()
    preds = Interpreter.get_tensor(output_index)
    float_predictions = preds[0].tolist()
    return dict(zip(classes,float_predictions ))

def lambda_handler(event, context):
    url = event['url']
    results = predict(url)
    return results










