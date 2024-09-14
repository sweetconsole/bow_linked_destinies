

screen bld_music_screen_notifier(group, name, text_style="default", text_size=None):
    modal False

    $ text_size = text_size if text_size is not None else renpy.style.styles[(text_style, )].size

    fixed:
        xoffset 40
        yoffset 40
        frame:
            xanchor 0.0
            yanchor 0.5
            ypos 46
            left_padding 100
            right_padding 15
            xminimum 90
            background Frame("bld_ap_music_text_panel", left=44, top=15)

            vbox:
                spacing 5
                text group style text_style size text_size font path_dir + "fonts/old_soviet.otf"
                text name style text_style size text_size font path_dir + "fonts/old_soviet.otf"

                at transform:
                    xpos -30 ypos 0 alpha 0.0
                    pause 0.25
                    ease 0.75 xpos 0 alpha 1.0
                    pause 3.0
                    ease 1.25 xpos -30 alpha 0.0 
                
            
        add "bld_ap_music_vinyl_record":
            at transform:
                xanchor 0.5 yanchor 0.5 xpos 30 ypos 46 rotate 720.0 subpixel True
                ease 4.0 rotate 0.0
                ease 2.0 rotate 720.0

        at transform:
            xpos -0.05 alpha 0.0 subpixel True
            ease 1.0 xpos 0.0 alpha 1.0
            pause 3.0
            ease 2.0 xpos -0.1 alpha 0.0

    timer 6.01 action Hide("bld_music_screen_notifier")