FROM golang:1.22.1

RUN apt-get update
RUN apt-get install unzip

# ENV PROTOC_ZIP=protoc-26.0-linux-x86_64.zip
# RUN curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v26.0/$PROTOC_ZIP
# RUN unzip -o $PROTOC_ZIP -d /usr/local bin/protoc
# RUN unzip -o $PROTOC_ZIP -d /usr/local 'include/*'
# RUN rm -f $PROTOC_ZIP

# Install grpc
RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.33.0
RUN go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.3.0

ENV PATH="$PATH:$HOME/.local/bin:$(go env GOPATH)/bin"

WORKDIR /go/src/app

COPY . .

EXPOSE 8080

ENTRYPOINT cd /go/src/app/executable && go run main.go

