from dagster import EnvVar, asset, define_asset_job
from dagster._core.definitions.definitions_class import Definitions
from dagster._utils.env import environ
from dagster_sigma import SigmaBaseUrl, SigmaOrganization

fake_client_id = "fake_client_id"
fake_client_secret = "fake_client_secret"

with environ({"SIGMA_CLIENT_ID": fake_client_id, "SIGMA_CLIENT_SECRET": fake_client_secret}):
    fake_token = "fake_token"
    resource = SigmaOrganization(
        base_url=SigmaBaseUrl.AWS_US,
        client_id=EnvVar("SIGMA_CLIENT_ID"),
        client_secret=EnvVar("SIGMA_CLIENT_SECRET"),
    )

    @asset
    def my_materializable_asset():
        pass

    sigma_defs = resource.build_defs()
    defs = Definitions.merge(
        Definitions(assets=[my_materializable_asset], jobs=[define_asset_job("all_asset_job")]),
        sigma_defs,
    )
