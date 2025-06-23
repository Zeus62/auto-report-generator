from flask import Flask, render_template, request , make_response
from weasyprint import HTML 
import sqlite3

app = Flask(__name__)

import sqlite3

def init_db():
    conn = sqlite3.connect('reports.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            title TEXT,
            category TEXT,
            date TEXT,
            summary TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Call this once at app startup
init_db()

@app.route('/', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        title = request.form.get('title')
        category = request.form.get('category')
        date = request.form.get('date')
        summary = request.form.get('summary')

        # Save to DB
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reports (name, email, title, category, date, summary)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, email, title, category, date, summary))
        conn.commit()
        conn.close()

        # Generate PDF (your existing code)
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
