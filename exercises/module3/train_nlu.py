from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer

def train_nlu(data, configs, model_dir,model_name):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir,fixed_model_name = model_name)
	
if __name__ == '__main__':
	train_nlu('./nlu.md', 'nlu_config.yml', './models/','testnlu')

