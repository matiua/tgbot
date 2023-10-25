from tgbot.utils.utils_functions import ots

##################################                #####################################
##################################     /start     #####################################
##################################                #####################################

# Стартовое фото, оставьте пустым если хотите убрать
start_photo = "https://cdn.discordapp.com/attachments/1044002825555939429/1095626850761453698/sakoshop.png"

# Стартовый текст
start_text = """
Головне меню
"""

no_sub = "<b>❗ Ошибка!\nВы не подписались на канал.</b>"

is_buy_text = "❌ Покупки тимчасово відключено!"
is_ban_text = f"<b>❌ Ви були заблоковані в роботі!</b>"
is_work_text = f"<b>❌ Робот знаходиться на тих. роботах!</b>"
is_refill_text = f"❌ Поповнення тимчасово відключено!"
is_ref_text = f"❗ Реферальна система вимкнена!"

yes_reffer = f"<b>❗ У вас є рефер!</b>"
invite_yourself = "<b>❗ Ви не можете запросити себе</b>"
new_refferal = "<b>💎 У вас новий реферал! @{user_name} \n" \
                "⚙️ Тепер у вас <code>{user_ref_count}</code> {convert_ref}!</b>"

##################################               #####################################
################################## Inline-Кнопки #####################################
##################################               #####################################


# Меню пользователя
products = "Магазин🛒"
refill = "Поповнити баланс 💰"
profile = "Профіль👤"
faq = "FAQ ❓"
support = "Допомога🙋‍♂️"
back = "⬅ Повернутись"
close_text = "Приховати ❌"

qiwi_text = "Fondy 🇺🇦"
yoomoney_text = "📌 ЮMoney"
liqpay_text = "Liqpay 🇺🇦"
lava_text = "Lava"
lzt_text = "💚 Lolz"
crystalPay_text = " CrystalPay 💵"


support_inl = "⚙️ Тех. Підтримка"


#####################################         #####################################
##################################### Профиль #####################################
#####################################         #####################################
profile_photo = "https://media.discordapp.net/attachments/1044002825555939429/1095644923572785234/profile.png?width=803&height=278"
# Кнопки Профиля
ref_system = "💎 Реферальна система"
promocode = "💰 Активувати промокод"
last_purchases_text = "⭐ Останні покупки"





def open_profile_text(user_id, user_name, balance, total_refill, reg_date, ref_count):
    msg = f"""<b><a href="{profile_photo}"> </a>
    👤 Ваш профіль:
    🆔 ID: <code>{user_id}</code>
    💰 Баланс: <code>{balance} UAH</code>
    💵 Усього поповнено: <code>{total_refill} UAH</code>
    👥 Рефералів: <code>{ref_count} людей</code></b>"""
    return (msg)


last_10_purc = "⚙️ Останні 10 покупок"
no_purcs = "❗ У вас відсутні покупки"
last_purc_text = "<b>🧾 Чек: <code>{receipt}</code> \n" \
                "💎 Товар: <code>{name} | {count}шт | {price} RUB</code> \n" \
                "🕰 Дата купівлі: <code>{date}</code> \n" \
                "💚 Товари: \n{link_items}</b>\n"

promo_act = "<b>📩 Для активації промокоду напишіть його назву</b>\n" \
            "<b>⚙️ Приклад: promo2023</b>"
no_uses_coupon = "<b>❌ Ви не встигли активувати промокод!</b>"
no_coupon = "<b>❌ Промокоду <code>{coupon}</code> не існує!</b>"
yes_coupon = "<b>✅ Ви успішно активували промокод та отримали <code>{discount} UAH</code>!</b>"
yes_uses_coupon = "<b>❌ Ви вже активували цей промокод!</b>"

new_ref_lvl = "<b>💚 У вас є новий реферальний рівень, {new_lvl}! До {next_lvl} рівня залишилося {remain_refs} {convert_ref}</b>"
max_ref_lvl = f"<b>💚 У вас є новий реферальний рівень, 3! Максимальний рівень!</b>"
cur_max_lvl = f"💚 У вас максимальний рівень!</b>"
next_lvl_remain = "💚 До наступного рівня залишилося запросити <code>{remain_refs} чел</code></b>"
ref_text = "<b>💎 Реферальна система \n\n" \
            "🔗 Посилання: \n" \
            "{ref_link} \n\n" \
            "📔 Наша реферальна система дозволить заробити велику суму без вкладень. Вам необхідно лише давати своє посилання друзям і ви отримуватимете довічно <code>{ref_percent}%</code> з їх поповнення в боті. \n\n" \
            "⚙️ Вас запросив: {reffer} \n" \
            "💵 Усього зароблено <code>{ref_earn} UAH</code> с {convert_ref} \n" \
            "📌 Усього у вас <code>{ref_count}</code> {convert_ref} \n" \
            "🎲 Реферальний рівень: <code>{ref_lvl}</code> \n" \
            "{mss}"
