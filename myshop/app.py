from flask import Flask, jsonify , render_template,redirect,url_for
app=Flask(__name__)
total=0
produits=[{"id":1,
           "marque":"HP",
           "model":"INSPIRON",
           "prix":"1000",
           "categorie":"ordinateur Portable",
           "qtt":42,
           "panier":"pn.png",
           "image":"3.png"},
           {"id":2,
           "marque":"DELL",
           "model":"INSPIRON",
           "prix":"2000",
           "categorie":"ordinateur Portable",
           "qtt":30,
            "panier":"pn.png",
           "image":"2.jpg"},
           {"id":3,
           "marque":"lenovo",
           "model":'INSPIRON',
           "panier":"pn.png",
           "prix":"3000",
           "categorie":"ordinateur Portable",
           "qtt":50,
           "image":"11.webp"},
           {"id":4,
           "marque":"HP",
           "panier":"pn.png",
           "model":"INSPIRON",
           "prix":"5500",
           "categorie":"ordinateur Portable",
           "qtt":60,
           "image":"3.png"},
           {"id":5,
           "marque":"macbook",
           "model":"INSPIRON",
           "panier":"pn.png",
           "prix":"4300",
           "categorie":"ordinateur Portable",
           "qtt":33,
           "image":"4.jpg"},
           {"id":6,
           "marque":"ASUS",
           "model":"INSPRON",
           "prix":"6000",
           "panier":"pn.png",
           "categorie":"ordinateur Portable",
           "qtt":42,
           "image":"18.png"},]

@app.route("/")
def home():
    return render_template('index.html',carte=cart,prdui=produits,q=qtt,to=total)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/detail")
def detail():
    return render_template('detail.html')

@app.route("/pannier")
def pannier():
    return render_template('pannier.html')

@app.route('/api/produits')
def listProd():
    return jsonify(produits)
cart=[]
qt=1
qtt=[qt,qt,qt,qt,qt,qt]
@app.route('/add/<int:idd>')
def add(idd): 
    global total
    if idd not in cart:
        cart.append(idd)
        total+=int(produits[idd-1]['prix'])
    else:
        qtt[idd-1]+=1
        total+=int(produits[idd-1]['prix'])
    return redirect(url_for('home'))
@app.route('/dele/<int:idd>')
def dele(idd):
    global total
    total-=qtt[idd-1]*int(produits[idd-1]['prix'])
    qtt[idd-1]=1
    if len(cart)==1:
        total=0
    for i in range(len(cart)):
        if idd==cart[i]:
            del(cart[i])
            return render_template('index.html',prdui=produits,carte=cart,q=qtt,to=total)

if __name__=="__main__":
    app.run(debug=True)