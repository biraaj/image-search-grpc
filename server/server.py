import grpc
import random
import os
from concurrent import futures
import image_search_pb2
import image_search_pb2_grpc

class ImageSearchServicer(image_search_pb2_grpc.ImageSearchServicer):
    def __init__(self, image_folder):
        self.image_folder = image_folder

    def SearchImage(self, request, *args):
        keyword = request.keyword
        print("request for keyword: ",keyword)
        image_files = [_files for _files in os.listdir(self.image_folder) if keyword in _files]
        if not image_files:
            print("images not found for: ", keyword)
            return image_search_pb2.ImageResponse(image_data=b'') #communication happens through binary format 
        image_file = random.choice(image_files)
        with open(os.path.join(self.image_folder, image_file), 'rb') as f:
            image_data = f.read()
        print("Sending image: ",image_file)
        return image_search_pb2.ImageResponse(image_data=image_data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_search_pb2_grpc.add_ImageSearchServicer_to_server(
        ImageSearchServicer('./images/'), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()