from main import app
from main import pagina_no_encontrada

if __name__ == '__main__': 
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)

    