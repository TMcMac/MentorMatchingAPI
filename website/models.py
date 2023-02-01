from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

#This is the general class that will hold basic info for EVERY user
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    latinX = db.Column(db.String(150))
    countryOrigin = db.Column(db.String(150))
    countryResidence = db.Column(db.String(150))
    currentAffiliation = db.Column(db.String(150))
    languages = db.Column(db.String(150))
    timezone = db.Column(db.String(150))
    lxaiUsername = db.Column(db.String(50))
    signupTimestamp = db.Column(db.DateTime(timezone=True), default=func.now())
    updatedTimestamp = db.Column(db.DateTime(timezone=True), default=func.now())
    password = db.Column(db.String(65))

    def __init__(self, id, email, firstName, lastName, password, gender=None, latinX=None,
                countryOrigin=None, countryResidence=None, currentAffiliation=None, languages=None,
                timezone=None, lxaiUsername=None, signupTimestamp=func.now(), updatedTime=func.now()) -> None:
        self.id = id
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.latinX = latinX
        self.countryOrigin = countryOrigin
        self.countryResidence = countryResidence
        self.currentAffiliation = currentAffiliation
        self.languages = languages
        self.timezone = timezone
        self.lxaiUsername = lxaiUsername
        self.signupTimestamp = signupTimestamp
        self.updatedTimestamp = updatedTime
        self.password = password

    def json(self):
        return {"id" : self.id, "email" : self.email, "firstName" : self.firstName, "lastName" : self.lastName,
                "gender" : self.gender, "latinX" : self.latinX, "countryOrigin": self.countryOrigin,
                "countryResidence" : self.countryResidence, "currentAffiliation" : self.currentAffiliation,
                "languages" : self.languages, "timezone" : self.timezone, "lxaiUsername" : self.lxaiUsername,
                "signupTimestamp" : self.signupTimestamp, "updatedTime" : self.updatedTimestamp}

    

#Users who are mentors will have answers to mentro specific questions here
class Mentor(db.Model):
    __tablename__ = "mentors"
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

    def __init__(self, id, user_id, seniorityLevel, linkToProfessional, previousMentor,
                mentorMotivation, hoursAvailable, preferencesMentee, preferencesMenteeOther,
                preferredOutcomes, preferredOutcomesOther, openToReview, skills, research,
                reviewerWorkshop, publishedWorkshop, reviewerTopTier, publishedTopTier, 
                reviewerAIJournals, publishedAIJournals, conferencePreferences, conferenceOther, updatedTime=func.now()) -> None:

        self.id = id
        self.user_id = user_id
        self.seniorityLevel = seniorityLevel
        self.linkToProfessional = linkToProfessional
        self.previousMentor = previousMentor
        self.mentorMotivation = mentorMotivation
        self.hoursAvailable = hoursAvailable
        self.preferencesMentee = preferencesMentee
        self.preferencesMenteeOther = preferencesMenteeOther
        self.preferredOutcomes = preferredOutcomes
        self.preferredOutcomesOther = preferredOutcomesOther
        self.openToReview = openToReview
        self.skills = skills
        self.research = research
        self.reviewerWorkshop = reviewerWorkshop
        self.publishedWorkshop = publishedWorkshop
        self.reviewerTopTier = reviewerTopTier
        self.publishedTopTier = publishedTopTier
        self.reviewerAIJournals = reviewerAIJournals
        self.publishedAIJournals = publishedAIJournals
        self.conferencePreferences = conferencePreferences
        self.conferenceOther = conferenceOther
        self.updatedTime = updatedTime

    def json(self):
        return {"id" : self.id, "user_id" : self.user_id, "self.seniorityLevel" : self.seniorityLevel, 
                "linkToProfessiona" : self.linkToProfessional, "previousMentor" : self.previousMentor, 
                "mentorMotivation" : self.mentorMotivation, "hoursAvailable" : self.hoursAvailable, 
                "preferencesMentee" : self.preferencesMentee, "preferencesMenteeOther" : self.preferencesMenteeOther, 
                "preferredOutcomes" : self.preferredOutcomes, "preferredOutcomesOther" : self.preferredOutcomesOther, 
                "openToReview" : self.openToReview, "skills" : self.skills, "research" : self.research, 
                "reviewerWorkshop" : self.reviewerWorkshop, "publishedWorkshop": self.publishedWorkshop, 
                "reviewerTopTier" : self.reviewerTopTier, "publishedTopTier" : self.publishedTopTier, 
                "reviewerAIJournals, " : self.reviewerAIJournals, "publishedAIJournals," : self.publishedAIJournals, 
                "conferencePreference" : self.conferencePreferences, "conferenceOther": self.conferenceOther, "updatedAt" : self.updatedTime}




#Users who are mentees will have answers to mentro specific questions here
class Mentee(db.Model):
    __tablename__ = "mentees"
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

    def __init__(self, id, user_id, currentLevel, linkToProfessional, menteeMotivation,
                motivationStatementLink, preferredOutcomes, careerGoals, openToReview, 
                skills, research, reviewerWorkshop, publishedWorkshop, reviewerTopTier, publishedTopTier, 
                reviewerAIJournals, publishedAIJournals, conferencePreferences, conferenceOther, updatedTime=func.now()) -> None:
                
        self.id = id
        self.user_id = user_id
        self.currentLevel = currentLevel
        self.linkToProfessional = linkToProfessional
        self.menteeMotivation = menteeMotivation
        self.motivationStatementLink = motivationStatementLink
        self.preferredOutcomes = preferredOutcomes
        self.careerGoals = careerGoals
        self.openToReview = openToReview
        self.skills = skills
        self.research = research
        self.reviewerWorkshop = reviewerWorkshop
        self.publishedWorkshop = publishedWorkshop
        self.reviewerTopTier = reviewerTopTier
        self.publishedTopTier = publishedTopTier
        self.reviewerAIJournals = reviewerAIJournals
        self.publishedAIJournals = publishedAIJournals
        self.conferencePreferences = conferencePreferences
        self.conferenceOther = conferenceOther
        self.updatedTime = updatedTime


    def json(self):
        return {"id" : self.id, "user_id" : self.user_id, "self.currentLevel" : self.currentLevel, 
                "linkToProfessional" : self.linkToProfessional, "menteeMotivation" : self.menteeMotivation,
                "motivationStatementLin" : self.motivationStatementLink, "preferredOutcomes" : self.preferredOutcomes,
                "careerGoals" : self.careerGoals, "openToReview" : self.openToReview, "skills" : self.skills, "research" : self.research, 
                "reviewerWorkshop" : self.reviewerWorkshop, "publishedWorkshop": self.publishedWorkshop, 
                "reviewerTopTier" : self.reviewerTopTier, "publishedTopTier" : self.publishedTopTier, 
                "reviewerAIJournals, " : self.reviewerAIJournals, "publishedAIJournals," : self.publishedAIJournals, 
                "conferencePreference" : self.conferencePreferences, "conferenceOther": self.conferenceOther, "updatedAt" : self.updatedTime}