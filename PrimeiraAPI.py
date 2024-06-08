from flask import Flask, jsonify, request

app = Flask(__name__)

animais = [
    {
        'id': 1,
        'nome': 'Liara',
        'espécie': 'felina',
        'sexo': 'F',
        'pelagem': 'rajada'
    },
    {
        'id': 2,
        'nome': 'Milla',
        'espécie': 'canina',
        'sexo': 'F',
        'pelagem': 'amarela'
    },
    {
        'id': 3,
        'nome': 'Lulu',
        'espécie': 'canina',
        'sexo': 'F',
        'pelagem': 'preta e branca'
    },
    {
        'id': 4,
        'nome': 'Luke',
        'espécie': 'felina',
        'sexo': 'M',
        'pelagem': 'branca'
    },
]

# Consultar(todos)
@app.route('/animais', methods=['GET'])
def obter_animais():
    return jsonify(animais)


# Consultar(id)
@app.route('/animais/<int:id>', methods=['GET'])
def obter_animal_por_id(id):
    for animal in animais:
        if animal.get('id') == id:
            return jsonify(animal)
    return jsonify({'erro': 'Animal não encontrado'}), 404

#Editar
@app.route('/animais/<int:id>', methods = ['PUT'])
def editar_animal_por_id(id):
    animal_modificado = request.get_json()
    for indice, animal in enumerate(animais):
        if animal.get('id') == id:
            animais[indice].update(animal_modificado)
            return jsonify(animais[indice])
    return jsonify({'erro': 'Animal não encontrado'}), 404

#Criar
@app.route('/animais', methods = ['POST'])
def incluir_novo_animal():
    novo_animal = request.get_json()
    animais.append(novo_animal)
    return jsonify(animais)

#Excluir
@app.route('/animais/<int:id>', methods = ['DELETE'])
def excluir_animais(id):
    for indice, animal in enumerate(animais):
        if animal.get('id') == id:
            del animais[indice]
            return jsonify({'mensagem': 'Animal excluído com sucesso'})
    return jsonify({'erro': 'Animal não encontrado'}), 404        
   
   
#Permite acessar localmente para manipular os dados
app.run(port=5000,host='localhost', debug = True)        
