FROM tensorflow/tensorflow:latest-gpu

# RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

# RUN pip install --upgrade pip

# RUN apt-get -y install git
# RUN git clone -b feat/transformer https://github.com/shiyoubun/ai-benchmark.git

COPY ./ /app/
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./main.py"]