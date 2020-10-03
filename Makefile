PORT := 8080

run:
	uvicorn server:app --reload --log-level debug --port $(PORT)
