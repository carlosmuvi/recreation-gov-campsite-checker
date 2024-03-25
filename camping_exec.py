import datetime
import subprocess
import telegram
import asyncio

bot = telegram.Bot("6013591773:AAGQoZ_729cnSwfADgARDH87ZHNLy7V684U")
telegram_chat_id = 5589934690

# Function to generate a list of weekends (Saturdays) between two dates
def generate_weekends(start_date, end_date):
    current_date = start_date
    weekends = []

    while current_date <= end_date:
        if current_date.weekday() == 5:  # 5 represents Saturday
            weekends.append(current_date)
        current_date += datetime.timedelta(days=1)

    return weekends


async def send_telegram_message(all_outputs):
    async with bot:
        await bot.send_message(text=all_outputs, chat_id=telegram_chat_id)

start_date = datetime.date(2024, 5, 7)
end_date = datetime.date(2023, 5, 9)

# Park IDs
# upper pines 232447
# lower pines 232450
# north pines 232449
# tahoe fallen leaf 232449
parks = "232769"

# Loop through the weekends and run the camping.py script
command = f"python3 camping.py --start-date {start_date} --end-date {end_date} --parks {parks}"
print(f"Running: {command}")

# Capture the output from the subprocess
result = subprocess.run(command, shell=True, capture_output=True, text=True)

print(result.stdout)
output = result.stdout

if ("0 site(s) available" not in output):
    # Run the async function to send the Telegram message
    asyncio.run(send_telegram_message(output))



