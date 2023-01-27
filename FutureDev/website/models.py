from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#This is the general class that will hold basic info for EVERY user
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    signup = db.Column(db.DateTime(timezone=True), default=func.now())
    firstName = db.Column(db.String(150))
    lasName = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    latinX = db.Column(db.String(150))
    countryOrigin = db.Column(db.String(150))
    countryResidence = db.Column(db.String(150))
    currentAffiliation = db.Column(db.String(150))
    languages = db.Column(db.String(150))
    timezone = db.Column(db.String(150))
    lxaiUsername = db.Column(db.String(50))
    

#Users who are mentors will have answers to mentro specific questions here
class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    seniorityLevel = db.Column(db.String(150))
    linkToProfessional = db.Column(db.String(150))
    previousMentor = db.Column(db.String(150))
    mentorMotivation = db.Column(db.String(150))
    hoursAvailable = db.Column(db.Integer)
    preferencesMentee = db.Column(db.String(275))
    preferencesMenteeOther = db.Column(db.String(300))
    preferredOutcomes = db.Column(db.String(200))
    preferredOutcomesOther = db.Column(db.String(300))
    openToReview = db.Column(db.Boolean)
    skills = db.Column(db.String(200))
    research = db.Column(db.String(300))
    reviewerWorkshop = db.Column(db.String(50))
    publishedWorkshop = db.Column(db.Boolean)
    reviewerTopTier = db.Column(db.String(50))
    publishedTopTier = db.Column(db.Boolean)
    reviewerAIJournals = db.Column(db.String(50))
    publishedAIJournals = db.Column(db.Boolean)
    conferencePreferences = db.Column(db.String(200))
    conferenceOther = db.Column(db.String(200))



#Users who are mentees will have answers to mentro specific questions here
class Mentee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    currentLevel = db.Column(db.String(150))
    linkToProfessional = db.Column(db.String(150))
    menteeMotivation = db.Column(db.String(150))
    motivationStatementLink = db.Column(db.String(300))
    preferredOutcomes = db.Column(db.String(200))
    careerGoals = db.Column(db.String(500))
    skills = db.Column(db.String(200))
    research = db.Column(db.String(300))
    reviewerWorkshop = db.Column(db.String(50))
    publishedWorkshop = db.Column(db.Boolean)
    reviewerTopTier = db.Column(db.String(50))
    publishedTopTier = db.Column(db.Boolean)
    reviewerAIJournals = db.Column(db.String(50))
    publishedAIJournals = db.Column(db.Boolean)
    conferencePreferences = db.Column(db.String(200))
    conferenceOther = db.Column(db.String(200))
    openToReview = db.Column(db.Boolean)