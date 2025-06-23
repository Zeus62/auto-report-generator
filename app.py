from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        title = request.form.get('title')
        category = request.form.get('category')
        date = request.form.get('date')
        summary = request.form.get('summary')

        print("Received form data:")
        print("Name:", name)
        print("Email:", email)
        print("Title:", title)
        print("Category:", category)
        print("Date:", date)
        print("Summary:", summary)

        return "Form submitted successfully! (Check your terminal)"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
