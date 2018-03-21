simple_rows = [['Bondage', ['Rope',
                            'Cuffs',
                            'Sleepsack']]]
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
    content = f'          <div id="{group}">\n'
    content += f'            <input class="{group}1" name="{group}" value="1" type="radio">\n'
    content += f'            <label for="{group}1">Haven\'t done</label>\n'
    content += f'            <input class="{group}2" name="{group}" value="2" type="radio">\n'
    content += f'            <label for="{group}2">Tried it</label>\n'
    content += f'            <input class="{group}3" name="{group}" value="3" type="radio">\n'
    content += f'            <label for="{group}3">Done a little</label>\n'
    content += f'            <input class="{group}4" name="{group}" value="4" type="radio">\n'
    content += f'            <label for="{group}4">Done a lot</label>\n'
    content += '          </div>\n'
    return content


def activity_div(group):
    content = f'          <div id="{group}">\n'
    content += f'            <input class="{group}1" name="{group}" value="1" type="radio">\n'
    content += f'            <label for="{group}1">Limit</label>\n'
    content += f'            <input class="{group}2" name="{group}" value="2" type="radio">\n'
    content += f'            <label for="{group}2">Really dislike</label>\n'
    content += f'            <input class="{group}3" name="{group}" value="3" type="radio">\n'
    content += f'            <label for="{group}3">Dislike</label>\n'
    content += f'            <input class="{group}4" name="{group}" value="4" type="radio">\n'
    content += f'            <label for="{group}4">Like</label>\n'
    content += f'            <input class="{group}5" name="{group}" value="5" type="radio">\n'
    content += f'            <label for="{group}5">Really like</label>\n'
    content += f'            <input class="{group}6" name="{group}" value="6" type="radio">\n'
    content += f'            <label for="{group}6">Love</label>\n'
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
        content += '    <tbody class="topic_group">\n'
        content += '      <tr class="topic">\n'
        content += f'      <td colspan="2">{topic[0]}</td>\n'
        content += '      </tr>\n'
        for activity in topic[1]:
            content += '      <tr class="activity">\n'
            content += '        <td colspan="2">\n'
            content += f'          {activity}\n'
            content += '        </td>'
            content += '      </tr>'
            content += '      <tr>\n'
            content += '        <td>\n'
            content += experience_div(f'c1e{counter}')
            content += activity_div(f'c1a{counter}')
            content += '        </td>\n'
            content += '        <td>\n'
            content += experience_div(f'c2e{counter}')
            content += activity_div(f'c2a{counter}')    
            content += '        </td>\n'
            content += '      </tr>\n'
            content += '    </tbody>\n'
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
