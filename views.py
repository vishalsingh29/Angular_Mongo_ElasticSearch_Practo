from models import Doctor, City, Review, Specialization, Clinic
from app import db, app
from flask import request, redirect, Blueprint, jsonify, Response, render_template, send_from_directory
from flask.views import MethodView

from elasticsearch import Elasticsearch
from flask.ext.mongoengine.wtf import model_form

es = Elasticsearch()
doctors = Blueprint('doctors', __name__, template_folder='templates')
city = Blueprint('city', __name__, template_folder='templates')


# @app.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory('static/js', path)

# @app.route('/angular/<path:path>')
# def send_angular(path):
#     return send_from_directory('static/angular', path)

# @app.route('/img/<path:path>')
# def send_img(path):
#     return send_from_directory('static/img', path)

@app.route('/')
def get():
    return render_template('index.html')


class ListView(MethodView):

    def get(self):
        doctors = Doctor.objects.all()
        return jsonify(results=doctors)

    def post(self):
        response = Doctor.objects.filter(
            email=request.form['email']).count()
        if response == 0:
            doctor = Doctor()
            for key in request.form:
                doctor[str(key)] = request.form[str(key)]
            print doctor.first_name
            body = {}
            if request.form.has_key('email'):
                body['email'] = request.form['email']
            if request.form.has_key('area'):
                body['area'] = request.form['area']
            if request.form.has_key('city'):
                body['city'] = request.form['city']
            if request.form.has_key('specialization'):
                doctor.specialization = []
                doctor.specialization.append(
                    request.form['specialization'])
                body['specialization'] = request.form['specialization']
            if request.form.has_key('education'):
                doctor.education = []
                doctor.education.append(request.form['education'])
            doctor.save()
            es.create(
                index='test', doc_type='doctor', id=doctor.id, body=body)
            return jsonify(status=True)
        return jsonify(status=False)


class UpdateDoctor(MethodView):

    def get(self, doctor_id):
        doctor = Doctor.objects.get(id=doctor_id)
        responseJson = {}
        responseJson['id'] = str(doctor.id)
        responseJson['name'] = doctor.first_name + " " + doctor.last_name
        responseJson['email'] = doctor.email
        responseJson['phone_number'] = doctor.phone_number
        responseJson['education'] = doctor.education[0]
        responseJson['experience_in_year'] = doctor.experience_in_year
        responseJson['recommendations'] = doctor.recommendations
        responseJson['area'] = doctor.area
        responseJson['city'] = doctor.city
        responseJson['clinics'] = doctor.clinics
        specialization = ', '.join(i for i in doctor.specialization)
        responseJson['specialization'] = specialization
        responseJson['services'] = ', '.join([i for i in doctor.services])
        return jsonify(results=responseJson)
        #return jsonify(results=doctors)

    def post(self, doctor_id):
        response = Doctor.objects.filter(email=request.form['email'])
        if response.count() == 0 or (doctor_id == str(response[0].id) and response.count() == 1):
            doctor = Doctor.objects.get(id=doctor_id)
            for key in request.form:
                if not str(key) == 'clinics':
                    doctor[str(key)] = request.form[str(key)]
            body = {}
            if request.form.has_key('email'):
                body['email'] = request.form['email']
            if request.form.has_key('area'):
                body['area'] = request.form['area']
            if request.form.has_key('city'):
                body['city'] = request.form['city']
            if request.form.has_key('specialization'):
                doctor.specialization = []
                doctor.specialization.append(
                    request.form['specialization'])
                body['specialization'] = request.form['specialization']
            doctor.save()
            es.delete(id=doctor_id, index='test', doc_type='doctor')
            es.create(index='test', doc_type='doctor', id=doctor.id, body=body)
            doctor.save()
            return jsonify(status=True)
        return jsonify(status=False)

    def delete(self, doctor_id):
        doctor = Doctor.objects.get(id=doctor_id)
        es.delete(id=doctor_id, index='test', doc_type='doctor')
        doctor.delete()
        return jsonify(status=True)


class GetAreas(MethodView):

    def get(self, city_name):
        print city_name
        city = City.objects.filter(name=city_name)[0].areas
        return jsonify(results=city)


class AddReview(MethodView):
    form = model_form(Review, exclude=['created_at'])

    def post(self, doctor_id):
        print doctor_id
        form = self.form(request.form)
        review = Review()
        form.populate_obj(review)
        doctor = Doctor.objects.get(id=doctor_id)
        doctor.reviews.append(review)
        doctor.save()
        return jsonify(results=True)


