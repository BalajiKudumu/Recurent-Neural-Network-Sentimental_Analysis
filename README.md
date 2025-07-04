# Recurrent Neural Network (RNN) for Sequence Modeling  

This repository implements a **Recurrent Neural Network (RNN)** — a type of neural network architecture designed for handling **sequential data** like text, time series, and speech.  

---

## What is an RNN?

A **Recurrent Neural Network (RNN)** is a neural architecture where connections between nodes form a directed graph along a temporal sequence. This allows the model to exhibit **temporal dynamic behavior**, processing input sequences one element at a time while maintaining a hidden state that captures information about previous elements.  

---
## Key Characteristics
- Sequence-aware — RNNs can model time series, text, speech, or any data where order matters.
- Shared weights — The same weights are applied at each time step, which makes the model efficient.
- Memory of past inputs — Hidden state captures prior information as the sequence is processed

---
## RNN Architecture  

An RNN processes sequences by iterating through the elements and updating its hidden state:  


![RNN Architecture](https://github.com/BalajiKudumu/Recurent-Neural-Network-Sentimental_Analysis/blob/main/RNN.png?raw=true)

Where:
- \( h_t \): Hidden state at time \( t \)  
- \( x_t \): Input at time \( t \)  
- \( y_t \): Output at time \( t \)  
- \( W_h, W_x, W_y \): Weight matrices  
- \( b, c \): Bias vectors  
- \( \sigma \): Activation function (commonly tanh or ReLU)  
- \( \phi \): Output activation (softmax for classification)

---

## Applications of RNN
- Natural Language Processing (NLP) → next word prediction, machine translation
- Time Series Forecasting → stock prices, sensor data
- Speech Recognition
- Music Generation
- Video Frame Prediction

## Limitations
- Vanishing/exploding gradient problem → hard to learn long-range dependencies
- Slow to train compared to feedforward networks

## Solution: Use advanced RNN variants like:
- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Unit)

## 📬 Contact

Maintained by **Balaji Kudumu**  
If you use this project in your research, please give appropriate credit.

---

## 📄 License

MIT License - see `LICENSE` file for details.
