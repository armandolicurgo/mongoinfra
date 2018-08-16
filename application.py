#
# application.py - implements  customerDocument html interface
# armandolicurgo@gmail.com 08/10/2018


from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask import request, redirect, url_for
from flask import Flask, render_template,jsonify, Response
from mongopart import insertDocument, connectionCollection, connectionString, connectionDatabase, getAllDocumentsHTML, getDocumentHTML, updateDocument,deleteDocument,getAllDocumentsJSON
from mongopart import insert2Document, connection2Collection, connection2String, connection2Database, getAllDocuments2HTML, getDocument2HTML, update2Document,delete2Document,getAllDocuments2JSON

from bson.objectid import ObjectId
import os



class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=0, max=80)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class Customer(Form):
    id_ = StringField("id_", [validators.Length(min=0, max=20)])
    customer = StringField("customer", [validators.Length(min=0, max=60)])
    customerid = StringField("customerid", [validators.Length(min=0, max=10)])
    address = StringField("address", [validators.Length(min=0, max=60)])
    address2 = StringField("address2", [validators.Length(min=0, max=60)])
    city = StringField("city", [validators.Length(min=0, max=60)])
    state_ = StringField("state", [validators.Length(min=0, max=40)])
    phone = StringField("phone", [validators.Length(min=0, max=60)])
    contact = StringField("contact", [validators.Length(min=0, max=60)])
    document_ = StringField("document", [validators.Length(min=0, max=20)])
    credit = StringField("credit", [validators.Length(min=0, max=5)])

class Product(Form):
    id_ = StringField("id_", [validators.Length(min=0, max=20)])
    group = StringField("Group", [validators.Length(min=0, max=60)])
    product = StringField("Product", [validators.Length(min=0, max=60)])
    productid = StringField("ProductId", [validators.Length(min=0, max=10)])
    price = StringField("Price", [validators.Length(min=0, max=12)])
    packing = StringField("Packing", [validators.Length(min=0, max=20)])
    unitperpack = StringField("UnitPerPack", [validators.Length(min=0, max=20)])
    credit = StringField("Credit", [validators.Length(min=0, max=3)])
    available = StringField("Available", [validators.Length(min=0, max=3)])

    
    
    
    
    

def up(pp):
    r = pp.replace("&lt;", "<")
    r = r.replace("&gt;", ">")
    r = r.replace("&#34;", '"')
    return r


def navigation():
    return """<a href="/">Main</a> <a href="/customer">Add customer</a> <a href="/customerlist">List</a> <a href="/ang">Ang</a> 
    <a href="/productlist">Product list</a> <a href="/">List</a> <a href="/ang">Ang</a> <br>
    """

def difd(d1,d2):
    dd2 = ",".join(d2)
    for one in d1:
        if dd2.find(one) == -1:
            print(one)
def difdir(d1,d2):
    difd(d1,d2)
    difd(d2,d1)

def get_file(filename):  # pragma: no cover
    try:
        #src = os.path.join(root_dir(), filename)
        src = filename
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)





app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def maain():
    difdir(dir(Product),dir(Customer))
    return redirect(url_for('customerlistall'))

