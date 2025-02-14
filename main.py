from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from schemas import EmpresaCreate, ObrigacaoAcessoriaCreate, EmpresaResponse, ObrigacaoAcessoriaResponse
from fastapi.middleware.cors import CORSMiddleware

# Configurações de banco de dados
DATABASE_URL = "postgresql://postgres:thiago123@localhost:5432/obrigacoes_api"

# Criação da engine e sessão
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Aplicação FastAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos
class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    endereco = Column(String)
    email = Column(String)
    telefone = Column(String)

    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")


class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    periodicidade = Column(String)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))

    empresa = relationship("Empresa", back_populates="obrigacoes")


# Criar todas as tabelas no banco
Base.metadata.create_all(bind=engine)

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas da API

@app.post("/empresas/", response_model=EmpresaResponse)
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = Empresa(
        nome=empresa.nome,
        cnpj=empresa.cnpj,
        endereco=empresa.endereco,
        email=empresa.email,
        telefone=empresa.telefone
    )
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresas/", response_model=List[EmpresaResponse])
def get_empresas(db: Session = Depends(get_db)):
    return db.query(Empresa).all()

@app.get("/empresas/{empresa_id}", response_model=EmpresaResponse)
def get_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@app.post("/obrigacoes/", response_model=ObrigacaoAcessoriaResponse)
def create_obrigacao(obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = ObrigacaoAcessoria(
        nome=obrigacao.nome,
        periodicidade=obrigacao.periodicidade,
        empresa_id=obrigacao.empresa_id
    )
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.get("/obrigacoes/", response_model=List[ObrigacaoAcessoriaResponse])
def get_obrigacoes(db: Session = Depends(get_db)):
    return db.query(ObrigacaoAcessoria).all()

@app.get("/obrigacoes/{obrigacao_id}", response_model=ObrigacaoAcessoriaResponse)
def get_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return db_obrigacao


