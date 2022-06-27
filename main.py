from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['TESTING'] = True
database = {}


@app.route('/', methods=['GET'])
def home():
    all_urls = {
        'all_participants': '/participant?ref_num=all',
        'retrieve_participant': '/participant?ref_num={ref_num}',
        'add_participant': '/participant/add/{ref_num}',
        'update_participant': '/participant/update/{ref_num}',
        'delete_participant': '/participant/delete/{ref_num}',
    }
    return jsonify(all_urls)


@app.route('/participant', methods=['GET'])
def get_participants():
    ref_num = request.args['ref_num']
    if ref_num == 'all':
        res = database
    else:
        if ref_num in database:
            res = database[ref_num]
        else:
            res = f'Reference number [{ref_num}] does not exist in the database.'
            return res
    return jsonify(res)


@app.route('/participant/add/<ref_num>', methods=['POST'])
def add_participant(ref_num):
    if ref_num in database:
        msg = f'Reference number [{ref_num}] already exists in the database.'
        ret = {
            'ref_num': ref_num,
            'status': 'fail',
            'msg': msg
        }
        return jsonify(ret)

    # Request body should contain name, date_of_birth, phone_number, and address.
    # body = body[ref_num]
    body = request.get_json()
    if 'name' not in body or 'date_of_birth' not in body or \
            'phone_number' not in body or 'address' not in body:
        msg = f'Request body should contain name, date_of_birth, phone_number, and address.'
        ret = {
            'ref_num': ref_num,
            'status': 'fail',
            'msg': msg
        }
        return jsonify(ret)

    database[ref_num] = body
    msg = f'Participant with reference number [{ref_num}] has been enrolled successfully. ' \
          f'body={database[ref_num]}'
    ret = {
        'ref_num': ref_num,
        'body': database[ref_num],
        'status': 'success',
        'msg': msg
    }
    return jsonify(ret)


@app.route('/participant/update/<ref_num>', methods=['POST'])
def update_participant(ref_num):
    if ref_num not in database:
        msg = f'Reference number [{ref_num}] does not exist in the database.'
        ret = {
            'ref_num': ref_num,
            'status': 'fail',
            'msg': msg
        }
        return jsonify(ret)

    # Request body should contain one of name, date_of_birth, phone_number, and address.
    body = request.get_json()
    participant_info = database[ref_num]
    if 'name' in body:
        participant_info['name'] = body['name']
    if 'date_of_birth' in body:
        participant_info['date_of_birth'] = body['date_of_birth']
    if 'phone_number' in body:
        participant_info['phone_number'] = body['phone_number']
    if 'address' in body:
        participant_info['address'] = body['address']

    msg = f'Participant with reference number [{ref_num}] has been updated successfully. ' \
          f'body={database[ref_num]}'
    ret = {
        'ref_num': ref_num,
        'body': database[ref_num],
        'status': 'success',
        'msg': msg
    }
    return jsonify(ret)


@app.route('/participant/delete/<ref_num>', methods=['DELETE'])
def remote_participant(ref_num):
    if ref_num not in database:
        msg = f'Reference number [{ref_num}] does not exist in the database.'
        ret = {
            'ref_num': ref_num,
            'status': 'fail',
            'msg': msg
        }
    else:
        del database[ref_num]
        msg = f'Participant with reference number [{ref_num}] has been deleted successfully.'
        ret = {
            'ref_num': ref_num,
            'status': 'success',
            'msg': msg
        }
    return jsonify(ret)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)

