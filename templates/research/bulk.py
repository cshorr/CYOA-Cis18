# I changed the story page, and home file.
#
#
#
# 1. Create a New Template File
# Create a new file, for example, story_page.html, inside your templates directory. This file will "inherit" from your base template and fill in the content block.
# 1. Create a New Template File
# Create a new file, for example, story_page.html, inside your templates directory. This file will "inherit" from your base template and fill in the content block.

{% extends "base.html" %}

{% block title %}{{ scene.title }}{% endblock %}

{% block content %}
<div class="story-content">
    <h2>{{ scene.title }}</h2>
    <p class="where-when">{{ scene.where_when }}</p>

    <pre>{{ scene.text }}</pre>

    <div class="choices">
        {% for choice in scene.choices %}
            <a href="/scene/{{ choice.next_id }}">{{ choice.label }}</a>
        {% endfor %}
    </div>

    <p class="exit-line">{{ scene.exit_line }}</p>
</div>
{% endblock %}

#2. Update Your Flask Route
# You would then modify your Flask route in app.py to render this new template and pass it the data.
from flask import Flask, render_template
import json

app = Flask(__name__)

# Load your JSON data (assuming it's in a file named scenes.json)
with open('scenes.json', 'r') as f:
    game_data = json.load(f)


@app.route('/')
def show_scene():
    # Retrieve the data for the starting scene
    start_scene = game_data['E-001']

    # Render the new template and pass the scene data
    return render_template('story_page.html', scene=start_scene, title=start_scene['title'], theme='your_theme_name')


if __name__ == '__main__':
    app.run(debug=True)

    #In this example, the show_scene function will fetch the data for scene "E-001" and pass it to the story_page.html template. The
    # {{ scene.text }} placeholder in your HTML will then be filled with the text from your JSON file,
    # with the <pre> tag ensuring the newlines are correctly displayed.