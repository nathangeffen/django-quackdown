from django.conf import settings


USER_CLAIM_FILES_FOLDER = getattr(settings, 'QUACKDOWN_USER_CLAIM_FILES_FOLDER', 
                                  'userclaimfiles')