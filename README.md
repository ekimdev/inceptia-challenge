![black](https://img.shields.io/badge/code%20style-black-black)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

<br/>
<div align="center">
  <h1 align="center">Inceptia Challenge</h1>
</div>

## Cómo empezar
1. Clonar el repositorio
```
$ git clone https://github.com/ekimdev/inceptia-challenge.git
```
2. crea un venv
```
python -m venv /tmp/venv
source /tmp/venv/bin/activate
```

### Cómo ejecutar geoapi.py

### Docker
```
make build
make run
```
#### Sin make
```
docker build -t geoapi .
docker run --rm geoapi:latest
```
#### Con logging
```
docker run --rm geoapi:latest --verbose
```
#### Para usar otro valor de max_temp
```
docker run --rm geoapi:latest -v --max-temp=16
```
#### Virtual env
```
python geoapi.py --help
```

### Cómo ejecutar product_available.py
#### Virtual env
```
$ python product_available.py
>>> Chocolate, 3
Hay stock de Chocolate

$ python product_available.py
>>> chocolate, 3
El producto chocolate no existe

$ python product_available.py
>>> Chocolate, 6
>>> Chocolate, 5
>>> Chocolate, 7
>>> Chocolate, 9
El producto Chocolate alcanzó el máximo de intentos
```
### Cómo ejecutar validate_discount.py
#### Virtual env
```
python validate_discount.py
```

## Ejecutar los tests
Se necesita `pytest` (`pip install pytest`)

```
make tests
```
