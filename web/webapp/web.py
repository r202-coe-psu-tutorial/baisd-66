from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = "change it when deploy"
