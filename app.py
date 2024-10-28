from flask import Flask, render_template
import json

app = Flask(__name__)

listofpizza = [{
    "name": "Маргарита",
    "description": "Сир Моцарела, томати, базилік",
    "price": "150 грн",
    "image_url": "https://i0.wp.com/caponepizza.kiev.ua/wp-content/uploads/2023/03/img_2179.jpeg?fit=770%2C798&ssl=1"
},
{
    "name": "Пепероні",
    "description": "Пепероні, сир, соус",
    "price": "170 грн",
    "image_url": 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPlQMFVqLJq0OnnLMYvVRVkqf0Yh2TxqvGbg&s'
},
{
    "name": "Гавайська",
    "description": "Курка, ананас, сир",
    "price": "180 грн",
    "image_url": "https://artpizza.com.ua/media/cache/25/2e/252e2761c12cf233874ad2b236fe3d0a.jpg"
}]
@app.route("/")
def hello_world():
    return "Welcome to our pizzeria!"

@app.route('/main/')
def mainpage():
    return render_template('index.html')

@app.get("/menu/")
def menu():
    context = {
        "title": "Menu",
        "menu": listofpizza
    }
    return render_template('menu.html', **context)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

    #static for CCS and image
    #templates for html