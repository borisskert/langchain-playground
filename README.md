# langchain playground

This repository serves as a playground for experimenting with the LangChain library. It contains various examples and
snippets to help you get started with building applications using LangChain.

## Getting Started

To get started, install python 3.12 and the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

To run the LangChain playground app, execute the following command:

```bash
streamlit run src/main.py
```

## If you want to use the weather-API tool, sign up at https://www.weatherapi.com/ and get your free API key.
Then run the app with the following command, replacing `YOUR_API_KEY` with your actual API key:

```bash
WEATHER_API_KEY=YOUR_API_KEY streamlit run src/main.py
```