@app.route('/ang', methods=['GET'])
def aang():
    content = get_file('./templates/ang.html')
    return Response(content, mimetype="text/html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        #           form.password.data)
        # db_session.add(user)
        #flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/customer', methods=['GET', 'POST'])
def customer1():
    form = Customer(request.form)
    if request.method == 'POST' and form.validate():
        print(form)
        query = {"customer": request.form["customer"],
                 "customerid": request.form["customerid"],
                 "address": request.form["address"],
                 "address2": request.form["address2"],
                 "city": request.form["city"],
                 "state_": request.form["state_"],
                 "phone": request.form["phone"],
                 "contact": request.form["contact"],
                 "document_": request.form["document_"],
                 "credit": request.form["credit"]}
        insertDocument(query)
        return redirect(url_for('customer1'))
    return navigation() + render_template('customer1.html', form=form)


@app.route('/customerupdate/<tid>', methods=['POST'])
def customer1update(tid):
    form = Customer(request.form)
    if True:  # form.validate():
        #print(form)
        #            "_id": request.form["id_"],
        query = {
            "customer": request.form["customer"],
            "customerid": request.form["customerid"],
            "address": request.form["address"],
            "address2": request.form["address2"],
            "city": request.form["city"],
            "state_": request.form["state_"],
            "phone": request.form["phone"],
            "contact": request.form["contact"],
            "document_": request.form["document_"],
            "credit": request.form["credit"]}
        updateDocument({"_id": ObjectId(tid)}, query )
        return redirect(url_for('customerlistall'))
    else:
        #print("nao validou")
        id_ = request.form["id_"]
        customer = request.form["customer"]
        customerid = request.form["customerid"]
        address = request.form["address"]
        address2 = request.form["address2"]
        city = request.form["city"]
        state_ = request.form["state_"]
        phone = request.form["phone"]
        contact = request.form["contact"]
        document_ = request.form["document_"]
        credit = request.form["credit"]
    return navigation() + render_template('customer2.html',
                                          form=form,
                                          id_=id_,
                                          customer=customer,
                                          customerid=customerid,
                                          address=address,
                                          address2=address2,
                                          city=city,
                                          state_=state_,
                                          phone=phone,
                                          contact=contact,
                                          document_=document_,
                                          credit=credit)


@app.route('/customer/<tid>', methods=['GET'])
def costumer2(tid):
    return navigation() + getDocumentHTML(tid)

@app.route('/customers', methods=['GET'])
def costmer2s():
        return getAllDocumentsJSON("")
        #return jsonify([{'Name':'Armando', 'Country':'Brasil'}])



@app.route('/customerdelete/<tid>', methods=['GET'])
def costumerdele(tid):
    deleteDocument({"_id": ObjectId(tid)} )
    return redirect(url_for('customerlistall'))



@app.route('/customerlist', methods=['GET', 'POST'])
def customerlistall():
    form = Customer(request.form)
    """getAllDocumentsHTML(sort):"""
    ret = getAllDocumentsHTML("")
    return navigation() + ret  # render_template("child.html",docs = ret)

################# products #########################
@app.route('/product', methods=['GET', 'POST'])
def product1():
    form = Product(request.form)
    if request.method == 'POST' and form.validate():
        print(form)
        query = {"Product": request.form["product"],
                 "ProductId": request.form["productid"],
                 "Group": request.form["group"],
                 "Price": request.form["price"],
                 "Packing": request.form["packing"],
                 "UnitPerPack": request.form["unitperpack"],
                 "Credit": request.form["credit"],
                 "Available": request.form["available"]}
        insertDocument(query)
        return redirect(url_for('product1'))
    return navigation() + render_template('product1.html', form=form)


@app.route('/productupdate/<tid>', methods=['POST'])
def product1update(tid):
    form = Product(request.form)
    if True:  # form.validate():
        #print(form)
        #            "_id": request.form["id_"],
        query = {"Product": request.form["product"],
                 "ProductId": request.form["productid"],
                 "Group": request.form["group"],
                 "Price": request.form["price"],
                 "Packing": request.form["packing"],
                 "UnitPerPack": request.form["unitperpack"],
                 "Credit": request.form["credit"],
                 "Available": request.form["available"]}
        updateDocument({"_id": ObjectId(tid)}, query )
        return redirect(url_for('productlistall'))
    else:
        #print("nao validou")
        id_ = request.form["id_"]
        product = request.form["product"]
        productid = request.form["productid"]
        group = request.form["group"]
        price = request.form["price"]
        packing = request.form["packing"]
        unitperpack = request.form["unitperpack"]
        credit = request.form["credit"]
        available = request.form["available"]
    return navigation() + render_template('product2.html',
                                          form=form,
                                          id_=id_,
                                          product=product,
                                          productid=productid,group=group,price=price,
                                          packing=packing,unitperpack=unitperpack,
                                          credit=credit,available=available)

@app.route('/product/<tid>', methods=['GET'])
def proer2(tid):
    return navigation() + getDocument2HTML(tid)

@app.route('/products', methods=['GET'])
def proder2s():
        return getAllDocumentsJSON("")
        #return jsonify([{'Name':'Armando', 'Country':'Brasil'}])



@app.route('/productdelete/<tid>', methods=['GET'])
def proddele(tid):
    deleteDocument({"_id": ObjectId(tid)} )
    return redirect(url_for('productlistall'))



@app.route('/productlist', methods=['GET', 'POST'])
def productlistall():
    form = Product(request.form)
    """getAllDocumentsHTML(sort):"""
    ret = getAllDocuments2HTML("")
    return navigation() + ret  # render_template("child.html",docs = ret)










if __name__ == "__main__":
    print(dir(app))
    app.run(debug=True)
