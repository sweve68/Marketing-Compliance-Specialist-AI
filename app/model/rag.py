from app.model.abstract_llm import AbstractLLM
from llama_index.llms import OpenAI
from llama_index.prompts import PromptTemplate
from llama_index import VectorStoreIndex
from llama_index import ServiceContext
from app.utils.url.url import get_html_page_text
from app.utils.token.token import count_tokens_in_prompt

class Rag(AbstractLLM):
    def __init__(self, temperature=0.1, model="gpt-3.5-turbo"):
        self.llm = OpenAI(temperature=temperature, model=model)
        self.service_context = ServiceContext.from_defaults(llm=self.llm)

    def index_documents(self, documents):
        self.index = VectorStoreIndex.from_documents(documents)

    def get_specific_text(self, url):
        return get_html_page_text(url)

    def check_for_compliance(self, target_str, template):
        qa_template = PromptTemplate(template)
        prompt = qa_template.format(query_str=target_str)
        count_tokens_in_prompt(prompt)
        query_engine = self.index.as_query_engine(service_context=self.service_context)
        result = query_engine.query(prompt)
        return result.response
