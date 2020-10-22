# coding: utf-8

# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.pet_api import PetApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from epiccore.api.billing_api import BillingApi
from epiccore.api.catalog_api import CatalogApi
from epiccore.api.data_api import DataApi
from epiccore.api.desktop_api import DesktopApi
from epiccore.api.job_api import JobApi
from epiccore.api.jobauth_api import JobauthApi
from epiccore.api.licenses_api import LicensesApi
from epiccore.api.profile_api import ProfileApi
from epiccore.api.projects_api import ProjectsApi
from epiccore.api.teams_api import TeamsApi
from epiccore.api.viz_api import VizApi