class SearchDoctor(MethodView):

    def get(self, city, area, specialization):
        #print city, area, specialization
        body = {"query": {"bool": {"must": [{"match": {"specialization": specialization}}, {
            "match": {"city": city}}, {"match": {"area": area}}]}}}
        results = es.search(index='test', body=body)
        list_of_doctors = []
        for result in results['hits']['hits']:
            print result
            doctor_object = Doctor.objects.get(id=result['_id'])
            list_of_doctors.append(doctor_object)
        responseJson = []
        for doctor in list_of_doctors:
            res = {}
            res['id'] = str(doctor.id)
            res['name'] = doctor.first_name + " " + doctor.last_name
            res['email'] = doctor.email
            res['phone_number'] = doctor.phone_number
            res['recommendations'] = doctor.recommendations
            res['experience_in_year'] = doctor.experience_in_year
            res['area'] = doctor.area
            res['city'] = doctor.city
            specialization = ', '.join(i for i in doctor.specialization)
            res['specialization'] = specialization
            responseJson.append(res)
        return jsonify(results=responseJson)
        #return jsonify(results=list_of_doctors)


class AddClinic(MethodView):

    def get(self):
        clinic = Clinic.objects.all()
        return jsonify(results=clinic)

    def post(self):
        clinic = Clinic()
        print request.form
        for key in request.form:
            clinic[str(key)] = request.form[str(key)]
        clinic.save()
        return jsonify(status=True)

# class UpdateClinic(MethodView):

#     def get(self, clinic_id):
#         clinic = Clinic.objects.get(id=clinic_id)
#         return jsonify(results=clinic)

#     def post(self,clinic_id):
#         clinic = Clinic.objects.get(id=clinic_id)
#         for key in request.form.keys():
#             doctor.clinic[str(key)] = request.form[str(key)]
#         clinic.save()
#         return jsonify(status=True)
#     def delete(self,clinic_id):
#         clinic = Clinic.objects.get(id=clinic_id)
#         clinic.delete()
#         return jsonify(status=True)


class UpdateClinic(MethodView):

    def post(self, doctor_id, index):
        doctor = Doctor.objects.get(id=doctor_id)
        for key in request.form.keys():
            print request.form[str(key)]
            doctor.clinics[int(index)][str(key)] = request.form[str(key)]
        body = {}
        list_of_areas = []
        list_of_cities = []
        for l in doctor.clinics:
            list_of_areas.append(l['area'])
            list_of_cities.append(l['city'])

        body['email'] = doctor.email
        body['specialization'] = doctor.specialization
        body['area'] = list_of_areas
        body['city'] = list_of_cities
        es.delete(id=doctor_id, index='test', doc_type='doctor')
        es.create(index='test', doc_type='doctor', id=doctor.id, body=body)
        doctor.save()
        return jsonify(results=True)


class UpdateSpecialization(MethodView):

    def post(self, doctor_id, index):
        doctor = Doctor.objects.get(id=doctor_id)
        print request.form
        doctor.specialization[int(index)] = request.form['name']
        body = {}
        list_of_areas = []
        list_of_cities = []
        for l in doctor.clinics:
            list_of_areas.append(l['area'])
            list_of_cities.append(l['city'])

        body['email'] = doctor.email
        body['specialization'] = doctor.specialization
        body['area'] = list_of_areas
        body['city'] = list_of_cities
        es.delete(id=doctor_id, index='test', doc_type='doctor')
        es.create(index='test', doc_type='doctor', id=doctor.id, body=body)
        doctor.save()
        return jsonify(results=True)


class AddClinicDoctor(MethodView):

    def post(self, doctor_id):
        print request.form
        doctor = Doctor.objects.get(id=doctor_id)
        doctor.clinics.append(request.form)
        body = {}
        list_of_areas = []
        list_of_cities = []
        for l in doctor.clinics:
            list_of_areas.append(l['area'])
            list_of_cities.append(l['city'])

        body['email'] = doctor.email
        body['specialization'] = doctor.specialization
        body['area'] = list_of_areas
        body['city'] = list_of_cities
        es.delete(id=doctor_id, index='test', doc_type='doctor')
        es.create(index='test', doc_type='doctor', id=doctor.id, body=body)
        doctor.save()
        return jsonify(status=True)


