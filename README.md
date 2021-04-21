## Desarrollo de RESTful APIs con Python y Flask

Api RESTful que permite la creacion de patentes a partir de un id y que permite
crear una matriz dados tres parametros y clacular la sumatorio en base a dos
coordenadas. Este proyecto esta construido con Python 3 y su framework Flask.

### ejecutar la API

Para ejecutar esta aplicación, es necesario Python 3+ y
[Pipenv](https://pipenv.readthedocs.io/en/latest/) instalados localmente.

Si es así, puedes ejecutar los siguientes comandos:

```bash
# Desde el directorio test-haibu-python
pipenv install
./bootstrap.sh
```

Luego es posible generar peticiones a la API. Por ejemplo, con `curl`,
 se pueden hacer peticiones de la siguiente forma:

```bash
# Creando una nueva matriz
curl -X POST -H "Content-Type: application/json" -d '{
    "r": 5,
    "c": 4,
    "z": 2,
    "x": 1,
    "y": 2
}' http://localhost:5000/matriz

# Consultar patente por id
curl http://localhost:5000/patentes/1000
```
## Ejecutando las pruebas unitarias
---
* Abrir consola de comandos y entrar en la ruta del proyecto, "/test-haibu-python/app"
* Para modulo patente, ejecutar $ python test_unit_patente.py
* Para modulo matriz, ejecutar $ python test_unit_matriz.py

### Construido con
* [flask](https://flask.palletsprojects.com/en/1.1.x/) - El framework web usado
* [pipenv](https://pipenv-es.readthedocs.io/es/latest/) - Manejador de dependencias

### Version 1.0.0
