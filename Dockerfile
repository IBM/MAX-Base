FROM continuumio/miniconda3:4.5.4

WORKDIR /workspace
RUN mkdir assets

COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
