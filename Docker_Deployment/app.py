import flask
from flask import request, jsonify
from flask_cors import CORS
app = flask.Flask(__name__)
CORS(app)

import spacy
nlp = spacy.load("en_core_web_sm")

# sample_text = "Apple is looking at buying U.K. startup for $1 billion"
def identify_entities(txt):
    out ={}
    entities_array=[]
    doc = nlp(txt)

    for ent in doc.ents:
        entity={}
        entity['text']=ent.text
        entity['start_char'] = str(ent.start_char)
        entity['end_char'] = str(ent.end_char)
        entity['label_'] = ent.label_
        entities_array.append(entity)

    out['entities'] = entities_array
    print (out)

    return out


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Get entities for a sentence</h1>
    <p> Call with post request { "text": "sentence"} </p>'''

@app.route('/getentities', methods=['GET', 'POST'])
def get_entities():
    if request.method == 'POST':
        data = request.get_json()
        text = data["text"]
        text=text.strip()
        print("text ", text)
        output = identify_entities(text)
    else:
        return "Error: No text field provided. Please specify a text."

    return jsonify(output)


if __name__ == '__main__':
    # app.run(host="0.0.0.0", debug=False)
    app.run(host='0.0.0.0', debug=False, port=80)
