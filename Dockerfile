FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install requests pytest
CMD ["python", "weather_agent.py"]


