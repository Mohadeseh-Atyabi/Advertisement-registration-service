from flask import Flask, render_template
from flask import request
from mongoDB import MongoDB
from abrArvan import AbrArvan
import rabbitPika
import os

app = Flask(__name__)
mongo = MongoDB()
abrarvan = AbrArvan()


@app.route('/', methods=['GET', 'POST'])
def handle():
    return "Hey! Welcome to my local host :)"


@app.route('/register', methods=['GET', 'POST'])
def handle_register():
    # Get information from the user
    email = str(request.args.get('email'))
    description = str(request.args.get('description'))
    image_path = str(request.args.get('image_path'))

    # Insert the email and description to the mongoDB
    id = mongo.insert(email, description)
    # Upload the image to the Abr Arvan
    abrarvan.upload(image_path, id)
    # Send the id to the RabbitPika queue
    rabbitPika.send(id)
    return "Your advertisement was registered with ID " + id


@app.route('/receive', methods=['GET', 'POST'])
def handle_receive():
    # Get information from the user
    id = request.args.get('id')
    # Fetch the data from mongoDB
    data = mongo.show(id)
    if data['state'] == 'Pending':
        return "Your advertisement is in the review queue"
    elif data['state'] == "Rejected":
        return "Your advertisement is rejected :("
    elif data['state'] == "Accepted":
        return show_advertisement(id, data)


def show_advertisement(id, data):
    IMG_FOLDER = os.path.join('static', 'IMG')
    app.config['UPLOAD_FOLDER'] = IMG_FOLDER
    Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], id + '.jpg')
    return render_template("index.html", user_image=Flask_Logo, description=data['description'], category=data['category'], state=data['state'])


if __name__ == "__main__":
    app.run(debug=True)