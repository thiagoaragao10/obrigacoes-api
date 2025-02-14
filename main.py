from fastapi import FastAPI
from models import Base, Empresa, ObrigacaoAcessoria
from database import engine
from sqlalchemy.orm import Session
from fastapi import Depends

app = FastAPI()

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

# Função para acessar o banco
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Estágio!"}

@app.get("/empresas")
def get_empresas(db: Session = Depends(get_db)):
    empresas = db.query(Empresa).all()
    return empresas

@app.get("/obrigacoes")
def get_obrigacoes(db: Session = Depends(get_db)):
    obrigacoes = db.query(ObrigacaoAcessoria).all()
    return obrigacoes

