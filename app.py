from flask import Flask, render_template, request , make_response
from weasyprint import HTML 
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

        rendered = render_template('report_template.html', 
                                   name=name, title=title, category=category, date=date, summary=summary)

        pdf = HTML(string=rendered).write_pdf()

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename="{title}.pdf"'

        return response

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
