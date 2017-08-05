import datetime
import random
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
@app.route('/')
def index():
    if "building" not in session:
        print "session is empty"
        session['visited_places'] = []
        return render_template("index.html", visited_place = "")
    else:
        if session["building"] == "farm":
            gold = random.randrange(10, 21)
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            visited_place = "Earned " + str(gold) + " golds from the " + session["building"] +"!" + " (" + time + ")"
        elif session["building"] == "cave":
            gold = random.randrange(5, 11)
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            visited_place = "Earned " + str(gold) + " golds from the " + session["building"] +"!" + " (" + time + ")"
        elif session["building"] == "house":
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            gold = random.randrange(2, 6)
            visited_place = "Earned " + str(gold) + " golds from the " + session["building"] +"!" + " (" + time + ")"
        elif session["building"] == "casino":
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            take_or_earn = random.randrange(0, 2)
            if take_or_earn == 0:
                gold = random.randrange(0, 51)
                visited_place = "Earned " + str(gold) + " golds from the " + session["building"] +"!" + " (" + time + ")"
            else:
                gold = random.randrange(0, 51)
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                visited_place = "Enter a casino and lost " + str(gold) + " golds OOUCHHH!"  + " (" + time + ")"
        elif session["building"] == '':
            return render_template("index.html", visited_place = session["visited_places"])
        session['visited_places'] += [visited_place]
        session['building'] = ''
        return render_template("index.html", visited_place = session["visited_places"])


@app.route("/process_money", methods=["POST"])
def process_money():
    session["building"] = request.form["building"]
    print "You visit " + session["building"]
    return redirect("/")
app.run(debug=True)
