FROM 873668083085.dkr.ecr.eu-west-2.amazonaws.com/text-improve:model
FROM python:3.7-slim

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/"
COPY --from=0 /root/.local /root/.local
COPY --from=0 /usr/src/model /usr/src/model

WORKDIR /usr/src/server
COPY . .

RUN pip install --user -r ./requirements.txt
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]