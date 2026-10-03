from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8626540833:AAELwq4FFJ6Rj9Z_f45JjZyCNhsjfNoyZbY"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🖨️ Tajaajila Maxxansaa", callback_data="services")],
        [InlineKeyboardButton("📦 Order Godhuu", callback_data="order")],
        [InlineKeyboardButton("💳 Kaffaltii", callback_data="payment")],
        [InlineKeyboardButton("📞 Nu Qunnamaa", callback_data="contact")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Akkam! 👋\n\n"
        "Baga nagaan dhuftan gara "
        "Mana Maxxansaa Gadaa Carcar 🖨️\n\n"
        "Maal gochuu barbaadda?",
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "services":
        text = (
            "🖨️ TAAJILAWWAN KEENYA\n\n"
            "• Kaardii eenyummaa fi hojii\n"
            "• Logo fi dizaayinii\n"
            "• T-Shirt, Vestii fi Cap\n"
            "• Stamp / Chappaa\n"
            "• Banner, Poster fi Flyer\n"
            "• Waraqaa waajjiraa fi ragaa\n"
            "• Invitation\n"
            "• Hojiiwwan maxxansaa adda addaa\n\n"
            "Qulqullinaan fi saffisaan ni hojjenna. ✅"
        )

    elif query.data == "order":
        text = (
            "📦 ORDER GODHUUF\n\n"
            "Suuraa ykn PDF hojii kee asitti ergi. 📄📷\n\n"
            "Ergasii maqaa kee fi hojii barbaaddu nuuf ibsi."
        )

    elif query.data == "payment":
        text = (
            "💳 ODEEFFANNOO KAFFALTII\n\n"
            "CBE: Amiin Abdulahab\n"
            "Telebirr: 0915527300\n\n"
            "Erga kaffaltii raawwatte booda ragaa kaffaltii nuuf ergi. ✅"
        )

    elif query.data == "contact":
        text = (
            "📞 NU QUNNAMAA\n\n"
            "Mana Maxxansaa Gadaa Carcar\n"
            "📱 091 552 7300\n"
            "📱 0715495273\n\n"
            "Galatoomaa! 🙏"
        )

    else:
        text = "Filannoo hin beekamne."

    await query.edit_message_text(text=text)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("🤖 Bot hojjachaa jira...")
    app.run_polling()


if __name__ == "__main__":
    main()