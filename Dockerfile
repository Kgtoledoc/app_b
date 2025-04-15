FROM public.ecr.aws/sam/build-python3.9:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el archivo .proto y compilarlo
COPY proto/image_processor.proto .
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image_processor.proto

COPY . .

CMD ["python", "app.py"]