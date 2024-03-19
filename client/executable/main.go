package main

import (
	"encoding/base64"
	"html/template"
	"log"
	"net/http"

	pb "github.com/biraaj/image-search-grpc/image_search" // Update this with the correct path to your Protobuf-generated code
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

// Server address
const serverAddress = "image-search:50051"

// HTML template
const htmlTemplate = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Search</title>
</head>
<body>
    <h1>Image Search</h1>
    <form action="/search" method="post">
        <label for="keyword">Keyword:</label>
        <input type="text" id="keyword" name="keyword">
        <button type="submit">Search</button>
    </form>
    {{if .Message}}
        <p>{{.Message}}</p>
    {{else}}
        {{if .ImageData}}
            <h2>Search Result</h2>
            <img src="data:image/png;base64,{{.ImageData}}" alt="Search Result">
        {{end}}
    {{end}}
</body>
</html>
`

// Encode image data to base64
func encodeBase64(data []byte) string {
	return base64.StdEncoding.EncodeToString(data)
}

// serves the index.html file
func IndexHandler(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "index.html")
}

// SearchHandler handles the search requests
func SearchHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	keyword := r.FormValue("keyword")
	log.Printf("keyword: %v", keyword)

	// gRPC client connection
	conn, err := grpc.Dial(serverAddress, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		http.Error(w, "Failed to connect to server", http.StatusInternalServerError)
		return
	}
	defer conn.Close()
	//log.Printf("Response from gRPC server: %v", conn)

	client := pb.NewImageSearchClient(conn)

	// gRPC request
	response, err := client.SearchImage(r.Context(), &pb.SearchRequest{Keyword: keyword})
	//log.Printf("Response from gRPC server after request: %v", response)
	if err != nil {
		http.Error(w, "Failed to search image", http.StatusInternalServerError)
		return
	}

	// Rendering HTML template with search result
	t := template.Must(template.New("index").Parse(htmlTemplate))
	data := struct {
		ImageData string
		Message   string
	}{
		ImageData: encodeBase64(response.ImageData),
		Message:   "No image found for the given keyword",
	}
	if len(response.ImageData) > 0 {
		data.Message = "" // Clear the message if image data is found
	}
	t.Execute(w, data)
}

func main() {
	http.HandleFunc("/", IndexHandler)
	http.HandleFunc("/search", SearchHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
