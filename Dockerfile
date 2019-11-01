FROM continuumio/miniconda3:4.7.12

WORKDIR /workspace
RUN mkdir assets

COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
