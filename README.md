# Unveil the Secrets of Iris Flowers with ML and Streamlit

## Explore the World of Flower Prediction

The goal of this project is not only to build a machine learning model that predicts Iris flower species, but also to deploy it on an AWS EC2 server. By doing so, the model can be accessed and used in real-world scenarios, with the ability to scale as needed for a growing number of users.

By leveraging cloud computing, I aim to make this prediction model more accessible, secure, and reliable. This will also open up new possibilities for data-driven decision-making by integrating the model with other systems.

## Set Up Your Iris Flower Prediction App on AWS

Ready to deploy your Iris flower prediction app on AWS? Follow these steps:

1. **Login to the AWS Console**  
   Access your AWS account and go to the EC2 dashboard.

2. **Launch an EC2 Instance**  
   Create a new EC2 instance with the necessary specifications for your app.

3. **Secure Your Instance**  
   Update the inbound rules for the security group linked to your EC2 instance to allow traffic on port 8501. This will make your Streamlit app accessible over the internet.

   ![image](https://github.com/user-attachments/assets/e65d5fc7-6930-4333-b21d-d2edd954264c)

4. **Set Up the EC2 Instance**  
   Run the following commands to prepare your EC2 instance for deployment:
```bash
sudo apt update
```

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```


```bash
git clone "Your-repository"
```

```bash
sudo apt install python3-pip
```

> Inside the ls "repository" 

```bash
pip3 install -r requirements.txt
```


6. Run Your Streamlit App: Once the setup is complete, navigate to your project directory and launch your Streamlit app using the following command:
```bash
python3 -m streamlit run test.py
```
