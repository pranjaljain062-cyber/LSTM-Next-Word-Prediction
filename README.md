# Next Word Prediction using LSTM

## Overview
This project is an experiment with Long Short-Term Memory (LSTM) networks for next-word prediction.

The goal was to train a deep learning model that takes a sentence as input and predicts the next possible word.

I built this project to understand how LSTM works with text data, sequential learning, and natural language processing.

## Dataset
- **Dataset:** High Quality English Sentences
- **Source:** [Hugging Face Dataset](https://huggingface.co/datasets/agentlans/high-quality-english-sentences)
- Used 40,000 sentences for this experiment.
- Text data was cleaned and preprocessed before training.

## Technologies Used
- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Streamlit

## Project Workflow
1. Load and explore the text dataset.
2. Clean and preprocess sentences.
3. Convert text into numerical sequences using Tokenization.
4. Create input sequences and target words.
5. Apply padding to make sequences uniform.
6. Create word embeddings using an Embedding layer.
7. Build and train an LSTM model.
8. Evaluate predictions.
9. Build a simple web interface using Streamlit.

## Model Architecture
The model uses:
- **Embedding Layer:** Converts word indices into dense vectors.
- **LSTM Layer:** Learns patterns and relationships in word sequences.
- **Dropout:** Helps reduce overfitting.
- **Dense Layer:** Predicts the next word from the vocabulary.

## Results and Limitations
The model was able to generate next-word predictions, but the prediction quality was low.

Some predictions were repetitive or lacked proper context. This experiment showed that training a useful language prediction model requires better contextual learning and more effective model architecture.

## What I Learned
- Text preprocessing and tokenization
- Creating input sequences and target words
- Word embeddings
- LSTM architecture
- Sequence prediction
- Overfitting and model evaluation
- Building a Streamlit application

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Future Improvements
- Experiment with larger and more diverse datasets.
- Improve prediction quality.
- Explore Attention Mechanisms.
- Learn and experiment with Transformer models.

## Conclusion
This project helped me understand how LSTM networks process sequential text data and perform next-word prediction. Although the model had limitations, it was a valuable hands-on learning experience in Deep Learning and NLP.