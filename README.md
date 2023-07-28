# Movie Recommender System

<!-- [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-username/your-repository) -->

## Overview

This repository contains a Movie Recommender System built using Python, Streamlit, TensorFlow, and scikit-learn. The system uses pre-trained embeddings from TensorFlow Hub to generate movie embeddings, and then implements the k-nearest neighbors algorithm to recommend similar movies based on user input.

![](https://github.com/Rishavgg/Movies-Recommendation-System/blob/main/Images/demo_GIF.gif)

## Getting Started

To run the Movie Recommender System on your local machine, follow the steps below:

1. Clone this repository to your local machine using the following command:      
git clone https://github.com/Rishavgg/Movies-Recommendation-System.git

2. Navigate to the repository directory: cd your-repository

3. Install the required dependencies by running:
pip install -r requirements.txt

4. Download the pre-trained model and embedding data:
- Model: Download the TensorFlow SavedModel format from [https://tfhub.dev/google/universal-sentence-encoder/4] and place it in the `model_savedmodel` directory.


## Running the App

To launch the Movie Recommender System app, run the following command in the terminal:
streamlit run app.py

The app will open in your default web browser, and you can start using it to get movie recommendations based on your input.

## Screenshots/GIFs

![Movie Recommender System Home Page](https://github.com/Rishavgg/Movies-Recommendation-System/blob/main/Images/home.png)

![Movie Recommendations](https://github.com/Rishavgg/Movies-Recommendation-System/blob/main/Images/recommendations.png)

## Overview what we have done
1. We start by importing the required libraries, including pandas, numpy, tensorflow, tensorflow_hub, and sklearn.
2. We define functions to load the pre-trained model, generate embeddings for texts, recommend movies based on the input text, and load movie data from a CSV file.
3. In the main() function, we load the movie data, select relevant columns, load the pre-trained model, and generate embeddings for movie overviews using the model.
4. We initialize the NearestNeighbors model, fit it with the embeddings, and get user input for movie recommendation.
5. The recommend_movies function then recommends movies based on the user input using the NearestNeighbors model.
6. The program is executed by calling the main() function.
## Deployment

The Movie Recommender System is currently only available on your local machine. To deploy it online, you can explore platforms like Streamlit Sharing, Heroku, or PythonAnywhere.

## Contributing

We welcome contributions from the community. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
