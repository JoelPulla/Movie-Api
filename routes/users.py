from fastapi import APIRouter

router = APIRouter()

@router.get('/User', tags=['User'])
def getUsers():
    return []