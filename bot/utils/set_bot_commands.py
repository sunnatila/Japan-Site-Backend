from aiogram import types



async def set_default_commands():
    from bot.loader import bot
    commands = [
            types.BotCommand(command="start", description="Botni ishga tushurish"),
            types.BotCommand(command="help", description="Yordam"),
        ]
    await bot.set_my_commands(
        commands, types.BotCommandScopeDefault()
    )
