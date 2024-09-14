init 5 python:
    
    def bld_show_music_notifier(group=None, name=None, text_style="default", text_size=None):
        song_data = { }

        song_data["group"] = group if group is not None else "Неизвестно"
        song_data["name"] = name if name is not None else "Неизвестно"
        song_data["text_style"] = text_style
        song_data["text_size"] = text_size if text_size is not None else renpy.style.styles[(text_style, )].size

        renpy.show_screen(_screen_name="bld_music_screen_notifier", **song_data)

