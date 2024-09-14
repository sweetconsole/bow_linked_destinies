
init 4:
    $ mods["bow_linked_destinies_start"] = u"Бантик связавший наши судьбы"

    $ config.developer = True
    $ config.console = True

    define iv = Character(u"Иван", color="#C70039", what_color="#f1d076")
    define lz = Character(u"Лиза", color="", what_color="#f1d076")

label bow_linked_destinies_start:
    jump bow_linked_destinies_prologue