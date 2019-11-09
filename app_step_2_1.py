import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

out ={}
entities_array=[]

for ent in doc.ents:
    entity={}
    entity['text']=ent.text
    entity['start_char'] = str(ent.start_char)
    entity['end_char'] = str(ent.end_char)
    entity['label_'] = ent.label_
    entities_array.append(entity)
    # print(ent.text, ent.start_char, ent.end_char, ent.label_)

out['entities'] = entities_array

print (out)