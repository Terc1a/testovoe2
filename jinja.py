import json
import jinja2
with open("data2.json", 'r') as json_file:
    json_data = json.load(json_file)
incoming_request = json.dumps(json_data)
template = jinja2.Template('{{ incoming_request.dialog_id }}, {{ incoming_request.text }}, {{ incoming_request.hook_type }}, {{ incoming_request.client.phone }}, {{ incoming_request.type }}')
incoming_request_1 = json.loads(incoming_request)
variable = template.render(incoming_request=incoming_request_1)
var_data = (json.loads(json.dumps(variable))).split()
data = {'backreq': []}
data['backreq'].append({
    'chat_id': var_data[0]
})
data['backreq'].append({
    'dialog': f'messages[{var_data[1]}]'
})
data['backreq'].append({
    'features': f'hook_type[{var_data[3]}],, client_phone[{var_data[4]}], type[{var_data[5]}]'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

ar = []

with open('data.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split(' ')
        if n !='':
            ar.append(n)

with open('back_request.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e)