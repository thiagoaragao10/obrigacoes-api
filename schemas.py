from pydantic import BaseModel
from typing import List, Optional

# Esquema para criar uma empresa
class EmpresaCreate(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

    class Config:
        orm_mode = True

# Esquema para a resposta de uma empresa
class EmpresaResponse(BaseModel):
    id: int
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

    class Config:
        orm_mode = True

# Esquema para criar uma obrigação acessória
class ObrigacaoAcessoriaCreate(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

    class Config:
        orm_mode = True

# Esquema para a resposta de uma obrigação acessória
class ObrigacaoAcessoriaResponse(BaseModel):
    id: int
    nome: str
    periodicidade: str
    empresa_id: int

    class Config:
        orm_mode = True

