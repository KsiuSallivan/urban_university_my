def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': type(obj).__module__
    }

    # Дополнительная информация в зависимости от типа объекта
    if isinstance(obj, (int, float, complex)):
        info['real'] = obj.real
        info['imag'] = obj.imag
    elif isinstance(obj, str):
        info['length'] = len(obj)
    elif hasattr(obj, '__len__'):
        info['length'] = len(obj)

    return info


# test
number_info = introspection_info(42)
print(number_info)