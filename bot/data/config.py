from environs import Env
import os

env = Env()
env.read_env(path=os.path.join('envs', '.env'))


BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
CHANNELS = env.list("CHANNELS")
