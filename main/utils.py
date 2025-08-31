from datetime import datetime

def user_Listing_attr(instance, filename):
    """
    This function returns the upload path for a file based on the user and current date.
    e.g., 'user_uploads/user_3/2025-06-16/myimage.png'
    """
    today = datetime.today().strftime('%Y-%m-%d')
    return f'user_uploads/main_{instance.seller.user.id}/{today}/{filename}'
