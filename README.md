## Dashboard da produção de Partos (Normais e de Risco) em Pernambuco


<hr>

```bash
# clonando...

$ git clone https://github.com/bernarducs/partos-risco-pe.git
$ cd partos-risco-pe
$ python -m venv ve; source ve/bin/activate; python -m pip install -U pip; pip install -r requirements.txt


# rodando...

$ python main.py

```

### Deploying com gunicorn:
<hr>

Na raiz do projeto:

`(ve) ~$ gunicorn --bind 0.0.0.0:5000 main:server`

Clique [aqui](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04) para deploy 
utilizando nginx web server.

### <i>TODO</i>:
<hr>

| TODO              | DONE        |
| ----------------- | ----------- |
| Documentação      | :red_circle:|
| Testes            | :red_circle:|