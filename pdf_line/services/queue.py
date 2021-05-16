import boto3


def get_queue(queue_name: str):

    if queue_name is None:
        raise TypeError

    sqs = boto3.resource("sqs")
    return sqs.get_queue_by_name(QueueName=queue_name)


def get(queue_name, message_type):
    pass
