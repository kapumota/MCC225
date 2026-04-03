FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8899 \
    MPLCONFIGDIR=/tmp/matplotlib

ARG INSTALL_OPCIONAL=true
ARG TORCH_FLAVOR=cpu

WORKDIR /workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    wget \
    tini \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-base.txt requirements-opcional.txt ./

RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install -r requirements-base.txt && \
    pip install --index-url https://download.pytorch.org/whl/${TORCH_FLAVOR} \
        torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 && \
    if [ "$INSTALL_OPCIONAL" = "true" ]; then \
        pip install -r requirements-opcional.txt; \
    fi

RUN python -m nltk.downloader punkt stopwords wordnet omw-1.4 averaged_perceptron_tagger && \
    python -m spacy download es_core_news_sm

EXPOSE 8899

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["sh", "-c", "jupyter lab --ip=0.0.0.0 --port=${PORT} --no-browser --allow-root --ServerApp.root_dir=/workspace"]