yes_refill_ref = "<b>💎 Ваш реферал {name} поповнив баланс на <code>{amount}₴</code> і з цього вам зараховано <code>{ref_amount}₴</code></b>"

#####################################         #####################################
#####################################   FAQ   #####################################
#####################################         #####################################

no_faq_text = "<b>⚙️ FAQ Не було налаштовано, зверніться до підтримки!</b>"
faq_chat_inl = "💎 Чат"
faq_news_inl = "Відгуки🎈"


################################                    ################################
################################   Тех. Поддержка   ################################
################################                    ################################

no_support = '<b>Ти можеш поставити своє запитання на <a href="https://t.me/sakomanager">підтримку</a>, але перед цим рекомендуємо ознайомитися з нашим <a href="https://telegra.ph/Otvety-na-voprosy-11-26-2">FAQ</a></b>'
yes_support = "<b>📩 Щоб звернутися до Тех. Підтримку натисніть кнопку знизу:</b>"

#######################################
#     Мин./Макс. Сумма пополнения     #        
#                                     #
min_amount = 50                        #
max_amount = 10000                   #
#                                     #
#                                     #
#######################################


################################                  ################################
################################    Пополнения    ################################
################################                  ################################


buy_photo = "https://media.discordapp.net/attachments/1044002825555939429/1095677390979616870/popovnia.png?width=803&height=278"

refill_text = f"<b><a href='{buy_photo}'>💰 Вибери спосіб поповнення:</a></b>"
refill_amount_text = f"<b>💰 Введіть суму поповнення (От {min_amount} до {max_amount})</b>"
refill_link_inl = "💵 Перейти до оплати"
refill_check_inl = "💎Перевірити оплату"
refill_check_no = "❌ Оплати не знайдено"
no_int_amount = "<b>❗ Сума поповнення має бути числом!</b>"
min_max_amount = f"<b>❗ Сума поповнення має бути більшою або дорівнює <code>{min_amount} UAH</code> але менше або дорівнює <code>{max_amount} UAH</code></b>"

def refill_gen_text(way, amount, id):
    msg = f"""
    <b>⭐ Поповнення через: <code>{way}</code>
    💰 Сума: <code>{amount} UAH</code>
    🆔 ID платежа: <code>{id}</code>
    💎 Щоб сплатити, натисніть кнопку внизу:</b>
    """

    return ots(msg)


def refill_success_text(way, amount, receipt):
    msg = f"""
<b>⭐ Ви успішно поповнили баланс на суму <code>{amount} UAH</code>
💎 Спосіб: <code>{way}</code>
🧾 Чек: <code>{receipt}</code></b>
    """

    return ots(msg)

##########################                                 ############################
##########################    Открытие категорий/Товары    ############################
##########################                                 ############################

open_pos_text = """
<b>💎 Категорія: <code>{cat_name}</code>

🛍️ Товар: <code>{pos_name}</code>
💰 Вартість: <code>{price} UAH</code>
🎲 Опис: </b>\n{desc}
"""

no_cats = f"<b>На жаль, на даний момент немає категорій. :(</b>"
available_cats = f"<b>Доступні на даний момент категорії:</b>"
current_cat = "<b>Поточна категорія: <code>{name}</code>:</b>"

no_products = f"<b>На жаль, на даний момент немає товарів :(</b>"
no_product = f"На жаль, зараз немає даного товару :("
gen_products = "Підготовка товарів..."

current_pod_cat = "<b>Поточна підкатегорія: <code>{name}</code></b>"

here_count_products = f"<b>❗ Введіть кількість товарів, які хочете купити:</b>"

choose_buy_product = "<b>❓ Ви впевнені, що хочете купити <code>{name}</code> у к-ві <code>1шт.</code>?</b>"
choose_buy_products = "<b>❓ Ви впевнені, що хочете купити <code>{name}</code> у к-ві <code>{amount}шт.</code>?</b>"

no_num_count = "<b>❗ Кількість має бути числом!</b>"

yes_buy_items = """
<b>✅ Ви успішно купили товар(и)</b>

🧾 Чек: <code>{receipt}</code>
️💎 Товар: <code>{name} | {amount}шт | {amount_pay}₴</code>
🎲 Дата: <code>{buy_time}</code>
"""

no_balance = "❗ У вас недостатньо коштів. Поповніть баланс!"
edit_prod = "<b>❗️ Товар, який ви хотіли купити, закінчився або змінився.</b>"
otmena_buy = "<b>❗ Ви скасували покупку товарів.</b>"
