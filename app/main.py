from os import environ
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model.zero_shot import ZeroShot
from app.model.rag import Rag
from llama_index.readers import SimpleWebPageReader
from app.template.template import *
import logging
from datetime import datetime
import json

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Zero shot
zero_shot= ZeroShot()
class FewShotLLMRequest(BaseModel):
    url: str

# RAG
rag = Rag()
class RagLLMRequest(BaseModel):
    url: str

def save_results_to_file(results, file_name, logger):
    file_path = f"app/data/tmp/{file_name}"
    with open(file_path, "w") as file:
        json.dump(results, file)
    logger.info(f"Results saved to: {file_path}")


@app.post("/zero_shot")
async def few_shot_llm(request: FewShotLLMRequest):
    try:
        text_to_check_for_compliance = zero_shot.get_specific_text(request.url)
        result = zero_shot.check_for_compliance(text_to_check_for_compliance, zero_shot_compliance_template)
        save_results_to_file(result, f"zeroShot_results_{datetime.now().strftime('%Y%m%d%H%M%S')}.json", logger)
        logger.info("ZeroShot compliance check successful")
        logger.info(f"Non-compliant results: {result}")
        return {"non_complaint_results": result}
    except Exception as e:
        logger.error(f"Error in FSCOT compliance check: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/rag")
async def rag_llm(request: RagLLMRequest):
    try:
        documents = SimpleWebPageReader(html_to_text=True).load_data([environ["STRIPE_URL"]])
        rag.index_documents(documents)
        text_to_check_for_compliance = rag.get_specific_text(request.url)
        non_complaint_results = rag.check_for_compliance(text_to_check_for_compliance, rag_non_compliance_template)
        save_results_to_file(non_complaint_results, f"rag_non_compliant_results_{datetime.now().strftime('%Y%m%d%H%M%S')}.json", logger)
        logger.info(f"Non-compliant results: {non_complaint_results}")
        complaint_suggestions_results = rag.check_for_compliance(non_complaint_results, rag_suggestion_template)
        logger.info(f"Possible suggestions: {complaint_suggestions_results}")
        logger.info("RAG non-compliance check successful")
        return {"non_complaint_results": non_complaint_results, "suggestions": complaint_suggestions_results}
    except Exception as e:
        logger.error(f"Error in RAG compliance check: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
