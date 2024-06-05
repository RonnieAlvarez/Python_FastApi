from fastapi import FastAPI
#import  uvicorn 

app=FastAPI()

@app.get('/')
def message():
    return 'Hola mundo!!! Hello'



# if __name__ == '__main__':
#     uvicorn.run('main:app',host='127.0.0.1',port=5000)
#
# es es una forma de iniciar la aplicacion
#
# otra forma es desde la terminal:
# uvicorn main:app --port 5000 --reload