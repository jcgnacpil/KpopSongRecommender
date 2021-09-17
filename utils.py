# Library for accessing Spotify API
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

def repeatAPICall(func, args, max_retry = 5):
    """
    Repeatedly calls spotipy func until a successful API request is made.
    
    Parameters:
        func : func
            Spotipy client function for making api calls
        args: dict
            Arguments to pass to func; Key: parameter, Value: parameter value
            Check Spotipy API of specified func for details
        max_retry: int
            Maximum iterations before prompting user to retry or skip
        
    Returns:
        result: dict
            Result of a successful API call, or none
        success: bool
            True if API call is successful, False otherwise
    """

    success = False
    res = None
    
    i = 0
    while i < max_retry:
        try: 
            res = func(**args)
            success = True
            return res, success
        except:
            print("Error in API call; retrying")
            i += 1
            pass
        
        if i >= max_retry:
            reset_loop = input("Max retry limit reached. Retry {} more time/s?".format(max_retry)).upper()
            reset_loop = True if reset_loop == 'Y' else False
            
            # Reset the index of the loop if user chooses to reset
            i = 0 if reset_loop else max_retry
    return res, success