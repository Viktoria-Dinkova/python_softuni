# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received in the input.
# Print the result on the console. For more clarification, see the examples below.
def loading_bar(percent_complite: int) -> list:
    ''''
    function that returns a loading bar depending on the received integer
        :param percent_complite - int

        :return bar_image - str
    '''
    percent = ['%'] * int(percent_complite / 10)
    dots = ['.'] * int(10 - (percent_complite / 10))
    bar_image = percent + dots
    output_image = "".join(bar_image)

    if percent_complite < 100:
        print(f'{str(percent_complite)}% [{output_image}]\nStill loading...')
    else:
        print(f'{str(percent_complite)}% Complete!\n[{output_image}]')

percent_of_loading = int(input())
loading_bar(percent_of_loading)