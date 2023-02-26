import openai
from typing import Dict, List, Tuple
import numpy as np
import tiktoken

COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"
organization = ""
openai.api_key = ""

MAX_SECTION_LEN = 500
SEPARATOR = "\n* "
ENCODING = "gpt2"  # encoding for text-davinci-003

encoding = tiktoken.get_encoding(ENCODING)
separator_len = len(encoding.encode(SEPARATOR))

EMBEDDINGS_HEADER = """Answer the question as truthfully as possible using the provided context, and if the answer is not contained, then make your best inference. Respond in the style and mannerisms of James Charles. You should use emojis in your response at the end of a sentence. At the end of your response give a suggestion for a message to send in chat. "\n\nContext:\n"""


def filterMessage(message, fltr) -> str:
	print("fm: " + fltr)

	completion = openai.Completion.create(
		model=COMPLETIONS_MODEL,
		prompt="Are any of the words in this message, '" + message + "', contained in this filter: " + fltr + "? It is possible that the words in the message are misspelled, are synonyms, or closely-related to the filter. Please take this into consideration when checking. If so, respond only with 'yes'. If not, respond only with 'no'.",
		temperature=0,
		max_tokens=320,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0
	)
	print("completed")
	return completion.choices[0].text.strip()

