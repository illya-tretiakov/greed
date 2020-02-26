# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# English translation by https://github.com/DarrenWestwood

# Currency symbol
currency_symbol = "грн"

# Positioning of the currency symbol
currency_format_string = "{value} {symbol}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} в наличии"

# Copies of a product in cart
in_cart_format_string = "{quantity} в корзине"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Заказ #{id}"

# Order info string, shown to the admins
order_format_string = "Покупатель\t{user}\n" \
                      "Дата заказа:\t{date}\n" \
                      "\n" \
                      "{items}\n" \
                      "Всего: <b>{value}</b>\n" \
                      "\n" \
                      "Примечания клиента:\n" \
                      "{notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Заказ {status_text}</b>\n" \
                           "{items}\n" \
                           "Всего: <b>{value}</b>\n" \
                           "\n" \
                           "Примечания: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Загружаются текущие транзакции...\n" \
                       "Пожалуйста, подождите пару секунд...</i>"

# Transactions page
transactions_page = "Страница <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = " 📄 .csv файл - это список всех операций, проведенных через бота.\n"

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Привет!\n" \
                           "Добро пожаловать в <b>HassanAlSabah</b> RC магазин !\n" \
                           "Сейчас находится в тестовом режиме.\n"

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "💰 У вас <b>{credit}</b> на счете.\n" \
                              "\n" \
                              "<i>Выберите нужное действие.</i>\n"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Привет, 💼 <b>админ</b>!\n" \
                               "Выберите действие.\n"

# Conversation: select a payment method
conversation_payment_method = "Как хочешь пополнить счет?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ Выберите товар для редактирования."

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ какой товар удалить?"

# Conversation: select a user to edit
conversation_admin_select_user = "Выберите пользователя"

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Выбери понравившийся товар и нажми кнопку Добавить когда определишься." \
                            "Когда закончишь покупки нажми Готово </i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 В корзине сейчас такие товары:\n" \
                            "{product_list}" \
                            "Всего: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Если хочешь купить уже, мой азартный друг, нажимай кнопку Готово.</i>\n"

# Conversation: the user activated the live orders mode
conversation_live_orders_start = "Ты в режиме <b>живых заказов!</b>\n" \
                                 "Заказы, которые оформили пользователи, появятся прям вот тут" \
                                 "и можно их обозначить ✅ выполненными." \
                                 "или ✴️ выдать пзшку.\n" \
                                 "\n" \
                                 "<i>нажми Стопэ чтобы перестать получать обновления и выйти отсюдова нахуй</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "Привет. Я доброжелательный помощник. Шо надо, животное?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "Повысить этого еблана до 💼 админа?\n" \
                                       "откатить нельзя!"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " Ты переключаешься в режим 👤 покупателя.\n" \
                                   "пиши /start чтобы вернуться в админку"

# Notification: the conversation has expired
conversation_expired = "🕐  Ты слишком долго не писал.. Надеюсь, ты не начал ходить в качалку и перестать юзать пхпх)\n"

# User menu: order
menu_order = "🛒 В магизн"

# User menu: order status
menu_order_status = "🛍 Мои заказы"

# User menu: add credit
menu_add_credit = "💵 Пополнить счет"

# User menu: bot info
menu_bot_info = "ℹ️ Инфо бота"

# User menu: cash
menu_cash = "💵 Деньги"

# User menu: credit card
menu_credit_card = "💳 Карта"

# Admin menu: products
menu_products = "📝️ Управление товаром"

# Admin menu: orders
menu_orders = "📦 Заказы"

# Menu: transactions
menu_transactions = "💳 Выданные клады"

# Menu: edit credit
menu_edit_credit = "💰 Создать транзакцию"

# Admin menu: go to user mode
menu_user_mode = "👤 Жамкни для перехода в режим покупателя"

# Admin menu: add product
menu_add_product = "✨ Добавить товар"

# Admin menu: delete product
menu_delete_product = "❌ Удалить товар"

# Menu: cancel
menu_cancel = "🔙 отмена"

# Menu: skip
menu_skip = "⏭ давай дальше"

# Menu: done
menu_done = "✅️ Готово"

# Menu: pay invoice
menu_pay = "💳 Оплата"

# Menu: complete
menu_complete = "✅ Завершена"

# Menu: refund
menu_refund = "✴️ Возврат"

# Menu: stop
menu_stop = "🛑 Стопэ"

# Menu: add to cart
menu_add_to_cart = "➕ Добавить"

# Menu: remove from cart
menu_remove_from_cart = "➖ Удалить"

# Menu: help menu
menu_help = "❓ Помощь/поддержка"

# Menu: guide
menu_guide = "📖 Для тех кто в танке"

# Menu: next page
menu_next = "▶️ След"

# Menu: previous page
menu_previous = "◀️ Пред"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Написать боссу"

# Menu: generate transactions .csv file
menu_csv = "📄.csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Редактировать админов"

# Emoji: unprocessed order
emoji_not_processed = "*️⃣"

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Emoji: yes
emoji_yes = "✅"

