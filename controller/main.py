from flask import Flask, Blueprint, request, render_template



main_blueprint = Blueprint("main_blueprint",__name__, template_folder= 'templates/main')

@main_blueprint.route('/', methods = ['GET','POST'])
def home():
    return render_template('main/homepage.html')







