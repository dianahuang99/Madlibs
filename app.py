from flask import Flask, request, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
debug = DebugToolbarExtension(app)
prompts = stories.story.prompts


@app.route("/")
def index():
    """Return homepage."""
    return render_template("home.html", prompts=prompts)

@app.route('/story')
def get_stories():
    answers = {}
    for prompt in prompts:
        answers[f"{prompt}"]=request.args[f"{prompt}"]
    text = stories.story.generate(answers)
    return render_template("story.html", prompts_taken=answers, text=text)