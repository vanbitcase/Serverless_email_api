# Serverless_email_api
This is an Restapi where the user  would able to send the email , I have used serverless service to host it. 

# Step 1 
Install all the requirements 

```Bash
npm install -g serverless

serverless create --template aws-python --path my-service
cd my-service

npm install serverless-offline --save-dev
```
# Step 2 
Now , take the cmd to project directory.Enter the following commands

```
serverless

```
then,

```
serverless offline start
```

# Step 3
After the proper running of the server less you get these url:

```
  ANY | http://0.0.0.0:3000/dev/apidata                             │   
   │   POST | http://0.0.0.0:3000/2015-03-31/functions/app/invocations
```

# Step 4 
Now use this Url  with request library and replace your URL in this code:

```
import requests

url = "http://localhost:3000/dev/apidata"
data = {
    "receiver_email": "vanshrastogi212@gmail.com",
    "subject": "Test Email",
    "body_text": "This is the body , assignment for internship."
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
```

IF all work perfectly you will get this response:

```
200
{'receiver_email': 'vanshrastogi212@gmail.com', 'status': 'Email sent successfully'}
```
