from flask_cors import CORS

cors = CORS(
    resources={r"/*": {"origins": ["http://127.0.0.1:5000"]}},
    supports_credentials=True
)
