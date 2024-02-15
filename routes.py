from flask import Flask, render_template
from models import db, Estudiante, Asignatura, Asistencia

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    estudiantes = Estudiante.query.all()
    asignaturas = Asignatura.query.all()
    return render_template('index.html', estudiantes=estudiantes, asignaturas=asignaturas)

if __name__ == '__main__':
    app.run(debug=True)