import os
from datasets import Dataset
from llama_index import ServiceContext
from llama_index import VectorStoreIndex
from llama_index.llms import OpenAI
from llama_index.readers import SimpleWebPageReader
from ragas import evaluate
from ragas.metrics import answer_relevancy, faithfulness

def evaluate_model(model_name, data_file):
    questions = []
    with open(data_file, "r") as f:
        for line in f:
            questions.append(line.strip())

    documents = SimpleWebPageReader(html_to_text=True).load_data(
        [os.environ["STRIPE_URL"]]
    )

    # limit the context window to 2048 tokens so that refine is used
    service_context = ServiceContext.from_defaults(
        llm=OpenAI(model=model_name, temperature=0.1), context_window=2048
    )

    index = VectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine(service_context=service_context)

    contexts = []
    answers = []

    for question in questions[:3]: # raises rate limit error
        response = query_engine.query(question)
        contexts.append([x.node.get_content() for x in response.source_nodes])
        answers.append(str(response))

    ds = Dataset.from_dict(
        {
            "question": questions[:3],
            "answer": answers,
            "contexts": contexts,
        }
    )

    result = evaluate(ds, [answer_relevancy, faithfulness])
    return result