from .models import Nomina
from sqlalchemy.orm import Session

def guardar_nomina(db: Session, data: dict):
    nomina = Nomina(
        tipo_contrato=data["tipo_contrato"],
        salario_bruto=data["salario_bruto"],
        descuentos=data["descuentos"],
        salario_neto=data["salario_neto"],
        salud=data["detalle_descuentos"]["salud"],
        pension=data["detalle_descuentos"]["pension"],
        cesantias=data["detalle_descuentos"]["cesantias"],
    )
    db.add(nomina)
    db.commit()
    db.refresh(nomina)
    return nomina
