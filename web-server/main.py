import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

'''Instancia de la aplicación FastAPI'''
app = FastAPI()
'''Decorador'''
@app.get('/')
def get_list():
     return [1,2,3]

'''Decorador'''
@app.get('/contact')
def get_list():
    return{'name': 'Platzi'}

'''Decorador'''
@app.get('/HTML', response_class=HTMLResponse)
def get_list():
    return """
    <h1> PAGINA WEB DESDE PYTHON</h1>
    <p>Desarrollando retorno de pagina web desde HTML</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()