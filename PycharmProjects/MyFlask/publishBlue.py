from flask import Blueprint

publish_blue=Blueprint('publish',__name__)

@publish_blue.route('/publish')
def publish():
    return "BLUEPRINT"