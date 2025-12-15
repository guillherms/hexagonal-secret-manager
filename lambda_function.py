from infra.container_infra.container import LambdaContainer

_container = LambdaContainer()

def lambda_handler(event, context):
    uc = _container.build_usecase()
    pessoa = uc.execute(event["id_pessoa"])
    return {"statusCode": 200, "body": pessoa}