from flask import Blueprint, request, render_template
from processing import calculate_sum, calculate_mode, calculate_difference, calculate_product, calculate_quotient
views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")
    # return '''
    # <html>
    #  <body>
    #   <div style="display:flex; flex-direction: horizontal; align-items: center;" >
    #    <a href ="/"><img src='https://iconarchive.com/download/i83704/custom-icon-design/mono-general-3/home.ico' style="width:auto; height: 1.5em; " ></a>
    #    <h1> &nbsp; Home </h1>
    #   </div>
    #   <p style="font-size: 20px;" ><a href ="/addition">Addition Calculator </a>
    #   <p style="font-size: 20px;" ><a href ="/subtraction">Subtraction Calculator </a>
    #   <p style="font-size: 20px;" ><a href ="/mode">Mode Calculator </a>
    # </html>
    # '''


@views.route('/addition', methods=["GET", "POST"])
def addition_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number2"])
        if number1 is not None and number2 is not None:
            result = calculate_sum(number1, number2)
            return render_template("result.html", result=result, link='/addition')

    return render_template("calculation.html", header="Addition", errors=errors)


@views.route('/subtraction', methods=["GET", "POST"])
def subtraction_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number2"])
        if number1 is not None and number2 is not None:
            result = calculate_difference(number1, number2)
            return render_template("result.html", result=result, link='/subtraction')

    return render_template("calculation.html", header="Subtraction", errors=errors)


@views.route('/multiplication', methods=["GET", "POST"])
def multiplication_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number2"])
        if number1 is not None and number2 is not None:
            result = calculate_product(number1, number2)
            return render_template("result.html", result=result, link='/multiplication')

    return render_template("calculation.html", header="Multiplication", errors=errors)


@views.route('/division', methods=["GET", "POST"])
def division_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number2"])
        if number1 is not None and number2 is not None:
            result = calculate_quotient(number1, number2)
            return render_template("result.html", result=result, link='/division')

    return render_template("calculation.html", header="Division", errors=errors)


inputs = []


@views.route("/mode", methods=["GET", "POST"])
def mode_page():
    errors = ""
    numbers_so_far = ""
    if request.method == "POST":
        try:
            inputs.append(float(request.form["number"]))
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(
                request.form["number"])
        if request.form["action"] == "Calculate number":
            result = calculate_mode(inputs)
            inputs.clear()
            return '''
             <html>
              <body>
               <p>{result}</p>
               <p><a href="/mode">Click here to calculate again</a>
              </body>
             </html>
            '''.format(result=result)
    if len(inputs) == 0:
        numbers_so_far = ""
    else:
        numbers_so_far = "<p>Numbers so far: </p>"
        for number in inputs:
            numbers_so_far += "<p>{}</p>".format(number)
    return '''
        <html>
            <body>
            <div style="display:flex; flex-direction: horizontal; align-items: center;" >
             <a href ="/"><img src='https://iconarchive.com/download/i83704/custom-icon-design/mono-general-3/home.ico' style="width:auto; height: 1.5em; " ></a>
             <h1> &nbsp; Mode Calculator </h1>
            </div>
                {numbers_so_far}
                {errors}
                <p>Enter your number:</p>
                <form method="post" actions=".">
                    <p><input name="number" /></p>
                    <p><input type="submit" name="action" value="Add another" /></p>
                    <p><input type="submit" name="action" value="Calculate number" /></p>
                </form>
            </body>
        </html>
    '''.format(numbers_so_far=numbers_so_far, errors=errors)
