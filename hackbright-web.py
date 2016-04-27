from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    project_info = hackbright.get_grades_by_github(github)
    print project_info
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            project_info=project_info)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    return render_template("student-add.html")


    


@app.route("/confirmation", methods=['POST'])
def confirm_student():

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name') 
    github = request.form.get('github')
    hackbright.make_new_student(first_name, last_name, github)
    return render_template("confirmation.html",
                            first_name=first_name,
                            last_name=last_name,
                            github=github)

@app.route("/project_information")
def project_information():

    title = request.form.get('title')
    description = request.form.get('description') 
    max_grade = request.form.get('max_grade')
    project_template = hackbright.get_project_by_title(title)
    return render_template("project_information.html",
                            title=title,
                            description=description,
                            max_grade=max_grade,
                            project_template=project_template)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)