# Emoji: no
emoji_no = "🚫"

# Text: unprocessed order
text_not_processed = "ожидает"

# Text: completed order
text_completed = "завершен"

# Text: refunded order
text_refunded = "выдан пз"

# cat
ask_product_cat = "Категория товара?"

# Add product: name?
ask_product_name = "как называется товар?"

# product amount
ask_product_amount = "Количество? (шт для колес, г для остального"

# product coords
ask_product_coords = "Координаты в формате xx.xxxxxx yy.yyyyyy"

# Add product: description?
ask_product_description = "описание товара?"

# Add product: price?
ask_product_price = "Цена?\n" \
                    "Пиши <code>X</code> если хочешь пока не выставлять на продажу"

# Add product: image?
ask_product_image = "🖼 Загрузи пикчу для товара. Если не надо жми дальше\n"

# Order product: notes?
ask_order_notes = " Желаете оставить комментарий к заказу?\n" \
                  "💼 Админы его прочитают, но не факт что будет не пох\n"

# Refund product: reason?
ask_refund_reason = " Объясни за пз\n" \
                    "👤  это увидит покупатель."

# Edit credit: notes?
ask_transaction_notes = " Добавить комент к транзакции.\n" \
                        "👤 после оплаты это увидят покупатель и админы в журнале операций"

# Edit credit: amount?
ask_credit = "Как хочешь изменить его/ее баланс?\n" \
             "\n" \
             "<i>Отправь количество, например, +200 или -100.</i>" \
 \
    # Header for the edit admin message
admin_properties = "<b>Разрешения для {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Редактировать товары"

# Edit admin: can receive orders?
prop_receive_orders = "Получать заказы"

# Edit admin: can create transactions?
prop_create_transactions = "Управление транзакциями"

# Edit admin: show on help message?
prop_display_on_help = "Поддержка покупателя"

# Thread has started downloading an image and might be unresponsive
downloading_image = "Скачиваю твою фотку\n" \
                    "погодь маленько\n"

# Edit product: current value
edit_current_value = "The current value is:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Press the jump button below this message to keep the same value.</i>"

# Payment: cash payment info
payment_cash = "You can pay cash at the physical location of the store.\n" \
               "Pay at checkout, and provide the store admin with this id:\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "На сколько пополняешь счет?\n" \
                    "\n" \
                    "<i>выбери кнопками или напиши цифру</i>"

# Payment: add funds invoice title
payment_invoice_title = "Добавить мани"

# Payment: add funds invoice description
payment_invoice_description = "Оплата по этому чеку закинет {amount} на твой кошелек."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Перезагрузка"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "комиссия"

# Notification: order has been placed
notification_order_placed = "Новый заказ:\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Ваш заказ завершен!\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Вам пзшечка!\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  Новая транзакция по вашему счету:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Поясни с чего нам выдавать пз:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = ' <i>где-то тут шастает еж...</i>' \
 \
    # Help: guide
help_msg = "Помощь по боту доступна по адресу:\n" \
           "https://пшелнах"

# Help: contact shopkeeper
contact_shopkeeper = "люди которые могут тебе ответить касательно магазина - \n" \
                     "{shopkeepers}\n" \
                     "<i>писать в адекватное время суток и желательно по делу, " \
                     "и тогда твой вопрос решится быстро, качественно и приятно.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ Товар добавлен/изменен!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ Товар удален!"

# Success: order has been created
success_order_created = "✅ Заказ был успешно отправлен.\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ ты обозначил #{order_id} как завершенный"

# Success: order was refunded successfully
success_order_refunded = "✴️ По заказу #{order_id} выдан пз."

# Success: transaction was created successfully
success_transaction_created = "✅ Транзакция была создана!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Этот бот работает только в приватных чатах."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ Меня перезапустили и я слегка ебанулся.\n" \
                           "Чтобы продолжить свои делишки снова напишите /start, пожалуйста."

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ максимум за одну транзакцию " \
                                "{max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ Минимум за транзакцию " \
                                 "{min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ все, просрал время на операцию "
# Error: a product with that name already exists
error_duplicate_name = "️⚠️ товар с таким именем уже существует!"

# Error: not enough credit to order
error_not_enough_credit = "⚠️ бро пополни счет, не хватает"

# Error: order has already been cleared
error_order_already_cleared = "⚠️  Этот заказ уже в обработке."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  нет заказов, показывать нечего."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  выбранного пользователя не существует!"

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Бляя<b>яяяяя</b>яяядь! Случилось недоразумение. " \
                               "Я уже сказал своему создателю, спокуха в общем, все починят, но позже.\n" \
                               "хз когда"

# shit holy shit
menu_extra = "гостинець від їжачка"

# payment method
payment_easy = "EasyPay"

# weed
cat_weed = "Weed"
cat_white = "Стимуляторы"
cat_wheels = "Таблы"

amount_quarter = "0.25"
amount_half = "0.5"
amount_one = "1"
amount_two = "2"
