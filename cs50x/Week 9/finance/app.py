import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, apology1

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    userid = session["user_id"]
    rows = db.execute("SELECT company, symbol, quantity FROM portfolio WHERE userid=?", userid)
    cash = db.execute("SELECT cash FROM users WHERE id=?", userid)[0]["cash"]
    return render_template("layout.html", rows=rows, lookup=lookup, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        try:
            qty = float(request.form.get("shares"))
            if (qty % 1) > 0:
                return apology("Not a valid quantity")
            elif qty < 1:
                return apology("Not a valid quantity")
        except:
            return apology("Invalid quantity")
        buy = request.form.get("symbol")
        temp = lookup(buy)
        if temp != None:
            name = temp["name"]
            price = (temp["price"])
            buy = (temp["symbol"])

            userid = session["user_id"]
            cash = db.execute("SELECT cash FROM users WHERE id=?", userid)[0]["cash"]
            total = price*float(qty)
            if float(cash) < total:
                return apology("not enough money")
            result = db.execute(
                "UPDATE portfolio set quantity=quantity+? where userid=? and symbol=?", qty, userid, buy)
            if not result:
                db.execute(
                    "INSERT INTO portfolio (userid, company, symbol, quantity) VALUES (?,?,?,?)", userid, name, buy, qty)
            db.execute("UPDATE users set cash=cash-? where id=?", total, userid)
            db.execute("INSERT INTO logs (userid, company, symbol, price, quantity, type) VALUES (?,?,?,?,?,'buy')",
                       userid, name, buy, price, qty)
            return redirect("/")
        else:
            return apology("Stock does not exist!")
    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    userid = session["user_id"]
    rows = db.execute("SELECT type, symbol, price, quantity, time FROM logs where userid=?", userid)
    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Login succesful!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        temp = lookup(symbol)
        if temp != None:
            name = temp["name"]
            price = usd(temp["price"])
            symbol = (temp["symbol"])

        else:
            return apology("Stock does not exist!")
        return render_template("quoted.html", name=name, price=price, symbol=symbol)
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if password != confirmation:
            return apology("Passwords do not match!")
        elif not username.strip():
            return apology("Name is blank!")
        elif not password.strip():
            return apology("Name is blank!")
        hashed = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hashed)
            flash("You have successfully registered!")
            return redirect("/")
        except ValueError:
            return apology("Duplicate username")
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    userid = session["user_id"]
    if request.method == "POST":
        try:
            qty = float(request.form.get("shares"))
            if (qty % 1) > 0:
                return apology("Not a valid quantity")
            elif qty < 1:
                return apology("Not a valid quantity")
        except:
            return apology("Invalid quantity")

        sell = request.form.get("symbol")
        if sell == "select":
            return apology("Please select a stock")
        curr = db.execute("SELECT quantity FROM portfolio WHERE symbol=?", sell)[0]["quantity"]
        if qty > (curr):
            return apology("Not a valid quantity")

        temp = lookup(sell)
        if temp != None:
            name = temp["name"]
            price = (temp["price"])
            sell = (temp["symbol"])
            total = price*qty
            db.execute(
                "UPDATE portfolio set quantity=quantity-? WHERE userid=? and symbol=?", qty, userid, sell)
            db.execute("DELETE FROM portfolio WHERE quantity=0")
            db.execute("INSERT INTO logs (userid, company, symbol, price, quantity, type) VALUES (?,?,?,?,?,'sell')",
                       userid, name, sell, price, qty)
            db.execute("UPDATE users set cash=cash+? where id=?", total, userid)
            return redirect("/")
        else:
            return apology("Stock does not exist!")
    rows = db.execute("SELECT symbol FROM portfolio WHERE userid=?", userid)
    return render_template("sell.html", rows=rows)


@app.route("/meme", methods=["GET", "POST"])
def meme():
    if request.method == "POST":
        top = request.form.get("top")
        bottom = request.form.get("bottom")
        return apology1(top, bottom)

    return render_template("meme.html")


@app.route("/topup", methods=["GET", "POST"])
def topup():
    if request.method == "POST":
        userid = session["user_id"]
        cash = request.form.get("cash")
        db.execute("UPDATE users set cash=cash+? where id=?", cash, userid)
        return redirect("/")

    return render_template("topup.html")
