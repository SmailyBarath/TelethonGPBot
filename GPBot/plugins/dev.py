import io
import sys
import traceback
from GPBot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import RPCError
from subprocess import getoutput as run

owner = 1891633746

@bot.on message(filters.user(owner) & filters.command("eval"))
async def eval(client, message):
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "<b>EVAL</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>OUTPUT</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(document=out_file,
                                           caption=cmd,
                                           disable_notification=True)
    else:
        await reply_to_.reply_text(final_output)
    await status_message.delete()


async def aexec(code, client, message):
    exec("async def __aexec(client, message): " +
         "".join(f"\n {l_}" for l_ in code.split("\n")))
    return await locals()["__aexec"](client, message)


@bot.on message(filters.command("leave") & filters.user(owner))
async def leave(client, message):
    cmd = message.text.split(maxsplit=1)[1]
    try:
        await client.leave_chat(int(cmd))
    except RPCError as e:
        print(e)


@bot.on message(filters.command("logs") & filters.user(owner))
def logs(_, m):
    run_logs = run("tail logs.txt")
    message = m.reply_text("sending logs...")
    with io.BytesIO(str.encode(run_logs)) as logs:
        logs.name = "logs.txt"
        m.reply_document(
            document=logs,
        )
    message.delete()


@bot.on message(filters.command("sh") & filters.user(owner))
def sh(_, m):
    code = m.text.replace(m.text.split(" ")[0], "")
    x = run(code)
    m.reply_text(f"**SHELL**: `{code}`\n\n**OUTPUT**:\n`{x}`")

