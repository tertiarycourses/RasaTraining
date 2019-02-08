from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/default/testnlu/")
message = "Are you located in CCK"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))