class DeleteClinic(MethodView):

    def delete(self, doctor_id, index):
        doctor = Doctor.objects.get(id=doctor_id)
        del doctor.clinics[index]
        doctor.save()
        body = {}
        body['email'] = doctor.email
        body['specialization'] = doctor.specialization
        body['city'] = doctor.city
        for doc in doctor.clinics:
            body['area'].append(doc['area'])
        es.delete(id=doctor_id, index='test', doc_type='doctor')
        es.create(index='test', doc_type='doctor', id=doctor.id, body=body)
        return jsonify(results=True)


class AddSpecializationDoctor(MethodView):

    def post(self, doctor_id):
        doctor = Doctor.objects.get(id=doctor_id)
        flag = 0
        for specialization in doctor.specialization:
            if str(specialization).lower() == str(request.form['specialization']).lower():
                flag = 1
        if flag == 0:
            doctor.specialization.append(request.form['specialization'])
        body = {}
        body['email'] = doctor.email
        body['area'] = doctor.area
        body['city'] = doctor.city
        body['specialization'] = doctor.specialization
        es.delete(id=doctor_id, index='test', doc_type='doctor')
        es.create(index='test', doc_type='doctor', id=doctor.id, body=body)
        doctor.save()
        return jsonify(results=True)


class RemoveSpecializationDoctor(MethodView):

    def delete(self, doctor_id, index):
        doctor = Doctor.objects.get(id=doctor_id)
        list_of_specialization = []
        del doctor.specialization[int(index)]
        for special in doctor.specialization:
            list_of_specialization.append(special)
        doctor.specialization = list_of_specialization
        body = {}
        body['email'] = doctor.email
        body['area'] = doctor.area
        body['city'] = doctor.city
        print body
        body['specialization'] = doctor.specialization
        es.delete(id=doctor_id, index='test', doc_type='doctor')
        es.create(index='test', doc_type='doctor', id=doctor.id, body=body)
        doctor.save()
        return jsonify(results=True)


class AddSpecialization(MethodView):

    def post(self):
        specialization = Specialization(
            name=request.form['specialization'].lower())
        specialization.save()
        return jsonify(result=True)


class SearchByName(MethodView):

    def get(self, name):
        doctor = Doctor.objects.filter(first_name=name)
        return jsonify(results=doctor)


class SearchByEmail(MethodView):

    def get(self, email):
        doctor = Doctor.objects.filter(email=email)
        return jsonify(results=doctor)


class SearchByCity(MethodView):

    def get(self, city):
        doctor = Doctor.objects.filter(city=city)
        return jsonify(results=doctor)

doctors.add_url_rule('/doctor', view_func=ListView.as_view('list'))
doctors.add_url_rule(
    '/doctor/<doctor_id>', view_func=UpdateDoctor.as_view('update'))
doctors.add_url_rule('/city/<city_name>', view_func=GetAreas.as_view('city'))
doctors.add_url_rule(
    '/add_review/<doctor_id>', view_func=AddReview.as_view('reviews'))
doctors.add_url_rule('/<city>/<area>/<specialization>',
                     view_func=SearchDoctor.as_view('search_doctor'))
doctors.add_url_rule(
    '/update_clinic/<doctor_id>/<index>', view_func=UpdateClinic.as_view('update_clinic'))
doctors.add_url_rule(
    '/clinic', view_func=AddClinic.as_view('add_clinic'))
doctors.add_url_rule('/add_specialization/<doctor_id>',
                     view_func=AddSpecializationDoctor.as_view('add_specialization'))
doctors.add_url_rule('/update_specialization/<doctor_id>/<index>',
                     view_func=UpdateSpecialization.as_view('update_specialization'))
doctors.add_url_rule('/delete_specialization/<doctor_id>/<index>',
                     view_func=RemoveSpecializationDoctor.as_view('remove_specialization'))
doctors.add_url_rule(
    '/add/specialization', view_func=AddSpecialization.as_view('add/specialization'))
doctors.add_url_rule('/delete_clinic/<doctor_id>/<int:index>',
                     view_func=DeleteClinic.as_view('delete_clinic'))
doctors.add_url_rule('/add_clinic/<doctor_id>',
                     view_func=AddClinicDoctor.as_view('add_clinic_doctor'))
doctors.add_url_rule(
    '/search_name/<name>', view_func=SearchByName.as_view('search_name'))
doctors.add_url_rule(
    '/search_email/<email>', view_func=SearchByEmail.as_view('search_email'))
doctors.add_url_rule(
    '/search_city/<city>', view_func=SearchByCity.as_view('search_city'))
