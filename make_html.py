simple_rows = [['Bondage', ['Bondage',
                            'Collars',
                            'Gags',
                            'Hoods',
                            'Handcuffs',
                            'Hog tie',
                            'Mummification',
                            'Sleepsack',
                            'Suspension',
                            'Cages',
                            'Sensory deprivation']],
                ['Dom / sub', ['Protocol',
                               'Humiliation',
                               'Small penis humiliation',
                               'Symbolic collar',
                               'Forced nudity',
                               'Chastity (shorter than a month)',
                               'Chastity (longer than a month)',
                               'Objectification',
                               'Inspections',
                               'Swallowing own come',
                               'Swallowing others’ come',
                               'Tickling',
                               'Armpit worship',
                               'Foot worship',
                               'Shaving',
                               'Cross dressing',
                               'Wrestling',
                               'Hypnosis',
                               'Bathroom control',
                               'Piss play',
                               'Scat',
                               '24/7',
                               'Contracts',
                               'Voyeurism',
                               'Exhibitionism']],
                ['S & M', ['Corporal punishment',
                           'Light pain',
                           'Heavy pain',
                           'Face slapping',
                           'Spanking',
                           'Nipple play',
                           'Nipple clamps',
                           'Clothespins',
                           'Caning',
                           'Flogging',
                           'E-stim',
                           'Hot wax',
                           'Hair pulling',
                           'CBT',
                           'Ball stretching',
                           'Breath play']],
                ['Role play / scenes', ['Public',
                                        'Medical play',
                                        'Pet play',
                                        'Age play',
                                        'Fantasy rape',
                                        'Rituals',
                                        'Interrogation',
                                        'Kidnapping',
                                        'Recording video or photography']],
                 ['Sexual', ['Kissing',
                             'Cuddling',
                             'Blow job (giving)',
                             'Blow job (receiving)',
                             'Cunnilingus (giving)',
                             'Cunnilingus (receiving)',
                             'Rimming (giving)',
                             'Rimming (receiving)',
                             'Butt plug',
                             'Anal sex (top)',
                             'Anal sex (bottom)',
                             'Pegging (top)',
                             'Pegging (bottom)',
                             'Vaginal sex (giving)',
                             'Vaginal sex (receiving)',
                             'Dildos',
                             'Vibrators',
                             'Fingering',
                             'Fisting',
                             'Anal orgasms',
                             'Prostage milking',
                             'Orgasm control / denial',
                             'Edging',
                             'Frottage',
                             'Phone sex / sexting / cyber']],
                 ['Fetish', ['Leather',
                             'Rubber / latex',
                             'Neoprene',
                             'Lycra',
                             'Uniforms',
                             'Socks',
                             'Feet',
                             'Furry']]]

                 
full_rows = [['Bondage', ['Rope',
                          'Cuffs',
                          'Gags',
                          'Mummification',
                          'Sleepsack',
                          'Suspension',
                          'Hoods',
                          'Collar',
                          'Extended periods of bondage'
                          'Hog tie']],
             ['Sex', ['Oral (giving)',
                      'Oral (receiving)',
                      'Anal sex (top)',
                      'Anal sex (bottom)',
                      'Rimming (giving)',
                      'Rimming (receiving)']]]


def experience_div(group):
    content = f'          <div id="{group}" class="experience radio_slider">\n'
    content += f'            <input id="{group}1" name="{group}" value="1" type="radio">\n'
    content += f'            <label for="{group}1" class="experience1">Haven\'t done</label>\n'
    content += f'            <input id="{group}2" name="{group}" value="2" type="radio">\n'
    content += f'            <label for="{group}2" class="experience2">Tried it</label>\n'
    content += f'            <input id="{group}3" name="{group}" value="3" type="radio">\n'
    content += f'            <label for="{group}3" class="experience3">Done a little</label>\n'
    content += f'            <input id="{group}4" name="{group}" value="4" type="radio">\n'
    content += f'            <label for="{group}4" class="experience4">Done a lot</label>\n'
    content += '          </div>\n'
    return content


def interest_div(group):
    content = f'          <div id="{group}" class="interest radio_slider">\n'
    content += f'            <input id="{group}1" name="{group}" value="1" type="radio">\n'
    content += f'            <label for="{group}1" class="interest1">Limit</label>\n'
    content += f'            <input id="{group}2" name="{group}" value="2" type="radio">\n'
    content += f'            <label for="{group}2" class="interest2">Dislike</label>\n'
    content += f'            <input id="{group}3" name="{group}" value="3" type="radio">\n'
    content += f'            <label for="{group}3" class="interest3">Will do</label>\n'
    content += f'            <input id="{group}4" name="{group}" value="4" type="radio">\n'
    content += f'            <label for="{group}4" class="interest4">Like</label>\n'
    content += f'            <input id="{group}5" name="{group}" value="5" type="radio">\n'
    content += f'            <label for="{group}5" class="interest5">Love</label>\n'
    content += f'            <input id="{group}6" name="{group}" value="6" type="radio">\n'
    content += f'            <label for="{group}6" class="interest6">Favorite</label>\n'
    content += '          </div>\n'
    return content


def fill_rows(name):
    counter = 0
    content = ''
    if name == 'simple':
        rows = simple_rows
    elif name == 'full':
        rows = full_rows
    for topic in rows:
        content += f'      <div class="topic">{topic[0]}</div>\n'
        for activity in topic[1]:
            alt = ' alt' if counter % 2 else ''
            content += f'      <div class="activity{alt}">\n'
            content += '        <div class="cell dom_cell" data-role="Dom">\n'
            content += experience_div(f'c1e{counter}')
            content += interest_div(f'c1a{counter}')
            content += '        </div>\n'
            content += f'        <div class="act_name">{activity}</div>\n'
            content += '        <div class="cell sub_cell" data-role="Sub">\n'
            content += experience_div(f'c2e{counter}')
            content += interest_div(f'c2a{counter}')
            content += '        </div>\n'
            content += '      </div>\n'
            counter += 1
    return content, counter


def main():
    for name in ['simple', 'full']:
        content = ''
        with open('templates/checklist.html', 'r') as file:
            content = file.read()
        replace_with, num_rows = fill_rows(name)
        content = content.replace('{{ checklist rows }}', replace_with)
        content = content.replace('{{ num_rows }}', str(num_rows))
        with open(f'build/{name}.html', 'w') as file:
            file.write(content)


if __name__ == '__main__':
    main()
