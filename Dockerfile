# Usando imagen lightweight alpine
FROM python:3.8-alpine

# Instalando Paquetes
RUN apk update
RUN pip install --no-cache-dir pipenv


# Definir directorio de trabajo y agregar código fuente
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY app ./app


# Instalar dependencias API
RUN pipenv install


# Iniciar app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]
