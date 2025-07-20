from app.model.abstract_llm import AbstractLLM
from app.utils.url.url import get_html_page_text
from app.utils.url.url import scrape_stripe_treasury_marketing_policy
from app.utils.token.token import count_tokens_in_prompt
from llama_index.llms import OpenAI
from llama_index.prompts import PromptTemplate
from os import environ

class ZeroShot(AbstractLLM):
    def __init__(self, temperature=0.1, model="gpt-3.5-turbo"):
        self.llm = OpenAI(temperature=temperature, model=model)
        self.context_str = scrape_stripe_treasury_marketing_policy(environ["STRIPE_URL"])

    def get_specific_text(self, url):
        return get_html_page_text(url)
    
    def check_for_compliance(self, target_str, template):
        qa_template = PromptTemplate(template)
        prompt = qa_template.format(context_str=self.context_str, query_str=target_str)
        count_tokens_in_prompt(prompt)
        result = self.llm.complete(prompt)
        return result.text
