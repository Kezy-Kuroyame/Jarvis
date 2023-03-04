import discord
import time


async def start_record(ctx):
    ctx.voice_client.start_recording(discord.sinks.MP3Sink(), finished_callback, ctx) # Start the recording


async def finished_callback(sink, ctx):
    # Here you can access the recorded files:
    recorded_users = [
        f"<@{user_id}>"
        for user_id, audio in sink.audio_data.items()
    ]
    files = [discord.File(audio.file, f"{user_id}.{sink.encoding}") for user_id, audio in sink.audio_data.items()]
    await ctx.channel.send(f"Finished! Recorded audio for {', '.join(recorded_users)}.", files=files)


async def stop_recording(ctx):
    ctx.voice_client.stop_recording() # Stop the recording, finished_callback will shortly after be called
    await ctx.respond("Stopped!")


@bot.command(aliases=['rec'])
async def manual_record(ctx):
    await start_record(ctx)
    time.sleep(5)
    await start_record(ctx)