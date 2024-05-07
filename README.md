# The tool is used to provide a weather by US zip code. It is built pn python Flask, having a simple UI.

# Usage

To run locally : `python3 app.py`
To rin containerized:
- build image using `docker build . -t webapp:1.0.0`
- run the container with `docker run -d -p 8080:8080 webapp:1.0.0`

application will listen on port 8080, you can access it on `http://localhost:8080`


.....
repo for GDE DevOps Course 03/2024
