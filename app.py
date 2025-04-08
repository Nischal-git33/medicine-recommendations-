from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static')
CORS(app)

medicines = [
    # Paracetamol
    {
        "medicine_name": "Calpol",
        "composition": "Paracetamol",
        "uses": "Fever, Mild pain",
        "side_effects": "Allergic reactions",
        "image_url": "/static/images/calpol.jpg"
    },
    {
        "medicine_name": "Crocin",
        "composition": "Paracetamol",
        "uses": "Fever, Cold",
        "side_effects": "Liver damage in overdose",
        "image_url": "/static/images/crocin.jpg"
    },
    {
        "medicine_name": "Dolo 650",
        "composition": "Paracetamol",
        "uses": "Headache, Fever",
        "side_effects": "Rash, Liver problems",
        "image_url": "/static/images/dolo650.jpg"
    },
    {
        "medicine_name": "P 500",
        "composition": "Paracetamol",
        "uses": "Pain relief, Headache",
        "side_effects": "Stomach upset",
        "image_url": "/static/images/p500.jpg"
    },
    {
        "medicine_name": "Metacin",
        "composition": "Paracetamol",
        "uses": "Fever, Pain relief",
        "side_effects": "Dizziness",
        "image_url": "/static/images/metacin.jpg"
    },
    # Ibuprofen
    {
        "medicine_name": "Brufen",
        "composition": "Ibuprofen",
        "uses": "Inflammation, Pain relief",
        "side_effects": "Stomach upset, Dizziness",
        "image_url": "/static/images/brufen.jpg"
    },
    {
        "medicine_name": "Ibugesic",
        "composition": "Ibuprofen",
        "uses": "Pain relief, Fever",
        "side_effects": "Headache, Nausea",
        "image_url": "/static/images/ibugesic.jpg"
    },
    {
        "medicine_name": "Nurofen",
        "composition": "Ibuprofen",
        "uses": "Pain relief, Fever",
        "side_effects": "Nausea, Vomiting",
        "image_url": "/static/images/nurofen.jpg"
    },
    {
        "medicine_name": "Advil",
        "composition": "Ibuprofen",
        "uses": "Pain relief, Headache",
        "side_effects": "Stomach upset",
        "image_url": "/static/images/advil.jpg"
    },
    {
        "medicine_name": "Motrin",
        "composition": "Ibuprofen",
        "uses": "Pain relief, Inflammation",
        "side_effects": "Dizziness, Stomach cramps",
        "image_url": "/static/images/motrin.jpg"
    },
    # Amoxicillin
    {
        "medicine_name": "Mox",
        "composition": "Amoxicillin",
        "uses": "Bacterial infections",
        "side_effects": "Diarrhea, Skin rash",
        "image_url": "/static/images/mox.jpg"
    },
    {
        "medicine_name": "Amoxil",
        "composition": "Amoxicillin",
        "uses": "Bacterial infections",
        "side_effects": "Rashes, Nausea",
        "image_url": "/static/images/amoxil.jpg"
    },
    {
        "medicine_name": "Trimox",
        "composition": "Amoxicillin",
        "uses": "Antibiotic for bacterial infections",
        "side_effects": "Nausea, Vomiting",
        "image_url": "/static/images/trimox.jpg"
    },
    {
        "medicine_name": "Amox",
        "composition": "Amoxicillin",
        "uses": "Bacterial infections",
        "side_effects": "Diarrhea, Allergic reactions",
        "image_url": "/static/images/amox.jpg"
    },
    {
        "medicine_name": "Almox",
        "composition": "Amoxicillin",
        "uses": "Infections",
        "side_effects": "Skin rash, Nausea",
        "image_url": "/static/images/almox.jpg"
    },
    # Azithromycin
    {
        "medicine_name": "Zithromax",
        "composition": "Azithromycin",
        "uses": "Bacterial infections",
        "side_effects": "Nausea, Vomiting",
        "image_url": "/static/images/zithromax.jpg"
    },
    {
        "medicine_name": "Azax",
        "composition": "Azithromycin",
        "uses": "Respiratory infections",
        "side_effects": "Diarrhea, Stomach pain",
        "image_url": "/static/images/azax.jpg"
    },
    {
        "medicine_name": "Azee",
        "composition": "Azithromycin",
        "uses": "Infections, Pneumonia",
        "side_effects": "Headache, Rash",
        "image_url": "/static/images/azee.jpg"
    },
    {
        "medicine_name": "Z-Pack",
        "composition": "Azithromycin",
        "uses": "Upper respiratory infections",
        "side_effects": "Nausea, Diarrhea",
        "image_url": "/static/images/zpack.jpg"
    },
    {
        "medicine_name": "Azithral",
        "composition": "Azithromycin",
        "uses": "Antibiotic",
        "side_effects": "Stomach upset",
        "image_url": "/static/images/azithral.jpg"
    },
    # Ciprofloxacin
    {
        "medicine_name": "Ciplox",
        "composition": "Ciprofloxacin",
        "uses": "Bacterial infections",
        "side_effects": "Nausea, Diarrhea",
        "image_url": "/static/images/ciplox.jpg"
    },
    {
        "medicine_name": "Cipro",
        "composition": "Ciprofloxacin",
        "uses": "Infections",
        "side_effects": "Dizziness, Diarrhea",
        "image_url": "/static/images/cipro.jpg"
    },
    {
        "medicine_name": "Ciprobid",
        "composition": "Ciprofloxacin",
        "uses": "Bacterial infections",
        "side_effects": "Nausea, Vomiting",
        "image_url": "/static/images/ciprobid.jpg"
    },
    {
        "medicine_name": "Ciprodar",
        "composition": "Ciprofloxacin",
        "uses": "Infections",
        "side_effects": "Nausea, Headache",
        "image_url": "/static/images/ciprodar.jpg"
    },
    {
        "medicine_name": "Cifran",
        "composition": "Ciprofloxacin",
        "uses": "Bacterial infections",
        "side_effects": "Rash, Stomach upset",
        "image_url": "/static/images/cifran.jpg"
    }
]

@app.route("/medicines")
def get_medicines():
    return jsonify(medicines)

if __name__ == "__main__":
    app.run(debug=True)