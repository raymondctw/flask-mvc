from flask import Blueprint, Flask, request, render_template


admin_blueprint = Blueprint('admin_blueprint', __name__, template_folder = 'templates/admin')

@admin_blueprint.route('/')
@admin_blueprint.route('/Dashboard')
def Dashboard():
    return 'Dashboard'


@admin_blueprint.route('/blog')
def blog():
    return 'blog'







