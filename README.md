
# App B

App B es el backend gRPC que procesa las imágenes recibidas de App A. Aplica transformaciones como redimensionar, desenfocar y rotar.

## Características

- Procesa imágenes utilizando gRPC.
- Aplica transformaciones a las imágenes.

## Requisitos

- Python 3.9+
- Docker

## Instalación

1. Clona el repositorio:
   git clone <URL_DEL_REPOSITORIO_APP_B>
   cd app_b
2. Instala las dependencias:
   pip install -r requirements.txt
3. Ejecuta la aplicación:
   python app.py
## Despliegue
App B se despliega en un clúster de Kubernetes. El despliegue se gestiona a través de AWS CodeBuild y Amazon EKS.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.