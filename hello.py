from flask import Flask , render_template

#create a flask isnstance 
app = Flask(__name__)

#create a route decorator 
@app.route('/')
def indext():
    first_name = "John"
    stuff = "This is <strong>Bold</strong>"
    favorite_pizza = ['Pepperoni' , "Cheese" ,"Mashrooms" , 41]
    return render_template('index.html',first_name=first_name , 
                            stuff = stuff , favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def usr(name):
    return render_template('user.html' , user_name =name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html' ) ,404

