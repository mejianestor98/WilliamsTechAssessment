import uvicorn
from ariadne import make_executable_schema, load_schema_from_path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from ariadne.asgi import GraphQL

from resolvers import resolvers


type_defs = load_schema_from_path('./schema')

schema = make_executable_schema(type_defs, resolvers)
graphql_app = GraphQL(schema)

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

app.mount('/graphql', graphql_app)
app.mount('/assets', StaticFiles(directory='./bundled_ui/assets'), name='assets')


@app.get('/')
def home():
    return FileResponse('./bundled_ui/index.html')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
