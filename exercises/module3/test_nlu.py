from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/test1/nlu")
message = "i need some help"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))
