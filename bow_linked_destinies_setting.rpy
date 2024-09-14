
init:
    $ path_dir = "mods/bow_linked_destinies/"

    $ bld_cold_wind_home = path_dir + "sounds/ambiences/cold_wind_home.ogg"

    $ bld_lena_screech = path_dir + "sounds/sfx/bld_lena_screech.ogg"

    # Фоны
    image bg bld_ext_storage_sunset = path_dir + "images/bg/ext_storage_sunset.jpg"
    image bg bld_int_dining_hall_people_sunset = path_dir + "images/bg/int_dining_hall_people_sunset.jpg"
    image bg bld_int_warehouse_sunset = path_dir + "images/bg/int_warehouse_sunset.jpg"

    # Изображения
    image cg bld_d1_food = path_dir + "images/cg/d1_food.jpg"
    image cg bld_d1_grasshopper = path_dir + "images/cg/d1_grasshopper.jpg"
    image cg bld_library_zhenya_asleep = path_dir + "images/cg/library_zhenya_asleep.jpg"
    image cg bld_me_mirror = path_dir + "images/cg/me_mirror.jpg"

    # Отображение музыки
    image bld_ap_music_text_panel = path_dir + "images/gui/music_text_panel.png"
    image bld_ap_music_vinyl_record = path_dir + "images/gui/vinyl_disk.png"

    image bld_chair = path_dir + "images/chair.png"

    transform bld_sit_left:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0
        ypos 0.22

    transform bld_sit_center:
        xalign 0.5
        yanchor 0.0
        ypos 0.22

    transform bld_sit_right:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0
        ypos 0.22

    transform bld_walkinggg:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 30 zoom 3 anchor (1920,1800)
        parallel:
            ease 0.35 pos (0, 0)
            ease 0.35 pos (25,25)
            ease 0.35 pos (0, 0)
            ease 0.35 pos (-25,25)
            repeat

    transform bld_car: 
        parallel:
            xalign 0.5 yalign 0.5
        parallel:
            linear 0.1 pos(0.501,0.501)
            linear 0.1 pos(0.5,0.5)
            linear 0.1 pos(0.501,0.501)
            linear 0.1 pos(0.5,0.501)
            linear 0.1 pos(0.501,0.5)
            linear 0.1 pos(0.5,0.5)
            repeat

    transform bld_tremors:
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,5)
        linear 0.1 pos (0,5)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        repeat
