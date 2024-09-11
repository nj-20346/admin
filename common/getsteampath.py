import winreg
import os
from .log import log
from .config import config
from .stack_error import stack_error
from pathlib import Path

# 通过注册表获取Steam安装路径
def get_steam_path():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Valve\Steam')
        steam_path = Path(winreg.QueryValueEx(key, 'SteamPath')[0])
        custom_steam_path = config["Custom_Steam_Path"]
        if not custom_steam_path == '':
            return Path(custom_steam_path)
        else:
            return steam_path
    except Exception as e:
        log.error(f'Steam路径获取失败, {stack_error(e)}')
        os.system('pause')
    
steam_path = get_steam_path()