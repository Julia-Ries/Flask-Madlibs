from flask import Flask, render_template, request
from stories import stories 

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)




# simple app
# @app.route("/")
# def show_story():
#     """Show madlibs form."""

#     prompts = story.prompts

#     return render_template("form.html", prompts = prompts)

# @app.route("/answers")
# def show_answers():
#     """show answers in story """

#     text = story.generate(request.args)

#     return render_template("answers.html", text = text)






# Further Study 
@app.route("/")
def show_story():

    return render_template("select-story.html", stories = stories.values())

@app.route("/questions")
def ask_questions():
    """Show madlibs form."""

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template("questions.html", 
                    story_id=story_id,
                    title=story.title,
                    prompts=prompts)

@app.route("/story")
def show_answers():
    """show answers in story """

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("answers.html", 
                            title=story.title,
                            text=text)