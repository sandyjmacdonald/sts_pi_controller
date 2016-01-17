import explorerhat as eh
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<state>")
def update_robot(state=None):
    if state == 'forward':
        eh.motor.one.backwards(100)
        eh.motor.two.forwards(100)
    if state == 'back':
        eh.motor.one.forwards(100)
        eh.motor.two.backwards(100)
    if state == 'left':
        eh.motor.two.stop()
        eh.motor.one.backwards(100)
    if state == 'right':
        eh.motor.one.stop()
        eh.motor.two.forwards(100)
    if state == 'stop':
        eh.motor.one.stop()
        eh.motor.two.stop()
    if state == 'anti-clockwise':
        eh.motor.one.backwards(100)
        eh.motor.two.backwards(100)
    if state == 'clockwise':
        eh.motor.one.forwards(100)
        eh.motor.two.forwards(100)
    template_data = {
        'title' : state,
    }
    return render_template('main.html', **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
