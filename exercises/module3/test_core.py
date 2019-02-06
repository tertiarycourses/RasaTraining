from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.agent import Agent

fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                          core_threshold=0.3,
                          nlu_threshold=0.3)

agent = Agent("domain2.yml", policies=[KerasPolicy(), fallback])

data = agent.load_data("stories2.md")
agent.train(data)