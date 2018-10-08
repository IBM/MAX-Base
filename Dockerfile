FROM continuumio/miniconda3:4.5.4

WORKDIR /workspace
RUN mkdir assets

COPY requirements.txt /workspace
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /workspace
