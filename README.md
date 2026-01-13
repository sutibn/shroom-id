<h1 align="center">shroomID</h1>

<p align="center">
    <img src='./img/preview.png?'>
    <img src='./img/mockup.png?'>
</p>

## Challenge
Foraging for wild mushrooms is a high-stakes task where the line between a safe find and a toxic one is often razor-thin. Even for experienced foragers, identifying species accurately is difficult. To help mitigate this risk, we’ve developed a machine learning classifier designed to automatically distinguish between edible and poisonous mushrooms with high precision.

## Approach
The goal is to provide a reliable safety layer through automation, reducing the chances of a dangerous misidentification. We utilized the UCI "[Mushroom](https://archive.ics.uci.edu/dataset/73/mushroom)" dataset, which provides a rich collection of physical traits—such as cap shape, gill size, and odor—across thousands of samples. By analyzing these fruiting body characteristics, our model learns to identify the subtle patterns that correlate with toxicity, turning raw physical data into a dependable classification tool.

## Usage
```
pip install streamlit
streamlit run app.py
```
