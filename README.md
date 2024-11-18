# Iris-Flower-Prediction-App-with-Streamlit
My primary aim is not solely to develop a prediction model, but to take it a step further by deploying it on an AWS EC2 server. I want to ensure that the model can be accessed and used in real-world scenarios, with the ability to scale as needed. This deployment will allow me to leverage the power of cloud computing for efficient performance, security, and reliability, making the model accessible to a wider audience and facilitating seamless integration with other systems

# Sreps in AWS:
1. Login with your AWS console and launch an EC2 instance.

2. Edit the inbound rule for the security group associated with your EC2 instance to allow traffic on port 8501:
Navigate to EC2 Dashboard → Security Groups.
Select the security group attached to your EC2 instance.
Click on Inbound rules → Edit inbound rules.
Add a new rule with the following settings:
Type: Custom TCP Rule
Port Range: 8501
Source: Anywhere (or specify your desired source IP range)
Save the rule.

3. Run the following commands:
sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install git curl unzip tar make sudo vim wget -y
sudo apt install git curl unzip tar make sudo vim wget -y
git clone "Your-repository"
sudo apt install python3-pip
pip3 install -r requirements.txt

