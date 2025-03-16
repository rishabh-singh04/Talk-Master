FROM python:3.9
COPY ./frontend /app
WORKDIR /app
RUN pip install streamlit
CMD ["streamlit", "run", "app.py"]