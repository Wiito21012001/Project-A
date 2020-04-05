from flask import *
from time import ctime

import pyrebase

config = {
    "apiKey": "AIzaSyDswJaV5gPgskgeILjNICTGLPv0_sMc_Wg",
    "authDomain": "application-testing01.firebaseapp.com",
    "databaseURL": "https://application-testing01.firebaseio.com",
    "projectId": "application-testing01",
    "storageBucket": "application-testing01.appspot.com",
    "messagingSenderId": "297615807434",
    "appId": "1:297615807434:web:8638ed5292ee8c88127533",
    "measurementId": "G-9WESBP4QKE"
}

firebase = pyrebase.initialize_app(config)


db = firebase.database()

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def Home():
    return render_template('RemakeMainPage.html')


@app.route('/TransactionsHistory')
def TransactionsPage():
    Transactions_Data = db.child('Transactions_Data').get().val().items()
    
    return render_template('RemakeTransactionsHistoryPage.html', Transactions_Data=Transactions_Data)


@app.route('/CardsList')
def CardsPage():
    Card_Data = db.child('Card_Data').get().val().items()
    
    return render_template('RemakeCardsListPage.html', Card_Data=Card_Data)


@app.route('/AddingTransactions', methods=['GET','POST'])
def AddingTransactionsPage():
    if request.method == 'POST':
        # print(request.form)
        Category = request.form['Category']
        Emojis = request.form['Emojis']
        Items = request.form['Items']
        Date = request.form['Date']
        Price = request.form['Price']

        db.child("Transactions_Data").push({
            "Category": Category,
            "Emojis": Emojis,
            "Items": Items,
            "Date": Date,
            "Price": Price
        })
    return render_template('RemakeAddingTransactions.html')


@app.route('/EditTransactions/<id>', methods=['GET','POST'])
def EditTransactionsPage(id):
    transaction = db.child('Transactions_Data').child(id).get()

    if request.method == 'POST':
        Category = request.form['Category']
        Emojis = request.form['Emojis']
        Items = request.form['Items']
        Date = request.form['Date']
        Price = request.form['Price']

        db.child("Transactions_Data").child(id).update({
            "Category": Category,
            "Emojis": Emojis,
            "Items": Items,
            "Date": Date,
            "Price": Price
        })

    return render_template('RemakeEditTransactions.html', id=id, transaction=transaction)


@app.route('/AddingCards', methods=['GET', 'POST'])
def AddingCardsPage():
    
    if request.method == 'POST':
        CardHolder = request.form['Card_Holder']
        CardNumber = request.form['Card_Number']
        ExpDate = request.form['Exp_Date']
        Cvc = request.form['CVC']

        db.child("Card_Data").push({
            "Card_Holder": CardHolder,
            "Card_Number": CardNumber,
            "Exp_Date": ExpDate,
            "CVC": Cvc,
        })
    return render_template('RemakeAddingCards.html')


@app.route('/EditCards')
def EditCardsPage():
    return render_template('RemakeEditCards.html')


if __name__ == '__main__':
    app.run(debug=True)
