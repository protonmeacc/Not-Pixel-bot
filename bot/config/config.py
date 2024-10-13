from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [426, 4260]
    START_DELAY: list[int] = [1, 240]
    ERROR_THRESHOLD: int = 5
    TIME_WINDOW_FOR_MAX_ERRORS: int = 240
    ERROR_THRESHOLD_SLEEP_DURATION: int = 3600
    SLEEP_AFTER_EACH_ERROR: int = 30
    AUTO_TASK: bool = False
    TASKS_TO_DO: list[str] = ["paint20pixels", "x:notpixel", "x:notcoin", "channel:notcoin", "channel:notpixel_channel"]
    AUTO_DRAW: bool = True
    JOIN_TG_CHANNELS: bool = True
    CLAIM_REWARD: bool = True
    AUTO_UPGRADE: bool = True
    REF_ID: str = 'f411905106'
    IGNORED_BOOSTS: list[str] = []
    IN_USE_SESSIONS_PATH: str = 'app_data/used_sessions.txt'
    PALETTE: list[str] = ["#e46e6e", "#FFD635", "#7EED56", "#00CCC0", "#51E9F4", "#94B3FF", "#E4ABFF",
                          "#FF99AA", "#FFB470", "#FFFFFF", "#BE0039", "#FF9600", "#00CC78", "#009EAA",
                          "#3690EA", "#6A5CFF", "#B44AC0", "#FF3881", "#9C6926", "#898D90", "#6D001A",
                          "#bf4300", "#00A368", "#00756F", "#2450A4", "#493AC1", "#811E9F", "#a00357",
                          "#6D482F", "#000000"]
    DRAW_IMAGE: bool = False
    DRAWING_START_COORDINATES: list[int] = [0, 0]
    IMAGE_PATH: str = "10x10.png"
    ENABLE_3X_REWARD: bool = True


settings = Settings()
