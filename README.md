# marketing-compliance-llm

```
# set below variables in your .env unless using export
STRIPE_URL=https://stripe.com/docs/treasury/marketing-treasury
OPENAI_API_KEY=sk-F3Jo***********************************VnDGP
```
### How to run the application on your local:
1. Go to ```marketing-compliance-llm```
2. To create a ```.venv```, run ```python3 -m venv .venv```
3. Run ```source .venv/bin/activate``` to activate virtual environment.
4. Create ```.env``` and paste shared env variables to it.
   Run ```1. set -a``` ```2. source .env``` ```3. set +a``` to set env variables. Or, export them manually ```export VAR=value``` in terminal.
5. Now, install dependencies ```pip3 install -r requirements.txt```.
6. Finally, run ```uvicorn app.main:app```
7. go to http://localhost:8000/docs

### Curl :-
``` There are two ways I decided to approach this. One is, RAG(Retrieval Augmentation) and Zero Shot ```
##### RAG Model
```
curl -X 'POST' \
  'http://localhost:8000/rag' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://www.joinguava.com/index.html"
}'
```

##### Zero Shot Model
```
curl -X 'POST' \
  'http://localhost:8000/fscot' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://www.joinguava.com/index.html"
}'
```
