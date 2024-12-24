from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from flask_cors import CORS 



app = Flask(__name__)

# Enabling CORS for all routes
CORS(app)

# Loading the Hugging Face BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Allowing file extensions for uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Checking if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Generating caption from image
def generate_caption(image_path):
    raw_image = Image.open(image_path).convert("RGB")
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Routing for uploading an image and generating a caption
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        # Saving the uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        file.save(file_path)
        
        # Generating and return caption
        caption = generate_caption(file_path)
        return jsonify({"caption": caption})
    else:
        return jsonify({"error": "Invalid file type"}), 400

if __name__ == "__main__":
    # Ensuring the uploads folder exists
    os.makedirs('uploads', exist_ok=True)
    
    # Running the Flask app locally
    app.run(debug=True)
