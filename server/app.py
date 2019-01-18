import os
import uuid

import stripe
from flask import Flask, jsonify, request
# from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
# CORS(app)

WORD = [
    {
        'id': uuid.uuid4().hex,
        '单词': 'Abandon',
        '释意': '放纵，放弃',
        '词性':"名次",
       
    },
     {
        'id': uuid.uuid4().hex,
        '单词': 'Abnormal',
        '释意': '反常的',
        '词性':"形容词",
       
    },
     {
        'id': uuid.uuid4().hex,
        '单词': 'Damp',
        '释意': '毒气',
        '词性':"名词",
       
    },
]


# sanity check route

@app.route('/word', methods=['GET', 'POST'])
def all_word():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        WORD.append({
            'id': uuid.uuid4().hex,
            '单词': post_data.get('word'),
            '释意': post_data.get('mean'),
            '词性': post_data.get('type')
        })
        response_object['message'] = '添加成功!'
    else:
        response_object['word'] = WORD
    return jsonify(response_object)


@app.route('/word/<word_id>', methods=['GET','PUT', 'DELETE'])
def single_word(word_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        # TODO: refactor to a lambda and filter
        return_word = ''
        for word in WORD:
            if word['id'] == word_id:
                return_word = word
        response_object['word'] = return_word
    if request.method == 'PUT':
        post_data = request.get_json()
       
        remove_word(word_id)
        WORD.append({
             'id': uuid.uuid4().hex,
            '单词': post_data.get('word'),
            '释意': post_data.get('mean'),
            '词性': post_data.get('type')
        })
        response_object['message'] = '单词已经更新!'
    if request.method == 'DELETE':
        remove_word(word_id)
        response_object['message'] = '单词删除成功!'
    return jsonify(response_object)




def remove_word(word_id):
    for word in WORD:
        if word['id'] == word_id:
            WORD.remove(word)
            return True
    return False


if __name__ == '__main__':
    app.run()
