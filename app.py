# !pip install Flask
# !pip install Flask_Cors

from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

app=Flask(__name__)
cors = CORS(app)
@cross_origin()
@app.route('/',methods=['POST','GET'])
def email_read():
  jsonfile = request.json
  #print(jsonfile)
  #print(type(jsonfile))
  #json_changes = json.dumps(jsonfile,indent=3)
  print(type(jsonfile))
  print(jsonfile)
  for i in range(0,3):
     print(jsonfile['recipents'][i])
  return 'Email Notification System Working',200

if __name__ == '__main__':
  app.run(debug=True)
