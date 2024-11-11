import uvicorn
from ariadne import make_executable_schema, load_schema_from_path
from fastapi import FastAPI
from ariadne.asgi import GraphQL

from resolvers import resolvers


type_defs = load_schema_from_path('./schema')

schema = make_executable_schema(type_defs, resolvers)
graphql_app = GraphQL(schema)

app = FastAPI()
app.mount('/graphql', graphql_app)


@app.get('/')  # will serve built frontend
def home():
    return 'Welcome to the FastAPI and GraphQL backend!'


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
