from fastapi import APIRouter


router = APIRouter()

@router.get('tv', tags=['tv'])
def getAllTv():
    return []