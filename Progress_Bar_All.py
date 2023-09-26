import PySimpleGUI as sg

def create_progress_bar(max_value, website, theme):
    """
    The function `create_progress_bar` creates a progress bar window with a specified maximum value, website name, and
    theme.

    :param max_value: The `max_value` parameter represents the maximum value of the progress bar. It determines the range of
    values that the progress bar can display
    :param website: The website parameter is a string that represents the name or URL of the website that the progress bar
    is associated with
    :param theme: The "theme" parameter is used to specify the color theme of the progress bar window. It can be set to any
    valid theme name supported by the PySimpleGUI library, such as 'DarkBlue', 'DarkRed', 'DarkAmber', etc
    :return: a window object.
    """
    sg.theme('DarkBlue')
    layout = [
              # [sg.theme('DarkRed')],
              [sg.Text("loading..", key="progtext")],
              [sg.Text(website, key="website")],
              [sg.ProgressBar(max_value= max_value, orientation='h', size=(50, 20), key='progressbar')],
              [sg.Button('Cancel')]]

    window = sg.Window(website, layout, finalize=True)
    # Percent = window['progtext']
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
    return window

def update_progress_bar(window, value, max_value, time, P_list, website, website_order):
    """
    The function `update_progress_bar` updates the progress bar, website name, and progress text in a window, based on the
    current value, maximum value, time, and other parameters.

    :param window: The "window" parameter is the GUI window object where the progress bar and other elements are displayed
    :param value: The current value of the progress bar (the number of items scraped so far)
    :param max_value: The maximum value of the progress bar, representing the total number of items to be scraped
    :param time: The `time` parameter is a variable that represents the time taken for the scraping process. It is passed to
    the `time_convert` function to convert it into a more readable format
    :param P_list: P_list is a list of Hersteller Teilenummer (manufacturer part numbers)
    :param website: The `website` parameter is a string that represents the name or URL of the website being scraped
    :param website_order: The parameter `website_order` represents the order in which the websites are being scraped. It is
    used to calculate the progress of the scraping process
    """
    smiley = [u'\U0001F604', u'\U0001F605', u'\U0001F607', u'\U0001F60E', u'\U0001F60A']  # Unicode code point for smiley face

    Hersteller_Teilenummer = P_list[value-1]
    scraped_to = int(website_order) - 1
    window['progressbar'].update_bar(value+(max_value*scraped_to))
    time = time_convert(time)
    window['website'].update(website)
    window['progtext'].update('\nScraping Hersteller Teilenummer \"'+str(Hersteller_Teilenummer)+'\" ./.'+str(smiley[3])+
    '\n'+str(value)+' out of '+str(max_value)+' scraped....'+'\n\n'+str(time))
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()

def time_convert(time):
    """
    The function `time_convert` takes a time in seconds as input and converts it into hours, minutes, and seconds, then
    returns a formatted string representing the time lapsed.

    :param time: The parameter "time" represents the number of seconds that have elapsed
    :return: a string that represents the time lapsed in hours, minutes, and seconds.
    """
    sec = time
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed : {0} Hour: {1} Minute : {2} Second ".format(int(hours), int(mins), int(sec)))
    if int(mins) <=1 and int(hours) <=1:
        StopWatch = "Time Lapsed : {0} Hour: {1} Minute : {2} Seconds ".format(int(hours), int(mins), int(sec))
    elif int(mins) >1 and int(hours) <=1:
        StopWatch = "Time Lapsed : {0} Hour: {1} Minutes : {2} Seconds ".format(int(hours), int(mins), int(sec))
    elif int(hours) >1 and int(mins) <= 1:
        StopWatch = "Time Lapsed : {0} Hours: {1} Minute : {2} Seconds ".format(int(hours), int(mins), int(sec))
    elif int(hours) >1 and int(mins) >1:
        StopWatch = "Time Lapsed : {0} Hours: {1} Minutes : {2} Seconds ".format(int(hours), int(mins), int(sec))
    else:
        StopWatch = "Time Lapsed : {0} Hours: {1} Minutes : {2} Seconds ".format(int(hours), int(mins), int(sec))
    return StopWatch

def close_progress_bar(window):
    """
    The function `close_progress_bar` closes a window.

    :param window: The "window" parameter is the window object that represents the progress bar window
    """
    window.close()



