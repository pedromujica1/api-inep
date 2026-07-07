from pydantic import BaseModel


class ETLRunRequest(BaseModel):
    ano: int
    origem: str | None = None
    recarregar_checkpoint: bool = False


class ETLRunResponse(BaseModel):
    ano: int
    status: str
    parquet_path: str | None = None
