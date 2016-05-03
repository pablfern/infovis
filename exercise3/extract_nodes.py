import json


# node = {
#     'name": ?,
#     "sent": ?,
#     "received": ?,
#     "total": ?,
#     "id": ?
# }


def create_graph_files(file_path='./final_data.txt'):
    next_id = 0
    nodes = {}
    links = {}

    with open(file_path) as f:
        content = f.readlines()
        
        for line in content:
            myjson = json.loads(line)
            _from = myjson['from'][0]
            if not _from == 'pablo.fernandez@oldcompany.com.ar':
                _nodes, next_id = _add_sent(_from, nodes, next_id)
            recipients = myjson['to']
            
            if not recipients.__class__ == list:
                recipients = [recipients]
            
            for recipient in recipients:
                if not recipient == 'pablo.fernandez@oldcompany.com.ar':
                    _nodes, next_id = _add_received(recipient, nodes, next_id)
                    if not _from == 'pablo.fernandez@oldcompany.com.ar':
                        if nodes[_from]['id'] > nodes[recipient]['id']:
                            link_id = str(nodes[_from]['id'])+str(nodes[recipient]['id'])
                        else:
                            link_id = str(nodes[recipient]['id'])+str(nodes[_from]['id'])
                        links[link_id] = {
                            "source": nodes[_from]['id'],
                            "target": nodes[recipient]['id'],
                            }
    _write_files(nodes, links)


def  _write_files(nodes, links):
    f = open('nodes.json','w')
    f.write('[\n')
    loop = 0
    for node in nodes.values():
        if not loop == 0:
            f.write(',\n')
        f.write(json.dumps(node))
        loop += 1
    f.write(']\n')

    f.close()
    f = open('links.json', 'w')
    f.write('[\n')
    loop = 0
    for link in links.values():
        if not loop == 0:
            f.write(',\n')
        f.write( json.dumps(link))
        loop += 1
    f.write(']\n')

def _add_sent(contact, nodes, next_id):
    return _add_node(contact, 1, 0, nodes, next_id)


def _add_received(contact, nodes, next_id):
    return _add_node(contact, 0, 1, nodes, next_id)


def _add_node(contact, sent, received, nodes, next_id):
    if contact in nodes:
        nodes[contact]['total'] = nodes[contact]['total'] + 1
        nodes[contact]['sent'] = nodes[contact]['sent'] + sent
        nodes[contact]['received'] = nodes[contact]['received'] + received
    else:
        nodes[contact] = {'name': contact,
                          'sent': sent,
                          'received': received,
                          'total': 1,
                          'id': next_id,
                          }
        next_id += 1
    return nodes, next_id


def get_top_senders(file_path='./final_data.txt', topN=10):
    senders = {}
    with open(file_path) as f:
        content = f.readlines()
        
        for line in content:
            myjson = json.loads(line)
            _from = myjson['from'][0]
            if not _from in senders:
                senders[_from] = 0
            senders[_from] = 1 + senders[_from]
    import operator
    return sorted(senders.items(), key=operator.itemgetter(1), reverse=True)[:topN] 


from sets import Set
def create_bundle(file_path='./final_data.txt'):
    nodes = {}
    with open(file_path) as f:
        content = f.readlines()

        for line in content:
            myjson = json.loads(line)
            _from = myjson['from'][0]

            recipients = myjson['to']
            if not recipients.__class__ == list:
                recipients = [recipients]

            if not _from in nodes:
                nodes[_from] = Set()
            for recipient in recipients:
                if not recipient in nodes:
                    nodes[recipient] = Set()
                if not recipient == 'pablo.fernandez@oldcompany.com.ar':
                    nodes[_from].add(recipient)
    
    f = open('readme-flare-imports.json','w')
    f.write('[\n')
    for node in nodes.keys():
        f.write('{"name":"' + node + '", "size": 1, ' + '"imports": [')
        loops = len(nodes[node])
        count = 1
        for recipient in nodes[node]:
            f.write('"' + recipient + '"')
            if count < loops:
                f.write(',')
        f.write(']},\n')
    f.write(']\n')
    print 'Fin!'
