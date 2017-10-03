#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "shipping.cost":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("shipping-zone")

    cost = {'Hypatia':'Creekside C, 2nd Floor', 'Darwin':'Creekside C, 1st Floor', 'Tesla':'Creekside C, 1st Floor', 'Jobs':'Creekside C, 1st Floor', 'Aristotle':'Creekside C, 2nd Floor', 'Archimedes':'Creekside C, 2nd Floor', 'Bohr':'Creekside C, 1st Floor', 'Da Vinci':'Creekside C, 1st Floor', 'Hawking':'Creekside C, 1st Floor', 'Plato':'Creekside C, 2nd Floor', 'Newton':'Creekside C, 1st Floor', 'Hobbes':'Creekside C, 1st Floor', 'Socrates':'Creekside C, 2nd Floor', 'DeBeuvoir':'Creekside C, 1st Floor', 'Pasteur':'Creekside C, 1st Floor', 'Indiana Jones':'Creekside E, 1st Floor', 'Sam Spade':'Creekside E, 2nd Floor', 'Captain Kirk':'Creekside E, 1st Floor', 'Harry Potter':'Creekside E, 2nd Floor', 'Frodo':'Creekside E, 1st Floor', 'Nemo':'Creekside E, 2nd Floor', 'Wonder Woman':'Creekside E, 1st Floor', 'Batman':'Creekside E, 1st Floor', 'Frankenstein':'Creekside E, 2nd Floor', 'GodFather':'Creekside E, 2nd Floor', 'Satine':'Creekside E, 1st Floor', 'Terminator':'Creekside E, 1st Floor', 'King Kong':'Creekside E, 1st Floor', 'Jack Sparrow':'Creekside E, 1st Floor', 'Ripley':'Creekside E, 1st Floor', 'Homer':'Creekside E, 2nd Floor', 'Blues Brothers':'Creekside E, 1st Floor', 'Willy Wonka':'Creekside E, 2nd Floor', 'Bond':'Creekside E, 1st Floor', 'Ferris Bueller':'Creekside E, 2nd Floor', 'Darth Vader':'Creekside E, 2nd Floor', 'ET':'Creekside E, 2nd Floor', 'Three Stooges':'Creekside E, 1st Floor', 'Rocky':'Creekside E, 2nd Floor', 'Mary Poppins':'Creekside E, 2nd Floor', 'Diamond':'Creekside F, 1st Floor', 'Aquamarine':'Creekside F, 1st Floor', 'Emerald':'Creekside F, 1st Floor', 'Garnet':'Creekside F, 1st Floor', 'Jade':'Creekside F, 1st Floor', 'Amethyst':'Creekside F, 1st Floor', 'Amber':'Creekside F, 1st Floor', 'Zircon':'Creekside F, 1st Floor', 'Azurite':'Creekside F, 1st Floor', 'Opal':'Creekside F, 1st Floor', 'Gold':'Creekside F, 1st Floor', 'Silver':'Creekside F, 1st Floor', 'Pearl':'Creekside F, 1st Floor', 'Ruby':'Creekside F, 2nd Floor', 'Sapphire':'Creekside F, 2nd Floor', 'Topaz':'Creekside F, 2nd Floor', 'Tiger Eye':'Creekside F, 2nd Floor', 'Citrine':'Creekside F, 2nd Floor', 'Peridot':'Creekside F, 2nd Floor', 'Coral':'Creekside F, 2nd Floor', 'Rhodonite':'Creekside F, 2nd Floor', 'Pyrite':'Creekside F, 2nd Floor', 'Tourmaline':'Creekside F, 2nd Floor', 'Spinel':'Creekside F, 2nd Floor'}

    speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) + " euros."

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
