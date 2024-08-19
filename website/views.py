from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, Flask, send_from_directory
from flask_login import login_required, current_user
from .models import Story
from . import db
import os
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'website/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        file = request.files['image']

        if len(title) < 1:
            flash('Title is too short!', category='error')
        elif len(content) < 1:
            flash('Content is too short!', category='error')
        
        elif file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            image = file.filename
            new_story = Story(title=title, image=image, content=content, user_id=current_user.id)
            db.session.add(new_story)
            db.session.commit()
            flash('Story added!', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('No file selected.', category='error')

    return render_template("home.html", user=current_user)

@views.route('/delete-story', methods=['POST'])
def delete_story():
    story = json.loads(request.data)
    storyId = story['storyId']
    story = Story.query.get(storyId)
    if story:
        if story.user_id == current_user.id:
            db.session.delete(story)
            db.session.commit()


    return jsonify({})

