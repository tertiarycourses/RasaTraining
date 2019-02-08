import rasa_core
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core import config

interpreter = RasaNLUInterpreter('./models/test1/nlu')
action_endpoint = EndpointConfig(url="http://localhost:5005/webhook")
agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
rasa_core.run.serve_application(agent ,channel='cmdline')
		
