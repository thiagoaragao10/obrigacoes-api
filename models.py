from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = 'empresas'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    endereco = Column(String)
    email = Column(String)
    telefone = Column(String)

    obrigações_acessoria = relationship("ObrigacaoAcessoria", back_populates="empresa")


class ObrigacaoAcessoria(Base):
    __tablename__ = 'obrigacoes_acessoria'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    periodicidade = Column(String)
    empresa_id = Column(Integer, ForeignKey('empresas.id'))

    empresa = relationship("Empresa", back_populates="obrigações_acessoria")

