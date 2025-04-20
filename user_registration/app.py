from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Registro exitoso para el usuario: {}'.format(form.nombre.data), 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
