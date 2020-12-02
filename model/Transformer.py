from transformers import pipeline
from typing import Optional


class Model:
    def __init__(self, initialise_all: Optional[bool] = False):
        print('Initialising...')
        if initialise_all:
            self.question_answering = pipeline('question-answering')
            self.text_generator = pipeline('text-generation')
            self.summarizer = pipeline("summarization")
            print('Initialised: 1) Question answering, 2) Text generator, 3) Summariser')
        else:
            self.text_generator = pipeline('text-generation')
            print('Initialised 1) Text generator')

    def question_answer(self, context: str, question: str) -> str:
        """[summary]

        Args:
            context (str): [description]
            question (str): [description]

        Returns:
            str: [description]
        """
        answer = self.question_answering(question, context=context)
        return answer

    def text_generation(self, sentence_start: str, max_length: Optional[int] = 100) -> str:
        """Generate text from a sentence start

        Args:
            sentence_start (str): Start of a sentence from which to generate
            max_length (Optional[int], optional): Max length of generated text. Defaults to 50.

        Returns:
            str: generated text
        """
        generated_text = self.text_generator(sentence_start,
                                             max_length, do_Sample=False)
        return generated_text

    def summarise(self, article: str) -> str:
        """[summary]

        Args:
            article (str): [description]

        Returns:
            str: [description]
        """
        summarised = self.summarizer(
            article, max_length=130, min_length=30, do_sample=False)
        return summarised
