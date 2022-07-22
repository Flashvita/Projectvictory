from .models import Category


def all_childrens(parent, children_list = {}):
    """ Определяем всех потомков и ложим их в children_list"""
    childrens = Category.objects.filter(parent=parent.pk)   
    d = {
        'id': parent.id,
        'title': parent.title,
        'level': parent.level,
        'slug': parent.slug,
        'road': parent.road,
        'children': []
    }
    if not childrens:
        children_list = d
        return d
    else:
        for children in childrens:
            kind = all_childrens(children, d['children'])
            d['children'].append(kind)
        children_list = d
        children_list
    return children_list


def category_tree(children_list = []):
    """ Формируем дерево категорий с потомками добавляя из  children_list """
    children_list.clear()
    for item in Category.objects.filter(parent=None):
        children_list.append(all_childrens(item))
    return children_list
