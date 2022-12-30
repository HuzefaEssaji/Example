from flask import Flask, render_template, request
# import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)  # Sets up the RPi lib to use the Broadcom pin mappings
                        #  for the pin names. This corresponds to the pin names
                        #  given in most documentation of the Pi header
# GPIO.setwarnings(False) # Turn off warnings that may crop up if you have the
                        #  GPIO pins exported for use via command line
# GPIO.setup(2, GPIO.OUT) # Set GPIO2 as an output

app = Flask(__name__)   # Create an instance of flask called "app"

@app.route("/")
def index():
    return render_template("index.html"), {"Refresh": "3; url=list_of_biochhemistry"}

@app.route("/list_of_biochhemistry")
def list_of_biochhemistry():
    
    return render_template("list_of_biochemistry.html")

@app.route("/test_done",methods=['GET','POST'])
def test_done():
    if request.method == "POST":
        test_list = request.form.getlist('test_list')
        for test in test_list:
            if (test == "ALBUMIN"):
                print("ALBUMIN DONE")
            elif test == "CHOLESTEROL":
                print("CHOLESTEROL DONE")
            elif test == "GLUCOSE":
                print("GLUCOSE DONE")
            elif test == "HDL":
                print("HDL DONE")
            elif test == "POTASSIUM":
                print("POTASSIUM DONE")
            elif test == "SODIUM":
                print("SODIUM DONE")
            elif test == "TP":
                print("TP DONE")
            elif test == "TRIGLYCERIDE":
                print("TRIGLYCERIDE DONE")
            elif test == "URIC/ACID":
                print("URIC/ACID DONE")
            elif test == "CREATININE":
                print("CREATININE DONE")
            elif test == "CRP":
                print("CRP DONE")
            
        
    return render_template("test_done.html"), {"Refresh": "2; url=list_of_biochhemistry"}


if __name__ == '__main__':
   app.run(debug = True)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)