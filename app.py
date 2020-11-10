from flask import Flask, jsonify, request
import pickle


app = Flask(__name__)
app.config['DEBUG'] = True


def predict_sentiment(text):
    model = pickle.load(open('sentiment.pk','rb'))
    result = model.predict([text])
    if result[0] == 1:
        return 'Positive'
    else:
        return 'Negtive'


@app.route('/',methods = ['GET'])
def home():
    return jsonify("test")

@app.route('/sentiment',methods= ['POST'])
def sentiment():
    data = request.json
    text = data['text']
    result = predict_sentiment(text)
    return jsonify({'text':text,'sentiment':result})

if __name__ == "__main__":
    app.run(debug=True)