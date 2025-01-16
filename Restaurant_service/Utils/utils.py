from Schemas import schemas


def create_payload_obj(id : int, role_type : str):

    payload=schemas.payload(id=id,role=role_type)

    return  payload