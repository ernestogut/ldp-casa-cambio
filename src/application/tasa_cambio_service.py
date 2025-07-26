from src.domain.ports.tasa_cambio_repository import TasaCambioRepository
from src.domain.models.tasa_cambio import TasaCambio
from typing import Optional, List


from src.domain.models.moneda import Moneda


class TasaCambioService:
    def __init__(self, tasa_repo: TasaCambioRepository):
        self.tasa_repo = tasa_repo

    def agregar_tasa(
        self,
        cod_origen: str,
        nom_origen: str,
        sim_origen: str,
        cod_destino: str,
        nom_destino: str,
        sim_destino: str,
        tasa: float,
    ) -> None:
        moneda_origen = Moneda(cod_origen, sim_origen, nom_origen)
        moneda_destino = Moneda(cod_destino, sim_destino, nom_destino)
        nueva_tasa = TasaCambio(moneda_origen, moneda_destino, tasa)
        self.tasa_repo.agregar_tasa(nueva_tasa)

    def actualizar_tasa(self, key: str, nueva_tasa: float) -> None:
        self.tasa_repo.actualizar_tasa(key, nueva_tasa)

    def eliminar_tasa(self, key: str) -> None:
        self.tasa_repo.eliminar_tasa(key)

    def obtener_tasa(self, key: str) -> Optional[TasaCambio]:
        return self.tasa_repo.obtener_tasa(key)

    def listar_tasas(self) -> List[TasaCambio]:
        return self.tasa_repo.listar_tasas()
