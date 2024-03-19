# image-search-grpc
This is project to demonstrate grpc functionalities with docker.
## The code structure for the project is as follows:
- Server Implementation Language: Python
- Client Implementation Language: GOLANG

## Steps to run the code:
- Prequisites:
  - Install docker: https://docs.docker.com/engine/install/
- git clone https://github.com/biraaj/image-search-grpc
- cd image-search-grpc
- Create network bridge using command line:
  - docker network create --driver bridge biraaj_cody_grpc
- Server:
  - cd server
  - docker build . -t biraaj-cody/image-search-server
  - docker run --net=biraaj_cody_grpc -p 50051:50051 --name image-search -v ./images:/app/images biraaj-cody/image-search-server
- Client:
  - cd .. && cd client
  - docker build . -t biraaj-cody/image-search-client
  - docker run --net=biraaj_cody_grpc -p 8082:8082  biraaj-cody/image-search-client


