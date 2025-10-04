
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime 

cred=credentials.Certificate('serviceAccount.json')

app = firebase_admin.initialize_app(cred)
db = firestore.client()


# doc_ref = db.collection("task").document("homework")
# doc_ref.set({"Name": "assignment", "done": False, "date": datetime.datetime.now()})
