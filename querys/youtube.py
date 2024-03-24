import pywhatkit

def queryYoutube(video):
    try:
        pywhatkit.playonyt(video)
        return f"here is {video}"
    except Exception as e:
        return "An error occurred:", str(e)

