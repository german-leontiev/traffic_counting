# Traffic counting

# Demo:

[![Demo](https://www.youtube.com/watch?v=O-WsFncBcrs)]

# How to use:

## Before run
- add coord of track zone in demo/sample/cam_04.json at the points field
- add coord of direction vector in the label: directions field
- to easy get coord from your image use the interactive_image.py
- download yolo weights from https://drive.google.com/file/d/10It3-bByVQUiLV9q4sdJDXQ3bNK9obKi/view?usp=sharing
## To run 
`python run.py --input_path=<>  --output_path=<> --weight=<weights path>`

Note: name of input file must be: cam_04.mp4

## How to run web app
Run `python app.py` and then go to `http://127.0.0.1:5003` in your web browser <br>
*!!! Tested on chromium-based browsers*

## To run container on local machine
`docker run -dit -p 5003:5003 germanleontiev/traffic_counting`

### project authors German, Julia, Dmitry

