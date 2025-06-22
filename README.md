# Recurrent Neural Network (RNN) for Sequence Modeling  

This repository implements a **Recurrent Neural Network (RNN)** — a type of neural network architecture designed for handling **sequential data** like text, time series, and speech.  

---

## What is an RNN?

A **Recurrent Neural Network (RNN)** is a neural architecture where connections between nodes form a directed graph along a temporal sequence. This allows the model to exhibit **temporal dynamic behavior**, processing input sequences one element at a time while maintaining a hidden state that captures information about previous elements.  

---

## RNN Architecture  

An RNN processes sequences by iterating through the elements and updating its hidden state:  

\[
h_t = \sigma \left( W_h \cdot h_{t-1} + W_x \cdot x_t + b \right)
\]

\[
y_t = \phi \left( W_y \cdot h_t + c \right)
\]

Where:
- \( h_t \): Hidden state at time \( t \)  
- \( x_t \): Input at time \( t \)  
- \( y_t \): Output at time \( t \)  
- \( W_h, W_x, W_y \): Weight matrices  
- \( b, c \): Bias vectors  
- \( \sigma \): Activation function (commonly tanh or ReLU)  
- \( \phi \): Output activation (softmax for classification)

---


