from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import engine, get_session
from models import Cliente, Factura
from sqlmodel import SQLModel

app = FastAPI(title="API de Clientes y Facturas", version="1.0")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# --- CRUD CLIENTES ---
@app.post("/clientes/", response_model=Cliente)
def crear_cliente(cliente: Cliente, session: Session = Depends(get_session)):
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente

@app.get("/clientes/", response_model=list[Cliente])
def listar_clientes(session: Session = Depends(get_session)):
    clientes = session.exec(select(Cliente)).all()
    return clientes

# --- CRUD FACTURAS ---
@app.post("/facturas/", response_model=Factura)
def crear_factura(factura: Factura, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, factura.cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    session.add(factura)
    session.commit()
    session.refresh(factura)
    return factura

@app.get("/facturas/", response_model=list[Factura])
def listar_facturas(session: Session = Depends(get_session)):
    facturas = session.exec(select(Factura)).all()
    return facturas