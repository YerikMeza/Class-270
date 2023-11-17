from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant



app = Flask(__name__)
fake = Faker()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def generate_token():
	TWILIO_ACCOUNT_SID = 'ACdd1a2772bd18cc179d9c099e164d04ad'
	TWILIO_SYNC_SERVICE_SID = 'ISecff86a9f14251cee60572138b8bf426'
	TWILIO_API_KEY = 'SK77ba003355a912df6d81e0b4fba716cd'
	TWILIO_API_SECRET = 'Bd7diWAJFXG36HaSGBKDvTaVggOYX38N'

	username = request.args.get('username', fake.user_name())

	token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)

	sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
	token.add_grant(sync_gran_access)
	return jsonify(identity=username, token=token.to_jwt().decode())


if __name__ == "__main__":
    app.run()

