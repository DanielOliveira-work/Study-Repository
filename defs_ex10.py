def report_card(info, name):
    """
    :info - student information. 
    """
    bigger = max(info.values()) 
    minor = min(info.values())
    average = (bigger + minor) / len(info)
    if average > 7:
        end_course = 'APROVADO'
    elif 5 < average < 7:
        end_course = 'RECUPERAÇÃO'
    else:
        end_course = 'REPROVADO'
    print(f'The {name} > Test quantities: {len(info)}, highest grade: {bigger}, lowest grade: {minor}, average: {average:.1f} \n{end_course}')
