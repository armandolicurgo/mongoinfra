@app.route('/product', methods=['GET', 'POST'])
def product1():
    form = product(request.form)
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
    form = product(request.form)
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
    return navigation() + getDocumentHTML(tid)

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
    form = product(request.form)
    """getAllDocumentsHTML(sort):"""
    ret = getAllDocumentsHTML("")
    return navigation() + ret  # render_template("child.html",docs = ret)




