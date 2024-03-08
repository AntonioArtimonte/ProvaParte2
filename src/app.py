from flask import Flask, request, render_template, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('caminhos.json')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/novo', methods=['GET', 'POST'])
def novo():
    if request.method == 'POST':
        coord_x = request.form['coord_x']
        coord_y = request.form['coord_y']
        coord_z = request.form['coord_z']
        rotation = request.form['rotation']
        db.insert({"nome": "Usuario", "coord_x": coord_x, "coord_y": coord_y, "coord_z": coord_z, "rotation": rotation})
    return render_template('index.html')

@app.route('/listas_caminhos')
def listar_caminhos():
    data = db.all()
    return render_template('lista.html', data=data)

@app.route('/pegar_caminho', methods=['GET', 'POST'])
def pegar_caminho():
    if request.method == 'POST':
        id = request.form['id']
        data = db.get(doc_ids=[id])
    
    return render_template('lista.html', data=data)
    


@app.route('/deletar_caminho', methods=['GET', 'POST'])
def deletar_caminho():
    id = int(request.form['id'])
    db.remove(doc_ids=[id])
    return render_template('index.html')

@app.route('/att_caminho')
def att_caminho():
    return render_template('att_caminho.html')

@app.route('/atualizar_caminho', methods=['GET', 'POST'])
def atualizar_caminho():
    if request.method == 'POST':
        id = int(request.form['id'])
        coord_x = request.form['coord_x']
        coord_y = request.form['coord_y']
        coord_z = request.form['coord_z']
        rotation = request.form['rotation']
        db.update({"coord_x": coord_x, "coord_y": coord_y, "coord_z": coord_z, "rotation": rotation}, doc_ids=[id])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
