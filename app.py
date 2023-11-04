import surveys
from flask import Flask, request, flash, render_template, redirect, session, make_response
app = Flask(__name__, static_folder="static")
app.config["SECRET_KEY"] = "samie"


responses = []
survey_types = {'personality_quiz': surveys.personality_quiz, 'satisfaction_survey': surveys.satisfaction_survey}
survey = None
num_of_survey_questions = None
current_question =0
response_dict = {}


# homepage route
@app.route("/")
def home_page():
  instructions = surveys.personality_quiz.instructions
  return render_template("index.html", instructions=instructions)

# Route to show one question at a time
@app.route("/questions/<int:id>", methods=["POST"])
def show_questions(id):
  global survey
  global num_of_survey_questions
  survey = request.form["survey"]
  num_of_survey_questions = len(survey_types.get(survey, "None").questions)
  session["user_responses"] = []

  if id < num_of_survey_questions:
      title = survey_types.get(survey, "New").title
      question = survey_types.get(survey, "New").questions[id].question
      return render_template("questions.html", survey=title, question=question, question_id=id)
  else:
    flash("Thank you for your valuable feedback.")
    return render_template("done.html")


@app.route("/questions/<int:id>")
def show_question(id):
    global current_question
    global num_of_survey_questions

    if "current_question" not in session:
        session["current_question"] = 0  # Initialize session variable

    current_question = session["current_question"]
    if current_question >= num_of_survey_questions:
        flash("Thank you for your valuable feedback.")
        return redirect("/done")
    elif id == current_question:
        title = survey_types.get(survey, "New").title
        question = survey_types.get(survey, "New").questions[current_question].question
        return render_template("questions.html", survey=title, question=question, question_id=current_question)
    else:
        next_url = f"/questions/{current_question}"
        flash("Invalid URL: Please answer the current question!")
        return redirect(next_url)

@app.route("/answer", methods=["POST"])
def get_answer():
    global current_question
    global num_of_survey_questions

    answered_qsn = survey_types.get(survey, "New").questions[current_question].question
    answer = request.form["answer"]
    responses.append(answer)

    # Add to session
    user_respo = session["user_responses"]
    user_respo.append(answer)
    session["user_reponses"] = user_respo

    # Add to the dict
    response_dict[answered_qsn] = answer
    current_question += 1
    session["current_question"] = current_question

    if current_question < num_of_survey_questions:
        next_url = f"/questions/{current_question}"
        return redirect(next_url)
    else:
        current_question = 0  # Reset the variable when the survey is done
        session["current_question"] = current_question
        flash("Thank you for your valuable feedback.")
        return redirect("/done")
    

@app.route("/done")
def quiz_done():
  all_questions = survey_types.get(survey, "New").questions

  return render_template("done.html", questions = all_questions, response_dict = response_dict)

# Working with coookies
@app.route("/cookie-form")
def show_cookie_form():
   return render_template("cookie-form.html")

@app.route("/cookies")
def make_cookies():
   fav_color = request.args["cookie_name"]
   html = render_template("show-cookies.html", fav_color=fav_color)
   res = make_response(html)
   res.set_cookie("fav_color", fav_color)
   return res