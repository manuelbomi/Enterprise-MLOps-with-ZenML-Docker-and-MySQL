FROM python:3.11-slim

WORKDIR /workspace/app

# System deps for mysql client and building packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential default-libmysqlclient-dev libffi-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY run_pipeline.sh /workspace/app/run_pipeline.sh
RUN chmod +x /workspace/app/run_pipeline.sh

ENV PYTHONUNBUFFERED=1

CMD ["/bin/bash"]
