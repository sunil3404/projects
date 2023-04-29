from fastapi import FastAPI
from fastapi import APIRouter
from routers import stud, dept, staff, user, post
from database import engine
import models, schemas
import uvicorn



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency


app.include_router(stud.router,
    prefix="/student",
    tags=["Students"],
    )
app.include_router(dept.router,
    prefix = '/department',
    tags = ['Department']               
    )
app.include_router(staff.router,
    prefix = '/staff',
    tags = ['Staff']               
    )
app.include_router(user.router,
    prefix = '/user',
    tags = ['User']               
    )
app.include_router(post.router,
    prefix = '/post',
    tags = ['Posts']               
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
