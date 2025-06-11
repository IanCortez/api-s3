import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    dir_name = event['body']['directory']
    dir_name = dir_name + '/'
    
    # Proceso    
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key={dir_name})
    
    return {
        'statusCode': 200,
        'msg': f'folder {dir_name} creado en {nombre_bucket}'
    }
