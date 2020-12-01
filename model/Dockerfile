FROM python:3.7-slim
ENV PYTHONPATH "${PYTHONPATH}:/usr/src"
ENV PATH=/root/.local/bin:$PATH

WORKDIR /usr/src/model
COPY ./requirements.txt .
RUN pip install --user -r ./requirements.txt
COPY . .



