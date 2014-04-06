import flask, flask.views, os
import getLetter as gl

app = flask.Flask(__name__)


app.secret_key = "hoku"

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template("index.html")
    def post(self):
        user_input = flask.request.form['expression']
        predictions = gl.GetProb(list(user_input))
        flask.flash(predictions)
        return self.get()

app.add_url_rule('/',view_func=View.as_view('main'), methods=['GET','POST'])

app.debug = True
app.run()
