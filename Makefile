.PHONY: up build pipeline create-service-account login run

build:
	docker compose build

up: build
	docker compose up -d

# Open an interactive shell in the app container:
shell:
	docker compose exec app bash

# Create a ZenML service account (run from inside app container after 'shell')
create-service-account:
	zenml service-account create demo-sa || true
	zenml service-account api-key demo-sa create --display-name demo-key || true
	zenml service-account list
	zenml service-account api-key demo-sa list

# Login using the API Key (run inside app container; see README to copy the key)
login:
	@echo "Run: zenml login <ZENML_SERVER_URL> --api-key and paste your API key"

# Run pipeline (run inside app container after login or after setting ZENML_STORE_URL & ZENML_STORE_API_KEY)
run:
	python /workspace/app/src/pipeline.py
