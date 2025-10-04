
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime 
import os 
base_dir = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(base_dir, "serviceAccount.json")
cred=credentials.Certificate(cred_path)

app = firebase_admin.initialize_app(cred)
db = firestore.client()


# doc_ref = db.collection("task").document("homework")
# doc_ref.set({"Name": "assignment", "done": False, "date": datetime.datetime.now()})
