from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        for i in footer_buttons:
            menu.append([i])
    return menu


def start_markup():
    button_list = [
        InlineKeyboardButton("Получить бесплатный Чизбургер де Люкс!", callback_data='ask_one')
    ]
    return InlineKeyboardMarkup(build_menu(button_list, 1))


def yes_no(next_step):
    button_list = [
        InlineKeyboardButton("ДА", callback_data=next_step),
        InlineKeyboardButton("НЕТ", callback_data=next_step)
    ]
    return InlineKeyboardMarkup(build_menu(button_list, 2))


def submit(status):
    button_list = [
        InlineKeyboardButton("ПОДТВЕРДИТЬ!", callback_data=status),
    ]

    return InlineKeyboardMarkup(build_menu(button_list, 1))
