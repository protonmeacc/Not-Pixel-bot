from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [3200, 3600]
    START_DELAY: list[int] = [5, 20]
    AUTO_PAINT: bool = True
    AUTO_MINING: bool = True
    AUTO_TASK: bool = True
    AUTO_UPGRADE: bool = True
    AUTO_UPGRADE_PAINT: bool = True
    MAX_PAINT_LEVEL: int = 5
    AUTO_UPGRADE_CHARGE: bool = True
    MAX_CHARGE_LEVEL: int = 5
    AUTO_UPGRADE_ENERGY: bool = True
    MAX_ENERGY_LEVEL: int = 2
    TASKS: list[str] = ["paint20pixels", "leagueBonusSilver", "x:notcoin", "x:notpixel"]
    COLORS: list[str] = ["#6A5CFF", "#e46e6e", "#FFD635", "#7EED56", "#00CCC0", "#51E9F4", "#94B3FF",
                         "#9C6926", "#6D001A", "#bf4300", "#000000", "#FFFFFF"]
    REF_ID: str = 'f7415971728'


settings = Settings()
