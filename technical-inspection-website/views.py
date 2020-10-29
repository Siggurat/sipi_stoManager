from flask import render_template, request, jsonify

from app import app
from extensions import db
from models import CarModel, Application
from forms import ApplicationForm


@app.route('/', methods=['GET'])
def index():
    application_form = ApplicationForm(meta={'csrf': False})

    return render_template('index.html', application_form=application_form)


@app.route('/brand/<car_brand_id>')
def get_models(car_brand_id):
    models = CarModel.query.filter_by(car_brand_id=car_brand_id).all()

    modelArray = []

    for model in models:
        modelObj = {}
        modelObj['id'] = model.id
        modelObj['name'] = model.name
        modelArray.append(modelObj)

    return jsonify({'models': modelArray})


@app.route('/register-app', methods=['POST'])
def register_application():
    application_form = ApplicationForm(meta={'csrf': False})

    if application_form.validate_on_submit():
        car_brand = request.form['car_brand']
        car_model = request.form['car_model']
        name = request.form['name']
        last_name = request.form['last_name']
        email = request.form['email']
        tel = request.form['tel']

        try:
            application = Application(name=name, last_name=last_name, email=email, tel=tel, car_brand_id=car_brand,
                                      car_model_id=car_model)
            db.session.add(application)
            db.session.commit()

            # !!!
            # Uncomment it if you want to use Mail
            # !!!

            # track_number = application.unique_track_number
            # send_application_registered_msg(name, email, track_number)

            return jsonify({'success': 'Ваша заявка была успешно подана!'})
        except Exception as e:
            return jsonify({'errors': f'Что-то пошло не так, попробуйте снова! {e}'})

    return jsonify({'errors': application_form.errors})


@app.route('/get-app-info/<track_number>')
def get_application_info(track_number):
    if track_number != 'None':
        try:
            application = Application.query.filter_by(unique_track_number=track_number).first()
            application_info = application.serialize()

            return jsonify({'fields': application_info})
        except:
            return jsonify({'error': f'Неверный трек-код. Попробуйте снова!'})
    else:
        return jsonify({'error': 'Введите трек-код!'})


