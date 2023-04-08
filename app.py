import flask
from flask import render_template, request, send_file
import tempfile
from run import main
import argparse
import subprocess
from pathlib import Path
from werkzeug.utils import secure_filename
import os

app = flask.Flask(__name__)



def rm_tree(pth):
    """
    This function cleans dir for next user
    :param pth: path to dir
    :return: None
    """
    pth = Path(pth)
    for child in pth.glob("*"):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()
    
    

@app.route("/", methods=["GET", "POST"])
def predict():
    """
    Simplest logic.
    If user loads page - sends template.
    If user sends image - removes bg from it
    """
    if request.method == "POST":
        f = request.files["file"]
        folder_name = "img/uploaded/"
        Path("img").mkdir(parents=True, exist_ok=True)
        rm_tree("img")
        Path(folder_name).mkdir(parents=True, exist_ok=True)

        filepath = folder_name + secure_filename(f.filename)
        f.save(filepath)
        
        rm_path = "static/result.mp4"
        if os.path.exists(rm_path):
            rm_tree(rm_path)
        os.mkdir(rm_path)
        
        subprocess.run(f"python run.py --input_path={filepath} --output_path=static/result.mp4/{filepath.split('/')[-1]} --weight=best.pt", shell=True)
           
        return send_file(f"static/result.mp4/{filepath.split('/')[-1]}/{filepath.split('/')[-1]}", as_attachment=True)

    return render_template("index.html")


app.run(host="0.0.0.0", port=5003)
