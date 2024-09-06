def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function() # выдаст:
                # Я в области видимости функции test_function
                # Process finished with exit code 0

# inner_function() - выдаст:
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?