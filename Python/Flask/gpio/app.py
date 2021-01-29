from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
     if request.method == "POST" and request.form.get("submitBtn"):
          GPIO.output(17,GPIO.HIGH)
          GPIO.output(18,GPIO.LOW)
          msg = "welcome!"
     if request.method == "POST" and request.form.get("submitBtn2"):
          GPIO.output(18,GPIO.HIGH)
          GPIO.output(17,GPIO.LOW)
          msg = "Welcome!"
     else:
          msg = "Welcome!"
     return render_template("index.html", msg=msg)

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)
