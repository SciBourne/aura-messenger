from fastapi import FastAPI
from versioned_fastapi import FastApiVersioner

from routes import router


app = FastAPI(
    title="Aura messenger",
    summary="REST API documentation",
)

app.include_router(router)


versions = FastApiVersioner(app)

versions.prefix_format = "/api/v{version}"
versions.default_version = 1
versions.version_fastapi()
