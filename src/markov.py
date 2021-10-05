import markovify

class MarkovGen:

  def __init__(self):
    self.generator = None
    self.prefix = "wordlists"

  def get_chef(self) -> str:
    with open(self.prefix + "/cooking.txt") as f:
      text = f.read()
      text_model = markovify.Text(text)
    return text_model.make_short_sentence(100)

  def get_death(self) -> str:
    with open(self.prefix + "/death.txt") as f:
      text = f.read()
      text_model = markovify.Text(text)
    return text_model.make_short_sentence(100)

