import boto3
import base64

def lambda_handler(event, context):
    body = event['body']
    # Entrada (json)
    nombre_bucket = body['bucket']
    dir_name = body['directory']
    filename = body['filename']
    file_content = body['file_content']

    directory = dir_name + '/' + filename
    file_content = base64.b64decode(file_content)
    
    # Proceso    
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=nombre_bucket,
        Key=directory,
        Body=file_content
    )
    
    return {
        'statusCode': 200,
        'msg': f'folder {dir_name} creado en {nombre_bucket}'
    }
