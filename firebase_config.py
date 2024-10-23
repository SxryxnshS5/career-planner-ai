import firebase_admin
from firebase_admin import credentials, firestore
import os

# Load the Firebase Admin SDK credentials
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

