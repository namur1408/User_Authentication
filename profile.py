import shutil
from fastapi import APIRouter, Depends, Request, File, UploadFile
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from pathlib import Path
from models import User
from database import get_db
from auth import get_current_user
from schemas import UserSchema
from templates import templates

router = APIRouter()
AVATAR_DIR = 'stativ/avatars'

@router.get('/profile')
def profile(request: Request, user: UserSchema = Depends(get_current_user)):
    if not user:
        return RedirectResponse(url = '/login')
    return templates.TemplateResponse("profile.html", {"request": request, "user": user})

@router.post('/profile/avatar')
def upload_avatar(
    request: Request,
    user: UserSchema = Depends(get_current_user),
    db: Session = Depends(get_db),
    file: UploadFile = File(...)
):
    if not user:
        return RedirectResponse(url='/login')
    file_path = Path(AVATAR_DIR) / f'user_{user.id}.jpg'
    with file_path.open('wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    db_user = db.query(User).filter(User.id==user.id).first()
    db_user.avatar = f'{AVATAR_DIR}/user_{user.id}.jpg'
    db.commit()
    return RedirectResponse(url='/profile',status_code=303)

