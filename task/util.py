


def make_template(template, task, solution,topic):
    replacements = {
        "<задание>": task,
        "<решение>":  solution,
        "<тема>":topic
    }

    for tag, replacement in replacements.items():
        template = template.replace(tag, replacement)

    return template







