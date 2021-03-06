from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.train import interactive
from rasa_core.utils import EndpointConfig


def nlu_train_interactive(interpreter,
                       domain_file="domain.yml",
                       training_data_file='stories.md'):
    action_endpoint = EndpointConfig(url="http://localhost:5005/webhook")						  
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), 
                  KerasPolicy(max_history=3, epochs=3, batch_size=50)],
                  interpreter=interpreter,
                  action_endpoint=action_endpoint)
    				  
    data = agent.load_data(training_data_file)			   
    agent.train(data)
    interactive.run_interactive_learning(agent, training_data_file)
    return agent


if __name__ == '__main__':
    nlu_interpreter = RasaNLUInterpreter('./models/test1/nlu/')
    nlu_train_interactive(nlu_interpreter)