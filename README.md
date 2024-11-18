# Unveil the Secrets of the Iris Flowers with ML and Streamlit
# Embark on a Captivating Journey of Flower Prediction
As a seasoned data enthusiast, my primary goal is not just to develop a robust prediction model, but to take it a step further by deploying it on an AWS EC2 server. I'm driven by a desire to ensure that this model can be accessed and utilized in real-world scenarios, with the ability to scale as needed to meet the demands of a growing user base.

By leveraging the power of cloud computing, I aim to create an efficient, secure, and reliable platform that will make this Iris flower prediction model accessible to a wider audience. This deployment will not only showcase the model's capabilities but also facilitate seamless integration with other systems, opening up a world of possibilities for data-driven decision-making.

# Conquer the Cloud: Setting Up Your Iris Flower Prediction App on AWS
Ready to take your Iris flower prediction model to new heights? Follow these steps to deploy your app on an AWS EC2 instance:

1. Login to the AWS Console: Access your AWS account and navigate to the EC2 dashboard.
2. Launch an EC2 Instance: Create a new EC2 instance with the desired specifications to accommodate your application.
3. Secure Your Instance: Edit the inbound rules for the security group associated with your EC2 instance to allow traffic on port 8501. This will ensure that your Streamlit app can be accessed from the internet.
4. Set the Stage for Your App: Run the following set of commands to prepare your EC2 instance for the deployment:
```sudo apt update```
`sudo apt-get update`
`sudo apt upgrade -y`
`sudo apt install git curl unzip tar make sudo vim wget -y`
`sudo apt install git curl unzip tar make sudo vim wget -y`
`git clone "Your-repository"`
`sudo apt install python3-pip`
`pip3 install -r requirements.txt`
9. Run Your Streamlit App: Once the setup is complete, navigate to your project directory and launch your Streamlit app using the following command:
streamlit run app.py
Your app will now be accessible from the public IP address of your EC2 instance on port 8501.
