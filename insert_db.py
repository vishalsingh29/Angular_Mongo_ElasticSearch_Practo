from random import randint
from faker import Factory
fake = Factory.create('en_US')
from Project import Doctor
from flask.views import MethodView

from elasticsearch import Elasticsearch
from flask.ext.mongoengine.wtf import model_form

es = Elasticsearch()


def ins():
    first_name = "Aditya"
    last_name = "Sharma"
    email = "aditya@gmail.com"
    phone_number = "8003580290"
    education = [
                {"college":"BITS Pilani","degree":"MBBS","year":"1992"},
                {"college":"BIT Mesra","degree":"Medicine","year":"1995"}
    ]
    experience_in_year = 10
    recommendations = 0
    description = "very experiened"
    area = "Gandhi Nagar"
    city = "Ahmedabad"
    services = ["Xray","MRI"]
    specialization = [
        "Dentist",
        "Psychologist"
    ]
    clinics = [
                { "area":"BTM", "city":"Bangalore", "fees":"600",
                "clinicName" : "XRAY Clinic", "timings":"12:00pm to 10:00pm" },
                { "area":"JP Nagar", "city":"Bangalore", "fees":"600",
                "clinicName" : "JP Clinic", "timings":"12:00am to 10:00am" },
    ]

    doc = Doctor(
        {

            "first_name" : first_name,
            "last_name" : last_name,
            "email" : email,
            "phone_number" : phone_number,
            "education" : education,
            "experience_in_year" : experience_in_year,
            "recommendations" : recommendations,
            "description" : description,
            "area" : area,
            "city" : city,
            "services" : services,
            "specialization" : specialization,
            "clinics" : clinics
        }
    )
    doc.save()
    body = {}
    body['email'] = email
    body['area'] = area
    body['city'] = city
    body['specialization'] = specialization
    es.create(
        index='test', doc_type='doctor', id=doc.id, body=body)
