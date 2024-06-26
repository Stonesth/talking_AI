# Talking AI

To run texte_to_speech.py you need to have
Anything LLM
LM Studio

Build Your Own Talking 'Bad Girlfriend' AI - 100% Local, Free & Uncensored
https://www.youtube.com/watch?v=XxcuG8Yljwc&t=154s

python -m venv venv
source venv/bin/activate

pip install pygame
pip install torch
pip install openai
pip install --upgrade pip setuptools wheel
pip install numpy
python -c "import numpy; print(numpy.get_include())"
export CFLAGS="-I/Users/thononpierre/Documents/Projet/Python/Project/AI_projects/talking_AI/venv/lib/python3.9/site-packages/numpy/core/include ${CFLAGS}"

git clone https://github.com/coqui-ai/TTS.git
cd TTS
pip install poetry
poetry install (Not succeed)
pip install -r requirements.txt
pip install .
cd ..

python texte_to_speech.py
