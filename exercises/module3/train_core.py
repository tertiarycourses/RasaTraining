from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.agent import Agent

fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                          core_threshold=0.3,
                          nlu_threshold=0.3)

agent = Agent('domain.yml', policies = [MemoizationPolicy(), 
		KerasPolicy(max_history=3, epochs=200, batch_size=50), fallback])

data = agent.load_data("stories.md")
agent.train(data)

agent.persist('./models/dialogue')

