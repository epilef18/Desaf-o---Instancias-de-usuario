import json
from usuario import Usuario
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)
 

def instancia(datos):
    try:
        return Usuario(
            nombre=datos.get('nombre'),
            apellido=datos.get('apellido'),
            email=datos.get('email'),
            genero=datos.get('genero')
        )
    except Exception as e:
        logging.error(f"Error al crear instancia de usuario {e}")
        return None

def main():

    lista_usuarios = []

    try:   
        with open("usuarios.txt", 'r') as file:
            for line in file:
                try:
                    datos = json.loads(line.strip())

                    usuario = instancia(datos)

                    if usuario:
                        lista_usuarios.append(usuario)

                except json.JSONDecodeError as e:
                    logging.error(f"Error al decodificar JSON: {e}")
                except Exception as e:
                    logging.error(f"Error al procesar línea {e}")

    except FileNotFoundError as e:
        logging.error(f"El archivo no se encuentra: {e}")
    except Exception as e:
        logging.error(f"Error al leer el archivo {e}")
    print(f"Se crearon {len(lista_usuarios)} instancias de usuario.")

if __name__ == "__main__":
    main()