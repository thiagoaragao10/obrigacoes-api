from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

DATABASE_URL = os.getenv("DATABASE_URL")  # Vai ser configurado no arquivo .env

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Obter a URL do banco de dados do .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Criar o engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Criar a classe base para os modelos
Base = declarative_base()

# Criar uma sessão para comunicação com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

