import random
import uuid
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, InlineQueryHandler, CommandHandler, ContextTypes

TOKEN = "8224666230:AAEH-vKIvdvcWOT2oBx4RR0lFkHBggu4RnI"  # your token

def generate_femboy():
    percent = random.randint(1, 100)

    extras = [
        "UwU", "OwO", ">_<", "Kawaii~", "nya~", "rawr x3",
        ":3", "hehe~", "Kyaa~", "✨", "🌸", "🎀", "💖"
    ]

    chaos = [
        "Boywife soon? 🍌💅",
        "Good Boy~ 😳",
        "Time to claim your bottom license! 🚨",
        "Your friends are OTW to Crack you 😭",
        "Open up little Omega 🤤",
        "Nyaa! What a cute catboy ✨",
        "You're Daddy's little kitten 😤",
        "Mm MPreg... 🍆😈"
    ]

    extra = random.choice(extras)
    chaos_text = random.choice(chaos)

    if percent == 100:
        return "100% Femboy! ULTIMATE KAWAII UwU 🌸✨ (FINAL FORM)"

    return f"{percent}% Femboy! {extra}\n{chaos_text}"

async def inline_femboy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query.strip()

    if query == "":
        result_text = f"You are... {generate_femboy()}"
    else:
        result_text = f"{query} is... {generate_femboy()}"

    # 🔥 REROLL BUTTON (addictive)
    keyboard = InlineKeyboardMarkup.from_button(
    InlineKeyboardButton(
        "🔁 Reroll again 😈",
        switch_inline_query=query
    )
        )

    # 👇 CLEAN + FORWARDABLE + VIRAL
    final_text = result_text + "\n\n👉 Try yours: @HowFemboyRUBot"

    results = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="Reveal your Femboy %",
            input_message_content=InputTextMessageContent(final_text),
            description="Click to reveal your fate 😏",
            reply_markup=keyboard
        )
    ]

    await update.inline_query.answer(results, cache_time=0)

# command version
async def femboy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result_text = f"{update.effective_user.first_name} is... {generate_femboy()}"
    final_text = result_text + "\n\n👉 Try yours: @HowFemboyRUBot"

    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton("🔁 Reroll again 😈", callback_data="reroll")
    )

    await update.message.reply_text(final_text, reply_markup=keyboard)

app = ApplicationBuilder().token("8224666230:AAEH-vKIvdvcWOT2oBx4RR0lFkHBggu4RnI").build()
app.add_handler(InlineQueryHandler(inline_femboy))
app.add_handler(CommandHandler("femboy", femboy))

print("🔥 Viral 67 Femboy Bot is running...")
app.run_polling()