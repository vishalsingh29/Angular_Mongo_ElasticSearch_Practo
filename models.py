import datetime
from flask import url_for
from app import db


class Review(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    author = db.StringField(verbose_name="Name", max_length=50, required=True)
    content = db.StringField(
        verbose_name="Content", max_length=255, required=True)


class Doctor(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    first_name = db.StringField(
        verbose_name="FirstName", max_length=50, required=True)
    last_name = db.StringField(
        verbose_name="LastName", max_length=50, required=False)
    email = db.EmailField(
        verbose_name="Email", max_length=50, required=True, unique=True)
    phone_number = db.IntField(
        verbose_name="Phone Number", required=True )
    education = db.ListField(db.StringField(
        verbose_name="Education", max_length=50, required=False))
    experience_in_year = db.IntField(
        verbose_name="ExperienceInYear", default=0, required=False)
    experience_in_month = db.IntField(
        verbose_name="ExperienceInMonth", default=0, required=False)
    recommendations = db.IntField(
        verbose_name="Recommendations", default=0, required=False)
    description = db.StringField(
        verbose_name="Description", max_length=255, required=False)
    experience_description = db.StringField(
        verbose_name="Experience_Description", max_length=255, required=False)
    awards = db.ListField(
        db.StringField(verbose_name="Awards", max_length=100, required=False))
    area = db.StringField(verbose_name="Area", max_length=100, required=False)
    city = db.StringField(verbose_name="City", max_length=100, required=False)
    membership = db.ListField(
        db.StringField(verbose_name="Membership", max_length=100, required=False))
    registration = db.ListField(
        db.StringField(verbose_name="Registration", max_length=100, required=False))
    services = db.ListField(
        db.StringField(verbose_name="Service", max_length=100, required=False))
    clinics = db.ListField(
        db.DictField(verbose_name="Clinic", required=False))
    specialization = db.ListField(
        db.StringField(verbose_name="Specialization", max_length=100, required=False, unique=True))
    reviews = db.ListField(db.EmbeddedDocumentField('Review'))


class City(db.Document):
    name = db.StringField(
        verbose_name="Name", max_length=100, required=True)
    state = db.StringField(
        verbose_name="State", max_length=50, required=True)
    country = db.StringField(
        verbose_name="Country", max_length=50, required=True)
    areas = db.ListField(db.StringField(max_length=100, required=True))


class Clinic(db.Document):
    name = db.StringField(
        verbose_name="Name", max_length=50, required=True)
    clinic_type = db.StringField(
        verbose_name="ClinicType", max_length=50, required=False)
    complete_address = db.StringField(
        verbose_name="Address", max_length=255, required=True)
    area = db.StringField(
        verbose_name="Area", max_length=255, required=True)
    city = db.StringField(
        verbose_name="City", max_length=255, required=True)

class Specialization(db.Document):
    name = db.StringField(
        verbose_name="Name", max_length=50, required=True)
