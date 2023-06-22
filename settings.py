from environs import Env
from dataclasses import dataclass

@dataclass
class Settings:
    bot_token: str
    admin_ids: list
    schedule_folser_url: str

def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bot_token=env.str('TOKEN'),
        admin_ids=env.list('ADMIN_IDS'),
        schedule_folser_url=env.str('SCHEDULE_FOLDER_LINK')
    )


GROUPS = [
        '1-1 А9', '2-1 А9', '3-1 А9', '4-1 А9',
        '1-1 Г9', '2-1 Г9', '3-1 Г9', '4-1 Г9',
        '1-1 Т9', '2-1 Т9', '3-1 Э9', '4-1 Э9',
        '1-1 С9', '2-1 С9', '3-1 С9', '4-1 С9',
        '1-1 П9', '2-1 П9', '3-1 П9', '4-1 П9',
        '1-2 П9', '2-2 П9', '3-2 П9', '4-2 П9',
        '1-1С11', '2-1С11', '3-1С11', '1-1П11',
        '1-1 Б9', '2-1 Б9', '3-1 Б9', '3-1П11',
        ]


settings = get_settings('data')