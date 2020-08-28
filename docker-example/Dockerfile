FROM python:3.8.2-slim

WORKDIR /usr/app/src

RUN pip install streamlit
RUN pip install bokeh
RUN pip install pandas



COPY streamlit_example/main.py ./main.py
COPY data /data

CMD ["sh", "-c", "streamlit run --server.port $PORT /usr/app/src/main.py"]