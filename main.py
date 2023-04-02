#Elīna Miltiņa 221RDC017 18.grupa
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    output = []
    for i, response in enumerate(result):
        output.append(response)
        if i < len(result) - 1:
            output.append(' ' if response != 'not found' and result[i + 1] == 'not found' else '\n')
    print(''.join(output))



def process_queries(queries):
    result = []
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            response = 'not found'
            if cur_query.number in contacts:
                response = contacts[cur_query.number]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
