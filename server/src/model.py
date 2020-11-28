from transformers import pipeline
from typing import Optional


def question_answer(context: str, question: str) -> str:
  """[summary]

  Args:
      context (str): [description]
      question (str): [description]

  Returns:
      str: [description]
  """
  nlp = pipeline("question-answering")
  answer = nlp(question, context=context)
  return answer


def text_generation(sentence_start: str, max_length: Optional[int] = 50) -> str:
  """Generate text from a sentence start

  Args:
      sentence_start (str): Start of a sentence from which to generate
      max_length (Optional[int], optional): Max length of generated text. Defaults to 50.

  Returns:
      str: generated text
  """
  text_generation = pipeline('text-generation')
  generated_text = text_generation(sentence_start,
                        max_length, do_Sample=False)
  return generated_text


def summarise(article: str) -> str:
  """[summary]

  Args:
      article (str): [description]

  Returns:
      str: [description]
  """
  summarizer = pipeline("summarization")
  summarised = summarizer(article, max_length=130, min_length=30, do_sample=False))
  return summarised
