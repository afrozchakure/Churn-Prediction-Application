FROM ubuntu

Label Amarkumar Belkhede "belkhedeamar@gmail.com"

WORKDIR /app

RUN apt-get -y update &&\
    apt-get -y install python3 python3-pip

RUN python3 -m pip install --upgrade pip



ADD python_requirements.txt .
RUN python3 -m pip install -r python_requirements.txt

ADD model.py .
ADD server.py .
ADD Telco-Customer-Churn.csv .
ADD serializer.py .
ADD static static
ADD templates templates
ADD model.pkl .
ADD EDA_and_Conclusion.pdf .
# RUN python3 -u modelV1.py

CMD [ "python3", "-u", "./server.py" ]
