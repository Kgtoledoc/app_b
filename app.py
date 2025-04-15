from concurrent import futures
import grpc
import image_processor_pb2
import image_processor_pb2_grpc
from PIL import Image
import io

class ImageProcessor(image_processor_pb2_grpc.ImageProcessorServicer):
    def ProcessImage(self, request, context):
        image = Image.open(io.BytesIO(request.image))
        # Apply transformations (resize, blur, rotate)
        image = image.resize((100, 100))
        image = image.rotate(45)
        output = io.BytesIO()
        image.save(output, format='JPEG')
        return image_processor_pb2.ImageResponse(image=output.getvalue())

def serve():
    print("gRPC Server Starting")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_processor_pb2_grpc.add_ImageProcessorServicer_to_server(ImageProcessor(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()