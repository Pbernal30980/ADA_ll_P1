# Proyecto 1 ADA II

## Integrantes
- **Pedro Bernal Londoño** - 2259548
- **Jota Emilio López** - 2259394 
- **Esmeralda Rivas Guzman** - 2259580


## Importante

Para correr el proyecto, se debe tener instalado python3 y pip3, además de tener instalado diferentes paquetes de python. Para instalar los paquetes necesarios, se debe ejecutar el siguiente comando en la terminal:
```bash
pip install -r requirements.txt
```

si esta en linux, debe configurar un ambiente virtual con python3 y activarlo, luego instalar los paquetes necesarios.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar el programa
```bash
python3 main.py
```

## Correr los tests
Para correr los tests, se debe ejecutar el siguiente comando en la terminal:
- Ejecutar todos los tests
```bash
sh test.sh
```
- Ejecutar un test en específico
```bash
sh test.sh smart_terminal_test
sh test.sh public_auction_test
```

## Ejecutar pruebas de rendimiento

Para ejecutar las pruebas de rendimiento, se debe ejecutar el siguiente comando en la terminal:
```bash
sh test.sh test_benchmark
```