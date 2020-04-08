# Level 1 Problems' solution

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "name is too short!"

print(old_macdonald('macdonald'))


def master_yoda(text):
    return ' '.join(text.split()[::-1])

print(master_yoda('We are ready'))