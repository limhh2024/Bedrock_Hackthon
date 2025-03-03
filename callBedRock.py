import boto3
import json
import os
from dotenv import load_dotenv

#Load env
if load_dotenv('.env'):
    ACCESS_KEY = os.getenv('ACCESS_KEY') 
    SECRET_KEY = os.getenv('SECRET_KEY')

#session = boto3.Session(profile_name="default", region_name="us-west-2")
#bedrock_agent_runtime = session.client(service_name='bedrock-agent-runtime', region_name='us-west-2')
#Get the AWS 
session = boto3.Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY, region_name="ap-southeast-1")
bedrock_agent_runtime = session.client(service_name='bedrock-agent-runtime', region_name='ap-southeast-1')

def call_bedrock_service(question):

    user_question = question

    knowledge_base_id = 'VTGYGMWVVQ'
    model_arn = 'arn:aws:bedrock:ap-southeast-1::foundation-model/anthropic.claude-3-haiku-20240307-v1:0'
    #model_arn = 'arn:aws:bedrock:ap-southeast-1::foundation-model/anthropic.claude-3-5-sonnet-20240620-v1:0'


    try:

        response = bedrock_agent_runtime.retrieve_and_generate(
            input={
                'text': user_question
            },

            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': knowledge_base_id,
                    'modelArn': model_arn
                }
            }

        )

        generated_text = response['output']['text']

        return generated_text

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

 

def main():
    while True:
        # get question from the user
        q = input("input your questions: ")
        resp = call_bedrock_service(q)
        print(resp)
        print()

if __name__ == '__main__':
    main()