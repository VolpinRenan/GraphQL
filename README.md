# GraphQL
Just a get started with GraphQL

![alt text](https://raw.githubusercontent.com/VolpinRenan/GraphQL/master/graphql0.png)


For get information
#### Example 1
```python
from sgqlc.endpoint.http import HTTPEndpoint

url = 'http://192.168.0.26:5000/graphql'
query = '''query {allEmployees{edges{node{id name department{name}}}}}'''

endpoint = HTTPEndpoint(url)
data = endpoint(query)
print(data)
```
```
{'data': {'allEmployees': {'edges': [{'node': {'id': 'RW1wbG95ZWU6MQ==', 'name': 'Peter', 'department': {'name': 'Engineering'}}}, {'node': {'id': 'RW1wbG95ZWU6Mg==', 'name': 'Roy', 'department': {'name': 'Engineering'}}}, {'node': {'id': 'RW1wbG95ZWU6Mw==', 'name': 'Tracy', 'department': {'name': 'Human Resources'}}}]}}}
```
#### Example 2
```python
from graphqlclient import GraphQLClient

client = GraphQLClient('http://192.168.0.26:5000/graphql')
result = client.execute('''{allEmployees{edges{node{id name department{name}}}}}''')
print(result)
```
```
{'data': {'allEmployees': {'edges': [{'node': {'id': 'RW1wbG95ZWU6MQ==', 'name': 'Peter', 'department': {'name': 'Engineering'}}}, {'node': {'id': 'RW1wbG95ZWU6Mg==', 'name': 'Roy', 'department': {'name': 'Engineering'}}}, {'node': {'id': 'RW1wbG95ZWU6Mw==', 'name': 'Tracy', 'department': {'name': 'Human Resources'}}}]}}}
```

#### Example 3
```python
import json
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

transport = RequestsHTTPTransport('http://192.168.0.26:5000/graphql')
client = Client(transport=transport)
response = client.execute(gql("{allEmployees{edges{node{id name department{name}}}}}"))
print(response)
```
```
{'allEmployees': {'edges': [{'node': {'id': 'RW1wbG95ZWU6MQ==', 'name': 'Peter', 'department': {'name': 'Engineering'}}}, {'node': {'id': 'RW1wbG95ZWU6Mg==', 'name': 'Roy', 'department': {'name': 'Engineering'}}}, {'node': {'id': 'RW1wbG95ZWU6Mw==', 'name': 'Tracy', 'department': {'name': 'Human Resources'}}}]}}
```
### MUTATION
JUST SYNTAX FOR DOING MUTATION

```python
from graphqlclient import GraphQLClient

client = GraphQLClient('http://192.168.0.26:8000/graphql')
result = client.execute('''mutation{createPost(username:"johndoe",title:"Vai Corinthians", body:"Body desc"){post{title body author{username}}}}''')
```

Mutation
# ![alt text](https://raw.githubusercontent.com/VolpinRenan/GraphQL/master/graphql2.png)
Query
# ![alt text](https://raw.githubusercontent.com/VolpinRenan/GraphQL/master/graphql1.png)
